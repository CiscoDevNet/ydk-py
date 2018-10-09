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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class RoutingProtocol(Identity):
    """
    Base identity from which routing protocol identities are
    derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:routing-protocol"):
        super(RoutingProtocol, self).__init__(ns, pref, tag)


class RoutingInstance(Identity):
    """
    Base identity from which identities describing routing
    instance types are derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:routing-instance"):
        super(RoutingInstance, self).__init__(ns, pref, tag)


class AddressFamily(Identity):
    """
    Base identity from which identities describing address
    families are derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:address-family"):
        super(AddressFamily, self).__init__(ns, pref, tag)


class RoutingState(Entity):
    """
    State data of the routing subsystem.
    
    .. attribute:: routing_instance
    
    	Each list entry is a container for state data of a routing instance.  An implementation MUST support routing instance(s) of the type 'rt\:default\-routing\-instance', and MAY support other types. An implementation MAY restrict the number of routing instances of each supported type.  An implementation SHOULD create at least one system\-controlled instance, and MAY allow the clients to create user\-controlled routing instances in configuration
    	**type**\: list of  		 :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("routing-instance", ("routing_instance", RoutingState.RoutingInstance))])
        self._leafs = OrderedDict()

        self.routing_instance = YList(self)
        self._segment_path = lambda: "ietf-routing:routing-state"
        self._is_frozen = True

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
        
        .. attribute:: name  (key)
        
        	The name of the routing instance.  For system\-controlled instances the name is persistent, i.e., it SHOULD NOT change across reboots
        	**type**\: str
        
        .. attribute:: type
        
        	The routing instance type
        	**type**\:  :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.RoutingInstance>`
        
        .. attribute:: router_id
        
        	A 32\-bit number in the form of a dotted quad that is used by some routing protocols identifying a router
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
        
        .. attribute:: interfaces
        
        	Network layer interfaces belonging to the routing instance
        	**type**\:  :py:class:`Interfaces <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Interfaces>`
        
        .. attribute:: routing_protocols
        
        	Container for the list of routing protocol instances
        	**type**\:  :py:class:`RoutingProtocols <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols>`
        
        .. attribute:: ribs
        
        	Container for RIBs
        	**type**\:  :py:class:`Ribs <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(RoutingState.RoutingInstance, self).__init__()

            self.yang_name = "routing-instance"
            self.yang_parent_name = "routing-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("interfaces", ("interfaces", RoutingState.RoutingInstance.Interfaces)), ("routing-protocols", ("routing_protocols", RoutingState.RoutingInstance.RoutingProtocols)), ("ribs", ("ribs", RoutingState.RoutingInstance.Ribs))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.ietf.ietf_routing', 'RoutingInstance')])),
                ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
            ])
            self.name = None
            self.type = None
            self.router_id = None

            self.interfaces = RoutingState.RoutingInstance.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.routing_protocols = RoutingState.RoutingInstance.RoutingProtocols()
            self.routing_protocols.parent = self
            self._children_name_map["routing_protocols"] = "routing-protocols"

            self.ribs = RoutingState.RoutingInstance.Ribs()
            self.ribs.parent = self
            self._children_name_map["ribs"] = "ribs"
            self._segment_path = lambda: "routing-instance" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "ietf-routing:routing-state/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RoutingState.RoutingInstance, [u'name', u'type', u'router_id'], name, value)


        class Interfaces(Entity):
            """
            Network layer interfaces belonging to the routing
            instance.
            
            .. attribute:: interface
            
            	Each entry is a reference to the name of a configured network layer interface
            	**type**\: list of str
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface', (YLeafList(YType.str, 'interface'), ['str'])),
                ])
                self.interface = []
                self._segment_path = lambda: "interfaces"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingState.RoutingInstance.Interfaces, [u'interface'], name, value)


        class RoutingProtocols(Entity):
            """
            Container for the list of routing protocol instances.
            
            .. attribute:: routing_protocol
            
            	State data of a routing protocol instance.  An implementation MUST provide exactly one system\-controlled instance of the type 'direct'. Other instances MAY be created by configuration
            	**type**\: list of  		 :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(RoutingState.RoutingInstance.RoutingProtocols, self).__init__()

                self.yang_name = "routing-protocols"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("routing-protocol", ("routing_protocol", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol))])
                self._leafs = OrderedDict()

                self.routing_protocol = YList(self)
                self._segment_path = lambda: "routing-protocols"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols, [], name, value)


            class RoutingProtocol(Entity):
                """
                State data of a routing protocol instance.
                
                An implementation MUST provide exactly one
                system\-controlled instance of the type 'direct'. Other
                instances MAY be created by configuration.
                
                .. attribute:: type  (key)
                
                	Type of the routing protocol
                	**type**\:  :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
                
                .. attribute:: name  (key)
                
                	The name of the routing protocol instance.  For system\-controlled instances this name is persistent, i.e., it SHOULD NOT change across reboots
                	**type**\: str
                
                .. attribute:: ospf
                
                	OSPF
                	**type**\:  :py:class:`Ospf <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol, self).__init__()

                    self.yang_name = "routing-protocol"
                    self.yang_parent_name = "routing-protocols"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['type','name']
                    self._child_classes = OrderedDict([("ietf-ospf:ospf", ("ospf", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf))])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.ietf.ietf_routing', 'RoutingProtocol')])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.type = None
                    self.name = None

                    self.ospf = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf()
                    self.ospf.parent = self
                    self._children_name_map["ospf"] = "ietf-ospf:ospf"
                    self._segment_path = lambda: "routing-protocol" + "[type='" + str(self.type) + "']" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol, [u'type', u'name'], name, value)


                class Ospf(Entity):
                    """
                    OSPF
                    
                    .. attribute:: operation_mode
                    
                    	OSPF operation mode
                    	**type**\:  :py:class:`OperationMode <ydk.models.ietf.ietf_ospf.OperationMode>`
                    
                    .. attribute:: instance
                    
                    	An OSPF routing protocol instance
                    	**type**\: list of  		 :py:class:`Instance <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance>`
                    
                    

                    """

                    _prefix = 'ospf'
                    _revision = '2015-03-09'

                    def __init__(self):
                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, self).__init__()

                        self.yang_name = "ospf"
                        self.yang_parent_name = "routing-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("instance", ("instance", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance))])
                        self._leafs = OrderedDict([
                            ('operation_mode', (YLeaf(YType.identityref, 'operation-mode'), [('ydk.models.ietf.ietf_ospf', 'OperationMode')])),
                        ])
                        self.operation_mode = None

                        self.instance = YList(self)
                        self._segment_path = lambda: "ietf-ospf:ospf"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, ['operation_mode'], name, value)


                    class Instance(Entity):
                        """
                        An OSPF routing protocol instance.
                        
                        .. attribute:: af  (key)
                        
                        	Address\-family of the instance
                        	**type**\:  :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                        
                        .. attribute:: router_id
                        
                        	Defined in RFC 2328. A 32\-bit number that uniquely identifies the router
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                        
                        .. attribute:: area
                        
                        	List of OSPF areas
                        	**type**\: list of  		 :py:class:`Area <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area>`
                        
                        .. attribute:: as_scope_lsas
                        
                        	List OSPF AS scope LSA databases
                        	**type**\: list of  		 :py:class:`AsScopeLsas <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas>`
                        
                        .. attribute:: topology
                        
                        	OSPF topology
                        	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology>`
                        
                        

                        """

                        _prefix = 'ospf'
                        _revision = '2015-03-09'

                        def __init__(self):
                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, self).__init__()

                            self.yang_name = "instance"
                            self.yang_parent_name = "ospf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['af']
                            self._child_classes = OrderedDict([("area", ("area", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area)), ("as-scope-lsas", ("as_scope_lsas", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas)), ("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology))])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.identityref, 'af'), [('ydk.models.ietf.ietf_routing', 'AddressFamily')])),
                                ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                            ])
                            self.af = None
                            self.router_id = None

                            self.area = YList(self)
                            self.as_scope_lsas = YList(self)
                            self.topology = YList(self)
                            self._segment_path = lambda: "instance" + "[af='" + str(self.af) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, ['af', 'router_id'], name, value)


                        class Area(Entity):
                            """
                            List of OSPF areas
                            
                            .. attribute:: area_id  (key)
                            
                            	Area ID
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..4294967295
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                            
                            .. attribute:: interfaces
                            
                            	List of OSPF interfaces
                            	**type**\: list of  		 :py:class:`Interfaces <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces>`
                            
                            .. attribute:: area_scope_lsas
                            
                            	List OSPF area scope LSA databases
                            	**type**\: list of  		 :py:class:`AreaScopeLsas <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, self).__init__()

                                self.yang_name = "area"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['area_id']
                                self._child_classes = OrderedDict([("interfaces", ("interfaces", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces)), ("area-scope-lsas", ("area_scope_lsas", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas))])
                                self._leafs = OrderedDict([
                                    ('area_id', (YLeaf(YType.str, 'area-id'), ['int','str'])),
                                ])
                                self.area_id = None

                                self.interfaces = YList(self)
                                self.area_scope_lsas = YList(self)
                                self._segment_path = lambda: "area" + "[area-id='" + str(self.area_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, ['area_id'], name, value)


                            class Interfaces(Entity):
                                """
                                List of OSPF interfaces.
                                
                                .. attribute:: interface  (key)
                                
                                	Interface
                                	**type**\: str
                                
                                .. attribute:: network_type
                                
                                	Network type
                                	**type**\:  :py:class:`NetworkType <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.NetworkType>`
                                
                                .. attribute:: passive
                                
                                	Enable/Disable passive
                                	**type**\: bool
                                
                                .. attribute:: demand_circuit
                                
                                	Enable/Disable demand circuit
                                	**type**\: bool
                                
                                .. attribute:: multi_area
                                
                                	Configure ospf multi\-area
                                	**type**\:  :py:class:`MultiArea <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea>`
                                
                                .. attribute:: static_neighbors
                                
                                	Static configured neighbors
                                	**type**\:  :py:class:`StaticNeighbors <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors>`
                                
                                .. attribute:: node_flag
                                
                                	Set prefix as a node representative prefix
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: fast_reroute
                                
                                	Fast\-reroute configuration
                                	**type**\:  :py:class:`FastReroute <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute>`
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\: bool
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\: bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\: bool
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\: bool
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:  :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity>`
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\: bool
                                
                                	**default value**\: true
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:  :py:class:`Authentication <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication>`
                                
                                .. attribute:: state
                                
                                	Interface state
                                	**type**\: str
                                
                                .. attribute:: hello_timer
                                
                                	Hello timer
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: milliseconds
                                
                                .. attribute:: wait_timer
                                
                                	Wait timer
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: milliseconds
                                
                                .. attribute:: dr
                                
                                	DR
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: bdr
                                
                                	BDR
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: neighbor
                                
                                	List of OSPF neighbors
                                	**type**\: list of  		 :py:class:`Neighbor <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor>`
                                
                                .. attribute:: link_scope_lsas
                                
                                	List OSPF link scope LSA databases
                                	**type**\: list of  		 :py:class:`LinkScopeLsas <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas>`
                                
                                .. attribute:: topology
                                
                                	OSPF interface topology
                                	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces, self).__init__()

                                    self.yang_name = "interfaces"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface']
                                    self._child_classes = OrderedDict([("multi-area", ("multi_area", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea)), ("static-neighbors", ("static_neighbors", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors)), ("fast-reroute", ("fast_reroute", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute)), ("ttl-security", ("ttl_security", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity)), ("authentication", ("authentication", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication)), ("neighbor", ("neighbor", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor)), ("link-scope-lsas", ("link_scope_lsas", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas)), ("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology))])
                                    self._leafs = OrderedDict([
                                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                        ('network_type', (YLeaf(YType.enumeration, 'network-type'), [('ydk.models.ietf.ietf_routing', 'RoutingState', 'RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.NetworkType')])),
                                        ('passive', (YLeaf(YType.boolean, 'passive'), ['bool'])),
                                        ('demand_circuit', (YLeaf(YType.boolean, 'demand-circuit'), ['bool'])),
                                        ('node_flag', (YLeaf(YType.boolean, 'node-flag'), ['bool'])),
                                        ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                        ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                        ('dead_interval', (YLeaf(YType.uint16, 'dead-interval'), ['int'])),
                                        ('retransmit_interval', (YLeaf(YType.uint16, 'retransmit-interval'), ['int'])),
                                        ('transmit_delay', (YLeaf(YType.uint16, 'transmit-delay'), ['int'])),
                                        ('mtu_ignore', (YLeaf(YType.boolean, 'mtu-ignore'), ['bool'])),
                                        ('lls', (YLeaf(YType.boolean, 'lls'), ['bool'])),
                                        ('prefix_suppression', (YLeaf(YType.boolean, 'prefix-suppression'), ['bool'])),
                                        ('bfd', (YLeaf(YType.boolean, 'bfd'), ['bool'])),
                                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                        ('state', (YLeaf(YType.str, 'state'), ['str'])),
                                        ('hello_timer', (YLeaf(YType.uint32, 'hello-timer'), ['int'])),
                                        ('wait_timer', (YLeaf(YType.uint32, 'wait-timer'), ['int'])),
                                        ('dr', (YLeaf(YType.str, 'dr'), ['str'])),
                                        ('bdr', (YLeaf(YType.str, 'bdr'), ['str'])),
                                    ])
                                    self.interface = None
                                    self.network_type = None
                                    self.passive = None
                                    self.demand_circuit = None
                                    self.node_flag = None
                                    self.cost = None
                                    self.hello_interval = None
                                    self.dead_interval = None
                                    self.retransmit_interval = None
                                    self.transmit_delay = None
                                    self.mtu_ignore = None
                                    self.lls = None
                                    self.prefix_suppression = None
                                    self.bfd = None
                                    self.enable = None
                                    self.state = None
                                    self.hello_timer = None
                                    self.wait_timer = None
                                    self.dr = None
                                    self.bdr = None

                                    self.multi_area = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea()
                                    self.multi_area.parent = self
                                    self._children_name_map["multi_area"] = "multi-area"

                                    self.static_neighbors = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors()
                                    self.static_neighbors.parent = self
                                    self._children_name_map["static_neighbors"] = "static-neighbors"

                                    self.fast_reroute = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute()
                                    self.fast_reroute.parent = self
                                    self._children_name_map["fast_reroute"] = "fast-reroute"

                                    self.ttl_security = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"

                                    self.authentication = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"

                                    self.neighbor = YList(self)
                                    self.link_scope_lsas = YList(self)
                                    self.topology = YList(self)
                                    self._segment_path = lambda: "interfaces" + "[interface='" + str(self.interface) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces, ['interface', 'network_type', 'passive', 'demand_circuit', 'node_flag', 'cost', 'hello_interval', 'dead_interval', 'retransmit_interval', 'transmit_delay', 'mtu_ignore', 'lls', 'prefix_suppression', 'bfd', 'enable', 'state', 'hello_timer', 'wait_timer', 'dr', 'bdr'], name, value)

                                class NetworkType(Enum):
                                    """
                                    NetworkType (Enum Class)

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



                                class MultiArea(Entity):
                                    """
                                    Configure ospf multi\-area.
                                    
                                    .. attribute:: multi_area_id
                                    
                                    	Multi\-area ID
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: int
                                    
                                    			**range:** 0..4294967295
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                    
                                    .. attribute:: cost
                                    
                                    	Interface cost for multi\-area
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea, self).__init__()

                                        self.yang_name = "multi-area"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('multi_area_id', (YLeaf(YType.str, 'multi-area-id'), ['int','str'])),
                                            ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                        ])
                                        self.multi_area_id = None
                                        self.cost = None
                                        self._segment_path = lambda: "multi-area"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea, ['multi_area_id', 'cost'], name, value)


                                class StaticNeighbors(Entity):
                                    """
                                    Static configured neighbors.
                                    
                                    .. attribute:: neighbor
                                    
                                    	Specify a neighbor router
                                    	**type**\: list of  		 :py:class:`Neighbor <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors, self).__init__()

                                        self.yang_name = "static-neighbors"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("neighbor", ("neighbor", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor))])
                                        self._leafs = OrderedDict()

                                        self.neighbor = YList(self)
                                        self._segment_path = lambda: "static-neighbors"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors, [], name, value)


                                    class Neighbor(Entity):
                                        """
                                        Specify a neighbor router.
                                        
                                        .. attribute:: address  (key)
                                        
                                        	Neighbor IP address
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cost
                                        
                                        	Neighbor cost
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: poll_interval
                                        
                                        	Neighbor poll interval
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        	**units**\: seconds
                                        
                                        .. attribute:: priority
                                        
                                        	Neighbor priority for DR election
                                        	**type**\: int
                                        
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
                                            self.ylist_key_names = ['address']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                                ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                                ('poll_interval', (YLeaf(YType.uint16, 'poll-interval'), ['int'])),
                                                ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                                            ])
                                            self.address = None
                                            self.cost = None
                                            self.poll_interval = None
                                            self.priority = None
                                            self._segment_path = lambda: "neighbor" + "[address='" + str(self.address) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor, ['address', 'cost', 'poll_interval', 'priority'], name, value)


                                class FastReroute(Entity):
                                    """
                                    Fast\-reroute configuration.
                                    
                                    .. attribute:: lfa
                                    
                                    	LFA configuration
                                    	**type**\:  :py:class:`Lfa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute, self).__init__()

                                        self.yang_name = "fast-reroute"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lfa", ("lfa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa))])
                                        self._leafs = OrderedDict()

                                        self.lfa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa()
                                        self.lfa.parent = self
                                        self._children_name_map["lfa"] = "lfa"
                                        self._segment_path = lambda: "fast-reroute"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute, [], name, value)


                                    class Lfa(Entity):
                                        """
                                        LFA configuration.
                                        
                                        .. attribute:: candidate_disabled
                                        
                                        	Prevent the interface to be used as backup
                                        	**type**\: bool
                                        
                                        .. attribute:: enabled
                                        
                                        	Activates LFA. This model assumes activation of per\-prefix LFA
                                        	**type**\: bool
                                        
                                        .. attribute:: remote_lfa
                                        
                                        	Remote LFA configuration
                                        	**type**\:  :py:class:`RemoteLfa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa, self).__init__()

                                            self.yang_name = "lfa"
                                            self.yang_parent_name = "fast-reroute"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("remote-lfa", ("remote_lfa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa))])
                                            self._leafs = OrderedDict([
                                                ('candidate_disabled', (YLeaf(YType.boolean, 'candidate-disabled'), ['bool'])),
                                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                            ])
                                            self.candidate_disabled = None
                                            self.enabled = None

                                            self.remote_lfa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa()
                                            self.remote_lfa.parent = self
                                            self._children_name_map["remote_lfa"] = "remote-lfa"
                                            self._segment_path = lambda: "lfa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa, ['candidate_disabled', 'enabled'], name, value)


                                        class RemoteLfa(Entity):
                                            """
                                            Remote LFA configuration.
                                            
                                            .. attribute:: enabled
                                            
                                            	Activates remote LFA
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa, self).__init__()

                                                self.yang_name = "remote-lfa"
                                                self.yang_parent_name = "lfa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                                ])
                                                self.enabled = None
                                                self._segment_path = lambda: "remote-lfa"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa, ['enabled'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\: bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('hops', (YLeaf(YType.uint8, 'hops'), ['int'])),
                                        ])
                                        self.enable = None
                                        self.hops = None
                                        self._segment_path = lambda: "ttl-security"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity, ['enable', 'hops'], name, value)


                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\: str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\: str
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:  :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("crypto-algorithm", ("crypto_algorithm", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm))])
                                        self._leafs = OrderedDict([
                                            ('sa', (YLeaf(YType.str, 'sa'), ['str'])),
                                            ('key_chain', (YLeaf(YType.str, 'key-chain'), ['str'])),
                                            ('key', (YLeaf(YType.str, 'key'), ['str'])),
                                        ])
                                        self.sa = None
                                        self.key_chain = None
                                        self.key = None

                                        self.crypto_algorithm = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._segment_path = lambda: "authentication"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication, ['sa', 'key_chain', 'key'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('hmac_sha1_12', (YLeaf(YType.empty, 'hmac-sha1-12'), ['Empty'])),
                                                ('hmac_sha1_20', (YLeaf(YType.empty, 'hmac-sha1-20'), ['Empty'])),
                                                ('md5', (YLeaf(YType.empty, 'md5'), ['Empty'])),
                                                ('sha_1', (YLeaf(YType.empty, 'sha-1'), ['Empty'])),
                                                ('hmac_sha_1', (YLeaf(YType.empty, 'hmac-sha-1'), ['Empty'])),
                                                ('hmac_sha_256', (YLeaf(YType.empty, 'hmac-sha-256'), ['Empty'])),
                                                ('hmac_sha_384', (YLeaf(YType.empty, 'hmac-sha-384'), ['Empty'])),
                                                ('hmac_sha_512', (YLeaf(YType.empty, 'hmac-sha-512'), ['Empty'])),
                                            ])
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.md5 = None
                                            self.sha_1 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self._segment_path = lambda: "crypto-algorithm"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'md5', 'sha_1', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512'], name, value)


                                class Neighbor(Entity):
                                    """
                                    List of OSPF neighbors.
                                    
                                    .. attribute:: neighbor_id  (key)
                                    
                                    	Neighbor ID
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address
                                    
                                    	Neighbor address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: dr
                                    
                                    	Designated Router
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: bdr
                                    
                                    	Backup Designated Router
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: state
                                    
                                    	OSPF neighbor state
                                    	**type**\:  :py:class:`NbrStateType <ydk.models.ietf.ietf_ospf.NbrStateType>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor, self).__init__()

                                        self.yang_name = "neighbor"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['neighbor_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('neighbor_id', (YLeaf(YType.str, 'neighbor-id'), ['str'])),
                                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                            ('dr', (YLeaf(YType.str, 'dr'), ['str'])),
                                            ('bdr', (YLeaf(YType.str, 'bdr'), ['str'])),
                                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.ietf.ietf_ospf', 'NbrStateType', '')])),
                                        ])
                                        self.neighbor_id = None
                                        self.address = None
                                        self.dr = None
                                        self.bdr = None
                                        self.state = None
                                        self._segment_path = lambda: "neighbor" + "[neighbor-id='" + str(self.neighbor_id) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor, ['neighbor_id', 'address', 'dr', 'bdr', 'state'], name, value)


                                class LinkScopeLsas(Entity):
                                    """
                                    List OSPF link scope LSA databases
                                    
                                    .. attribute:: lsa_type  (key)
                                    
                                    	OSPF link scope LSA type
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: link_scope_lsa
                                    
                                    	List of OSPF link scope LSAs
                                    	**type**\: list of  		 :py:class:`LinkScopeLsa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas, self).__init__()

                                        self.yang_name = "link-scope-lsas"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['lsa_type']
                                        self._child_classes = OrderedDict([("link-scope-lsa", ("link_scope_lsa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa))])
                                        self._leafs = OrderedDict([
                                            ('lsa_type', (YLeaf(YType.uint8, 'lsa-type'), ['int'])),
                                        ])
                                        self.lsa_type = None

                                        self.link_scope_lsa = YList(self)
                                        self._segment_path = lambda: "link-scope-lsas" + "[lsa-type='" + str(self.lsa_type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas, ['lsa_type'], name, value)


                                    class LinkScopeLsa(Entity):
                                        """
                                        List of OSPF link scope LSAs
                                        
                                        .. attribute:: lsa_id  (key)
                                        
                                        	LSA ID
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: int
                                        
                                        			**range:** 0..4294967295
                                        
                                        .. attribute:: adv_router  (key)
                                        
                                        	Advertising router
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: decoded_completed
                                        
                                        	The OSPF LSA body is fully decoded
                                        	**type**\: bool
                                        
                                        .. attribute:: raw_data
                                        
                                        	The complete LSA in network byte order as received/sent over the wire
                                        	**type**\: str
                                        
                                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                        
                                        .. attribute:: ospfv2
                                        
                                        	OSPFv2 LSA
                                        	**type**\:  :py:class:`Ospfv2 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2>`
                                        
                                        .. attribute:: ospfv3
                                        
                                        	OSPFv3 LSA
                                        	**type**\:  :py:class:`Ospfv3 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa, self).__init__()

                                            self.yang_name = "link-scope-lsa"
                                            self.yang_parent_name = "link-scope-lsas"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['lsa_id','adv_router']
                                            self._child_classes = OrderedDict([("ospfv2", ("ospfv2", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2)), ("ospfv3", ("ospfv3", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3))])
                                            self._leafs = OrderedDict([
                                                ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','int'])),
                                                ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                                ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                                                ('raw_data', (YLeaf(YType.str, 'raw-data'), ['str'])),
                                            ])
                                            self.lsa_id = None
                                            self.adv_router = None
                                            self.decoded_completed = None
                                            self.raw_data = None

                                            self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2()
                                            self.ospfv2.parent = self
                                            self._children_name_map["ospfv2"] = "ospfv2"

                                            self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3()
                                            self.ospfv3.parent = self
                                            self._children_name_map["ospfv3"] = "ospfv3"
                                            self._segment_path = lambda: "link-scope-lsa" + "[lsa-id='" + str(self.lsa_id) + "']" + "[adv-router='" + str(self.adv_router) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                                        class Ospfv2(Entity):
                                            """
                                            OSPFv2 LSA
                                            
                                            .. attribute:: header
                                            
                                            	Decoded OSPFv2 LSA header data
                                            	**type**\:  :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header>`
                                            
                                            .. attribute:: body
                                            
                                            	Decoded OSPFv2 LSA body data
                                            	**type**\:  :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2, self).__init__()

                                                self.yang_name = "ospfv2"
                                                self.yang_parent_name = "link-scope-lsa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("header", ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header)), ("body", ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body))])
                                                self._leafs = OrderedDict()

                                                self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header()
                                                self.header.parent = self
                                                self._children_name_map["header"] = "header"

                                                self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body()
                                                self.body.parent = self
                                                self._children_name_map["body"] = "body"
                                                self._segment_path = lambda: "ospfv2"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2, [], name, value)


                                            class Header(Entity):
                                                """
                                                Decoded OSPFv2 LSA header data.
                                                
                                                .. attribute:: options
                                                
                                                	LSA option
                                                	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: lsa_id
                                                
                                                	LSA ID
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: opaque_type
                                                
                                                	Opaque type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: opaque_id
                                                
                                                	Opaque id
                                                	**type**\: int
                                                
                                                	**range:** 0..16777215
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: age
                                                
                                                	LSA age
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: type
                                                
                                                	LSA type
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: adv_router
                                                
                                                	LSA advertising router
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: seq_num
                                                
                                                	LSA sequence number
                                                	**type**\: str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: checksum
                                                
                                                	LSA checksum
                                                	**type**\: str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: length
                                                
                                                	LSA length
                                                	**type**\: int
                                                
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
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                        ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str'])),
                                                        ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                                        ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                                        ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                        ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                                        ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                        ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                    ])
                                                    self.options = Bits()
                                                    self.lsa_id = None
                                                    self.opaque_type = None
                                                    self.opaque_id = None
                                                    self.age = None
                                                    self.type = None
                                                    self.adv_router = None
                                                    self.seq_num = None
                                                    self.checksum = None
                                                    self.length = None
                                                    self._segment_path = lambda: "header"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header, ['options', 'lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                                            class Body(Entity):
                                                """
                                                Decoded OSPFv2 LSA body data.
                                                
                                                .. attribute:: router
                                                
                                                	Router LSA
                                                	**type**\:  :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router>`
                                                
                                                .. attribute:: network
                                                
                                                	Network LSA
                                                	**type**\:  :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network>`
                                                
                                                .. attribute:: summary
                                                
                                                	Summary LSA
                                                	**type**\:  :py:class:`Summary <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary>`
                                                
                                                .. attribute:: external
                                                
                                                	External LSA
                                                	**type**\:  :py:class:`External <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External>`
                                                
                                                .. attribute:: opaque
                                                
                                                	Opaque LSA
                                                	**type**\:  :py:class:`Opaque <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body, self).__init__()

                                                    self.yang_name = "body"
                                                    self.yang_parent_name = "ospfv2"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("router", ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router)), ("network", ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network)), ("summary", ("summary", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary)), ("external", ("external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External)), ("opaque", ("opaque", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque))])
                                                    self._leafs = OrderedDict()

                                                    self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router()
                                                    self.router.parent = self
                                                    self._children_name_map["router"] = "router"

                                                    self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network()
                                                    self.network.parent = self
                                                    self._children_name_map["network"] = "network"

                                                    self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary()
                                                    self.summary.parent = self
                                                    self._children_name_map["summary"] = "summary"

                                                    self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External()
                                                    self.external.parent = self
                                                    self._children_name_map["external"] = "external"

                                                    self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque()
                                                    self.opaque.parent = self
                                                    self._children_name_map["opaque"] = "opaque"
                                                    self._segment_path = lambda: "body"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body, [], name, value)


                                                class Router(Entity):
                                                    """
                                                    Router LSA.
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Flags>`
                                                    
                                                    .. attribute:: num_of_links
                                                    
                                                    	Number of links
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: link
                                                    
                                                    	Router LSA link
                                                    	**type**\: list of  		 :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router, self).__init__()

                                                        self.yang_name = "router"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link))])
                                                        self._leafs = OrderedDict([
                                                            ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                            ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                                        ])
                                                        self.flags = Bits()
                                                        self.num_of_links = None

                                                        self.link = YList(self)
                                                        self._segment_path = lambda: "router"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router, ['flags', 'num_of_links'], name, value)


                                                    class Link(Entity):
                                                        """
                                                        Router LSA link.
                                                        
                                                        .. attribute:: link_id  (key)
                                                        
                                                        	Link ID
                                                        	**type**\: union of the below types:
                                                        
                                                        		**type**\: str
                                                        
                                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        		**type**\: str
                                                        
                                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                        
                                                        .. attribute:: link_data  (key)
                                                        
                                                        	Link data
                                                        	**type**\: union of the below types:
                                                        
                                                        		**type**\: str
                                                        
                                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        		**type**\: int
                                                        
                                                        			**range:** 0..4294967295
                                                        
                                                        .. attribute:: type
                                                        
                                                        	Link type
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: topology
                                                        
                                                        	Topology specific information
                                                        	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link, self).__init__()

                                                            self.yang_name = "link"
                                                            self.yang_parent_name = "router"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['link_id','link_data']
                                                            self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology))])
                                                            self._leafs = OrderedDict([
                                                                ('link_id', (YLeaf(YType.str, 'link-id'), ['str','str'])),
                                                                ('link_data', (YLeaf(YType.str, 'link-data'), ['str','int'])),
                                                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                                            ])
                                                            self.link_id = None
                                                            self.link_data = None
                                                            self.type = None

                                                            self.topology = YList(self)
                                                            self._segment_path = lambda: "link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link, ['link_id', 'link_data', 'type'], name, value)


                                                        class Topology(Entity):
                                                            """
                                                            Topology specific information.
                                                            
                                                            .. attribute:: mt_id  (key)
                                                            
                                                            	The MT\-ID for topology enabled on the link
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..255
                                                            
                                                            .. attribute:: metric
                                                            
                                                            	Metric for the topology
                                                            	**type**\: int
                                                            
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
                                                                self.ylist_key_names = ['mt_id']
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                                    ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                                                ])
                                                                self.mt_id = None
                                                                self.metric = None
                                                                self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology, ['mt_id', 'metric'], name, value)


                                                class Network(Entity):
                                                    """
                                                    Network LSA.
                                                    
                                                    .. attribute:: network_mask
                                                    
                                                    	The IP address mask for the network
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: attached_router
                                                    
                                                    	List of the routers attached to the network
                                                    	**type**\: list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network, self).__init__()

                                                        self.yang_name = "network"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                            ('attached_router', (YLeafList(YType.str, 'attached-router'), ['str'])),
                                                        ])
                                                        self.network_mask = None
                                                        self.attached_router = []
                                                        self._segment_path = lambda: "network"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network, ['network_mask', 'attached_router'], name, value)


                                                class Summary(Entity):
                                                    """
                                                    Summary LSA.
                                                    
                                                    .. attribute:: network_mask
                                                    
                                                    	The IP address mask for the network
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: topology
                                                    
                                                    	Topology specific information
                                                    	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary, self).__init__()

                                                        self.yang_name = "summary"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology))])
                                                        self._leafs = OrderedDict([
                                                            ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                        ])
                                                        self.network_mask = None

                                                        self.topology = YList(self)
                                                        self._segment_path = lambda: "summary"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary, ['network_mask'], name, value)


                                                    class Topology(Entity):
                                                        """
                                                        Topology specific information.
                                                        
                                                        .. attribute:: mt_id  (key)
                                                        
                                                        	The MT\-ID for topology enabled on the link
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric for the topology
                                                        	**type**\: int
                                                        
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
                                                            self.ylist_key_names = ['mt_id']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                            ])
                                                            self.mt_id = None
                                                            self.metric = None
                                                            self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology, ['mt_id', 'metric'], name, value)


                                                class External(Entity):
                                                    """
                                                    External LSA.
                                                    
                                                    .. attribute:: network_mask
                                                    
                                                    	The IP address mask for the network
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: topology
                                                    
                                                    	Topology specific information
                                                    	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External, self).__init__()

                                                        self.yang_name = "external"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology))])
                                                        self._leafs = OrderedDict([
                                                            ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                        ])
                                                        self.network_mask = None

                                                        self.topology = YList(self)
                                                        self._segment_path = lambda: "external"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External, ['network_mask'], name, value)


                                                    class Topology(Entity):
                                                        """
                                                        Topology specific information.
                                                        
                                                        .. attribute:: mt_id  (key)
                                                        
                                                        	The MT\-ID for topology enabled on the link
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: flags
                                                        
                                                        	Flags
                                                        	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology.Flags>`
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric for the topology
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..16777215
                                                        
                                                        .. attribute:: forwarding_address
                                                        
                                                        	Forwarding address
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: external_route_tag
                                                        
                                                        	Route tag
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology, self).__init__()

                                                            self.yang_name = "topology"
                                                            self.yang_parent_name = "external"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['mt_id']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                                ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                                ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                                ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                            ])
                                                            self.mt_id = None
                                                            self.flags = Bits()
                                                            self.metric = None
                                                            self.forwarding_address = None
                                                            self.external_route_tag = None
                                                            self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology, ['mt_id', 'flags', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                                                class Opaque(Entity):
                                                    """
                                                    Opaque LSA.
                                                    
                                                    .. attribute:: unknown_tlv
                                                    
                                                    	Unknown TLV
                                                    	**type**\: list of  		 :py:class:`UnknownTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv>`
                                                    
                                                    .. attribute:: router_address_tlv
                                                    
                                                    	Router address TLV
                                                    	**type**\:  :py:class:`RouterAddressTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv>`
                                                    
                                                    .. attribute:: link_tlv
                                                    
                                                    	Link TLV
                                                    	**type**\:  :py:class:`LinkTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque, self).__init__()

                                                        self.yang_name = "opaque"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("unknown-tlv", ("unknown_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv)), ("router-address-tlv", ("router_address_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv)), ("link-tlv", ("link_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv))])
                                                        self._leafs = OrderedDict()

                                                        self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                        self.router_address_tlv.parent = self
                                                        self._children_name_map["router_address_tlv"] = "router-address-tlv"

                                                        self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                        self.link_tlv.parent = self
                                                        self._children_name_map["link_tlv"] = "link-tlv"

                                                        self.unknown_tlv = YList(self)
                                                        self._segment_path = lambda: "opaque"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque, [], name, value)


                                                    class UnknownTlv(Entity):
                                                        """
                                                        Unknown TLV.
                                                        
                                                        .. attribute:: type  (key)
                                                        
                                                        	TLV type
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: length
                                                        
                                                        	TLV length
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: value
                                                        
                                                        	TLV value
                                                        	**type**\: str
                                                        
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
                                                            self.ylist_key_names = ['type']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                                            ])
                                                            self.type = None
                                                            self.length = None
                                                            self.value = None
                                                            self._segment_path = lambda: "unknown-tlv" + "[type='" + str(self.type) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, ['type', 'length', 'value'], name, value)


                                                    class RouterAddressTlv(Entity):
                                                        """
                                                        Router address TLV.
                                                        
                                                        .. attribute:: router_address
                                                        
                                                        	Router address
                                                        	**type**\: str
                                                        
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
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('router_address', (YLeaf(YType.str, 'router-address'), ['str'])),
                                                            ])
                                                            self.router_address = None
                                                            self._segment_path = lambda: "router-address-tlv"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, ['router_address'], name, value)


                                                    class LinkTlv(Entity):
                                                        """
                                                        Link TLV.
                                                        
                                                        .. attribute:: link_type
                                                        
                                                        	Link type
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        .. attribute:: link_id
                                                        
                                                        	Link ID
                                                        	**type**\: union of the below types:
                                                        
                                                        		**type**\: str
                                                        
                                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        		**type**\: str
                                                        
                                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        .. attribute:: local_if_ipv4_addr
                                                        
                                                        	List of local interface IPv4 addresses
                                                        	**type**\: list of str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: local_remote_ipv4_addr
                                                        
                                                        	List of remote interface IPv4 addresses
                                                        	**type**\: list of str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                        
                                                        .. attribute:: te_metric
                                                        
                                                        	TE metric
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: max_bandwidth
                                                        
                                                        	Maximum bandwidth
                                                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                        
                                                        	**range:** \-92233720368547758.08..92233720368547758.07
                                                        
                                                        .. attribute:: max_reservable_bandwidth
                                                        
                                                        	Maximum reservable bandwidth
                                                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                        
                                                        	**range:** \-92233720368547758.08..92233720368547758.07
                                                        
                                                        .. attribute:: unreserved_bandwidth
                                                        
                                                        	Unreserved bandwidth
                                                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                        
                                                        	**range:** \-92233720368547758.08..92233720368547758.07
                                                        
                                                        .. attribute:: admin_group
                                                        
                                                        	Administrative group/Resource class/Color
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: unknown_subtlv
                                                        
                                                        	Unknown sub\-TLV
                                                        	**type**\: list of  		 :py:class:`UnknownSubtlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv, self).__init__()

                                                            self.yang_name = "link-tlv"
                                                            self.yang_parent_name = "opaque"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_classes = OrderedDict([("unknown-subtlv", ("unknown_subtlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv))])
                                                            self._leafs = OrderedDict([
                                                                ('link_type', (YLeaf(YType.uint8, 'link-type'), ['int'])),
                                                                ('link_id', (YLeaf(YType.str, 'link-id'), ['str','str'])),
                                                                ('local_if_ipv4_addr', (YLeafList(YType.str, 'local-if-ipv4-addr'), ['str'])),
                                                                ('local_remote_ipv4_addr', (YLeafList(YType.str, 'local-remote-ipv4-addr'), ['str'])),
                                                                ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                                                                ('max_bandwidth', (YLeaf(YType.str, 'max-bandwidth'), ['Decimal64'])),
                                                                ('max_reservable_bandwidth', (YLeaf(YType.str, 'max-reservable-bandwidth'), ['Decimal64'])),
                                                                ('unreserved_bandwidth', (YLeaf(YType.str, 'unreserved-bandwidth'), ['Decimal64'])),
                                                                ('admin_group', (YLeaf(YType.uint32, 'admin-group'), ['int'])),
                                                            ])
                                                            self.link_type = None
                                                            self.link_id = None
                                                            self.local_if_ipv4_addr = []
                                                            self.local_remote_ipv4_addr = []
                                                            self.te_metric = None
                                                            self.max_bandwidth = None
                                                            self.max_reservable_bandwidth = None
                                                            self.unreserved_bandwidth = None
                                                            self.admin_group = None

                                                            self.unknown_subtlv = YList(self)
                                                            self._segment_path = lambda: "link-tlv"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv, ['link_type', 'link_id', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'te_metric', 'max_bandwidth', 'max_reservable_bandwidth', 'unreserved_bandwidth', 'admin_group'], name, value)


                                                        class UnknownSubtlv(Entity):
                                                            """
                                                            Unknown sub\-TLV.
                                                            
                                                            .. attribute:: type  (key)
                                                            
                                                            	TLV type
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..65535
                                                            
                                                            .. attribute:: length
                                                            
                                                            	TLV length
                                                            	**type**\: int
                                                            
                                                            	**range:** 0..65535
                                                            
                                                            .. attribute:: value
                                                            
                                                            	TLV value
                                                            	**type**\: str
                                                            
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
                                                                self.ylist_key_names = ['type']
                                                                self._child_classes = OrderedDict([])
                                                                self._leafs = OrderedDict([
                                                                    ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                                    ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                                    ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                                                ])
                                                                self.type = None
                                                                self.length = None
                                                                self.value = None
                                                                self._segment_path = lambda: "unknown-subtlv" + "[type='" + str(self.type) + "']"
                                                                self._is_frozen = True

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, ['type', 'length', 'value'], name, value)


                                        class Ospfv3(Entity):
                                            """
                                            OSPFv3 LSA
                                            
                                            .. attribute:: header
                                            
                                            	Decoded OSPFv3 LSA header data
                                            	**type**\:  :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header>`
                                            
                                            .. attribute:: body
                                            
                                            	Decoded OSPF LSA body data
                                            	**type**\:  :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3, self).__init__()

                                                self.yang_name = "ospfv3"
                                                self.yang_parent_name = "link-scope-lsa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("header", ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header)), ("body", ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body))])
                                                self._leafs = OrderedDict()

                                                self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header()
                                                self.header.parent = self
                                                self._children_name_map["header"] = "header"

                                                self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body()
                                                self.body.parent = self
                                                self._children_name_map["body"] = "body"
                                                self._segment_path = lambda: "ospfv3"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3, [], name, value)


                                            class Header(Entity):
                                                """
                                                Decoded OSPFv3 LSA header data.
                                                
                                                .. attribute:: lsa_id
                                                
                                                	LSA ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: age
                                                
                                                	LSA age
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: type
                                                
                                                	LSA type
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: adv_router
                                                
                                                	LSA advertising router
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: seq_num
                                                
                                                	LSA sequence number
                                                	**type**\: str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: checksum
                                                
                                                	LSA checksum
                                                	**type**\: str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: length
                                                
                                                	LSA length
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header.Options>`
                                                
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
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('lsa_id', (YLeaf(YType.uint32, 'lsa-id'), ['int'])),
                                                        ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                        ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                                        ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                        ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                        ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                    ])
                                                    self.lsa_id = None
                                                    self.age = None
                                                    self.type = None
                                                    self.adv_router = None
                                                    self.seq_num = None
                                                    self.checksum = None
                                                    self.length = None
                                                    self.options = Bits()
                                                    self._segment_path = lambda: "header"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header, ['lsa_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'options'], name, value)


                                            class Body(Entity):
                                                """
                                                Decoded OSPF LSA body data.
                                                
                                                .. attribute:: router
                                                
                                                	Router LSA
                                                	**type**\:  :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router>`
                                                
                                                .. attribute:: network
                                                
                                                	Network LSA
                                                	**type**\:  :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network>`
                                                
                                                .. attribute:: inter_area_prefix
                                                
                                                	Inter\-Area\-Prefix LSA
                                                	**type**\:  :py:class:`InterAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix>`
                                                
                                                .. attribute:: inter_area_router
                                                
                                                	Inter\-Area\-Router LSA
                                                	**type**\:  :py:class:`InterAreaRouter <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter>`
                                                
                                                .. attribute:: as_external
                                                
                                                	AS\-External LSA
                                                	**type**\:  :py:class:`AsExternal <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal>`
                                                
                                                .. attribute:: nssa
                                                
                                                	NSSA LSA
                                                	**type**\:  :py:class:`Nssa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa>`
                                                
                                                .. attribute:: link
                                                
                                                	Link LSA
                                                	**type**\:  :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link>`
                                                
                                                .. attribute:: intra_area_prefix
                                                
                                                	Intra\-Area\-Prefix LSA
                                                	**type**\:  :py:class:`IntraAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body, self).__init__()

                                                    self.yang_name = "body"
                                                    self.yang_parent_name = "ospfv3"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("router", ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router)), ("network", ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network)), ("inter-area-prefix", ("inter_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix)), ("inter-area-router", ("inter_area_router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter)), ("as-external", ("as_external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal)), ("nssa", ("nssa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa)), ("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link)), ("intra-area-prefix", ("intra_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix))])
                                                    self._leafs = OrderedDict()

                                                    self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router()
                                                    self.router.parent = self
                                                    self._children_name_map["router"] = "router"

                                                    self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network()
                                                    self.network.parent = self
                                                    self._children_name_map["network"] = "network"

                                                    self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                                    self.inter_area_prefix.parent = self
                                                    self._children_name_map["inter_area_prefix"] = "inter-area-prefix"

                                                    self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter()
                                                    self.inter_area_router.parent = self
                                                    self._children_name_map["inter_area_router"] = "inter-area-router"

                                                    self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal()
                                                    self.as_external.parent = self
                                                    self._children_name_map["as_external"] = "as-external"

                                                    self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa()
                                                    self.nssa.parent = self
                                                    self._children_name_map["nssa"] = "nssa"

                                                    self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link()
                                                    self.link.parent = self
                                                    self._children_name_map["link"] = "link"

                                                    self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                                    self.intra_area_prefix.parent = self
                                                    self._children_name_map["intra_area_prefix"] = "intra-area-prefix"
                                                    self._segment_path = lambda: "body"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body, [], name, value)


                                                class Router(Entity):
                                                    """
                                                    Router LSA.
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	LSA option
                                                    	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Flags>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: link
                                                    
                                                    	Router LSA link
                                                    	**type**\: list of  		 :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router, self).__init__()

                                                        self.yang_name = "router"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link))])
                                                        self._leafs = OrderedDict([
                                                            ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                            ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                        ])
                                                        self.flags = Bits()
                                                        self.options = Bits()

                                                        self.link = YList(self)
                                                        self._segment_path = lambda: "router"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router, ['flags', 'options'], name, value)


                                                    class Link(Entity):
                                                        """
                                                        Router LSA link.
                                                        
                                                        .. attribute:: interface_id  (key)
                                                        
                                                        	Interface ID
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neighbor_interface_id  (key)
                                                        
                                                        	Neighbor Interface ID
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..4294967295
                                                        
                                                        .. attribute:: neighbor_router_id  (key)
                                                        
                                                        	Neighbor Router ID
                                                        	**type**\: str
                                                        
                                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                        
                                                        .. attribute:: type
                                                        
                                                        	Link type
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link, self).__init__()

                                                            self.yang_name = "link"
                                                            self.yang_parent_name = "router"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                                                ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                                                ('neighbor_router_id', (YLeaf(YType.str, 'neighbor-router-id'), ['str'])),
                                                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                                            ])
                                                            self.interface_id = None
                                                            self.neighbor_interface_id = None
                                                            self.neighbor_router_id = None
                                                            self.type = None
                                                            self.metric = None
                                                            self._segment_path = lambda: "link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                                                class Network(Entity):
                                                    """
                                                    Network LSA.
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: attached_router
                                                    
                                                    	List of the routers attached to the network
                                                    	**type**\: list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network, self).__init__()

                                                        self.yang_name = "network"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                            ('attached_router', (YLeafList(YType.str, 'attached-router'), ['str'])),
                                                        ])
                                                        self.options = Bits()
                                                        self.attached_router = []
                                                        self._segment_path = lambda: "network"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network, ['options', 'attached_router'], name, value)


                                                class InterAreaPrefix(Entity):
                                                    """
                                                    Inter\-Area\-Prefix LSA.
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: prefix
                                                    
                                                    	Prefix
                                                    	**type**\: str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\: str
                                                    
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
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                            ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                        ])
                                                        self.metric = None
                                                        self.prefix = None
                                                        self.prefix_options = None
                                                        self._segment_path = lambda: "inter-area-prefix"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix, ['metric', 'prefix', 'prefix_options'], name, value)


                                                class InterAreaRouter(Entity):
                                                    """
                                                    Inter\-Area\-Router LSA.
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: destination_router_id
                                                    
                                                    	The Router ID of the router being described by the LSA
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter, self).__init__()

                                                        self.yang_name = "inter-area-router"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                            ('destination_router_id', (YLeaf(YType.str, 'destination-router-id'), ['str'])),
                                                        ])
                                                        self.options = Bits()
                                                        self.metric = None
                                                        self.destination_router_id = None
                                                        self._segment_path = lambda: "inter-area-router"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter, ['options', 'metric', 'destination_router_id'], name, value)


                                                class AsExternal(Entity):
                                                    """
                                                    AS\-External LSA.
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal.Flags>`
                                                    
                                                    .. attribute:: referenced_ls_type
                                                    
                                                    	Referenced Link State type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: prefix
                                                    
                                                    	Prefix
                                                    	**type**\: str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\: str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: forwarding_address
                                                    
                                                    	Forwarding address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: external_route_tag
                                                    
                                                    	Route tag
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: referenced_link_state_id
                                                    
                                                    	Referenced Link State ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal, self).__init__()

                                                        self.yang_name = "as-external"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                            ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                            ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                            ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                            ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                            ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                            ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                        ])
                                                        self.metric = None
                                                        self.flags = Bits()
                                                        self.referenced_ls_type = None
                                                        self.prefix = None
                                                        self.prefix_options = None
                                                        self.forwarding_address = None
                                                        self.external_route_tag = None
                                                        self.referenced_link_state_id = None
                                                        self._segment_path = lambda: "as-external"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal, ['metric', 'flags', 'referenced_ls_type', 'prefix', 'prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                                class Nssa(Entity):
                                                    """
                                                    NSSA LSA.
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa.Flags>`
                                                    
                                                    .. attribute:: referenced_ls_type
                                                    
                                                    	Referenced Link State type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: prefix
                                                    
                                                    	Prefix
                                                    	**type**\: str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\: str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: forwarding_address
                                                    
                                                    	Forwarding address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: external_route_tag
                                                    
                                                    	Route tag
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: referenced_link_state_id
                                                    
                                                    	Referenced Link State ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa, self).__init__()

                                                        self.yang_name = "nssa"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                            ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                            ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                            ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                            ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                            ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                            ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                        ])
                                                        self.metric = None
                                                        self.flags = Bits()
                                                        self.referenced_ls_type = None
                                                        self.prefix = None
                                                        self.prefix_options = None
                                                        self.forwarding_address = None
                                                        self.external_route_tag = None
                                                        self.referenced_link_state_id = None
                                                        self._segment_path = lambda: "nssa"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa, ['metric', 'flags', 'referenced_ls_type', 'prefix', 'prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                                class Link(Entity):
                                                    """
                                                    Link LSA.
                                                    
                                                    .. attribute:: rtr_priority
                                                    
                                                    	Router Priority of the interface
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: options
                                                    
                                                    	OSPFv3 LSA options
                                                    	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.Options>`
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: link_local_interface_address
                                                    
                                                    	The originating router's link\-local interface address on the link
                                                    	**type**\: union of the below types:
                                                    
                                                    		**type**\: str
                                                    
                                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    		**type**\: str
                                                    
                                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: num_of_prefixes
                                                    
                                                    	Number of prefixes
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: prefix_list
                                                    
                                                    	List of prefixes associated with the link
                                                    	**type**\: list of  		 :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link, self).__init__()

                                                        self.yang_name = "link"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("prefix-list", ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList))])
                                                        self._leafs = OrderedDict([
                                                            ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                                            ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                            ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                                            ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                                        ])
                                                        self.rtr_priority = None
                                                        self.options = Bits()
                                                        self.link_local_interface_address = None
                                                        self.num_of_prefixes = None

                                                        self.prefix_list = YList(self)
                                                        self._segment_path = lambda: "link"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link, ['rtr_priority', 'options', 'link_local_interface_address', 'num_of_prefixes'], name, value)


                                                    class PrefixList(Entity):
                                                        """
                                                        List of prefixes associated with the link.
                                                        
                                                        .. attribute:: prefix  (key)
                                                        
                                                        	Prefix
                                                        	**type**\: str
                                                        
                                                        .. attribute:: prefix_options
                                                        
                                                        	Prefix options
                                                        	**type**\: str
                                                        
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
                                                            self.ylist_key_names = ['prefix']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                                ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                            ])
                                                            self.prefix = None
                                                            self.prefix_options = None
                                                            self._segment_path = lambda: "prefix-list" + "[prefix='" + str(self.prefix) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList, ['prefix', 'prefix_options'], name, value)


                                                class IntraAreaPrefix(Entity):
                                                    """
                                                    Intra\-Area\-Prefix LSA.
                                                    
                                                    .. attribute:: referenced_ls_type
                                                    
                                                    	Referenced Link State type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: referenced_link_state_id
                                                    
                                                    	Referenced Link State ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: referenced_adv_router
                                                    
                                                    	Referenced Advertising Router
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: num_of_prefixes
                                                    
                                                    	Number of prefixes
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: prefix_list
                                                    
                                                    	List of prefixes associated with the link
                                                    	**type**\: list of  		 :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix, self).__init__()

                                                        self.yang_name = "intra-area-prefix"
                                                        self.yang_parent_name = "body"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("prefix-list", ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList))])
                                                        self._leafs = OrderedDict([
                                                            ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                            ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                            ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str'])),
                                                            ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                                        ])
                                                        self.referenced_ls_type = None
                                                        self.referenced_link_state_id = None
                                                        self.referenced_adv_router = None
                                                        self.num_of_prefixes = None

                                                        self.prefix_list = YList(self)
                                                        self._segment_path = lambda: "intra-area-prefix"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                                                    class PrefixList(Entity):
                                                        """
                                                        List of prefixes associated with the link.
                                                        
                                                        .. attribute:: prefix  (key)
                                                        
                                                        	Prefix
                                                        	**type**\: str
                                                        
                                                        .. attribute:: prefix_options
                                                        
                                                        	Prefix options
                                                        	**type**\: str
                                                        
                                                        	**mandatory**\: True
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..16777215
                                                        
                                                        

                                                        """

                                                        _prefix = 'ospf'
                                                        _revision = '2015-03-09'

                                                        def __init__(self):
                                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, self).__init__()

                                                            self.yang_name = "prefix-list"
                                                            self.yang_parent_name = "intra-area-prefix"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = ['prefix']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                                ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                            ])
                                                            self.prefix = None
                                                            self.prefix_options = None
                                                            self.metric = None
                                                            self._segment_path = lambda: "prefix-list" + "[prefix='" + str(self.prefix) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, ['prefix', 'prefix_options', 'metric'], name, value)


                                class Topology(Entity):
                                    """
                                    OSPF interface topology.
                                    
                                    .. attribute:: name  (key)
                                    
                                    	One of the topology enabled on this interface
                                    	**type**\: str
                                    
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
                                        self.ylist_key_names = ['name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                        ])
                                        self.name = None
                                        self._segment_path = lambda: "topology" + "[name='" + str(self.name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology, ['name'], name, value)


                            class AreaScopeLsas(Entity):
                                """
                                List OSPF area scope LSA databases
                                
                                .. attribute:: lsa_type  (key)
                                
                                	OSPF area scope LSA type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: area_scope_lsa
                                
                                	List of OSPF area scope LSAs
                                	**type**\: list of  		 :py:class:`AreaScopeLsa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas, self).__init__()

                                    self.yang_name = "area-scope-lsas"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['lsa_type']
                                    self._child_classes = OrderedDict([("area-scope-lsa", ("area_scope_lsa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa))])
                                    self._leafs = OrderedDict([
                                        ('lsa_type', (YLeaf(YType.uint8, 'lsa-type'), ['int'])),
                                    ])
                                    self.lsa_type = None

                                    self.area_scope_lsa = YList(self)
                                    self._segment_path = lambda: "area-scope-lsas" + "[lsa-type='" + str(self.lsa_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas, ['lsa_type'], name, value)


                                class AreaScopeLsa(Entity):
                                    """
                                    List of OSPF area scope LSAs
                                    
                                    .. attribute:: lsa_id  (key)
                                    
                                    	LSA ID
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: int
                                    
                                    			**range:** 0..4294967295
                                    
                                    .. attribute:: adv_router  (key)
                                    
                                    	Advertising router
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: decoded_completed
                                    
                                    	The OSPF LSA body is fully decoded
                                    	**type**\: bool
                                    
                                    .. attribute:: raw_data
                                    
                                    	The complete LSA in network byte order as received/sent over the wire
                                    	**type**\: str
                                    
                                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                    
                                    .. attribute:: ospfv2
                                    
                                    	OSPFv2 LSA
                                    	**type**\:  :py:class:`Ospfv2 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2>`
                                    
                                    .. attribute:: ospfv3
                                    
                                    	OSPFv3 LSA
                                    	**type**\:  :py:class:`Ospfv3 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa, self).__init__()

                                        self.yang_name = "area-scope-lsa"
                                        self.yang_parent_name = "area-scope-lsas"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['lsa_id','adv_router']
                                        self._child_classes = OrderedDict([("ospfv2", ("ospfv2", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2)), ("ospfv3", ("ospfv3", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3))])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','int'])),
                                            ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                            ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                                            ('raw_data', (YLeaf(YType.str, 'raw-data'), ['str'])),
                                        ])
                                        self.lsa_id = None
                                        self.adv_router = None
                                        self.decoded_completed = None
                                        self.raw_data = None

                                        self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2()
                                        self.ospfv2.parent = self
                                        self._children_name_map["ospfv2"] = "ospfv2"

                                        self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3()
                                        self.ospfv3.parent = self
                                        self._children_name_map["ospfv3"] = "ospfv3"
                                        self._segment_path = lambda: "area-scope-lsa" + "[lsa-id='" + str(self.lsa_id) + "']" + "[adv-router='" + str(self.adv_router) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                                    class Ospfv2(Entity):
                                        """
                                        OSPFv2 LSA
                                        
                                        .. attribute:: header
                                        
                                        	Decoded OSPFv2 LSA header data
                                        	**type**\:  :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header>`
                                        
                                        .. attribute:: body
                                        
                                        	Decoded OSPFv2 LSA body data
                                        	**type**\:  :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2, self).__init__()

                                            self.yang_name = "ospfv2"
                                            self.yang_parent_name = "area-scope-lsa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("header", ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header)), ("body", ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body))])
                                            self._leafs = OrderedDict()

                                            self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header()
                                            self.header.parent = self
                                            self._children_name_map["header"] = "header"

                                            self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body()
                                            self.body.parent = self
                                            self._children_name_map["body"] = "body"
                                            self._segment_path = lambda: "ospfv2"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2, [], name, value)


                                        class Header(Entity):
                                            """
                                            Decoded OSPFv2 LSA header data.
                                            
                                            .. attribute:: options
                                            
                                            	LSA option
                                            	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: lsa_id
                                            
                                            	LSA ID
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: opaque_type
                                            
                                            	Opaque type
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: opaque_id
                                            
                                            	Opaque id
                                            	**type**\: int
                                            
                                            	**range:** 0..16777215
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: age
                                            
                                            	LSA age
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: type
                                            
                                            	LSA type
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: adv_router
                                            
                                            	LSA advertising router
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: seq_num
                                            
                                            	LSA sequence number
                                            	**type**\: str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: checksum
                                            
                                            	LSA checksum
                                            	**type**\: str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: length
                                            
                                            	LSA length
                                            	**type**\: int
                                            
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
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                    ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str'])),
                                                    ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                                    ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                                    ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                    ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                    ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                                    ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                    ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                    ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                ])
                                                self.options = Bits()
                                                self.lsa_id = None
                                                self.opaque_type = None
                                                self.opaque_id = None
                                                self.age = None
                                                self.type = None
                                                self.adv_router = None
                                                self.seq_num = None
                                                self.checksum = None
                                                self.length = None
                                                self._segment_path = lambda: "header"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header, ['options', 'lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                                        class Body(Entity):
                                            """
                                            Decoded OSPFv2 LSA body data.
                                            
                                            .. attribute:: router
                                            
                                            	Router LSA
                                            	**type**\:  :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router>`
                                            
                                            .. attribute:: network
                                            
                                            	Network LSA
                                            	**type**\:  :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network>`
                                            
                                            .. attribute:: summary
                                            
                                            	Summary LSA
                                            	**type**\:  :py:class:`Summary <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary>`
                                            
                                            .. attribute:: external
                                            
                                            	External LSA
                                            	**type**\:  :py:class:`External <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External>`
                                            
                                            .. attribute:: opaque
                                            
                                            	Opaque LSA
                                            	**type**\:  :py:class:`Opaque <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body, self).__init__()

                                                self.yang_name = "body"
                                                self.yang_parent_name = "ospfv2"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("router", ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router)), ("network", ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network)), ("summary", ("summary", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary)), ("external", ("external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External)), ("opaque", ("opaque", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque))])
                                                self._leafs = OrderedDict()

                                                self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router()
                                                self.router.parent = self
                                                self._children_name_map["router"] = "router"

                                                self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network()
                                                self.network.parent = self
                                                self._children_name_map["network"] = "network"

                                                self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary()
                                                self.summary.parent = self
                                                self._children_name_map["summary"] = "summary"

                                                self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External()
                                                self.external.parent = self
                                                self._children_name_map["external"] = "external"

                                                self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque()
                                                self.opaque.parent = self
                                                self._children_name_map["opaque"] = "opaque"
                                                self._segment_path = lambda: "body"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body, [], name, value)


                                            class Router(Entity):
                                                """
                                                Router LSA.
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Flags>`
                                                
                                                .. attribute:: num_of_links
                                                
                                                	Number of links
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: link
                                                
                                                	Router LSA link
                                                	**type**\: list of  		 :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router, self).__init__()

                                                    self.yang_name = "router"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link))])
                                                    self._leafs = OrderedDict([
                                                        ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                        ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                                    ])
                                                    self.flags = Bits()
                                                    self.num_of_links = None

                                                    self.link = YList(self)
                                                    self._segment_path = lambda: "router"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router, ['flags', 'num_of_links'], name, value)


                                                class Link(Entity):
                                                    """
                                                    Router LSA link.
                                                    
                                                    .. attribute:: link_id  (key)
                                                    
                                                    	Link ID
                                                    	**type**\: union of the below types:
                                                    
                                                    		**type**\: str
                                                    
                                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    		**type**\: str
                                                    
                                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    .. attribute:: link_data  (key)
                                                    
                                                    	Link data
                                                    	**type**\: union of the below types:
                                                    
                                                    		**type**\: str
                                                    
                                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    		**type**\: int
                                                    
                                                    			**range:** 0..4294967295
                                                    
                                                    .. attribute:: type
                                                    
                                                    	Link type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: topology
                                                    
                                                    	Topology specific information
                                                    	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link, self).__init__()

                                                        self.yang_name = "link"
                                                        self.yang_parent_name = "router"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['link_id','link_data']
                                                        self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology))])
                                                        self._leafs = OrderedDict([
                                                            ('link_id', (YLeaf(YType.str, 'link-id'), ['str','str'])),
                                                            ('link_data', (YLeaf(YType.str, 'link-data'), ['str','int'])),
                                                            ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                                        ])
                                                        self.link_id = None
                                                        self.link_data = None
                                                        self.type = None

                                                        self.topology = YList(self)
                                                        self._segment_path = lambda: "link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link, ['link_id', 'link_data', 'type'], name, value)


                                                    class Topology(Entity):
                                                        """
                                                        Topology specific information.
                                                        
                                                        .. attribute:: mt_id  (key)
                                                        
                                                        	The MT\-ID for topology enabled on the link
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..255
                                                        
                                                        .. attribute:: metric
                                                        
                                                        	Metric for the topology
                                                        	**type**\: int
                                                        
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
                                                            self.ylist_key_names = ['mt_id']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                                            ])
                                                            self.mt_id = None
                                                            self.metric = None
                                                            self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology, ['mt_id', 'metric'], name, value)


                                            class Network(Entity):
                                                """
                                                Network LSA.
                                                
                                                .. attribute:: network_mask
                                                
                                                	The IP address mask for the network
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: attached_router
                                                
                                                	List of the routers attached to the network
                                                	**type**\: list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network, self).__init__()

                                                    self.yang_name = "network"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                        ('attached_router', (YLeafList(YType.str, 'attached-router'), ['str'])),
                                                    ])
                                                    self.network_mask = None
                                                    self.attached_router = []
                                                    self._segment_path = lambda: "network"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network, ['network_mask', 'attached_router'], name, value)


                                            class Summary(Entity):
                                                """
                                                Summary LSA.
                                                
                                                .. attribute:: network_mask
                                                
                                                	The IP address mask for the network
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: topology
                                                
                                                	Topology specific information
                                                	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary, self).__init__()

                                                    self.yang_name = "summary"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology))])
                                                    self._leafs = OrderedDict([
                                                        ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                    ])
                                                    self.network_mask = None

                                                    self.topology = YList(self)
                                                    self._segment_path = lambda: "summary"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary, ['network_mask'], name, value)


                                                class Topology(Entity):
                                                    """
                                                    Topology specific information.
                                                    
                                                    .. attribute:: mt_id  (key)
                                                    
                                                    	The MT\-ID for topology enabled on the link
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric for the topology
                                                    	**type**\: int
                                                    
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
                                                        self.ylist_key_names = ['mt_id']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ])
                                                        self.mt_id = None
                                                        self.metric = None
                                                        self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology, ['mt_id', 'metric'], name, value)


                                            class External(Entity):
                                                """
                                                External LSA.
                                                
                                                .. attribute:: network_mask
                                                
                                                	The IP address mask for the network
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: topology
                                                
                                                	Topology specific information
                                                	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External, self).__init__()

                                                    self.yang_name = "external"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology))])
                                                    self._leafs = OrderedDict([
                                                        ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                    ])
                                                    self.network_mask = None

                                                    self.topology = YList(self)
                                                    self._segment_path = lambda: "external"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External, ['network_mask'], name, value)


                                                class Topology(Entity):
                                                    """
                                                    Topology specific information.
                                                    
                                                    .. attribute:: mt_id  (key)
                                                    
                                                    	The MT\-ID for topology enabled on the link
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: flags
                                                    
                                                    	Flags
                                                    	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology.Flags>`
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric for the topology
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    .. attribute:: forwarding_address
                                                    
                                                    	Forwarding address
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: external_route_tag
                                                    
                                                    	Route tag
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology, self).__init__()

                                                        self.yang_name = "topology"
                                                        self.yang_parent_name = "external"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['mt_id']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                            ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                            ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                            ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                        ])
                                                        self.mt_id = None
                                                        self.flags = Bits()
                                                        self.metric = None
                                                        self.forwarding_address = None
                                                        self.external_route_tag = None
                                                        self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology, ['mt_id', 'flags', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                                            class Opaque(Entity):
                                                """
                                                Opaque LSA.
                                                
                                                .. attribute:: unknown_tlv
                                                
                                                	Unknown TLV
                                                	**type**\: list of  		 :py:class:`UnknownTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv>`
                                                
                                                .. attribute:: router_address_tlv
                                                
                                                	Router address TLV
                                                	**type**\:  :py:class:`RouterAddressTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv>`
                                                
                                                .. attribute:: link_tlv
                                                
                                                	Link TLV
                                                	**type**\:  :py:class:`LinkTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque, self).__init__()

                                                    self.yang_name = "opaque"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("unknown-tlv", ("unknown_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv)), ("router-address-tlv", ("router_address_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv)), ("link-tlv", ("link_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv))])
                                                    self._leafs = OrderedDict()

                                                    self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                    self.router_address_tlv.parent = self
                                                    self._children_name_map["router_address_tlv"] = "router-address-tlv"

                                                    self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                    self.link_tlv.parent = self
                                                    self._children_name_map["link_tlv"] = "link-tlv"

                                                    self.unknown_tlv = YList(self)
                                                    self._segment_path = lambda: "opaque"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque, [], name, value)


                                                class UnknownTlv(Entity):
                                                    """
                                                    Unknown TLV.
                                                    
                                                    .. attribute:: type  (key)
                                                    
                                                    	TLV type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: length
                                                    
                                                    	TLV length
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: value
                                                    
                                                    	TLV value
                                                    	**type**\: str
                                                    
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
                                                        self.ylist_key_names = ['type']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                            ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                                        ])
                                                        self.type = None
                                                        self.length = None
                                                        self.value = None
                                                        self._segment_path = lambda: "unknown-tlv" + "[type='" + str(self.type) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, ['type', 'length', 'value'], name, value)


                                                class RouterAddressTlv(Entity):
                                                    """
                                                    Router address TLV.
                                                    
                                                    .. attribute:: router_address
                                                    
                                                    	Router address
                                                    	**type**\: str
                                                    
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
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('router_address', (YLeaf(YType.str, 'router-address'), ['str'])),
                                                        ])
                                                        self.router_address = None
                                                        self._segment_path = lambda: "router-address-tlv"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, ['router_address'], name, value)


                                                class LinkTlv(Entity):
                                                    """
                                                    Link TLV.
                                                    
                                                    .. attribute:: link_type
                                                    
                                                    	Link type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: link_id
                                                    
                                                    	Link ID
                                                    	**type**\: union of the below types:
                                                    
                                                    		**type**\: str
                                                    
                                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    		**type**\: str
                                                    
                                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: local_if_ipv4_addr
                                                    
                                                    	List of local interface IPv4 addresses
                                                    	**type**\: list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: local_remote_ipv4_addr
                                                    
                                                    	List of remote interface IPv4 addresses
                                                    	**type**\: list of str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                    
                                                    .. attribute:: te_metric
                                                    
                                                    	TE metric
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: max_bandwidth
                                                    
                                                    	Maximum bandwidth
                                                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                    
                                                    	**range:** \-92233720368547758.08..92233720368547758.07
                                                    
                                                    .. attribute:: max_reservable_bandwidth
                                                    
                                                    	Maximum reservable bandwidth
                                                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                    
                                                    	**range:** \-92233720368547758.08..92233720368547758.07
                                                    
                                                    .. attribute:: unreserved_bandwidth
                                                    
                                                    	Unreserved bandwidth
                                                    	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                    
                                                    	**range:** \-92233720368547758.08..92233720368547758.07
                                                    
                                                    .. attribute:: admin_group
                                                    
                                                    	Administrative group/Resource class/Color
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: unknown_subtlv
                                                    
                                                    	Unknown sub\-TLV
                                                    	**type**\: list of  		 :py:class:`UnknownSubtlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv, self).__init__()

                                                        self.yang_name = "link-tlv"
                                                        self.yang_parent_name = "opaque"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = []
                                                        self._child_classes = OrderedDict([("unknown-subtlv", ("unknown_subtlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv))])
                                                        self._leafs = OrderedDict([
                                                            ('link_type', (YLeaf(YType.uint8, 'link-type'), ['int'])),
                                                            ('link_id', (YLeaf(YType.str, 'link-id'), ['str','str'])),
                                                            ('local_if_ipv4_addr', (YLeafList(YType.str, 'local-if-ipv4-addr'), ['str'])),
                                                            ('local_remote_ipv4_addr', (YLeafList(YType.str, 'local-remote-ipv4-addr'), ['str'])),
                                                            ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                                                            ('max_bandwidth', (YLeaf(YType.str, 'max-bandwidth'), ['Decimal64'])),
                                                            ('max_reservable_bandwidth', (YLeaf(YType.str, 'max-reservable-bandwidth'), ['Decimal64'])),
                                                            ('unreserved_bandwidth', (YLeaf(YType.str, 'unreserved-bandwidth'), ['Decimal64'])),
                                                            ('admin_group', (YLeaf(YType.uint32, 'admin-group'), ['int'])),
                                                        ])
                                                        self.link_type = None
                                                        self.link_id = None
                                                        self.local_if_ipv4_addr = []
                                                        self.local_remote_ipv4_addr = []
                                                        self.te_metric = None
                                                        self.max_bandwidth = None
                                                        self.max_reservable_bandwidth = None
                                                        self.unreserved_bandwidth = None
                                                        self.admin_group = None

                                                        self.unknown_subtlv = YList(self)
                                                        self._segment_path = lambda: "link-tlv"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv, ['link_type', 'link_id', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'te_metric', 'max_bandwidth', 'max_reservable_bandwidth', 'unreserved_bandwidth', 'admin_group'], name, value)


                                                    class UnknownSubtlv(Entity):
                                                        """
                                                        Unknown sub\-TLV.
                                                        
                                                        .. attribute:: type  (key)
                                                        
                                                        	TLV type
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: length
                                                        
                                                        	TLV length
                                                        	**type**\: int
                                                        
                                                        	**range:** 0..65535
                                                        
                                                        .. attribute:: value
                                                        
                                                        	TLV value
                                                        	**type**\: str
                                                        
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
                                                            self.ylist_key_names = ['type']
                                                            self._child_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                                            ])
                                                            self.type = None
                                                            self.length = None
                                                            self.value = None
                                                            self._segment_path = lambda: "unknown-subtlv" + "[type='" + str(self.type) + "']"
                                                            self._is_frozen = True

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, ['type', 'length', 'value'], name, value)


                                    class Ospfv3(Entity):
                                        """
                                        OSPFv3 LSA
                                        
                                        .. attribute:: header
                                        
                                        	Decoded OSPFv3 LSA header data
                                        	**type**\:  :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header>`
                                        
                                        .. attribute:: body
                                        
                                        	Decoded OSPF LSA body data
                                        	**type**\:  :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3, self).__init__()

                                            self.yang_name = "ospfv3"
                                            self.yang_parent_name = "area-scope-lsa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("header", ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header)), ("body", ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body))])
                                            self._leafs = OrderedDict()

                                            self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header()
                                            self.header.parent = self
                                            self._children_name_map["header"] = "header"

                                            self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body()
                                            self.body.parent = self
                                            self._children_name_map["body"] = "body"
                                            self._segment_path = lambda: "ospfv3"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3, [], name, value)


                                        class Header(Entity):
                                            """
                                            Decoded OSPFv3 LSA header data.
                                            
                                            .. attribute:: lsa_id
                                            
                                            	LSA ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: age
                                            
                                            	LSA age
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: type
                                            
                                            	LSA type
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: adv_router
                                            
                                            	LSA advertising router
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: seq_num
                                            
                                            	LSA sequence number
                                            	**type**\: str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: checksum
                                            
                                            	LSA checksum
                                            	**type**\: str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: length
                                            
                                            	LSA length
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header.Options>`
                                            
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
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('lsa_id', (YLeaf(YType.uint32, 'lsa-id'), ['int'])),
                                                    ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                    ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                    ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                                    ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                    ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                    ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                    ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                ])
                                                self.lsa_id = None
                                                self.age = None
                                                self.type = None
                                                self.adv_router = None
                                                self.seq_num = None
                                                self.checksum = None
                                                self.length = None
                                                self.options = Bits()
                                                self._segment_path = lambda: "header"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header, ['lsa_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'options'], name, value)


                                        class Body(Entity):
                                            """
                                            Decoded OSPF LSA body data.
                                            
                                            .. attribute:: router
                                            
                                            	Router LSA
                                            	**type**\:  :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router>`
                                            
                                            .. attribute:: network
                                            
                                            	Network LSA
                                            	**type**\:  :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network>`
                                            
                                            .. attribute:: inter_area_prefix
                                            
                                            	Inter\-Area\-Prefix LSA
                                            	**type**\:  :py:class:`InterAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix>`
                                            
                                            .. attribute:: inter_area_router
                                            
                                            	Inter\-Area\-Router LSA
                                            	**type**\:  :py:class:`InterAreaRouter <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter>`
                                            
                                            .. attribute:: as_external
                                            
                                            	AS\-External LSA
                                            	**type**\:  :py:class:`AsExternal <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal>`
                                            
                                            .. attribute:: nssa
                                            
                                            	NSSA LSA
                                            	**type**\:  :py:class:`Nssa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa>`
                                            
                                            .. attribute:: link
                                            
                                            	Link LSA
                                            	**type**\:  :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link>`
                                            
                                            .. attribute:: intra_area_prefix
                                            
                                            	Intra\-Area\-Prefix LSA
                                            	**type**\:  :py:class:`IntraAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body, self).__init__()

                                                self.yang_name = "body"
                                                self.yang_parent_name = "ospfv3"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("router", ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router)), ("network", ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network)), ("inter-area-prefix", ("inter_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix)), ("inter-area-router", ("inter_area_router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter)), ("as-external", ("as_external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal)), ("nssa", ("nssa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa)), ("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link)), ("intra-area-prefix", ("intra_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix))])
                                                self._leafs = OrderedDict()

                                                self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router()
                                                self.router.parent = self
                                                self._children_name_map["router"] = "router"

                                                self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network()
                                                self.network.parent = self
                                                self._children_name_map["network"] = "network"

                                                self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                                self.inter_area_prefix.parent = self
                                                self._children_name_map["inter_area_prefix"] = "inter-area-prefix"

                                                self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter()
                                                self.inter_area_router.parent = self
                                                self._children_name_map["inter_area_router"] = "inter-area-router"

                                                self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal()
                                                self.as_external.parent = self
                                                self._children_name_map["as_external"] = "as-external"

                                                self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa()
                                                self.nssa.parent = self
                                                self._children_name_map["nssa"] = "nssa"

                                                self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link()
                                                self.link.parent = self
                                                self._children_name_map["link"] = "link"

                                                self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                                self.intra_area_prefix.parent = self
                                                self._children_name_map["intra_area_prefix"] = "intra-area-prefix"
                                                self._segment_path = lambda: "body"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body, [], name, value)


                                            class Router(Entity):
                                                """
                                                Router LSA.
                                                
                                                .. attribute:: flags
                                                
                                                	LSA option
                                                	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Flags>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: link
                                                
                                                	Router LSA link
                                                	**type**\: list of  		 :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router, self).__init__()

                                                    self.yang_name = "router"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link))])
                                                    self._leafs = OrderedDict([
                                                        ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                        ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                    ])
                                                    self.flags = Bits()
                                                    self.options = Bits()

                                                    self.link = YList(self)
                                                    self._segment_path = lambda: "router"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router, ['flags', 'options'], name, value)


                                                class Link(Entity):
                                                    """
                                                    Router LSA link.
                                                    
                                                    .. attribute:: interface_id  (key)
                                                    
                                                    	Interface ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: neighbor_interface_id  (key)
                                                    
                                                    	Neighbor Interface ID
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: neighbor_router_id  (key)
                                                    
                                                    	Neighbor Router ID
                                                    	**type**\: str
                                                    
                                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                    
                                                    .. attribute:: type
                                                    
                                                    	Link type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link, self).__init__()

                                                        self.yang_name = "link"
                                                        self.yang_parent_name = "router"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                                            ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                                            ('neighbor_router_id', (YLeaf(YType.str, 'neighbor-router-id'), ['str'])),
                                                            ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                                            ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                                        ])
                                                        self.interface_id = None
                                                        self.neighbor_interface_id = None
                                                        self.neighbor_router_id = None
                                                        self.type = None
                                                        self.metric = None
                                                        self._segment_path = lambda: "link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                                            class Network(Entity):
                                                """
                                                Network LSA.
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: attached_router
                                                
                                                	List of the routers attached to the network
                                                	**type**\: list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network, self).__init__()

                                                    self.yang_name = "network"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                        ('attached_router', (YLeafList(YType.str, 'attached-router'), ['str'])),
                                                    ])
                                                    self.options = Bits()
                                                    self.attached_router = []
                                                    self._segment_path = lambda: "network"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network, ['options', 'attached_router'], name, value)


                                            class InterAreaPrefix(Entity):
                                                """
                                                Inter\-Area\-Prefix LSA.
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: prefix
                                                
                                                	Prefix
                                                	**type**\: str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\: str
                                                
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
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                        ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                    ])
                                                    self.metric = None
                                                    self.prefix = None
                                                    self.prefix_options = None
                                                    self._segment_path = lambda: "inter-area-prefix"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix, ['metric', 'prefix', 'prefix_options'], name, value)


                                            class InterAreaRouter(Entity):
                                                """
                                                Inter\-Area\-Router LSA.
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: destination_router_id
                                                
                                                	The Router ID of the router being described by the LSA
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter, self).__init__()

                                                    self.yang_name = "inter-area-router"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ('destination_router_id', (YLeaf(YType.str, 'destination-router-id'), ['str'])),
                                                    ])
                                                    self.options = Bits()
                                                    self.metric = None
                                                    self.destination_router_id = None
                                                    self._segment_path = lambda: "inter-area-router"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter, ['options', 'metric', 'destination_router_id'], name, value)


                                            class AsExternal(Entity):
                                                """
                                                AS\-External LSA.
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal.Flags>`
                                                
                                                .. attribute:: referenced_ls_type
                                                
                                                	Referenced Link State type
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: prefix
                                                
                                                	Prefix
                                                	**type**\: str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\: str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: forwarding_address
                                                
                                                	Forwarding address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: external_route_tag
                                                
                                                	Route tag
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: referenced_link_state_id
                                                
                                                	Referenced Link State ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal, self).__init__()

                                                    self.yang_name = "as-external"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                        ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                        ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                        ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                        ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                        ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                    ])
                                                    self.metric = None
                                                    self.flags = Bits()
                                                    self.referenced_ls_type = None
                                                    self.prefix = None
                                                    self.prefix_options = None
                                                    self.forwarding_address = None
                                                    self.external_route_tag = None
                                                    self.referenced_link_state_id = None
                                                    self._segment_path = lambda: "as-external"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal, ['metric', 'flags', 'referenced_ls_type', 'prefix', 'prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                            class Nssa(Entity):
                                                """
                                                NSSA LSA.
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa.Flags>`
                                                
                                                .. attribute:: referenced_ls_type
                                                
                                                	Referenced Link State type
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: prefix
                                                
                                                	Prefix
                                                	**type**\: str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\: str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: forwarding_address
                                                
                                                	Forwarding address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: external_route_tag
                                                
                                                	Route tag
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: referenced_link_state_id
                                                
                                                	Referenced Link State ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa, self).__init__()

                                                    self.yang_name = "nssa"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                        ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                        ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                        ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                        ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                        ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                    ])
                                                    self.metric = None
                                                    self.flags = Bits()
                                                    self.referenced_ls_type = None
                                                    self.prefix = None
                                                    self.prefix_options = None
                                                    self.forwarding_address = None
                                                    self.external_route_tag = None
                                                    self.referenced_link_state_id = None
                                                    self._segment_path = lambda: "nssa"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa, ['metric', 'flags', 'referenced_ls_type', 'prefix', 'prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                            class Link(Entity):
                                                """
                                                Link LSA.
                                                
                                                .. attribute:: rtr_priority
                                                
                                                	Router Priority of the interface
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: options
                                                
                                                	OSPFv3 LSA options
                                                	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.Options>`
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: link_local_interface_address
                                                
                                                	The originating router's link\-local interface address on the link
                                                	**type**\: union of the below types:
                                                
                                                		**type**\: str
                                                
                                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                		**type**\: str
                                                
                                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: num_of_prefixes
                                                
                                                	Number of prefixes
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: prefix_list
                                                
                                                	List of prefixes associated with the link
                                                	**type**\: list of  		 :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link, self).__init__()

                                                    self.yang_name = "link"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("prefix-list", ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList))])
                                                    self._leafs = OrderedDict([
                                                        ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                                        ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                        ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                                        ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                                    ])
                                                    self.rtr_priority = None
                                                    self.options = Bits()
                                                    self.link_local_interface_address = None
                                                    self.num_of_prefixes = None

                                                    self.prefix_list = YList(self)
                                                    self._segment_path = lambda: "link"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link, ['rtr_priority', 'options', 'link_local_interface_address', 'num_of_prefixes'], name, value)


                                                class PrefixList(Entity):
                                                    """
                                                    List of prefixes associated with the link.
                                                    
                                                    .. attribute:: prefix  (key)
                                                    
                                                    	Prefix
                                                    	**type**\: str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\: str
                                                    
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
                                                        self.ylist_key_names = ['prefix']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                            ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                        ])
                                                        self.prefix = None
                                                        self.prefix_options = None
                                                        self._segment_path = lambda: "prefix-list" + "[prefix='" + str(self.prefix) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList, ['prefix', 'prefix_options'], name, value)


                                            class IntraAreaPrefix(Entity):
                                                """
                                                Intra\-Area\-Prefix LSA.
                                                
                                                .. attribute:: referenced_ls_type
                                                
                                                	Referenced Link State type
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: referenced_link_state_id
                                                
                                                	Referenced Link State ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: referenced_adv_router
                                                
                                                	Referenced Advertising Router
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: num_of_prefixes
                                                
                                                	Number of prefixes
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: prefix_list
                                                
                                                	List of prefixes associated with the link
                                                	**type**\: list of  		 :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix, self).__init__()

                                                    self.yang_name = "intra-area-prefix"
                                                    self.yang_parent_name = "body"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("prefix-list", ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList))])
                                                    self._leafs = OrderedDict([
                                                        ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                        ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                        ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str'])),
                                                        ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                                    ])
                                                    self.referenced_ls_type = None
                                                    self.referenced_link_state_id = None
                                                    self.referenced_adv_router = None
                                                    self.num_of_prefixes = None

                                                    self.prefix_list = YList(self)
                                                    self._segment_path = lambda: "intra-area-prefix"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                                                class PrefixList(Entity):
                                                    """
                                                    List of prefixes associated with the link.
                                                    
                                                    .. attribute:: prefix  (key)
                                                    
                                                    	Prefix
                                                    	**type**\: str
                                                    
                                                    .. attribute:: prefix_options
                                                    
                                                    	Prefix options
                                                    	**type**\: str
                                                    
                                                    	**mandatory**\: True
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..16777215
                                                    
                                                    

                                                    """

                                                    _prefix = 'ospf'
                                                    _revision = '2015-03-09'

                                                    def __init__(self):
                                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, self).__init__()

                                                        self.yang_name = "prefix-list"
                                                        self.yang_parent_name = "intra-area-prefix"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['prefix']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                            ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ])
                                                        self.prefix = None
                                                        self.prefix_options = None
                                                        self.metric = None
                                                        self._segment_path = lambda: "prefix-list" + "[prefix='" + str(self.prefix) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, ['prefix', 'prefix_options', 'metric'], name, value)


                        class AsScopeLsas(Entity):
                            """
                            List OSPF AS scope LSA databases
                            
                            .. attribute:: lsa_type  (key)
                            
                            	OSPF AS scope LSA type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: as_scope_lsa
                            
                            	List of OSPF AS scope LSAs
                            	**type**\: list of  		 :py:class:`AsScopeLsa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas, self).__init__()

                                self.yang_name = "as-scope-lsas"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['lsa_type']
                                self._child_classes = OrderedDict([("as-scope-lsa", ("as_scope_lsa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa))])
                                self._leafs = OrderedDict([
                                    ('lsa_type', (YLeaf(YType.uint8, 'lsa-type'), ['int'])),
                                ])
                                self.lsa_type = None

                                self.as_scope_lsa = YList(self)
                                self._segment_path = lambda: "as-scope-lsas" + "[lsa-type='" + str(self.lsa_type) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas, ['lsa_type'], name, value)


                            class AsScopeLsa(Entity):
                                """
                                List of OSPF AS scope LSAs
                                
                                .. attribute:: lsa_id  (key)
                                
                                	LSA ID
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: int
                                
                                			**range:** 0..4294967295
                                
                                .. attribute:: adv_router  (key)
                                
                                	Advertising router
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: decoded_completed
                                
                                	The OSPF LSA body is fully decoded
                                	**type**\: bool
                                
                                .. attribute:: raw_data
                                
                                	The complete LSA in network byte order as received/sent over the wire
                                	**type**\: str
                                
                                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                                
                                .. attribute:: ospfv2
                                
                                	OSPFv2 LSA
                                	**type**\:  :py:class:`Ospfv2 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2>`
                                
                                .. attribute:: ospfv3
                                
                                	OSPFv3 LSA
                                	**type**\:  :py:class:`Ospfv3 <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa, self).__init__()

                                    self.yang_name = "as-scope-lsa"
                                    self.yang_parent_name = "as-scope-lsas"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['lsa_id','adv_router']
                                    self._child_classes = OrderedDict([("ospfv2", ("ospfv2", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2)), ("ospfv3", ("ospfv3", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3))])
                                    self._leafs = OrderedDict([
                                        ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','int'])),
                                        ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                        ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                                        ('raw_data', (YLeaf(YType.str, 'raw-data'), ['str'])),
                                    ])
                                    self.lsa_id = None
                                    self.adv_router = None
                                    self.decoded_completed = None
                                    self.raw_data = None

                                    self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2()
                                    self.ospfv2.parent = self
                                    self._children_name_map["ospfv2"] = "ospfv2"

                                    self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3()
                                    self.ospfv3.parent = self
                                    self._children_name_map["ospfv3"] = "ospfv3"
                                    self._segment_path = lambda: "as-scope-lsa" + "[lsa-id='" + str(self.lsa_id) + "']" + "[adv-router='" + str(self.adv_router) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                                class Ospfv2(Entity):
                                    """
                                    OSPFv2 LSA
                                    
                                    .. attribute:: header
                                    
                                    	Decoded OSPFv2 LSA header data
                                    	**type**\:  :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header>`
                                    
                                    .. attribute:: body
                                    
                                    	Decoded OSPFv2 LSA body data
                                    	**type**\:  :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2, self).__init__()

                                        self.yang_name = "ospfv2"
                                        self.yang_parent_name = "as-scope-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("header", ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header)), ("body", ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body))])
                                        self._leafs = OrderedDict()

                                        self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header()
                                        self.header.parent = self
                                        self._children_name_map["header"] = "header"

                                        self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body()
                                        self.body.parent = self
                                        self._children_name_map["body"] = "body"
                                        self._segment_path = lambda: "ospfv2"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2, [], name, value)


                                    class Header(Entity):
                                        """
                                        Decoded OSPFv2 LSA header data.
                                        
                                        .. attribute:: options
                                        
                                        	LSA option
                                        	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header.Options>`
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: lsa_id
                                        
                                        	LSA ID
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: opaque_type
                                        
                                        	Opaque type
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: opaque_id
                                        
                                        	Opaque id
                                        	**type**\: int
                                        
                                        	**range:** 0..16777215
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: age
                                        
                                        	LSA age
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: type
                                        
                                        	LSA type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: adv_router
                                        
                                        	LSA advertising router
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: seq_num
                                        
                                        	LSA sequence number
                                        	**type**\: str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: checksum
                                        
                                        	LSA checksum
                                        	**type**\: str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: length
                                        
                                        	LSA length
                                        	**type**\: int
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str'])),
                                                ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                                ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                                ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                                ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                            ])
                                            self.options = Bits()
                                            self.lsa_id = None
                                            self.opaque_type = None
                                            self.opaque_id = None
                                            self.age = None
                                            self.type = None
                                            self.adv_router = None
                                            self.seq_num = None
                                            self.checksum = None
                                            self.length = None
                                            self._segment_path = lambda: "header"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header, ['options', 'lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                                    class Body(Entity):
                                        """
                                        Decoded OSPFv2 LSA body data.
                                        
                                        .. attribute:: router
                                        
                                        	Router LSA
                                        	**type**\:  :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router>`
                                        
                                        .. attribute:: network
                                        
                                        	Network LSA
                                        	**type**\:  :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network>`
                                        
                                        .. attribute:: summary
                                        
                                        	Summary LSA
                                        	**type**\:  :py:class:`Summary <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary>`
                                        
                                        .. attribute:: external
                                        
                                        	External LSA
                                        	**type**\:  :py:class:`External <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External>`
                                        
                                        .. attribute:: opaque
                                        
                                        	Opaque LSA
                                        	**type**\:  :py:class:`Opaque <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body, self).__init__()

                                            self.yang_name = "body"
                                            self.yang_parent_name = "ospfv2"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("router", ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router)), ("network", ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network)), ("summary", ("summary", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary)), ("external", ("external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External)), ("opaque", ("opaque", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque))])
                                            self._leafs = OrderedDict()

                                            self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router()
                                            self.router.parent = self
                                            self._children_name_map["router"] = "router"

                                            self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network()
                                            self.network.parent = self
                                            self._children_name_map["network"] = "network"

                                            self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary()
                                            self.summary.parent = self
                                            self._children_name_map["summary"] = "summary"

                                            self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External()
                                            self.external.parent = self
                                            self._children_name_map["external"] = "external"

                                            self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque()
                                            self.opaque.parent = self
                                            self._children_name_map["opaque"] = "opaque"
                                            self._segment_path = lambda: "body"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body, [], name, value)


                                        class Router(Entity):
                                            """
                                            Router LSA.
                                            
                                            .. attribute:: flags
                                            
                                            	Flags
                                            	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Flags>`
                                            
                                            .. attribute:: num_of_links
                                            
                                            	Number of links
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: link
                                            
                                            	Router LSA link
                                            	**type**\: list of  		 :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router, self).__init__()

                                                self.yang_name = "router"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link))])
                                                self._leafs = OrderedDict([
                                                    ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                    ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                                ])
                                                self.flags = Bits()
                                                self.num_of_links = None

                                                self.link = YList(self)
                                                self._segment_path = lambda: "router"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router, ['flags', 'num_of_links'], name, value)


                                            class Link(Entity):
                                                """
                                                Router LSA link.
                                                
                                                .. attribute:: link_id  (key)
                                                
                                                	Link ID
                                                	**type**\: union of the below types:
                                                
                                                		**type**\: str
                                                
                                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                		**type**\: str
                                                
                                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                .. attribute:: link_data  (key)
                                                
                                                	Link data
                                                	**type**\: union of the below types:
                                                
                                                		**type**\: str
                                                
                                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                		**type**\: int
                                                
                                                			**range:** 0..4294967295
                                                
                                                .. attribute:: type
                                                
                                                	Link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: topology
                                                
                                                	Topology specific information
                                                	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link, self).__init__()

                                                    self.yang_name = "link"
                                                    self.yang_parent_name = "router"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['link_id','link_data']
                                                    self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology))])
                                                    self._leafs = OrderedDict([
                                                        ('link_id', (YLeaf(YType.str, 'link-id'), ['str','str'])),
                                                        ('link_data', (YLeaf(YType.str, 'link-data'), ['str','int'])),
                                                        ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                                    ])
                                                    self.link_id = None
                                                    self.link_data = None
                                                    self.type = None

                                                    self.topology = YList(self)
                                                    self._segment_path = lambda: "link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link, ['link_id', 'link_data', 'type'], name, value)


                                                class Topology(Entity):
                                                    """
                                                    Topology specific information.
                                                    
                                                    .. attribute:: mt_id  (key)
                                                    
                                                    	The MT\-ID for topology enabled on the link
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..255
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric for the topology
                                                    	**type**\: int
                                                    
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
                                                        self.ylist_key_names = ['mt_id']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                            ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                                        ])
                                                        self.mt_id = None
                                                        self.metric = None
                                                        self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology, ['mt_id', 'metric'], name, value)


                                        class Network(Entity):
                                            """
                                            Network LSA.
                                            
                                            .. attribute:: network_mask
                                            
                                            	The IP address mask for the network
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: attached_router
                                            
                                            	List of the routers attached to the network
                                            	**type**\: list of str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network, self).__init__()

                                                self.yang_name = "network"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                    ('attached_router', (YLeafList(YType.str, 'attached-router'), ['str'])),
                                                ])
                                                self.network_mask = None
                                                self.attached_router = []
                                                self._segment_path = lambda: "network"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network, ['network_mask', 'attached_router'], name, value)


                                        class Summary(Entity):
                                            """
                                            Summary LSA.
                                            
                                            .. attribute:: network_mask
                                            
                                            	The IP address mask for the network
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: topology
                                            
                                            	Topology specific information
                                            	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary, self).__init__()

                                                self.yang_name = "summary"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology))])
                                                self._leafs = OrderedDict([
                                                    ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                ])
                                                self.network_mask = None

                                                self.topology = YList(self)
                                                self._segment_path = lambda: "summary"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary, ['network_mask'], name, value)


                                            class Topology(Entity):
                                                """
                                                Topology specific information.
                                                
                                                .. attribute:: mt_id  (key)
                                                
                                                	The MT\-ID for topology enabled on the link
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: metric
                                                
                                                	Metric for the topology
                                                	**type**\: int
                                                
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
                                                    self.ylist_key_names = ['mt_id']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ])
                                                    self.mt_id = None
                                                    self.metric = None
                                                    self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology, ['mt_id', 'metric'], name, value)


                                        class External(Entity):
                                            """
                                            External LSA.
                                            
                                            .. attribute:: network_mask
                                            
                                            	The IP address mask for the network
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: topology
                                            
                                            	Topology specific information
                                            	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External, self).__init__()

                                                self.yang_name = "external"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("topology", ("topology", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology))])
                                                self._leafs = OrderedDict([
                                                    ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str'])),
                                                ])
                                                self.network_mask = None

                                                self.topology = YList(self)
                                                self._segment_path = lambda: "external"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External, ['network_mask'], name, value)


                                            class Topology(Entity):
                                                """
                                                Topology specific information.
                                                
                                                .. attribute:: mt_id  (key)
                                                
                                                	The MT\-ID for topology enabled on the link
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: flags
                                                
                                                	Flags
                                                	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology.Flags>`
                                                
                                                .. attribute:: metric
                                                
                                                	Metric for the topology
                                                	**type**\: int
                                                
                                                	**range:** 0..16777215
                                                
                                                .. attribute:: forwarding_address
                                                
                                                	Forwarding address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: external_route_tag
                                                
                                                	Route tag
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology, self).__init__()

                                                    self.yang_name = "topology"
                                                    self.yang_parent_name = "external"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['mt_id']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                                        ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                        ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                        ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                    ])
                                                    self.mt_id = None
                                                    self.flags = Bits()
                                                    self.metric = None
                                                    self.forwarding_address = None
                                                    self.external_route_tag = None
                                                    self._segment_path = lambda: "topology" + "[mt-id='" + str(self.mt_id) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology, ['mt_id', 'flags', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                                        class Opaque(Entity):
                                            """
                                            Opaque LSA.
                                            
                                            .. attribute:: unknown_tlv
                                            
                                            	Unknown TLV
                                            	**type**\: list of  		 :py:class:`UnknownTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv>`
                                            
                                            .. attribute:: router_address_tlv
                                            
                                            	Router address TLV
                                            	**type**\:  :py:class:`RouterAddressTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv>`
                                            
                                            .. attribute:: link_tlv
                                            
                                            	Link TLV
                                            	**type**\:  :py:class:`LinkTlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque, self).__init__()

                                                self.yang_name = "opaque"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("unknown-tlv", ("unknown_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv)), ("router-address-tlv", ("router_address_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv)), ("link-tlv", ("link_tlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv))])
                                                self._leafs = OrderedDict()

                                                self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                self.router_address_tlv.parent = self
                                                self._children_name_map["router_address_tlv"] = "router-address-tlv"

                                                self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                self.link_tlv.parent = self
                                                self._children_name_map["link_tlv"] = "link-tlv"

                                                self.unknown_tlv = YList(self)
                                                self._segment_path = lambda: "opaque"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque, [], name, value)


                                            class UnknownTlv(Entity):
                                                """
                                                Unknown TLV.
                                                
                                                .. attribute:: type  (key)
                                                
                                                	TLV type
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: length
                                                
                                                	TLV length
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                .. attribute:: value
                                                
                                                	TLV value
                                                	**type**\: str
                                                
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
                                                    self.ylist_key_names = ['type']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                        ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                                    ])
                                                    self.type = None
                                                    self.length = None
                                                    self.value = None
                                                    self._segment_path = lambda: "unknown-tlv" + "[type='" + str(self.type) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv, ['type', 'length', 'value'], name, value)


                                            class RouterAddressTlv(Entity):
                                                """
                                                Router address TLV.
                                                
                                                .. attribute:: router_address
                                                
                                                	Router address
                                                	**type**\: str
                                                
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
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('router_address', (YLeaf(YType.str, 'router-address'), ['str'])),
                                                    ])
                                                    self.router_address = None
                                                    self._segment_path = lambda: "router-address-tlv"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv, ['router_address'], name, value)


                                            class LinkTlv(Entity):
                                                """
                                                Link TLV.
                                                
                                                .. attribute:: link_type
                                                
                                                	Link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: link_id
                                                
                                                	Link ID
                                                	**type**\: union of the below types:
                                                
                                                		**type**\: str
                                                
                                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                		**type**\: str
                                                
                                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: local_if_ipv4_addr
                                                
                                                	List of local interface IPv4 addresses
                                                	**type**\: list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: local_remote_ipv4_addr
                                                
                                                	List of remote interface IPv4 addresses
                                                	**type**\: list of str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: te_metric
                                                
                                                	TE metric
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: max_bandwidth
                                                
                                                	Maximum bandwidth
                                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                
                                                	**range:** \-92233720368547758.08..92233720368547758.07
                                                
                                                .. attribute:: max_reservable_bandwidth
                                                
                                                	Maximum reservable bandwidth
                                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                
                                                	**range:** \-92233720368547758.08..92233720368547758.07
                                                
                                                .. attribute:: unreserved_bandwidth
                                                
                                                	Unreserved bandwidth
                                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                                
                                                	**range:** \-92233720368547758.08..92233720368547758.07
                                                
                                                .. attribute:: admin_group
                                                
                                                	Administrative group/Resource class/Color
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: unknown_subtlv
                                                
                                                	Unknown sub\-TLV
                                                	**type**\: list of  		 :py:class:`UnknownSubtlv <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv>`
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv, self).__init__()

                                                    self.yang_name = "link-tlv"
                                                    self.yang_parent_name = "opaque"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([("unknown-subtlv", ("unknown_subtlv", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv))])
                                                    self._leafs = OrderedDict([
                                                        ('link_type', (YLeaf(YType.uint8, 'link-type'), ['int'])),
                                                        ('link_id', (YLeaf(YType.str, 'link-id'), ['str','str'])),
                                                        ('local_if_ipv4_addr', (YLeafList(YType.str, 'local-if-ipv4-addr'), ['str'])),
                                                        ('local_remote_ipv4_addr', (YLeafList(YType.str, 'local-remote-ipv4-addr'), ['str'])),
                                                        ('te_metric', (YLeaf(YType.uint32, 'te-metric'), ['int'])),
                                                        ('max_bandwidth', (YLeaf(YType.str, 'max-bandwidth'), ['Decimal64'])),
                                                        ('max_reservable_bandwidth', (YLeaf(YType.str, 'max-reservable-bandwidth'), ['Decimal64'])),
                                                        ('unreserved_bandwidth', (YLeaf(YType.str, 'unreserved-bandwidth'), ['Decimal64'])),
                                                        ('admin_group', (YLeaf(YType.uint32, 'admin-group'), ['int'])),
                                                    ])
                                                    self.link_type = None
                                                    self.link_id = None
                                                    self.local_if_ipv4_addr = []
                                                    self.local_remote_ipv4_addr = []
                                                    self.te_metric = None
                                                    self.max_bandwidth = None
                                                    self.max_reservable_bandwidth = None
                                                    self.unreserved_bandwidth = None
                                                    self.admin_group = None

                                                    self.unknown_subtlv = YList(self)
                                                    self._segment_path = lambda: "link-tlv"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv, ['link_type', 'link_id', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'te_metric', 'max_bandwidth', 'max_reservable_bandwidth', 'unreserved_bandwidth', 'admin_group'], name, value)


                                                class UnknownSubtlv(Entity):
                                                    """
                                                    Unknown sub\-TLV.
                                                    
                                                    .. attribute:: type  (key)
                                                    
                                                    	TLV type
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: length
                                                    
                                                    	TLV length
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..65535
                                                    
                                                    .. attribute:: value
                                                    
                                                    	TLV value
                                                    	**type**\: str
                                                    
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
                                                        self.ylist_key_names = ['type']
                                                        self._child_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                            ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                                                        ])
                                                        self.type = None
                                                        self.length = None
                                                        self.value = None
                                                        self._segment_path = lambda: "unknown-subtlv" + "[type='" + str(self.type) + "']"
                                                        self._is_frozen = True

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv, ['type', 'length', 'value'], name, value)


                                class Ospfv3(Entity):
                                    """
                                    OSPFv3 LSA
                                    
                                    .. attribute:: header
                                    
                                    	Decoded OSPFv3 LSA header data
                                    	**type**\:  :py:class:`Header <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header>`
                                    
                                    .. attribute:: body
                                    
                                    	Decoded OSPF LSA body data
                                    	**type**\:  :py:class:`Body <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3, self).__init__()

                                        self.yang_name = "ospfv3"
                                        self.yang_parent_name = "as-scope-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("header", ("header", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header)), ("body", ("body", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body))])
                                        self._leafs = OrderedDict()

                                        self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header()
                                        self.header.parent = self
                                        self._children_name_map["header"] = "header"

                                        self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body()
                                        self.body.parent = self
                                        self._children_name_map["body"] = "body"
                                        self._segment_path = lambda: "ospfv3"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3, [], name, value)


                                    class Header(Entity):
                                        """
                                        Decoded OSPFv3 LSA header data.
                                        
                                        .. attribute:: lsa_id
                                        
                                        	LSA ID
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: age
                                        
                                        	LSA age
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: type
                                        
                                        	LSA type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: adv_router
                                        
                                        	LSA advertising router
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: seq_num
                                        
                                        	LSA sequence number
                                        	**type**\: str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: checksum
                                        
                                        	LSA checksum
                                        	**type**\: str
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: length
                                        
                                        	LSA length
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: options
                                        
                                        	OSPFv3 LSA options
                                        	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header.Options>`
                                        
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
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('lsa_id', (YLeaf(YType.uint32, 'lsa-id'), ['int'])),
                                                ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str'])),
                                                ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                                ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                            ])
                                            self.lsa_id = None
                                            self.age = None
                                            self.type = None
                                            self.adv_router = None
                                            self.seq_num = None
                                            self.checksum = None
                                            self.length = None
                                            self.options = Bits()
                                            self._segment_path = lambda: "header"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header, ['lsa_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'options'], name, value)


                                    class Body(Entity):
                                        """
                                        Decoded OSPF LSA body data.
                                        
                                        .. attribute:: router
                                        
                                        	Router LSA
                                        	**type**\:  :py:class:`Router <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router>`
                                        
                                        .. attribute:: network
                                        
                                        	Network LSA
                                        	**type**\:  :py:class:`Network <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network>`
                                        
                                        .. attribute:: inter_area_prefix
                                        
                                        	Inter\-Area\-Prefix LSA
                                        	**type**\:  :py:class:`InterAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix>`
                                        
                                        .. attribute:: inter_area_router
                                        
                                        	Inter\-Area\-Router LSA
                                        	**type**\:  :py:class:`InterAreaRouter <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter>`
                                        
                                        .. attribute:: as_external
                                        
                                        	AS\-External LSA
                                        	**type**\:  :py:class:`AsExternal <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal>`
                                        
                                        .. attribute:: nssa
                                        
                                        	NSSA LSA
                                        	**type**\:  :py:class:`Nssa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa>`
                                        
                                        .. attribute:: link
                                        
                                        	Link LSA
                                        	**type**\:  :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link>`
                                        
                                        .. attribute:: intra_area_prefix
                                        
                                        	Intra\-Area\-Prefix LSA
                                        	**type**\:  :py:class:`IntraAreaPrefix <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body, self).__init__()

                                            self.yang_name = "body"
                                            self.yang_parent_name = "ospfv3"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("router", ("router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router)), ("network", ("network", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network)), ("inter-area-prefix", ("inter_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix)), ("inter-area-router", ("inter_area_router", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter)), ("as-external", ("as_external", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal)), ("nssa", ("nssa", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa)), ("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link)), ("intra-area-prefix", ("intra_area_prefix", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix))])
                                            self._leafs = OrderedDict()

                                            self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router()
                                            self.router.parent = self
                                            self._children_name_map["router"] = "router"

                                            self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network()
                                            self.network.parent = self
                                            self._children_name_map["network"] = "network"

                                            self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                            self.inter_area_prefix.parent = self
                                            self._children_name_map["inter_area_prefix"] = "inter-area-prefix"

                                            self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter()
                                            self.inter_area_router.parent = self
                                            self._children_name_map["inter_area_router"] = "inter-area-router"

                                            self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal()
                                            self.as_external.parent = self
                                            self._children_name_map["as_external"] = "as-external"

                                            self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa()
                                            self.nssa.parent = self
                                            self._children_name_map["nssa"] = "nssa"

                                            self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link()
                                            self.link.parent = self
                                            self._children_name_map["link"] = "link"

                                            self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                            self.intra_area_prefix.parent = self
                                            self._children_name_map["intra_area_prefix"] = "intra-area-prefix"
                                            self._segment_path = lambda: "body"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body, [], name, value)


                                        class Router(Entity):
                                            """
                                            Router LSA.
                                            
                                            .. attribute:: flags
                                            
                                            	LSA option
                                            	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Flags>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: link
                                            
                                            	Router LSA link
                                            	**type**\: list of  		 :py:class:`Link <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router, self).__init__()

                                                self.yang_name = "router"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("link", ("link", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link))])
                                                self._leafs = OrderedDict([
                                                    ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                    ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                ])
                                                self.flags = Bits()
                                                self.options = Bits()

                                                self.link = YList(self)
                                                self._segment_path = lambda: "router"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router, ['flags', 'options'], name, value)


                                            class Link(Entity):
                                                """
                                                Router LSA link.
                                                
                                                .. attribute:: interface_id  (key)
                                                
                                                	Interface ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neighbor_interface_id  (key)
                                                
                                                	Neighbor Interface ID
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: neighbor_router_id  (key)
                                                
                                                	Neighbor Router ID
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                                
                                                .. attribute:: type
                                                
                                                	Link type
                                                	**type**\: int
                                                
                                                	**range:** 0..255
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..65535
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link, self).__init__()

                                                    self.yang_name = "link"
                                                    self.yang_parent_name = "router"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                                        ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                                        ('neighbor_router_id', (YLeaf(YType.str, 'neighbor-router-id'), ['str'])),
                                                        ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                                        ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                                    ])
                                                    self.interface_id = None
                                                    self.neighbor_interface_id = None
                                                    self.neighbor_router_id = None
                                                    self.type = None
                                                    self.metric = None
                                                    self._segment_path = lambda: "link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                                        class Network(Entity):
                                            """
                                            Network LSA.
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: attached_router
                                            
                                            	List of the routers attached to the network
                                            	**type**\: list of str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network, self).__init__()

                                                self.yang_name = "network"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                    ('attached_router', (YLeafList(YType.str, 'attached-router'), ['str'])),
                                                ])
                                                self.options = Bits()
                                                self.attached_router = []
                                                self._segment_path = lambda: "network"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network, ['options', 'attached_router'], name, value)


                                        class InterAreaPrefix(Entity):
                                            """
                                            Inter\-Area\-Prefix LSA.
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\: int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: prefix
                                            
                                            	Prefix
                                            	**type**\: str
                                            
                                            .. attribute:: prefix_options
                                            
                                            	Prefix options
                                            	**type**\: str
                                            
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
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                    ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                ])
                                                self.metric = None
                                                self.prefix = None
                                                self.prefix_options = None
                                                self._segment_path = lambda: "inter-area-prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix, ['metric', 'prefix', 'prefix_options'], name, value)


                                        class InterAreaRouter(Entity):
                                            """
                                            Inter\-Area\-Router LSA.
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\: int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: destination_router_id
                                            
                                            	The Router ID of the router being described by the LSA
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter, self).__init__()

                                                self.yang_name = "inter-area-router"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ('destination_router_id', (YLeaf(YType.str, 'destination-router-id'), ['str'])),
                                                ])
                                                self.options = Bits()
                                                self.metric = None
                                                self.destination_router_id = None
                                                self._segment_path = lambda: "inter-area-router"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter, ['options', 'metric', 'destination_router_id'], name, value)


                                        class AsExternal(Entity):
                                            """
                                            AS\-External LSA.
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\: int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: flags
                                            
                                            	Flags
                                            	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal.Flags>`
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: prefix
                                            
                                            	Prefix
                                            	**type**\: str
                                            
                                            .. attribute:: prefix_options
                                            
                                            	Prefix options
                                            	**type**\: str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: forwarding_address
                                            
                                            	Forwarding address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: external_route_tag
                                            
                                            	Route tag
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: referenced_link_state_id
                                            
                                            	Referenced Link State ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal, self).__init__()

                                                self.yang_name = "as-external"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                    ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                    ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                    ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                    ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                    ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                ])
                                                self.metric = None
                                                self.flags = Bits()
                                                self.referenced_ls_type = None
                                                self.prefix = None
                                                self.prefix_options = None
                                                self.forwarding_address = None
                                                self.external_route_tag = None
                                                self.referenced_link_state_id = None
                                                self._segment_path = lambda: "as-external"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal, ['metric', 'flags', 'referenced_ls_type', 'prefix', 'prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                        class Nssa(Entity):
                                            """
                                            NSSA LSA.
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\: int
                                            
                                            	**range:** 0..16777215
                                            
                                            .. attribute:: flags
                                            
                                            	Flags
                                            	**type**\:  :py:class:`Flags <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa.Flags>`
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: prefix
                                            
                                            	Prefix
                                            	**type**\: str
                                            
                                            .. attribute:: prefix_options
                                            
                                            	Prefix options
                                            	**type**\: str
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: forwarding_address
                                            
                                            	Forwarding address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: external_route_tag
                                            
                                            	Route tag
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: referenced_link_state_id
                                            
                                            	Referenced Link State ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa, self).__init__()

                                                self.yang_name = "nssa"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ('flags', (YLeaf(YType.bits, 'flags'), ['Bits'])),
                                                    ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                    ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                    ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str'])),
                                                    ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                    ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                ])
                                                self.metric = None
                                                self.flags = Bits()
                                                self.referenced_ls_type = None
                                                self.prefix = None
                                                self.prefix_options = None
                                                self.forwarding_address = None
                                                self.external_route_tag = None
                                                self.referenced_link_state_id = None
                                                self._segment_path = lambda: "nssa"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa, ['metric', 'flags', 'referenced_ls_type', 'prefix', 'prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                        class Link(Entity):
                                            """
                                            Link LSA.
                                            
                                            .. attribute:: rtr_priority
                                            
                                            	Router Priority of the interface
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: options
                                            
                                            	OSPFv3 LSA options
                                            	**type**\:  :py:class:`Options <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.Options>`
                                            
                                            	**mandatory**\: True
                                            
                                            .. attribute:: link_local_interface_address
                                            
                                            	The originating router's link\-local interface address on the link
                                            	**type**\: union of the below types:
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: num_of_prefixes
                                            
                                            	Number of prefixes
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: prefix_list
                                            
                                            	List of prefixes associated with the link
                                            	**type**\: list of  		 :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link, self).__init__()

                                                self.yang_name = "link"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("prefix-list", ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList))])
                                                self._leafs = OrderedDict([
                                                    ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                                    ('options', (YLeaf(YType.bits, 'options'), ['Bits'])),
                                                    ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                                    ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                                ])
                                                self.rtr_priority = None
                                                self.options = Bits()
                                                self.link_local_interface_address = None
                                                self.num_of_prefixes = None

                                                self.prefix_list = YList(self)
                                                self._segment_path = lambda: "link"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link, ['rtr_priority', 'options', 'link_local_interface_address', 'num_of_prefixes'], name, value)


                                            class PrefixList(Entity):
                                                """
                                                List of prefixes associated with the link.
                                                
                                                .. attribute:: prefix  (key)
                                                
                                                	Prefix
                                                	**type**\: str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\: str
                                                
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
                                                    self.ylist_key_names = ['prefix']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                        ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                    ])
                                                    self.prefix = None
                                                    self.prefix_options = None
                                                    self._segment_path = lambda: "prefix-list" + "[prefix='" + str(self.prefix) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList, ['prefix', 'prefix_options'], name, value)


                                        class IntraAreaPrefix(Entity):
                                            """
                                            Intra\-Area\-Prefix LSA.
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: referenced_link_state_id
                                            
                                            	Referenced Link State ID
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: referenced_adv_router
                                            
                                            	Referenced Advertising Router
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: num_of_prefixes
                                            
                                            	Number of prefixes
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: prefix_list
                                            
                                            	List of prefixes associated with the link
                                            	**type**\: list of  		 :py:class:`PrefixList <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList>`
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix, self).__init__()

                                                self.yang_name = "intra-area-prefix"
                                                self.yang_parent_name = "body"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("prefix-list", ("prefix_list", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList))])
                                                self._leafs = OrderedDict([
                                                    ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                    ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                    ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str'])),
                                                    ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                                ])
                                                self.referenced_ls_type = None
                                                self.referenced_link_state_id = None
                                                self.referenced_adv_router = None
                                                self.num_of_prefixes = None

                                                self.prefix_list = YList(self)
                                                self._segment_path = lambda: "intra-area-prefix"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                                            class PrefixList(Entity):
                                                """
                                                List of prefixes associated with the link.
                                                
                                                .. attribute:: prefix  (key)
                                                
                                                	Prefix
                                                	**type**\: str
                                                
                                                .. attribute:: prefix_options
                                                
                                                	Prefix options
                                                	**type**\: str
                                                
                                                	**mandatory**\: True
                                                
                                                .. attribute:: metric
                                                
                                                	Metric
                                                	**type**\: int
                                                
                                                	**range:** 0..16777215
                                                
                                                

                                                """

                                                _prefix = 'ospf'
                                                _revision = '2015-03-09'

                                                def __init__(self):
                                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, self).__init__()

                                                    self.yang_name = "prefix-list"
                                                    self.yang_parent_name = "intra-area-prefix"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['prefix']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                                        ('prefix_options', (YLeaf(YType.str, 'prefix-options'), ['str'])),
                                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ])
                                                    self.prefix = None
                                                    self.prefix_options = None
                                                    self.metric = None
                                                    self._segment_path = lambda: "prefix-list" + "[prefix='" + str(self.prefix) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList, ['prefix', 'prefix_options', 'metric'], name, value)


                        class Topology(Entity):
                            """
                            OSPF topology.
                            
                            .. attribute:: name  (key)
                            
                            	RIB
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
                            
                            .. attribute:: area
                            
                            	List of ospf areas
                            	**type**\: list of  		 :py:class:`Area <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, self).__init__()

                                self.yang_name = "topology"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_classes = OrderedDict([("area", ("area", RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area))])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.name = None

                                self.area = YList(self)
                                self._segment_path = lambda: "topology" + "[name='" + str(self.name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, ['name'], name, value)


                            class Area(Entity):
                                """
                                List of ospf areas
                                
                                .. attribute:: area_id  (key)
                                
                                	Area ID
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 0..4294967295
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, self).__init__()

                                    self.yang_name = "area"
                                    self.yang_parent_name = "topology"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['area_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('area_id', (YLeaf(YType.str, 'area-id'), ['int','str'])),
                                    ])
                                    self.area_id = None
                                    self._segment_path = lambda: "area" + "[area-id='" + str(self.area_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, ['area_id'], name, value)


        class Ribs(Entity):
            """
            Container for RIBs.
            
            .. attribute:: rib
            
            	Each entry represents a RIB identified by the 'name' key. All routes in a RIB MUST belong to the same address family.  For each routing instance, an implementation SHOULD provide one system\-controlled default RIB for each supported address family
            	**type**\: list of  		 :py:class:`Rib <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(RoutingState.RoutingInstance.Ribs, self).__init__()

                self.yang_name = "ribs"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rib", ("rib", RoutingState.RoutingInstance.Ribs.Rib))])
                self._leafs = OrderedDict()

                self.rib = YList(self)
                self._segment_path = lambda: "ribs"
                self._is_frozen = True

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
                
                .. attribute:: name  (key)
                
                	The name of the RIB
                	**type**\: str
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:  :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                
                	**mandatory**\: True
                
                .. attribute:: default_rib
                
                	This flag has the value of 'true' if and only if the RIB is the default RIB for the given address family.  A default RIB always receives direct routes. By default it also receives routes from all routing protocols
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: routes
                
                	Current content of the RIB
                	**type**\:  :py:class:`Routes <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(RoutingState.RoutingInstance.Ribs.Rib, self).__init__()

                    self.yang_name = "rib"
                    self.yang_parent_name = "ribs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("routes", ("routes", RoutingState.RoutingInstance.Ribs.Rib.Routes))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('address_family', (YLeaf(YType.identityref, 'address-family'), [('ydk.models.ietf.ietf_routing', 'AddressFamily')])),
                        ('default_rib', (YLeaf(YType.boolean, 'default-rib'), ['bool'])),
                    ])
                    self.name = None
                    self.address_family = None
                    self.default_rib = None

                    self.routes = RoutingState.RoutingInstance.Ribs.Rib.Routes()
                    self.routes.parent = self
                    self._children_name_map["routes"] = "routes"
                    self._segment_path = lambda: "rib" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib, [u'name', u'address_family', u'default_rib'], name, value)


                class Routes(Entity):
                    """
                    Current content of the RIB.
                    
                    .. attribute:: route
                    
                    	A RIB route entry. This data node MUST be augmented with information specific for routes of each address family
                    	**type**\: list of  		 :py:class:`Route <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route>`
                    
                    

                    """

                    _prefix = 'rt'
                    _revision = '2015-05-25'

                    def __init__(self):
                        super(RoutingState.RoutingInstance.Ribs.Rib.Routes, self).__init__()

                        self.yang_name = "routes"
                        self.yang_parent_name = "rib"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("route", ("route", RoutingState.RoutingInstance.Ribs.Rib.Routes.Route))])
                        self._leafs = OrderedDict()

                        self.route = YList(self)
                        self._segment_path = lambda: "routes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib.Routes, [], name, value)


                    class Route(Entity):
                        """
                        A RIB route entry. This data node MUST be augmented
                        with information specific for routes of each address
                        family.
                        
                        .. attribute:: destination_prefix  (key)
                        
                        	Destination IP address with prefix
                        	**type**\: str
                        
                        .. attribute:: route_preference
                        
                        	This route attribute, also known as administrative distance, allows for selecting the preferred route among routes with the same destination prefix. A smaller value means a more preferred route
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: metric
                        
                        	Route metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop
                        
                        	Route's next\-hop attribute
                        	**type**\:  :py:class:`NextHop <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop>`
                        
                        .. attribute:: source_protocol
                        
                        	Type of the routing protocol from which the route originated
                        	**type**\:  :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: active
                        
                        	Presence of this leaf indicates that the route is preferred among all routes in the same RIB that have the same destination prefix
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: last_updated
                        
                        	Time stamp of the last modification of the route. If the route was never modified, it is the time when the route was inserted into the RIB
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: update_source
                        
                        	Update source for the route
                        	**type**\: str
                        
                        .. attribute:: tag
                        
                        	OSPF route tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: route_type
                        
                        	OSPF route type
                        	**type**\:  :py:class:`RouteType <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.RouteType>`
                        
                        

                        """

                        _prefix = 'rt'
                        _revision = '2015-05-25'

                        def __init__(self):
                            super(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route, self).__init__()

                            self.yang_name = "route"
                            self.yang_parent_name = "routes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['destination_prefix']
                            self._child_classes = OrderedDict([("next-hop", ("next_hop", RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop))])
                            self._leafs = OrderedDict([
                                ('destination_prefix', (YLeaf(YType.str, 'destination-prefix'), ['str'])),
                                ('route_preference', (YLeaf(YType.uint32, 'route-preference'), ['int'])),
                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                ('source_protocol', (YLeaf(YType.identityref, 'source-protocol'), [('ydk.models.ietf.ietf_routing', 'RoutingProtocol')])),
                                ('active', (YLeaf(YType.empty, 'active'), ['Empty'])),
                                ('last_updated', (YLeaf(YType.str, 'last-updated'), ['str'])),
                                ('update_source', (YLeaf(YType.str, 'update-source'), ['str'])),
                                ('tag', (YLeaf(YType.uint32, 'ietf-ospf:tag'), ['int'])),
                                ('route_type', (YLeaf(YType.enumeration, 'ietf-ospf:route-type'), [('ydk.models.ietf.ietf_routing', 'RoutingState', 'RoutingInstance.Ribs.Rib.Routes.Route.RouteType')])),
                            ])
                            self.destination_prefix = None
                            self.route_preference = None
                            self.metric = None
                            self.source_protocol = None
                            self.active = None
                            self.last_updated = None
                            self.update_source = None
                            self.tag = None
                            self.route_type = None

                            self.next_hop = RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop()
                            self.next_hop.parent = self
                            self._children_name_map["next_hop"] = "next-hop"
                            self._segment_path = lambda: "route" + "[destination-prefix='" + str(self.destination_prefix) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route, [u'destination_prefix', u'route_preference', u'metric', u'source_protocol', u'active', u'last_updated', u'update_source', 'tag', 'route_type'], name, value)

                        class RouteType(Enum):
                            """
                            RouteType (Enum Class)

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
                            
                            .. attribute:: outgoing_interface
                            
                            	Name of the outgoing interface
                            	**type**\: str
                            
                            .. attribute:: next_hop_address
                            
                            	IP address
                            	**type**\: str
                            
                            .. attribute:: special_next_hop
                            
                            	Special next\-hop options
                            	**type**\:  :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop.SpecialNextHop>`
                            
                            

                            """

                            _prefix = 'rt'
                            _revision = '2015-05-25'

                            def __init__(self):
                                super(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop, self).__init__()

                                self.yang_name = "next-hop"
                                self.yang_parent_name = "route"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                                    ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                    ('special_next_hop', (YLeaf(YType.enumeration, 'special-next-hop'), [('ydk.models.ietf.ietf_routing', 'RoutingState', 'RoutingInstance.Ribs.Rib.Routes.Route.NextHop.SpecialNextHop')])),
                                ])
                                self.outgoing_interface = None
                                self.next_hop_address = None
                                self.special_next_hop = None
                                self._segment_path = lambda: "next-hop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop, [u'outgoing_interface', u'next_hop_address', u'special_next_hop'], name, value)

                            class SpecialNextHop(Enum):
                                """
                                SpecialNextHop (Enum Class)

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
        self._top_entity = RoutingState()
        return self._top_entity

class Routing(Entity):
    """
    Configuration parameters for the routing subsystem.
    
    .. attribute:: routing_instance
    
    	Configuration of a routing instance
    	**type**\: list of  		 :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.Routing.RoutingInstance>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("routing-instance", ("routing_instance", Routing.RoutingInstance))])
        self._leafs = OrderedDict()

        self.routing_instance = YList(self)
        self._segment_path = lambda: "ietf-routing:routing"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Routing, [], name, value)


    class RoutingInstance(Entity):
        """
        Configuration of a routing instance.
        
        .. attribute:: name  (key)
        
        	The name of the routing instance.  For system\-controlled entries, the value of this leaf must be the same as the name of the corresponding entry in state data.  For user\-controlled entries, an arbitrary name can be used
        	**type**\: str
        
        .. attribute:: type
        
        	The type of the routing instance
        	**type**\:  :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.RoutingInstance>`
        
        	**default value**\: rt:default-routing-instance
        
        .. attribute:: enabled
        
        	Enable/disable the routing instance.  If this parameter is false, the parent routing instance is disabled and does not appear in state data, despite any other configuration that might be present
        	**type**\: bool
        
        	**default value**\: true
        
        .. attribute:: router_id
        
        	A 32\-bit number in the form of a dotted quad that is used by some routing protocols identifying a router
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
        
        .. attribute:: description
        
        	Textual description of the routing instance
        	**type**\: str
        
        .. attribute:: interfaces
        
        	Assignment of the routing instance's interfaces
        	**type**\:  :py:class:`Interfaces <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Interfaces>`
        
        .. attribute:: routing_protocols
        
        	Configuration of routing protocol instances
        	**type**\:  :py:class:`RoutingProtocols <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols>`
        
        .. attribute:: ribs
        
        	Configuration of RIBs
        	**type**\:  :py:class:`Ribs <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(Routing.RoutingInstance, self).__init__()

            self.yang_name = "routing-instance"
            self.yang_parent_name = "routing"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_classes = OrderedDict([("interfaces", ("interfaces", Routing.RoutingInstance.Interfaces)), ("routing-protocols", ("routing_protocols", Routing.RoutingInstance.RoutingProtocols)), ("ribs", ("ribs", Routing.RoutingInstance.Ribs))])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.ietf.ietf_routing', 'RoutingInstance')])),
                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                ('description', (YLeaf(YType.str, 'description'), ['str'])),
            ])
            self.name = None
            self.type = None
            self.enabled = None
            self.router_id = None
            self.description = None

            self.interfaces = Routing.RoutingInstance.Interfaces()
            self.interfaces.parent = self
            self._children_name_map["interfaces"] = "interfaces"

            self.routing_protocols = Routing.RoutingInstance.RoutingProtocols()
            self.routing_protocols.parent = self
            self._children_name_map["routing_protocols"] = "routing-protocols"

            self.ribs = Routing.RoutingInstance.Ribs()
            self.ribs.parent = self
            self._children_name_map["ribs"] = "ribs"
            self._segment_path = lambda: "routing-instance" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "ietf-routing:routing/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Routing.RoutingInstance, [u'name', u'type', u'enabled', u'router_id', u'description'], name, value)


        class Interfaces(Entity):
            """
            Assignment of the routing instance's interfaces.
            
            .. attribute:: interface
            
            	The name of a configured network layer interface to be assigned to the routing\-instance
            	**type**\: list of str
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface', (YLeafList(YType.str, 'interface'), ['str'])),
                ])
                self.interface = []
                self._segment_path = lambda: "interfaces"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Routing.RoutingInstance.Interfaces, [u'interface'], name, value)


        class RoutingProtocols(Entity):
            """
            Configuration of routing protocol instances.
            
            .. attribute:: routing_protocol
            
            	Each entry contains configuration of a routing protocol instance
            	**type**\: list of  		 :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(Routing.RoutingInstance.RoutingProtocols, self).__init__()

                self.yang_name = "routing-protocols"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("routing-protocol", ("routing_protocol", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol))])
                self._leafs = OrderedDict()

                self.routing_protocol = YList(self)
                self._segment_path = lambda: "routing-protocols"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols, [], name, value)


            class RoutingProtocol(Entity):
                """
                Each entry contains configuration of a routing protocol
                instance.
                
                .. attribute:: type  (key)
                
                	Type of the routing protocol \- an identity derived from the 'routing\-protocol' base identity
                	**type**\:  :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
                
                .. attribute:: name  (key)
                
                	An arbitrary name of the routing protocol instance
                	**type**\: str
                
                .. attribute:: description
                
                	Textual description of the routing protocol instance
                	**type**\: str
                
                .. attribute:: static_routes
                
                	Configuration of the 'static' pseudo\-protocol.  Address\-family\-specific modules augment this node with their lists of routes
                	**type**\:  :py:class:`StaticRoutes <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes>`
                
                .. attribute:: ospf
                
                	OSPF
                	**type**\:  :py:class:`Ospf <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol, self).__init__()

                    self.yang_name = "routing-protocol"
                    self.yang_parent_name = "routing-protocols"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['type','name']
                    self._child_classes = OrderedDict([("static-routes", ("static_routes", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes)), ("ietf-ospf:ospf", ("ospf", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf))])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.identityref, 'type'), [('ydk.models.ietf.ietf_routing', 'RoutingProtocol')])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ])
                    self.type = None
                    self.name = None
                    self.description = None

                    self.static_routes = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes()
                    self.static_routes.parent = self
                    self._children_name_map["static_routes"] = "static-routes"

                    self.ospf = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf()
                    self.ospf.parent = self
                    self._children_name_map["ospf"] = "ietf-ospf:ospf"
                    self._segment_path = lambda: "routing-protocol" + "[type='" + str(self.type) + "']" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol, [u'type', u'name', u'description'], name, value)


                class StaticRoutes(Entity):
                    """
                    Configuration of the 'static' pseudo\-protocol.
                    
                    Address\-family\-specific modules augment this node with
                    their lists of routes.
                    
                    .. attribute:: ipv6
                    
                    	Configuration of a 'static' pseudo\-protocol instance consists of a list of routes
                    	**type**\:  :py:class:`Ipv6 <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6>`
                    
                    .. attribute:: ipv4
                    
                    	Configuration of a 'static' pseudo\-protocol instance consists of a list of routes
                    	**type**\:  :py:class:`Ipv4 <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4>`
                    
                    

                    """

                    _prefix = 'rt'
                    _revision = '2015-05-25'

                    def __init__(self):
                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes, self).__init__()

                        self.yang_name = "static-routes"
                        self.yang_parent_name = "routing-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ietf-ipv6-unicast-routing:ipv6", ("ipv6", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6)), ("ietf-ipv4-unicast-routing:ipv4", ("ipv4", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4))])
                        self._leafs = OrderedDict()

                        self.ipv6 = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ietf-ipv6-unicast-routing:ipv6"

                        self.ipv4 = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ietf-ipv4-unicast-routing:ipv4"
                        self._segment_path = lambda: "static-routes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes, [], name, value)


                    class Ipv6(Entity):
                        """
                        Configuration of a 'static' pseudo\-protocol instance
                        consists of a list of routes.
                        
                        .. attribute:: route
                        
                        	A user\-ordered list of static routes
                        	**type**\: list of  		 :py:class:`Route <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route>`
                        
                        

                        """

                        _prefix = 'v6ur'
                        _revision = '2015-05-25'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "static-routes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route", ("route", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route))])
                            self._leafs = OrderedDict()

                            self.route = YList(self)
                            self._segment_path = lambda: "ietf-ipv6-unicast-routing:ipv6"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6, [], name, value)


                        class Route(Entity):
                            """
                            A user\-ordered list of static routes.
                            
                            .. attribute:: destination_prefix  (key)
                            
                            	IPv6 destination prefix
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
                            
                            	**mandatory**\: True
                            
                            .. attribute:: description
                            
                            	Textual description of the route
                            	**type**\: str
                            
                            .. attribute:: next_hop
                            
                            	Configuration of next\-hop
                            	**type**\:  :py:class:`NextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop>`
                            
                            

                            """

                            _prefix = 'v6ur'
                            _revision = '2015-05-25'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['destination_prefix']
                                self._child_classes = OrderedDict([("next-hop", ("next_hop", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop))])
                                self._leafs = OrderedDict([
                                    ('destination_prefix', (YLeaf(YType.str, 'destination-prefix'), ['str'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ])
                                self.destination_prefix = None
                                self.description = None

                                self.next_hop = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                                self._segment_path = lambda: "route" + "[destination-prefix='" + str(self.destination_prefix) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route, ['destination_prefix', 'description'], name, value)


                            class NextHop(Entity):
                                """
                                Configuration of next\-hop.
                                
                                .. attribute:: outgoing_interface
                                
                                	Name of the outgoing interface
                                	**type**\: str
                                
                                .. attribute:: special_next_hop
                                
                                	Special next\-hop options
                                	**type**\:  :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop.SpecialNextHop>`
                                
                                .. attribute:: next_hop_address
                                
                                	IPv6 address of the next\-hop
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'v6ur'
                                _revision = '2015-05-25'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                                        ('special_next_hop', (YLeaf(YType.enumeration, 'special-next-hop'), [('ydk.models.ietf.ietf_routing', 'Routing', 'RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop.SpecialNextHop')])),
                                        ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                    ])
                                    self.outgoing_interface = None
                                    self.special_next_hop = None
                                    self.next_hop_address = None
                                    self._segment_path = lambda: "next-hop"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop, [u'outgoing_interface', u'special_next_hop', 'next_hop_address'], name, value)

                                class SpecialNextHop(Enum):
                                    """
                                    SpecialNextHop (Enum Class)

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



                    class Ipv4(Entity):
                        """
                        Configuration of a 'static' pseudo\-protocol instance
                        consists of a list of routes.
                        
                        .. attribute:: route
                        
                        	A user\-ordered list of static routes
                        	**type**\: list of  		 :py:class:`Route <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route>`
                        
                        

                        """

                        _prefix = 'v4ur'
                        _revision = '2015-05-25'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "static-routes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route", ("route", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route))])
                            self._leafs = OrderedDict()

                            self.route = YList(self)
                            self._segment_path = lambda: "ietf-ipv4-unicast-routing:ipv4"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4, [], name, value)


                        class Route(Entity):
                            """
                            A user\-ordered list of static routes.
                            
                            .. attribute:: destination_prefix  (key)
                            
                            	IPv4 destination prefix
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
                            
                            	**mandatory**\: True
                            
                            .. attribute:: description
                            
                            	Textual description of the route
                            	**type**\: str
                            
                            .. attribute:: next_hop
                            
                            	Configuration of next\-hop
                            	**type**\:  :py:class:`NextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop>`
                            
                            

                            """

                            _prefix = 'v4ur'
                            _revision = '2015-05-25'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route, self).__init__()

                                self.yang_name = "route"
                                self.yang_parent_name = "ipv4"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['destination_prefix']
                                self._child_classes = OrderedDict([("next-hop", ("next_hop", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop))])
                                self._leafs = OrderedDict([
                                    ('destination_prefix', (YLeaf(YType.str, 'destination-prefix'), ['str'])),
                                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                ])
                                self.destination_prefix = None
                                self.description = None

                                self.next_hop = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                                self._segment_path = lambda: "route" + "[destination-prefix='" + str(self.destination_prefix) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route, ['destination_prefix', 'description'], name, value)


                            class NextHop(Entity):
                                """
                                Configuration of next\-hop.
                                
                                .. attribute:: outgoing_interface
                                
                                	Name of the outgoing interface
                                	**type**\: str
                                
                                .. attribute:: special_next_hop
                                
                                	Special next\-hop options
                                	**type**\:  :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop.SpecialNextHop>`
                                
                                .. attribute:: next_hop_address
                                
                                	IPv4 address of the next\-hop
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'v4ur'
                                _revision = '2015-05-25'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop, self).__init__()

                                    self.yang_name = "next-hop"
                                    self.yang_parent_name = "route"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                                        ('special_next_hop', (YLeaf(YType.enumeration, 'special-next-hop'), [('ydk.models.ietf.ietf_routing', 'Routing', 'RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop.SpecialNextHop')])),
                                        ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                                    ])
                                    self.outgoing_interface = None
                                    self.special_next_hop = None
                                    self.next_hop_address = None
                                    self._segment_path = lambda: "next-hop"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop, [u'outgoing_interface', u'special_next_hop', 'next_hop_address'], name, value)

                                class SpecialNextHop(Enum):
                                    """
                                    SpecialNextHop (Enum Class)

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



                class Ospf(Entity):
                    """
                    OSPF.
                    
                    .. attribute:: all_instances_inherit
                    
                    	Inheritance support to all instances
                    	**type**\:  :py:class:`AllInstancesInherit <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit>`
                    
                    .. attribute:: operation_mode
                    
                    	OSPF operation mode
                    	**type**\:  :py:class:`OperationMode <ydk.models.ietf.ietf_ospf.OperationMode>`
                    
                    	**default value**\: ospf:ships-in-the-night
                    
                    .. attribute:: instance
                    
                    	An OSPF routing protocol instance
                    	**type**\: list of  		 :py:class:`Instance <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance>`
                    
                    

                    """

                    _prefix = 'ospf'
                    _revision = '2015-03-09'

                    def __init__(self):
                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, self).__init__()

                        self.yang_name = "ospf"
                        self.yang_parent_name = "routing-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("all-instances-inherit", ("all_instances_inherit", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit)), ("instance", ("instance", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance))])
                        self._leafs = OrderedDict([
                            ('operation_mode', (YLeaf(YType.identityref, 'operation-mode'), [('ydk.models.ietf.ietf_ospf', 'OperationMode')])),
                        ])
                        self.operation_mode = None

                        self.all_instances_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit()
                        self.all_instances_inherit.parent = self
                        self._children_name_map["all_instances_inherit"] = "all-instances-inherit"

                        self.instance = YList(self)
                        self._segment_path = lambda: "ietf-ospf:ospf"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf, ['operation_mode'], name, value)


                    class AllInstancesInherit(Entity):
                        """
                        Inheritance support to all instances.
                        
                        .. attribute:: area
                        
                        	Area config to be inherited by all areas in all instances
                        	**type**\:  :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area>`
                        
                        .. attribute:: interface
                        
                        	Interface config to be inherited by all interfaces in all instances
                        	**type**\:  :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface>`
                        
                        

                        """

                        _prefix = 'ospf'
                        _revision = '2015-03-09'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit, self).__init__()

                            self.yang_name = "all-instances-inherit"
                            self.yang_parent_name = "ospf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("area", ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area)), ("interface", ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface))])
                            self._leafs = OrderedDict()

                            self.area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area()
                            self.area.parent = self
                            self._children_name_map["area"] = "area"

                            self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._segment_path = lambda: "all-instances-inherit"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit, [], name, value)


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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "area"
                                self._is_frozen = True


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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "interface"
                                self._is_frozen = True


                    class Instance(Entity):
                        """
                        An OSPF routing protocol instance.
                        
                        .. attribute:: af  (key)
                        
                        	Address\-family of the instance
                        	**type**\:  :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                        
                        .. attribute:: router_id
                        
                        	Defined in RFC 2328. A 32\-bit number that uniquely identifies the router
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                        
                        .. attribute:: admin_distance
                        
                        	Admin distance config state
                        	**type**\:  :py:class:`AdminDistance <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance>`
                        
                        .. attribute:: nsr
                        
                        	NSR config state
                        	**type**\:  :py:class:`Nsr <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr>`
                        
                        .. attribute:: graceful_restart
                        
                        	Graceful restart config state
                        	**type**\:  :py:class:`GracefulRestart <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart>`
                        
                        .. attribute:: enable
                        
                        	Enable/Disable the protocol
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: auto_cost
                        
                        	Auto cost config state
                        	**type**\:  :py:class:`AutoCost <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost>`
                        
                        .. attribute:: spf_control
                        
                        	SPF calculation control
                        	**type**\:  :py:class:`SpfControl <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl>`
                        
                        .. attribute:: database_control
                        
                        	Database maintenance control
                        	**type**\:  :py:class:`DatabaseControl <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl>`
                        
                        .. attribute:: reload_control
                        
                        	Protocol reload control
                        	**type**\:  :py:class:`ReloadControl <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl>`
                        
                        .. attribute:: mpls
                        
                        	OSPF MPLS config state
                        	**type**\:  :py:class:`Mpls <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls>`
                        
                        .. attribute:: fast_reroute
                        
                        	This container may be augmented with global parameters for IPFRR
                        	**type**\:  :py:class:`FastReroute <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute>`
                        
                        .. attribute:: all_areas_inherit
                        
                        	Inheritance for all areas
                        	**type**\:  :py:class:`AllAreasInherit <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit>`
                        
                        .. attribute:: area
                        
                        	List of ospf areas
                        	**type**\: list of  		 :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area>`
                        
                        .. attribute:: topology
                        
                        	OSPF topology
                        	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology>`
                        
                        

                        """

                        _prefix = 'ospf'
                        _revision = '2015-03-09'

                        def __init__(self):
                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, self).__init__()

                            self.yang_name = "instance"
                            self.yang_parent_name = "ospf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['af']
                            self._child_classes = OrderedDict([("admin-distance", ("admin_distance", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance)), ("nsr", ("nsr", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr)), ("graceful-restart", ("graceful_restart", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart)), ("auto-cost", ("auto_cost", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost)), ("spf-control", ("spf_control", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl)), ("database-control", ("database_control", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl)), ("reload-control", ("reload_control", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl)), ("mpls", ("mpls", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls)), ("fast-reroute", ("fast_reroute", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute)), ("all-areas-inherit", ("all_areas_inherit", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit)), ("area", ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area)), ("topology", ("topology", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology))])
                            self._leafs = OrderedDict([
                                ('af', (YLeaf(YType.identityref, 'af'), [('ydk.models.ietf.ietf_routing', 'AddressFamily')])),
                                ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ])
                            self.af = None
                            self.router_id = None
                            self.enable = None

                            self.admin_distance = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance()
                            self.admin_distance.parent = self
                            self._children_name_map["admin_distance"] = "admin-distance"

                            self.nsr = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr()
                            self.nsr.parent = self
                            self._children_name_map["nsr"] = "nsr"

                            self.graceful_restart = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart()
                            self.graceful_restart.parent = self
                            self._children_name_map["graceful_restart"] = "graceful-restart"

                            self.auto_cost = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost()
                            self.auto_cost.parent = self
                            self._children_name_map["auto_cost"] = "auto-cost"

                            self.spf_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl()
                            self.spf_control.parent = self
                            self._children_name_map["spf_control"] = "spf-control"

                            self.database_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl()
                            self.database_control.parent = self
                            self._children_name_map["database_control"] = "database-control"

                            self.reload_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl()
                            self.reload_control.parent = self
                            self._children_name_map["reload_control"] = "reload-control"

                            self.mpls = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls()
                            self.mpls.parent = self
                            self._children_name_map["mpls"] = "mpls"

                            self.fast_reroute = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute()
                            self.fast_reroute.parent = self
                            self._children_name_map["fast_reroute"] = "fast-reroute"

                            self.all_areas_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit()
                            self.all_areas_inherit.parent = self
                            self._children_name_map["all_areas_inherit"] = "all-areas-inherit"

                            self.area = YList(self)
                            self.topology = YList(self)
                            self._segment_path = lambda: "instance" + "[af='" + str(self.af) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance, ['af', 'router_id', 'enable'], name, value)


                        class AdminDistance(Entity):
                            """
                            Admin distance config state.
                            
                            .. attribute:: intra_area
                            
                            	Admin distance for intra\-area route
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: inter_area
                            
                            	Admin distance for inter\-area route
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: internal
                            
                            	Admin distance for both intra\-area and inter\-area route
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: external
                            
                            	Admin distance for both external route
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('intra_area', (YLeaf(YType.uint8, 'intra-area'), ['int'])),
                                    ('inter_area', (YLeaf(YType.uint8, 'inter-area'), ['int'])),
                                    ('internal', (YLeaf(YType.uint8, 'internal'), ['int'])),
                                    ('external', (YLeaf(YType.uint8, 'external'), ['int'])),
                                ])
                                self.intra_area = None
                                self.inter_area = None
                                self.internal = None
                                self.external = None
                                self._segment_path = lambda: "admin-distance"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance, ['intra_area', 'inter_area', 'internal', 'external'], name, value)


                        class Nsr(Entity):
                            """
                            NSR config state.
                            
                            .. attribute:: enable
                            
                            	Enable/Disable NSR
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr, self).__init__()

                                self.yang_name = "nsr"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ])
                                self.enable = None
                                self._segment_path = lambda: "nsr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr, ['enable'], name, value)


                        class GracefulRestart(Entity):
                            """
                            Graceful restart config state.
                            
                            .. attribute:: enable
                            
                            	Enable/Disable graceful restart as defined in RFC 3623
                            	**type**\: bool
                            
                            .. attribute:: helper_enable
                            
                            	Enable RestartHelperSupport in RFC 3623 Section B.2
                            	**type**\: bool
                            
                            .. attribute:: restart_interval
                            
                            	RestartInterval option in RFC 3623 Section B.1
                            	**type**\: int
                            
                            	**range:** 1..1800
                            
                            	**units**\: seconds
                            
                            	**default value**\: 120
                            
                            .. attribute:: helper_strict_lsa_checking
                            
                            	RestartHelperStrictLSAChecking option in RFC 3623 Section B.2
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart, self).__init__()

                                self.yang_name = "graceful-restart"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ('helper_enable', (YLeaf(YType.boolean, 'helper-enable'), ['bool'])),
                                    ('restart_interval', (YLeaf(YType.uint16, 'restart-interval'), ['int'])),
                                    ('helper_strict_lsa_checking', (YLeaf(YType.boolean, 'helper-strict-lsa-checking'), ['bool'])),
                                ])
                                self.enable = None
                                self.helper_enable = None
                                self.restart_interval = None
                                self.helper_strict_lsa_checking = None
                                self._segment_path = lambda: "graceful-restart"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart, ['enable', 'helper_enable', 'restart_interval', 'helper_strict_lsa_checking'], name, value)


                        class AutoCost(Entity):
                            """
                            Auto cost config state.
                            
                            .. attribute:: enable
                            
                            	Enable/Disable auto cost
                            	**type**\: bool
                            
                            .. attribute:: reference_bandwidth
                            
                            	Configure reference bandwidth in term of Mbits
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ('reference_bandwidth', (YLeaf(YType.uint32, 'reference-bandwidth'), ['int'])),
                                ])
                                self.enable = None
                                self.reference_bandwidth = None
                                self._segment_path = lambda: "auto-cost"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost, ['enable', 'reference_bandwidth'], name, value)


                        class SpfControl(Entity):
                            """
                            SPF calculation control.
                            
                            .. attribute:: paths
                            
                            	Maximum number of ECMP paths
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('paths', (YLeaf(YType.uint16, 'paths'), ['int'])),
                                ])
                                self.paths = None
                                self._segment_path = lambda: "spf-control"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl, ['paths'], name, value)


                        class DatabaseControl(Entity):
                            """
                            Database maintenance control.
                            
                            .. attribute:: max_lsa
                            
                            	Maximum number of LSAs OSPF will receive
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('max_lsa', (YLeaf(YType.uint32, 'max-lsa'), ['int'])),
                                ])
                                self.max_lsa = None
                                self._segment_path = lambda: "database-control"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl, ['max_lsa'], name, value)


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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict()
                                self._segment_path = lambda: "reload-control"
                                self._is_frozen = True


                        class Mpls(Entity):
                            """
                            OSPF MPLS config state.
                            
                            .. attribute:: te_rid
                            
                            	Traffic Engineering stable IP address for system
                            	**type**\:  :py:class:`TeRid <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid>`
                            
                            .. attribute:: ldp
                            
                            	OSPF MPLS LDP config state
                            	**type**\:  :py:class:`Ldp <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls, self).__init__()

                                self.yang_name = "mpls"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("te-rid", ("te_rid", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid)), ("ldp", ("ldp", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp))])
                                self._leafs = OrderedDict()

                                self.te_rid = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid()
                                self.te_rid.parent = self
                                self._children_name_map["te_rid"] = "te-rid"

                                self.ldp = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp()
                                self.ldp.parent = self
                                self._children_name_map["ldp"] = "ldp"
                                self._segment_path = lambda: "mpls"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls, [], name, value)


                            class TeRid(Entity):
                                """
                                Traffic Engineering stable IP address for system.
                                
                                .. attribute:: interface
                                
                                	Take the interface's IPv4 address as TE router ID
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: router_id
                                
                                	Explicitly configure the TE router ID
                                	**type**\: str
                                
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
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ])
                                    self.interface = None
                                    self.router_id = None
                                    self._segment_path = lambda: "te-rid"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid, ['interface', 'router_id'], name, value)


                            class Ldp(Entity):
                                """
                                OSPF MPLS LDP config state.
                                
                                .. attribute:: igp_sync
                                
                                	Enable LDP IGP synchronization
                                	**type**\: bool
                                
                                .. attribute:: autoconfig
                                
                                	Enable LDP IGP interface auto\-configuration
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp, self).__init__()

                                    self.yang_name = "ldp"
                                    self.yang_parent_name = "mpls"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('igp_sync', (YLeaf(YType.boolean, 'igp-sync'), ['bool'])),
                                        ('autoconfig', (YLeaf(YType.boolean, 'autoconfig'), ['bool'])),
                                    ])
                                    self.igp_sync = None
                                    self.autoconfig = None
                                    self._segment_path = lambda: "ldp"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp, ['igp_sync', 'autoconfig'], name, value)


                        class FastReroute(Entity):
                            """
                            This container may be augmented with global
                            parameters for IPFRR.
                            
                            .. attribute:: lfa
                            
                            	This container may be augmented with global parameters for LFA. Creating the container has no effect on LFA activation
                            	**type**\:  :py:class:`Lfa <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute, self).__init__()

                                self.yang_name = "fast-reroute"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("lfa", ("lfa", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa))])
                                self._leafs = OrderedDict()

                                self.lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa()
                                self.lfa.parent = self
                                self._children_name_map["lfa"] = "lfa"
                                self._segment_path = lambda: "fast-reroute"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute, [], name, value)


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
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict()
                                    self._segment_path = lambda: "lfa"
                                    self._is_frozen = True


                        class AllAreasInherit(Entity):
                            """
                            Inheritance for all areas.
                            
                            .. attribute:: area
                            
                            	Area config to be inherited by all areas
                            	**type**\:  :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area>`
                            
                            .. attribute:: interface
                            
                            	Interface config to be inherited by all interfaces in all areas
                            	**type**\:  :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit, self).__init__()

                                self.yang_name = "all-areas-inherit"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("area", ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area)), ("interface", ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface))])
                                self._leafs = OrderedDict()

                                self.area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area()
                                self.area.parent = self
                                self._children_name_map["area"] = "area"

                                self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface()
                                self.interface.parent = self
                                self._children_name_map["interface"] = "interface"
                                self._segment_path = lambda: "all-areas-inherit"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit, [], name, value)


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
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict()
                                    self._segment_path = lambda: "area"
                                    self._is_frozen = True


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
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict()
                                    self._segment_path = lambda: "interface"
                                    self._is_frozen = True


                        class Area(Entity):
                            """
                            List of ospf areas
                            
                            .. attribute:: area_id  (key)
                            
                            	Area ID
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..4294967295
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                            
                            .. attribute:: area_type
                            
                            	Area type
                            	**type**\:  :py:class:`AreaType <ydk.models.ietf.ietf_ospf.AreaType>`
                            
                            	**default value**\: normal
                            
                            .. attribute:: summary
                            
                            	Enable/Disable summary generation to the stub or NSSA area
                            	**type**\: bool
                            
                            .. attribute:: default_cost
                            
                            	Set the summary default\-cost for a stub or NSSA area
                            	**type**\: int
                            
                            	**range:** 1..16777215
                            
                            .. attribute:: range
                            
                            	Summarize routes matching address/mask (border routers only)
                            	**type**\: list of  		 :py:class:`Range <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range>`
                            
                            .. attribute:: all_interfaces_inherit
                            
                            	Inheritance for all interfaces
                            	**type**\:  :py:class:`AllInterfacesInherit <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit>`
                            
                            .. attribute:: virtual_link
                            
                            	OSPF virtual link
                            	**type**\: list of  		 :py:class:`VirtualLink <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink>`
                            
                            .. attribute:: sham_link
                            
                            	OSPF sham link
                            	**type**\: list of  		 :py:class:`ShamLink <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink>`
                            
                            .. attribute:: interface
                            
                            	List of OSPF interfaces
                            	**type**\: list of  		 :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, self).__init__()

                                self.yang_name = "area"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['area_id']
                                self._child_classes = OrderedDict([("range", ("range", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range)), ("all-interfaces-inherit", ("all_interfaces_inherit", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit)), ("virtual-link", ("virtual_link", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink)), ("sham-link", ("sham_link", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink)), ("interface", ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface))])
                                self._leafs = OrderedDict([
                                    ('area_id', (YLeaf(YType.str, 'area-id'), ['int','str'])),
                                    ('area_type', (YLeaf(YType.identityref, 'area-type'), [('ydk.models.ietf.ietf_ospf', 'AreaType')])),
                                    ('summary', (YLeaf(YType.boolean, 'summary'), ['bool'])),
                                    ('default_cost', (YLeaf(YType.uint32, 'default-cost'), ['int'])),
                                ])
                                self.area_id = None
                                self.area_type = None
                                self.summary = None
                                self.default_cost = None

                                self.all_interfaces_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit()
                                self.all_interfaces_inherit.parent = self
                                self._children_name_map["all_interfaces_inherit"] = "all-interfaces-inherit"

                                self.range = YList(self)
                                self.virtual_link = YList(self)
                                self.sham_link = YList(self)
                                self.interface = YList(self)
                                self._segment_path = lambda: "area" + "[area-id='" + str(self.area_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area, ['area_id', 'area_type', 'summary', 'default_cost'], name, value)


                            class Range(Entity):
                                """
                                Summarize routes matching address/mask (border
                                routers only)
                                
                                .. attribute:: prefix  (key)
                                
                                	IPv4 or IPv6 prefix
                                	**type**\: str
                                
                                .. attribute:: advertise
                                
                                	Advertise or hide
                                	**type**\: bool
                                
                                .. attribute:: cost
                                
                                	Cost of summary route
                                	**type**\: int
                                
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
                                    self.ylist_key_names = ['prefix']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                        ('advertise', (YLeaf(YType.boolean, 'advertise'), ['bool'])),
                                        ('cost', (YLeaf(YType.uint32, 'cost'), ['int'])),
                                    ])
                                    self.prefix = None
                                    self.advertise = None
                                    self.cost = None
                                    self._segment_path = lambda: "range" + "[prefix='" + str(self.prefix) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range, ['prefix', 'advertise', 'cost'], name, value)


                            class AllInterfacesInherit(Entity):
                                """
                                Inheritance for all interfaces
                                
                                .. attribute:: interface
                                
                                	Interface config to be inherited by all interfaces
                                	**type**\:  :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit, self).__init__()

                                    self.yang_name = "all-interfaces-inherit"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("interface", ("interface", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface))])
                                    self._leafs = OrderedDict()

                                    self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface()
                                    self.interface.parent = self
                                    self._children_name_map["interface"] = "interface"
                                    self._segment_path = lambda: "all-interfaces-inherit"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit, [], name, value)


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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict()
                                        self._segment_path = lambda: "interface"
                                        self._is_frozen = True


                            class VirtualLink(Entity):
                                """
                                OSPF virtual link
                                
                                .. attribute:: router_id  (key)
                                
                                	Virtual link router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\: bool
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\: bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\: bool
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\: bool
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:  :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity>`
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\: bool
                                
                                	**default value**\: true
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:  :py:class:`Authentication <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink, self).__init__()

                                    self.yang_name = "virtual-link"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['router_id']
                                    self._child_classes = OrderedDict([("ttl-security", ("ttl_security", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity)), ("authentication", ("authentication", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication))])
                                    self._leafs = OrderedDict([
                                        ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                        ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                        ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                        ('dead_interval', (YLeaf(YType.uint16, 'dead-interval'), ['int'])),
                                        ('retransmit_interval', (YLeaf(YType.uint16, 'retransmit-interval'), ['int'])),
                                        ('transmit_delay', (YLeaf(YType.uint16, 'transmit-delay'), ['int'])),
                                        ('mtu_ignore', (YLeaf(YType.boolean, 'mtu-ignore'), ['bool'])),
                                        ('lls', (YLeaf(YType.boolean, 'lls'), ['bool'])),
                                        ('prefix_suppression', (YLeaf(YType.boolean, 'prefix-suppression'), ['bool'])),
                                        ('bfd', (YLeaf(YType.boolean, 'bfd'), ['bool'])),
                                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ])
                                    self.router_id = None
                                    self.cost = None
                                    self.hello_interval = None
                                    self.dead_interval = None
                                    self.retransmit_interval = None
                                    self.transmit_delay = None
                                    self.mtu_ignore = None
                                    self.lls = None
                                    self.prefix_suppression = None
                                    self.bfd = None
                                    self.enable = None

                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"

                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"
                                    self._segment_path = lambda: "virtual-link" + "[router-id='" + str(self.router_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink, ['router_id', 'cost', 'hello_interval', 'dead_interval', 'retransmit_interval', 'transmit_delay', 'mtu_ignore', 'lls', 'prefix_suppression', 'bfd', 'enable'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\: bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('hops', (YLeaf(YType.uint8, 'hops'), ['int'])),
                                        ])
                                        self.enable = None
                                        self.hops = None
                                        self._segment_path = lambda: "ttl-security"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity, ['enable', 'hops'], name, value)


                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\: str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\: str
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:  :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "virtual-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("crypto-algorithm", ("crypto_algorithm", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm))])
                                        self._leafs = OrderedDict([
                                            ('sa', (YLeaf(YType.str, 'sa'), ['str'])),
                                            ('key_chain', (YLeaf(YType.str, 'key-chain'), ['str'])),
                                            ('key', (YLeaf(YType.str, 'key'), ['str'])),
                                        ])
                                        self.sa = None
                                        self.key_chain = None
                                        self.key = None

                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._segment_path = lambda: "authentication"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication, ['sa', 'key_chain', 'key'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('hmac_sha1_12', (YLeaf(YType.empty, 'hmac-sha1-12'), ['Empty'])),
                                                ('hmac_sha1_20', (YLeaf(YType.empty, 'hmac-sha1-20'), ['Empty'])),
                                                ('md5', (YLeaf(YType.empty, 'md5'), ['Empty'])),
                                                ('sha_1', (YLeaf(YType.empty, 'sha-1'), ['Empty'])),
                                                ('hmac_sha_1', (YLeaf(YType.empty, 'hmac-sha-1'), ['Empty'])),
                                                ('hmac_sha_256', (YLeaf(YType.empty, 'hmac-sha-256'), ['Empty'])),
                                                ('hmac_sha_384', (YLeaf(YType.empty, 'hmac-sha-384'), ['Empty'])),
                                                ('hmac_sha_512', (YLeaf(YType.empty, 'hmac-sha-512'), ['Empty'])),
                                            ])
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.md5 = None
                                            self.sha_1 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self._segment_path = lambda: "crypto-algorithm"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'md5', 'sha_1', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512'], name, value)


                            class ShamLink(Entity):
                                """
                                OSPF sham link
                                
                                .. attribute:: local_id  (key)
                                
                                	Address of the local end\-point
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: remote_id  (key)
                                
                                	Address of the remote end\-point
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\: bool
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\: bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\: bool
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\: bool
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:  :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity>`
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\: bool
                                
                                	**default value**\: true
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:  :py:class:`Authentication <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink, self).__init__()

                                    self.yang_name = "sham-link"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['local_id','remote_id']
                                    self._child_classes = OrderedDict([("ttl-security", ("ttl_security", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity)), ("authentication", ("authentication", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication))])
                                    self._leafs = OrderedDict([
                                        ('local_id', (YLeaf(YType.str, 'local-id'), ['str','str'])),
                                        ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str','str'])),
                                        ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                        ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                        ('dead_interval', (YLeaf(YType.uint16, 'dead-interval'), ['int'])),
                                        ('retransmit_interval', (YLeaf(YType.uint16, 'retransmit-interval'), ['int'])),
                                        ('transmit_delay', (YLeaf(YType.uint16, 'transmit-delay'), ['int'])),
                                        ('mtu_ignore', (YLeaf(YType.boolean, 'mtu-ignore'), ['bool'])),
                                        ('lls', (YLeaf(YType.boolean, 'lls'), ['bool'])),
                                        ('prefix_suppression', (YLeaf(YType.boolean, 'prefix-suppression'), ['bool'])),
                                        ('bfd', (YLeaf(YType.boolean, 'bfd'), ['bool'])),
                                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ])
                                    self.local_id = None
                                    self.remote_id = None
                                    self.cost = None
                                    self.hello_interval = None
                                    self.dead_interval = None
                                    self.retransmit_interval = None
                                    self.transmit_delay = None
                                    self.mtu_ignore = None
                                    self.lls = None
                                    self.prefix_suppression = None
                                    self.bfd = None
                                    self.enable = None

                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"

                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"
                                    self._segment_path = lambda: "sham-link" + "[local-id='" + str(self.local_id) + "']" + "[remote-id='" + str(self.remote_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink, ['local_id', 'remote_id', 'cost', 'hello_interval', 'dead_interval', 'retransmit_interval', 'transmit_delay', 'mtu_ignore', 'lls', 'prefix_suppression', 'bfd', 'enable'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\: bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('hops', (YLeaf(YType.uint8, 'hops'), ['int'])),
                                        ])
                                        self.enable = None
                                        self.hops = None
                                        self._segment_path = lambda: "ttl-security"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity, ['enable', 'hops'], name, value)


                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\: str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\: str
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:  :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "sham-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("crypto-algorithm", ("crypto_algorithm", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm))])
                                        self._leafs = OrderedDict([
                                            ('sa', (YLeaf(YType.str, 'sa'), ['str'])),
                                            ('key_chain', (YLeaf(YType.str, 'key-chain'), ['str'])),
                                            ('key', (YLeaf(YType.str, 'key'), ['str'])),
                                        ])
                                        self.sa = None
                                        self.key_chain = None
                                        self.key = None

                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._segment_path = lambda: "authentication"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication, ['sa', 'key_chain', 'key'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('hmac_sha1_12', (YLeaf(YType.empty, 'hmac-sha1-12'), ['Empty'])),
                                                ('hmac_sha1_20', (YLeaf(YType.empty, 'hmac-sha1-20'), ['Empty'])),
                                                ('md5', (YLeaf(YType.empty, 'md5'), ['Empty'])),
                                                ('sha_1', (YLeaf(YType.empty, 'sha-1'), ['Empty'])),
                                                ('hmac_sha_1', (YLeaf(YType.empty, 'hmac-sha-1'), ['Empty'])),
                                                ('hmac_sha_256', (YLeaf(YType.empty, 'hmac-sha-256'), ['Empty'])),
                                                ('hmac_sha_384', (YLeaf(YType.empty, 'hmac-sha-384'), ['Empty'])),
                                                ('hmac_sha_512', (YLeaf(YType.empty, 'hmac-sha-512'), ['Empty'])),
                                            ])
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.md5 = None
                                            self.sha_1 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self._segment_path = lambda: "crypto-algorithm"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'md5', 'sha_1', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512'], name, value)


                            class Interface(Entity):
                                """
                                List of OSPF interfaces.
                                
                                .. attribute:: interface  (key)
                                
                                	Interface
                                	**type**\: str
                                
                                	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                                
                                .. attribute:: network_type
                                
                                	Network type
                                	**type**\:  :py:class:`NetworkType <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.NetworkType>`
                                
                                .. attribute:: passive
                                
                                	Enable/Disable passive
                                	**type**\: bool
                                
                                .. attribute:: demand_circuit
                                
                                	Enable/Disable demand circuit
                                	**type**\: bool
                                
                                .. attribute:: multi_area
                                
                                	Configure ospf multi\-area
                                	**type**\:  :py:class:`MultiArea <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea>`
                                
                                .. attribute:: static_neighbors
                                
                                	Static configured neighbors
                                	**type**\:  :py:class:`StaticNeighbors <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors>`
                                
                                .. attribute:: node_flag
                                
                                	Set prefix as a node representative prefix
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: fast_reroute
                                
                                	Fast\-reroute configuration
                                	**type**\:  :py:class:`FastReroute <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute>`
                                
                                .. attribute:: cost
                                
                                	Interface cost
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                .. attribute:: hello_interval
                                
                                	Time between hello packets
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: dead_interval
                                
                                	Interval after which a neighbor is declared dead
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: retransmit_interval
                                
                                	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: transmit_delay
                                
                                	Estimated time needed to send link\-state update
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: seconds
                                
                                .. attribute:: mtu_ignore
                                
                                	Enable/Disable ignoring of MTU in DBD packets
                                	**type**\: bool
                                
                                .. attribute:: lls
                                
                                	Enable/Disable link\-local signaling (LLS) support
                                	**type**\: bool
                                
                                .. attribute:: prefix_suppression
                                
                                	Suppress advertisement of the prefixes
                                	**type**\: bool
                                
                                .. attribute:: bfd
                                
                                	Enable/disable bfd
                                	**type**\: bool
                                
                                .. attribute:: ttl_security
                                
                                	TTL security check
                                	**type**\:  :py:class:`TtlSecurity <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity>`
                                
                                .. attribute:: enable
                                
                                	Enable/disable protocol on the interface
                                	**type**\: bool
                                
                                	**default value**\: true
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:  :py:class:`Authentication <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication>`
                                
                                .. attribute:: topology
                                
                                	OSPF interface topology
                                	**type**\: list of  		 :py:class:`Topology <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface, self).__init__()

                                    self.yang_name = "interface"
                                    self.yang_parent_name = "area"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface']
                                    self._child_classes = OrderedDict([("multi-area", ("multi_area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea)), ("static-neighbors", ("static_neighbors", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors)), ("fast-reroute", ("fast_reroute", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute)), ("ttl-security", ("ttl_security", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity)), ("authentication", ("authentication", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication)), ("topology", ("topology", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology))])
                                    self._leafs = OrderedDict([
                                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                        ('network_type', (YLeaf(YType.enumeration, 'network-type'), [('ydk.models.ietf.ietf_routing', 'Routing', 'RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.NetworkType')])),
                                        ('passive', (YLeaf(YType.boolean, 'passive'), ['bool'])),
                                        ('demand_circuit', (YLeaf(YType.boolean, 'demand-circuit'), ['bool'])),
                                        ('node_flag', (YLeaf(YType.boolean, 'node-flag'), ['bool'])),
                                        ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                        ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                                        ('dead_interval', (YLeaf(YType.uint16, 'dead-interval'), ['int'])),
                                        ('retransmit_interval', (YLeaf(YType.uint16, 'retransmit-interval'), ['int'])),
                                        ('transmit_delay', (YLeaf(YType.uint16, 'transmit-delay'), ['int'])),
                                        ('mtu_ignore', (YLeaf(YType.boolean, 'mtu-ignore'), ['bool'])),
                                        ('lls', (YLeaf(YType.boolean, 'lls'), ['bool'])),
                                        ('prefix_suppression', (YLeaf(YType.boolean, 'prefix-suppression'), ['bool'])),
                                        ('bfd', (YLeaf(YType.boolean, 'bfd'), ['bool'])),
                                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                    ])
                                    self.interface = None
                                    self.network_type = None
                                    self.passive = None
                                    self.demand_circuit = None
                                    self.node_flag = None
                                    self.cost = None
                                    self.hello_interval = None
                                    self.dead_interval = None
                                    self.retransmit_interval = None
                                    self.transmit_delay = None
                                    self.mtu_ignore = None
                                    self.lls = None
                                    self.prefix_suppression = None
                                    self.bfd = None
                                    self.enable = None

                                    self.multi_area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea()
                                    self.multi_area.parent = self
                                    self._children_name_map["multi_area"] = "multi-area"

                                    self.static_neighbors = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors()
                                    self.static_neighbors.parent = self
                                    self._children_name_map["static_neighbors"] = "static-neighbors"

                                    self.fast_reroute = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute()
                                    self.fast_reroute.parent = self
                                    self._children_name_map["fast_reroute"] = "fast-reroute"

                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self._children_name_map["ttl_security"] = "ttl-security"

                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"

                                    self.topology = YList(self)
                                    self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface, ['interface', 'network_type', 'passive', 'demand_circuit', 'node_flag', 'cost', 'hello_interval', 'dead_interval', 'retransmit_interval', 'transmit_delay', 'mtu_ignore', 'lls', 'prefix_suppression', 'bfd', 'enable'], name, value)

                                class NetworkType(Enum):
                                    """
                                    NetworkType (Enum Class)

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



                                class MultiArea(Entity):
                                    """
                                    Configure ospf multi\-area.
                                    
                                    .. attribute:: multi_area_id
                                    
                                    	Multi\-area ID
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: int
                                    
                                    			**range:** 0..4294967295
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                    
                                    .. attribute:: cost
                                    
                                    	Interface cost for multi\-area
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea, self).__init__()

                                        self.yang_name = "multi-area"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('multi_area_id', (YLeaf(YType.str, 'multi-area-id'), ['int','str'])),
                                            ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                        ])
                                        self.multi_area_id = None
                                        self.cost = None
                                        self._segment_path = lambda: "multi-area"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea, ['multi_area_id', 'cost'], name, value)


                                class StaticNeighbors(Entity):
                                    """
                                    Static configured neighbors.
                                    
                                    .. attribute:: neighbor
                                    
                                    	Specify a neighbor router
                                    	**type**\: list of  		 :py:class:`Neighbor <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors, self).__init__()

                                        self.yang_name = "static-neighbors"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("neighbor", ("neighbor", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor))])
                                        self._leafs = OrderedDict()

                                        self.neighbor = YList(self)
                                        self._segment_path = lambda: "static-neighbors"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors, [], name, value)


                                    class Neighbor(Entity):
                                        """
                                        Specify a neighbor router.
                                        
                                        .. attribute:: address  (key)
                                        
                                        	Neighbor IP address
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: cost
                                        
                                        	Neighbor cost
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        .. attribute:: poll_interval
                                        
                                        	Neighbor poll interval
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        	**units**\: seconds
                                        
                                        .. attribute:: priority
                                        
                                        	Neighbor priority for DR election
                                        	**type**\: int
                                        
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
                                            self.ylist_key_names = ['address']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                                ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                                ('poll_interval', (YLeaf(YType.uint16, 'poll-interval'), ['int'])),
                                                ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                                            ])
                                            self.address = None
                                            self.cost = None
                                            self.poll_interval = None
                                            self.priority = None
                                            self._segment_path = lambda: "neighbor" + "[address='" + str(self.address) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor, ['address', 'cost', 'poll_interval', 'priority'], name, value)


                                class FastReroute(Entity):
                                    """
                                    Fast\-reroute configuration.
                                    
                                    .. attribute:: lfa
                                    
                                    	LFA configuration
                                    	**type**\:  :py:class:`Lfa <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute, self).__init__()

                                        self.yang_name = "fast-reroute"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lfa", ("lfa", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa))])
                                        self._leafs = OrderedDict()

                                        self.lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa()
                                        self.lfa.parent = self
                                        self._children_name_map["lfa"] = "lfa"
                                        self._segment_path = lambda: "fast-reroute"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute, [], name, value)


                                    class Lfa(Entity):
                                        """
                                        LFA configuration.
                                        
                                        .. attribute:: candidate_disabled
                                        
                                        	Prevent the interface to be used as backup
                                        	**type**\: bool
                                        
                                        .. attribute:: enabled
                                        
                                        	Activates LFA. This model assumes activation of per\-prefix LFA
                                        	**type**\: bool
                                        
                                        .. attribute:: remote_lfa
                                        
                                        	Remote LFA configuration
                                        	**type**\:  :py:class:`RemoteLfa <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa, self).__init__()

                                            self.yang_name = "lfa"
                                            self.yang_parent_name = "fast-reroute"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("remote-lfa", ("remote_lfa", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa))])
                                            self._leafs = OrderedDict([
                                                ('candidate_disabled', (YLeaf(YType.boolean, 'candidate-disabled'), ['bool'])),
                                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                            ])
                                            self.candidate_disabled = None
                                            self.enabled = None

                                            self.remote_lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa()
                                            self.remote_lfa.parent = self
                                            self._children_name_map["remote_lfa"] = "remote-lfa"
                                            self._segment_path = lambda: "lfa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa, ['candidate_disabled', 'enabled'], name, value)


                                        class RemoteLfa(Entity):
                                            """
                                            Remote LFA configuration.
                                            
                                            .. attribute:: enabled
                                            
                                            	Activates remote LFA
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa, self).__init__()

                                                self.yang_name = "remote-lfa"
                                                self.yang_parent_name = "lfa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                                ])
                                                self.enabled = None
                                                self._segment_path = lambda: "remote-lfa"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa, ['enabled'], name, value)


                                class TtlSecurity(Entity):
                                    """
                                    TTL security check.
                                    
                                    .. attribute:: enable
                                    
                                    	Enable/Disable TTL security check
                                    	**type**\: bool
                                    
                                    .. attribute:: hops
                                    
                                    	Maximum number of hops that a OSPF packet may have traveled
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('hops', (YLeaf(YType.uint8, 'hops'), ['int'])),
                                        ])
                                        self.enable = None
                                        self.hops = None
                                        self._segment_path = lambda: "ttl-security"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity, ['enable', 'hops'], name, value)


                                class Authentication(Entity):
                                    """
                                    Authentication configuration.
                                    
                                    .. attribute:: sa
                                    
                                    	SA name
                                    	**type**\: str
                                    
                                    .. attribute:: key_chain
                                    
                                    	key\-chain name
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_key_chain.KeyChains>`
                                    
                                    .. attribute:: key
                                    
                                    	Key string in ASCII format
                                    	**type**\: str
                                    
                                    .. attribute:: crypto_algorithm
                                    
                                    	Cryptographic algorithm associated with key
                                    	**type**\:  :py:class:`CryptoAlgorithm <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("crypto-algorithm", ("crypto_algorithm", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm))])
                                        self._leafs = OrderedDict([
                                            ('sa', (YLeaf(YType.str, 'sa'), ['str'])),
                                            ('key_chain', (YLeaf(YType.str, 'key-chain'), ['str'])),
                                            ('key', (YLeaf(YType.str, 'key'), ['str'])),
                                        ])
                                        self.sa = None
                                        self.key_chain = None
                                        self.key = None

                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self._children_name_map["crypto_algorithm"] = "crypto-algorithm"
                                        self._segment_path = lambda: "authentication"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication, ['sa', 'key_chain', 'key'], name, value)


                                    class CryptoAlgorithm(Entity):
                                        """
                                        Cryptographic algorithm associated with key.
                                        
                                        .. attribute:: hmac_sha1_12
                                        
                                        	The HMAC\-SHA1\-12 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha1_20
                                        
                                        	The HMAC\-SHA1\-20 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: md5
                                        
                                        	The MD5 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: sha_1
                                        
                                        	The SHA\-1 algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_1
                                        
                                        	HMAC\-SHA\-1 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_256
                                        
                                        	HMAC\-SHA\-256 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_384
                                        
                                        	HMAC\-SHA\-384 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: hmac_sha_512
                                        
                                        	HMAC\-SHA\-512 authentication algorithm
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        

                                        """

                                        _prefix = 'ospf'
                                        _revision = '2015-03-09'

                                        def __init__(self):
                                            super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm, self).__init__()

                                            self.yang_name = "crypto-algorithm"
                                            self.yang_parent_name = "authentication"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('hmac_sha1_12', (YLeaf(YType.empty, 'hmac-sha1-12'), ['Empty'])),
                                                ('hmac_sha1_20', (YLeaf(YType.empty, 'hmac-sha1-20'), ['Empty'])),
                                                ('md5', (YLeaf(YType.empty, 'md5'), ['Empty'])),
                                                ('sha_1', (YLeaf(YType.empty, 'sha-1'), ['Empty'])),
                                                ('hmac_sha_1', (YLeaf(YType.empty, 'hmac-sha-1'), ['Empty'])),
                                                ('hmac_sha_256', (YLeaf(YType.empty, 'hmac-sha-256'), ['Empty'])),
                                                ('hmac_sha_384', (YLeaf(YType.empty, 'hmac-sha-384'), ['Empty'])),
                                                ('hmac_sha_512', (YLeaf(YType.empty, 'hmac-sha-512'), ['Empty'])),
                                            ])
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.md5 = None
                                            self.sha_1 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self._segment_path = lambda: "crypto-algorithm"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm, ['hmac_sha1_12', 'hmac_sha1_20', 'md5', 'sha_1', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512'], name, value)


                                class Topology(Entity):
                                    """
                                    OSPF interface topology.
                                    
                                    .. attribute:: name  (key)
                                    
                                    	One of the topology enabled on this interface
                                    	**type**\: str
                                    
                                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
                                    
                                    .. attribute:: cost
                                    
                                    	Interface cost for this topology
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = ['name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('cost', (YLeaf(YType.uint32, 'cost'), ['int'])),
                                        ])
                                        self.name = None
                                        self.cost = None
                                        self._segment_path = lambda: "topology" + "[name='" + str(self.name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology, ['name', 'cost'], name, value)


                        class Topology(Entity):
                            """
                            OSPF topology.
                            
                            .. attribute:: name  (key)
                            
                            	RIB
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
                            
                            .. attribute:: area
                            
                            	List of ospf areas
                            	**type**\: list of  		 :py:class:`Area <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area>`
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, self).__init__()

                                self.yang_name = "topology"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_classes = OrderedDict([("area", ("area", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area))])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.name = None

                                self.area = YList(self)
                                self._segment_path = lambda: "topology" + "[name='" + str(self.name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology, ['name'], name, value)


                            class Area(Entity):
                                """
                                List of ospf areas
                                
                                .. attribute:: area_id  (key)
                                
                                	Area ID
                                	**type**\: union of the below types:
                                
                                		**type**\: int
                                
                                			**range:** 0..4294967295
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])
                                
                                .. attribute:: area_type
                                
                                	Area type
                                	**type**\:  :py:class:`AreaType <ydk.models.ietf.ietf_ospf.AreaType>`
                                
                                	**default value**\: normal
                                
                                .. attribute:: summary
                                
                                	Enable/Disable summary generation to the stub or NSSA area
                                	**type**\: bool
                                
                                .. attribute:: default_cost
                                
                                	Set the summary default\-cost for a stub or NSSA area
                                	**type**\: int
                                
                                	**range:** 1..16777215
                                
                                .. attribute:: range
                                
                                	Summarize routes matching address/mask (border routers only)
                                	**type**\: list of  		 :py:class:`Range <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    super(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, self).__init__()

                                    self.yang_name = "area"
                                    self.yang_parent_name = "topology"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['area_id']
                                    self._child_classes = OrderedDict([("range", ("range", Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range))])
                                    self._leafs = OrderedDict([
                                        ('area_id', (YLeaf(YType.str, 'area-id'), ['int','str'])),
                                        ('area_type', (YLeaf(YType.identityref, 'area-type'), [('ydk.models.ietf.ietf_ospf', 'AreaType')])),
                                        ('summary', (YLeaf(YType.boolean, 'summary'), ['bool'])),
                                        ('default_cost', (YLeaf(YType.uint32, 'default-cost'), ['int'])),
                                    ])
                                    self.area_id = None
                                    self.area_type = None
                                    self.summary = None
                                    self.default_cost = None

                                    self.range = YList(self)
                                    self._segment_path = lambda: "area" + "[area-id='" + str(self.area_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area, ['area_id', 'area_type', 'summary', 'default_cost'], name, value)


                                class Range(Entity):
                                    """
                                    Summarize routes matching address/mask (border
                                    routers only)
                                    
                                    .. attribute:: prefix  (key)
                                    
                                    	IPv4 or IPv6 prefix
                                    	**type**\: str
                                    
                                    .. attribute:: advertise
                                    
                                    	Advertise or hide
                                    	**type**\: bool
                                    
                                    .. attribute:: cost
                                    
                                    	Cost of summary route
                                    	**type**\: int
                                    
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
                                        self.ylist_key_names = ['prefix']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                            ('advertise', (YLeaf(YType.boolean, 'advertise'), ['bool'])),
                                            ('cost', (YLeaf(YType.uint32, 'cost'), ['int'])),
                                        ])
                                        self.prefix = None
                                        self.advertise = None
                                        self.cost = None
                                        self._segment_path = lambda: "range" + "[prefix='" + str(self.prefix) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range, ['prefix', 'advertise', 'cost'], name, value)


        class Ribs(Entity):
            """
            Configuration of RIBs.
            
            .. attribute:: rib
            
            	Each entry contains configuration for a RIB identified by the 'name' key.  Entries having the same key as a system\-controlled entry of the list /routing\-state/routing\-instance/ribs/rib are used for configuring parameters of that entry. Other entries define additional user\-controlled RIBs
            	**type**\: list of  		 :py:class:`Rib <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(Routing.RoutingInstance.Ribs, self).__init__()

                self.yang_name = "ribs"
                self.yang_parent_name = "routing-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rib", ("rib", Routing.RoutingInstance.Ribs.Rib))])
                self._leafs = OrderedDict()

                self.rib = YList(self)
                self._segment_path = lambda: "ribs"
                self._is_frozen = True

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
                
                .. attribute:: name  (key)
                
                	The name of the RIB.  For system\-controlled entries, the value of this leaf must be the same as the name of the corresponding entry in state data.  For user\-controlled entries, an arbitrary name can be used
                	**type**\: str
                
                .. attribute:: address_family
                
                	Address family
                	**type**\:  :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
                
                .. attribute:: description
                
                	Textual description of the RIB
                	**type**\: str
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(Routing.RoutingInstance.Ribs.Rib, self).__init__()

                    self.yang_name = "rib"
                    self.yang_parent_name = "ribs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('address_family', (YLeaf(YType.identityref, 'address-family'), [('ydk.models.ietf.ietf_routing', 'AddressFamily')])),
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                    ])
                    self.name = None
                    self.address_family = None
                    self.description = None
                    self._segment_path = lambda: "rib" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Routing.RoutingInstance.Ribs.Rib, [u'name', u'address_family', u'description'], name, value)

    def clone_ptr(self):
        self._top_entity = Routing()
        return self._top_entity

class FibRoute(Entity):
    """
    Return the active FIB route that a routing\-instance uses for
    sending packets to a destination address.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.ietf.ietf_routing.FibRoute.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.ietf.ietf_routing.FibRoute.Output>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = FibRoute.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"

        self.output = FibRoute.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._segment_path = lambda: "ietf-routing:fib-route"
        self._is_frozen = True


    class Input(Entity):
        """
        
        
        .. attribute:: routing_instance_name
        
        	Name of the routing instance whose forwarding information base is being queried.  If the routing instance with name equal to the value of this parameter doesn't exist, then this operation SHALL fail with error\-tag 'data\-missing' and error\-app\-tag 'routing\-instance\-not\-found'
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: destination_address
        
        	Network layer destination address.  Address family specific modules MUST augment this container with a leaf named 'address'
        	**type**\:  :py:class:`DestinationAddress <ydk.models.ietf.ietf_routing.FibRoute.Input.DestinationAddress>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(FibRoute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "fib-route"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("destination-address", ("destination_address", FibRoute.Input.DestinationAddress))])
            self._leafs = OrderedDict([
                ('routing_instance_name', (YLeaf(YType.str, 'routing-instance-name'), ['str'])),
            ])
            self.routing_instance_name = None

            self.destination_address = FibRoute.Input.DestinationAddress()
            self.destination_address.parent = self
            self._children_name_map["destination_address"] = "destination-address"
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "ietf-routing:fib-route/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FibRoute.Input, [u'routing_instance_name'], name, value)


        class DestinationAddress(Entity):
            """
            Network layer destination address.
            
            Address family specific modules MUST augment this
            container with a leaf named 'address'.
            
            .. attribute:: address_family
            
            	Address family
            	**type**\:  :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
            
            	**mandatory**\: True
            
            .. attribute:: ietf_ipv6_unicast_routing_address
            
            	IPv6 destination address
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ietf_ipv4_unicast_routing_address
            
            	IPv4 destination address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(FibRoute.Input.DestinationAddress, self).__init__()

                self.yang_name = "destination-address"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('address_family', (YLeaf(YType.identityref, 'address-family'), [('ydk.models.ietf.ietf_routing', 'AddressFamily')])),
                    ('ietf_ipv6_unicast_routing_address', (YLeaf(YType.str, 'ietf-ipv6-unicast-routing:address'), ['str'])),
                    ('ietf_ipv4_unicast_routing_address', (YLeaf(YType.str, 'ietf-ipv4-unicast-routing:address'), ['str'])),
                ])
                self.address_family = None
                self.ietf_ipv6_unicast_routing_address = None
                self.ietf_ipv4_unicast_routing_address = None
                self._segment_path = lambda: "destination-address"
                self._absolute_path = lambda: "ietf-routing:fib-route/input/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FibRoute.Input.DestinationAddress, [u'address_family', 'ietf_ipv6_unicast_routing_address', 'ietf_ipv4_unicast_routing_address'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: route
        
        	The active FIB route for the specified destination.  If the routing instance has no active FIB route for the destination address, no output is returned \- the server SHALL send an <rpc\-reply> containing a single element <ok>.  Address family specific modules MUST augment this list with appropriate route contents
        	**type**\:  :py:class:`Route <ydk.models.ietf.ietf_routing.FibRoute.Output.Route>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            super(FibRoute.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "fib-route"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("route", ("route", FibRoute.Output.Route))])
            self._leafs = OrderedDict()

            self.route = FibRoute.Output.Route()
            self.route.parent = self
            self._children_name_map["route"] = "route"
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "ietf-routing:fib-route/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FibRoute.Output, [], name, value)


        class Route(Entity):
            """
            The active FIB route for the specified destination.
            
            If the routing instance has no active FIB route for the
            destination address, no output is returned \- the server
            SHALL send an <rpc\-reply> containing a single element
            <ok>.
            
            Address family specific modules MUST augment this list
            with appropriate route contents.
            
            .. attribute:: address_family
            
            	Address family
            	**type**\:  :py:class:`AddressFamily <ydk.models.ietf.ietf_routing.AddressFamily>`
            
            	**mandatory**\: True
            
            .. attribute:: next_hop
            
            	Route's next\-hop attribute
            	**type**\:  :py:class:`NextHop <ydk.models.ietf.ietf_routing.FibRoute.Output.Route.NextHop>`
            
            .. attribute:: source_protocol
            
            	Type of the routing protocol from which the route originated
            	**type**\:  :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingProtocol>`
            
            	**mandatory**\: True
            
            .. attribute:: active
            
            	Presence of this leaf indicates that the route is preferred among all routes in the same RIB that have the same destination prefix
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: last_updated
            
            	Time stamp of the last modification of the route. If the route was never modified, it is the time when the route was inserted into the RIB
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: ietf_ipv6_unicast_routing_destination_prefix
            
            	IPv6 destination prefix
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(/(([0\-9])\|([0\-9]{2})\|(1[0\-1][0\-9])\|(12[0\-8])))
            
            .. attribute:: ietf_ipv4_unicast_routing_destination_prefix
            
            	IPv4 destination prefix
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])/(([0\-9])\|([1\-2][0\-9])\|(3[0\-2]))
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                super(FibRoute.Output.Route, self).__init__()

                self.yang_name = "route"
                self.yang_parent_name = "output"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("next-hop", ("next_hop", FibRoute.Output.Route.NextHop))])
                self._leafs = OrderedDict([
                    ('address_family', (YLeaf(YType.identityref, 'address-family'), [('ydk.models.ietf.ietf_routing', 'AddressFamily')])),
                    ('source_protocol', (YLeaf(YType.identityref, 'source-protocol'), [('ydk.models.ietf.ietf_routing', 'RoutingProtocol')])),
                    ('active', (YLeaf(YType.empty, 'active'), ['Empty'])),
                    ('last_updated', (YLeaf(YType.str, 'last-updated'), ['str'])),
                    ('ietf_ipv6_unicast_routing_destination_prefix', (YLeaf(YType.str, 'ietf-ipv6-unicast-routing:destination-prefix'), ['str'])),
                    ('ietf_ipv4_unicast_routing_destination_prefix', (YLeaf(YType.str, 'ietf-ipv4-unicast-routing:destination-prefix'), ['str'])),
                ])
                self.address_family = None
                self.source_protocol = None
                self.active = None
                self.last_updated = None
                self.ietf_ipv6_unicast_routing_destination_prefix = None
                self.ietf_ipv4_unicast_routing_destination_prefix = None

                self.next_hop = FibRoute.Output.Route.NextHop()
                self.next_hop.parent = self
                self._children_name_map["next_hop"] = "next-hop"
                self._segment_path = lambda: "route"
                self._absolute_path = lambda: "ietf-routing:fib-route/output/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FibRoute.Output.Route, [u'address_family', u'source_protocol', u'active', u'last_updated', 'ietf_ipv6_unicast_routing_destination_prefix', 'ietf_ipv4_unicast_routing_destination_prefix'], name, value)


            class NextHop(Entity):
                """
                Route's next\-hop attribute.
                
                .. attribute:: outgoing_interface
                
                	Name of the outgoing interface
                	**type**\: str
                
                .. attribute:: ietf_routing_next_hop_address
                
                	IP address
                	**type**\: str
                
                .. attribute:: ietf_ipv6_unicast_routing_next_hop_address
                
                	IPv6 address of the next\-hop
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ietf_ipv4_unicast_routing_next_hop_address
                
                	IPv4 address of the next\-hop
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: special_next_hop
                
                	Special next\-hop options
                	**type**\:  :py:class:`SpecialNextHop <ydk.models.ietf.ietf_routing.FibRoute.Output.Route.NextHop.SpecialNextHop>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    super(FibRoute.Output.Route.NextHop, self).__init__()

                    self.yang_name = "next-hop"
                    self.yang_parent_name = "route"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('outgoing_interface', (YLeaf(YType.str, 'outgoing-interface'), ['str'])),
                        ('ietf_routing_next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str'])),
                        ('ietf_ipv6_unicast_routing_next_hop_address', (YLeaf(YType.str, 'ietf-ipv6-unicast-routing:next-hop-address'), ['str'])),
                        ('ietf_ipv4_unicast_routing_next_hop_address', (YLeaf(YType.str, 'ietf-ipv4-unicast-routing:next-hop-address'), ['str'])),
                        ('special_next_hop', (YLeaf(YType.enumeration, 'special-next-hop'), [('ydk.models.ietf.ietf_routing', 'FibRoute', 'Output.Route.NextHop.SpecialNextHop')])),
                    ])
                    self.outgoing_interface = None
                    self.ietf_routing_next_hop_address = None
                    self.ietf_ipv6_unicast_routing_next_hop_address = None
                    self.ietf_ipv4_unicast_routing_next_hop_address = None
                    self.special_next_hop = None
                    self._segment_path = lambda: "next-hop"
                    self._absolute_path = lambda: "ietf-routing:fib-route/output/route/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(FibRoute.Output.Route.NextHop, [u'outgoing_interface', u'ietf_routing_next_hop_address', 'ietf_ipv6_unicast_routing_next_hop_address', 'ietf_ipv4_unicast_routing_next_hop_address', u'special_next_hop'], name, value)

                class SpecialNextHop(Enum):
                    """
                    SpecialNextHop (Enum Class)

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

class VrfRoutingInstance(RoutingInstance):
    """
    This identity represents a VRF routing instance. The type is
    distinct from the default\-routing\-instance. There may be
    multiple vrf\-routing\-interfaces.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:vrf-routing-instance"):
        super(VrfRoutingInstance, self).__init__(ns, pref, tag)


class Direct(RoutingProtocol):
    """
    Routing pseudo\-protocol that provides routes to directly
    connected networks.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:direct"):
        super(Direct, self).__init__(ns, pref, tag)


class DefaultRoutingInstance(RoutingInstance):
    """
    This identity represents either a default routing instance, or
    the only routing instance on systems that do not support
    multiple instances.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:default-routing-instance"):
        super(DefaultRoutingInstance, self).__init__(ns, pref, tag)


class Static(RoutingProtocol):
    """
    Static routing pseudo\-protocol.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:static"):
        super(Static, self).__init__(ns, pref, tag)


class Ipv4(AddressFamily):
    """
    This identity represents IPv4 address family.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:ipv4"):
        super(Ipv4, self).__init__(ns, pref, tag)


class Ipv6(AddressFamily):
    """
    This identity represents IPv6 address family.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self, ns="urn:ietf:params:xml:ns:yang:ietf-routing", pref="ietf-routing", tag="ietf-routing:ipv6"):
        super(Ipv6, self).__init__(ns, pref, tag)


