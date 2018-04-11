""" Cisco_IOS_XE_ospf_oper 

This module contains a collection of YANG definitions for
monitoring the operation of ospf protocol in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AddressFamily(Enum):
    """
    AddressFamily (Enum Class)

    Address family type

    .. data:: address_family_ipv4 = 0

    .. data:: address_family_ipv6 = 1

    """

    address_family_ipv4 = Enum.YLeaf(0, "address-family-ipv4")

    address_family_ipv6 = Enum.YLeaf(1, "address-family-ipv6")


class NbrStateType(Enum):
    """
    NbrStateType (Enum Class)

    OSPF neighbor state type

    .. data:: ospf_nbr_down = 1

    	Neighbor state down

    .. data:: ospf_nbr_attempt = 2

    	Neighbor attempt state

    .. data:: ospf_nbr_init = 3

    	Neighbor init state

    .. data:: ospf_nbr_two_way = 4

    	Neighbor 2-way state

    .. data:: ospf_nbr_exchange_start = 5

    	Neighbor exchange start state

    .. data:: ospf_nbr_exchange = 6

    	Neighbor exchange state

    .. data:: ospf_nbr_loading = 7

    	Neighbor loading state

    .. data:: ospf_nbr_full = 8

    	Neighbor full state

    """

    ospf_nbr_down = Enum.YLeaf(1, "ospf-nbr-down")

    ospf_nbr_attempt = Enum.YLeaf(2, "ospf-nbr-attempt")

    ospf_nbr_init = Enum.YLeaf(3, "ospf-nbr-init")

    ospf_nbr_two_way = Enum.YLeaf(4, "ospf-nbr-two-way")

    ospf_nbr_exchange_start = Enum.YLeaf(5, "ospf-nbr-exchange-start")

    ospf_nbr_exchange = Enum.YLeaf(6, "ospf-nbr-exchange")

    ospf_nbr_loading = Enum.YLeaf(7, "ospf-nbr-loading")

    ospf_nbr_full = Enum.YLeaf(8, "ospf-nbr-full")


class OspfAuthType(Enum):
    """
    OspfAuthType (Enum Class)

    OSPF Authentication type

    .. data:: ospf_auth_ipsec = 0

    .. data:: ospf_auth_trailer_keychain = 1

    .. data:: ospf_auth_trailer_key = 2

    .. data:: ospf_auth_type_none = 3

    """

    ospf_auth_ipsec = Enum.YLeaf(0, "ospf-auth-ipsec")

    ospf_auth_trailer_keychain = Enum.YLeaf(1, "ospf-auth-trailer-keychain")

    ospf_auth_trailer_key = Enum.YLeaf(2, "ospf-auth-trailer-key")

    ospf_auth_type_none = Enum.YLeaf(3, "ospf-auth-type-none")


class OspfNetworkType(Enum):
    """
    OspfNetworkType (Enum Class)

    OSPF network type

    .. data:: ospf_broadcast = 0

    	OSPF broadcast multi-access network

    .. data:: ospf_non_broadcast = 1

    	OSPF Non-Broadcast Multi-Access (NBMA) network

    .. data:: ospf_point_to_multipoint = 2

    	OSPF point-to-multipoint network

    .. data:: ospf_point_to_point = 3

    	OSPF point-to-point network

    """

    ospf_broadcast = Enum.YLeaf(0, "ospf-broadcast")

    ospf_non_broadcast = Enum.YLeaf(1, "ospf-non-broadcast")

    ospf_point_to_multipoint = Enum.YLeaf(2, "ospf-point-to-multipoint")

    ospf_point_to_point = Enum.YLeaf(3, "ospf-point-to-point")


class OspfOperationMode(Enum):
    """
    OspfOperationMode (Enum Class)

    OSPF operational mode

    .. data:: ospf_ships_in_the_night = 0

    	Ships-in-the-night operation mode in which each OSPF instance carries only one address family

    """

    ospf_ships_in_the_night = Enum.YLeaf(0, "ospf-ships-in-the-night")



class OspfOperData(Entity):
    """
    Operational state of ospf
    
    .. attribute:: ospf_state
    
    	OSPF operational state
    	**type**\:  :py:class:`OspfState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'ospf-ios-xe-oper'
    _revision = '2017-10-10'

    def __init__(self):
        super(OspfOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "ospf-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-ospf-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ospf-state", ("ospf_state", OspfOperData.OspfState))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ospf_state = None
        self._children_name_map["ospf_state"] = "ospf-state"
        self._children_yang_names.add("ospf-state")
        self._segment_path = lambda: "Cisco-IOS-XE-ospf-oper:ospf-oper-data"


    class OspfState(Entity):
        """
        OSPF operational state
        
        .. attribute:: op_mode
        
        	OSPF operation mode
        	**type**\:  :py:class:`OspfOperationMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperationMode>`
        
        .. attribute:: ospf_instance
        
        	OSPF routing protocol instance
        	**type**\: list of  		 :py:class:`OspfInstance <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ospf-ios-xe-oper'
        _revision = '2017-10-10'

        def __init__(self):
            super(OspfOperData.OspfState, self).__init__()

            self.yang_name = "ospf-state"
            self.yang_parent_name = "ospf-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ospf-instance", ("ospf_instance", OspfOperData.OspfState.OspfInstance))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('op_mode', YLeaf(YType.enumeration, 'op-mode')),
            ])
            self.op_mode = None

            self.ospf_instance = YList(self)
            self._segment_path = lambda: "ospf-state"
            self._absolute_path = lambda: "Cisco-IOS-XE-ospf-oper:ospf-oper-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(OspfOperData.OspfState, ['op_mode'], name, value)


        class OspfInstance(Entity):
            """
            OSPF routing protocol instance
            
            .. attribute:: af  (key)
            
            	Address\-family of the instance
            	**type**\:  :py:class:`AddressFamily <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.AddressFamily>`
            
            .. attribute:: router_id  (key)
            
            	Defined in RFC 2328. A 32\-bit number that uniquely identifies the router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospf_area
            
            	List of ospf areas
            	**type**\: list of  		 :py:class:`OspfArea <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea>`
            
            .. attribute:: link_scope_lsas
            
            	List OSPF link scope LSA
            	**type**\: list of  		 :py:class:`LinkScopeLsas <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas>`
            
            .. attribute:: multi_topology
            
            	OSPF multi\-topology interface augmentation
            	**type**\: list of  		 :py:class:`MultiTopology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.MultiTopology>`
            
            

            """

            _prefix = 'ospf-ios-xe-oper'
            _revision = '2017-10-10'

            def __init__(self):
                super(OspfOperData.OspfState.OspfInstance, self).__init__()

                self.yang_name = "ospf-instance"
                self.yang_parent_name = "ospf-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['af','router_id']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("ospf-area", ("ospf_area", OspfOperData.OspfState.OspfInstance.OspfArea)), ("link-scope-lsas", ("link_scope_lsas", OspfOperData.OspfState.OspfInstance.LinkScopeLsas)), ("multi-topology", ("multi_topology", OspfOperData.OspfState.OspfInstance.MultiTopology))])
                self._leafs = OrderedDict([
                    ('af', YLeaf(YType.enumeration, 'af')),
                    ('router_id', YLeaf(YType.uint32, 'router-id')),
                ])
                self.af = None
                self.router_id = None

                self.ospf_area = YList(self)
                self.link_scope_lsas = YList(self)
                self.multi_topology = YList(self)
                self._segment_path = lambda: "ospf-instance" + "[af='" + str(self.af) + "']" + "[router-id='" + str(self.router_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-ospf-oper:ospf-oper-data/ospf-state/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(OspfOperData.OspfState.OspfInstance, ['af', 'router_id'], name, value)


            class OspfArea(Entity):
                """
                List of ospf areas
                
                .. attribute:: area_id  (key)
                
                	OSPF area ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ospf_interface
                
                	List of OSPF interfaces
                	**type**\: list of  		 :py:class:`OspfInterface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface>`
                
                .. attribute:: area_scope_lsa
                
                	List of OSPF area scope LSA
                	**type**\: list of  		 :py:class:`AreaScopeLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2017-10-10'

                def __init__(self):
                    super(OspfOperData.OspfState.OspfInstance.OspfArea, self).__init__()

                    self.yang_name = "ospf-area"
                    self.yang_parent_name = "ospf-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['area_id']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ospf-interface", ("ospf_interface", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface)), ("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa))])
                    self._leafs = OrderedDict([
                        ('area_id', YLeaf(YType.uint32, 'area-id')),
                    ])
                    self.area_id = None

                    self.ospf_interface = YList(self)
                    self.area_scope_lsa = YList(self)
                    self._segment_path = lambda: "ospf-area" + "[area-id='" + str(self.area_id) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea, ['area_id'], name, value)


                class OspfInterface(Entity):
                    """
                    List of OSPF interfaces
                    
                    .. attribute:: name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: network_type
                    
                    	Network type
                    	**type**\:  :py:class:`OspfNetworkType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfNetworkType>`
                    
                    .. attribute:: passive
                    
                    	Enable/Disable passive
                    	**type**\: bool
                    
                    .. attribute:: demand_circuit
                    
                    	Enable/Disable demand circuit
                    	**type**\: bool
                    
                    .. attribute:: multi_area
                    
                    	Multi Area
                    	**type**\:  :py:class:`MultiArea <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.MultiArea>`
                    
                    .. attribute:: static_neighbor
                    
                    	Staticly configured neighbors
                    	**type**\: list of  		 :py:class:`StaticNeighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.StaticNeighbor>`
                    
                    .. attribute:: node_flag
                    
                    	Set prefix as a node representative prefix
                    	**type**\: bool
                    
                    .. attribute:: fast_reroute
                    
                    	Fast reroute config
                    	**type**\:  :py:class:`FastReroute <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute>`
                    
                    .. attribute:: cost
                    
                    	Interface cost
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: hello_interval
                    
                    	Time between hello packets
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: dead_interval
                    
                    	Interval after which a neighbor is declared dead
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: retransmit_interval
                    
                    	Time between retransmitting unacknowledged Link State Advertisements (LSAs)
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: transmit_delay
                    
                    	Estimated time needed to send link\-state update
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
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
                    
                    	TTL security
                    	**type**\:  :py:class:`TtlSecurity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity>`
                    
                    .. attribute:: enable
                    
                    	Enable/disable protocol on the interface
                    	**type**\: bool
                    
                    .. attribute:: authentication
                    
                    	Authentication configuration
                    	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication>`
                    
                    .. attribute:: state
                    
                    	Interface state
                    	**type**\: str
                    
                    .. attribute:: hello_timer
                    
                    	Hello timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: wait_timer
                    
                    	Wait timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dr
                    
                    	Designated Router
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: bdr
                    
                    	Backup Designated Router
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ospf_neighbor
                    
                    	List of OSPF neighbors
                    	**type**\: list of  		 :py:class:`OspfNeighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor>`
                    
                    .. attribute:: intf_link_scope_lsas
                    
                    	List OSPF link scope LSAs
                    	**type**\: list of  		 :py:class:`IntfLinkScopeLsas <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas>`
                    
                    .. attribute:: intf_multi_topology
                    
                    	OSPF interface topology
                    	**type**\: list of  		 :py:class:`IntfMultiTopology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfMultiTopology>`
                    
                    .. attribute:: priority
                    
                    	Configure OSPF router priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface, self).__init__()

                        self.yang_name = "ospf-interface"
                        self.yang_parent_name = "ospf-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_container_classes = OrderedDict([("multi-area", ("multi_area", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.MultiArea)), ("fast-reroute", ("fast_reroute", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute)), ("ttl-security", ("ttl_security", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity)), ("authentication", ("authentication", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication))])
                        self._child_list_classes = OrderedDict([("static-neighbor", ("static_neighbor", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.StaticNeighbor)), ("ospf-neighbor", ("ospf_neighbor", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor)), ("intf-link-scope-lsas", ("intf_link_scope_lsas", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas)), ("intf-multi-topology", ("intf_multi_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfMultiTopology))])
                        self._leafs = OrderedDict([
                            ('name', YLeaf(YType.str, 'name')),
                            ('network_type', YLeaf(YType.enumeration, 'network-type')),
                            ('passive', YLeaf(YType.boolean, 'passive')),
                            ('demand_circuit', YLeaf(YType.boolean, 'demand-circuit')),
                            ('node_flag', YLeaf(YType.boolean, 'node-flag')),
                            ('cost', YLeaf(YType.uint16, 'cost')),
                            ('hello_interval', YLeaf(YType.uint16, 'hello-interval')),
                            ('dead_interval', YLeaf(YType.uint16, 'dead-interval')),
                            ('retransmit_interval', YLeaf(YType.uint16, 'retransmit-interval')),
                            ('transmit_delay', YLeaf(YType.uint16, 'transmit-delay')),
                            ('mtu_ignore', YLeaf(YType.boolean, 'mtu-ignore')),
                            ('lls', YLeaf(YType.boolean, 'lls')),
                            ('prefix_suppression', YLeaf(YType.boolean, 'prefix-suppression')),
                            ('bfd', YLeaf(YType.boolean, 'bfd')),
                            ('enable', YLeaf(YType.boolean, 'enable')),
                            ('state', YLeaf(YType.str, 'state')),
                            ('hello_timer', YLeaf(YType.uint32, 'hello-timer')),
                            ('wait_timer', YLeaf(YType.uint32, 'wait-timer')),
                            ('dr', YLeaf(YType.str, 'dr')),
                            ('bdr', YLeaf(YType.str, 'bdr')),
                            ('priority', YLeaf(YType.uint8, 'priority')),
                        ])
                        self.name = None
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
                        self.priority = None

                        self.multi_area = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.MultiArea()
                        self.multi_area.parent = self
                        self._children_name_map["multi_area"] = "multi-area"
                        self._children_yang_names.add("multi-area")

                        self.fast_reroute = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute()
                        self.fast_reroute.parent = self
                        self._children_name_map["fast_reroute"] = "fast-reroute"
                        self._children_yang_names.add("fast-reroute")

                        self.ttl_security = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity()
                        self.ttl_security.parent = self
                        self._children_name_map["ttl_security"] = "ttl-security"
                        self._children_yang_names.add("ttl-security")

                        self.authentication = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"
                        self._children_yang_names.add("authentication")

                        self.static_neighbor = YList(self)
                        self.ospf_neighbor = YList(self)
                        self.intf_link_scope_lsas = YList(self)
                        self.intf_multi_topology = YList(self)
                        self._segment_path = lambda: "ospf-interface" + "[name='" + str(self.name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface, ['name', 'network_type', 'passive', 'demand_circuit', 'node_flag', 'cost', 'hello_interval', 'dead_interval', 'retransmit_interval', 'transmit_delay', 'mtu_ignore', 'lls', 'prefix_suppression', 'bfd', 'enable', 'state', 'hello_timer', 'wait_timer', 'dr', 'bdr', 'priority'], name, value)


                    class MultiArea(Entity):
                        """
                        Multi Area
                        
                        .. attribute:: multi_area_id
                        
                        	Multi\-area ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cost
                        
                        	Interface cost for multi\-area
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.MultiArea, self).__init__()

                            self.yang_name = "multi-area"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('multi_area_id', YLeaf(YType.uint32, 'multi-area-id')),
                                ('cost', YLeaf(YType.uint16, 'cost')),
                            ])
                            self.multi_area_id = None
                            self.cost = None
                            self._segment_path = lambda: "multi-area"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.MultiArea, ['multi_area_id', 'cost'], name, value)


                    class StaticNeighbor(Entity):
                        """
                        Staticly configured neighbors
                        
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
                        
                        	**range:** 0..65535
                        
                        .. attribute:: poll_interval
                        
                        	Neighbor polling intervali in seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**units**\: seconds
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.StaticNeighbor, self).__init__()

                            self.yang_name = "static-neighbor"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', YLeaf(YType.str, 'address')),
                                ('cost', YLeaf(YType.uint16, 'cost')),
                                ('poll_interval', YLeaf(YType.uint16, 'poll-interval')),
                            ])
                            self.address = None
                            self.cost = None
                            self.poll_interval = None
                            self._segment_path = lambda: "static-neighbor" + "[address='" + str(self.address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.StaticNeighbor, ['address', 'cost', 'poll_interval'], name, value)


                    class FastReroute(Entity):
                        """
                        Fast reroute config
                        
                        .. attribute:: candidate_disabled
                        
                        	Prevent the interface to be used as backup
                        	**type**\: bool
                        
                        .. attribute:: enabled
                        
                        	Activates LFA. This model assumes activation of per\-prefix LFA
                        	**type**\: bool
                        
                        .. attribute:: remote_lfa_enabled
                        
                        	Activates remote LFA
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute, self).__init__()

                            self.yang_name = "fast-reroute"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('candidate_disabled', YLeaf(YType.boolean, 'candidate-disabled')),
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('remote_lfa_enabled', YLeaf(YType.boolean, 'remote-lfa-enabled')),
                            ])
                            self.candidate_disabled = None
                            self.enabled = None
                            self.remote_lfa_enabled = None
                            self._segment_path = lambda: "fast-reroute"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute, ['candidate_disabled', 'enabled', 'remote_lfa_enabled'], name, value)


                    class TtlSecurity(Entity):
                        """
                        TTL security
                        
                        .. attribute:: enabled
                        
                        	Enable/Disable TTL security check
                        	**type**\: bool
                        
                        .. attribute:: hops
                        
                        	Maximum number of hops that a OSPF packet may have traveled
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity, self).__init__()

                            self.yang_name = "ttl-security"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ('hops', YLeaf(YType.uint8, 'hops')),
                            ])
                            self.enabled = None
                            self.hops = None
                            self._segment_path = lambda: "ttl-security"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity, ['enabled', 'hops'], name, value)


                    class Authentication(Entity):
                        """
                        Authentication configuration
                        
                        .. attribute:: sa
                        
                        	SA name
                        	**type**\: str
                        
                        .. attribute:: key_chain
                        
                        	key\-chain name
                        	**type**\: str
                        
                        .. attribute:: key_string
                        
                        	Key string in ASCII format
                        	**type**\: str
                        
                        .. attribute:: crypto_algorithm_val
                        
                        	Crypto algorithm
                        	**type**\:  :py:class:`CryptoAlgorithmVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal>`
                        
                        .. attribute:: no_auth
                        
                        	No authentication enabled
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("crypto-algorithm-val", ("crypto_algorithm_val", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sa', YLeaf(YType.str, 'sa')),
                                ('key_chain', YLeaf(YType.str, 'key-chain')),
                                ('key_string', YLeaf(YType.str, 'key-string')),
                                ('no_auth', YLeaf(YType.uint32, 'no-auth')),
                            ])
                            self.sa = None
                            self.key_chain = None
                            self.key_string = None
                            self.no_auth = None

                            self.crypto_algorithm_val = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal()
                            self.crypto_algorithm_val.parent = self
                            self._children_name_map["crypto_algorithm_val"] = "crypto-algorithm-val"
                            self._children_yang_names.add("crypto-algorithm-val")
                            self._segment_path = lambda: "authentication"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication, ['sa', 'key_chain', 'key_string', 'no_auth'], name, value)


                        class CryptoAlgorithmVal(Entity):
                            """
                            Crypto algorithm
                            
                            .. attribute:: hmac_sha1_12
                            
                            	HMAC\-SHA1\-12 algorithm
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: hmac_sha1_20
                            
                            	HMAC\-SHA1\-20 algorithm
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: md5
                            
                            	MD5 algorithm
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: sha_1
                            
                            	SHA\-1 algorithm
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

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal, self).__init__()

                                self.yang_name = "crypto-algorithm-val"
                                self.yang_parent_name = "authentication"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('hmac_sha1_12', YLeaf(YType.empty, 'hmac-sha1-12')),
                                    ('hmac_sha1_20', YLeaf(YType.empty, 'hmac-sha1-20')),
                                    ('md5', YLeaf(YType.empty, 'md5')),
                                    ('sha_1', YLeaf(YType.empty, 'sha-1')),
                                    ('hmac_sha_1', YLeaf(YType.empty, 'hmac-sha-1')),
                                    ('hmac_sha_256', YLeaf(YType.empty, 'hmac-sha-256')),
                                    ('hmac_sha_384', YLeaf(YType.empty, 'hmac-sha-384')),
                                    ('hmac_sha_512', YLeaf(YType.empty, 'hmac-sha-512')),
                                ])
                                self.hmac_sha1_12 = None
                                self.hmac_sha1_20 = None
                                self.md5 = None
                                self.sha_1 = None
                                self.hmac_sha_1 = None
                                self.hmac_sha_256 = None
                                self.hmac_sha_384 = None
                                self.hmac_sha_512 = None
                                self._segment_path = lambda: "crypto-algorithm-val"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal, ['hmac_sha1_12', 'hmac_sha1_20', 'md5', 'sha_1', 'hmac_sha_1', 'hmac_sha_256', 'hmac_sha_384', 'hmac_sha_512'], name, value)


                    class OspfNeighbor(Entity):
                        """
                        List of OSPF neighbors
                        
                        .. attribute:: neighbor_id  (key)
                        
                        	OSPF neighbor ID
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address
                        
                        	Neighbor address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: dr
                        
                        	Designated Router
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: bdr
                        
                        	Backup Designated Router
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: state
                        
                        	OSPF neighbor state
                        	**type**\:  :py:class:`NbrStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.NbrStateType>`
                        
                        .. attribute:: stats
                        
                        	Per\-neighbor statistics
                        	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor, self).__init__()

                            self.yang_name = "ospf-neighbor"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['neighbor_id']
                            self._child_container_classes = OrderedDict([("stats", ("stats", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('neighbor_id', YLeaf(YType.str, 'neighbor-id')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('dr', YLeaf(YType.str, 'dr')),
                                ('bdr', YLeaf(YType.str, 'bdr')),
                                ('state', YLeaf(YType.enumeration, 'state')),
                            ])
                            self.neighbor_id = None
                            self.address = None
                            self.dr = None
                            self.bdr = None
                            self.state = None

                            self.stats = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                            self._children_yang_names.add("stats")
                            self._segment_path = lambda: "ospf-neighbor" + "[neighbor-id='" + str(self.neighbor_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor, ['neighbor_id', 'address', 'dr', 'bdr', 'state'], name, value)


                        class Stats(Entity):
                            """
                            Per\-neighbor statistics
                            
                            .. attribute:: nbr_event_count
                            
                            	The number of time this neighbor has changed state or an error has occurred
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nbr_retrans_qlen
                            
                            	The current length of the retransmission queue
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats, self).__init__()

                                self.yang_name = "stats"
                                self.yang_parent_name = "ospf-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('nbr_event_count', YLeaf(YType.uint32, 'nbr-event-count')),
                                    ('nbr_retrans_qlen', YLeaf(YType.uint32, 'nbr-retrans-qlen')),
                                ])
                                self.nbr_event_count = None
                                self.nbr_retrans_qlen = None
                                self._segment_path = lambda: "stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats, ['nbr_event_count', 'nbr_retrans_qlen'], name, value)


                    class IntfLinkScopeLsas(Entity):
                        """
                        List OSPF link scope LSAs
                        
                        .. attribute:: lsa_type  (key)
                        
                        	OSPF link scope LSA type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: link_scope_lsa
                        
                        	List of OSPF link scope LSAs
                        	**type**\: list of  		 :py:class:`LinkScopeLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa>`
                        
                        .. attribute:: area_scope_lsa
                        
                        	List OSPF area scope LSA databases
                        	**type**\: list of  		 :py:class:`AreaScopeLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas, self).__init__()

                            self.yang_name = "intf-link-scope-lsas"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['lsa_type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("link-scope-lsa", ("link_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa)), ("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa))])
                            self._leafs = OrderedDict([
                                ('lsa_type', YLeaf(YType.uint32, 'lsa-type')),
                            ])
                            self.lsa_type = None

                            self.link_scope_lsa = YList(self)
                            self.area_scope_lsa = YList(self)
                            self._segment_path = lambda: "intf-link-scope-lsas" + "[lsa-type='" + str(self.lsa_type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas, ['lsa_type'], name, value)


                        class LinkScopeLsa(Entity):
                            """
                            List of OSPF link scope LSAs
                            
                            .. attribute:: lsa_id  (key)
                            
                            	LSA ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adv_router  (key)
                            
                            	Advertising router
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: decoded_completed
                            
                            	The OSPF LSA body is fully decoded
                            	**type**\: bool
                            
                            .. attribute:: raw_data
                            
                            	The complete LSA in network byte order as received/sent over the wire
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            .. attribute:: version
                            
                            	Version
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ospfv2_lsa
                            
                            	OSPFv2 LSA
                            	**type**\:  :py:class:`Ospfv2Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa>`
                            
                            .. attribute:: ospfv2_link
                            
                            	OSPFv2 LSA link
                            	**type**\: list of  		 :py:class:`Ospfv2Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link>`
                            
                            .. attribute:: ospfv2_topology
                            
                            	Summary LSA
                            	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Topology>`
                            
                            .. attribute:: ospfv2_external
                            
                            	External LSA
                            	**type**\: list of  		 :py:class:`Ospfv2External <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2External>`
                            
                            .. attribute:: ospfv2_unknown_tlv
                            
                            	OSPFv2 Unknown TLV
                            	**type**\: list of  		 :py:class:`Ospfv2UnknownTlv <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv>`
                            
                            .. attribute:: ospfv3_lsa_val
                            
                            	OSPFv3 LSA
                            	**type**\:  :py:class:`Ospfv3LsaVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal>`
                            
                            .. attribute:: ospfv3_link
                            
                            	OSPFv3 links
                            	**type**\: list of  		 :py:class:`Ospfv3Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3Link>`
                            
                            .. attribute:: ospfv3_prefix_list
                            
                            	OSPFv3 prefix\-list
                            	**type**\: list of  		 :py:class:`Ospfv3PrefixList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList>`
                            
                            .. attribute:: ospfv3_ia_prefix
                            
                            	OSPFv3 intra\-area prefix\-list
                            	**type**\: list of  		 :py:class:`Ospfv3IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix>`
                            
                            .. attribute:: multi_topology
                            
                            	OSPF multi\-topology interface augmentation
                            	**type**\: list of  		 :py:class:`MultiTopology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.MultiTopology>`
                            
                            .. attribute:: router_address
                            
                            	Router address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tlv
                            
                            	Link TLV
                            	**type**\:  :py:class:`Tlv <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv>`
                            
                            .. attribute:: unknown_sub_tlv
                            
                            	OSPFv2 Unknown sub TLV
                            	**type**\: list of  		 :py:class:`UnknownSubTlv <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.UnknownSubTlv>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa, self).__init__()

                                self.yang_name = "link-scope-lsa"
                                self.yang_parent_name = "intf-link-scope-lsas"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['lsa_id','adv_router']
                                self._child_container_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa)), ("ospfv3-lsa-val", ("ospfv3_lsa_val", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal)), ("tlv", ("tlv", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv))])
                                self._child_list_classes = OrderedDict([("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2External)), ("ospfv2-unknown-tlv", ("ospfv2_unknown_tlv", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3Link)), ("ospfv3-prefix-list", ("ospfv3_prefix_list", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix)), ("multi-topology", ("multi_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.MultiTopology)), ("unknown-sub-tlv", ("unknown_sub_tlv", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.UnknownSubTlv))])
                                self._leafs = OrderedDict([
                                    ('lsa_id', YLeaf(YType.uint32, 'lsa-id')),
                                    ('adv_router', YLeaf(YType.str, 'adv-router')),
                                    ('decoded_completed', YLeaf(YType.boolean, 'decoded-completed')),
                                    ('raw_data', YLeafList(YType.uint8, 'raw-data')),
                                    ('version', YLeaf(YType.uint32, 'version')),
                                    ('router_address', YLeaf(YType.str, 'router-address')),
                                ])
                                self.lsa_id = None
                                self.adv_router = None
                                self.decoded_completed = None
                                self.raw_data = []
                                self.version = None
                                self.router_address = None

                                self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa()
                                self.ospfv2_lsa.parent = self
                                self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"
                                self._children_yang_names.add("ospfv2-lsa")

                                self.ospfv3_lsa_val = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal()
                                self.ospfv3_lsa_val.parent = self
                                self._children_name_map["ospfv3_lsa_val"] = "ospfv3-lsa-val"
                                self._children_yang_names.add("ospfv3-lsa-val")

                                self.tlv = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv()
                                self.tlv.parent = self
                                self._children_name_map["tlv"] = "tlv"
                                self._children_yang_names.add("tlv")

                                self.ospfv2_link = YList(self)
                                self.ospfv2_topology = YList(self)
                                self.ospfv2_external = YList(self)
                                self.ospfv2_unknown_tlv = YList(self)
                                self.ospfv3_link = YList(self)
                                self.ospfv3_prefix_list = YList(self)
                                self.ospfv3_ia_prefix = YList(self)
                                self.multi_topology = YList(self)
                                self.unknown_sub_tlv = YList(self)
                                self._segment_path = lambda: "link-scope-lsa" + "[lsa-id='" + str(self.lsa_id) + "']" + "[adv-router='" + str(self.adv_router) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data', 'version', 'router_address'], name, value)


                            class Ospfv2Lsa(Entity):
                                """
                                OSPFv2 LSA
                                
                                .. attribute:: header
                                
                                	Decoded OSPFv2 LSA header data
                                	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header>`
                                
                                .. attribute:: lsa_body
                                
                                	Decoded OSPFv2 LSA body data
                                	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa, self).__init__()

                                    self.yang_name = "ospfv2-lsa"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"
                                    self._children_yang_names.add("header")

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._children_yang_names.add("lsa-body")
                                    self._segment_path = lambda: "ospfv2-lsa"


                                class Header(Entity):
                                    """
                                    Decoded OSPFv2 LSA header data
                                    
                                    .. attribute:: lsa_id
                                    
                                    	LSA ID
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: opaque_type
                                    
                                    	Opaque type
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: opaque_id
                                    
                                    	Opaque ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: age
                                    
                                    	LSA age
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: type
                                    
                                    	LSA type
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: adv_router
                                    
                                    	LSA advertising router
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: seq_num
                                    
                                    	LSA sequence number
                                    	**type**\: str
                                    
                                    .. attribute:: checksum
                                    
                                    	LSA checksum
                                    	**type**\: str
                                    
                                    .. attribute:: length
                                    
                                    	LSA length
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: flag_options
                                    
                                    	LSA options
                                    	**type**\:  :py:class:`LsaFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.LsaFlagOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                            ('opaque_type', YLeaf(YType.uint8, 'opaque-type')),
                                            ('opaque_id', YLeaf(YType.uint32, 'opaque-id')),
                                            ('age', YLeaf(YType.uint16, 'age')),
                                            ('type', YLeaf(YType.uint16, 'type')),
                                            ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                            ('seq_num', YLeaf(YType.str, 'seq-num')),
                                            ('checksum', YLeaf(YType.str, 'checksum')),
                                            ('length', YLeaf(YType.uint16, 'length')),
                                            ('flag_options', YLeaf(YType.bits, 'flag-options')),
                                        ])
                                        self.lsa_id = None
                                        self.opaque_type = None
                                        self.opaque_id = None
                                        self.age = None
                                        self.type = None
                                        self.adv_router = None
                                        self.seq_num = None
                                        self.checksum = None
                                        self.length = None
                                        self.flag_options = Bits()
                                        self._segment_path = lambda: "header"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header, ['lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'flag_options'], name, value)


                                class LsaBody(Entity):
                                    """
                                    Decoded OSPFv2 LSA body data
                                    
                                    .. attribute:: num_of_links
                                    
                                    	Number of links
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: network
                                    
                                    	Network details
                                    	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network>`
                                    
                                    .. attribute:: summary_mask
                                    
                                    	Summary mask
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: external_mask
                                    
                                    	External mask
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: body_flag_options
                                    
                                    	LSA body flags
                                    	**type**\:  :py:class:`Ospfv2LsaBodyFlagsOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2LsaBodyFlagsOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_of_links', YLeaf(YType.uint16, 'num-of-links')),
                                            ('summary_mask', YLeaf(YType.str, 'summary-mask')),
                                            ('external_mask', YLeaf(YType.str, 'external-mask')),
                                            ('body_flag_options', YLeaf(YType.bits, 'body-flag-options')),
                                        ])
                                        self.num_of_links = None
                                        self.summary_mask = None
                                        self.external_mask = None
                                        self.body_flag_options = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"
                                        self._children_yang_names.add("network")
                                        self._segment_path = lambda: "lsa-body"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody, ['num_of_links', 'summary_mask', 'external_mask', 'body_flag_options'], name, value)


                                    class Network(Entity):
                                        """
                                        Network details
                                        
                                        .. attribute:: network_mask
                                        
                                        	IP network mask
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: attached_router
                                        
                                        	List of the routers attached to the network
                                        	**type**\: list of int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('network_mask', YLeaf(YType.str, 'network-mask')),
                                                ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                            ])
                                            self.network_mask = None
                                            self.attached_router = []
                                            self._segment_path = lambda: "network"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network, ['network_mask', 'attached_router'], name, value)


                            class Ospfv2Link(Entity):
                                """
                                OSPFv2 LSA link
                                
                                .. attribute:: link_id  (key)
                                
                                	Link ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: link_data  (key)
                                
                                	Link data
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: type
                                
                                	Link type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: ospfv2_topology
                                
                                	Topology specific information
                                	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link, self).__init__()

                                    self.yang_name = "ospfv2-link"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['link_id','link_data']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology))])
                                    self._leafs = OrderedDict([
                                        ('link_id', YLeaf(YType.uint32, 'link-id')),
                                        ('link_data', YLeaf(YType.uint32, 'link-data')),
                                        ('type', YLeaf(YType.uint8, 'type')),
                                    ])
                                    self.link_id = None
                                    self.link_data = None
                                    self.type = None

                                    self.ospfv2_topology = YList(self)
                                    self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link, ['link_id', 'link_data', 'type'], name, value)


                                class Ospfv2Topology(Entity):
                                    """
                                    Topology specific information
                                    
                                    .. attribute:: mt_id  (key)
                                    
                                    	MT\-ID for topology enabled link
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for the topology
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                        self.yang_name = "ospfv2-topology"
                                        self.yang_parent_name = "ospfv2-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['mt_id']
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                            ('metric', YLeaf(YType.uint16, 'metric')),
                                        ])
                                        self.mt_id = None
                                        self.metric = None
                                        self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                            class Ospfv2Topology(Entity):
                                """
                                Summary LSA
                                
                                .. attribute:: mt_id  (key)
                                
                                	MT\-ID for topology enabled link
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric
                                
                                	Metric for the topology
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Topology, self).__init__()

                                    self.yang_name = "ospfv2-topology"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                        ('metric', YLeaf(YType.uint16, 'metric')),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                            class Ospfv2External(Entity):
                                """
                                External LSA
                                
                                .. attribute:: mt_id  (key)
                                
                                	MT\-ID for topology enabled on the link
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric
                                
                                	Metric for the topology
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: forwarding_address
                                
                                	Forwarding address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: external_route_tag
                                
                                	Route tag
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2External, self).__init__()

                                    self.yang_name = "ospfv2-external"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                        ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self.forwarding_address = None
                                    self.external_route_tag = None
                                    self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2External, ['mt_id', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                            class Ospfv2UnknownTlv(Entity):
                                """
                                OSPFv2 Unknown TLV
                                
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
                                	**type**\: list of int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv, self).__init__()

                                    self.yang_name = "ospfv2-unknown-tlv"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['type']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.uint16, 'type')),
                                        ('length', YLeaf(YType.uint16, 'length')),
                                        ('value', YLeafList(YType.uint8, 'value')),
                                    ])
                                    self.type = None
                                    self.length = None
                                    self.value = []
                                    self._segment_path = lambda: "ospfv2-unknown-tlv" + "[type='" + str(self.type) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv, ['type', 'length', 'value'], name, value)


                            class Ospfv3LsaVal(Entity):
                                """
                                OSPFv3 LSA
                                
                                .. attribute:: header
                                
                                	Decoded OSPFv3 LSA header
                                	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header>`
                                
                                .. attribute:: lsa_body
                                
                                	Decoded OSPFv3 LSA body
                                	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal, self).__init__()

                                    self.yang_name = "ospfv3-lsa-val"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"
                                    self._children_yang_names.add("header")

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._children_yang_names.add("lsa-body")
                                    self._segment_path = lambda: "ospfv3-lsa-val"


                                class Header(Entity):
                                    """
                                    Decoded OSPFv3 LSA header
                                    
                                    .. attribute:: lsa_id
                                    
                                    	LSA ID
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: lsa_header
                                    
                                    	LSA header
                                    	**type**\:  :py:class:`LsaHeader <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader>`
                                    
                                    .. attribute:: lsa_hdr_options
                                    
                                    	OSPFv3 LSA options
                                    	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv3-lsa-val"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                            ('lsa_hdr_options', YLeaf(YType.bits, 'lsa-hdr-options')),
                                        ])
                                        self.lsa_id = None
                                        self.lsa_hdr_options = Bits()

                                        self.lsa_header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader()
                                        self.lsa_header.parent = self
                                        self._children_name_map["lsa_header"] = "lsa-header"
                                        self._children_yang_names.add("lsa-header")
                                        self._segment_path = lambda: "header"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header, ['lsa_id', 'lsa_hdr_options'], name, value)


                                    class LsaHeader(Entity):
                                        """
                                        LSA header
                                        
                                        .. attribute:: age
                                        
                                        	LSA age
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: type
                                        
                                        	LSA type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: adv_router
                                        
                                        	LSA advertising router
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: seq_num
                                        
                                        	LSA sequence number
                                        	**type**\: str
                                        
                                        .. attribute:: checksum
                                        
                                        	LSA checksum
                                        	**type**\: str
                                        
                                        .. attribute:: length
                                        
                                        	LSA length
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader, self).__init__()

                                            self.yang_name = "lsa-header"
                                            self.yang_parent_name = "header"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('age', YLeaf(YType.uint16, 'age')),
                                                ('type', YLeaf(YType.uint16, 'type')),
                                                ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                                ('seq_num', YLeaf(YType.str, 'seq-num')),
                                                ('checksum', YLeaf(YType.str, 'checksum')),
                                                ('length', YLeaf(YType.uint16, 'length')),
                                            ])
                                            self.age = None
                                            self.type = None
                                            self.adv_router = None
                                            self.seq_num = None
                                            self.checksum = None
                                            self.length = None
                                            self._segment_path = lambda: "lsa-header"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader, ['age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                                class LsaBody(Entity):
                                    """
                                    Decoded OSPFv3 LSA body
                                    
                                    .. attribute:: network
                                    
                                    	OSPFv3 network
                                    	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network>`
                                    
                                    .. attribute:: prefix
                                    
                                    	OSPFv3 inter area prefix
                                    	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix>`
                                    
                                    .. attribute:: ia_router
                                    
                                    	OSPFv3 inter area router
                                    	**type**\:  :py:class:`IaRouter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter>`
                                    
                                    .. attribute:: lsa_external
                                    
                                    	OSPFv3 LSA external
                                    	**type**\:  :py:class:`LsaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal>`
                                    
                                    .. attribute:: nssa
                                    
                                    	OSPFv3 NSSA
                                    	**type**\:  :py:class:`Nssa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa>`
                                    
                                    .. attribute:: link_data
                                    
                                    	OSPFv3 Link data
                                    	**type**\:  :py:class:`LinkData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData>`
                                    
                                    .. attribute:: ia_prefix
                                    
                                    	OSPFv3 Intra area prefixes
                                    	**type**\:  :py:class:`IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix>`
                                    
                                    .. attribute:: lsa_flag_options
                                    
                                    	LSA options
                                    	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                    
                                    .. attribute:: lsa_body_flags
                                    
                                    	LSA Body Flags
                                    	**type**\:  :py:class:`Ospfv3LsaBodyFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaBodyFlagOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv3-lsa-val"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_flag_options', YLeaf(YType.bits, 'lsa-flag-options')),
                                            ('lsa_body_flags', YLeaf(YType.bits, 'lsa-body-flags')),
                                        ])
                                        self.lsa_flag_options = Bits()
                                        self.lsa_body_flags = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"
                                        self._children_yang_names.add("network")

                                        self.prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix()
                                        self.prefix.parent = self
                                        self._children_name_map["prefix"] = "prefix"
                                        self._children_yang_names.add("prefix")

                                        self.ia_router = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter()
                                        self.ia_router.parent = self
                                        self._children_name_map["ia_router"] = "ia-router"
                                        self._children_yang_names.add("ia-router")

                                        self.lsa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal()
                                        self.lsa_external.parent = self
                                        self._children_name_map["lsa_external"] = "lsa-external"
                                        self._children_yang_names.add("lsa-external")

                                        self.nssa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa()
                                        self.nssa.parent = self
                                        self._children_name_map["nssa"] = "nssa"
                                        self._children_yang_names.add("nssa")

                                        self.link_data = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData()
                                        self.link_data.parent = self
                                        self._children_name_map["link_data"] = "link-data"
                                        self._children_yang_names.add("link-data")

                                        self.ia_prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix()
                                        self.ia_prefix.parent = self
                                        self._children_name_map["ia_prefix"] = "ia-prefix"
                                        self._children_yang_names.add("ia-prefix")
                                        self._segment_path = lambda: "lsa-body"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody, ['lsa_flag_options', 'lsa_body_flags'], name, value)


                                    class Network(Entity):
                                        """
                                        OSPFv3 network
                                        
                                        .. attribute:: attached_router
                                        
                                        	List of the routers attached to the network
                                        	**type**\: list of int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lsa_net_options
                                        
                                        	Network LSA options
                                        	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                                ('lsa_net_options', YLeaf(YType.bits, 'lsa-net-options')),
                                            ])
                                            self.attached_router = []
                                            self.lsa_net_options = Bits()
                                            self._segment_path = lambda: "network"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network, ['attached_router', 'lsa_net_options'], name, value)


                                    class Prefix(Entity):
                                        """
                                        OSPFv3 inter area prefix
                                        
                                        .. attribute:: metric
                                        
                                        	Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ia_prefix
                                        
                                        	Inter area Prefix
                                        	**type**\: str
                                        
                                        .. attribute:: ia_prefix_options
                                        
                                        	Inter area prefix options
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix, self).__init__()

                                            self.yang_name = "prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', YLeaf(YType.uint32, 'metric')),
                                                ('ia_prefix', YLeaf(YType.str, 'ia-prefix')),
                                                ('ia_prefix_options', YLeaf(YType.str, 'ia-prefix-options')),
                                            ])
                                            self.metric = None
                                            self.ia_prefix = None
                                            self.ia_prefix_options = None
                                            self._segment_path = lambda: "prefix"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix, ['metric', 'ia_prefix', 'ia_prefix_options'], name, value)


                                    class IaRouter(Entity):
                                        """
                                        OSPFv3 inter area router
                                        
                                        .. attribute:: metric
                                        
                                        	Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: destination_router_id
                                        
                                        	Router ID of the router being described by the LSA
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lsa_ia_options
                                        
                                        	Inter area LSA options
                                        	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter, self).__init__()

                                            self.yang_name = "ia-router"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', YLeaf(YType.uint32, 'metric')),
                                                ('destination_router_id', YLeaf(YType.uint32, 'destination-router-id')),
                                                ('lsa_ia_options', YLeaf(YType.bits, 'lsa-ia-options')),
                                            ])
                                            self.metric = None
                                            self.destination_router_id = None
                                            self.lsa_ia_options = Bits()
                                            self._segment_path = lambda: "ia-router"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter, ['metric', 'destination_router_id', 'lsa_ia_options'], name, value)


                                    class LsaExternal(Entity):
                                        """
                                        OSPFv3 LSA external
                                        
                                        .. attribute:: metric
                                        
                                        	Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: flags
                                        
                                        	LSA Flags
                                        	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags>`
                                        
                                        .. attribute:: referenced_ls_type
                                        
                                        	Referenced Link State type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: external_prefix
                                        
                                        	Prefix
                                        	**type**\: str
                                        
                                        .. attribute:: external_prefix_options
                                        
                                        	Prefix options
                                        	**type**\: str
                                        
                                        .. attribute:: forwarding_address
                                        
                                        	Forwarding address
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
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

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal, self).__init__()

                                            self.yang_name = "lsa-external"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', YLeaf(YType.uint32, 'metric')),
                                                ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                                ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                                ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                                ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                                ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                                ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                            ])
                                            self.metric = None
                                            self.referenced_ls_type = None
                                            self.external_prefix = None
                                            self.external_prefix_options = None
                                            self.forwarding_address = None
                                            self.external_route_tag = None
                                            self.referenced_link_state_id = None

                                            self.flags = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags()
                                            self.flags.parent = self
                                            self._children_name_map["flags"] = "flags"
                                            self._children_yang_names.add("flags")
                                            self._segment_path = lambda: "lsa-external"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                        class Flags(Entity):
                                            """
                                            LSA Flags
                                            
                                            .. attribute:: e_flag
                                            
                                            	When set, the metric specified is a Type 2 external metric
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ospf-ios-xe-oper'
                                            _revision = '2017-10-10'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags, self).__init__()

                                                self.yang_name = "flags"
                                                self.yang_parent_name = "lsa-external"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                                ])
                                                self.e_flag = None
                                                self._segment_path = lambda: "flags"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags, ['e_flag'], name, value)


                                    class Nssa(Entity):
                                        """
                                        OSPFv3 NSSA
                                        
                                        .. attribute:: lsa_nssa_external
                                        
                                        	NSSA LSA
                                        	**type**\:  :py:class:`LsaNssaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa, self).__init__()

                                            self.yang_name = "nssa"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal()
                                            self.lsa_nssa_external.parent = self
                                            self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                            self._children_yang_names.add("lsa-nssa-external")
                                            self._segment_path = lambda: "nssa"


                                        class LsaNssaExternal(Entity):
                                            """
                                            NSSA LSA
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: flags
                                            
                                            	LSA Flags
                                            	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags>`
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: external_prefix
                                            
                                            	Prefix
                                            	**type**\: str
                                            
                                            .. attribute:: external_prefix_options
                                            
                                            	Prefix options
                                            	**type**\: str
                                            
                                            .. attribute:: forwarding_address
                                            
                                            	Forwarding address
                                            	**type**\: union of the below types:
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
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

                                            _prefix = 'ospf-ios-xe-oper'
                                            _revision = '2017-10-10'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                                self.yang_name = "lsa-nssa-external"
                                                self.yang_parent_name = "nssa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('metric', YLeaf(YType.uint32, 'metric')),
                                                    ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                                    ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                                    ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                                    ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                                    ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                                    ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                                ])
                                                self.metric = None
                                                self.referenced_ls_type = None
                                                self.external_prefix = None
                                                self.external_prefix_options = None
                                                self.forwarding_address = None
                                                self.external_route_tag = None
                                                self.referenced_link_state_id = None

                                                self.flags = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags()
                                                self.flags.parent = self
                                                self._children_name_map["flags"] = "flags"
                                                self._children_yang_names.add("flags")
                                                self._segment_path = lambda: "lsa-nssa-external"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                            class Flags(Entity):
                                                """
                                                LSA Flags
                                                
                                                .. attribute:: e_flag
                                                
                                                	When set, the metric specified is a Type 2 external metric
                                                	**type**\: bool
                                                
                                                

                                                """

                                                _prefix = 'ospf-ios-xe-oper'
                                                _revision = '2017-10-10'

                                                def __init__(self):
                                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                                    self.yang_name = "flags"
                                                    self.yang_parent_name = "lsa-nssa-external"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                                    ])
                                                    self.e_flag = None
                                                    self._segment_path = lambda: "flags"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags, ['e_flag'], name, value)


                                    class LinkData(Entity):
                                        """
                                        OSPFv3 Link data
                                        
                                        .. attribute:: rtr_priority
                                        
                                        	Router priority of the interce
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
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
                                        
                                        .. attribute:: lsa_id_options
                                        
                                        	Link data LSA options
                                        	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData, self).__init__()

                                            self.yang_name = "link-data"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rtr_priority', YLeaf(YType.uint8, 'rtr-priority')),
                                                ('link_local_interface_address', YLeaf(YType.str, 'link-local-interface-address')),
                                                ('num_of_prefixes', YLeaf(YType.uint32, 'num-of-prefixes')),
                                                ('lsa_id_options', YLeaf(YType.bits, 'lsa-id-options')),
                                            ])
                                            self.rtr_priority = None
                                            self.link_local_interface_address = None
                                            self.num_of_prefixes = None
                                            self.lsa_id_options = Bits()
                                            self._segment_path = lambda: "link-data"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData, ['rtr_priority', 'link_local_interface_address', 'num_of_prefixes', 'lsa_id_options'], name, value)


                                    class IaPrefix(Entity):
                                        """
                                        OSPFv3 Intra area prefixes
                                        
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
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: num_of_prefixes
                                        
                                        	Number of prefixes
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix, self).__init__()

                                            self.yang_name = "ia-prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                                ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                                ('referenced_adv_router', YLeaf(YType.str, 'referenced-adv-router')),
                                                ('num_of_prefixes', YLeaf(YType.uint16, 'num-of-prefixes')),
                                            ])
                                            self.referenced_ls_type = None
                                            self.referenced_link_state_id = None
                                            self.referenced_adv_router = None
                                            self.num_of_prefixes = None
                                            self._segment_path = lambda: "ia-prefix"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                            class Ospfv3Link(Entity):
                                """
                                OSPFv3 links
                                
                                .. attribute:: interface_id  (key)
                                
                                	Interface ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: neighbor_interface_id  (key)
                                
                                	Neighbor interface ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: neighbor_router_id  (key)
                                
                                	Neighbor router ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: type
                                
                                	Link type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3Link, self).__init__()

                                    self.yang_name = "ospfv3-link"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_id', YLeaf(YType.uint32, 'interface-id')),
                                        ('neighbor_interface_id', YLeaf(YType.uint32, 'neighbor-interface-id')),
                                        ('neighbor_router_id', YLeaf(YType.uint32, 'neighbor-router-id')),
                                        ('type', YLeaf(YType.uint8, 'type')),
                                        ('metric', YLeaf(YType.uint16, 'metric')),
                                    ])
                                    self.interface_id = None
                                    self.neighbor_interface_id = None
                                    self.neighbor_router_id = None
                                    self.type = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                            class Ospfv3PrefixList(Entity):
                                """
                                OSPFv3 prefix\-list
                                
                                .. attribute:: prefix  (key)
                                
                                	Prefix
                                	**type**\: str
                                
                                .. attribute:: prefix_options
                                
                                	Prefix options
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList, self).__init__()

                                    self.yang_name = "ospfv3-prefix-list"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['prefix']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix', YLeaf(YType.str, 'prefix')),
                                        ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                                    ])
                                    self.prefix = None
                                    self.prefix_options = None
                                    self._segment_path = lambda: "ospfv3-prefix-list" + "[prefix='" + str(self.prefix) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList, ['prefix', 'prefix_options'], name, value)


                            class Ospfv3IaPrefix(Entity):
                                """
                                OSPFv3 intra\-area prefix\-list
                                
                                .. attribute:: prefix  (key)
                                
                                	Prefix
                                	**type**\: str
                                
                                .. attribute:: prefix_options
                                
                                	Prefix options
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix, self).__init__()

                                    self.yang_name = "ospfv3-ia-prefix"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['prefix']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix', YLeaf(YType.str, 'prefix')),
                                        ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                                    ])
                                    self.prefix = None
                                    self.prefix_options = None
                                    self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix, ['prefix', 'prefix_options'], name, value)


                            class MultiTopology(Entity):
                                """
                                OSPF multi\-topology interface augmentation
                                
                                .. attribute:: name  (key)
                                
                                	One of the topology enabled on this interface
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.MultiTopology, self).__init__()

                                    self.yang_name = "multi-topology"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', YLeaf(YType.str, 'name')),
                                    ])
                                    self.name = None
                                    self._segment_path = lambda: "multi-topology" + "[name='" + str(self.name) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.MultiTopology, ['name'], name, value)


                            class Tlv(Entity):
                                """
                                Link TLV
                                
                                .. attribute:: link_type
                                
                                	Link type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: link_id
                                
                                	Link ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: local_if_ipv4_addr
                                
                                	List of local interface IPv4 addresses
                                	**type**\: union of the below types:
                                
                                		**type**\: list of str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: list of str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: local_remote_ipv4_addr
                                
                                	List of remote interface IPv4 addresses
                                	**type**\: union of the below types:
                                
                                		**type**\: list of str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: list of str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
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
                                
                                	Unrseerved bandwidth
                                	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                                
                                	**range:** \-92233720368547758.08..92233720368547758.07
                                
                                .. attribute:: admin_group
                                
                                	Administrative group/Resource class/Color
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv, self).__init__()

                                    self.yang_name = "tlv"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('link_type', YLeaf(YType.uint8, 'link-type')),
                                        ('link_id', YLeaf(YType.uint32, 'link-id')),
                                        ('local_if_ipv4_addr', YLeafList(YType.str, 'local-if-ipv4-addr')),
                                        ('local_remote_ipv4_addr', YLeafList(YType.str, 'local-remote-ipv4-addr')),
                                        ('te_metric', YLeaf(YType.uint32, 'te-metric')),
                                        ('max_bandwidth', YLeaf(YType.str, 'max-bandwidth')),
                                        ('max_reservable_bandwidth', YLeaf(YType.str, 'max-reservable-bandwidth')),
                                        ('unreserved_bandwidth', YLeaf(YType.str, 'unreserved-bandwidth')),
                                        ('admin_group', YLeaf(YType.uint32, 'admin-group')),
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
                                    self._segment_path = lambda: "tlv"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv, ['link_type', 'link_id', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'te_metric', 'max_bandwidth', 'max_reservable_bandwidth', 'unreserved_bandwidth', 'admin_group'], name, value)


                            class UnknownSubTlv(Entity):
                                """
                                OSPFv2 Unknown sub TLV
                                
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
                                	**type**\: list of int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.UnknownSubTlv, self).__init__()

                                    self.yang_name = "unknown-sub-tlv"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['type']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', YLeaf(YType.uint16, 'type')),
                                        ('length', YLeaf(YType.uint16, 'length')),
                                        ('value', YLeafList(YType.uint8, 'value')),
                                    ])
                                    self.type = None
                                    self.length = None
                                    self.value = []
                                    self._segment_path = lambda: "unknown-sub-tlv" + "[type='" + str(self.type) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.UnknownSubTlv, ['type', 'length', 'value'], name, value)


                        class AreaScopeLsa(Entity):
                            """
                            List OSPF area scope LSA databases
                            
                            .. attribute:: lsa_type  (key)
                            
                            	LSA Type
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: adv_router  (key)
                            
                            	Advertising router
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: decoded_completed
                            
                            	The OSPF LSA body is fully decoded
                            	**type**\: bool
                            
                            .. attribute:: raw_data
                            
                            	The complete LSA in network byte order as received/sent over the wire
                            	**type**\: list of int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ospfv2_lsa
                            
                            	OSPFv2 LSA
                            	**type**\:  :py:class:`Ospfv2Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa>`
                            
                            .. attribute:: ospfv2_link
                            
                            	Router LSA link
                            	**type**\: list of  		 :py:class:`Ospfv2Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link>`
                            
                            .. attribute:: ospfv2_topology
                            
                            	Summary LSA
                            	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Topology>`
                            
                            .. attribute:: ospfv2_external
                            
                            	External LSA
                            	**type**\: list of  		 :py:class:`Ospfv2External <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2External>`
                            
                            .. attribute:: ospfv3_lsa
                            
                            	OSPFv3 LSA
                            	**type**\:  :py:class:`Ospfv3Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa>`
                            
                            .. attribute:: ospfv3_link
                            
                            	OSPFv3 links
                            	**type**\: list of  		 :py:class:`Ospfv3Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Link>`
                            
                            .. attribute:: ospfv3_prefix
                            
                            	OSPFv3 prefix\-list
                            	**type**\: list of  		 :py:class:`Ospfv3Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Prefix>`
                            
                            .. attribute:: ospfv3_ia_prefix
                            
                            	OSPFv3 intra\-area prefix\-list
                            	**type**\: list of  		 :py:class:`Ospfv3IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa, self).__init__()

                                self.yang_name = "area-scope-lsa"
                                self.yang_parent_name = "intf-link-scope-lsas"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['lsa_type','adv_router']
                                self._child_container_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa)), ("ospfv3-lsa", ("ospfv3_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa))])
                                self._child_list_classes = OrderedDict([("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2External)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Link)), ("ospfv3-prefix", ("ospfv3_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Prefix)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix))])
                                self._leafs = OrderedDict([
                                    ('lsa_type', YLeaf(YType.uint32, 'lsa-type')),
                                    ('adv_router', YLeaf(YType.str, 'adv-router')),
                                    ('decoded_completed', YLeaf(YType.boolean, 'decoded-completed')),
                                    ('raw_data', YLeafList(YType.uint8, 'raw-data')),
                                ])
                                self.lsa_type = None
                                self.adv_router = None
                                self.decoded_completed = None
                                self.raw_data = []

                                self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa()
                                self.ospfv2_lsa.parent = self
                                self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"
                                self._children_yang_names.add("ospfv2-lsa")

                                self.ospfv3_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa()
                                self.ospfv3_lsa.parent = self
                                self._children_name_map["ospfv3_lsa"] = "ospfv3-lsa"
                                self._children_yang_names.add("ospfv3-lsa")

                                self.ospfv2_link = YList(self)
                                self.ospfv2_topology = YList(self)
                                self.ospfv2_external = YList(self)
                                self.ospfv3_link = YList(self)
                                self.ospfv3_prefix = YList(self)
                                self.ospfv3_ia_prefix = YList(self)
                                self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']" + "[adv-router='" + str(self.adv_router) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa, ['lsa_type', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                            class Ospfv2Lsa(Entity):
                                """
                                OSPFv2 LSA
                                
                                .. attribute:: header
                                
                                	Decoded OSPFv2 LSA header data
                                	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header>`
                                
                                .. attribute:: lsa_body
                                
                                	Decoded OSPFv2 LSA body data
                                	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa, self).__init__()

                                    self.yang_name = "ospfv2-lsa"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"
                                    self._children_yang_names.add("header")

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._children_yang_names.add("lsa-body")
                                    self._segment_path = lambda: "ospfv2-lsa"


                                class Header(Entity):
                                    """
                                    Decoded OSPFv2 LSA header data
                                    
                                    .. attribute:: lsa_id
                                    
                                    	LSA ID
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: opaque_type
                                    
                                    	Opaque type
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: opaque_id
                                    
                                    	Opaque ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: age
                                    
                                    	LSA age
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: type
                                    
                                    	LSA type
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: adv_router
                                    
                                    	LSA advertising router
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: seq_num
                                    
                                    	LSA sequence number
                                    	**type**\: str
                                    
                                    .. attribute:: checksum
                                    
                                    	LSA checksum
                                    	**type**\: str
                                    
                                    .. attribute:: length
                                    
                                    	LSA length
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: flag_options
                                    
                                    	LSA options
                                    	**type**\:  :py:class:`LsaFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.LsaFlagOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                            ('opaque_type', YLeaf(YType.uint8, 'opaque-type')),
                                            ('opaque_id', YLeaf(YType.uint32, 'opaque-id')),
                                            ('age', YLeaf(YType.uint16, 'age')),
                                            ('type', YLeaf(YType.uint16, 'type')),
                                            ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                            ('seq_num', YLeaf(YType.str, 'seq-num')),
                                            ('checksum', YLeaf(YType.str, 'checksum')),
                                            ('length', YLeaf(YType.uint16, 'length')),
                                            ('flag_options', YLeaf(YType.bits, 'flag-options')),
                                        ])
                                        self.lsa_id = None
                                        self.opaque_type = None
                                        self.opaque_id = None
                                        self.age = None
                                        self.type = None
                                        self.adv_router = None
                                        self.seq_num = None
                                        self.checksum = None
                                        self.length = None
                                        self.flag_options = Bits()
                                        self._segment_path = lambda: "header"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header, ['lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'flag_options'], name, value)


                                class LsaBody(Entity):
                                    """
                                    Decoded OSPFv2 LSA body data
                                    
                                    .. attribute:: num_of_links
                                    
                                    	Number of links
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: network
                                    
                                    	Network details
                                    	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network>`
                                    
                                    .. attribute:: summary_mask
                                    
                                    	Summary mask
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: external_mask
                                    
                                    	External mask
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: body_flag_options
                                    
                                    	LSA body flags
                                    	**type**\:  :py:class:`Ospfv2LsaBodyFlagsOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2LsaBodyFlagsOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_of_links', YLeaf(YType.uint16, 'num-of-links')),
                                            ('summary_mask', YLeaf(YType.str, 'summary-mask')),
                                            ('external_mask', YLeaf(YType.str, 'external-mask')),
                                            ('body_flag_options', YLeaf(YType.bits, 'body-flag-options')),
                                        ])
                                        self.num_of_links = None
                                        self.summary_mask = None
                                        self.external_mask = None
                                        self.body_flag_options = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"
                                        self._children_yang_names.add("network")
                                        self._segment_path = lambda: "lsa-body"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody, ['num_of_links', 'summary_mask', 'external_mask', 'body_flag_options'], name, value)


                                    class Network(Entity):
                                        """
                                        Network details
                                        
                                        .. attribute:: network_mask
                                        
                                        	IP network mask
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: attached_router
                                        
                                        	List of the routers attached to the network
                                        	**type**\: list of int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('network_mask', YLeaf(YType.str, 'network-mask')),
                                                ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                            ])
                                            self.network_mask = None
                                            self.attached_router = []
                                            self._segment_path = lambda: "network"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network, ['network_mask', 'attached_router'], name, value)


                            class Ospfv2Link(Entity):
                                """
                                Router LSA link
                                
                                .. attribute:: link_id  (key)
                                
                                	Link ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: link_data  (key)
                                
                                	Link data
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: type
                                
                                	Link type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: ospfv2_topology
                                
                                	Topology specific information
                                	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link, self).__init__()

                                    self.yang_name = "ospfv2-link"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['link_id','link_data']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology))])
                                    self._leafs = OrderedDict([
                                        ('link_id', YLeaf(YType.uint32, 'link-id')),
                                        ('link_data', YLeaf(YType.uint32, 'link-data')),
                                        ('type', YLeaf(YType.uint8, 'type')),
                                    ])
                                    self.link_id = None
                                    self.link_data = None
                                    self.type = None

                                    self.ospfv2_topology = YList(self)
                                    self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link, ['link_id', 'link_data', 'type'], name, value)


                                class Ospfv2Topology(Entity):
                                    """
                                    Topology specific information
                                    
                                    .. attribute:: mt_id  (key)
                                    
                                    	MT\-ID for topology enabled link
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: metric
                                    
                                    	Metric for the topology
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                        self.yang_name = "ospfv2-topology"
                                        self.yang_parent_name = "ospfv2-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['mt_id']
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                            ('metric', YLeaf(YType.uint16, 'metric')),
                                        ])
                                        self.mt_id = None
                                        self.metric = None
                                        self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                            class Ospfv2Topology(Entity):
                                """
                                Summary LSA
                                
                                .. attribute:: mt_id  (key)
                                
                                	MT\-ID for topology enabled link
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric
                                
                                	Metric for the topology
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Topology, self).__init__()

                                    self.yang_name = "ospfv2-topology"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                        ('metric', YLeaf(YType.uint16, 'metric')),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                            class Ospfv2External(Entity):
                                """
                                External LSA
                                
                                .. attribute:: mt_id  (key)
                                
                                	MT\-ID for topology enabled on the link
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric
                                
                                	Metric for the topology
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: forwarding_address
                                
                                	Forwarding address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: external_route_tag
                                
                                	Route tag
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2External, self).__init__()

                                    self.yang_name = "ospfv2-external"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                        ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self.forwarding_address = None
                                    self.external_route_tag = None
                                    self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2External, ['mt_id', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                            class Ospfv3Lsa(Entity):
                                """
                                OSPFv3 LSA
                                
                                .. attribute:: header
                                
                                	Decoded OSPFv3 LSA header
                                	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header>`
                                
                                .. attribute:: lsa_body
                                
                                	Decoded OSPFv3 LSA body
                                	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa, self).__init__()

                                    self.yang_name = "ospfv3-lsa"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"
                                    self._children_yang_names.add("header")

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._children_yang_names.add("lsa-body")
                                    self._segment_path = lambda: "ospfv3-lsa"


                                class Header(Entity):
                                    """
                                    Decoded OSPFv3 LSA header
                                    
                                    .. attribute:: lsa_id
                                    
                                    	LSA ID
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: lsa_header
                                    
                                    	LSA header
                                    	**type**\:  :py:class:`LsaHeader <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader>`
                                    
                                    .. attribute:: lsa_hdr_options
                                    
                                    	OSPFv3 LSA options
                                    	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv3-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                            ('lsa_hdr_options', YLeaf(YType.bits, 'lsa-hdr-options')),
                                        ])
                                        self.lsa_id = None
                                        self.lsa_hdr_options = Bits()

                                        self.lsa_header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader()
                                        self.lsa_header.parent = self
                                        self._children_name_map["lsa_header"] = "lsa-header"
                                        self._children_yang_names.add("lsa-header")
                                        self._segment_path = lambda: "header"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header, ['lsa_id', 'lsa_hdr_options'], name, value)


                                    class LsaHeader(Entity):
                                        """
                                        LSA header
                                        
                                        .. attribute:: age
                                        
                                        	LSA age
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: type
                                        
                                        	LSA type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: adv_router
                                        
                                        	LSA advertising router
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: seq_num
                                        
                                        	LSA sequence number
                                        	**type**\: str
                                        
                                        .. attribute:: checksum
                                        
                                        	LSA checksum
                                        	**type**\: str
                                        
                                        .. attribute:: length
                                        
                                        	LSA length
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader, self).__init__()

                                            self.yang_name = "lsa-header"
                                            self.yang_parent_name = "header"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('age', YLeaf(YType.uint16, 'age')),
                                                ('type', YLeaf(YType.uint16, 'type')),
                                                ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                                ('seq_num', YLeaf(YType.str, 'seq-num')),
                                                ('checksum', YLeaf(YType.str, 'checksum')),
                                                ('length', YLeaf(YType.uint16, 'length')),
                                            ])
                                            self.age = None
                                            self.type = None
                                            self.adv_router = None
                                            self.seq_num = None
                                            self.checksum = None
                                            self.length = None
                                            self._segment_path = lambda: "lsa-header"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader, ['age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                                class LsaBody(Entity):
                                    """
                                    Decoded OSPFv3 LSA body
                                    
                                    .. attribute:: network
                                    
                                    	OSPFv3 network
                                    	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network>`
                                    
                                    .. attribute:: prefix
                                    
                                    	OSPFv3 inter area prefix
                                    	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix>`
                                    
                                    .. attribute:: ia_router
                                    
                                    	OSPFv3 inter area router
                                    	**type**\:  :py:class:`IaRouter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter>`
                                    
                                    .. attribute:: lsa_external
                                    
                                    	OSPFv3 LSA external
                                    	**type**\:  :py:class:`LsaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal>`
                                    
                                    .. attribute:: nssa
                                    
                                    	OSPFv3 NSSA
                                    	**type**\:  :py:class:`Nssa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa>`
                                    
                                    .. attribute:: link_data
                                    
                                    	OSPFv3 Link data
                                    	**type**\:  :py:class:`LinkData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData>`
                                    
                                    .. attribute:: ia_prefix
                                    
                                    	OSPFv3 Intra area prefixes
                                    	**type**\:  :py:class:`IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix>`
                                    
                                    .. attribute:: lsa_flag_options
                                    
                                    	LSA options
                                    	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                    
                                    .. attribute:: lsa_body_flags
                                    
                                    	LSA Body Flags
                                    	**type**\:  :py:class:`Ospfv3LsaBodyFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaBodyFlagOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv3-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_flag_options', YLeaf(YType.bits, 'lsa-flag-options')),
                                            ('lsa_body_flags', YLeaf(YType.bits, 'lsa-body-flags')),
                                        ])
                                        self.lsa_flag_options = Bits()
                                        self.lsa_body_flags = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"
                                        self._children_yang_names.add("network")

                                        self.prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix()
                                        self.prefix.parent = self
                                        self._children_name_map["prefix"] = "prefix"
                                        self._children_yang_names.add("prefix")

                                        self.ia_router = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter()
                                        self.ia_router.parent = self
                                        self._children_name_map["ia_router"] = "ia-router"
                                        self._children_yang_names.add("ia-router")

                                        self.lsa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal()
                                        self.lsa_external.parent = self
                                        self._children_name_map["lsa_external"] = "lsa-external"
                                        self._children_yang_names.add("lsa-external")

                                        self.nssa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa()
                                        self.nssa.parent = self
                                        self._children_name_map["nssa"] = "nssa"
                                        self._children_yang_names.add("nssa")

                                        self.link_data = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData()
                                        self.link_data.parent = self
                                        self._children_name_map["link_data"] = "link-data"
                                        self._children_yang_names.add("link-data")

                                        self.ia_prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix()
                                        self.ia_prefix.parent = self
                                        self._children_name_map["ia_prefix"] = "ia-prefix"
                                        self._children_yang_names.add("ia-prefix")
                                        self._segment_path = lambda: "lsa-body"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody, ['lsa_flag_options', 'lsa_body_flags'], name, value)


                                    class Network(Entity):
                                        """
                                        OSPFv3 network
                                        
                                        .. attribute:: attached_router
                                        
                                        	List of the routers attached to the network
                                        	**type**\: list of int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lsa_net_options
                                        
                                        	Network LSA options
                                        	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                                ('lsa_net_options', YLeaf(YType.bits, 'lsa-net-options')),
                                            ])
                                            self.attached_router = []
                                            self.lsa_net_options = Bits()
                                            self._segment_path = lambda: "network"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network, ['attached_router', 'lsa_net_options'], name, value)


                                    class Prefix(Entity):
                                        """
                                        OSPFv3 inter area prefix
                                        
                                        .. attribute:: metric
                                        
                                        	Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ia_prefix
                                        
                                        	Inter area Prefix
                                        	**type**\: str
                                        
                                        .. attribute:: ia_prefix_options
                                        
                                        	Inter area prefix options
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix, self).__init__()

                                            self.yang_name = "prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', YLeaf(YType.uint32, 'metric')),
                                                ('ia_prefix', YLeaf(YType.str, 'ia-prefix')),
                                                ('ia_prefix_options', YLeaf(YType.str, 'ia-prefix-options')),
                                            ])
                                            self.metric = None
                                            self.ia_prefix = None
                                            self.ia_prefix_options = None
                                            self._segment_path = lambda: "prefix"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix, ['metric', 'ia_prefix', 'ia_prefix_options'], name, value)


                                    class IaRouter(Entity):
                                        """
                                        OSPFv3 inter area router
                                        
                                        .. attribute:: metric
                                        
                                        	Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: destination_router_id
                                        
                                        	Router ID of the router being described by the LSA
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lsa_ia_options
                                        
                                        	Inter area LSA options
                                        	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter, self).__init__()

                                            self.yang_name = "ia-router"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', YLeaf(YType.uint32, 'metric')),
                                                ('destination_router_id', YLeaf(YType.uint32, 'destination-router-id')),
                                                ('lsa_ia_options', YLeaf(YType.bits, 'lsa-ia-options')),
                                            ])
                                            self.metric = None
                                            self.destination_router_id = None
                                            self.lsa_ia_options = Bits()
                                            self._segment_path = lambda: "ia-router"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter, ['metric', 'destination_router_id', 'lsa_ia_options'], name, value)


                                    class LsaExternal(Entity):
                                        """
                                        OSPFv3 LSA external
                                        
                                        .. attribute:: metric
                                        
                                        	Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: flags
                                        
                                        	LSA Flags
                                        	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags>`
                                        
                                        .. attribute:: referenced_ls_type
                                        
                                        	Referenced Link State type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: external_prefix
                                        
                                        	Prefix
                                        	**type**\: str
                                        
                                        .. attribute:: external_prefix_options
                                        
                                        	Prefix options
                                        	**type**\: str
                                        
                                        .. attribute:: forwarding_address
                                        
                                        	Forwarding address
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
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

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal, self).__init__()

                                            self.yang_name = "lsa-external"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', YLeaf(YType.uint32, 'metric')),
                                                ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                                ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                                ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                                ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                                ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                                ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                            ])
                                            self.metric = None
                                            self.referenced_ls_type = None
                                            self.external_prefix = None
                                            self.external_prefix_options = None
                                            self.forwarding_address = None
                                            self.external_route_tag = None
                                            self.referenced_link_state_id = None

                                            self.flags = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags()
                                            self.flags.parent = self
                                            self._children_name_map["flags"] = "flags"
                                            self._children_yang_names.add("flags")
                                            self._segment_path = lambda: "lsa-external"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                        class Flags(Entity):
                                            """
                                            LSA Flags
                                            
                                            .. attribute:: e_flag
                                            
                                            	When set, the metric specified is a Type 2 external metric
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ospf-ios-xe-oper'
                                            _revision = '2017-10-10'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags, self).__init__()

                                                self.yang_name = "flags"
                                                self.yang_parent_name = "lsa-external"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                                ])
                                                self.e_flag = None
                                                self._segment_path = lambda: "flags"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags, ['e_flag'], name, value)


                                    class Nssa(Entity):
                                        """
                                        OSPFv3 NSSA
                                        
                                        .. attribute:: lsa_nssa_external
                                        
                                        	NSSA LSA
                                        	**type**\:  :py:class:`LsaNssaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa, self).__init__()

                                            self.yang_name = "nssa"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict()

                                            self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal()
                                            self.lsa_nssa_external.parent = self
                                            self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                            self._children_yang_names.add("lsa-nssa-external")
                                            self._segment_path = lambda: "nssa"


                                        class LsaNssaExternal(Entity):
                                            """
                                            NSSA LSA
                                            
                                            .. attribute:: metric
                                            
                                            	Metric
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: flags
                                            
                                            	LSA Flags
                                            	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags>`
                                            
                                            .. attribute:: referenced_ls_type
                                            
                                            	Referenced Link State type
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: external_prefix
                                            
                                            	Prefix
                                            	**type**\: str
                                            
                                            .. attribute:: external_prefix_options
                                            
                                            	Prefix options
                                            	**type**\: str
                                            
                                            .. attribute:: forwarding_address
                                            
                                            	Forwarding address
                                            	**type**\: union of the below types:
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
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

                                            _prefix = 'ospf-ios-xe-oper'
                                            _revision = '2017-10-10'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                                self.yang_name = "lsa-nssa-external"
                                                self.yang_parent_name = "nssa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('metric', YLeaf(YType.uint32, 'metric')),
                                                    ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                                    ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                                    ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                                    ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                                    ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                                    ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                                ])
                                                self.metric = None
                                                self.referenced_ls_type = None
                                                self.external_prefix = None
                                                self.external_prefix_options = None
                                                self.forwarding_address = None
                                                self.external_route_tag = None
                                                self.referenced_link_state_id = None

                                                self.flags = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags()
                                                self.flags.parent = self
                                                self._children_name_map["flags"] = "flags"
                                                self._children_yang_names.add("flags")
                                                self._segment_path = lambda: "lsa-nssa-external"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                            class Flags(Entity):
                                                """
                                                LSA Flags
                                                
                                                .. attribute:: e_flag
                                                
                                                	When set, the metric specified is a Type 2 external metric
                                                	**type**\: bool
                                                
                                                

                                                """

                                                _prefix = 'ospf-ios-xe-oper'
                                                _revision = '2017-10-10'

                                                def __init__(self):
                                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                                    self.yang_name = "flags"
                                                    self.yang_parent_name = "lsa-nssa-external"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                                    ])
                                                    self.e_flag = None
                                                    self._segment_path = lambda: "flags"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, ['e_flag'], name, value)


                                    class LinkData(Entity):
                                        """
                                        OSPFv3 Link data
                                        
                                        .. attribute:: rtr_priority
                                        
                                        	Router priority of the interce
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
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
                                        
                                        .. attribute:: lsa_id_options
                                        
                                        	Link data LSA options
                                        	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData, self).__init__()

                                            self.yang_name = "link-data"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rtr_priority', YLeaf(YType.uint8, 'rtr-priority')),
                                                ('link_local_interface_address', YLeaf(YType.str, 'link-local-interface-address')),
                                                ('num_of_prefixes', YLeaf(YType.uint32, 'num-of-prefixes')),
                                                ('lsa_id_options', YLeaf(YType.bits, 'lsa-id-options')),
                                            ])
                                            self.rtr_priority = None
                                            self.link_local_interface_address = None
                                            self.num_of_prefixes = None
                                            self.lsa_id_options = Bits()
                                            self._segment_path = lambda: "link-data"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData, ['rtr_priority', 'link_local_interface_address', 'num_of_prefixes', 'lsa_id_options'], name, value)


                                    class IaPrefix(Entity):
                                        """
                                        OSPFv3 Intra area prefixes
                                        
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
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: num_of_prefixes
                                        
                                        	Number of prefixes
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix, self).__init__()

                                            self.yang_name = "ia-prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                                ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                                ('referenced_adv_router', YLeaf(YType.str, 'referenced-adv-router')),
                                                ('num_of_prefixes', YLeaf(YType.uint16, 'num-of-prefixes')),
                                            ])
                                            self.referenced_ls_type = None
                                            self.referenced_link_state_id = None
                                            self.referenced_adv_router = None
                                            self.num_of_prefixes = None
                                            self._segment_path = lambda: "ia-prefix"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                            class Ospfv3Link(Entity):
                                """
                                OSPFv3 links
                                
                                .. attribute:: interface_id  (key)
                                
                                	Interface ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: neighbor_interface_id  (key)
                                
                                	Neighbor interface ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: neighbor_router_id  (key)
                                
                                	Neighbor router ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: type
                                
                                	Link type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Link, self).__init__()

                                    self.yang_name = "ospfv3-link"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_id', YLeaf(YType.uint32, 'interface-id')),
                                        ('neighbor_interface_id', YLeaf(YType.uint32, 'neighbor-interface-id')),
                                        ('neighbor_router_id', YLeaf(YType.uint32, 'neighbor-router-id')),
                                        ('type', YLeaf(YType.uint8, 'type')),
                                        ('metric', YLeaf(YType.uint16, 'metric')),
                                    ])
                                    self.interface_id = None
                                    self.neighbor_interface_id = None
                                    self.neighbor_router_id = None
                                    self.type = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                            class Ospfv3Prefix(Entity):
                                """
                                OSPFv3 prefix\-list
                                
                                .. attribute:: prefix  (key)
                                
                                	Prefix
                                	**type**\: str
                                
                                .. attribute:: prefix_options
                                
                                	Prefix options
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Prefix, self).__init__()

                                    self.yang_name = "ospfv3-prefix"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['prefix']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix', YLeaf(YType.str, 'prefix')),
                                        ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                                    ])
                                    self.prefix = None
                                    self.prefix_options = None
                                    self._segment_path = lambda: "ospfv3-prefix" + "[prefix='" + str(self.prefix) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Prefix, ['prefix', 'prefix_options'], name, value)


                            class Ospfv3IaPrefix(Entity):
                                """
                                OSPFv3 intra\-area prefix\-list
                                
                                .. attribute:: prefix  (key)
                                
                                	Prefix
                                	**type**\: str
                                
                                .. attribute:: prefix_options
                                
                                	Prefix options
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix, self).__init__()

                                    self.yang_name = "ospfv3-ia-prefix"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['prefix']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('prefix', YLeaf(YType.str, 'prefix')),
                                        ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                                    ])
                                    self.prefix = None
                                    self.prefix_options = None
                                    self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix, ['prefix', 'prefix_options'], name, value)


                    class IntfMultiTopology(Entity):
                        """
                        OSPF interface topology
                        
                        .. attribute:: name  (key)
                        
                        	One of the topology enabled on this interface
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfMultiTopology, self).__init__()

                            self.yang_name = "intf-multi-topology"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', YLeaf(YType.str, 'name')),
                            ])
                            self.name = None
                            self._segment_path = lambda: "intf-multi-topology" + "[name='" + str(self.name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfMultiTopology, ['name'], name, value)


                class AreaScopeLsa(Entity):
                    """
                    List of OSPF area scope LSA
                    
                    .. attribute:: lsa_type  (key)
                    
                    	OSPF link scope LSA type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: area_scope_lsa
                    
                    	List of OSPF link scope LSAs
                    	**type**\: list of  		 :py:class:`AreaScopeLsa_ <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa, self).__init__()

                        self.yang_name = "area-scope-lsa"
                        self.yang_parent_name = "ospf-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsa_type']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_))])
                        self._leafs = OrderedDict([
                            ('lsa_type', YLeaf(YType.uint32, 'lsa-type')),
                        ])
                        self.lsa_type = None

                        self.area_scope_lsa = YList(self)
                        self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa, ['lsa_type'], name, value)


                    class AreaScopeLsa_(Entity):
                        """
                        List of OSPF link scope LSAs
                        
                        .. attribute:: lsa_type  (key)
                        
                        	LSA Type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: adv_router  (key)
                        
                        	Advertising router
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: decoded_completed
                        
                        	The OSPF LSA body is fully decoded
                        	**type**\: bool
                        
                        .. attribute:: raw_data
                        
                        	The complete LSA in network byte order as received/sent over the wire
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ospfv2_lsa
                        
                        	OSPFv2 LSA
                        	**type**\:  :py:class:`Ospfv2Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa>`
                        
                        .. attribute:: ospfv2_link
                        
                        	Router LSA link
                        	**type**\: list of  		 :py:class:`Ospfv2Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link>`
                        
                        .. attribute:: ospfv2_topology
                        
                        	Summary LSA
                        	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Topology>`
                        
                        .. attribute:: ospfv2_external
                        
                        	External LSA
                        	**type**\: list of  		 :py:class:`Ospfv2External <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2External>`
                        
                        .. attribute:: ospfv3_lsa
                        
                        	OSPFv3 LSA
                        	**type**\:  :py:class:`Ospfv3Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa>`
                        
                        .. attribute:: ospfv3_link
                        
                        	OSPFv3 links
                        	**type**\: list of  		 :py:class:`Ospfv3Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Link>`
                        
                        .. attribute:: ospfv3_prefix
                        
                        	OSPFv3 prefix\-list
                        	**type**\: list of  		 :py:class:`Ospfv3Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Prefix>`
                        
                        .. attribute:: ospfv3_ia_prefix
                        
                        	OSPFv3 intra\-area prefix\-list
                        	**type**\: list of  		 :py:class:`Ospfv3IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3IaPrefix>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_, self).__init__()

                            self.yang_name = "area-scope-lsa"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['lsa_type','adv_router']
                            self._child_container_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa)), ("ospfv3-lsa", ("ospfv3_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa))])
                            self._child_list_classes = OrderedDict([("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2External)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Link)), ("ospfv3-prefix", ("ospfv3_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Prefix)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3IaPrefix))])
                            self._leafs = OrderedDict([
                                ('lsa_type', YLeaf(YType.uint32, 'lsa-type')),
                                ('adv_router', YLeaf(YType.str, 'adv-router')),
                                ('decoded_completed', YLeaf(YType.boolean, 'decoded-completed')),
                                ('raw_data', YLeafList(YType.uint8, 'raw-data')),
                            ])
                            self.lsa_type = None
                            self.adv_router = None
                            self.decoded_completed = None
                            self.raw_data = []

                            self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa()
                            self.ospfv2_lsa.parent = self
                            self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"
                            self._children_yang_names.add("ospfv2-lsa")

                            self.ospfv3_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa()
                            self.ospfv3_lsa.parent = self
                            self._children_name_map["ospfv3_lsa"] = "ospfv3-lsa"
                            self._children_yang_names.add("ospfv3-lsa")

                            self.ospfv2_link = YList(self)
                            self.ospfv2_topology = YList(self)
                            self.ospfv2_external = YList(self)
                            self.ospfv3_link = YList(self)
                            self.ospfv3_prefix = YList(self)
                            self.ospfv3_ia_prefix = YList(self)
                            self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']" + "[adv-router='" + str(self.adv_router) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_, ['lsa_type', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                        class Ospfv2Lsa(Entity):
                            """
                            OSPFv2 LSA
                            
                            .. attribute:: header
                            
                            	Decoded OSPFv2 LSA header data
                            	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header>`
                            
                            .. attribute:: lsa_body
                            
                            	Decoded OSPFv2 LSA body data
                            	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa, self).__init__()

                                self.yang_name = "ospfv2-lsa"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.header = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header()
                                self.header.parent = self
                                self._children_name_map["header"] = "header"
                                self._children_yang_names.add("header")

                                self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody()
                                self.lsa_body.parent = self
                                self._children_name_map["lsa_body"] = "lsa-body"
                                self._children_yang_names.add("lsa-body")
                                self._segment_path = lambda: "ospfv2-lsa"


                            class Header(Entity):
                                """
                                Decoded OSPFv2 LSA header data
                                
                                .. attribute:: lsa_id
                                
                                	LSA ID
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: opaque_type
                                
                                	Opaque type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: opaque_id
                                
                                	Opaque ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: age
                                
                                	LSA age
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: type
                                
                                	LSA type
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: adv_router
                                
                                	LSA advertising router
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: seq_num
                                
                                	LSA sequence number
                                	**type**\: str
                                
                                .. attribute:: checksum
                                
                                	LSA checksum
                                	**type**\: str
                                
                                .. attribute:: length
                                
                                	LSA length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: flag_options
                                
                                	LSA options
                                	**type**\:  :py:class:`LsaFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.LsaFlagOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header, self).__init__()

                                    self.yang_name = "header"
                                    self.yang_parent_name = "ospfv2-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                        ('opaque_type', YLeaf(YType.uint8, 'opaque-type')),
                                        ('opaque_id', YLeaf(YType.uint32, 'opaque-id')),
                                        ('age', YLeaf(YType.uint16, 'age')),
                                        ('type', YLeaf(YType.uint16, 'type')),
                                        ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                        ('seq_num', YLeaf(YType.str, 'seq-num')),
                                        ('checksum', YLeaf(YType.str, 'checksum')),
                                        ('length', YLeaf(YType.uint16, 'length')),
                                        ('flag_options', YLeaf(YType.bits, 'flag-options')),
                                    ])
                                    self.lsa_id = None
                                    self.opaque_type = None
                                    self.opaque_id = None
                                    self.age = None
                                    self.type = None
                                    self.adv_router = None
                                    self.seq_num = None
                                    self.checksum = None
                                    self.length = None
                                    self.flag_options = Bits()
                                    self._segment_path = lambda: "header"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header, ['lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'flag_options'], name, value)


                            class LsaBody(Entity):
                                """
                                Decoded OSPFv2 LSA body data
                                
                                .. attribute:: num_of_links
                                
                                	Number of links
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: network
                                
                                	Network details
                                	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network>`
                                
                                .. attribute:: summary_mask
                                
                                	Summary mask
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: external_mask
                                
                                	External mask
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: body_flag_options
                                
                                	LSA body flags
                                	**type**\:  :py:class:`Ospfv2LsaBodyFlagsOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2LsaBodyFlagsOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody, self).__init__()

                                    self.yang_name = "lsa-body"
                                    self.yang_parent_name = "ospfv2-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('num_of_links', YLeaf(YType.uint16, 'num-of-links')),
                                        ('summary_mask', YLeaf(YType.str, 'summary-mask')),
                                        ('external_mask', YLeaf(YType.str, 'external-mask')),
                                        ('body_flag_options', YLeaf(YType.bits, 'body-flag-options')),
                                    ])
                                    self.num_of_links = None
                                    self.summary_mask = None
                                    self.external_mask = None
                                    self.body_flag_options = Bits()

                                    self.network = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network()
                                    self.network.parent = self
                                    self._children_name_map["network"] = "network"
                                    self._children_yang_names.add("network")
                                    self._segment_path = lambda: "lsa-body"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody, ['num_of_links', 'summary_mask', 'external_mask', 'body_flag_options'], name, value)


                                class Network(Entity):
                                    """
                                    Network details
                                    
                                    .. attribute:: network_mask
                                    
                                    	IP network mask
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: attached_router
                                    
                                    	List of the routers attached to the network
                                    	**type**\: list of int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                        self.yang_name = "network"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('network_mask', YLeaf(YType.str, 'network-mask')),
                                            ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                        ])
                                        self.network_mask = None
                                        self.attached_router = []
                                        self._segment_path = lambda: "network"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network, ['network_mask', 'attached_router'], name, value)


                        class Ospfv2Link(Entity):
                            """
                            Router LSA link
                            
                            .. attribute:: link_id  (key)
                            
                            	Link ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: link_data  (key)
                            
                            	Link data
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Link type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: ospfv2_topology
                            
                            	Topology specific information
                            	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link.Ospfv2Topology>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link, self).__init__()

                                self.yang_name = "ospfv2-link"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['link_id','link_data']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link.Ospfv2Topology))])
                                self._leafs = OrderedDict([
                                    ('link_id', YLeaf(YType.uint32, 'link-id')),
                                    ('link_data', YLeaf(YType.uint32, 'link-data')),
                                    ('type', YLeaf(YType.uint8, 'type')),
                                ])
                                self.link_id = None
                                self.link_data = None
                                self.type = None

                                self.ospfv2_topology = YList(self)
                                self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link, ['link_id', 'link_data', 'type'], name, value)


                            class Ospfv2Topology(Entity):
                                """
                                Topology specific information
                                
                                .. attribute:: mt_id  (key)
                                
                                	MT\-ID for topology enabled link
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: metric
                                
                                	Metric for the topology
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link.Ospfv2Topology, self).__init__()

                                    self.yang_name = "ospfv2-topology"
                                    self.yang_parent_name = "ospfv2-link"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                        ('metric', YLeaf(YType.uint16, 'metric')),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                        class Ospfv2Topology(Entity):
                            """
                            Summary LSA
                            
                            .. attribute:: mt_id  (key)
                            
                            	MT\-ID for topology enabled link
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric
                            
                            	Metric for the topology
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Topology, self).__init__()

                                self.yang_name = "ospfv2-topology"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                    ('metric', YLeaf(YType.uint16, 'metric')),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                        class Ospfv2External(Entity):
                            """
                            External LSA
                            
                            .. attribute:: mt_id  (key)
                            
                            	MT\-ID for topology enabled on the link
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric
                            
                            	Metric for the topology
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: forwarding_address
                            
                            	Forwarding address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: external_route_tag
                            
                            	Route tag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2External, self).__init__()

                                self.yang_name = "ospfv2-external"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                    ('metric', YLeaf(YType.uint32, 'metric')),
                                    ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                    ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self.forwarding_address = None
                                self.external_route_tag = None
                                self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2External, ['mt_id', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                        class Ospfv3Lsa(Entity):
                            """
                            OSPFv3 LSA
                            
                            .. attribute:: header
                            
                            	Decoded OSPFv3 LSA header
                            	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header>`
                            
                            .. attribute:: lsa_body
                            
                            	Decoded OSPFv3 LSA body
                            	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa, self).__init__()

                                self.yang_name = "ospfv3-lsa"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.header = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header()
                                self.header.parent = self
                                self._children_name_map["header"] = "header"
                                self._children_yang_names.add("header")

                                self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody()
                                self.lsa_body.parent = self
                                self._children_name_map["lsa_body"] = "lsa-body"
                                self._children_yang_names.add("lsa-body")
                                self._segment_path = lambda: "ospfv3-lsa"


                            class Header(Entity):
                                """
                                Decoded OSPFv3 LSA header
                                
                                .. attribute:: lsa_id
                                
                                	LSA ID
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: lsa_header
                                
                                	LSA header
                                	**type**\:  :py:class:`LsaHeader <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader>`
                                
                                .. attribute:: lsa_hdr_options
                                
                                	OSPFv3 LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header, self).__init__()

                                    self.yang_name = "header"
                                    self.yang_parent_name = "ospfv3-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                        ('lsa_hdr_options', YLeaf(YType.bits, 'lsa-hdr-options')),
                                    ])
                                    self.lsa_id = None
                                    self.lsa_hdr_options = Bits()

                                    self.lsa_header = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader()
                                    self.lsa_header.parent = self
                                    self._children_name_map["lsa_header"] = "lsa-header"
                                    self._children_yang_names.add("lsa-header")
                                    self._segment_path = lambda: "header"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header, ['lsa_id', 'lsa_hdr_options'], name, value)


                                class LsaHeader(Entity):
                                    """
                                    LSA header
                                    
                                    .. attribute:: age
                                    
                                    	LSA age
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: type
                                    
                                    	LSA type
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: adv_router
                                    
                                    	LSA advertising router
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: seq_num
                                    
                                    	LSA sequence number
                                    	**type**\: str
                                    
                                    .. attribute:: checksum
                                    
                                    	LSA checksum
                                    	**type**\: str
                                    
                                    .. attribute:: length
                                    
                                    	LSA length
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader, self).__init__()

                                        self.yang_name = "lsa-header"
                                        self.yang_parent_name = "header"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('age', YLeaf(YType.uint16, 'age')),
                                            ('type', YLeaf(YType.uint16, 'type')),
                                            ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                            ('seq_num', YLeaf(YType.str, 'seq-num')),
                                            ('checksum', YLeaf(YType.str, 'checksum')),
                                            ('length', YLeaf(YType.uint16, 'length')),
                                        ])
                                        self.age = None
                                        self.type = None
                                        self.adv_router = None
                                        self.seq_num = None
                                        self.checksum = None
                                        self.length = None
                                        self._segment_path = lambda: "lsa-header"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader, ['age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                            class LsaBody(Entity):
                                """
                                Decoded OSPFv3 LSA body
                                
                                .. attribute:: network
                                
                                	OSPFv3 network
                                	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network>`
                                
                                .. attribute:: prefix
                                
                                	OSPFv3 inter area prefix
                                	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix>`
                                
                                .. attribute:: ia_router
                                
                                	OSPFv3 inter area router
                                	**type**\:  :py:class:`IaRouter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter>`
                                
                                .. attribute:: lsa_external
                                
                                	OSPFv3 LSA external
                                	**type**\:  :py:class:`LsaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal>`
                                
                                .. attribute:: nssa
                                
                                	OSPFv3 NSSA
                                	**type**\:  :py:class:`Nssa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa>`
                                
                                .. attribute:: link_data
                                
                                	OSPFv3 Link data
                                	**type**\:  :py:class:`LinkData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData>`
                                
                                .. attribute:: ia_prefix
                                
                                	OSPFv3 Intra area prefixes
                                	**type**\:  :py:class:`IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix>`
                                
                                .. attribute:: lsa_flag_options
                                
                                	LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                .. attribute:: lsa_body_flags
                                
                                	LSA Body Flags
                                	**type**\:  :py:class:`Ospfv3LsaBodyFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaBodyFlagOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody, self).__init__()

                                    self.yang_name = "lsa-body"
                                    self.yang_parent_name = "ospfv3-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('lsa_flag_options', YLeaf(YType.bits, 'lsa-flag-options')),
                                        ('lsa_body_flags', YLeaf(YType.bits, 'lsa-body-flags')),
                                    ])
                                    self.lsa_flag_options = Bits()
                                    self.lsa_body_flags = Bits()

                                    self.network = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network()
                                    self.network.parent = self
                                    self._children_name_map["network"] = "network"
                                    self._children_yang_names.add("network")

                                    self.prefix = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix()
                                    self.prefix.parent = self
                                    self._children_name_map["prefix"] = "prefix"
                                    self._children_yang_names.add("prefix")

                                    self.ia_router = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter()
                                    self.ia_router.parent = self
                                    self._children_name_map["ia_router"] = "ia-router"
                                    self._children_yang_names.add("ia-router")

                                    self.lsa_external = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal()
                                    self.lsa_external.parent = self
                                    self._children_name_map["lsa_external"] = "lsa-external"
                                    self._children_yang_names.add("lsa-external")

                                    self.nssa = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa()
                                    self.nssa.parent = self
                                    self._children_name_map["nssa"] = "nssa"
                                    self._children_yang_names.add("nssa")

                                    self.link_data = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData()
                                    self.link_data.parent = self
                                    self._children_name_map["link_data"] = "link-data"
                                    self._children_yang_names.add("link-data")

                                    self.ia_prefix = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix()
                                    self.ia_prefix.parent = self
                                    self._children_name_map["ia_prefix"] = "ia-prefix"
                                    self._children_yang_names.add("ia-prefix")
                                    self._segment_path = lambda: "lsa-body"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody, ['lsa_flag_options', 'lsa_body_flags'], name, value)


                                class Network(Entity):
                                    """
                                    OSPFv3 network
                                    
                                    .. attribute:: attached_router
                                    
                                    	List of the routers attached to the network
                                    	**type**\: list of int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: lsa_net_options
                                    
                                    	Network LSA options
                                    	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network, self).__init__()

                                        self.yang_name = "network"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                            ('lsa_net_options', YLeaf(YType.bits, 'lsa-net-options')),
                                        ])
                                        self.attached_router = []
                                        self.lsa_net_options = Bits()
                                        self._segment_path = lambda: "network"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network, ['attached_router', 'lsa_net_options'], name, value)


                                class Prefix(Entity):
                                    """
                                    OSPFv3 inter area prefix
                                    
                                    .. attribute:: metric
                                    
                                    	Metric
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: ia_prefix
                                    
                                    	Inter area Prefix
                                    	**type**\: str
                                    
                                    .. attribute:: ia_prefix_options
                                    
                                    	Inter area prefix options
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix, self).__init__()

                                        self.yang_name = "prefix"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric', YLeaf(YType.uint32, 'metric')),
                                            ('ia_prefix', YLeaf(YType.str, 'ia-prefix')),
                                            ('ia_prefix_options', YLeaf(YType.str, 'ia-prefix-options')),
                                        ])
                                        self.metric = None
                                        self.ia_prefix = None
                                        self.ia_prefix_options = None
                                        self._segment_path = lambda: "prefix"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix, ['metric', 'ia_prefix', 'ia_prefix_options'], name, value)


                                class IaRouter(Entity):
                                    """
                                    OSPFv3 inter area router
                                    
                                    .. attribute:: metric
                                    
                                    	Metric
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: destination_router_id
                                    
                                    	Router ID of the router being described by the LSA
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: lsa_ia_options
                                    
                                    	Inter area LSA options
                                    	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter, self).__init__()

                                        self.yang_name = "ia-router"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric', YLeaf(YType.uint32, 'metric')),
                                            ('destination_router_id', YLeaf(YType.uint32, 'destination-router-id')),
                                            ('lsa_ia_options', YLeaf(YType.bits, 'lsa-ia-options')),
                                        ])
                                        self.metric = None
                                        self.destination_router_id = None
                                        self.lsa_ia_options = Bits()
                                        self._segment_path = lambda: "ia-router"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter, ['metric', 'destination_router_id', 'lsa_ia_options'], name, value)


                                class LsaExternal(Entity):
                                    """
                                    OSPFv3 LSA external
                                    
                                    .. attribute:: metric
                                    
                                    	Metric
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: flags
                                    
                                    	LSA Flags
                                    	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal.Flags>`
                                    
                                    .. attribute:: referenced_ls_type
                                    
                                    	Referenced Link State type
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: external_prefix
                                    
                                    	Prefix
                                    	**type**\: str
                                    
                                    .. attribute:: external_prefix_options
                                    
                                    	Prefix options
                                    	**type**\: str
                                    
                                    .. attribute:: forwarding_address
                                    
                                    	Forwarding address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
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

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal, self).__init__()

                                        self.yang_name = "lsa-external"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal.Flags))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric', YLeaf(YType.uint32, 'metric')),
                                            ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                            ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                            ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                            ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                            ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                            ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                        ])
                                        self.metric = None
                                        self.referenced_ls_type = None
                                        self.external_prefix = None
                                        self.external_prefix_options = None
                                        self.forwarding_address = None
                                        self.external_route_tag = None
                                        self.referenced_link_state_id = None

                                        self.flags = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal.Flags()
                                        self.flags.parent = self
                                        self._children_name_map["flags"] = "flags"
                                        self._children_yang_names.add("flags")
                                        self._segment_path = lambda: "lsa-external"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                    class Flags(Entity):
                                        """
                                        LSA Flags
                                        
                                        .. attribute:: e_flag
                                        
                                        	When set, the metric specified is a Type 2 external metric
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal.Flags, self).__init__()

                                            self.yang_name = "flags"
                                            self.yang_parent_name = "lsa-external"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                            ])
                                            self.e_flag = None
                                            self._segment_path = lambda: "flags"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal.Flags, ['e_flag'], name, value)


                                class Nssa(Entity):
                                    """
                                    OSPFv3 NSSA
                                    
                                    .. attribute:: lsa_nssa_external
                                    
                                    	NSSA LSA
                                    	**type**\:  :py:class:`LsaNssaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa, self).__init__()

                                        self.yang_name = "nssa"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict()

                                        self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal()
                                        self.lsa_nssa_external.parent = self
                                        self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                        self._children_yang_names.add("lsa-nssa-external")
                                        self._segment_path = lambda: "nssa"


                                    class LsaNssaExternal(Entity):
                                        """
                                        NSSA LSA
                                        
                                        .. attribute:: metric
                                        
                                        	Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: flags
                                        
                                        	LSA Flags
                                        	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags>`
                                        
                                        .. attribute:: referenced_ls_type
                                        
                                        	Referenced Link State type
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: external_prefix
                                        
                                        	Prefix
                                        	**type**\: str
                                        
                                        .. attribute:: external_prefix_options
                                        
                                        	Prefix options
                                        	**type**\: str
                                        
                                        .. attribute:: forwarding_address
                                        
                                        	Forwarding address
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
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

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                            self.yang_name = "lsa-nssa-external"
                                            self.yang_parent_name = "nssa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', YLeaf(YType.uint32, 'metric')),
                                                ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                                ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                                ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                                ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                                ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                                ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                            ])
                                            self.metric = None
                                            self.referenced_ls_type = None
                                            self.external_prefix = None
                                            self.external_prefix_options = None
                                            self.forwarding_address = None
                                            self.external_route_tag = None
                                            self.referenced_link_state_id = None

                                            self.flags = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags()
                                            self.flags.parent = self
                                            self._children_name_map["flags"] = "flags"
                                            self._children_yang_names.add("flags")
                                            self._segment_path = lambda: "lsa-nssa-external"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                        class Flags(Entity):
                                            """
                                            LSA Flags
                                            
                                            .. attribute:: e_flag
                                            
                                            	When set, the metric specified is a Type 2 external metric
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ospf-ios-xe-oper'
                                            _revision = '2017-10-10'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                                self.yang_name = "flags"
                                                self.yang_parent_name = "lsa-nssa-external"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                                ])
                                                self.e_flag = None
                                                self._segment_path = lambda: "flags"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, ['e_flag'], name, value)


                                class LinkData(Entity):
                                    """
                                    OSPFv3 Link data
                                    
                                    .. attribute:: rtr_priority
                                    
                                    	Router priority of the interce
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
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
                                    
                                    .. attribute:: lsa_id_options
                                    
                                    	Link data LSA options
                                    	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData, self).__init__()

                                        self.yang_name = "link-data"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('rtr_priority', YLeaf(YType.uint8, 'rtr-priority')),
                                            ('link_local_interface_address', YLeaf(YType.str, 'link-local-interface-address')),
                                            ('num_of_prefixes', YLeaf(YType.uint32, 'num-of-prefixes')),
                                            ('lsa_id_options', YLeaf(YType.bits, 'lsa-id-options')),
                                        ])
                                        self.rtr_priority = None
                                        self.link_local_interface_address = None
                                        self.num_of_prefixes = None
                                        self.lsa_id_options = Bits()
                                        self._segment_path = lambda: "link-data"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData, ['rtr_priority', 'link_local_interface_address', 'num_of_prefixes', 'lsa_id_options'], name, value)


                                class IaPrefix(Entity):
                                    """
                                    OSPFv3 Intra area prefixes
                                    
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
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: num_of_prefixes
                                    
                                    	Number of prefixes
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix, self).__init__()

                                        self.yang_name = "ia-prefix"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                            ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                            ('referenced_adv_router', YLeaf(YType.str, 'referenced-adv-router')),
                                            ('num_of_prefixes', YLeaf(YType.uint16, 'num-of-prefixes')),
                                        ])
                                        self.referenced_ls_type = None
                                        self.referenced_link_state_id = None
                                        self.referenced_adv_router = None
                                        self.num_of_prefixes = None
                                        self._segment_path = lambda: "ia-prefix"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                        class Ospfv3Link(Entity):
                            """
                            OSPFv3 links
                            
                            .. attribute:: interface_id  (key)
                            
                            	Interface ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: neighbor_interface_id  (key)
                            
                            	Neighbor interface ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: neighbor_router_id  (key)
                            
                            	Neighbor router ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Link type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: metric
                            
                            	Metric
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Link, self).__init__()

                                self.yang_name = "ospfv3-link"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_id', YLeaf(YType.uint32, 'interface-id')),
                                    ('neighbor_interface_id', YLeaf(YType.uint32, 'neighbor-interface-id')),
                                    ('neighbor_router_id', YLeaf(YType.uint32, 'neighbor-router-id')),
                                    ('type', YLeaf(YType.uint8, 'type')),
                                    ('metric', YLeaf(YType.uint16, 'metric')),
                                ])
                                self.interface_id = None
                                self.neighbor_interface_id = None
                                self.neighbor_router_id = None
                                self.type = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                        class Ospfv3Prefix(Entity):
                            """
                            OSPFv3 prefix\-list
                            
                            .. attribute:: prefix  (key)
                            
                            	Prefix
                            	**type**\: str
                            
                            .. attribute:: prefix_options
                            
                            	Prefix options
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Prefix, self).__init__()

                                self.yang_name = "ospfv3-prefix"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['prefix']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                    ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                                ])
                                self.prefix = None
                                self.prefix_options = None
                                self._segment_path = lambda: "ospfv3-prefix" + "[prefix='" + str(self.prefix) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Prefix, ['prefix', 'prefix_options'], name, value)


                        class Ospfv3IaPrefix(Entity):
                            """
                            OSPFv3 intra\-area prefix\-list
                            
                            .. attribute:: prefix  (key)
                            
                            	Prefix
                            	**type**\: str
                            
                            .. attribute:: prefix_options
                            
                            	Prefix options
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3IaPrefix, self).__init__()

                                self.yang_name = "ospfv3-ia-prefix"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['prefix']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                    ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                                ])
                                self.prefix = None
                                self.prefix_options = None
                                self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3IaPrefix, ['prefix', 'prefix_options'], name, value)


            class LinkScopeLsas(Entity):
                """
                List OSPF link scope LSA
                
                .. attribute:: lsa_type  (key)
                
                	OSPF link scope LSA type
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: link_scope_lsa
                
                	List of OSPF link scope LSAs
                	**type**\: list of  		 :py:class:`LinkScopeLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa>`
                
                .. attribute:: area_scope_lsa
                
                	List OSPF area scope LSA databases
                	**type**\: list of  		 :py:class:`AreaScopeLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2017-10-10'

                def __init__(self):
                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas, self).__init__()

                    self.yang_name = "link-scope-lsas"
                    self.yang_parent_name = "ospf-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['lsa_type']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("link-scope-lsa", ("link_scope_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa)), ("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa))])
                    self._leafs = OrderedDict([
                        ('lsa_type', YLeaf(YType.uint32, 'lsa-type')),
                    ])
                    self.lsa_type = None

                    self.link_scope_lsa = YList(self)
                    self.area_scope_lsa = YList(self)
                    self._segment_path = lambda: "link-scope-lsas" + "[lsa-type='" + str(self.lsa_type) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas, ['lsa_type'], name, value)


                class LinkScopeLsa(Entity):
                    """
                    List of OSPF link scope LSAs
                    
                    .. attribute:: lsa_id  (key)
                    
                    	LSA ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: adv_router  (key)
                    
                    	Advertising router
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: decoded_completed
                    
                    	The OSPF LSA body is fully decoded
                    	**type**\: bool
                    
                    .. attribute:: raw_data
                    
                    	The complete LSA in network byte order as received/sent over the wire
                    	**type**\: list of int
                    
                    	**range:** 0..255
                    
                    .. attribute:: version
                    
                    	Version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ospfv2_lsa
                    
                    	OSPFv2 LSA
                    	**type**\:  :py:class:`Ospfv2Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa>`
                    
                    .. attribute:: ospfv2_link
                    
                    	OSPFv2 LSA link
                    	**type**\: list of  		 :py:class:`Ospfv2Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link>`
                    
                    .. attribute:: ospfv2_topology
                    
                    	Summary LSA
                    	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Topology>`
                    
                    .. attribute:: ospfv2_external
                    
                    	External LSA
                    	**type**\: list of  		 :py:class:`Ospfv2External <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2External>`
                    
                    .. attribute:: ospfv2_unknown_tlv
                    
                    	OSPFv2 Unknown TLV
                    	**type**\: list of  		 :py:class:`Ospfv2UnknownTlv <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv>`
                    
                    .. attribute:: ospfv3_lsa_val
                    
                    	OSPFv3 LSA
                    	**type**\:  :py:class:`Ospfv3LsaVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal>`
                    
                    .. attribute:: ospfv3_link
                    
                    	OSPFv3 links
                    	**type**\: list of  		 :py:class:`Ospfv3Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3Link>`
                    
                    .. attribute:: ospfv3_prefix_list
                    
                    	OSPFv3 prefix\-list
                    	**type**\: list of  		 :py:class:`Ospfv3PrefixList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList>`
                    
                    .. attribute:: ospfv3_ia_prefix
                    
                    	OSPFv3 intra\-area prefix\-list
                    	**type**\: list of  		 :py:class:`Ospfv3IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix>`
                    
                    .. attribute:: multi_topology
                    
                    	OSPF multi\-topology interface augmentation
                    	**type**\: list of  		 :py:class:`MultiTopology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.MultiTopology>`
                    
                    .. attribute:: router_address
                    
                    	Router address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: tlv
                    
                    	Link TLV
                    	**type**\:  :py:class:`Tlv <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv>`
                    
                    .. attribute:: unknown_sub_tlv
                    
                    	OSPFv2 Unknown sub TLV
                    	**type**\: list of  		 :py:class:`UnknownSubTlv <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.UnknownSubTlv>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa, self).__init__()

                        self.yang_name = "link-scope-lsa"
                        self.yang_parent_name = "link-scope-lsas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsa_id','adv_router']
                        self._child_container_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa)), ("ospfv3-lsa-val", ("ospfv3_lsa_val", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal)), ("tlv", ("tlv", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv))])
                        self._child_list_classes = OrderedDict([("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2External)), ("ospfv2-unknown-tlv", ("ospfv2_unknown_tlv", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3Link)), ("ospfv3-prefix-list", ("ospfv3_prefix_list", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix)), ("multi-topology", ("multi_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.MultiTopology)), ("unknown-sub-tlv", ("unknown_sub_tlv", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.UnknownSubTlv))])
                        self._leafs = OrderedDict([
                            ('lsa_id', YLeaf(YType.uint32, 'lsa-id')),
                            ('adv_router', YLeaf(YType.str, 'adv-router')),
                            ('decoded_completed', YLeaf(YType.boolean, 'decoded-completed')),
                            ('raw_data', YLeafList(YType.uint8, 'raw-data')),
                            ('version', YLeaf(YType.uint32, 'version')),
                            ('router_address', YLeaf(YType.str, 'router-address')),
                        ])
                        self.lsa_id = None
                        self.adv_router = None
                        self.decoded_completed = None
                        self.raw_data = []
                        self.version = None
                        self.router_address = None

                        self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa()
                        self.ospfv2_lsa.parent = self
                        self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"
                        self._children_yang_names.add("ospfv2-lsa")

                        self.ospfv3_lsa_val = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal()
                        self.ospfv3_lsa_val.parent = self
                        self._children_name_map["ospfv3_lsa_val"] = "ospfv3-lsa-val"
                        self._children_yang_names.add("ospfv3-lsa-val")

                        self.tlv = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv()
                        self.tlv.parent = self
                        self._children_name_map["tlv"] = "tlv"
                        self._children_yang_names.add("tlv")

                        self.ospfv2_link = YList(self)
                        self.ospfv2_topology = YList(self)
                        self.ospfv2_external = YList(self)
                        self.ospfv2_unknown_tlv = YList(self)
                        self.ospfv3_link = YList(self)
                        self.ospfv3_prefix_list = YList(self)
                        self.ospfv3_ia_prefix = YList(self)
                        self.multi_topology = YList(self)
                        self.unknown_sub_tlv = YList(self)
                        self._segment_path = lambda: "link-scope-lsa" + "[lsa-id='" + str(self.lsa_id) + "']" + "[adv-router='" + str(self.adv_router) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa, ['lsa_id', 'adv_router', 'decoded_completed', 'raw_data', 'version', 'router_address'], name, value)


                    class Ospfv2Lsa(Entity):
                        """
                        OSPFv2 LSA
                        
                        .. attribute:: header
                        
                        	Decoded OSPFv2 LSA header data
                        	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header>`
                        
                        .. attribute:: lsa_body
                        
                        	Decoded OSPFv2 LSA body data
                        	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa, self).__init__()

                            self.yang_name = "ospfv2-lsa"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"
                            self._children_yang_names.add("header")

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._children_yang_names.add("lsa-body")
                            self._segment_path = lambda: "ospfv2-lsa"


                        class Header(Entity):
                            """
                            Decoded OSPFv2 LSA header data
                            
                            .. attribute:: lsa_id
                            
                            	LSA ID
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: opaque_type
                            
                            	Opaque type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: opaque_id
                            
                            	Opaque ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: age
                            
                            	LSA age
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: type
                            
                            	LSA type
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: adv_router
                            
                            	LSA advertising router
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seq_num
                            
                            	LSA sequence number
                            	**type**\: str
                            
                            .. attribute:: checksum
                            
                            	LSA checksum
                            	**type**\: str
                            
                            .. attribute:: length
                            
                            	LSA length
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: flag_options
                            
                            	LSA options
                            	**type**\:  :py:class:`LsaFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.LsaFlagOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                    ('opaque_type', YLeaf(YType.uint8, 'opaque-type')),
                                    ('opaque_id', YLeaf(YType.uint32, 'opaque-id')),
                                    ('age', YLeaf(YType.uint16, 'age')),
                                    ('type', YLeaf(YType.uint16, 'type')),
                                    ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                    ('seq_num', YLeaf(YType.str, 'seq-num')),
                                    ('checksum', YLeaf(YType.str, 'checksum')),
                                    ('length', YLeaf(YType.uint16, 'length')),
                                    ('flag_options', YLeaf(YType.bits, 'flag-options')),
                                ])
                                self.lsa_id = None
                                self.opaque_type = None
                                self.opaque_id = None
                                self.age = None
                                self.type = None
                                self.adv_router = None
                                self.seq_num = None
                                self.checksum = None
                                self.length = None
                                self.flag_options = Bits()
                                self._segment_path = lambda: "header"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header, ['lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'flag_options'], name, value)


                        class LsaBody(Entity):
                            """
                            Decoded OSPFv2 LSA body data
                            
                            .. attribute:: num_of_links
                            
                            	Number of links
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: network
                            
                            	Network details
                            	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network>`
                            
                            .. attribute:: summary_mask
                            
                            	Summary mask
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: external_mask
                            
                            	External mask
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: body_flag_options
                            
                            	LSA body flags
                            	**type**\:  :py:class:`Ospfv2LsaBodyFlagsOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2LsaBodyFlagsOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_of_links', YLeaf(YType.uint16, 'num-of-links')),
                                    ('summary_mask', YLeaf(YType.str, 'summary-mask')),
                                    ('external_mask', YLeaf(YType.str, 'external-mask')),
                                    ('body_flag_options', YLeaf(YType.bits, 'body-flag-options')),
                                ])
                                self.num_of_links = None
                                self.summary_mask = None
                                self.external_mask = None
                                self.body_flag_options = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"
                                self._children_yang_names.add("network")
                                self._segment_path = lambda: "lsa-body"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody, ['num_of_links', 'summary_mask', 'external_mask', 'body_flag_options'], name, value)


                            class Network(Entity):
                                """
                                Network details
                                
                                .. attribute:: network_mask
                                
                                	IP network mask
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: attached_router
                                
                                	List of the routers attached to the network
                                	**type**\: list of int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('network_mask', YLeaf(YType.str, 'network-mask')),
                                        ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                    ])
                                    self.network_mask = None
                                    self.attached_router = []
                                    self._segment_path = lambda: "network"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network, ['network_mask', 'attached_router'], name, value)


                    class Ospfv2Link(Entity):
                        """
                        OSPFv2 LSA link
                        
                        .. attribute:: link_id  (key)
                        
                        	Link ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: link_data  (key)
                        
                        	Link data
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Link type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ospfv2_topology
                        
                        	Topology specific information
                        	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link, self).__init__()

                            self.yang_name = "ospfv2-link"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['link_id','link_data']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology))])
                            self._leafs = OrderedDict([
                                ('link_id', YLeaf(YType.uint32, 'link-id')),
                                ('link_data', YLeaf(YType.uint32, 'link-data')),
                                ('type', YLeaf(YType.uint8, 'type')),
                            ])
                            self.link_id = None
                            self.link_data = None
                            self.type = None

                            self.ospfv2_topology = YList(self)
                            self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link, ['link_id', 'link_data', 'type'], name, value)


                        class Ospfv2Topology(Entity):
                            """
                            Topology specific information
                            
                            .. attribute:: mt_id  (key)
                            
                            	MT\-ID for topology enabled link
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric
                            
                            	Metric for the topology
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                self.yang_name = "ospfv2-topology"
                                self.yang_parent_name = "ospfv2-link"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                    ('metric', YLeaf(YType.uint16, 'metric')),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                    class Ospfv2Topology(Entity):
                        """
                        Summary LSA
                        
                        .. attribute:: mt_id  (key)
                        
                        	MT\-ID for topology enabled link
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: metric
                        
                        	Metric for the topology
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Topology, self).__init__()

                            self.yang_name = "ospfv2-topology"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                ('metric', YLeaf(YType.uint16, 'metric')),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                    class Ospfv2External(Entity):
                        """
                        External LSA
                        
                        .. attribute:: mt_id  (key)
                        
                        	MT\-ID for topology enabled on the link
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: metric
                        
                        	Metric for the topology
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: forwarding_address
                        
                        	Forwarding address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: external_route_tag
                        
                        	Route tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2External, self).__init__()

                            self.yang_name = "ospfv2-external"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                ('metric', YLeaf(YType.uint32, 'metric')),
                                ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self.forwarding_address = None
                            self.external_route_tag = None
                            self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2External, ['mt_id', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                    class Ospfv2UnknownTlv(Entity):
                        """
                        OSPFv2 Unknown TLV
                        
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
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv, self).__init__()

                            self.yang_name = "ospfv2-unknown-tlv"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', YLeaf(YType.uint16, 'type')),
                                ('length', YLeaf(YType.uint16, 'length')),
                                ('value', YLeafList(YType.uint8, 'value')),
                            ])
                            self.type = None
                            self.length = None
                            self.value = []
                            self._segment_path = lambda: "ospfv2-unknown-tlv" + "[type='" + str(self.type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv, ['type', 'length', 'value'], name, value)


                    class Ospfv3LsaVal(Entity):
                        """
                        OSPFv3 LSA
                        
                        .. attribute:: header
                        
                        	Decoded OSPFv3 LSA header
                        	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header>`
                        
                        .. attribute:: lsa_body
                        
                        	Decoded OSPFv3 LSA body
                        	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal, self).__init__()

                            self.yang_name = "ospfv3-lsa-val"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"
                            self._children_yang_names.add("header")

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._children_yang_names.add("lsa-body")
                            self._segment_path = lambda: "ospfv3-lsa-val"


                        class Header(Entity):
                            """
                            Decoded OSPFv3 LSA header
                            
                            .. attribute:: lsa_id
                            
                            	LSA ID
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: lsa_header
                            
                            	LSA header
                            	**type**\:  :py:class:`LsaHeader <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader>`
                            
                            .. attribute:: lsa_hdr_options
                            
                            	OSPFv3 LSA options
                            	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv3-lsa-val"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                    ('lsa_hdr_options', YLeaf(YType.bits, 'lsa-hdr-options')),
                                ])
                                self.lsa_id = None
                                self.lsa_hdr_options = Bits()

                                self.lsa_header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader()
                                self.lsa_header.parent = self
                                self._children_name_map["lsa_header"] = "lsa-header"
                                self._children_yang_names.add("lsa-header")
                                self._segment_path = lambda: "header"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header, ['lsa_id', 'lsa_hdr_options'], name, value)


                            class LsaHeader(Entity):
                                """
                                LSA header
                                
                                .. attribute:: age
                                
                                	LSA age
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: type
                                
                                	LSA type
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: adv_router
                                
                                	LSA advertising router
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: seq_num
                                
                                	LSA sequence number
                                	**type**\: str
                                
                                .. attribute:: checksum
                                
                                	LSA checksum
                                	**type**\: str
                                
                                .. attribute:: length
                                
                                	LSA length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader, self).__init__()

                                    self.yang_name = "lsa-header"
                                    self.yang_parent_name = "header"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('age', YLeaf(YType.uint16, 'age')),
                                        ('type', YLeaf(YType.uint16, 'type')),
                                        ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                        ('seq_num', YLeaf(YType.str, 'seq-num')),
                                        ('checksum', YLeaf(YType.str, 'checksum')),
                                        ('length', YLeaf(YType.uint16, 'length')),
                                    ])
                                    self.age = None
                                    self.type = None
                                    self.adv_router = None
                                    self.seq_num = None
                                    self.checksum = None
                                    self.length = None
                                    self._segment_path = lambda: "lsa-header"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader, ['age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                        class LsaBody(Entity):
                            """
                            Decoded OSPFv3 LSA body
                            
                            .. attribute:: network
                            
                            	OSPFv3 network
                            	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network>`
                            
                            .. attribute:: prefix
                            
                            	OSPFv3 inter area prefix
                            	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix>`
                            
                            .. attribute:: ia_router
                            
                            	OSPFv3 inter area router
                            	**type**\:  :py:class:`IaRouter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter>`
                            
                            .. attribute:: lsa_external
                            
                            	OSPFv3 LSA external
                            	**type**\:  :py:class:`LsaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal>`
                            
                            .. attribute:: nssa
                            
                            	OSPFv3 NSSA
                            	**type**\:  :py:class:`Nssa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa>`
                            
                            .. attribute:: link_data
                            
                            	OSPFv3 Link data
                            	**type**\:  :py:class:`LinkData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData>`
                            
                            .. attribute:: ia_prefix
                            
                            	OSPFv3 Intra area prefixes
                            	**type**\:  :py:class:`IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix>`
                            
                            .. attribute:: lsa_flag_options
                            
                            	LSA options
                            	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                            
                            .. attribute:: lsa_body_flags
                            
                            	LSA Body Flags
                            	**type**\:  :py:class:`Ospfv3LsaBodyFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaBodyFlagOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv3-lsa-val"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_flag_options', YLeaf(YType.bits, 'lsa-flag-options')),
                                    ('lsa_body_flags', YLeaf(YType.bits, 'lsa-body-flags')),
                                ])
                                self.lsa_flag_options = Bits()
                                self.lsa_body_flags = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"
                                self._children_yang_names.add("network")

                                self.prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix()
                                self.prefix.parent = self
                                self._children_name_map["prefix"] = "prefix"
                                self._children_yang_names.add("prefix")

                                self.ia_router = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter()
                                self.ia_router.parent = self
                                self._children_name_map["ia_router"] = "ia-router"
                                self._children_yang_names.add("ia-router")

                                self.lsa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal()
                                self.lsa_external.parent = self
                                self._children_name_map["lsa_external"] = "lsa-external"
                                self._children_yang_names.add("lsa-external")

                                self.nssa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa()
                                self.nssa.parent = self
                                self._children_name_map["nssa"] = "nssa"
                                self._children_yang_names.add("nssa")

                                self.link_data = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData()
                                self.link_data.parent = self
                                self._children_name_map["link_data"] = "link-data"
                                self._children_yang_names.add("link-data")

                                self.ia_prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix()
                                self.ia_prefix.parent = self
                                self._children_name_map["ia_prefix"] = "ia-prefix"
                                self._children_yang_names.add("ia-prefix")
                                self._segment_path = lambda: "lsa-body"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody, ['lsa_flag_options', 'lsa_body_flags'], name, value)


                            class Network(Entity):
                                """
                                OSPFv3 network
                                
                                .. attribute:: attached_router
                                
                                	List of the routers attached to the network
                                	**type**\: list of int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lsa_net_options
                                
                                	Network LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                        ('lsa_net_options', YLeaf(YType.bits, 'lsa-net-options')),
                                    ])
                                    self.attached_router = []
                                    self.lsa_net_options = Bits()
                                    self._segment_path = lambda: "network"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network, ['attached_router', 'lsa_net_options'], name, value)


                            class Prefix(Entity):
                                """
                                OSPFv3 inter area prefix
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ia_prefix
                                
                                	Inter area Prefix
                                	**type**\: str
                                
                                .. attribute:: ia_prefix_options
                                
                                	Inter area prefix options
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('ia_prefix', YLeaf(YType.str, 'ia-prefix')),
                                        ('ia_prefix_options', YLeaf(YType.str, 'ia-prefix-options')),
                                    ])
                                    self.metric = None
                                    self.ia_prefix = None
                                    self.ia_prefix_options = None
                                    self._segment_path = lambda: "prefix"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix, ['metric', 'ia_prefix', 'ia_prefix_options'], name, value)


                            class IaRouter(Entity):
                                """
                                OSPFv3 inter area router
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: destination_router_id
                                
                                	Router ID of the router being described by the LSA
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lsa_ia_options
                                
                                	Inter area LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter, self).__init__()

                                    self.yang_name = "ia-router"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('destination_router_id', YLeaf(YType.uint32, 'destination-router-id')),
                                        ('lsa_ia_options', YLeaf(YType.bits, 'lsa-ia-options')),
                                    ])
                                    self.metric = None
                                    self.destination_router_id = None
                                    self.lsa_ia_options = Bits()
                                    self._segment_path = lambda: "ia-router"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter, ['metric', 'destination_router_id', 'lsa_ia_options'], name, value)


                            class LsaExternal(Entity):
                                """
                                OSPFv3 LSA external
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: flags
                                
                                	LSA Flags
                                	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags>`
                                
                                .. attribute:: referenced_ls_type
                                
                                	Referenced Link State type
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: external_prefix
                                
                                	Prefix
                                	**type**\: str
                                
                                .. attribute:: external_prefix_options
                                
                                	Prefix options
                                	**type**\: str
                                
                                .. attribute:: forwarding_address
                                
                                	Forwarding address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
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

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal, self).__init__()

                                    self.yang_name = "lsa-external"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                        ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                        ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                        ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                        ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                        ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                    ])
                                    self.metric = None
                                    self.referenced_ls_type = None
                                    self.external_prefix = None
                                    self.external_prefix_options = None
                                    self.forwarding_address = None
                                    self.external_route_tag = None
                                    self.referenced_link_state_id = None

                                    self.flags = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags()
                                    self.flags.parent = self
                                    self._children_name_map["flags"] = "flags"
                                    self._children_yang_names.add("flags")
                                    self._segment_path = lambda: "lsa-external"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                class Flags(Entity):
                                    """
                                    LSA Flags
                                    
                                    .. attribute:: e_flag
                                    
                                    	When set, the metric specified is a Type 2 external metric
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags, self).__init__()

                                        self.yang_name = "flags"
                                        self.yang_parent_name = "lsa-external"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                        ])
                                        self.e_flag = None
                                        self._segment_path = lambda: "flags"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags, ['e_flag'], name, value)


                            class Nssa(Entity):
                                """
                                OSPFv3 NSSA
                                
                                .. attribute:: lsa_nssa_external
                                
                                	NSSA LSA
                                	**type**\:  :py:class:`LsaNssaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa, self).__init__()

                                    self.yang_name = "nssa"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal()
                                    self.lsa_nssa_external.parent = self
                                    self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                    self._children_yang_names.add("lsa-nssa-external")
                                    self._segment_path = lambda: "nssa"


                                class LsaNssaExternal(Entity):
                                    """
                                    NSSA LSA
                                    
                                    .. attribute:: metric
                                    
                                    	Metric
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: flags
                                    
                                    	LSA Flags
                                    	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags>`
                                    
                                    .. attribute:: referenced_ls_type
                                    
                                    	Referenced Link State type
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: external_prefix
                                    
                                    	Prefix
                                    	**type**\: str
                                    
                                    .. attribute:: external_prefix_options
                                    
                                    	Prefix options
                                    	**type**\: str
                                    
                                    .. attribute:: forwarding_address
                                    
                                    	Forwarding address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
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

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                        self.yang_name = "lsa-nssa-external"
                                        self.yang_parent_name = "nssa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric', YLeaf(YType.uint32, 'metric')),
                                            ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                            ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                            ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                            ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                            ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                            ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                        ])
                                        self.metric = None
                                        self.referenced_ls_type = None
                                        self.external_prefix = None
                                        self.external_prefix_options = None
                                        self.forwarding_address = None
                                        self.external_route_tag = None
                                        self.referenced_link_state_id = None

                                        self.flags = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags()
                                        self.flags.parent = self
                                        self._children_name_map["flags"] = "flags"
                                        self._children_yang_names.add("flags")
                                        self._segment_path = lambda: "lsa-nssa-external"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                    class Flags(Entity):
                                        """
                                        LSA Flags
                                        
                                        .. attribute:: e_flag
                                        
                                        	When set, the metric specified is a Type 2 external metric
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                            self.yang_name = "flags"
                                            self.yang_parent_name = "lsa-nssa-external"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                            ])
                                            self.e_flag = None
                                            self._segment_path = lambda: "flags"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags, ['e_flag'], name, value)


                            class LinkData(Entity):
                                """
                                OSPFv3 Link data
                                
                                .. attribute:: rtr_priority
                                
                                	Router priority of the interce
                                	**type**\: int
                                
                                	**range:** 0..255
                                
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
                                
                                .. attribute:: lsa_id_options
                                
                                	Link data LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData, self).__init__()

                                    self.yang_name = "link-data"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('rtr_priority', YLeaf(YType.uint8, 'rtr-priority')),
                                        ('link_local_interface_address', YLeaf(YType.str, 'link-local-interface-address')),
                                        ('num_of_prefixes', YLeaf(YType.uint32, 'num-of-prefixes')),
                                        ('lsa_id_options', YLeaf(YType.bits, 'lsa-id-options')),
                                    ])
                                    self.rtr_priority = None
                                    self.link_local_interface_address = None
                                    self.num_of_prefixes = None
                                    self.lsa_id_options = Bits()
                                    self._segment_path = lambda: "link-data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData, ['rtr_priority', 'link_local_interface_address', 'num_of_prefixes', 'lsa_id_options'], name, value)


                            class IaPrefix(Entity):
                                """
                                OSPFv3 Intra area prefixes
                                
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
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: num_of_prefixes
                                
                                	Number of prefixes
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix, self).__init__()

                                    self.yang_name = "ia-prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                        ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                        ('referenced_adv_router', YLeaf(YType.str, 'referenced-adv-router')),
                                        ('num_of_prefixes', YLeaf(YType.uint16, 'num-of-prefixes')),
                                    ])
                                    self.referenced_ls_type = None
                                    self.referenced_link_state_id = None
                                    self.referenced_adv_router = None
                                    self.num_of_prefixes = None
                                    self._segment_path = lambda: "ia-prefix"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                    class Ospfv3Link(Entity):
                        """
                        OSPFv3 links
                        
                        .. attribute:: interface_id  (key)
                        
                        	Interface ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor_interface_id  (key)
                        
                        	Neighbor interface ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor_router_id  (key)
                        
                        	Neighbor router ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Link type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3Link, self).__init__()

                            self.yang_name = "ospfv3-link"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_id', YLeaf(YType.uint32, 'interface-id')),
                                ('neighbor_interface_id', YLeaf(YType.uint32, 'neighbor-interface-id')),
                                ('neighbor_router_id', YLeaf(YType.uint32, 'neighbor-router-id')),
                                ('type', YLeaf(YType.uint8, 'type')),
                                ('metric', YLeaf(YType.uint16, 'metric')),
                            ])
                            self.interface_id = None
                            self.neighbor_interface_id = None
                            self.neighbor_router_id = None
                            self.type = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                    class Ospfv3PrefixList(Entity):
                        """
                        OSPFv3 prefix\-list
                        
                        .. attribute:: prefix  (key)
                        
                        	Prefix
                        	**type**\: str
                        
                        .. attribute:: prefix_options
                        
                        	Prefix options
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList, self).__init__()

                            self.yang_name = "ospfv3-prefix-list"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['prefix']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', YLeaf(YType.str, 'prefix')),
                                ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                            ])
                            self.prefix = None
                            self.prefix_options = None
                            self._segment_path = lambda: "ospfv3-prefix-list" + "[prefix='" + str(self.prefix) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList, ['prefix', 'prefix_options'], name, value)


                    class Ospfv3IaPrefix(Entity):
                        """
                        OSPFv3 intra\-area prefix\-list
                        
                        .. attribute:: prefix  (key)
                        
                        	Prefix
                        	**type**\: str
                        
                        .. attribute:: prefix_options
                        
                        	Prefix options
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix, self).__init__()

                            self.yang_name = "ospfv3-ia-prefix"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['prefix']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', YLeaf(YType.str, 'prefix')),
                                ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                            ])
                            self.prefix = None
                            self.prefix_options = None
                            self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix, ['prefix', 'prefix_options'], name, value)


                    class MultiTopology(Entity):
                        """
                        OSPF multi\-topology interface augmentation
                        
                        .. attribute:: name  (key)
                        
                        	One of the topology enabled on this interface
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.MultiTopology, self).__init__()

                            self.yang_name = "multi-topology"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', YLeaf(YType.str, 'name')),
                            ])
                            self.name = None
                            self._segment_path = lambda: "multi-topology" + "[name='" + str(self.name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.MultiTopology, ['name'], name, value)


                    class Tlv(Entity):
                        """
                        Link TLV
                        
                        .. attribute:: link_type
                        
                        	Link type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: link_id
                        
                        	Link ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_if_ipv4_addr
                        
                        	List of local interface IPv4 addresses
                        	**type**\: union of the below types:
                        
                        		**type**\: list of str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: list of str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: local_remote_ipv4_addr
                        
                        	List of remote interface IPv4 addresses
                        	**type**\: union of the below types:
                        
                        		**type**\: list of str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: list of str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
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
                        
                        	Unrseerved bandwidth
                        	**type**\: :py:class:`Decimal64<ydk.types.Decimal64>`
                        
                        	**range:** \-92233720368547758.08..92233720368547758.07
                        
                        .. attribute:: admin_group
                        
                        	Administrative group/Resource class/Color
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv, self).__init__()

                            self.yang_name = "tlv"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('link_type', YLeaf(YType.uint8, 'link-type')),
                                ('link_id', YLeaf(YType.uint32, 'link-id')),
                                ('local_if_ipv4_addr', YLeafList(YType.str, 'local-if-ipv4-addr')),
                                ('local_remote_ipv4_addr', YLeafList(YType.str, 'local-remote-ipv4-addr')),
                                ('te_metric', YLeaf(YType.uint32, 'te-metric')),
                                ('max_bandwidth', YLeaf(YType.str, 'max-bandwidth')),
                                ('max_reservable_bandwidth', YLeaf(YType.str, 'max-reservable-bandwidth')),
                                ('unreserved_bandwidth', YLeaf(YType.str, 'unreserved-bandwidth')),
                                ('admin_group', YLeaf(YType.uint32, 'admin-group')),
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
                            self._segment_path = lambda: "tlv"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv, ['link_type', 'link_id', 'local_if_ipv4_addr', 'local_remote_ipv4_addr', 'te_metric', 'max_bandwidth', 'max_reservable_bandwidth', 'unreserved_bandwidth', 'admin_group'], name, value)


                    class UnknownSubTlv(Entity):
                        """
                        OSPFv2 Unknown sub TLV
                        
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
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.UnknownSubTlv, self).__init__()

                            self.yang_name = "unknown-sub-tlv"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', YLeaf(YType.uint16, 'type')),
                                ('length', YLeaf(YType.uint16, 'length')),
                                ('value', YLeafList(YType.uint8, 'value')),
                            ])
                            self.type = None
                            self.length = None
                            self.value = []
                            self._segment_path = lambda: "unknown-sub-tlv" + "[type='" + str(self.type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.UnknownSubTlv, ['type', 'length', 'value'], name, value)


                class AreaScopeLsa(Entity):
                    """
                    List OSPF area scope LSA databases
                    
                    .. attribute:: lsa_type  (key)
                    
                    	LSA Type
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: adv_router  (key)
                    
                    	Advertising router
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: decoded_completed
                    
                    	The OSPF LSA body is fully decoded
                    	**type**\: bool
                    
                    .. attribute:: raw_data
                    
                    	The complete LSA in network byte order as received/sent over the wire
                    	**type**\: list of int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ospfv2_lsa
                    
                    	OSPFv2 LSA
                    	**type**\:  :py:class:`Ospfv2Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa>`
                    
                    .. attribute:: ospfv2_link
                    
                    	Router LSA link
                    	**type**\: list of  		 :py:class:`Ospfv2Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link>`
                    
                    .. attribute:: ospfv2_topology
                    
                    	Summary LSA
                    	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Topology>`
                    
                    .. attribute:: ospfv2_external
                    
                    	External LSA
                    	**type**\: list of  		 :py:class:`Ospfv2External <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2External>`
                    
                    .. attribute:: ospfv3_lsa
                    
                    	OSPFv3 LSA
                    	**type**\:  :py:class:`Ospfv3Lsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa>`
                    
                    .. attribute:: ospfv3_link
                    
                    	OSPFv3 links
                    	**type**\: list of  		 :py:class:`Ospfv3Link <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Link>`
                    
                    .. attribute:: ospfv3_prefix
                    
                    	OSPFv3 prefix\-list
                    	**type**\: list of  		 :py:class:`Ospfv3Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Prefix>`
                    
                    .. attribute:: ospfv3_ia_prefix
                    
                    	OSPFv3 intra\-area prefix\-list
                    	**type**\: list of  		 :py:class:`Ospfv3IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2017-10-10'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa, self).__init__()

                        self.yang_name = "area-scope-lsa"
                        self.yang_parent_name = "link-scope-lsas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsa_type','adv_router']
                        self._child_container_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa)), ("ospfv3-lsa", ("ospfv3_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa))])
                        self._child_list_classes = OrderedDict([("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2External)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Link)), ("ospfv3-prefix", ("ospfv3_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Prefix)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix))])
                        self._leafs = OrderedDict([
                            ('lsa_type', YLeaf(YType.uint32, 'lsa-type')),
                            ('adv_router', YLeaf(YType.str, 'adv-router')),
                            ('decoded_completed', YLeaf(YType.boolean, 'decoded-completed')),
                            ('raw_data', YLeafList(YType.uint8, 'raw-data')),
                        ])
                        self.lsa_type = None
                        self.adv_router = None
                        self.decoded_completed = None
                        self.raw_data = []

                        self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa()
                        self.ospfv2_lsa.parent = self
                        self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"
                        self._children_yang_names.add("ospfv2-lsa")

                        self.ospfv3_lsa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa()
                        self.ospfv3_lsa.parent = self
                        self._children_name_map["ospfv3_lsa"] = "ospfv3-lsa"
                        self._children_yang_names.add("ospfv3-lsa")

                        self.ospfv2_link = YList(self)
                        self.ospfv2_topology = YList(self)
                        self.ospfv2_external = YList(self)
                        self.ospfv3_link = YList(self)
                        self.ospfv3_prefix = YList(self)
                        self.ospfv3_ia_prefix = YList(self)
                        self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']" + "[adv-router='" + str(self.adv_router) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa, ['lsa_type', 'adv_router', 'decoded_completed', 'raw_data'], name, value)


                    class Ospfv2Lsa(Entity):
                        """
                        OSPFv2 LSA
                        
                        .. attribute:: header
                        
                        	Decoded OSPFv2 LSA header data
                        	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header>`
                        
                        .. attribute:: lsa_body
                        
                        	Decoded OSPFv2 LSA body data
                        	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa, self).__init__()

                            self.yang_name = "ospfv2-lsa"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"
                            self._children_yang_names.add("header")

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._children_yang_names.add("lsa-body")
                            self._segment_path = lambda: "ospfv2-lsa"


                        class Header(Entity):
                            """
                            Decoded OSPFv2 LSA header data
                            
                            .. attribute:: lsa_id
                            
                            	LSA ID
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: opaque_type
                            
                            	Opaque type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: opaque_id
                            
                            	Opaque ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: age
                            
                            	LSA age
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: type
                            
                            	LSA type
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: adv_router
                            
                            	LSA advertising router
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seq_num
                            
                            	LSA sequence number
                            	**type**\: str
                            
                            .. attribute:: checksum
                            
                            	LSA checksum
                            	**type**\: str
                            
                            .. attribute:: length
                            
                            	LSA length
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: flag_options
                            
                            	LSA options
                            	**type**\:  :py:class:`LsaFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.LsaFlagOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                    ('opaque_type', YLeaf(YType.uint8, 'opaque-type')),
                                    ('opaque_id', YLeaf(YType.uint32, 'opaque-id')),
                                    ('age', YLeaf(YType.uint16, 'age')),
                                    ('type', YLeaf(YType.uint16, 'type')),
                                    ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                    ('seq_num', YLeaf(YType.str, 'seq-num')),
                                    ('checksum', YLeaf(YType.str, 'checksum')),
                                    ('length', YLeaf(YType.uint16, 'length')),
                                    ('flag_options', YLeaf(YType.bits, 'flag-options')),
                                ])
                                self.lsa_id = None
                                self.opaque_type = None
                                self.opaque_id = None
                                self.age = None
                                self.type = None
                                self.adv_router = None
                                self.seq_num = None
                                self.checksum = None
                                self.length = None
                                self.flag_options = Bits()
                                self._segment_path = lambda: "header"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header, ['lsa_id', 'opaque_type', 'opaque_id', 'age', 'type', 'adv_router', 'seq_num', 'checksum', 'length', 'flag_options'], name, value)


                        class LsaBody(Entity):
                            """
                            Decoded OSPFv2 LSA body data
                            
                            .. attribute:: num_of_links
                            
                            	Number of links
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: network
                            
                            	Network details
                            	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network>`
                            
                            .. attribute:: summary_mask
                            
                            	Summary mask
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: external_mask
                            
                            	External mask
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: body_flag_options
                            
                            	LSA body flags
                            	**type**\:  :py:class:`Ospfv2LsaBodyFlagsOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2LsaBodyFlagsOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('num_of_links', YLeaf(YType.uint16, 'num-of-links')),
                                    ('summary_mask', YLeaf(YType.str, 'summary-mask')),
                                    ('external_mask', YLeaf(YType.str, 'external-mask')),
                                    ('body_flag_options', YLeaf(YType.bits, 'body-flag-options')),
                                ])
                                self.num_of_links = None
                                self.summary_mask = None
                                self.external_mask = None
                                self.body_flag_options = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"
                                self._children_yang_names.add("network")
                                self._segment_path = lambda: "lsa-body"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody, ['num_of_links', 'summary_mask', 'external_mask', 'body_flag_options'], name, value)


                            class Network(Entity):
                                """
                                Network details
                                
                                .. attribute:: network_mask
                                
                                	IP network mask
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: attached_router
                                
                                	List of the routers attached to the network
                                	**type**\: list of int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('network_mask', YLeaf(YType.str, 'network-mask')),
                                        ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                    ])
                                    self.network_mask = None
                                    self.attached_router = []
                                    self._segment_path = lambda: "network"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network, ['network_mask', 'attached_router'], name, value)


                    class Ospfv2Link(Entity):
                        """
                        Router LSA link
                        
                        .. attribute:: link_id  (key)
                        
                        	Link ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: link_data  (key)
                        
                        	Link data
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Link type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: ospfv2_topology
                        
                        	Topology specific information
                        	**type**\: list of  		 :py:class:`Ospfv2Topology <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link, self).__init__()

                            self.yang_name = "ospfv2-link"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['link_id','link_data']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology))])
                            self._leafs = OrderedDict([
                                ('link_id', YLeaf(YType.uint32, 'link-id')),
                                ('link_data', YLeaf(YType.uint32, 'link-data')),
                                ('type', YLeaf(YType.uint8, 'type')),
                            ])
                            self.link_id = None
                            self.link_data = None
                            self.type = None

                            self.ospfv2_topology = YList(self)
                            self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link, ['link_id', 'link_data', 'type'], name, value)


                        class Ospfv2Topology(Entity):
                            """
                            Topology specific information
                            
                            .. attribute:: mt_id  (key)
                            
                            	MT\-ID for topology enabled link
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: metric
                            
                            	Metric for the topology
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                self.yang_name = "ospfv2-topology"
                                self.yang_parent_name = "ospfv2-link"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                    ('metric', YLeaf(YType.uint16, 'metric')),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                    class Ospfv2Topology(Entity):
                        """
                        Summary LSA
                        
                        .. attribute:: mt_id  (key)
                        
                        	MT\-ID for topology enabled link
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: metric
                        
                        	Metric for the topology
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Topology, self).__init__()

                            self.yang_name = "ospfv2-topology"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                ('metric', YLeaf(YType.uint16, 'metric')),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Topology, ['mt_id', 'metric'], name, value)


                    class Ospfv2External(Entity):
                        """
                        External LSA
                        
                        .. attribute:: mt_id  (key)
                        
                        	MT\-ID for topology enabled on the link
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: metric
                        
                        	Metric for the topology
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: forwarding_address
                        
                        	Forwarding address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: external_route_tag
                        
                        	Route tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2External, self).__init__()

                            self.yang_name = "ospfv2-external"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', YLeaf(YType.uint32, 'mt-id')),
                                ('metric', YLeaf(YType.uint32, 'metric')),
                                ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self.forwarding_address = None
                            self.external_route_tag = None
                            self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2External, ['mt_id', 'metric', 'forwarding_address', 'external_route_tag'], name, value)


                    class Ospfv3Lsa(Entity):
                        """
                        OSPFv3 LSA
                        
                        .. attribute:: header
                        
                        	Decoded OSPFv3 LSA header
                        	**type**\:  :py:class:`Header <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header>`
                        
                        .. attribute:: lsa_body
                        
                        	Decoded OSPFv3 LSA body
                        	**type**\:  :py:class:`LsaBody <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa, self).__init__()

                            self.yang_name = "ospfv3-lsa"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"
                            self._children_yang_names.add("header")

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._children_yang_names.add("lsa-body")
                            self._segment_path = lambda: "ospfv3-lsa"


                        class Header(Entity):
                            """
                            Decoded OSPFv3 LSA header
                            
                            .. attribute:: lsa_id
                            
                            	LSA ID
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: lsa_header
                            
                            	LSA header
                            	**type**\:  :py:class:`LsaHeader <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader>`
                            
                            .. attribute:: lsa_hdr_options
                            
                            	OSPFv3 LSA options
                            	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv3-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_id', YLeaf(YType.str, 'lsa-id')),
                                    ('lsa_hdr_options', YLeaf(YType.bits, 'lsa-hdr-options')),
                                ])
                                self.lsa_id = None
                                self.lsa_hdr_options = Bits()

                                self.lsa_header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader()
                                self.lsa_header.parent = self
                                self._children_name_map["lsa_header"] = "lsa-header"
                                self._children_yang_names.add("lsa-header")
                                self._segment_path = lambda: "header"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header, ['lsa_id', 'lsa_hdr_options'], name, value)


                            class LsaHeader(Entity):
                                """
                                LSA header
                                
                                .. attribute:: age
                                
                                	LSA age
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: type
                                
                                	LSA type
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: adv_router
                                
                                	LSA advertising router
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: seq_num
                                
                                	LSA sequence number
                                	**type**\: str
                                
                                .. attribute:: checksum
                                
                                	LSA checksum
                                	**type**\: str
                                
                                .. attribute:: length
                                
                                	LSA length
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader, self).__init__()

                                    self.yang_name = "lsa-header"
                                    self.yang_parent_name = "header"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('age', YLeaf(YType.uint16, 'age')),
                                        ('type', YLeaf(YType.uint16, 'type')),
                                        ('adv_router', YLeaf(YType.uint32, 'adv-router')),
                                        ('seq_num', YLeaf(YType.str, 'seq-num')),
                                        ('checksum', YLeaf(YType.str, 'checksum')),
                                        ('length', YLeaf(YType.uint16, 'length')),
                                    ])
                                    self.age = None
                                    self.type = None
                                    self.adv_router = None
                                    self.seq_num = None
                                    self.checksum = None
                                    self.length = None
                                    self._segment_path = lambda: "lsa-header"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader, ['age', 'type', 'adv_router', 'seq_num', 'checksum', 'length'], name, value)


                        class LsaBody(Entity):
                            """
                            Decoded OSPFv3 LSA body
                            
                            .. attribute:: network
                            
                            	OSPFv3 network
                            	**type**\:  :py:class:`Network <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network>`
                            
                            .. attribute:: prefix
                            
                            	OSPFv3 inter area prefix
                            	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix>`
                            
                            .. attribute:: ia_router
                            
                            	OSPFv3 inter area router
                            	**type**\:  :py:class:`IaRouter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter>`
                            
                            .. attribute:: lsa_external
                            
                            	OSPFv3 LSA external
                            	**type**\:  :py:class:`LsaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal>`
                            
                            .. attribute:: nssa
                            
                            	OSPFv3 NSSA
                            	**type**\:  :py:class:`Nssa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa>`
                            
                            .. attribute:: link_data
                            
                            	OSPFv3 Link data
                            	**type**\:  :py:class:`LinkData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData>`
                            
                            .. attribute:: ia_prefix
                            
                            	OSPFv3 Intra area prefixes
                            	**type**\:  :py:class:`IaPrefix <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix>`
                            
                            .. attribute:: lsa_flag_options
                            
                            	LSA options
                            	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                            
                            .. attribute:: lsa_body_flags
                            
                            	LSA Body Flags
                            	**type**\:  :py:class:`Ospfv3LsaBodyFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaBodyFlagOptions>`
                            
                            

                            """

                            _prefix = 'ospf-ios-xe-oper'
                            _revision = '2017-10-10'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv3-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_flag_options', YLeaf(YType.bits, 'lsa-flag-options')),
                                    ('lsa_body_flags', YLeaf(YType.bits, 'lsa-body-flags')),
                                ])
                                self.lsa_flag_options = Bits()
                                self.lsa_body_flags = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"
                                self._children_yang_names.add("network")

                                self.prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix()
                                self.prefix.parent = self
                                self._children_name_map["prefix"] = "prefix"
                                self._children_yang_names.add("prefix")

                                self.ia_router = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter()
                                self.ia_router.parent = self
                                self._children_name_map["ia_router"] = "ia-router"
                                self._children_yang_names.add("ia-router")

                                self.lsa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal()
                                self.lsa_external.parent = self
                                self._children_name_map["lsa_external"] = "lsa-external"
                                self._children_yang_names.add("lsa-external")

                                self.nssa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa()
                                self.nssa.parent = self
                                self._children_name_map["nssa"] = "nssa"
                                self._children_yang_names.add("nssa")

                                self.link_data = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData()
                                self.link_data.parent = self
                                self._children_name_map["link_data"] = "link-data"
                                self._children_yang_names.add("link-data")

                                self.ia_prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix()
                                self.ia_prefix.parent = self
                                self._children_name_map["ia_prefix"] = "ia-prefix"
                                self._children_yang_names.add("ia-prefix")
                                self._segment_path = lambda: "lsa-body"

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody, ['lsa_flag_options', 'lsa_body_flags'], name, value)


                            class Network(Entity):
                                """
                                OSPFv3 network
                                
                                .. attribute:: attached_router
                                
                                	List of the routers attached to the network
                                	**type**\: list of int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lsa_net_options
                                
                                	Network LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('attached_router', YLeafList(YType.uint32, 'attached-router')),
                                        ('lsa_net_options', YLeaf(YType.bits, 'lsa-net-options')),
                                    ])
                                    self.attached_router = []
                                    self.lsa_net_options = Bits()
                                    self._segment_path = lambda: "network"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network, ['attached_router', 'lsa_net_options'], name, value)


                            class Prefix(Entity):
                                """
                                OSPFv3 inter area prefix
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ia_prefix
                                
                                	Inter area Prefix
                                	**type**\: str
                                
                                .. attribute:: ia_prefix_options
                                
                                	Inter area prefix options
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('ia_prefix', YLeaf(YType.str, 'ia-prefix')),
                                        ('ia_prefix_options', YLeaf(YType.str, 'ia-prefix-options')),
                                    ])
                                    self.metric = None
                                    self.ia_prefix = None
                                    self.ia_prefix_options = None
                                    self._segment_path = lambda: "prefix"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix, ['metric', 'ia_prefix', 'ia_prefix_options'], name, value)


                            class IaRouter(Entity):
                                """
                                OSPFv3 inter area router
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: destination_router_id
                                
                                	Router ID of the router being described by the LSA
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lsa_ia_options
                                
                                	Inter area LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter, self).__init__()

                                    self.yang_name = "ia-router"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('destination_router_id', YLeaf(YType.uint32, 'destination-router-id')),
                                        ('lsa_ia_options', YLeaf(YType.bits, 'lsa-ia-options')),
                                    ])
                                    self.metric = None
                                    self.destination_router_id = None
                                    self.lsa_ia_options = Bits()
                                    self._segment_path = lambda: "ia-router"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter, ['metric', 'destination_router_id', 'lsa_ia_options'], name, value)


                            class LsaExternal(Entity):
                                """
                                OSPFv3 LSA external
                                
                                .. attribute:: metric
                                
                                	Metric
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: flags
                                
                                	LSA Flags
                                	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags>`
                                
                                .. attribute:: referenced_ls_type
                                
                                	Referenced Link State type
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: external_prefix
                                
                                	Prefix
                                	**type**\: str
                                
                                .. attribute:: external_prefix_options
                                
                                	Prefix options
                                	**type**\: str
                                
                                .. attribute:: forwarding_address
                                
                                	Forwarding address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
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

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal, self).__init__()

                                    self.yang_name = "lsa-external"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', YLeaf(YType.uint32, 'metric')),
                                        ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                        ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                        ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                        ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                        ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                        ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                    ])
                                    self.metric = None
                                    self.referenced_ls_type = None
                                    self.external_prefix = None
                                    self.external_prefix_options = None
                                    self.forwarding_address = None
                                    self.external_route_tag = None
                                    self.referenced_link_state_id = None

                                    self.flags = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags()
                                    self.flags.parent = self
                                    self._children_name_map["flags"] = "flags"
                                    self._children_yang_names.add("flags")
                                    self._segment_path = lambda: "lsa-external"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                class Flags(Entity):
                                    """
                                    LSA Flags
                                    
                                    .. attribute:: e_flag
                                    
                                    	When set, the metric specified is a Type 2 external metric
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags, self).__init__()

                                        self.yang_name = "flags"
                                        self.yang_parent_name = "lsa-external"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                        ])
                                        self.e_flag = None
                                        self._segment_path = lambda: "flags"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags, ['e_flag'], name, value)


                            class Nssa(Entity):
                                """
                                OSPFv3 NSSA
                                
                                .. attribute:: lsa_nssa_external
                                
                                	NSSA LSA
                                	**type**\:  :py:class:`LsaNssaExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa, self).__init__()

                                    self.yang_name = "nssa"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict()

                                    self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal()
                                    self.lsa_nssa_external.parent = self
                                    self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                    self._children_yang_names.add("lsa-nssa-external")
                                    self._segment_path = lambda: "nssa"


                                class LsaNssaExternal(Entity):
                                    """
                                    NSSA LSA
                                    
                                    .. attribute:: metric
                                    
                                    	Metric
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: flags
                                    
                                    	LSA Flags
                                    	**type**\:  :py:class:`Flags <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags>`
                                    
                                    .. attribute:: referenced_ls_type
                                    
                                    	Referenced Link State type
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: external_prefix
                                    
                                    	Prefix
                                    	**type**\: str
                                    
                                    .. attribute:: external_prefix_options
                                    
                                    	Prefix options
                                    	**type**\: str
                                    
                                    .. attribute:: forwarding_address
                                    
                                    	Forwarding address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
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

                                    _prefix = 'ospf-ios-xe-oper'
                                    _revision = '2017-10-10'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                        self.yang_name = "lsa-nssa-external"
                                        self.yang_parent_name = "nssa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric', YLeaf(YType.uint32, 'metric')),
                                            ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                            ('external_prefix', YLeaf(YType.str, 'external-prefix')),
                                            ('external_prefix_options', YLeaf(YType.str, 'external-prefix-options')),
                                            ('forwarding_address', YLeaf(YType.str, 'forwarding-address')),
                                            ('external_route_tag', YLeaf(YType.uint32, 'external-route-tag')),
                                            ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                        ])
                                        self.metric = None
                                        self.referenced_ls_type = None
                                        self.external_prefix = None
                                        self.external_prefix_options = None
                                        self.forwarding_address = None
                                        self.external_route_tag = None
                                        self.referenced_link_state_id = None

                                        self.flags = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags()
                                        self.flags.parent = self
                                        self._children_name_map["flags"] = "flags"
                                        self._children_yang_names.add("flags")
                                        self._segment_path = lambda: "lsa-nssa-external"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, ['metric', 'referenced_ls_type', 'external_prefix', 'external_prefix_options', 'forwarding_address', 'external_route_tag', 'referenced_link_state_id'], name, value)


                                    class Flags(Entity):
                                        """
                                        LSA Flags
                                        
                                        .. attribute:: e_flag
                                        
                                        	When set, the metric specified is a Type 2 external metric
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'ospf-ios-xe-oper'
                                        _revision = '2017-10-10'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                            self.yang_name = "flags"
                                            self.yang_parent_name = "lsa-nssa-external"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('e_flag', YLeaf(YType.boolean, 'e-flag')),
                                            ])
                                            self.e_flag = None
                                            self._segment_path = lambda: "flags"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, ['e_flag'], name, value)


                            class LinkData(Entity):
                                """
                                OSPFv3 Link data
                                
                                .. attribute:: rtr_priority
                                
                                	Router priority of the interce
                                	**type**\: int
                                
                                	**range:** 0..255
                                
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
                                
                                .. attribute:: lsa_id_options
                                
                                	Link data LSA options
                                	**type**\:  :py:class:`Ospfv3LsaOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv3LsaOptions>`
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData, self).__init__()

                                    self.yang_name = "link-data"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('rtr_priority', YLeaf(YType.uint8, 'rtr-priority')),
                                        ('link_local_interface_address', YLeaf(YType.str, 'link-local-interface-address')),
                                        ('num_of_prefixes', YLeaf(YType.uint32, 'num-of-prefixes')),
                                        ('lsa_id_options', YLeaf(YType.bits, 'lsa-id-options')),
                                    ])
                                    self.rtr_priority = None
                                    self.link_local_interface_address = None
                                    self.num_of_prefixes = None
                                    self.lsa_id_options = Bits()
                                    self._segment_path = lambda: "link-data"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData, ['rtr_priority', 'link_local_interface_address', 'num_of_prefixes', 'lsa_id_options'], name, value)


                            class IaPrefix(Entity):
                                """
                                OSPFv3 Intra area prefixes
                                
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
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: num_of_prefixes
                                
                                	Number of prefixes
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ospf-ios-xe-oper'
                                _revision = '2017-10-10'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix, self).__init__()

                                    self.yang_name = "ia-prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('referenced_ls_type', YLeaf(YType.uint16, 'referenced-ls-type')),
                                        ('referenced_link_state_id', YLeaf(YType.uint32, 'referenced-link-state-id')),
                                        ('referenced_adv_router', YLeaf(YType.str, 'referenced-adv-router')),
                                        ('num_of_prefixes', YLeaf(YType.uint16, 'num-of-prefixes')),
                                    ])
                                    self.referenced_ls_type = None
                                    self.referenced_link_state_id = None
                                    self.referenced_adv_router = None
                                    self.num_of_prefixes = None
                                    self._segment_path = lambda: "ia-prefix"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix, ['referenced_ls_type', 'referenced_link_state_id', 'referenced_adv_router', 'num_of_prefixes'], name, value)


                    class Ospfv3Link(Entity):
                        """
                        OSPFv3 links
                        
                        .. attribute:: interface_id  (key)
                        
                        	Interface ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor_interface_id  (key)
                        
                        	Neighbor interface ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor_router_id  (key)
                        
                        	Neighbor router ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Link type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: metric
                        
                        	Metric
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Link, self).__init__()

                            self.yang_name = "ospfv3-link"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_id', YLeaf(YType.uint32, 'interface-id')),
                                ('neighbor_interface_id', YLeaf(YType.uint32, 'neighbor-interface-id')),
                                ('neighbor_router_id', YLeaf(YType.uint32, 'neighbor-router-id')),
                                ('type', YLeaf(YType.uint8, 'type')),
                                ('metric', YLeaf(YType.uint16, 'metric')),
                            ])
                            self.interface_id = None
                            self.neighbor_interface_id = None
                            self.neighbor_router_id = None
                            self.type = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Link, ['interface_id', 'neighbor_interface_id', 'neighbor_router_id', 'type', 'metric'], name, value)


                    class Ospfv3Prefix(Entity):
                        """
                        OSPFv3 prefix\-list
                        
                        .. attribute:: prefix  (key)
                        
                        	Prefix
                        	**type**\: str
                        
                        .. attribute:: prefix_options
                        
                        	Prefix options
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Prefix, self).__init__()

                            self.yang_name = "ospfv3-prefix"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['prefix']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', YLeaf(YType.str, 'prefix')),
                                ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                            ])
                            self.prefix = None
                            self.prefix_options = None
                            self._segment_path = lambda: "ospfv3-prefix" + "[prefix='" + str(self.prefix) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Prefix, ['prefix', 'prefix_options'], name, value)


                    class Ospfv3IaPrefix(Entity):
                        """
                        OSPFv3 intra\-area prefix\-list
                        
                        .. attribute:: prefix  (key)
                        
                        	Prefix
                        	**type**\: str
                        
                        .. attribute:: prefix_options
                        
                        	Prefix options
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2017-10-10'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix, self).__init__()

                            self.yang_name = "ospfv3-ia-prefix"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['prefix']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('prefix', YLeaf(YType.str, 'prefix')),
                                ('prefix_options', YLeaf(YType.str, 'prefix-options')),
                            ])
                            self.prefix = None
                            self.prefix_options = None
                            self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix, ['prefix', 'prefix_options'], name, value)


            class MultiTopology(Entity):
                """
                OSPF multi\-topology interface augmentation
                
                .. attribute:: name  (key)
                
                	One of the topology enabled on this interface
                	**type**\: str
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2017-10-10'

                def __init__(self):
                    super(OspfOperData.OspfState.OspfInstance.MultiTopology, self).__init__()

                    self.yang_name = "multi-topology"
                    self.yang_parent_name = "ospf-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', YLeaf(YType.str, 'name')),
                    ])
                    self.name = None
                    self._segment_path = lambda: "multi-topology" + "[name='" + str(self.name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.MultiTopology, ['name'], name, value)

    def clone_ptr(self):
        self._top_entity = OspfOperData()
        return self._top_entity

