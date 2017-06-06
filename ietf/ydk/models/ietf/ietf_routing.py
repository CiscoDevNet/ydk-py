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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AddressFamilyIdentity(object):
    """
    Base identity from which identities describing address
    families are derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['AddressFamilyIdentity']['meta_info']


class RoutingProtocolIdentity(object):
    """
    Base identity from which routing protocol identities are
    derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['RoutingProtocolIdentity']['meta_info']


class RoutingInstanceIdentity(object):
    """
    Base identity from which identities describing routing
    instance types are derived.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        pass

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['RoutingInstanceIdentity']['meta_info']


class RoutingState(object):
    """
    State data of the routing subsystem.
    
    .. attribute:: routing_instance
    
    	Each list entry is a container for state data of a routing instance.  An implementation MUST support routing instance(s) of the type 'rt\:default\-routing\-instance', and MAY support other types. An implementation MAY restrict the number of routing instances of each supported type.  An implementation SHOULD create at least one system\-controlled instance, and MAY allow the clients to create user\-controlled routing instances in configuration
    	**type**\: list of    :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance>`
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        self.routing_instance = YList()
        self.routing_instance.parent = self
        self.routing_instance.name = 'routing_instance'


    class RoutingInstance(object):
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
        	**type**\:   :py:class:`RoutingInstanceIdentity <ydk.models.ietf.ietf_routing.RoutingInstanceIdentity>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            self.parent = None
            self.name = None
            self.interfaces = RoutingState.RoutingInstance.Interfaces()
            self.interfaces.parent = self
            self.ribs = RoutingState.RoutingInstance.Ribs()
            self.ribs.parent = self
            self.router_id = None
            self.routing_protocols = RoutingState.RoutingInstance.RoutingProtocols()
            self.routing_protocols.parent = self
            self.type = None


        class Interfaces(object):
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
                self.parent = None
                self.interface = YLeafList()
                self.interface.parent = self
                self.interface.name = 'interface'

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-routing:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.interface is not None:
                    for child in self.interface:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['RoutingState.RoutingInstance.Interfaces']['meta_info']


        class RoutingProtocols(object):
            """
            Container for the list of routing protocol instances.
            
            .. attribute:: routing_protocol
            
            	State data of a routing protocol instance.  An implementation MUST provide exactly one system\-controlled instance of the type 'direct'. Other instances MAY be created by configuration
            	**type**\: list of    :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                self.parent = None
                self.routing_protocol = YList()
                self.routing_protocol.parent = self
                self.routing_protocol.name = 'routing_protocol'


            class RoutingProtocol(object):
                """
                State data of a routing protocol instance.
                
                An implementation MUST provide exactly one
                system\-controlled instance of the type 'direct'. Other
                instances MAY be created by configuration.
                
                .. attribute:: type  <key>
                
                	Type of the routing protocol
                	**type**\:   :py:class:`RoutingProtocolIdentity <ydk.models.ietf.ietf_routing.RoutingProtocolIdentity>`
                
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
                    self.parent = None
                    self.type = None
                    self.name = None
                    self.ospf = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf()
                    self.ospf.parent = self


                class Ospf(object):
                    """
                    OSPF
                    
                    .. attribute:: instance
                    
                    	An OSPF routing protocol instance
                    	**type**\: list of    :py:class:`Instance <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance>`
                    
                    .. attribute:: operation_mode
                    
                    	OSPF operation mode
                    	**type**\:   :py:class:`OperationModeIdentity <ydk.models.ietf.ietf_ospf.OperationModeIdentity>`
                    
                    

                    """

                    _prefix = 'ospf'
                    _revision = '2015-03-09'

                    def __init__(self):
                        self.parent = None
                        self.instance = YList()
                        self.instance.parent = self
                        self.instance.name = 'instance'
                        self.operation_mode = None


                    class Instance(object):
                        """
                        An OSPF routing protocol instance.
                        
                        .. attribute:: af  <key>
                        
                        	Address\-family of the instance
                        	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_routing.AddressFamilyIdentity>`
                        
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
                            self.parent = None
                            self.af = None
                            self.area = YList()
                            self.area.parent = self
                            self.area.name = 'area'
                            self.as_scope_lsas = YList()
                            self.as_scope_lsas.parent = self
                            self.as_scope_lsas.name = 'as_scope_lsas'
                            self.router_id = None
                            self.topology = YList()
                            self.topology.parent = self
                            self.topology.name = 'topology'


                        class Area(object):
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
                                self.parent = None
                                self.area_id = None
                                self.area_scope_lsas = YList()
                                self.area_scope_lsas.parent = self
                                self.area_scope_lsas.name = 'area_scope_lsas'
                                self.interfaces = YList()
                                self.interfaces.parent = self
                                self.interfaces.name = 'interfaces'


                            class Interfaces(object):
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
                                	**type**\:   :py:class:`NetworkTypeEnum <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.NetworkTypeEnum>`
                                
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
                                    self.parent = None
                                    self.interface = None
                                    self.authentication = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication()
                                    self.authentication.parent = self
                                    self.bdr = None
                                    self.bfd = None
                                    self.cost = None
                                    self.dead_interval = None
                                    self.demand_circuit = None
                                    self.dr = None
                                    self.enable = None
                                    self.fast_reroute = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute()
                                    self.fast_reroute.parent = self
                                    self.hello_interval = None
                                    self.hello_timer = None
                                    self.link_scope_lsas = YList()
                                    self.link_scope_lsas.parent = self
                                    self.link_scope_lsas.name = 'link_scope_lsas'
                                    self.lls = None
                                    self.mtu_ignore = None
                                    self.multi_area = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea()
                                    self.multi_area.parent = self
                                    self.neighbor = YList()
                                    self.neighbor.parent = self
                                    self.neighbor.name = 'neighbor'
                                    self.network_type = None
                                    self.node_flag = None
                                    self.passive = None
                                    self.prefix_suppression = None
                                    self.retransmit_interval = None
                                    self.state = None
                                    self.static_neighbors = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors()
                                    self.static_neighbors.parent = self
                                    self.topology = YList()
                                    self.topology.parent = self
                                    self.topology.name = 'topology'
                                    self.transmit_delay = None
                                    self.ttl_security = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity()
                                    self.ttl_security.parent = self
                                    self.wait_timer = None

                                class NetworkTypeEnum(Enum):
                                    """
                                    NetworkTypeEnum

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

                                    broadcast = 0

                                    non_broadcast = 1

                                    point_to_multipoint = 2

                                    point_to_point = 3


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.NetworkTypeEnum']



                                class MultiArea(object):
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
                                        self.parent = None
                                        self.cost = None
                                        self.multi_area_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:multi-area'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.cost is not None:
                                            return True

                                        if self.multi_area_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea']['meta_info']


                                class StaticNeighbors(object):
                                    """
                                    Static configured neighbors.
                                    
                                    .. attribute:: neighbor
                                    
                                    	Specify a neighbor router
                                    	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.neighbor = YList()
                                        self.neighbor.parent = self
                                        self.neighbor.name = 'neighbor'


                                    class Neighbor(object):
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
                                            self.parent = None
                                            self.address = None
                                            self.cost = None
                                            self.poll_interval = None
                                            self.priority = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.address is None:
                                                raise YPYModelError('Key property address is None')

                                            return self.parent._common_path +'/ietf-ospf:neighbor[ietf-ospf:address = ' + str(self.address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.address is not None:
                                                return True

                                            if self.cost is not None:
                                                return True

                                            if self.poll_interval is not None:
                                                return True

                                            if self.priority is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:static-neighbors'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.neighbor is not None:
                                            for child_ref in self.neighbor:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors']['meta_info']


                                class FastReroute(object):
                                    """
                                    Fast\-reroute configuration.
                                    
                                    .. attribute:: lfa
                                    
                                    	LFA configuration
                                    	**type**\:   :py:class:`Lfa <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lfa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa()
                                        self.lfa.parent = self


                                    class Lfa(object):
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
                                            self.parent = None
                                            self.candidate_disabled = None
                                            self.enabled = None
                                            self.remote_lfa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa()
                                            self.remote_lfa.parent = self


                                        class RemoteLfa(object):
                                            """
                                            Remote LFA configuration.
                                            
                                            .. attribute:: enabled
                                            
                                            	Activates remote LFA
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.enabled = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:remote-lfa'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.enabled is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:lfa'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.candidate_disabled is not None:
                                                return True

                                            if self.enabled is not None:
                                                return True

                                            if self.remote_lfa is not None and self.remote_lfa._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:fast-reroute'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lfa is not None and self.lfa._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute']['meta_info']


                                class TtlSecurity(object):
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
                                        self.parent = None
                                        self.enable = None
                                        self.hops = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:ttl-security'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.enable is not None:
                                            return True

                                        if self.hops is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity']['meta_info']


                                class Authentication(object):
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
                                        self.parent = None
                                        self.crypto_algorithm = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self.key = None
                                        self.key_chain = None
                                        self.sa = None


                                    class CryptoAlgorithm(object):
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
                                            self.parent = None
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self.md5 = None
                                            self.sha_1 = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:crypto-algorithm'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.hmac_sha1_12 is not None:
                                                return True

                                            if self.hmac_sha1_20 is not None:
                                                return True

                                            if self.hmac_sha_1 is not None:
                                                return True

                                            if self.hmac_sha_256 is not None:
                                                return True

                                            if self.hmac_sha_384 is not None:
                                                return True

                                            if self.hmac_sha_512 is not None:
                                                return True

                                            if self.md5 is not None:
                                                return True

                                            if self.sha_1 is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:authentication'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.crypto_algorithm is not None and self.crypto_algorithm._has_data():
                                            return True

                                        if self.key is not None:
                                            return True

                                        if self.key_chain is not None:
                                            return True

                                        if self.sa is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication']['meta_info']


                                class Neighbor(object):
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
                                    	**type**\:   :py:class:`NbrStateTypeEnum <ydk.models.ietf.ietf_ospf.NbrStateTypeEnum>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.neighbor_id = None
                                        self.address = None
                                        self.bdr = None
                                        self.dr = None
                                        self.state = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.neighbor_id is None:
                                            raise YPYModelError('Key property neighbor_id is None')

                                        return self.parent._common_path +'/ietf-ospf:neighbor[ietf-ospf:neighbor-id = ' + str(self.neighbor_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.neighbor_id is not None:
                                            return True

                                        if self.address is not None:
                                            return True

                                        if self.bdr is not None:
                                            return True

                                        if self.dr is not None:
                                            return True

                                        if self.state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor']['meta_info']


                                class LinkScopeLsas(object):
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
                                        self.parent = None
                                        self.lsa_type = None
                                        self.link_scope_lsa = YList()
                                        self.link_scope_lsa.parent = self
                                        self.link_scope_lsa.name = 'link_scope_lsa'


                                    class LinkScopeLsa(object):
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
                                            self.parent = None
                                            self.lsa_id = None
                                            self.adv_router = None
                                            self.decoded_completed = None
                                            self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2()
                                            self.ospfv2.parent = self
                                            self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3()
                                            self.ospfv3.parent = self
                                            self.raw_data = None


                                        class Ospfv2(object):
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
                                                self.parent = None
                                                self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body()
                                                self.body.parent = self
                                                self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header()
                                                self.header.parent = self


                                            class Header(object):
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
                                                    self.parent = None
                                                    self.adv_router = None
                                                    self.age = None
                                                    self.checksum = None
                                                    self.length = None
                                                    self.lsa_id = None
                                                    self.opaque_id = None
                                                    self.opaque_type = None
                                                    self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header.Options()
                                                    self.seq_num = None
                                                    self.type = None

                                                class Options(FixedBitsDict):
                                                    """
                                                    Options

                                                    LSA option.
                                                    Keys are:- R , MC , DC , MT , E , P , Upward , AF

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'R':False,
                                                            'MC':False,
                                                            'DC':False,
                                                            'MT':False,
                                                            'E':False,
                                                            'P':False,
                                                            'Upward':False,
                                                            'AF':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:header'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.adv_router is not None:
                                                        return True

                                                    if self.age is not None:
                                                        return True

                                                    if self.checksum is not None:
                                                        return True

                                                    if self.length is not None:
                                                        return True

                                                    if self.lsa_id is not None:
                                                        return True

                                                    if self.opaque_id is not None:
                                                        return True

                                                    if self.opaque_type is not None:
                                                        return True

                                                    if self.options is not None:
                                                        if self.options._has_data():
                                                            return True

                                                    if self.seq_num is not None:
                                                        return True

                                                    if self.type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header']['meta_info']


                                            class Body(object):
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
                                                    self.parent = None
                                                    self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External()
                                                    self.external.parent = self
                                                    self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network()
                                                    self.network.parent = self
                                                    self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque()
                                                    self.opaque.parent = self
                                                    self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router()
                                                    self.router.parent = self
                                                    self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary()
                                                    self.summary.parent = self


                                                class Router(object):
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
                                                        self.parent = None
                                                        self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Flags()
                                                        self.link = YList()
                                                        self.link.parent = self
                                                        self.link.name = 'link'
                                                        self.num_of_links = None

                                                    class Flags(FixedBitsDict):
                                                        """
                                                        Flags

                                                        Flags
                                                        Keys are:- E , B , V

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'E':False,
                                                                'B':False,
                                                                'V':False,
                                                            }
                                                            self._pos_map = { 
                                                            }


                                                    class Link(object):
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
                                                            self.parent = None
                                                            self.link_id = None
                                                            self.link_data = None
                                                            self.topology = YList()
                                                            self.topology.parent = self
                                                            self.topology.name = 'topology'
                                                            self.type = None


                                                        class Topology(object):
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
                                                                self.parent = None
                                                                self.mt_id = None
                                                                self.metric = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                                if self.mt_id is None:
                                                                    raise YPYModelError('Key property mt_id is None')

                                                                return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.mt_id is not None:
                                                                    return True

                                                                if self.metric is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.link_id is None:
                                                                raise YPYModelError('Key property link_id is None')
                                                            if self.link_data is None:
                                                                raise YPYModelError('Key property link_data is None')

                                                            return self.parent._common_path +'/ietf-ospf:link[ietf-ospf:link-id = ' + str(self.link_id) + '][ietf-ospf:link-data = ' + str(self.link_data) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.link_id is not None:
                                                                return True

                                                            if self.link_data is not None:
                                                                return True

                                                            if self.topology is not None:
                                                                for child_ref in self.topology:
                                                                    if child_ref._has_data():
                                                                        return True

                                                            if self.type is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:router'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.flags is not None:
                                                            if self.flags._has_data():
                                                                return True

                                                        if self.link is not None:
                                                            for child_ref in self.link:
                                                                if child_ref._has_data():
                                                                    return True

                                                        if self.num_of_links is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router']['meta_info']


                                                class Network(object):
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
                                                        self.parent = None
                                                        self.attached_router = YLeafList()
                                                        self.attached_router.parent = self
                                                        self.attached_router.name = 'attached_router'
                                                        self.network_mask = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:network'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.attached_router is not None:
                                                            for child in self.attached_router:
                                                                if child is not None:
                                                                    return True

                                                        if self.network_mask is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network']['meta_info']


                                                class Summary(object):
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
                                                        self.parent = None
                                                        self.network_mask = None
                                                        self.topology = YList()
                                                        self.topology.parent = self
                                                        self.topology.name = 'topology'


                                                    class Topology(object):
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
                                                            self.parent = None
                                                            self.mt_id = None
                                                            self.metric = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.mt_id is None:
                                                                raise YPYModelError('Key property mt_id is None')

                                                            return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.mt_id is not None:
                                                                return True

                                                            if self.metric is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:summary'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.network_mask is not None:
                                                            return True

                                                        if self.topology is not None:
                                                            for child_ref in self.topology:
                                                                if child_ref._has_data():
                                                                    return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary']['meta_info']


                                                class External(object):
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
                                                        self.parent = None
                                                        self.network_mask = None
                                                        self.topology = YList()
                                                        self.topology.parent = self
                                                        self.topology.name = 'topology'


                                                    class Topology(object):
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
                                                            self.parent = None
                                                            self.mt_id = None
                                                            self.external_route_tag = None
                                                            self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology.Flags()
                                                            self.forwarding_address = None
                                                            self.metric = None

                                                        class Flags(FixedBitsDict):
                                                            """
                                                            Flags

                                                            Flags.
                                                            Keys are:- E

                                                            """

                                                            def __init__(self):
                                                                self._dictionary = { 
                                                                    'E':False,
                                                                }
                                                                self._pos_map = { 
                                                                }

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.mt_id is None:
                                                                raise YPYModelError('Key property mt_id is None')

                                                            return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.mt_id is not None:
                                                                return True

                                                            if self.external_route_tag is not None:
                                                                return True

                                                            if self.flags is not None:
                                                                if self.flags._has_data():
                                                                    return True

                                                            if self.forwarding_address is not None:
                                                                return True

                                                            if self.metric is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:external'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.network_mask is not None:
                                                            return True

                                                        if self.topology is not None:
                                                            for child_ref in self.topology:
                                                                if child_ref._has_data():
                                                                    return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External']['meta_info']


                                                class Opaque(object):
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
                                                        self.parent = None
                                                        self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                        self.link_tlv.parent = self
                                                        self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                        self.router_address_tlv.parent = self
                                                        self.unknown_tlv = YList()
                                                        self.unknown_tlv.parent = self
                                                        self.unknown_tlv.name = 'unknown_tlv'


                                                    class UnknownTlv(object):
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
                                                            self.parent = None
                                                            self.type = None
                                                            self.length = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.type is None:
                                                                raise YPYModelError('Key property type is None')

                                                            return self.parent._common_path +'/ietf-ospf:unknown-tlv[ietf-ospf:type = ' + str(self.type) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.type is not None:
                                                                return True

                                                            if self.length is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv']['meta_info']


                                                    class RouterAddressTlv(object):
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
                                                            self.parent = None
                                                            self.router_address = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/ietf-ospf:router-address-tlv'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.router_address is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv']['meta_info']


                                                    class LinkTlv(object):
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
                                                            self.parent = None
                                                            self.admin_group = None
                                                            self.link_id = None
                                                            self.link_type = None
                                                            self.local_if_ipv4_addr = YLeafList()
                                                            self.local_if_ipv4_addr.parent = self
                                                            self.local_if_ipv4_addr.name = 'local_if_ipv4_addr'
                                                            self.local_remote_ipv4_addr = YLeafList()
                                                            self.local_remote_ipv4_addr.parent = self
                                                            self.local_remote_ipv4_addr.name = 'local_remote_ipv4_addr'
                                                            self.max_bandwidth = None
                                                            self.max_reservable_bandwidth = None
                                                            self.te_metric = None
                                                            self.unknown_subtlv = YList()
                                                            self.unknown_subtlv.parent = self
                                                            self.unknown_subtlv.name = 'unknown_subtlv'
                                                            self.unreserved_bandwidth = None


                                                        class UnknownSubtlv(object):
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
                                                                self.parent = None
                                                                self.type = None
                                                                self.length = None
                                                                self.value = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                                if self.type is None:
                                                                    raise YPYModelError('Key property type is None')

                                                                return self.parent._common_path +'/ietf-ospf:unknown-subtlv[ietf-ospf:type = ' + str(self.type) + ']'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.type is not None:
                                                                    return True

                                                                if self.length is not None:
                                                                    return True

                                                                if self.value is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/ietf-ospf:link-tlv'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.admin_group is not None:
                                                                return True

                                                            if self.link_id is not None:
                                                                return True

                                                            if self.link_type is not None:
                                                                return True

                                                            if self.local_if_ipv4_addr is not None:
                                                                for child in self.local_if_ipv4_addr:
                                                                    if child is not None:
                                                                        return True

                                                            if self.local_remote_ipv4_addr is not None:
                                                                for child in self.local_remote_ipv4_addr:
                                                                    if child is not None:
                                                                        return True

                                                            if self.max_bandwidth is not None:
                                                                return True

                                                            if self.max_reservable_bandwidth is not None:
                                                                return True

                                                            if self.te_metric is not None:
                                                                return True

                                                            if self.unknown_subtlv is not None:
                                                                for child_ref in self.unknown_subtlv:
                                                                    if child_ref._has_data():
                                                                        return True

                                                            if self.unreserved_bandwidth is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:opaque'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.link_tlv is not None and self.link_tlv._has_data():
                                                            return True

                                                        if self.router_address_tlv is not None and self.router_address_tlv._has_data():
                                                            return True

                                                        if self.unknown_tlv is not None:
                                                            for child_ref in self.unknown_tlv:
                                                                if child_ref._has_data():
                                                                    return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:body'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.external is not None and self.external._has_data():
                                                        return True

                                                    if self.network is not None and self.network._has_data():
                                                        return True

                                                    if self.opaque is not None and self.opaque._has_data():
                                                        return True

                                                    if self.router is not None and self.router._has_data():
                                                        return True

                                                    if self.summary is not None and self.summary._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:ospfv2'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.body is not None and self.body._has_data():
                                                    return True

                                                if self.header is not None and self.header._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2']['meta_info']


                                        class Ospfv3(object):
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
                                                self.parent = None
                                                self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body()
                                                self.body.parent = self
                                                self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header()
                                                self.header.parent = self


                                            class Header(object):
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
                                                    self.parent = None
                                                    self.adv_router = None
                                                    self.age = None
                                                    self.checksum = None
                                                    self.length = None
                                                    self.lsa_id = None
                                                    self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header.Options()
                                                    self.seq_num = None
                                                    self.type = None

                                                class Options(FixedBitsDict):
                                                    """
                                                    Options

                                                    OSPFv3 LSA options.
                                                    Keys are:- R , N , DC , E , V6 , AF

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'R':False,
                                                            'N':False,
                                                            'DC':False,
                                                            'E':False,
                                                            'V6':False,
                                                            'AF':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:header'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.adv_router is not None:
                                                        return True

                                                    if self.age is not None:
                                                        return True

                                                    if self.checksum is not None:
                                                        return True

                                                    if self.length is not None:
                                                        return True

                                                    if self.lsa_id is not None:
                                                        return True

                                                    if self.options is not None:
                                                        if self.options._has_data():
                                                            return True

                                                    if self.seq_num is not None:
                                                        return True

                                                    if self.type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header']['meta_info']


                                            class Body(object):
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
                                                    self.parent = None
                                                    self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal()
                                                    self.as_external.parent = self
                                                    self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                                    self.inter_area_prefix.parent = self
                                                    self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter()
                                                    self.inter_area_router.parent = self
                                                    self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                                    self.intra_area_prefix.parent = self
                                                    self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link()
                                                    self.link.parent = self
                                                    self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network()
                                                    self.network.parent = self
                                                    self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa()
                                                    self.nssa.parent = self
                                                    self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router()
                                                    self.router.parent = self


                                                class Router(object):
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
                                                        self.parent = None
                                                        self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Flags()
                                                        self.link = YList()
                                                        self.link.parent = self
                                                        self.link.name = 'link'
                                                        self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Options()

                                                    class Flags(FixedBitsDict):
                                                        """
                                                        Flags

                                                        LSA option.
                                                        Keys are:- E , Nt , B , V

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'E':False,
                                                                'Nt':False,
                                                                'B':False,
                                                                'V':False,
                                                            }
                                                            self._pos_map = { 
                                                            }

                                                    class Options(FixedBitsDict):
                                                        """
                                                        Options

                                                        OSPFv3 LSA options.
                                                        Keys are:- R , N , DC , E , V6 , AF

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'R':False,
                                                                'N':False,
                                                                'DC':False,
                                                                'E':False,
                                                                'V6':False,
                                                                'AF':False,
                                                            }
                                                            self._pos_map = { 
                                                            }


                                                    class Link(object):
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
                                                            self.parent = None
                                                            self.interface_id = None
                                                            self.neighbor_interface_id = None
                                                            self.neighbor_router_id = None
                                                            self.metric = None
                                                            self.type = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.interface_id is None:
                                                                raise YPYModelError('Key property interface_id is None')
                                                            if self.neighbor_interface_id is None:
                                                                raise YPYModelError('Key property neighbor_interface_id is None')
                                                            if self.neighbor_router_id is None:
                                                                raise YPYModelError('Key property neighbor_router_id is None')

                                                            return self.parent._common_path +'/ietf-ospf:link[ietf-ospf:interface-id = ' + str(self.interface_id) + '][ietf-ospf:neighbor-interface-id = ' + str(self.neighbor_interface_id) + '][ietf-ospf:neighbor-router-id = ' + str(self.neighbor_router_id) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.interface_id is not None:
                                                                return True

                                                            if self.neighbor_interface_id is not None:
                                                                return True

                                                            if self.neighbor_router_id is not None:
                                                                return True

                                                            if self.metric is not None:
                                                                return True

                                                            if self.type is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:router'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.flags is not None:
                                                            if self.flags._has_data():
                                                                return True

                                                        if self.link is not None:
                                                            for child_ref in self.link:
                                                                if child_ref._has_data():
                                                                    return True

                                                        if self.options is not None:
                                                            if self.options._has_data():
                                                                return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router']['meta_info']


                                                class Network(object):
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
                                                        self.parent = None
                                                        self.attached_router = YLeafList()
                                                        self.attached_router.parent = self
                                                        self.attached_router.name = 'attached_router'
                                                        self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network.Options()

                                                    class Options(FixedBitsDict):
                                                        """
                                                        Options

                                                        OSPFv3 LSA options.
                                                        Keys are:- R , N , DC , E , V6 , AF

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'R':False,
                                                                'N':False,
                                                                'DC':False,
                                                                'E':False,
                                                                'V6':False,
                                                                'AF':False,
                                                            }
                                                            self._pos_map = { 
                                                            }

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:network'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.attached_router is not None:
                                                            for child in self.attached_router:
                                                                if child is not None:
                                                                    return True

                                                        if self.options is not None:
                                                            if self.options._has_data():
                                                                return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network']['meta_info']


                                                class InterAreaPrefix(object):
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
                                                        self.parent = None
                                                        self.metric = None
                                                        self.prefix = None
                                                        self.prefix_options = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:inter-area-prefix'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.metric is not None:
                                                            return True

                                                        if self.prefix is not None:
                                                            return True

                                                        if self.prefix_options is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix']['meta_info']


                                                class InterAreaRouter(object):
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
                                                        self.parent = None
                                                        self.destination_router_id = None
                                                        self.metric = None
                                                        self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter.Options()

                                                    class Options(FixedBitsDict):
                                                        """
                                                        Options

                                                        OSPFv3 LSA options.
                                                        Keys are:- R , N , DC , E , V6 , AF

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'R':False,
                                                                'N':False,
                                                                'DC':False,
                                                                'E':False,
                                                                'V6':False,
                                                                'AF':False,
                                                            }
                                                            self._pos_map = { 
                                                            }

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:inter-area-router'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.destination_router_id is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        if self.options is not None:
                                                            if self.options._has_data():
                                                                return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter']['meta_info']


                                                class AsExternal(object):
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
                                                        self.parent = None
                                                        self.external_route_tag = None
                                                        self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal.Flags()
                                                        self.forwarding_address = None
                                                        self.metric = None
                                                        self.prefix = None
                                                        self.prefix_options = None
                                                        self.referenced_link_state_id = None
                                                        self.referenced_ls_type = None

                                                    class Flags(FixedBitsDict):
                                                        """
                                                        Flags

                                                        Flags.
                                                        Keys are:- E

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'E':False,
                                                            }
                                                            self._pos_map = { 
                                                            }

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:as-external'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.external_route_tag is not None:
                                                            return True

                                                        if self.flags is not None:
                                                            if self.flags._has_data():
                                                                return True

                                                        if self.forwarding_address is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        if self.prefix is not None:
                                                            return True

                                                        if self.prefix_options is not None:
                                                            return True

                                                        if self.referenced_link_state_id is not None:
                                                            return True

                                                        if self.referenced_ls_type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal']['meta_info']


                                                class Nssa(object):
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
                                                        self.parent = None
                                                        self.external_route_tag = None
                                                        self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa.Flags()
                                                        self.forwarding_address = None
                                                        self.metric = None
                                                        self.prefix = None
                                                        self.prefix_options = None
                                                        self.referenced_link_state_id = None
                                                        self.referenced_ls_type = None

                                                    class Flags(FixedBitsDict):
                                                        """
                                                        Flags

                                                        Flags.
                                                        Keys are:- E

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'E':False,
                                                            }
                                                            self._pos_map = { 
                                                            }

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:nssa'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.external_route_tag is not None:
                                                            return True

                                                        if self.flags is not None:
                                                            if self.flags._has_data():
                                                                return True

                                                        if self.forwarding_address is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        if self.prefix is not None:
                                                            return True

                                                        if self.prefix_options is not None:
                                                            return True

                                                        if self.referenced_link_state_id is not None:
                                                            return True

                                                        if self.referenced_ls_type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa']['meta_info']


                                                class Link(object):
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
                                                        self.parent = None
                                                        self.link_local_interface_address = None
                                                        self.num_of_prefixes = None
                                                        self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.Options()
                                                        self.prefix_list = YList()
                                                        self.prefix_list.parent = self
                                                        self.prefix_list.name = 'prefix_list'
                                                        self.rtr_priority = None

                                                    class Options(FixedBitsDict):
                                                        """
                                                        Options

                                                        OSPFv3 LSA options.
                                                        Keys are:- R , N , DC , E , V6 , AF

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'R':False,
                                                                'N':False,
                                                                'DC':False,
                                                                'E':False,
                                                                'V6':False,
                                                                'AF':False,
                                                            }
                                                            self._pos_map = { 
                                                            }


                                                    class PrefixList(object):
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
                                                            self.parent = None
                                                            self.prefix = None
                                                            self.prefix_options = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.prefix is None:
                                                                raise YPYModelError('Key property prefix is None')

                                                            return self.parent._common_path +'/ietf-ospf:prefix-list[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.prefix is not None:
                                                                return True

                                                            if self.prefix_options is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:link'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.link_local_interface_address is not None:
                                                            return True

                                                        if self.num_of_prefixes is not None:
                                                            return True

                                                        if self.options is not None:
                                                            if self.options._has_data():
                                                                return True

                                                        if self.prefix_list is not None:
                                                            for child_ref in self.prefix_list:
                                                                if child_ref._has_data():
                                                                    return True

                                                        if self.rtr_priority is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link']['meta_info']


                                                class IntraAreaPrefix(object):
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
                                                        self.parent = None
                                                        self.num_of_prefixes = None
                                                        self.prefix_list = YList()
                                                        self.prefix_list.parent = self
                                                        self.prefix_list.name = 'prefix_list'
                                                        self.referenced_adv_router = None
                                                        self.referenced_link_state_id = None
                                                        self.referenced_ls_type = None


                                                    class PrefixList(object):
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
                                                            self.parent = None
                                                            self.prefix = None
                                                            self.metric = None
                                                            self.prefix_options = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.prefix is None:
                                                                raise YPYModelError('Key property prefix is None')

                                                            return self.parent._common_path +'/ietf-ospf:prefix-list[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.prefix is not None:
                                                                return True

                                                            if self.metric is not None:
                                                                return True

                                                            if self.prefix_options is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:intra-area-prefix'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.num_of_prefixes is not None:
                                                            return True

                                                        if self.prefix_list is not None:
                                                            for child_ref in self.prefix_list:
                                                                if child_ref._has_data():
                                                                    return True

                                                        if self.referenced_adv_router is not None:
                                                            return True

                                                        if self.referenced_link_state_id is not None:
                                                            return True

                                                        if self.referenced_ls_type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:body'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.as_external is not None and self.as_external._has_data():
                                                        return True

                                                    if self.inter_area_prefix is not None and self.inter_area_prefix._has_data():
                                                        return True

                                                    if self.inter_area_router is not None and self.inter_area_router._has_data():
                                                        return True

                                                    if self.intra_area_prefix is not None and self.intra_area_prefix._has_data():
                                                        return True

                                                    if self.link is not None and self.link._has_data():
                                                        return True

                                                    if self.network is not None and self.network._has_data():
                                                        return True

                                                    if self.nssa is not None and self.nssa._has_data():
                                                        return True

                                                    if self.router is not None and self.router._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:ospfv3'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.body is not None and self.body._has_data():
                                                    return True

                                                if self.header is not None and self.header._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.lsa_id is None:
                                                raise YPYModelError('Key property lsa_id is None')
                                            if self.adv_router is None:
                                                raise YPYModelError('Key property adv_router is None')

                                            return self.parent._common_path +'/ietf-ospf:link-scope-lsa[ietf-ospf:lsa-id = ' + str(self.lsa_id) + '][ietf-ospf:adv-router = ' + str(self.adv_router) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.lsa_id is not None:
                                                return True

                                            if self.adv_router is not None:
                                                return True

                                            if self.decoded_completed is not None:
                                                return True

                                            if self.ospfv2 is not None and self.ospfv2._has_data():
                                                return True

                                            if self.ospfv3 is not None and self.ospfv3._has_data():
                                                return True

                                            if self.raw_data is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.lsa_type is None:
                                            raise YPYModelError('Key property lsa_type is None')

                                        return self.parent._common_path +'/ietf-ospf:link-scope-lsas[ietf-ospf:lsa-type = ' + str(self.lsa_type) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lsa_type is not None:
                                            return True

                                        if self.link_scope_lsa is not None:
                                            for child_ref in self.link_scope_lsa:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas']['meta_info']


                                class Topology(object):
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
                                        self.parent = None
                                        self.name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.name is None:
                                            raise YPYModelError('Key property name is None')

                                        return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:name = ' + str(self.name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface is None:
                                        raise YPYModelError('Key property interface is None')

                                    return self.parent._common_path +'/ietf-ospf:interfaces[ietf-ospf:interface = ' + str(self.interface) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.interface is not None:
                                        return True

                                    if self.authentication is not None and self.authentication._has_data():
                                        return True

                                    if self.bdr is not None:
                                        return True

                                    if self.bfd is not None:
                                        return True

                                    if self.cost is not None:
                                        return True

                                    if self.dead_interval is not None:
                                        return True

                                    if self.demand_circuit is not None:
                                        return True

                                    if self.dr is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.fast_reroute is not None and self.fast_reroute._has_data():
                                        return True

                                    if self.hello_interval is not None:
                                        return True

                                    if self.hello_timer is not None:
                                        return True

                                    if self.link_scope_lsas is not None:
                                        for child_ref in self.link_scope_lsas:
                                            if child_ref._has_data():
                                                return True

                                    if self.lls is not None:
                                        return True

                                    if self.mtu_ignore is not None:
                                        return True

                                    if self.multi_area is not None and self.multi_area._has_data():
                                        return True

                                    if self.neighbor is not None:
                                        for child_ref in self.neighbor:
                                            if child_ref._has_data():
                                                return True

                                    if self.network_type is not None:
                                        return True

                                    if self.node_flag is not None:
                                        return True

                                    if self.passive is not None:
                                        return True

                                    if self.prefix_suppression is not None:
                                        return True

                                    if self.retransmit_interval is not None:
                                        return True

                                    if self.state is not None:
                                        return True

                                    if self.static_neighbors is not None and self.static_neighbors._has_data():
                                        return True

                                    if self.topology is not None:
                                        for child_ref in self.topology:
                                            if child_ref._has_data():
                                                return True

                                    if self.transmit_delay is not None:
                                        return True

                                    if self.ttl_security is not None and self.ttl_security._has_data():
                                        return True

                                    if self.wait_timer is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']


                            class AreaScopeLsas(object):
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
                                    self.parent = None
                                    self.lsa_type = None
                                    self.area_scope_lsa = YList()
                                    self.area_scope_lsa.parent = self
                                    self.area_scope_lsa.name = 'area_scope_lsa'


                                class AreaScopeLsa(object):
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
                                        self.parent = None
                                        self.lsa_id = None
                                        self.adv_router = None
                                        self.decoded_completed = None
                                        self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2()
                                        self.ospfv2.parent = self
                                        self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3()
                                        self.ospfv3.parent = self
                                        self.raw_data = None


                                    class Ospfv2(object):
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
                                            self.parent = None
                                            self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body()
                                            self.body.parent = self
                                            self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header()
                                            self.header.parent = self


                                        class Header(object):
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
                                                self.parent = None
                                                self.adv_router = None
                                                self.age = None
                                                self.checksum = None
                                                self.length = None
                                                self.lsa_id = None
                                                self.opaque_id = None
                                                self.opaque_type = None
                                                self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header.Options()
                                                self.seq_num = None
                                                self.type = None

                                            class Options(FixedBitsDict):
                                                """
                                                Options

                                                LSA option.
                                                Keys are:- R , MC , DC , MT , E , P , Upward , AF

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'R':False,
                                                        'MC':False,
                                                        'DC':False,
                                                        'MT':False,
                                                        'E':False,
                                                        'P':False,
                                                        'Upward':False,
                                                        'AF':False,
                                                    }
                                                    self._pos_map = { 
                                                    }

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:header'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.adv_router is not None:
                                                    return True

                                                if self.age is not None:
                                                    return True

                                                if self.checksum is not None:
                                                    return True

                                                if self.length is not None:
                                                    return True

                                                if self.lsa_id is not None:
                                                    return True

                                                if self.opaque_id is not None:
                                                    return True

                                                if self.opaque_type is not None:
                                                    return True

                                                if self.options is not None:
                                                    if self.options._has_data():
                                                        return True

                                                if self.seq_num is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header']['meta_info']


                                        class Body(object):
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
                                                self.parent = None
                                                self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External()
                                                self.external.parent = self
                                                self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network()
                                                self.network.parent = self
                                                self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque()
                                                self.opaque.parent = self
                                                self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router()
                                                self.router.parent = self
                                                self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary()
                                                self.summary.parent = self


                                            class Router(object):
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
                                                    self.parent = None
                                                    self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Flags()
                                                    self.link = YList()
                                                    self.link.parent = self
                                                    self.link.name = 'link'
                                                    self.num_of_links = None

                                                class Flags(FixedBitsDict):
                                                    """
                                                    Flags

                                                    Flags
                                                    Keys are:- E , B , V

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'E':False,
                                                            'B':False,
                                                            'V':False,
                                                        }
                                                        self._pos_map = { 
                                                        }


                                                class Link(object):
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
                                                        self.parent = None
                                                        self.link_id = None
                                                        self.link_data = None
                                                        self.topology = YList()
                                                        self.topology.parent = self
                                                        self.topology.name = 'topology'
                                                        self.type = None


                                                    class Topology(object):
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
                                                            self.parent = None
                                                            self.mt_id = None
                                                            self.metric = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.mt_id is None:
                                                                raise YPYModelError('Key property mt_id is None')

                                                            return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.mt_id is not None:
                                                                return True

                                                            if self.metric is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.link_id is None:
                                                            raise YPYModelError('Key property link_id is None')
                                                        if self.link_data is None:
                                                            raise YPYModelError('Key property link_data is None')

                                                        return self.parent._common_path +'/ietf-ospf:link[ietf-ospf:link-id = ' + str(self.link_id) + '][ietf-ospf:link-data = ' + str(self.link_data) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.link_id is not None:
                                                            return True

                                                        if self.link_data is not None:
                                                            return True

                                                        if self.topology is not None:
                                                            for child_ref in self.topology:
                                                                if child_ref._has_data():
                                                                    return True

                                                        if self.type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:router'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.flags is not None:
                                                        if self.flags._has_data():
                                                            return True

                                                    if self.link is not None:
                                                        for child_ref in self.link:
                                                            if child_ref._has_data():
                                                                return True

                                                    if self.num_of_links is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router']['meta_info']


                                            class Network(object):
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
                                                    self.parent = None
                                                    self.attached_router = YLeafList()
                                                    self.attached_router.parent = self
                                                    self.attached_router.name = 'attached_router'
                                                    self.network_mask = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:network'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.attached_router is not None:
                                                        for child in self.attached_router:
                                                            if child is not None:
                                                                return True

                                                    if self.network_mask is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network']['meta_info']


                                            class Summary(object):
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
                                                    self.parent = None
                                                    self.network_mask = None
                                                    self.topology = YList()
                                                    self.topology.parent = self
                                                    self.topology.name = 'topology'


                                                class Topology(object):
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
                                                        self.parent = None
                                                        self.mt_id = None
                                                        self.metric = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.mt_id is None:
                                                            raise YPYModelError('Key property mt_id is None')

                                                        return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.mt_id is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:summary'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.network_mask is not None:
                                                        return True

                                                    if self.topology is not None:
                                                        for child_ref in self.topology:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary']['meta_info']


                                            class External(object):
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
                                                    self.parent = None
                                                    self.network_mask = None
                                                    self.topology = YList()
                                                    self.topology.parent = self
                                                    self.topology.name = 'topology'


                                                class Topology(object):
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
                                                        self.parent = None
                                                        self.mt_id = None
                                                        self.external_route_tag = None
                                                        self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology.Flags()
                                                        self.forwarding_address = None
                                                        self.metric = None

                                                    class Flags(FixedBitsDict):
                                                        """
                                                        Flags

                                                        Flags.
                                                        Keys are:- E

                                                        """

                                                        def __init__(self):
                                                            self._dictionary = { 
                                                                'E':False,
                                                            }
                                                            self._pos_map = { 
                                                            }

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.mt_id is None:
                                                            raise YPYModelError('Key property mt_id is None')

                                                        return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.mt_id is not None:
                                                            return True

                                                        if self.external_route_tag is not None:
                                                            return True

                                                        if self.flags is not None:
                                                            if self.flags._has_data():
                                                                return True

                                                        if self.forwarding_address is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:external'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.network_mask is not None:
                                                        return True

                                                    if self.topology is not None:
                                                        for child_ref in self.topology:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External']['meta_info']


                                            class Opaque(object):
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
                                                    self.parent = None
                                                    self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                    self.link_tlv.parent = self
                                                    self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                    self.router_address_tlv.parent = self
                                                    self.unknown_tlv = YList()
                                                    self.unknown_tlv.parent = self
                                                    self.unknown_tlv.name = 'unknown_tlv'


                                                class UnknownTlv(object):
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
                                                        self.parent = None
                                                        self.type = None
                                                        self.length = None
                                                        self.value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.type is None:
                                                            raise YPYModelError('Key property type is None')

                                                        return self.parent._common_path +'/ietf-ospf:unknown-tlv[ietf-ospf:type = ' + str(self.type) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.type is not None:
                                                            return True

                                                        if self.length is not None:
                                                            return True

                                                        if self.value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv']['meta_info']


                                                class RouterAddressTlv(object):
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
                                                        self.parent = None
                                                        self.router_address = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:router-address-tlv'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.router_address is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv']['meta_info']


                                                class LinkTlv(object):
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
                                                        self.parent = None
                                                        self.admin_group = None
                                                        self.link_id = None
                                                        self.link_type = None
                                                        self.local_if_ipv4_addr = YLeafList()
                                                        self.local_if_ipv4_addr.parent = self
                                                        self.local_if_ipv4_addr.name = 'local_if_ipv4_addr'
                                                        self.local_remote_ipv4_addr = YLeafList()
                                                        self.local_remote_ipv4_addr.parent = self
                                                        self.local_remote_ipv4_addr.name = 'local_remote_ipv4_addr'
                                                        self.max_bandwidth = None
                                                        self.max_reservable_bandwidth = None
                                                        self.te_metric = None
                                                        self.unknown_subtlv = YList()
                                                        self.unknown_subtlv.parent = self
                                                        self.unknown_subtlv.name = 'unknown_subtlv'
                                                        self.unreserved_bandwidth = None


                                                    class UnknownSubtlv(object):
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
                                                            self.parent = None
                                                            self.type = None
                                                            self.length = None
                                                            self.value = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                                            if self.type is None:
                                                                raise YPYModelError('Key property type is None')

                                                            return self.parent._common_path +'/ietf-ospf:unknown-subtlv[ietf-ospf:type = ' + str(self.type) + ']'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.type is not None:
                                                                return True

                                                            if self.length is not None:
                                                                return True

                                                            if self.value is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/ietf-ospf:link-tlv'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.admin_group is not None:
                                                            return True

                                                        if self.link_id is not None:
                                                            return True

                                                        if self.link_type is not None:
                                                            return True

                                                        if self.local_if_ipv4_addr is not None:
                                                            for child in self.local_if_ipv4_addr:
                                                                if child is not None:
                                                                    return True

                                                        if self.local_remote_ipv4_addr is not None:
                                                            for child in self.local_remote_ipv4_addr:
                                                                if child is not None:
                                                                    return True

                                                        if self.max_bandwidth is not None:
                                                            return True

                                                        if self.max_reservable_bandwidth is not None:
                                                            return True

                                                        if self.te_metric is not None:
                                                            return True

                                                        if self.unknown_subtlv is not None:
                                                            for child_ref in self.unknown_subtlv:
                                                                if child_ref._has_data():
                                                                    return True

                                                        if self.unreserved_bandwidth is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:opaque'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.link_tlv is not None and self.link_tlv._has_data():
                                                        return True

                                                    if self.router_address_tlv is not None and self.router_address_tlv._has_data():
                                                        return True

                                                    if self.unknown_tlv is not None:
                                                        for child_ref in self.unknown_tlv:
                                                            if child_ref._has_data():
                                                                return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:body'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.external is not None and self.external._has_data():
                                                    return True

                                                if self.network is not None and self.network._has_data():
                                                    return True

                                                if self.opaque is not None and self.opaque._has_data():
                                                    return True

                                                if self.router is not None and self.router._has_data():
                                                    return True

                                                if self.summary is not None and self.summary._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:ospfv2'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.body is not None and self.body._has_data():
                                                return True

                                            if self.header is not None and self.header._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2']['meta_info']


                                    class Ospfv3(object):
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
                                            self.parent = None
                                            self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body()
                                            self.body.parent = self
                                            self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header()
                                            self.header.parent = self


                                        class Header(object):
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
                                                self.parent = None
                                                self.adv_router = None
                                                self.age = None
                                                self.checksum = None
                                                self.length = None
                                                self.lsa_id = None
                                                self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header.Options()
                                                self.seq_num = None
                                                self.type = None

                                            class Options(FixedBitsDict):
                                                """
                                                Options

                                                OSPFv3 LSA options.
                                                Keys are:- R , N , DC , E , V6 , AF

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'R':False,
                                                        'N':False,
                                                        'DC':False,
                                                        'E':False,
                                                        'V6':False,
                                                        'AF':False,
                                                    }
                                                    self._pos_map = { 
                                                    }

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:header'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.adv_router is not None:
                                                    return True

                                                if self.age is not None:
                                                    return True

                                                if self.checksum is not None:
                                                    return True

                                                if self.length is not None:
                                                    return True

                                                if self.lsa_id is not None:
                                                    return True

                                                if self.options is not None:
                                                    if self.options._has_data():
                                                        return True

                                                if self.seq_num is not None:
                                                    return True

                                                if self.type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header']['meta_info']


                                        class Body(object):
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
                                                self.parent = None
                                                self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal()
                                                self.as_external.parent = self
                                                self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                                self.inter_area_prefix.parent = self
                                                self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter()
                                                self.inter_area_router.parent = self
                                                self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                                self.intra_area_prefix.parent = self
                                                self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link()
                                                self.link.parent = self
                                                self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network()
                                                self.network.parent = self
                                                self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa()
                                                self.nssa.parent = self
                                                self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router()
                                                self.router.parent = self


                                            class Router(object):
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
                                                    self.parent = None
                                                    self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Flags()
                                                    self.link = YList()
                                                    self.link.parent = self
                                                    self.link.name = 'link'
                                                    self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Options()

                                                class Flags(FixedBitsDict):
                                                    """
                                                    Flags

                                                    LSA option.
                                                    Keys are:- E , Nt , B , V

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'E':False,
                                                            'Nt':False,
                                                            'B':False,
                                                            'V':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                class Options(FixedBitsDict):
                                                    """
                                                    Options

                                                    OSPFv3 LSA options.
                                                    Keys are:- R , N , DC , E , V6 , AF

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'R':False,
                                                            'N':False,
                                                            'DC':False,
                                                            'E':False,
                                                            'V6':False,
                                                            'AF':False,
                                                        }
                                                        self._pos_map = { 
                                                        }


                                                class Link(object):
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
                                                        self.parent = None
                                                        self.interface_id = None
                                                        self.neighbor_interface_id = None
                                                        self.neighbor_router_id = None
                                                        self.metric = None
                                                        self.type = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.interface_id is None:
                                                            raise YPYModelError('Key property interface_id is None')
                                                        if self.neighbor_interface_id is None:
                                                            raise YPYModelError('Key property neighbor_interface_id is None')
                                                        if self.neighbor_router_id is None:
                                                            raise YPYModelError('Key property neighbor_router_id is None')

                                                        return self.parent._common_path +'/ietf-ospf:link[ietf-ospf:interface-id = ' + str(self.interface_id) + '][ietf-ospf:neighbor-interface-id = ' + str(self.neighbor_interface_id) + '][ietf-ospf:neighbor-router-id = ' + str(self.neighbor_router_id) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.interface_id is not None:
                                                            return True

                                                        if self.neighbor_interface_id is not None:
                                                            return True

                                                        if self.neighbor_router_id is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        if self.type is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:router'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.flags is not None:
                                                        if self.flags._has_data():
                                                            return True

                                                    if self.link is not None:
                                                        for child_ref in self.link:
                                                            if child_ref._has_data():
                                                                return True

                                                    if self.options is not None:
                                                        if self.options._has_data():
                                                            return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router']['meta_info']


                                            class Network(object):
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
                                                    self.parent = None
                                                    self.attached_router = YLeafList()
                                                    self.attached_router.parent = self
                                                    self.attached_router.name = 'attached_router'
                                                    self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network.Options()

                                                class Options(FixedBitsDict):
                                                    """
                                                    Options

                                                    OSPFv3 LSA options.
                                                    Keys are:- R , N , DC , E , V6 , AF

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'R':False,
                                                            'N':False,
                                                            'DC':False,
                                                            'E':False,
                                                            'V6':False,
                                                            'AF':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:network'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.attached_router is not None:
                                                        for child in self.attached_router:
                                                            if child is not None:
                                                                return True

                                                    if self.options is not None:
                                                        if self.options._has_data():
                                                            return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network']['meta_info']


                                            class InterAreaPrefix(object):
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
                                                    self.parent = None
                                                    self.metric = None
                                                    self.prefix = None
                                                    self.prefix_options = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:inter-area-prefix'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.metric is not None:
                                                        return True

                                                    if self.prefix is not None:
                                                        return True

                                                    if self.prefix_options is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix']['meta_info']


                                            class InterAreaRouter(object):
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
                                                    self.parent = None
                                                    self.destination_router_id = None
                                                    self.metric = None
                                                    self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter.Options()

                                                class Options(FixedBitsDict):
                                                    """
                                                    Options

                                                    OSPFv3 LSA options.
                                                    Keys are:- R , N , DC , E , V6 , AF

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'R':False,
                                                            'N':False,
                                                            'DC':False,
                                                            'E':False,
                                                            'V6':False,
                                                            'AF':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:inter-area-router'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.destination_router_id is not None:
                                                        return True

                                                    if self.metric is not None:
                                                        return True

                                                    if self.options is not None:
                                                        if self.options._has_data():
                                                            return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter']['meta_info']


                                            class AsExternal(object):
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
                                                    self.parent = None
                                                    self.external_route_tag = None
                                                    self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal.Flags()
                                                    self.forwarding_address = None
                                                    self.metric = None
                                                    self.prefix = None
                                                    self.prefix_options = None
                                                    self.referenced_link_state_id = None
                                                    self.referenced_ls_type = None

                                                class Flags(FixedBitsDict):
                                                    """
                                                    Flags

                                                    Flags.
                                                    Keys are:- E

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'E':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:as-external'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.external_route_tag is not None:
                                                        return True

                                                    if self.flags is not None:
                                                        if self.flags._has_data():
                                                            return True

                                                    if self.forwarding_address is not None:
                                                        return True

                                                    if self.metric is not None:
                                                        return True

                                                    if self.prefix is not None:
                                                        return True

                                                    if self.prefix_options is not None:
                                                        return True

                                                    if self.referenced_link_state_id is not None:
                                                        return True

                                                    if self.referenced_ls_type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal']['meta_info']


                                            class Nssa(object):
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
                                                    self.parent = None
                                                    self.external_route_tag = None
                                                    self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa.Flags()
                                                    self.forwarding_address = None
                                                    self.metric = None
                                                    self.prefix = None
                                                    self.prefix_options = None
                                                    self.referenced_link_state_id = None
                                                    self.referenced_ls_type = None

                                                class Flags(FixedBitsDict):
                                                    """
                                                    Flags

                                                    Flags.
                                                    Keys are:- E

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'E':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:nssa'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.external_route_tag is not None:
                                                        return True

                                                    if self.flags is not None:
                                                        if self.flags._has_data():
                                                            return True

                                                    if self.forwarding_address is not None:
                                                        return True

                                                    if self.metric is not None:
                                                        return True

                                                    if self.prefix is not None:
                                                        return True

                                                    if self.prefix_options is not None:
                                                        return True

                                                    if self.referenced_link_state_id is not None:
                                                        return True

                                                    if self.referenced_ls_type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa']['meta_info']


                                            class Link(object):
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
                                                    self.parent = None
                                                    self.link_local_interface_address = None
                                                    self.num_of_prefixes = None
                                                    self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.Options()
                                                    self.prefix_list = YList()
                                                    self.prefix_list.parent = self
                                                    self.prefix_list.name = 'prefix_list'
                                                    self.rtr_priority = None

                                                class Options(FixedBitsDict):
                                                    """
                                                    Options

                                                    OSPFv3 LSA options.
                                                    Keys are:- R , N , DC , E , V6 , AF

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'R':False,
                                                            'N':False,
                                                            'DC':False,
                                                            'E':False,
                                                            'V6':False,
                                                            'AF':False,
                                                        }
                                                        self._pos_map = { 
                                                        }


                                                class PrefixList(object):
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
                                                        self.parent = None
                                                        self.prefix = None
                                                        self.prefix_options = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.prefix is None:
                                                            raise YPYModelError('Key property prefix is None')

                                                        return self.parent._common_path +'/ietf-ospf:prefix-list[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.prefix is not None:
                                                            return True

                                                        if self.prefix_options is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:link'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.link_local_interface_address is not None:
                                                        return True

                                                    if self.num_of_prefixes is not None:
                                                        return True

                                                    if self.options is not None:
                                                        if self.options._has_data():
                                                            return True

                                                    if self.prefix_list is not None:
                                                        for child_ref in self.prefix_list:
                                                            if child_ref._has_data():
                                                                return True

                                                    if self.rtr_priority is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link']['meta_info']


                                            class IntraAreaPrefix(object):
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
                                                    self.parent = None
                                                    self.num_of_prefixes = None
                                                    self.prefix_list = YList()
                                                    self.prefix_list.parent = self
                                                    self.prefix_list.name = 'prefix_list'
                                                    self.referenced_adv_router = None
                                                    self.referenced_link_state_id = None
                                                    self.referenced_ls_type = None


                                                class PrefixList(object):
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
                                                        self.parent = None
                                                        self.prefix = None
                                                        self.metric = None
                                                        self.prefix_options = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.prefix is None:
                                                            raise YPYModelError('Key property prefix is None')

                                                        return self.parent._common_path +'/ietf-ospf:prefix-list[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.prefix is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        if self.prefix_options is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:intra-area-prefix'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.num_of_prefixes is not None:
                                                        return True

                                                    if self.prefix_list is not None:
                                                        for child_ref in self.prefix_list:
                                                            if child_ref._has_data():
                                                                return True

                                                    if self.referenced_adv_router is not None:
                                                        return True

                                                    if self.referenced_link_state_id is not None:
                                                        return True

                                                    if self.referenced_ls_type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:body'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.as_external is not None and self.as_external._has_data():
                                                    return True

                                                if self.inter_area_prefix is not None and self.inter_area_prefix._has_data():
                                                    return True

                                                if self.inter_area_router is not None and self.inter_area_router._has_data():
                                                    return True

                                                if self.intra_area_prefix is not None and self.intra_area_prefix._has_data():
                                                    return True

                                                if self.link is not None and self.link._has_data():
                                                    return True

                                                if self.network is not None and self.network._has_data():
                                                    return True

                                                if self.nssa is not None and self.nssa._has_data():
                                                    return True

                                                if self.router is not None and self.router._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:ospfv3'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.body is not None and self.body._has_data():
                                                return True

                                            if self.header is not None and self.header._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.lsa_id is None:
                                            raise YPYModelError('Key property lsa_id is None')
                                        if self.adv_router is None:
                                            raise YPYModelError('Key property adv_router is None')

                                        return self.parent._common_path +'/ietf-ospf:area-scope-lsa[ietf-ospf:lsa-id = ' + str(self.lsa_id) + '][ietf-ospf:adv-router = ' + str(self.adv_router) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.lsa_id is not None:
                                            return True

                                        if self.adv_router is not None:
                                            return True

                                        if self.decoded_completed is not None:
                                            return True

                                        if self.ospfv2 is not None and self.ospfv2._has_data():
                                            return True

                                        if self.ospfv3 is not None and self.ospfv3._has_data():
                                            return True

                                        if self.raw_data is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.lsa_type is None:
                                        raise YPYModelError('Key property lsa_type is None')

                                    return self.parent._common_path +'/ietf-ospf:area-scope-lsas[ietf-ospf:lsa-type = ' + str(self.lsa_type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.lsa_type is not None:
                                        return True

                                    if self.area_scope_lsa is not None:
                                        for child_ref in self.area_scope_lsa:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.area_id is None:
                                    raise YPYModelError('Key property area_id is None')

                                return self.parent._common_path +'/ietf-ospf:area[ietf-ospf:area-id = ' + str(self.area_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.area_id is not None:
                                    return True

                                if self.area_scope_lsas is not None:
                                    for child_ref in self.area_scope_lsas:
                                        if child_ref._has_data():
                                            return True

                                if self.interfaces is not None:
                                    for child_ref in self.interfaces:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']


                        class AsScopeLsas(object):
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
                                self.parent = None
                                self.lsa_type = None
                                self.as_scope_lsa = YList()
                                self.as_scope_lsa.parent = self
                                self.as_scope_lsa.name = 'as_scope_lsa'


                            class AsScopeLsa(object):
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
                                    self.parent = None
                                    self.lsa_id = None
                                    self.adv_router = None
                                    self.decoded_completed = None
                                    self.ospfv2 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2()
                                    self.ospfv2.parent = self
                                    self.ospfv3 = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3()
                                    self.ospfv3.parent = self
                                    self.raw_data = None


                                class Ospfv2(object):
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
                                        self.parent = None
                                        self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body()
                                        self.body.parent = self
                                        self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header()
                                        self.header.parent = self


                                    class Header(object):
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
                                            self.parent = None
                                            self.adv_router = None
                                            self.age = None
                                            self.checksum = None
                                            self.length = None
                                            self.lsa_id = None
                                            self.opaque_id = None
                                            self.opaque_type = None
                                            self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header.Options()
                                            self.seq_num = None
                                            self.type = None

                                        class Options(FixedBitsDict):
                                            """
                                            Options

                                            LSA option.
                                            Keys are:- R , MC , DC , MT , E , P , Upward , AF

                                            """

                                            def __init__(self):
                                                self._dictionary = { 
                                                    'R':False,
                                                    'MC':False,
                                                    'DC':False,
                                                    'MT':False,
                                                    'E':False,
                                                    'P':False,
                                                    'Upward':False,
                                                    'AF':False,
                                                }
                                                self._pos_map = { 
                                                }

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:header'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.adv_router is not None:
                                                return True

                                            if self.age is not None:
                                                return True

                                            if self.checksum is not None:
                                                return True

                                            if self.length is not None:
                                                return True

                                            if self.lsa_id is not None:
                                                return True

                                            if self.opaque_id is not None:
                                                return True

                                            if self.opaque_type is not None:
                                                return True

                                            if self.options is not None:
                                                if self.options._has_data():
                                                    return True

                                            if self.seq_num is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header']['meta_info']


                                    class Body(object):
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
                                            self.parent = None
                                            self.external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External()
                                            self.external.parent = self
                                            self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network()
                                            self.network.parent = self
                                            self.opaque = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque()
                                            self.opaque.parent = self
                                            self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router()
                                            self.router.parent = self
                                            self.summary = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary()
                                            self.summary.parent = self


                                        class Router(object):
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
                                                self.parent = None
                                                self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Flags()
                                                self.link = YList()
                                                self.link.parent = self
                                                self.link.name = 'link'
                                                self.num_of_links = None

                                            class Flags(FixedBitsDict):
                                                """
                                                Flags

                                                Flags
                                                Keys are:- E , B , V

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'E':False,
                                                        'B':False,
                                                        'V':False,
                                                    }
                                                    self._pos_map = { 
                                                    }


                                            class Link(object):
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
                                                    self.parent = None
                                                    self.link_id = None
                                                    self.link_data = None
                                                    self.topology = YList()
                                                    self.topology.parent = self
                                                    self.topology.name = 'topology'
                                                    self.type = None


                                                class Topology(object):
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
                                                        self.parent = None
                                                        self.mt_id = None
                                                        self.metric = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.mt_id is None:
                                                            raise YPYModelError('Key property mt_id is None')

                                                        return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.mt_id is not None:
                                                            return True

                                                        if self.metric is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.link_id is None:
                                                        raise YPYModelError('Key property link_id is None')
                                                    if self.link_data is None:
                                                        raise YPYModelError('Key property link_data is None')

                                                    return self.parent._common_path +'/ietf-ospf:link[ietf-ospf:link-id = ' + str(self.link_id) + '][ietf-ospf:link-data = ' + str(self.link_data) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.link_id is not None:
                                                        return True

                                                    if self.link_data is not None:
                                                        return True

                                                    if self.topology is not None:
                                                        for child_ref in self.topology:
                                                            if child_ref._has_data():
                                                                return True

                                                    if self.type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:router'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.flags is not None:
                                                    if self.flags._has_data():
                                                        return True

                                                if self.link is not None:
                                                    for child_ref in self.link:
                                                        if child_ref._has_data():
                                                            return True

                                                if self.num_of_links is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router']['meta_info']


                                        class Network(object):
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
                                                self.parent = None
                                                self.attached_router = YLeafList()
                                                self.attached_router.parent = self
                                                self.attached_router.name = 'attached_router'
                                                self.network_mask = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:network'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attached_router is not None:
                                                    for child in self.attached_router:
                                                        if child is not None:
                                                            return True

                                                if self.network_mask is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network']['meta_info']


                                        class Summary(object):
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
                                                self.parent = None
                                                self.network_mask = None
                                                self.topology = YList()
                                                self.topology.parent = self
                                                self.topology.name = 'topology'


                                            class Topology(object):
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
                                                    self.parent = None
                                                    self.mt_id = None
                                                    self.metric = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.mt_id is None:
                                                        raise YPYModelError('Key property mt_id is None')

                                                    return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.mt_id is not None:
                                                        return True

                                                    if self.metric is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:summary'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.network_mask is not None:
                                                    return True

                                                if self.topology is not None:
                                                    for child_ref in self.topology:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary']['meta_info']


                                        class External(object):
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
                                                self.parent = None
                                                self.network_mask = None
                                                self.topology = YList()
                                                self.topology.parent = self
                                                self.topology.name = 'topology'


                                            class Topology(object):
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
                                                    self.parent = None
                                                    self.mt_id = None
                                                    self.external_route_tag = None
                                                    self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology.Flags()
                                                    self.forwarding_address = None
                                                    self.metric = None

                                                class Flags(FixedBitsDict):
                                                    """
                                                    Flags

                                                    Flags.
                                                    Keys are:- E

                                                    """

                                                    def __init__(self):
                                                        self._dictionary = { 
                                                            'E':False,
                                                        }
                                                        self._pos_map = { 
                                                        }

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.mt_id is None:
                                                        raise YPYModelError('Key property mt_id is None')

                                                    return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:mt-id = ' + str(self.mt_id) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.mt_id is not None:
                                                        return True

                                                    if self.external_route_tag is not None:
                                                        return True

                                                    if self.flags is not None:
                                                        if self.flags._has_data():
                                                            return True

                                                    if self.forwarding_address is not None:
                                                        return True

                                                    if self.metric is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:external'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.network_mask is not None:
                                                    return True

                                                if self.topology is not None:
                                                    for child_ref in self.topology:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External']['meta_info']


                                        class Opaque(object):
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
                                                self.parent = None
                                                self.link_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv()
                                                self.link_tlv.parent = self
                                                self.router_address_tlv = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv()
                                                self.router_address_tlv.parent = self
                                                self.unknown_tlv = YList()
                                                self.unknown_tlv.parent = self
                                                self.unknown_tlv.name = 'unknown_tlv'


                                            class UnknownTlv(object):
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
                                                    self.parent = None
                                                    self.type = None
                                                    self.length = None
                                                    self.value = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.type is None:
                                                        raise YPYModelError('Key property type is None')

                                                    return self.parent._common_path +'/ietf-ospf:unknown-tlv[ietf-ospf:type = ' + str(self.type) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.type is not None:
                                                        return True

                                                    if self.length is not None:
                                                        return True

                                                    if self.value is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv']['meta_info']


                                            class RouterAddressTlv(object):
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
                                                    self.parent = None
                                                    self.router_address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:router-address-tlv'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.router_address is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv']['meta_info']


                                            class LinkTlv(object):
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
                                                    self.parent = None
                                                    self.admin_group = None
                                                    self.link_id = None
                                                    self.link_type = None
                                                    self.local_if_ipv4_addr = YLeafList()
                                                    self.local_if_ipv4_addr.parent = self
                                                    self.local_if_ipv4_addr.name = 'local_if_ipv4_addr'
                                                    self.local_remote_ipv4_addr = YLeafList()
                                                    self.local_remote_ipv4_addr.parent = self
                                                    self.local_remote_ipv4_addr.name = 'local_remote_ipv4_addr'
                                                    self.max_bandwidth = None
                                                    self.max_reservable_bandwidth = None
                                                    self.te_metric = None
                                                    self.unknown_subtlv = YList()
                                                    self.unknown_subtlv.parent = self
                                                    self.unknown_subtlv.name = 'unknown_subtlv'
                                                    self.unreserved_bandwidth = None


                                                class UnknownSubtlv(object):
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
                                                        self.parent = None
                                                        self.type = None
                                                        self.length = None
                                                        self.value = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                                        if self.type is None:
                                                            raise YPYModelError('Key property type is None')

                                                        return self.parent._common_path +'/ietf-ospf:unknown-subtlv[ietf-ospf:type = ' + str(self.type) + ']'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.type is not None:
                                                            return True

                                                        if self.length is not None:
                                                            return True

                                                        if self.value is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/ietf-ospf:link-tlv'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.admin_group is not None:
                                                        return True

                                                    if self.link_id is not None:
                                                        return True

                                                    if self.link_type is not None:
                                                        return True

                                                    if self.local_if_ipv4_addr is not None:
                                                        for child in self.local_if_ipv4_addr:
                                                            if child is not None:
                                                                return True

                                                    if self.local_remote_ipv4_addr is not None:
                                                        for child in self.local_remote_ipv4_addr:
                                                            if child is not None:
                                                                return True

                                                    if self.max_bandwidth is not None:
                                                        return True

                                                    if self.max_reservable_bandwidth is not None:
                                                        return True

                                                    if self.te_metric is not None:
                                                        return True

                                                    if self.unknown_subtlv is not None:
                                                        for child_ref in self.unknown_subtlv:
                                                            if child_ref._has_data():
                                                                return True

                                                    if self.unreserved_bandwidth is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:opaque'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.link_tlv is not None and self.link_tlv._has_data():
                                                    return True

                                                if self.router_address_tlv is not None and self.router_address_tlv._has_data():
                                                    return True

                                                if self.unknown_tlv is not None:
                                                    for child_ref in self.unknown_tlv:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:body'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.external is not None and self.external._has_data():
                                                return True

                                            if self.network is not None and self.network._has_data():
                                                return True

                                            if self.opaque is not None and self.opaque._has_data():
                                                return True

                                            if self.router is not None and self.router._has_data():
                                                return True

                                            if self.summary is not None and self.summary._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:ospfv2'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.body is not None and self.body._has_data():
                                            return True

                                        if self.header is not None and self.header._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2']['meta_info']


                                class Ospfv3(object):
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
                                        self.parent = None
                                        self.body = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body()
                                        self.body.parent = self
                                        self.header = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header()
                                        self.header.parent = self


                                    class Header(object):
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
                                            self.parent = None
                                            self.adv_router = None
                                            self.age = None
                                            self.checksum = None
                                            self.length = None
                                            self.lsa_id = None
                                            self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header.Options()
                                            self.seq_num = None
                                            self.type = None

                                        class Options(FixedBitsDict):
                                            """
                                            Options

                                            OSPFv3 LSA options.
                                            Keys are:- R , N , DC , E , V6 , AF

                                            """

                                            def __init__(self):
                                                self._dictionary = { 
                                                    'R':False,
                                                    'N':False,
                                                    'DC':False,
                                                    'E':False,
                                                    'V6':False,
                                                    'AF':False,
                                                }
                                                self._pos_map = { 
                                                }

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:header'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.adv_router is not None:
                                                return True

                                            if self.age is not None:
                                                return True

                                            if self.checksum is not None:
                                                return True

                                            if self.length is not None:
                                                return True

                                            if self.lsa_id is not None:
                                                return True

                                            if self.options is not None:
                                                if self.options._has_data():
                                                    return True

                                            if self.seq_num is not None:
                                                return True

                                            if self.type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header']['meta_info']


                                    class Body(object):
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
                                            self.parent = None
                                            self.as_external = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal()
                                            self.as_external.parent = self
                                            self.inter_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix()
                                            self.inter_area_prefix.parent = self
                                            self.inter_area_router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter()
                                            self.inter_area_router.parent = self
                                            self.intra_area_prefix = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix()
                                            self.intra_area_prefix.parent = self
                                            self.link = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link()
                                            self.link.parent = self
                                            self.network = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network()
                                            self.network.parent = self
                                            self.nssa = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa()
                                            self.nssa.parent = self
                                            self.router = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router()
                                            self.router.parent = self


                                        class Router(object):
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
                                                self.parent = None
                                                self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Flags()
                                                self.link = YList()
                                                self.link.parent = self
                                                self.link.name = 'link'
                                                self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Options()

                                            class Flags(FixedBitsDict):
                                                """
                                                Flags

                                                LSA option.
                                                Keys are:- E , Nt , B , V

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'E':False,
                                                        'Nt':False,
                                                        'B':False,
                                                        'V':False,
                                                    }
                                                    self._pos_map = { 
                                                    }

                                            class Options(FixedBitsDict):
                                                """
                                                Options

                                                OSPFv3 LSA options.
                                                Keys are:- R , N , DC , E , V6 , AF

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'R':False,
                                                        'N':False,
                                                        'DC':False,
                                                        'E':False,
                                                        'V6':False,
                                                        'AF':False,
                                                    }
                                                    self._pos_map = { 
                                                    }


                                            class Link(object):
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
                                                    self.parent = None
                                                    self.interface_id = None
                                                    self.neighbor_interface_id = None
                                                    self.neighbor_router_id = None
                                                    self.metric = None
                                                    self.type = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.interface_id is None:
                                                        raise YPYModelError('Key property interface_id is None')
                                                    if self.neighbor_interface_id is None:
                                                        raise YPYModelError('Key property neighbor_interface_id is None')
                                                    if self.neighbor_router_id is None:
                                                        raise YPYModelError('Key property neighbor_router_id is None')

                                                    return self.parent._common_path +'/ietf-ospf:link[ietf-ospf:interface-id = ' + str(self.interface_id) + '][ietf-ospf:neighbor-interface-id = ' + str(self.neighbor_interface_id) + '][ietf-ospf:neighbor-router-id = ' + str(self.neighbor_router_id) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.interface_id is not None:
                                                        return True

                                                    if self.neighbor_interface_id is not None:
                                                        return True

                                                    if self.neighbor_router_id is not None:
                                                        return True

                                                    if self.metric is not None:
                                                        return True

                                                    if self.type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:router'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.flags is not None:
                                                    if self.flags._has_data():
                                                        return True

                                                if self.link is not None:
                                                    for child_ref in self.link:
                                                        if child_ref._has_data():
                                                            return True

                                                if self.options is not None:
                                                    if self.options._has_data():
                                                        return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router']['meta_info']


                                        class Network(object):
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
                                                self.parent = None
                                                self.attached_router = YLeafList()
                                                self.attached_router.parent = self
                                                self.attached_router.name = 'attached_router'
                                                self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network.Options()

                                            class Options(FixedBitsDict):
                                                """
                                                Options

                                                OSPFv3 LSA options.
                                                Keys are:- R , N , DC , E , V6 , AF

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'R':False,
                                                        'N':False,
                                                        'DC':False,
                                                        'E':False,
                                                        'V6':False,
                                                        'AF':False,
                                                    }
                                                    self._pos_map = { 
                                                    }

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:network'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.attached_router is not None:
                                                    for child in self.attached_router:
                                                        if child is not None:
                                                            return True

                                                if self.options is not None:
                                                    if self.options._has_data():
                                                        return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network']['meta_info']


                                        class InterAreaPrefix(object):
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
                                                self.parent = None
                                                self.metric = None
                                                self.prefix = None
                                                self.prefix_options = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:inter-area-prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.metric is not None:
                                                    return True

                                                if self.prefix is not None:
                                                    return True

                                                if self.prefix_options is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix']['meta_info']


                                        class InterAreaRouter(object):
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
                                                self.parent = None
                                                self.destination_router_id = None
                                                self.metric = None
                                                self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter.Options()

                                            class Options(FixedBitsDict):
                                                """
                                                Options

                                                OSPFv3 LSA options.
                                                Keys are:- R , N , DC , E , V6 , AF

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'R':False,
                                                        'N':False,
                                                        'DC':False,
                                                        'E':False,
                                                        'V6':False,
                                                        'AF':False,
                                                    }
                                                    self._pos_map = { 
                                                    }

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:inter-area-router'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.destination_router_id is not None:
                                                    return True

                                                if self.metric is not None:
                                                    return True

                                                if self.options is not None:
                                                    if self.options._has_data():
                                                        return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter']['meta_info']


                                        class AsExternal(object):
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
                                                self.parent = None
                                                self.external_route_tag = None
                                                self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal.Flags()
                                                self.forwarding_address = None
                                                self.metric = None
                                                self.prefix = None
                                                self.prefix_options = None
                                                self.referenced_link_state_id = None
                                                self.referenced_ls_type = None

                                            class Flags(FixedBitsDict):
                                                """
                                                Flags

                                                Flags.
                                                Keys are:- E

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'E':False,
                                                    }
                                                    self._pos_map = { 
                                                    }

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:as-external'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.external_route_tag is not None:
                                                    return True

                                                if self.flags is not None:
                                                    if self.flags._has_data():
                                                        return True

                                                if self.forwarding_address is not None:
                                                    return True

                                                if self.metric is not None:
                                                    return True

                                                if self.prefix is not None:
                                                    return True

                                                if self.prefix_options is not None:
                                                    return True

                                                if self.referenced_link_state_id is not None:
                                                    return True

                                                if self.referenced_ls_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal']['meta_info']


                                        class Nssa(object):
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
                                                self.parent = None
                                                self.external_route_tag = None
                                                self.flags = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa.Flags()
                                                self.forwarding_address = None
                                                self.metric = None
                                                self.prefix = None
                                                self.prefix_options = None
                                                self.referenced_link_state_id = None
                                                self.referenced_ls_type = None

                                            class Flags(FixedBitsDict):
                                                """
                                                Flags

                                                Flags.
                                                Keys are:- E

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'E':False,
                                                    }
                                                    self._pos_map = { 
                                                    }

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:nssa'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.external_route_tag is not None:
                                                    return True

                                                if self.flags is not None:
                                                    if self.flags._has_data():
                                                        return True

                                                if self.forwarding_address is not None:
                                                    return True

                                                if self.metric is not None:
                                                    return True

                                                if self.prefix is not None:
                                                    return True

                                                if self.prefix_options is not None:
                                                    return True

                                                if self.referenced_link_state_id is not None:
                                                    return True

                                                if self.referenced_ls_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa']['meta_info']


                                        class Link(object):
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
                                                self.parent = None
                                                self.link_local_interface_address = None
                                                self.num_of_prefixes = None
                                                self.options = RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.Options()
                                                self.prefix_list = YList()
                                                self.prefix_list.parent = self
                                                self.prefix_list.name = 'prefix_list'
                                                self.rtr_priority = None

                                            class Options(FixedBitsDict):
                                                """
                                                Options

                                                OSPFv3 LSA options.
                                                Keys are:- R , N , DC , E , V6 , AF

                                                """

                                                def __init__(self):
                                                    self._dictionary = { 
                                                        'R':False,
                                                        'N':False,
                                                        'DC':False,
                                                        'E':False,
                                                        'V6':False,
                                                        'AF':False,
                                                    }
                                                    self._pos_map = { 
                                                    }


                                            class PrefixList(object):
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
                                                    self.parent = None
                                                    self.prefix = None
                                                    self.prefix_options = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.prefix is None:
                                                        raise YPYModelError('Key property prefix is None')

                                                    return self.parent._common_path +'/ietf-ospf:prefix-list[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.prefix is not None:
                                                        return True

                                                    if self.prefix_options is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:link'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.link_local_interface_address is not None:
                                                    return True

                                                if self.num_of_prefixes is not None:
                                                    return True

                                                if self.options is not None:
                                                    if self.options._has_data():
                                                        return True

                                                if self.prefix_list is not None:
                                                    for child_ref in self.prefix_list:
                                                        if child_ref._has_data():
                                                            return True

                                                if self.rtr_priority is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link']['meta_info']


                                        class IntraAreaPrefix(object):
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
                                                self.parent = None
                                                self.num_of_prefixes = None
                                                self.prefix_list = YList()
                                                self.prefix_list.parent = self
                                                self.prefix_list.name = 'prefix_list'
                                                self.referenced_adv_router = None
                                                self.referenced_link_state_id = None
                                                self.referenced_ls_type = None


                                            class PrefixList(object):
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
                                                    self.parent = None
                                                    self.prefix = None
                                                    self.metric = None
                                                    self.prefix_options = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.prefix is None:
                                                        raise YPYModelError('Key property prefix is None')

                                                    return self.parent._common_path +'/ietf-ospf:prefix-list[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.prefix is not None:
                                                        return True

                                                    if self.metric is not None:
                                                        return True

                                                    if self.prefix_options is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:intra-area-prefix'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.num_of_prefixes is not None:
                                                    return True

                                                if self.prefix_list is not None:
                                                    for child_ref in self.prefix_list:
                                                        if child_ref._has_data():
                                                            return True

                                                if self.referenced_adv_router is not None:
                                                    return True

                                                if self.referenced_link_state_id is not None:
                                                    return True

                                                if self.referenced_ls_type is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:body'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.as_external is not None and self.as_external._has_data():
                                                return True

                                            if self.inter_area_prefix is not None and self.inter_area_prefix._has_data():
                                                return True

                                            if self.inter_area_router is not None and self.inter_area_router._has_data():
                                                return True

                                            if self.intra_area_prefix is not None and self.intra_area_prefix._has_data():
                                                return True

                                            if self.link is not None and self.link._has_data():
                                                return True

                                            if self.network is not None and self.network._has_data():
                                                return True

                                            if self.nssa is not None and self.nssa._has_data():
                                                return True

                                            if self.router is not None and self.router._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:ospfv3'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.body is not None and self.body._has_data():
                                            return True

                                        if self.header is not None and self.header._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.lsa_id is None:
                                        raise YPYModelError('Key property lsa_id is None')
                                    if self.adv_router is None:
                                        raise YPYModelError('Key property adv_router is None')

                                    return self.parent._common_path +'/ietf-ospf:as-scope-lsa[ietf-ospf:lsa-id = ' + str(self.lsa_id) + '][ietf-ospf:adv-router = ' + str(self.adv_router) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.lsa_id is not None:
                                        return True

                                    if self.adv_router is not None:
                                        return True

                                    if self.decoded_completed is not None:
                                        return True

                                    if self.ospfv2 is not None and self.ospfv2._has_data():
                                        return True

                                    if self.ospfv3 is not None and self.ospfv3._has_data():
                                        return True

                                    if self.raw_data is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.lsa_type is None:
                                    raise YPYModelError('Key property lsa_type is None')

                                return self.parent._common_path +'/ietf-ospf:as-scope-lsas[ietf-ospf:lsa-type = ' + str(self.lsa_type) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.lsa_type is not None:
                                    return True

                                if self.as_scope_lsa is not None:
                                    for child_ref in self.as_scope_lsa:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas']['meta_info']


                        class Topology(object):
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
                                self.parent = None
                                self.name = None
                                self.area = YList()
                                self.area.parent = self
                                self.area.name = 'area'


                            class Area(object):
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
                                    self.parent = None
                                    self.area_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.area_id is None:
                                        raise YPYModelError('Key property area_id is None')

                                    return self.parent._common_path +'/ietf-ospf:area[ietf-ospf:area-id = ' + str(self.area_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.area_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.area is not None:
                                    for child_ref in self.area:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.af is None:
                                raise YPYModelError('Key property af is None')

                            return self.parent._common_path +'/ietf-ospf:instance[ietf-ospf:af = ' + str(self.af) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af is not None:
                                return True

                            if self.area is not None:
                                for child_ref in self.area:
                                    if child_ref._has_data():
                                        return True

                            if self.as_scope_lsas is not None:
                                for child_ref in self.as_scope_lsas:
                                    if child_ref._has_data():
                                        return True

                            if self.router_id is not None:
                                return True

                            if self.topology is not None:
                                for child_ref in self.topology:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_routing as meta
                            return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-ospf:ospf'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.instance is not None:
                            for child_ref in self.instance:
                                if child_ref._has_data():
                                    return True

                        if self.operation_mode is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_routing as meta
                        return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-routing:routing-protocol[ietf-routing:type = ' + str(self.type) + '][ietf-routing:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.ospf is not None and self.ospf._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_routing as meta
                    return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-routing:routing-protocols'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.routing_protocol is not None:
                    for child_ref in self.routing_protocol:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['RoutingState.RoutingInstance.RoutingProtocols']['meta_info']


        class Ribs(object):
            """
            Container for RIBs.
            
            .. attribute:: rib
            
            	Each entry represents a RIB identified by the 'name' key. All routes in a RIB MUST belong to the same address family.  For each routing instance, an implementation SHOULD provide one system\-controlled default RIB for each supported address family
            	**type**\: list of    :py:class:`Rib <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                self.parent = None
                self.rib = YList()
                self.rib.parent = self
                self.rib.name = 'rib'


            class Rib(object):
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
                	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_routing.AddressFamilyIdentity>`
                
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
                    self.parent = None
                    self.name = None
                    self.address_family = None
                    self.default_rib = None
                    self.routes = RoutingState.RoutingInstance.Ribs.Rib.Routes()
                    self.routes.parent = self


                class Routes(object):
                    """
                    Current content of the RIB.
                    
                    .. attribute:: route
                    
                    	A RIB route entry. This data node MUST be augmented with information specific for routes of each address family
                    	**type**\: list of    :py:class:`Route <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route>`
                    
                    

                    """

                    _prefix = 'rt'
                    _revision = '2015-05-25'

                    def __init__(self):
                        self.parent = None
                        self.route = YList()
                        self.route.parent = self
                        self.route.name = 'route'


                    class Route(object):
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
                        	**type**\:   :py:class:`RouteTypeEnum <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.RouteTypeEnum>`
                        
                        .. attribute:: source_protocol
                        
                        	Type of the routing protocol from which the route originated
                        	**type**\:   :py:class:`RoutingProtocolIdentity <ydk.models.ietf.ietf_routing.RoutingProtocolIdentity>`
                        
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
                            self.parent = None
                            self.destination_prefix = None
                            self.active = None
                            self.last_updated = None
                            self.metric = None
                            self.next_hop = RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop()
                            self.next_hop.parent = self
                            self.route_preference = None
                            self.route_type = None
                            self.source_protocol = None
                            self.tag = None
                            self.update_source = None

                        class RouteTypeEnum(Enum):
                            """
                            RouteTypeEnum

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

                            intra_area = 0

                            inter_area = 1

                            external_1 = 2

                            external_2 = 3

                            nssa_1 = 4

                            nssa_2 = 5


                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.RouteTypeEnum']



                        class NextHop(object):
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
                            	**type**\:   :py:class:`SpecialNextHopEnum <ydk.models.ietf.ietf_routing.RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop.SpecialNextHopEnum>`
                            
                            

                            """

                            _prefix = 'rt'
                            _revision = '2015-05-25'

                            def __init__(self):
                                self.parent = None
                                self.next_hop_address = None
                                self.outgoing_interface = None
                                self.special_next_hop = None

                            class SpecialNextHopEnum(Enum):
                                """
                                SpecialNextHopEnum

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

                                blackhole = 0

                                unreachable = 1

                                prohibit = 2

                                receive = 3


                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop.SpecialNextHopEnum']


                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-routing:next-hop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.next_hop_address is not None:
                                    return True

                                if self.outgoing_interface is not None:
                                    return True

                                if self.special_next_hop is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.destination_prefix is None:
                                raise YPYModelError('Key property destination_prefix is None')

                            return self.parent._common_path +'/ietf-routing:route[ietf-routing:destination-prefix = ' + str(self.destination_prefix) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.destination_prefix is not None:
                                return True

                            if self.active is not None:
                                return True

                            if self.last_updated is not None:
                                return True

                            if self.metric is not None:
                                return True

                            if self.next_hop is not None and self.next_hop._has_data():
                                return True

                            if self.route_preference is not None:
                                return True

                            if self.route_type is not None:
                                return True

                            if self.source_protocol is not None:
                                return True

                            if self.tag is not None:
                                return True

                            if self.update_source is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_routing as meta
                            return meta._meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes.Route']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-routing:routes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.route is not None:
                            for child_ref in self.route:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_routing as meta
                        return meta._meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-routing:rib[ietf-routing:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.address_family is not None:
                        return True

                    if self.default_rib is not None:
                        return True

                    if self.routes is not None and self.routes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_routing as meta
                    return meta._meta_table['RoutingState.RoutingInstance.Ribs.Rib']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-routing:ribs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rib is not None:
                    for child_ref in self.rib:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['RoutingState.RoutingInstance.Ribs']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-routing:routing-state/ietf-routing:routing-instance[ietf-routing:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.name is not None:
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.ribs is not None and self.ribs._has_data():
                return True

            if self.router_id is not None:
                return True

            if self.routing_protocols is not None and self.routing_protocols._has_data():
                return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_routing as meta
            return meta._meta_table['RoutingState.RoutingInstance']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-routing:routing-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.routing_instance is not None:
            for child_ref in self.routing_instance:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['RoutingState']['meta_info']


class Routing(object):
    """
    Configuration parameters for the routing subsystem.
    
    .. attribute:: routing_instance
    
    	Configuration of a routing instance
    	**type**\: list of    :py:class:`RoutingInstance <ydk.models.ietf.ietf_routing.Routing.RoutingInstance>`
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        self.routing_instance = YList()
        self.routing_instance.parent = self
        self.routing_instance.name = 'routing_instance'


    class RoutingInstance(object):
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
        	**type**\:   :py:class:`RoutingInstanceIdentity <ydk.models.ietf.ietf_routing.RoutingInstanceIdentity>`
        
        	**default value**\: rt:default-routing-instance
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            self.parent = None
            self.name = None
            self.description = None
            self.enabled = None
            self.interfaces = Routing.RoutingInstance.Interfaces()
            self.interfaces.parent = self
            self.ribs = Routing.RoutingInstance.Ribs()
            self.ribs.parent = self
            self.router_id = None
            self.routing_protocols = Routing.RoutingInstance.RoutingProtocols()
            self.routing_protocols.parent = self
            self.type = None


        class Interfaces(object):
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
                self.parent = None
                self.interface = YLeafList()
                self.interface.parent = self
                self.interface.name = 'interface'

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-routing:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child in self.interface:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['Routing.RoutingInstance.Interfaces']['meta_info']


        class RoutingProtocols(object):
            """
            Configuration of routing protocol instances.
            
            .. attribute:: routing_protocol
            
            	Each entry contains configuration of a routing protocol instance
            	**type**\: list of    :py:class:`RoutingProtocol <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                self.parent = None
                self.routing_protocol = YList()
                self.routing_protocol.parent = self
                self.routing_protocol.name = 'routing_protocol'


            class RoutingProtocol(object):
                """
                Each entry contains configuration of a routing protocol
                instance.
                
                .. attribute:: type  <key>
                
                	Type of the routing protocol \- an identity derived from the 'routing\-protocol' base identity
                	**type**\:   :py:class:`RoutingProtocolIdentity <ydk.models.ietf.ietf_routing.RoutingProtocolIdentity>`
                
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
                    self.parent = None
                    self.type = None
                    self.name = None
                    self.description = None
                    self.ospf = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf()
                    self.ospf.parent = self
                    self.static_routes = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes()
                    self.static_routes.parent = self


                class StaticRoutes(object):
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
                        self.parent = None
                        self.ipv4 = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4()
                        self.ipv4.parent = self
                        self.ipv6 = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6()
                        self.ipv6.parent = self


                    class Ipv4(object):
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
                            self.parent = None
                            self.route = YList()
                            self.route.parent = self
                            self.route.name = 'route'


                        class Route(object):
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
                                self.parent = None
                                self.destination_prefix = None
                                self.description = None
                                self.next_hop = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop()
                                self.next_hop.parent = self


                            class NextHop(object):
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
                                	**type**\:   :py:class:`SpecialNextHopEnum <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop.SpecialNextHopEnum>`
                                
                                

                                """

                                _prefix = 'v4ur'
                                _revision = '2015-05-25'

                                def __init__(self):
                                    self.parent = None
                                    self.next_hop_address = None
                                    self.outgoing_interface = None
                                    self.special_next_hop = None

                                class SpecialNextHopEnum(Enum):
                                    """
                                    SpecialNextHopEnum

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

                                    blackhole = 0

                                    unreachable = 1

                                    prohibit = 2

                                    receive = 3


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop.SpecialNextHopEnum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ipv4-unicast-routing:next-hop'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.next_hop_address is not None:
                                        return True

                                    if self.outgoing_interface is not None:
                                        return True

                                    if self.special_next_hop is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.destination_prefix is None:
                                    raise YPYModelError('Key property destination_prefix is None')

                                return self.parent._common_path +'/ietf-ipv4-unicast-routing:route[ietf-ipv4-unicast-routing:destination-prefix = ' + str(self.destination_prefix) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.destination_prefix is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.next_hop is not None and self.next_hop._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-ipv4-unicast-routing:ipv4'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.route is not None:
                                for child_ref in self.route:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_routing as meta
                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4']['meta_info']


                    class Ipv6(object):
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
                            self.parent = None
                            self.route = YList()
                            self.route.parent = self
                            self.route.name = 'route'


                        class Route(object):
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
                                self.parent = None
                                self.destination_prefix = None
                                self.description = None
                                self.next_hop = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop()
                                self.next_hop.parent = self


                            class NextHop(object):
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
                                	**type**\:   :py:class:`SpecialNextHopEnum <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop.SpecialNextHopEnum>`
                                
                                

                                """

                                _prefix = 'v6ur'
                                _revision = '2015-05-25'

                                def __init__(self):
                                    self.parent = None
                                    self.next_hop_address = None
                                    self.outgoing_interface = None
                                    self.special_next_hop = None

                                class SpecialNextHopEnum(Enum):
                                    """
                                    SpecialNextHopEnum

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

                                    blackhole = 0

                                    unreachable = 1

                                    prohibit = 2

                                    receive = 3


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop.SpecialNextHopEnum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ipv6-unicast-routing:next-hop'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.next_hop_address is not None:
                                        return True

                                    if self.outgoing_interface is not None:
                                        return True

                                    if self.special_next_hop is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.destination_prefix is None:
                                    raise YPYModelError('Key property destination_prefix is None')

                                return self.parent._common_path +'/ietf-ipv6-unicast-routing:route[ietf-ipv6-unicast-routing:destination-prefix = ' + str(self.destination_prefix) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.destination_prefix is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.next_hop is not None and self.next_hop._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-ipv6-unicast-routing:ipv6'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.route is not None:
                                for child_ref in self.route:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_routing as meta
                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-routing:static-routes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ipv4 is not None and self.ipv4._has_data():
                            return True

                        if self.ipv6 is not None and self.ipv6._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_routing as meta
                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes']['meta_info']


                class Ospf(object):
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
                    	**type**\:   :py:class:`OperationModeIdentity <ydk.models.ietf.ietf_ospf.OperationModeIdentity>`
                    
                    	**default value**\: ospf:ships-in-the-night
                    
                    

                    """

                    _prefix = 'ospf'
                    _revision = '2015-03-09'

                    def __init__(self):
                        self.parent = None
                        self.all_instances_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit()
                        self.all_instances_inherit.parent = self
                        self.instance = YList()
                        self.instance.parent = self
                        self.instance.name = 'instance'
                        self.operation_mode = None


                    class AllInstancesInherit(object):
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
                            self.parent = None
                            self.area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area()
                            self.area.parent = self
                            self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface()
                            self.interface.parent = self


                        class Area(object):
                            """
                            Area config to be inherited by all areas in
                            all instances.
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:area'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area']['meta_info']


                        class Interface(object):
                            """
                            Interface config to be inherited by all interfaces
                            in all instances.
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:interface'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/ietf-ospf:all-instances-inherit'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.area is not None and self.area._has_data():
                                return True

                            if self.interface is not None and self.interface._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_routing as meta
                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit']['meta_info']


                    class Instance(object):
                        """
                        An OSPF routing protocol instance.
                        
                        .. attribute:: af  <key>
                        
                        	Address\-family of the instance
                        	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_routing.AddressFamilyIdentity>`
                        
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
                            self.parent = None
                            self.af = None
                            self.admin_distance = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance()
                            self.admin_distance.parent = self
                            self.all_areas_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit()
                            self.all_areas_inherit.parent = self
                            self.area = YList()
                            self.area.parent = self
                            self.area.name = 'area'
                            self.auto_cost = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost()
                            self.auto_cost.parent = self
                            self.database_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl()
                            self.database_control.parent = self
                            self.enable = None
                            self.fast_reroute = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute()
                            self.fast_reroute.parent = self
                            self.graceful_restart = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart()
                            self.graceful_restart.parent = self
                            self.mpls = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls()
                            self.mpls.parent = self
                            self.nsr = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr()
                            self.nsr.parent = self
                            self.reload_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl()
                            self.reload_control.parent = self
                            self.router_id = None
                            self.spf_control = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl()
                            self.spf_control.parent = self
                            self.topology = YList()
                            self.topology.parent = self
                            self.topology.name = 'topology'


                        class AdminDistance(object):
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
                                self.parent = None
                                self.external = None
                                self.inter_area = None
                                self.internal = None
                                self.intra_area = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:admin-distance'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.external is not None:
                                    return True

                                if self.inter_area is not None:
                                    return True

                                if self.internal is not None:
                                    return True

                                if self.intra_area is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance']['meta_info']


                        class Nsr(object):
                            """
                            NSR config state.
                            
                            .. attribute:: enable
                            
                            	Enable/Disable NSR
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:nsr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr']['meta_info']


                        class GracefulRestart(object):
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
                                self.parent = None
                                self.enable = None
                                self.helper_enable = None
                                self.helper_strict_lsa_checking = None
                                self.restart_interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:graceful-restart'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.helper_enable is not None:
                                    return True

                                if self.helper_strict_lsa_checking is not None:
                                    return True

                                if self.restart_interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart']['meta_info']


                        class AutoCost(object):
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
                                self.parent = None
                                self.enable = None
                                self.reference_bandwidth = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:auto-cost'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.reference_bandwidth is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost']['meta_info']


                        class SpfControl(object):
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
                                self.parent = None
                                self.paths = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:spf-control'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.paths is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl']['meta_info']


                        class DatabaseControl(object):
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
                                self.parent = None
                                self.max_lsa = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:database-control'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.max_lsa is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl']['meta_info']


                        class ReloadControl(object):
                            """
                            Protocol reload control.
                            
                            

                            """

                            _prefix = 'ospf'
                            _revision = '2015-03-09'

                            def __init__(self):
                                self.parent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:reload-control'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl']['meta_info']


                        class Mpls(object):
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
                                self.parent = None
                                self.ldp = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp()
                                self.ldp.parent = self
                                self.te_rid = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid()
                                self.te_rid.parent = self


                            class TeRid(object):
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
                                    self.parent = None
                                    self.interface = None
                                    self.router_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ospf:te-rid'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.interface is not None:
                                        return True

                                    if self.router_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid']['meta_info']


                            class Ldp(object):
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
                                    self.parent = None
                                    self.autoconfig = None
                                    self.igp_sync = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ospf:ldp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.autoconfig is not None:
                                        return True

                                    if self.igp_sync is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:mpls'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ldp is not None and self.ldp._has_data():
                                    return True

                                if self.te_rid is not None and self.te_rid._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls']['meta_info']


                        class FastReroute(object):
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
                                self.parent = None
                                self.lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa()
                                self.lfa.parent = self


                            class Lfa(object):
                                """
                                This container may be augmented with
                                global parameters for LFA.
                                Creating the container has no effect on
                                LFA activation.
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    self.parent = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ospf:lfa'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:fast-reroute'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.lfa is not None and self.lfa._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute']['meta_info']


                        class AllAreasInherit(object):
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
                                self.parent = None
                                self.area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area()
                                self.area.parent = self
                                self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface()
                                self.interface.parent = self


                            class Area(object):
                                """
                                Area config to be inherited by all areas.
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    self.parent = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ospf:area'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area']['meta_info']


                            class Interface(object):
                                """
                                Interface config to be inherited by all interfaces
                                in all areas.
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    self.parent = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ospf:interface'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/ietf-ospf:all-areas-inherit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.area is not None and self.area._has_data():
                                    return True

                                if self.interface is not None and self.interface._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit']['meta_info']


                        class Area(object):
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
                            	**type**\:   :py:class:`AreaTypeIdentity <ydk.models.ietf.ietf_ospf.AreaTypeIdentity>`
                            
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
                                self.parent = None
                                self.area_id = None
                                self.all_interfaces_inherit = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit()
                                self.all_interfaces_inherit.parent = self
                                self.area_type = None
                                self.default_cost = None
                                self.interface = YList()
                                self.interface.parent = self
                                self.interface.name = 'interface'
                                self.range = YList()
                                self.range.parent = self
                                self.range.name = 'range'
                                self.sham_link = YList()
                                self.sham_link.parent = self
                                self.sham_link.name = 'sham_link'
                                self.summary = None
                                self.virtual_link = YList()
                                self.virtual_link.parent = self
                                self.virtual_link.name = 'virtual_link'


                            class Range(object):
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
                                    self.parent = None
                                    self.prefix = None
                                    self.advertise = None
                                    self.cost = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.prefix is None:
                                        raise YPYModelError('Key property prefix is None')

                                    return self.parent._common_path +'/ietf-ospf:range[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.prefix is not None:
                                        return True

                                    if self.advertise is not None:
                                        return True

                                    if self.cost is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range']['meta_info']


                            class AllInterfacesInherit(object):
                                """
                                Inheritance for all interfaces
                                
                                .. attribute:: interface
                                
                                	Interface config to be inherited by all interfaces
                                	**type**\:   :py:class:`Interface <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface>`
                                
                                

                                """

                                _prefix = 'ospf'
                                _revision = '2015-03-09'

                                def __init__(self):
                                    self.parent = None
                                    self.interface = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface()
                                    self.interface.parent = self


                                class Interface(object):
                                    """
                                    Interface config to be inherited by all
                                    interfaces.
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        self.parent = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:interface'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/ietf-ospf:all-interfaces-inherit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.interface is not None and self.interface._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit']['meta_info']


                            class VirtualLink(object):
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
                                    self.parent = None
                                    self.router_id = None
                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication()
                                    self.authentication.parent = self
                                    self.bfd = None
                                    self.cost = None
                                    self.dead_interval = None
                                    self.enable = None
                                    self.hello_interval = None
                                    self.lls = None
                                    self.mtu_ignore = None
                                    self.prefix_suppression = None
                                    self.retransmit_interval = None
                                    self.transmit_delay = None
                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity()
                                    self.ttl_security.parent = self


                                class TtlSecurity(object):
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
                                        self.parent = None
                                        self.enable = None
                                        self.hops = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:ttl-security'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.enable is not None:
                                            return True

                                        if self.hops is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity']['meta_info']


                                class Authentication(object):
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
                                        self.parent = None
                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self.key = None
                                        self.key_chain = None
                                        self.sa = None


                                    class CryptoAlgorithm(object):
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
                                            self.parent = None
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self.md5 = None
                                            self.sha_1 = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:crypto-algorithm'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.hmac_sha1_12 is not None:
                                                return True

                                            if self.hmac_sha1_20 is not None:
                                                return True

                                            if self.hmac_sha_1 is not None:
                                                return True

                                            if self.hmac_sha_256 is not None:
                                                return True

                                            if self.hmac_sha_384 is not None:
                                                return True

                                            if self.hmac_sha_512 is not None:
                                                return True

                                            if self.md5 is not None:
                                                return True

                                            if self.sha_1 is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:authentication'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.crypto_algorithm is not None and self.crypto_algorithm._has_data():
                                            return True

                                        if self.key is not None:
                                            return True

                                        if self.key_chain is not None:
                                            return True

                                        if self.sa is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.router_id is None:
                                        raise YPYModelError('Key property router_id is None')

                                    return self.parent._common_path +'/ietf-ospf:virtual-link[ietf-ospf:router-id = ' + str(self.router_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.router_id is not None:
                                        return True

                                    if self.authentication is not None and self.authentication._has_data():
                                        return True

                                    if self.bfd is not None:
                                        return True

                                    if self.cost is not None:
                                        return True

                                    if self.dead_interval is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.hello_interval is not None:
                                        return True

                                    if self.lls is not None:
                                        return True

                                    if self.mtu_ignore is not None:
                                        return True

                                    if self.prefix_suppression is not None:
                                        return True

                                    if self.retransmit_interval is not None:
                                        return True

                                    if self.transmit_delay is not None:
                                        return True

                                    if self.ttl_security is not None and self.ttl_security._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink']['meta_info']


                            class ShamLink(object):
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
                                    self.parent = None
                                    self.local_id = None
                                    self.remote_id = None
                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication()
                                    self.authentication.parent = self
                                    self.bfd = None
                                    self.cost = None
                                    self.dead_interval = None
                                    self.enable = None
                                    self.hello_interval = None
                                    self.lls = None
                                    self.mtu_ignore = None
                                    self.prefix_suppression = None
                                    self.retransmit_interval = None
                                    self.transmit_delay = None
                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity()
                                    self.ttl_security.parent = self


                                class TtlSecurity(object):
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
                                        self.parent = None
                                        self.enable = None
                                        self.hops = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:ttl-security'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.enable is not None:
                                            return True

                                        if self.hops is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity']['meta_info']


                                class Authentication(object):
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
                                        self.parent = None
                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self.key = None
                                        self.key_chain = None
                                        self.sa = None


                                    class CryptoAlgorithm(object):
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
                                            self.parent = None
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self.md5 = None
                                            self.sha_1 = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:crypto-algorithm'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.hmac_sha1_12 is not None:
                                                return True

                                            if self.hmac_sha1_20 is not None:
                                                return True

                                            if self.hmac_sha_1 is not None:
                                                return True

                                            if self.hmac_sha_256 is not None:
                                                return True

                                            if self.hmac_sha_384 is not None:
                                                return True

                                            if self.hmac_sha_512 is not None:
                                                return True

                                            if self.md5 is not None:
                                                return True

                                            if self.sha_1 is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:authentication'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.crypto_algorithm is not None and self.crypto_algorithm._has_data():
                                            return True

                                        if self.key is not None:
                                            return True

                                        if self.key_chain is not None:
                                            return True

                                        if self.sa is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.local_id is None:
                                        raise YPYModelError('Key property local_id is None')
                                    if self.remote_id is None:
                                        raise YPYModelError('Key property remote_id is None')

                                    return self.parent._common_path +'/ietf-ospf:sham-link[ietf-ospf:local-id = ' + str(self.local_id) + '][ietf-ospf:remote-id = ' + str(self.remote_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.local_id is not None:
                                        return True

                                    if self.remote_id is not None:
                                        return True

                                    if self.authentication is not None and self.authentication._has_data():
                                        return True

                                    if self.bfd is not None:
                                        return True

                                    if self.cost is not None:
                                        return True

                                    if self.dead_interval is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.hello_interval is not None:
                                        return True

                                    if self.lls is not None:
                                        return True

                                    if self.mtu_ignore is not None:
                                        return True

                                    if self.prefix_suppression is not None:
                                        return True

                                    if self.retransmit_interval is not None:
                                        return True

                                    if self.transmit_delay is not None:
                                        return True

                                    if self.ttl_security is not None and self.ttl_security._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink']['meta_info']


                            class Interface(object):
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
                                	**type**\:   :py:class:`NetworkTypeEnum <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.NetworkTypeEnum>`
                                
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
                                    self.parent = None
                                    self.interface = None
                                    self.authentication = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication()
                                    self.authentication.parent = self
                                    self.bfd = None
                                    self.cost = None
                                    self.dead_interval = None
                                    self.demand_circuit = None
                                    self.enable = None
                                    self.fast_reroute = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute()
                                    self.fast_reroute.parent = self
                                    self.hello_interval = None
                                    self.lls = None
                                    self.mtu_ignore = None
                                    self.multi_area = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea()
                                    self.multi_area.parent = self
                                    self.network_type = None
                                    self.node_flag = None
                                    self.passive = None
                                    self.prefix_suppression = None
                                    self.retransmit_interval = None
                                    self.static_neighbors = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors()
                                    self.static_neighbors.parent = self
                                    self.topology = YList()
                                    self.topology.parent = self
                                    self.topology.name = 'topology'
                                    self.transmit_delay = None
                                    self.ttl_security = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity()
                                    self.ttl_security.parent = self

                                class NetworkTypeEnum(Enum):
                                    """
                                    NetworkTypeEnum

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

                                    broadcast = 0

                                    non_broadcast = 1

                                    point_to_multipoint = 2

                                    point_to_point = 3


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.NetworkTypeEnum']



                                class MultiArea(object):
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
                                        self.parent = None
                                        self.cost = None
                                        self.multi_area_id = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:multi-area'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.cost is not None:
                                            return True

                                        if self.multi_area_id is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea']['meta_info']


                                class StaticNeighbors(object):
                                    """
                                    Static configured neighbors.
                                    
                                    .. attribute:: neighbor
                                    
                                    	Specify a neighbor router
                                    	**type**\: list of    :py:class:`Neighbor <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.neighbor = YList()
                                        self.neighbor.parent = self
                                        self.neighbor.name = 'neighbor'


                                    class Neighbor(object):
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
                                            self.parent = None
                                            self.address = None
                                            self.cost = None
                                            self.poll_interval = None
                                            self.priority = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.address is None:
                                                raise YPYModelError('Key property address is None')

                                            return self.parent._common_path +'/ietf-ospf:neighbor[ietf-ospf:address = ' + str(self.address) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.address is not None:
                                                return True

                                            if self.cost is not None:
                                                return True

                                            if self.poll_interval is not None:
                                                return True

                                            if self.priority is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:static-neighbors'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.neighbor is not None:
                                            for child_ref in self.neighbor:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors']['meta_info']


                                class FastReroute(object):
                                    """
                                    Fast\-reroute configuration.
                                    
                                    .. attribute:: lfa
                                    
                                    	LFA configuration
                                    	**type**\:   :py:class:`Lfa <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa>`
                                    
                                    

                                    """

                                    _prefix = 'ospf'
                                    _revision = '2015-03-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa()
                                        self.lfa.parent = self


                                    class Lfa(object):
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
                                            self.parent = None
                                            self.candidate_disabled = None
                                            self.enabled = None
                                            self.remote_lfa = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa()
                                            self.remote_lfa.parent = self


                                        class RemoteLfa(object):
                                            """
                                            Remote LFA configuration.
                                            
                                            .. attribute:: enabled
                                            
                                            	Activates remote LFA
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'ospf'
                                            _revision = '2015-03-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.enabled = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/ietf-ospf:remote-lfa'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.enabled is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ietf._meta import _ietf_routing as meta
                                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:lfa'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.candidate_disabled is not None:
                                                return True

                                            if self.enabled is not None:
                                                return True

                                            if self.remote_lfa is not None and self.remote_lfa._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:fast-reroute'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.lfa is not None and self.lfa._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute']['meta_info']


                                class TtlSecurity(object):
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
                                        self.parent = None
                                        self.enable = None
                                        self.hops = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:ttl-security'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.enable is not None:
                                            return True

                                        if self.hops is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity']['meta_info']


                                class Authentication(object):
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
                                        self.parent = None
                                        self.crypto_algorithm = Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm()
                                        self.crypto_algorithm.parent = self
                                        self.key = None
                                        self.key_chain = None
                                        self.sa = None


                                    class CryptoAlgorithm(object):
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
                                            self.parent = None
                                            self.hmac_sha1_12 = None
                                            self.hmac_sha1_20 = None
                                            self.hmac_sha_1 = None
                                            self.hmac_sha_256 = None
                                            self.hmac_sha_384 = None
                                            self.hmac_sha_512 = None
                                            self.md5 = None
                                            self.sha_1 = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/ietf-ospf:crypto-algorithm'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.hmac_sha1_12 is not None:
                                                return True

                                            if self.hmac_sha1_20 is not None:
                                                return True

                                            if self.hmac_sha_1 is not None:
                                                return True

                                            if self.hmac_sha_256 is not None:
                                                return True

                                            if self.hmac_sha_384 is not None:
                                                return True

                                            if self.hmac_sha_512 is not None:
                                                return True

                                            if self.md5 is not None:
                                                return True

                                            if self.sha_1 is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ietf._meta import _ietf_routing as meta
                                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/ietf-ospf:authentication'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.crypto_algorithm is not None and self.crypto_algorithm._has_data():
                                            return True

                                        if self.key is not None:
                                            return True

                                        if self.key_chain is not None:
                                            return True

                                        if self.sa is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication']['meta_info']


                                class Topology(object):
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
                                        self.parent = None
                                        self.name = None
                                        self.cost = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.name is None:
                                            raise YPYModelError('Key property name is None')

                                        return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:name = ' + str(self.name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.name is not None:
                                            return True

                                        if self.cost is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.interface is None:
                                        raise YPYModelError('Key property interface is None')

                                    return self.parent._common_path +'/ietf-ospf:interface[ietf-ospf:interface = ' + str(self.interface) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.interface is not None:
                                        return True

                                    if self.authentication is not None and self.authentication._has_data():
                                        return True

                                    if self.bfd is not None:
                                        return True

                                    if self.cost is not None:
                                        return True

                                    if self.dead_interval is not None:
                                        return True

                                    if self.demand_circuit is not None:
                                        return True

                                    if self.enable is not None:
                                        return True

                                    if self.fast_reroute is not None and self.fast_reroute._has_data():
                                        return True

                                    if self.hello_interval is not None:
                                        return True

                                    if self.lls is not None:
                                        return True

                                    if self.mtu_ignore is not None:
                                        return True

                                    if self.multi_area is not None and self.multi_area._has_data():
                                        return True

                                    if self.network_type is not None:
                                        return True

                                    if self.node_flag is not None:
                                        return True

                                    if self.passive is not None:
                                        return True

                                    if self.prefix_suppression is not None:
                                        return True

                                    if self.retransmit_interval is not None:
                                        return True

                                    if self.static_neighbors is not None and self.static_neighbors._has_data():
                                        return True

                                    if self.topology is not None:
                                        for child_ref in self.topology:
                                            if child_ref._has_data():
                                                return True

                                    if self.transmit_delay is not None:
                                        return True

                                    if self.ttl_security is not None and self.ttl_security._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.area_id is None:
                                    raise YPYModelError('Key property area_id is None')

                                return self.parent._common_path +'/ietf-ospf:area[ietf-ospf:area-id = ' + str(self.area_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.area_id is not None:
                                    return True

                                if self.all_interfaces_inherit is not None and self.all_interfaces_inherit._has_data():
                                    return True

                                if self.area_type is not None:
                                    return True

                                if self.default_cost is not None:
                                    return True

                                if self.interface is not None:
                                    for child_ref in self.interface:
                                        if child_ref._has_data():
                                            return True

                                if self.range is not None:
                                    for child_ref in self.range:
                                        if child_ref._has_data():
                                            return True

                                if self.sham_link is not None:
                                    for child_ref in self.sham_link:
                                        if child_ref._has_data():
                                            return True

                                if self.summary is not None:
                                    return True

                                if self.virtual_link is not None:
                                    for child_ref in self.virtual_link:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']


                        class Topology(object):
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
                                self.parent = None
                                self.name = None
                                self.area = YList()
                                self.area.parent = self
                                self.area.name = 'area'


                            class Area(object):
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
                                	**type**\:   :py:class:`AreaTypeIdentity <ydk.models.ietf.ietf_ospf.AreaTypeIdentity>`
                                
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
                                    self.parent = None
                                    self.area_id = None
                                    self.area_type = None
                                    self.default_cost = None
                                    self.range = YList()
                                    self.range.parent = self
                                    self.range.name = 'range'
                                    self.summary = None


                                class Range(object):
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
                                        self.parent = None
                                        self.prefix = None
                                        self.advertise = None
                                        self.cost = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.prefix is None:
                                            raise YPYModelError('Key property prefix is None')

                                        return self.parent._common_path +'/ietf-ospf:range[ietf-ospf:prefix = ' + str(self.prefix) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.prefix is not None:
                                            return True

                                        if self.advertise is not None:
                                            return True

                                        if self.cost is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ietf._meta import _ietf_routing as meta
                                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.area_id is None:
                                        raise YPYModelError('Key property area_id is None')

                                    return self.parent._common_path +'/ietf-ospf:area[ietf-ospf:area-id = ' + str(self.area_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.area_id is not None:
                                        return True

                                    if self.area_type is not None:
                                        return True

                                    if self.default_cost is not None:
                                        return True

                                    if self.range is not None:
                                        for child_ref in self.range:
                                            if child_ref._has_data():
                                                return True

                                    if self.summary is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ietf._meta import _ietf_routing as meta
                                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/ietf-ospf:topology[ietf-ospf:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.area is not None:
                                    for child_ref in self.area:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ietf._meta import _ietf_routing as meta
                                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.af is None:
                                raise YPYModelError('Key property af is None')

                            return self.parent._common_path +'/ietf-ospf:instance[ietf-ospf:af = ' + str(self.af) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.af is not None:
                                return True

                            if self.admin_distance is not None and self.admin_distance._has_data():
                                return True

                            if self.all_areas_inherit is not None and self.all_areas_inherit._has_data():
                                return True

                            if self.area is not None:
                                for child_ref in self.area:
                                    if child_ref._has_data():
                                        return True

                            if self.auto_cost is not None and self.auto_cost._has_data():
                                return True

                            if self.database_control is not None and self.database_control._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.fast_reroute is not None and self.fast_reroute._has_data():
                                return True

                            if self.graceful_restart is not None and self.graceful_restart._has_data():
                                return True

                            if self.mpls is not None and self.mpls._has_data():
                                return True

                            if self.nsr is not None and self.nsr._has_data():
                                return True

                            if self.reload_control is not None and self.reload_control._has_data():
                                return True

                            if self.router_id is not None:
                                return True

                            if self.spf_control is not None and self.spf_control._has_data():
                                return True

                            if self.topology is not None:
                                for child_ref in self.topology:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ietf._meta import _ietf_routing as meta
                            return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/ietf-ospf:ospf'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.all_instances_inherit is not None and self.all_instances_inherit._has_data():
                            return True

                        if self.instance is not None:
                            for child_ref in self.instance:
                                if child_ref._has_data():
                                    return True

                        if self.operation_mode is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_routing as meta
                        return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.type is None:
                        raise YPYModelError('Key property type is None')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-routing:routing-protocol[ietf-routing:type = ' + str(self.type) + '][ietf-routing:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.type is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.ospf is not None and self.ospf._has_data():
                        return True

                    if self.static_routes is not None and self.static_routes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_routing as meta
                    return meta._meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-routing:routing-protocols'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.routing_protocol is not None:
                    for child_ref in self.routing_protocol:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['Routing.RoutingInstance.RoutingProtocols']['meta_info']


        class Ribs(object):
            """
            Configuration of RIBs.
            
            .. attribute:: rib
            
            	Each entry contains configuration for a RIB identified by the 'name' key.  Entries having the same key as a system\-controlled entry of the list /routing\-state/routing\-instance/ribs/rib are used for configuring parameters of that entry. Other entries define additional user\-controlled RIBs
            	**type**\: list of    :py:class:`Rib <ydk.models.ietf.ietf_routing.Routing.RoutingInstance.Ribs.Rib>`
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                self.parent = None
                self.rib = YList()
                self.rib.parent = self
                self.rib.name = 'rib'


            class Rib(object):
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
                	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_routing.AddressFamilyIdentity>`
                
                .. attribute:: description
                
                	Textual description of the RIB
                	**type**\:  str
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.address_family = None
                    self.description = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/ietf-routing:rib[ietf-routing:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.address_family is not None:
                        return True

                    if self.description is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_routing as meta
                    return meta._meta_table['Routing.RoutingInstance.Ribs.Rib']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/ietf-routing:ribs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.rib is not None:
                    for child_ref in self.rib:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['Routing.RoutingInstance.Ribs']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-routing:routing/ietf-routing:routing-instance[ietf-routing:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.description is not None:
                return True

            if self.enabled is not None:
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            if self.ribs is not None and self.ribs._has_data():
                return True

            if self.router_id is not None:
                return True

            if self.routing_protocols is not None and self.routing_protocols._has_data():
                return True

            if self.type is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_routing as meta
            return meta._meta_table['Routing.RoutingInstance']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-routing:routing'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.routing_instance is not None:
            for child_ref in self.routing_instance:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['Routing']['meta_info']


class FibRouteRpc(object):
    """
    Return the active FIB route that a routing\-instance uses for
    sending packets to a destination address.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.ietf.ietf_routing.FibRouteRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.ietf.ietf_routing.FibRouteRpc.Output>`
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        self.input = FibRouteRpc.Input()
        self.input.parent = self
        self.output = FibRouteRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: destination_address
        
        	Network layer destination address.  Address family specific modules MUST augment this container with a leaf named 'address'
        	**type**\:   :py:class:`DestinationAddress <ydk.models.ietf.ietf_routing.FibRouteRpc.Input.DestinationAddress>`
        
        .. attribute:: routing_instance_name
        
        	Name of the routing instance whose forwarding information base is being queried.  If the routing instance with name equal to the value of this parameter doesn't exist, then this operation SHALL fail with error\-tag 'data\-missing' and error\-app\-tag 'routing\-instance\-not\-found'
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            self.parent = None
            self.destination_address = FibRouteRpc.Input.DestinationAddress()
            self.destination_address.parent = self
            self.routing_instance_name = None


        class DestinationAddress(object):
            """
            Network layer destination address.
            
            Address family specific modules MUST augment this
            container with a leaf named 'address'.
            
            .. attribute:: address_family
            
            	Address family
            	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_routing.AddressFamilyIdentity>`
            
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
                self.parent = None
                self.address_family = None
                self.ietf_ipv4_unicast_routing_address = None
                self.ietf_ipv6_unicast_routing_address = None

            @property
            def _common_path(self):

                return '/ietf-routing:fib-route/ietf-routing:input/ietf-routing:destination-address'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.address_family is not None:
                    return True

                if self.ietf_ipv4_unicast_routing_address is not None:
                    return True

                if self.ietf_ipv6_unicast_routing_address is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['FibRouteRpc.Input.DestinationAddress']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-routing:fib-route/ietf-routing:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.destination_address is not None and self.destination_address._has_data():
                return True

            if self.routing_instance_name is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_routing as meta
            return meta._meta_table['FibRouteRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: route
        
        	The active FIB route for the specified destination.  If the routing instance has no active FIB route for the destination address, no output is returned \- the server SHALL send an <rpc\-reply> containing a single element <ok>.  Address family specific modules MUST augment this list with appropriate route contents
        	**type**\:   :py:class:`Route <ydk.models.ietf.ietf_routing.FibRouteRpc.Output.Route>`
        
        

        """

        _prefix = 'rt'
        _revision = '2015-05-25'

        def __init__(self):
            self.parent = None
            self.route = FibRouteRpc.Output.Route()
            self.route.parent = self


        class Route(object):
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
            	**type**\:   :py:class:`AddressFamilyIdentity <ydk.models.ietf.ietf_routing.AddressFamilyIdentity>`
            
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
            	**type**\:   :py:class:`NextHop <ydk.models.ietf.ietf_routing.FibRouteRpc.Output.Route.NextHop>`
            
            .. attribute:: source_protocol
            
            	Type of the routing protocol from which the route originated
            	**type**\:   :py:class:`RoutingProtocolIdentity <ydk.models.ietf.ietf_routing.RoutingProtocolIdentity>`
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'rt'
            _revision = '2015-05-25'

            def __init__(self):
                self.parent = None
                self.active = None
                self.address_family = None
                self.ietf_ipv4_unicast_routing_destination_prefix = None
                self.ietf_ipv6_unicast_routing_destination_prefix = None
                self.last_updated = None
                self.next_hop = FibRouteRpc.Output.Route.NextHop()
                self.next_hop.parent = self
                self.source_protocol = None


            class NextHop(object):
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
                	**type**\:   :py:class:`SpecialNextHopEnum <ydk.models.ietf.ietf_routing.FibRouteRpc.Output.Route.NextHop.SpecialNextHopEnum>`
                
                

                """

                _prefix = 'rt'
                _revision = '2015-05-25'

                def __init__(self):
                    self.parent = None
                    self.ietf_ipv4_unicast_routing_next_hop_address = None
                    self.ietf_ipv6_unicast_routing_next_hop_address = None
                    self.ietf_routing_next_hop_address = None
                    self.outgoing_interface = None
                    self.special_next_hop = None

                class SpecialNextHopEnum(Enum):
                    """
                    SpecialNextHopEnum

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

                    blackhole = 0

                    unreachable = 1

                    prohibit = 2

                    receive = 3


                    @staticmethod
                    def _meta_info():
                        from ydk.models.ietf._meta import _ietf_routing as meta
                        return meta._meta_table['FibRouteRpc.Output.Route.NextHop.SpecialNextHopEnum']


                @property
                def _common_path(self):

                    return '/ietf-routing:fib-route/ietf-routing:output/ietf-routing:route/ietf-routing:next-hop'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    if self.parent is None:
                        raise YPYError('Parent reference is needed to determine if entity has configuration data')
                    return self.parent.is_config()

                def _has_data(self):
                    if self.ietf_ipv4_unicast_routing_next_hop_address is not None:
                        return True

                    if self.ietf_ipv6_unicast_routing_next_hop_address is not None:
                        return True

                    if self.ietf_routing_next_hop_address is not None:
                        return True

                    if self.outgoing_interface is not None:
                        return True

                    if self.special_next_hop is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ietf._meta import _ietf_routing as meta
                    return meta._meta_table['FibRouteRpc.Output.Route.NextHop']['meta_info']

            @property
            def _common_path(self):

                return '/ietf-routing:fib-route/ietf-routing:output/ietf-routing:route'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.active is not None:
                    return True

                if self.address_family is not None:
                    return True

                if self.ietf_ipv4_unicast_routing_destination_prefix is not None:
                    return True

                if self.ietf_ipv6_unicast_routing_destination_prefix is not None:
                    return True

                if self.last_updated is not None:
                    return True

                if self.next_hop is not None and self.next_hop._has_data():
                    return True

                if self.source_protocol is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_routing as meta
                return meta._meta_table['FibRouteRpc.Output.Route']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-routing:fib-route/ietf-routing:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.route is not None and self.route._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_routing as meta
            return meta._meta_table['FibRouteRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-routing:fib-route'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['FibRouteRpc']['meta_info']


class DefaultRoutingInstanceIdentity(RoutingInstanceIdentity):
    """
    This identity represents either a default routing instance, or
    the only routing instance on systems that do not support
    multiple instances.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        RoutingInstanceIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['DefaultRoutingInstanceIdentity']['meta_info']


class StaticIdentity(RoutingProtocolIdentity):
    """
    Static routing pseudo\-protocol.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['StaticIdentity']['meta_info']


class VrfRoutingInstanceIdentity(RoutingInstanceIdentity):
    """
    This identity represents a VRF routing instance. The type is
    distinct from the default\-routing\-instance. There may be
    multiple vrf\-routing\-interfaces.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        RoutingInstanceIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['VrfRoutingInstanceIdentity']['meta_info']


class Ipv6Identity(AddressFamilyIdentity):
    """
    This identity represents IPv6 address family.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['Ipv6Identity']['meta_info']


class DirectIdentity(RoutingProtocolIdentity):
    """
    Routing pseudo\-protocol that provides routes to directly
    connected networks.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        RoutingProtocolIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['DirectIdentity']['meta_info']


class Ipv4Identity(AddressFamilyIdentity):
    """
    This identity represents IPv4 address family.
    
    

    """

    _prefix = 'rt'
    _revision = '2015-05-25'

    def __init__(self):
        AddressFamilyIdentity.__init__(self)

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_routing as meta
        return meta._meta_table['Ipv4Identity']['meta_info']


