""" Cisco_IOS_XE_ospf_oper 

This module contains a collection of YANG definitions for
monitoring the operation of ospf protocol in a Network Element.
Copyright (c) 2016\-2018 by Cisco Systems, Inc.
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


class OspfExternalMetricType(Enum):
    """
    OspfExternalMetricType (Enum Class)

    External metric type

    .. data:: ospf_ext_metric_type_1 = 0

    .. data:: ospf_ext_metric_type_2 = 1

    """

    ospf_ext_metric_type_1 = Enum.YLeaf(0, "ospf-ext-metric-type-1")

    ospf_ext_metric_type_2 = Enum.YLeaf(1, "ospf-ext-metric-type-2")


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


class Ospfv2AuthTypeSelection(Enum):
    """
    Ospfv2AuthTypeSelection (Enum Class)

    The authentication type

    .. data:: ospfv2_auth_none = 0

    	No authentication configured

    .. data:: ospfv2_auth_trailer_key = 1

    	Authentication uses the trailer key

    .. data:: ospfv2_auth_trailer_key_chain = 2

    	Authentication uses a trailer key chain

    """

    ospfv2_auth_none = Enum.YLeaf(0, "ospfv2-auth-none")

    ospfv2_auth_trailer_key = Enum.YLeaf(1, "ospfv2-auth-trailer-key")

    ospfv2_auth_trailer_key_chain = Enum.YLeaf(2, "ospfv2-auth-trailer-key-chain")


class Ospfv2CryptoAlgorithm(Enum):
    """
    Ospfv2CryptoAlgorithm (Enum Class)

    The algorithm in use

    .. data:: ospfv2_crypto_cleartest = 0

    	The OSPFv2 authentication is sent as cleartext

    .. data:: ospfv2_crypto_md5 = 1

    	The OSPFv2 authentication is encrypted using 

    	Message Digest 5

    """

    ospfv2_crypto_cleartest = Enum.YLeaf(0, "ospfv2-crypto-cleartest")

    ospfv2_crypto_md5 = Enum.YLeaf(1, "ospfv2-crypto-md5")


class Ospfv2IntfState(Enum):
    """
    Ospfv2IntfState (Enum Class)

    The possible states that an interface can be in

    .. data:: ospfv2_interface_state_down = 0

    	The interface is in the down state

    .. data:: ospfv2_interface_state_loopback = 1

    	The interface is in loopback state

    .. data:: ospfv2_interface_state_waiting = 2

    	The interface is in waiting state

    .. data:: ospfv2_interface_state_point_to_mpoint = 3

    	The interface is in point-to-multipoint state

    .. data:: ospfv2_interface_state_point_to_point = 4

    	The interface is in point-to-point state

    .. data:: ospfv2_interface_state_dr = 5

    	The interface is in the designated router state

    .. data:: ospfv2_interface_state_backup = 6

    	The interface is providing backup for another 

    	interface

    .. data:: ospfv2_interface_state_other = 7

    	The interface is in a state other than the ones

    	nummerated in this list

    """

    ospfv2_interface_state_down = Enum.YLeaf(0, "ospfv2-interface-state-down")

    ospfv2_interface_state_loopback = Enum.YLeaf(1, "ospfv2-interface-state-loopback")

    ospfv2_interface_state_waiting = Enum.YLeaf(2, "ospfv2-interface-state-waiting")

    ospfv2_interface_state_point_to_mpoint = Enum.YLeaf(3, "ospfv2-interface-state-point-to-mpoint")

    ospfv2_interface_state_point_to_point = Enum.YLeaf(4, "ospfv2-interface-state-point-to-point")

    ospfv2_interface_state_dr = Enum.YLeaf(5, "ospfv2-interface-state-dr")

    ospfv2_interface_state_backup = Enum.YLeaf(6, "ospfv2-interface-state-backup")

    ospfv2_interface_state_other = Enum.YLeaf(7, "ospfv2-interface-state-other")


class Ospfv2LsaType(Enum):
    """
    Ospfv2LsaType (Enum Class)

    Link State Advertisement type

    .. data:: ospfv2_lsa_type_unsupported_lsa_type = 0

    .. data:: ospfv2_lsa_type_router = 1

    .. data:: ospfv2_lsa_type_network = 2

    .. data:: ospfv2_lsa_type_summary_net = 3

    .. data:: ospfv2_lsa_type_summary_router = 4

    .. data:: ospfv2_lsa_type_as_external = 5

    .. data:: ospfv2_lsa_type_nssa = 6

    .. data:: ospfv2_lsa_type_link_scope_opaque = 7

    .. data:: ospfv2_lsa_type_area_scope_opaque = 8

    .. data:: ospfv2_lsa_type_as_scope_opaque = 9

    """

    ospfv2_lsa_type_unsupported_lsa_type = Enum.YLeaf(0, "ospfv2-lsa-type-unsupported-lsa-type")

    ospfv2_lsa_type_router = Enum.YLeaf(1, "ospfv2-lsa-type-router")

    ospfv2_lsa_type_network = Enum.YLeaf(2, "ospfv2-lsa-type-network")

    ospfv2_lsa_type_summary_net = Enum.YLeaf(3, "ospfv2-lsa-type-summary-net")

    ospfv2_lsa_type_summary_router = Enum.YLeaf(4, "ospfv2-lsa-type-summary-router")

    ospfv2_lsa_type_as_external = Enum.YLeaf(5, "ospfv2-lsa-type-as-external")

    ospfv2_lsa_type_nssa = Enum.YLeaf(6, "ospfv2-lsa-type-nssa")

    ospfv2_lsa_type_link_scope_opaque = Enum.YLeaf(7, "ospfv2-lsa-type-link-scope-opaque")

    ospfv2_lsa_type_area_scope_opaque = Enum.YLeaf(8, "ospfv2-lsa-type-area-scope-opaque")

    ospfv2_lsa_type_as_scope_opaque = Enum.YLeaf(9, "ospfv2-lsa-type-as-scope-opaque")



class OspfOperData(Entity):
    """
    Operational state of ospf
    
    .. attribute:: ospf_state
    
    	OSPF operational state
    	**type**\:  :py:class:`OspfState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.OspfState>`
    
    	**presence node**\: True
    
    .. attribute:: ospfv2_instance
    
    	The OSPF instance
    	**type**\: list of  		 :py:class:`Ospfv2Instance <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance>`
    
    

    """

    _prefix = 'ospf-ios-xe-oper'
    _revision = '2018-02-01'

    def __init__(self):
        super(OspfOperData, self).__init__()
        self._top_entity = None

        self.yang_name = "ospf-oper-data"
        self.yang_parent_name = "Cisco-IOS-XE-ospf-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ospf-state", ("ospf_state", OspfOperData.OspfState)), ("ospfv2-instance", ("ospfv2_instance", OspfOperData.Ospfv2Instance))])
        self._leafs = OrderedDict()

        self.ospf_state = None
        self._children_name_map["ospf_state"] = "ospf-state"

        self.ospfv2_instance = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-ospf-oper:ospf-oper-data"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(OspfOperData, [], name, value)


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
        _revision = '2018-02-01'

        def __init__(self):
            super(OspfOperData.OspfState, self).__init__()

            self.yang_name = "ospf-state"
            self.yang_parent_name = "ospf-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospf-instance", ("ospf_instance", OspfOperData.OspfState.OspfInstance))])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('op_mode', (YLeaf(YType.enumeration, 'op-mode'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'OspfOperationMode', '')])),
            ])
            self.op_mode = None

            self.ospf_instance = YList(self)
            self._segment_path = lambda: "ospf-state"
            self._absolute_path = lambda: "Cisco-IOS-XE-ospf-oper:ospf-oper-data/%s" % self._segment_path()
            self._is_frozen = True

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
            
            .. attribute:: process_id
            
            	The process identifier used to refer to this instance
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'ospf-ios-xe-oper'
            _revision = '2018-02-01'

            def __init__(self):
                super(OspfOperData.OspfState.OspfInstance, self).__init__()

                self.yang_name = "ospf-instance"
                self.yang_parent_name = "ospf-state"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['af','router_id']
                self._child_classes = OrderedDict([("ospf-area", ("ospf_area", OspfOperData.OspfState.OspfInstance.OspfArea)), ("link-scope-lsas", ("link_scope_lsas", OspfOperData.OspfState.OspfInstance.LinkScopeLsas)), ("multi-topology", ("multi_topology", OspfOperData.OspfState.OspfInstance.MultiTopology))])
                self._leafs = OrderedDict([
                    ('af', (YLeaf(YType.enumeration, 'af'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'AddressFamily', '')])),
                    ('router_id', (YLeaf(YType.uint32, 'router-id'), ['int'])),
                    ('process_id', (YLeaf(YType.uint16, 'process-id'), ['int'])),
                ])
                self.af = None
                self.router_id = None
                self.process_id = None

                self.ospf_area = YList(self)
                self.link_scope_lsas = YList(self)
                self.multi_topology = YList(self)
                self._segment_path = lambda: "ospf-instance" + "[af='" + str(self.af) + "']" + "[router-id='" + str(self.router_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-ospf-oper:ospf-oper-data/ospf-state/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OspfOperData.OspfState.OspfInstance, ['af', 'router_id', 'process_id'], name, value)


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
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.OspfState.OspfInstance.OspfArea, self).__init__()

                    self.yang_name = "ospf-area"
                    self.yang_parent_name = "ospf-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['area_id']
                    self._child_classes = OrderedDict([("ospf-interface", ("ospf_interface", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface)), ("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa))])
                    self._leafs = OrderedDict([
                        ('area_id', (YLeaf(YType.uint32, 'area-id'), ['int'])),
                    ])
                    self.area_id = None

                    self.ospf_interface = YList(self)
                    self.area_scope_lsa = YList(self)
                    self._segment_path = lambda: "ospf-area" + "[area-id='" + str(self.area_id) + "']"
                    self._is_frozen = True

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
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface, self).__init__()

                        self.yang_name = "ospf-interface"
                        self.yang_parent_name = "ospf-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([("multi-area", ("multi_area", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.MultiArea)), ("static-neighbor", ("static_neighbor", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.StaticNeighbor)), ("fast-reroute", ("fast_reroute", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute)), ("ttl-security", ("ttl_security", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity)), ("authentication", ("authentication", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication)), ("ospf-neighbor", ("ospf_neighbor", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor)), ("intf-link-scope-lsas", ("intf_link_scope_lsas", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas)), ("intf-multi-topology", ("intf_multi_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfMultiTopology))])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('network_type', (YLeaf(YType.enumeration, 'network-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'OspfNetworkType', '')])),
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
                            ('dr', (YLeaf(YType.str, 'dr'), ['str','str'])),
                            ('bdr', (YLeaf(YType.str, 'bdr'), ['str','str'])),
                            ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
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

                        self.fast_reroute = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute()
                        self.fast_reroute.parent = self
                        self._children_name_map["fast_reroute"] = "fast-reroute"

                        self.ttl_security = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity()
                        self.ttl_security.parent = self
                        self._children_name_map["ttl_security"] = "ttl-security"

                        self.authentication = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication()
                        self.authentication.parent = self
                        self._children_name_map["authentication"] = "authentication"

                        self.static_neighbor = YList(self)
                        self.ospf_neighbor = YList(self)
                        self.intf_link_scope_lsas = YList(self)
                        self.intf_multi_topology = YList(self)
                        self._segment_path = lambda: "ospf-interface" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.MultiArea, self).__init__()

                            self.yang_name = "multi-area"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('multi_area_id', (YLeaf(YType.uint32, 'multi-area-id'), ['int'])),
                                ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                            ])
                            self.multi_area_id = None
                            self.cost = None
                            self._segment_path = lambda: "multi-area"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.StaticNeighbor, self).__init__()

                            self.yang_name = "static-neighbor"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                                ('poll_interval', (YLeaf(YType.uint16, 'poll-interval'), ['int'])),
                            ])
                            self.address = None
                            self.cost = None
                            self.poll_interval = None
                            self._segment_path = lambda: "static-neighbor" + "[address='" + str(self.address) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.FastReroute, self).__init__()

                            self.yang_name = "fast-reroute"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('candidate_disabled', (YLeaf(YType.boolean, 'candidate-disabled'), ['bool'])),
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('remote_lfa_enabled', (YLeaf(YType.boolean, 'remote-lfa-enabled'), ['bool'])),
                            ])
                            self.candidate_disabled = None
                            self.enabled = None
                            self.remote_lfa_enabled = None
                            self._segment_path = lambda: "fast-reroute"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.TtlSecurity, self).__init__()

                            self.yang_name = "ttl-security"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('enabled', (YLeaf(YType.boolean, 'enabled'), ['bool'])),
                                ('hops', (YLeaf(YType.uint8, 'hops'), ['int'])),
                            ])
                            self.enabled = None
                            self.hops = None
                            self._segment_path = lambda: "ttl-security"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication, self).__init__()

                            self.yang_name = "authentication"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("crypto-algorithm-val", ("crypto_algorithm_val", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal))])
                            self._leafs = OrderedDict([
                                ('sa', (YLeaf(YType.str, 'sa'), ['str'])),
                                ('key_chain', (YLeaf(YType.str, 'key-chain'), ['str'])),
                                ('key_string', (YLeaf(YType.str, 'key-string'), ['str'])),
                                ('no_auth', (YLeaf(YType.uint32, 'no-auth'), ['int'])),
                            ])
                            self.sa = None
                            self.key_chain = None
                            self.key_string = None
                            self.no_auth = None

                            self.crypto_algorithm_val = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal()
                            self.crypto_algorithm_val.parent = self
                            self._children_name_map["crypto_algorithm_val"] = "crypto-algorithm-val"
                            self._segment_path = lambda: "authentication"
                            self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.Authentication.CryptoAlgorithmVal, self).__init__()

                                self.yang_name = "crypto-algorithm-val"
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
                                self._segment_path = lambda: "crypto-algorithm-val"
                                self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor, self).__init__()

                            self.yang_name = "ospf-neighbor"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['neighbor_id']
                            self._child_classes = OrderedDict([("stats", ("stats", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats))])
                            self._leafs = OrderedDict([
                                ('neighbor_id', (YLeaf(YType.str, 'neighbor-id'), ['str','str'])),
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('dr', (YLeaf(YType.str, 'dr'), ['str','str'])),
                                ('bdr', (YLeaf(YType.str, 'bdr'), ['str','str'])),
                                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'NbrStateType', '')])),
                            ])
                            self.neighbor_id = None
                            self.address = None
                            self.dr = None
                            self.bdr = None
                            self.state = None

                            self.stats = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                            self._segment_path = lambda: "ospf-neighbor" + "[neighbor-id='" + str(self.neighbor_id) + "']"
                            self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.OspfNeighbor.Stats, self).__init__()

                                self.yang_name = "stats"
                                self.yang_parent_name = "ospf-neighbor"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('nbr_event_count', (YLeaf(YType.uint32, 'nbr-event-count'), ['int'])),
                                    ('nbr_retrans_qlen', (YLeaf(YType.uint32, 'nbr-retrans-qlen'), ['int'])),
                                ])
                                self.nbr_event_count = None
                                self.nbr_retrans_qlen = None
                                self._segment_path = lambda: "stats"
                                self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas, self).__init__()

                            self.yang_name = "intf-link-scope-lsas"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['lsa_type']
                            self._child_classes = OrderedDict([("link-scope-lsa", ("link_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa)), ("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa))])
                            self._leafs = OrderedDict([
                                ('lsa_type', (YLeaf(YType.uint32, 'lsa-type'), ['int'])),
                            ])
                            self.lsa_type = None

                            self.link_scope_lsa = YList(self)
                            self.area_scope_lsa = YList(self)
                            self._segment_path = lambda: "intf-link-scope-lsas" + "[lsa-type='" + str(self.lsa_type) + "']"
                            self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa, self).__init__()

                                self.yang_name = "link-scope-lsa"
                                self.yang_parent_name = "intf-link-scope-lsas"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['lsa_id','adv_router']
                                self._child_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa)), ("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2External)), ("ospfv2-unknown-tlv", ("ospfv2_unknown_tlv", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv)), ("ospfv3-lsa-val", ("ospfv3_lsa_val", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3Link)), ("ospfv3-prefix-list", ("ospfv3_prefix_list", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix)), ("multi-topology", ("multi_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.MultiTopology)), ("tlv", ("tlv", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv)), ("unknown-sub-tlv", ("unknown_sub_tlv", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.UnknownSubTlv))])
                                self._leafs = OrderedDict([
                                    ('lsa_id', (YLeaf(YType.uint32, 'lsa-id'), ['int'])),
                                    ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str','str'])),
                                    ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                                    ('raw_data', (YLeafList(YType.uint8, 'raw-data'), ['int'])),
                                    ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                                    ('router_address', (YLeaf(YType.str, 'router-address'), ['str','str'])),
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

                                self.ospfv3_lsa_val = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal()
                                self.ospfv3_lsa_val.parent = self
                                self._children_name_map["ospfv3_lsa_val"] = "ospfv3-lsa-val"

                                self.tlv = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv()
                                self.tlv.parent = self
                                self._children_name_map["tlv"] = "tlv"

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
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa, self).__init__()

                                    self.yang_name = "ospfv2-lsa"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody))])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._segment_path = lambda: "ospfv2-lsa"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa, [], name, value)


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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                            ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                            ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                            ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                            ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                            ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                            ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                            ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                            ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                            ('flag_options', (YLeaf(YType.bits, 'flag-options'), ['Bits'])),
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
                                        self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                        self._leafs = OrderedDict([
                                            ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                            ('summary_mask', (YLeaf(YType.str, 'summary-mask'), ['str','str'])),
                                            ('external_mask', (YLeaf(YType.str, 'external-mask'), ['str','str'])),
                                            ('body_flag_options', (YLeaf(YType.bits, 'body-flag-options'), ['Bits'])),
                                        ])
                                        self.num_of_links = None
                                        self.summary_mask = None
                                        self.external_mask = None
                                        self.body_flag_options = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"
                                        self._segment_path = lambda: "lsa-body"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str','str'])),
                                                ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                            ])
                                            self.network_mask = None
                                            self.attached_router = []
                                            self._segment_path = lambda: "network"
                                            self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link, self).__init__()

                                    self.yang_name = "ospfv2-link"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['link_id','link_data']
                                    self._child_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology))])
                                    self._leafs = OrderedDict([
                                        ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                                        ('link_data', (YLeaf(YType.uint32, 'link-data'), ['int'])),
                                        ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                    ])
                                    self.link_id = None
                                    self.link_data = None
                                    self.type = None

                                    self.ospfv2_topology = YList(self)
                                    self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                                    self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                        self.yang_name = "ospfv2-topology"
                                        self.yang_parent_name = "ospfv2-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['mt_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                            ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                        ])
                                        self.mt_id = None
                                        self.metric = None
                                        self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                        self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2Topology, self).__init__()

                                    self.yang_name = "ospfv2-topology"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                        ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2External, self).__init__()

                                    self.yang_name = "ospfv2-external"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                        ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self.forwarding_address = None
                                    self.external_route_tag = None
                                    self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv, self).__init__()

                                    self.yang_name = "ospfv2-unknown-tlv"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                        ('value', (YLeafList(YType.uint8, 'value'), ['int'])),
                                    ])
                                    self.type = None
                                    self.length = None
                                    self.value = []
                                    self._segment_path = lambda: "ospfv2-unknown-tlv" + "[type='" + str(self.type) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal, self).__init__()

                                    self.yang_name = "ospfv3-lsa-val"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody))])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._segment_path = lambda: "ospfv3-lsa-val"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal, [], name, value)


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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv3-lsa-val"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader))])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                            ('lsa_hdr_options', (YLeaf(YType.bits, 'lsa-hdr-options'), ['Bits'])),
                                        ])
                                        self.lsa_id = None
                                        self.lsa_hdr_options = Bits()

                                        self.lsa_header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader()
                                        self.lsa_header.parent = self
                                        self._children_name_map["lsa_header"] = "lsa-header"
                                        self._segment_path = lambda: "header"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader, self).__init__()

                                            self.yang_name = "lsa-header"
                                            self.yang_parent_name = "header"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                                ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                            ])
                                            self.age = None
                                            self.type = None
                                            self.adv_router = None
                                            self.seq_num = None
                                            self.checksum = None
                                            self.length = None
                                            self._segment_path = lambda: "lsa-header"
                                            self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv3-lsa-val"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix))])
                                        self._leafs = OrderedDict([
                                            ('lsa_flag_options', (YLeaf(YType.bits, 'lsa-flag-options'), ['Bits'])),
                                            ('lsa_body_flags', (YLeaf(YType.bits, 'lsa-body-flags'), ['Bits'])),
                                        ])
                                        self.lsa_flag_options = Bits()
                                        self.lsa_body_flags = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"

                                        self.prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix()
                                        self.prefix.parent = self
                                        self._children_name_map["prefix"] = "prefix"

                                        self.ia_router = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter()
                                        self.ia_router.parent = self
                                        self._children_name_map["ia_router"] = "ia-router"

                                        self.lsa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal()
                                        self.lsa_external.parent = self
                                        self._children_name_map["lsa_external"] = "lsa-external"

                                        self.nssa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa()
                                        self.nssa.parent = self
                                        self._children_name_map["nssa"] = "nssa"

                                        self.link_data = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData()
                                        self.link_data.parent = self
                                        self._children_name_map["link_data"] = "link-data"

                                        self.ia_prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix()
                                        self.ia_prefix.parent = self
                                        self._children_name_map["ia_prefix"] = "ia-prefix"
                                        self._segment_path = lambda: "lsa-body"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                                ('lsa_net_options', (YLeaf(YType.bits, 'lsa-net-options'), ['Bits'])),
                                            ])
                                            self.attached_router = []
                                            self.lsa_net_options = Bits()
                                            self._segment_path = lambda: "network"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix, self).__init__()

                                            self.yang_name = "prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('ia_prefix', (YLeaf(YType.str, 'ia-prefix'), ['str'])),
                                                ('ia_prefix_options', (YLeaf(YType.str, 'ia-prefix-options'), ['str'])),
                                            ])
                                            self.metric = None
                                            self.ia_prefix = None
                                            self.ia_prefix_options = None
                                            self._segment_path = lambda: "prefix"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter, self).__init__()

                                            self.yang_name = "ia-router"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('destination_router_id', (YLeaf(YType.uint32, 'destination-router-id'), ['int'])),
                                                ('lsa_ia_options', (YLeaf(YType.bits, 'lsa-ia-options'), ['Bits'])),
                                            ])
                                            self.metric = None
                                            self.destination_router_id = None
                                            self.lsa_ia_options = Bits()
                                            self._segment_path = lambda: "ia-router"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal, self).__init__()

                                            self.yang_name = "lsa-external"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags))])
                                            self._leafs = OrderedDict([
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                                ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                                ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                                ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                            self._segment_path = lambda: "lsa-external"
                                            self._is_frozen = True

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
                                            _revision = '2018-02-01'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags, self).__init__()

                                                self.yang_name = "flags"
                                                self.yang_parent_name = "lsa-external"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                                ])
                                                self.e_flag = None
                                                self._segment_path = lambda: "flags"
                                                self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa, self).__init__()

                                            self.yang_name = "nssa"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal))])
                                            self._leafs = OrderedDict()

                                            self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal()
                                            self.lsa_nssa_external.parent = self
                                            self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                            self._segment_path = lambda: "nssa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa, [], name, value)


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
                                            _revision = '2018-02-01'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                                self.yang_name = "lsa-nssa-external"
                                                self.yang_parent_name = "nssa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                                self._leafs = OrderedDict([
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                    ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                                    ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                                    ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                                    ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                    ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                                self._segment_path = lambda: "lsa-nssa-external"
                                                self._is_frozen = True

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
                                                _revision = '2018-02-01'

                                                def __init__(self):
                                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                                    self.yang_name = "flags"
                                                    self.yang_parent_name = "lsa-nssa-external"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                                    ])
                                                    self.e_flag = None
                                                    self._segment_path = lambda: "flags"
                                                    self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData, self).__init__()

                                            self.yang_name = "link-data"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                                ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                                ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                                ('lsa_id_options', (YLeaf(YType.bits, 'lsa-id-options'), ['Bits'])),
                                            ])
                                            self.rtr_priority = None
                                            self.link_local_interface_address = None
                                            self.num_of_prefixes = None
                                            self.lsa_id_options = Bits()
                                            self._segment_path = lambda: "link-data"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix, self).__init__()

                                            self.yang_name = "ia-prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str','str'])),
                                                ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                            ])
                                            self.referenced_ls_type = None
                                            self.referenced_link_state_id = None
                                            self.referenced_adv_router = None
                                            self.num_of_prefixes = None
                                            self._segment_path = lambda: "ia-prefix"
                                            self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3Link, self).__init__()

                                    self.yang_name = "ospfv3-link"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                        ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                        ('neighbor_router_id', (YLeaf(YType.uint32, 'neighbor-router-id'), ['int'])),
                                        ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                        ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                    ])
                                    self.interface_id = None
                                    self.neighbor_interface_id = None
                                    self.neighbor_router_id = None
                                    self.type = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList, self).__init__()

                                    self.yang_name = "ospfv3-prefix-list"
                                    self.yang_parent_name = "link-scope-lsa"
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
                                    self._segment_path = lambda: "ospfv3-prefix-list" + "[prefix='" + str(self.prefix) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix, self).__init__()

                                    self.yang_name = "ospfv3-ia-prefix"
                                    self.yang_parent_name = "link-scope-lsa"
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
                                    self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.MultiTopology, self).__init__()

                                    self.yang_name = "multi-topology"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ])
                                    self.name = None
                                    self._segment_path = lambda: "multi-topology" + "[name='" + str(self.name) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.Tlv, self).__init__()

                                    self.yang_name = "tlv"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('link_type', (YLeaf(YType.uint8, 'link-type'), ['int'])),
                                        ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                                        ('local_if_ipv4_addr', (YLeafList(YType.str, 'local-if-ipv4-addr'), ['str','str'])),
                                        ('local_remote_ipv4_addr', (YLeafList(YType.str, 'local-remote-ipv4-addr'), ['str','str'])),
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
                                    self._segment_path = lambda: "tlv"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.LinkScopeLsa.UnknownSubTlv, self).__init__()

                                    self.yang_name = "unknown-sub-tlv"
                                    self.yang_parent_name = "link-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                        ('value', (YLeafList(YType.uint8, 'value'), ['int'])),
                                    ])
                                    self.type = None
                                    self.length = None
                                    self.value = []
                                    self._segment_path = lambda: "unknown-sub-tlv" + "[type='" + str(self.type) + "']"
                                    self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa, self).__init__()

                                self.yang_name = "area-scope-lsa"
                                self.yang_parent_name = "intf-link-scope-lsas"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['lsa_type','adv_router']
                                self._child_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa)), ("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2External)), ("ospfv3-lsa", ("ospfv3_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Link)), ("ospfv3-prefix", ("ospfv3_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Prefix)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix))])
                                self._leafs = OrderedDict([
                                    ('lsa_type', (YLeaf(YType.uint32, 'lsa-type'), ['int'])),
                                    ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str','str'])),
                                    ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                                    ('raw_data', (YLeafList(YType.uint8, 'raw-data'), ['int'])),
                                ])
                                self.lsa_type = None
                                self.adv_router = None
                                self.decoded_completed = None
                                self.raw_data = []

                                self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa()
                                self.ospfv2_lsa.parent = self
                                self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"

                                self.ospfv3_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa()
                                self.ospfv3_lsa.parent = self
                                self._children_name_map["ospfv3_lsa"] = "ospfv3-lsa"

                                self.ospfv2_link = YList(self)
                                self.ospfv2_topology = YList(self)
                                self.ospfv2_external = YList(self)
                                self.ospfv3_link = YList(self)
                                self.ospfv3_prefix = YList(self)
                                self.ospfv3_ia_prefix = YList(self)
                                self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']" + "[adv-router='" + str(self.adv_router) + "']"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa, self).__init__()

                                    self.yang_name = "ospfv2-lsa"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody))])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._segment_path = lambda: "ospfv2-lsa"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa, [], name, value)


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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                            ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                            ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                            ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                            ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                            ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                            ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                            ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                            ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                            ('flag_options', (YLeaf(YType.bits, 'flag-options'), ['Bits'])),
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
                                        self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv2-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                        self._leafs = OrderedDict([
                                            ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                            ('summary_mask', (YLeaf(YType.str, 'summary-mask'), ['str','str'])),
                                            ('external_mask', (YLeaf(YType.str, 'external-mask'), ['str','str'])),
                                            ('body_flag_options', (YLeaf(YType.bits, 'body-flag-options'), ['Bits'])),
                                        ])
                                        self.num_of_links = None
                                        self.summary_mask = None
                                        self.external_mask = None
                                        self.body_flag_options = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"
                                        self._segment_path = lambda: "lsa-body"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str','str'])),
                                                ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                            ])
                                            self.network_mask = None
                                            self.attached_router = []
                                            self._segment_path = lambda: "network"
                                            self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link, self).__init__()

                                    self.yang_name = "ospfv2-link"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['link_id','link_data']
                                    self._child_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology))])
                                    self._leafs = OrderedDict([
                                        ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                                        ('link_data', (YLeaf(YType.uint32, 'link-data'), ['int'])),
                                        ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                    ])
                                    self.link_id = None
                                    self.link_data = None
                                    self.type = None

                                    self.ospfv2_topology = YList(self)
                                    self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                                    self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                        self.yang_name = "ospfv2-topology"
                                        self.yang_parent_name = "ospfv2-link"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['mt_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                            ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                        ])
                                        self.mt_id = None
                                        self.metric = None
                                        self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                        self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2Topology, self).__init__()

                                    self.yang_name = "ospfv2-topology"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                        ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv2External, self).__init__()

                                    self.yang_name = "ospfv2-external"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                        ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self.forwarding_address = None
                                    self.external_route_tag = None
                                    self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa, self).__init__()

                                    self.yang_name = "ospfv3-lsa"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody))])
                                    self._leafs = OrderedDict()

                                    self.header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header()
                                    self.header.parent = self
                                    self._children_name_map["header"] = "header"

                                    self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody()
                                    self.lsa_body.parent = self
                                    self._children_name_map["lsa_body"] = "lsa-body"
                                    self._segment_path = lambda: "ospfv3-lsa"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa, [], name, value)


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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header, self).__init__()

                                        self.yang_name = "header"
                                        self.yang_parent_name = "ospfv3-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader))])
                                        self._leafs = OrderedDict([
                                            ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                            ('lsa_hdr_options', (YLeaf(YType.bits, 'lsa-hdr-options'), ['Bits'])),
                                        ])
                                        self.lsa_id = None
                                        self.lsa_hdr_options = Bits()

                                        self.lsa_header = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader()
                                        self.lsa_header.parent = self
                                        self._children_name_map["lsa_header"] = "lsa-header"
                                        self._segment_path = lambda: "header"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader, self).__init__()

                                            self.yang_name = "lsa-header"
                                            self.yang_parent_name = "header"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                                ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                                ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                                ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                            ])
                                            self.age = None
                                            self.type = None
                                            self.adv_router = None
                                            self.seq_num = None
                                            self.checksum = None
                                            self.length = None
                                            self._segment_path = lambda: "lsa-header"
                                            self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody, self).__init__()

                                        self.yang_name = "lsa-body"
                                        self.yang_parent_name = "ospfv3-lsa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix))])
                                        self._leafs = OrderedDict([
                                            ('lsa_flag_options', (YLeaf(YType.bits, 'lsa-flag-options'), ['Bits'])),
                                            ('lsa_body_flags', (YLeaf(YType.bits, 'lsa-body-flags'), ['Bits'])),
                                        ])
                                        self.lsa_flag_options = Bits()
                                        self.lsa_body_flags = Bits()

                                        self.network = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network()
                                        self.network.parent = self
                                        self._children_name_map["network"] = "network"

                                        self.prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix()
                                        self.prefix.parent = self
                                        self._children_name_map["prefix"] = "prefix"

                                        self.ia_router = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter()
                                        self.ia_router.parent = self
                                        self._children_name_map["ia_router"] = "ia-router"

                                        self.lsa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal()
                                        self.lsa_external.parent = self
                                        self._children_name_map["lsa_external"] = "lsa-external"

                                        self.nssa = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa()
                                        self.nssa.parent = self
                                        self._children_name_map["nssa"] = "nssa"

                                        self.link_data = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData()
                                        self.link_data.parent = self
                                        self._children_name_map["link_data"] = "link-data"

                                        self.ia_prefix = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix()
                                        self.ia_prefix.parent = self
                                        self._children_name_map["ia_prefix"] = "ia-prefix"
                                        self._segment_path = lambda: "lsa-body"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network, self).__init__()

                                            self.yang_name = "network"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                                ('lsa_net_options', (YLeaf(YType.bits, 'lsa-net-options'), ['Bits'])),
                                            ])
                                            self.attached_router = []
                                            self.lsa_net_options = Bits()
                                            self._segment_path = lambda: "network"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix, self).__init__()

                                            self.yang_name = "prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('ia_prefix', (YLeaf(YType.str, 'ia-prefix'), ['str'])),
                                                ('ia_prefix_options', (YLeaf(YType.str, 'ia-prefix-options'), ['str'])),
                                            ])
                                            self.metric = None
                                            self.ia_prefix = None
                                            self.ia_prefix_options = None
                                            self._segment_path = lambda: "prefix"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter, self).__init__()

                                            self.yang_name = "ia-router"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('destination_router_id', (YLeaf(YType.uint32, 'destination-router-id'), ['int'])),
                                                ('lsa_ia_options', (YLeaf(YType.bits, 'lsa-ia-options'), ['Bits'])),
                                            ])
                                            self.metric = None
                                            self.destination_router_id = None
                                            self.lsa_ia_options = Bits()
                                            self._segment_path = lambda: "ia-router"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal, self).__init__()

                                            self.yang_name = "lsa-external"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags))])
                                            self._leafs = OrderedDict([
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                                ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                                ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                                ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                            self._segment_path = lambda: "lsa-external"
                                            self._is_frozen = True

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
                                            _revision = '2018-02-01'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags, self).__init__()

                                                self.yang_name = "flags"
                                                self.yang_parent_name = "lsa-external"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                                ])
                                                self.e_flag = None
                                                self._segment_path = lambda: "flags"
                                                self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa, self).__init__()

                                            self.yang_name = "nssa"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal))])
                                            self._leafs = OrderedDict()

                                            self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal()
                                            self.lsa_nssa_external.parent = self
                                            self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                            self._segment_path = lambda: "nssa"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa, [], name, value)


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
                                            _revision = '2018-02-01'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                                self.yang_name = "lsa-nssa-external"
                                                self.yang_parent_name = "nssa"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                                self._leafs = OrderedDict([
                                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                    ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                    ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                                    ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                                    ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                                    ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                    ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                                self._segment_path = lambda: "lsa-nssa-external"
                                                self._is_frozen = True

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
                                                _revision = '2018-02-01'

                                                def __init__(self):
                                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                                    self.yang_name = "flags"
                                                    self.yang_parent_name = "lsa-nssa-external"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                                    ])
                                                    self.e_flag = None
                                                    self._segment_path = lambda: "flags"
                                                    self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData, self).__init__()

                                            self.yang_name = "link-data"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                                ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                                ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                                ('lsa_id_options', (YLeaf(YType.bits, 'lsa-id-options'), ['Bits'])),
                                            ])
                                            self.rtr_priority = None
                                            self.link_local_interface_address = None
                                            self.num_of_prefixes = None
                                            self.lsa_id_options = Bits()
                                            self._segment_path = lambda: "link-data"
                                            self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix, self).__init__()

                                            self.yang_name = "ia-prefix"
                                            self.yang_parent_name = "lsa-body"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                                ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str','str'])),
                                                ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                            ])
                                            self.referenced_ls_type = None
                                            self.referenced_link_state_id = None
                                            self.referenced_adv_router = None
                                            self.num_of_prefixes = None
                                            self._segment_path = lambda: "ia-prefix"
                                            self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Link, self).__init__()

                                    self.yang_name = "ospfv3-link"
                                    self.yang_parent_name = "area-scope-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                        ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                        ('neighbor_router_id', (YLeaf(YType.uint32, 'neighbor-router-id'), ['int'])),
                                        ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                        ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                    ])
                                    self.interface_id = None
                                    self.neighbor_interface_id = None
                                    self.neighbor_router_id = None
                                    self.type = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3Prefix, self).__init__()

                                    self.yang_name = "ospfv3-prefix"
                                    self.yang_parent_name = "area-scope-lsa"
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
                                    self._segment_path = lambda: "ospfv3-prefix" + "[prefix='" + str(self.prefix) + "']"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfLinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix, self).__init__()

                                    self.yang_name = "ospfv3-ia-prefix"
                                    self.yang_parent_name = "area-scope-lsa"
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
                                    self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"
                                    self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.OspfInterface.IntfMultiTopology, self).__init__()

                            self.yang_name = "intf-multi-topology"
                            self.yang_parent_name = "ospf-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.name = None
                            self._segment_path = lambda: "intf-multi-topology" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

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
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa, self).__init__()

                        self.yang_name = "area-scope-lsa"
                        self.yang_parent_name = "ospf-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsa_type']
                        self._child_classes = OrderedDict([("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_))])
                        self._leafs = OrderedDict([
                            ('lsa_type', (YLeaf(YType.uint32, 'lsa-type'), ['int'])),
                        ])
                        self.lsa_type = None

                        self.area_scope_lsa = YList(self)
                        self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']"
                        self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_, self).__init__()

                            self.yang_name = "area-scope-lsa"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['lsa_type','adv_router']
                            self._child_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa)), ("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2External)), ("ospfv3-lsa", ("ospfv3_lsa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Link)), ("ospfv3-prefix", ("ospfv3_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Prefix)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3IaPrefix))])
                            self._leafs = OrderedDict([
                                ('lsa_type', (YLeaf(YType.uint32, 'lsa-type'), ['int'])),
                                ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str','str'])),
                                ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                                ('raw_data', (YLeafList(YType.uint8, 'raw-data'), ['int'])),
                            ])
                            self.lsa_type = None
                            self.adv_router = None
                            self.decoded_completed = None
                            self.raw_data = []

                            self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa()
                            self.ospfv2_lsa.parent = self
                            self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"

                            self.ospfv3_lsa = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa()
                            self.ospfv3_lsa.parent = self
                            self._children_name_map["ospfv3_lsa"] = "ospfv3-lsa"

                            self.ospfv2_link = YList(self)
                            self.ospfv2_topology = YList(self)
                            self.ospfv2_external = YList(self)
                            self.ospfv3_link = YList(self)
                            self.ospfv3_prefix = YList(self)
                            self.ospfv3_ia_prefix = YList(self)
                            self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']" + "[adv-router='" + str(self.adv_router) + "']"
                            self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa, self).__init__()

                                self.yang_name = "ospfv2-lsa"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody))])
                                self._leafs = OrderedDict()

                                self.header = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header()
                                self.header.parent = self
                                self._children_name_map["header"] = "header"

                                self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody()
                                self.lsa_body.parent = self
                                self._children_name_map["lsa_body"] = "lsa-body"
                                self._segment_path = lambda: "ospfv2-lsa"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa, [], name, value)


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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.Header, self).__init__()

                                    self.yang_name = "header"
                                    self.yang_parent_name = "ospfv2-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                        ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                        ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                        ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                        ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                        ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                        ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                        ('flag_options', (YLeaf(YType.bits, 'flag-options'), ['Bits'])),
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
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody, self).__init__()

                                    self.yang_name = "lsa-body"
                                    self.yang_parent_name = "ospfv2-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network))])
                                    self._leafs = OrderedDict([
                                        ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                        ('summary_mask', (YLeaf(YType.str, 'summary-mask'), ['str','str'])),
                                        ('external_mask', (YLeaf(YType.str, 'external-mask'), ['str','str'])),
                                        ('body_flag_options', (YLeaf(YType.bits, 'body-flag-options'), ['Bits'])),
                                    ])
                                    self.num_of_links = None
                                    self.summary_mask = None
                                    self.external_mask = None
                                    self.body_flag_options = Bits()

                                    self.network = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network()
                                    self.network.parent = self
                                    self._children_name_map["network"] = "network"
                                    self._segment_path = lambda: "lsa-body"
                                    self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                        self.yang_name = "network"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str','str'])),
                                            ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                        ])
                                        self.network_mask = None
                                        self.attached_router = []
                                        self._segment_path = lambda: "network"
                                        self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link, self).__init__()

                                self.yang_name = "ospfv2-link"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['link_id','link_data']
                                self._child_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link.Ospfv2Topology))])
                                self._leafs = OrderedDict([
                                    ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                                    ('link_data', (YLeaf(YType.uint32, 'link-data'), ['int'])),
                                    ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                ])
                                self.link_id = None
                                self.link_data = None
                                self.type = None

                                self.ospfv2_topology = YList(self)
                                self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Link.Ospfv2Topology, self).__init__()

                                    self.yang_name = "ospfv2-topology"
                                    self.yang_parent_name = "ospfv2-link"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['mt_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                        ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                    ])
                                    self.mt_id = None
                                    self.metric = None
                                    self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                    self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2Topology, self).__init__()

                                self.yang_name = "ospfv2-topology"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                    ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv2External, self).__init__()

                                self.yang_name = "ospfv2-external"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                    ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                    ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self.forwarding_address = None
                                self.external_route_tag = None
                                self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"
                                self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa, self).__init__()

                                self.yang_name = "ospfv3-lsa"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody))])
                                self._leafs = OrderedDict()

                                self.header = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header()
                                self.header.parent = self
                                self._children_name_map["header"] = "header"

                                self.lsa_body = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody()
                                self.lsa_body.parent = self
                                self._children_name_map["lsa_body"] = "lsa-body"
                                self._segment_path = lambda: "ospfv3-lsa"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa, [], name, value)


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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header, self).__init__()

                                    self.yang_name = "header"
                                    self.yang_parent_name = "ospfv3-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader))])
                                    self._leafs = OrderedDict([
                                        ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                        ('lsa_hdr_options', (YLeaf(YType.bits, 'lsa-hdr-options'), ['Bits'])),
                                    ])
                                    self.lsa_id = None
                                    self.lsa_hdr_options = Bits()

                                    self.lsa_header = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader()
                                    self.lsa_header.parent = self
                                    self._children_name_map["lsa_header"] = "lsa-header"
                                    self._segment_path = lambda: "header"
                                    self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.Header.LsaHeader, self).__init__()

                                        self.yang_name = "lsa-header"
                                        self.yang_parent_name = "header"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                            ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                            ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                            ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                            ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                            ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                        ])
                                        self.age = None
                                        self.type = None
                                        self.adv_router = None
                                        self.seq_num = None
                                        self.checksum = None
                                        self.length = None
                                        self._segment_path = lambda: "lsa-header"
                                        self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody, self).__init__()

                                    self.yang_name = "lsa-body"
                                    self.yang_parent_name = "ospfv3-lsa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix))])
                                    self._leafs = OrderedDict([
                                        ('lsa_flag_options', (YLeaf(YType.bits, 'lsa-flag-options'), ['Bits'])),
                                        ('lsa_body_flags', (YLeaf(YType.bits, 'lsa-body-flags'), ['Bits'])),
                                    ])
                                    self.lsa_flag_options = Bits()
                                    self.lsa_body_flags = Bits()

                                    self.network = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network()
                                    self.network.parent = self
                                    self._children_name_map["network"] = "network"

                                    self.prefix = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix()
                                    self.prefix.parent = self
                                    self._children_name_map["prefix"] = "prefix"

                                    self.ia_router = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter()
                                    self.ia_router.parent = self
                                    self._children_name_map["ia_router"] = "ia-router"

                                    self.lsa_external = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal()
                                    self.lsa_external.parent = self
                                    self._children_name_map["lsa_external"] = "lsa-external"

                                    self.nssa = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa()
                                    self.nssa.parent = self
                                    self._children_name_map["nssa"] = "nssa"

                                    self.link_data = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData()
                                    self.link_data.parent = self
                                    self._children_name_map["link_data"] = "link-data"

                                    self.ia_prefix = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix()
                                    self.ia_prefix.parent = self
                                    self._children_name_map["ia_prefix"] = "ia-prefix"
                                    self._segment_path = lambda: "lsa-body"
                                    self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Network, self).__init__()

                                        self.yang_name = "network"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                            ('lsa_net_options', (YLeaf(YType.bits, 'lsa-net-options'), ['Bits'])),
                                        ])
                                        self.attached_router = []
                                        self.lsa_net_options = Bits()
                                        self._segment_path = lambda: "network"
                                        self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Prefix, self).__init__()

                                        self.yang_name = "prefix"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('ia_prefix', (YLeaf(YType.str, 'ia-prefix'), ['str'])),
                                            ('ia_prefix_options', (YLeaf(YType.str, 'ia-prefix-options'), ['str'])),
                                        ])
                                        self.metric = None
                                        self.ia_prefix = None
                                        self.ia_prefix_options = None
                                        self._segment_path = lambda: "prefix"
                                        self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaRouter, self).__init__()

                                        self.yang_name = "ia-router"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('destination_router_id', (YLeaf(YType.uint32, 'destination-router-id'), ['int'])),
                                            ('lsa_ia_options', (YLeaf(YType.bits, 'lsa-ia-options'), ['Bits'])),
                                        ])
                                        self.metric = None
                                        self.destination_router_id = None
                                        self.lsa_ia_options = Bits()
                                        self._segment_path = lambda: "ia-router"
                                        self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal, self).__init__()

                                        self.yang_name = "lsa-external"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal.Flags))])
                                        self._leafs = OrderedDict([
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                            ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                            ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                            ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                            ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                            ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                        self._segment_path = lambda: "lsa-external"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LsaExternal.Flags, self).__init__()

                                            self.yang_name = "flags"
                                            self.yang_parent_name = "lsa-external"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                            ])
                                            self.e_flag = None
                                            self._segment_path = lambda: "flags"
                                            self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa, self).__init__()

                                        self.yang_name = "nssa"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal))])
                                        self._leafs = OrderedDict()

                                        self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal()
                                        self.lsa_nssa_external.parent = self
                                        self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                        self._segment_path = lambda: "nssa"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa, [], name, value)


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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                            self.yang_name = "lsa-nssa-external"
                                            self.yang_parent_name = "nssa"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                            self._leafs = OrderedDict([
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                                ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                                ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                                ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                                ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                                ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                            self._segment_path = lambda: "lsa-nssa-external"
                                            self._is_frozen = True

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
                                            _revision = '2018-02-01'

                                            def __init__(self):
                                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                                self.yang_name = "flags"
                                                self.yang_parent_name = "lsa-nssa-external"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                                ])
                                                self.e_flag = None
                                                self._segment_path = lambda: "flags"
                                                self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.LinkData, self).__init__()

                                        self.yang_name = "link-data"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                            ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                            ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                            ('lsa_id_options', (YLeaf(YType.bits, 'lsa-id-options'), ['Bits'])),
                                        ])
                                        self.rtr_priority = None
                                        self.link_local_interface_address = None
                                        self.num_of_prefixes = None
                                        self.lsa_id_options = Bits()
                                        self._segment_path = lambda: "link-data"
                                        self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Lsa.LsaBody.IaPrefix, self).__init__()

                                        self.yang_name = "ia-prefix"
                                        self.yang_parent_name = "lsa-body"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                            ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                            ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str','str'])),
                                            ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                        ])
                                        self.referenced_ls_type = None
                                        self.referenced_link_state_id = None
                                        self.referenced_adv_router = None
                                        self.num_of_prefixes = None
                                        self._segment_path = lambda: "ia-prefix"
                                        self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Link, self).__init__()

                                self.yang_name = "ospfv3-link"
                                self.yang_parent_name = "area-scope-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                    ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                    ('neighbor_router_id', (YLeaf(YType.uint32, 'neighbor-router-id'), ['int'])),
                                    ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                    ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                ])
                                self.interface_id = None
                                self.neighbor_interface_id = None
                                self.neighbor_router_id = None
                                self.type = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                                self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3Prefix, self).__init__()

                                self.yang_name = "ospfv3-prefix"
                                self.yang_parent_name = "area-scope-lsa"
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
                                self._segment_path = lambda: "ospfv3-prefix" + "[prefix='" + str(self.prefix) + "']"
                                self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.OspfArea.AreaScopeLsa.AreaScopeLsa_.Ospfv3IaPrefix, self).__init__()

                                self.yang_name = "ospfv3-ia-prefix"
                                self.yang_parent_name = "area-scope-lsa"
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
                                self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"
                                self._is_frozen = True

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
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas, self).__init__()

                    self.yang_name = "link-scope-lsas"
                    self.yang_parent_name = "ospf-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['lsa_type']
                    self._child_classes = OrderedDict([("link-scope-lsa", ("link_scope_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa)), ("area-scope-lsa", ("area_scope_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa))])
                    self._leafs = OrderedDict([
                        ('lsa_type', (YLeaf(YType.uint32, 'lsa-type'), ['int'])),
                    ])
                    self.lsa_type = None

                    self.link_scope_lsa = YList(self)
                    self.area_scope_lsa = YList(self)
                    self._segment_path = lambda: "link-scope-lsas" + "[lsa-type='" + str(self.lsa_type) + "']"
                    self._is_frozen = True

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
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa, self).__init__()

                        self.yang_name = "link-scope-lsa"
                        self.yang_parent_name = "link-scope-lsas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsa_id','adv_router']
                        self._child_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa)), ("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2External)), ("ospfv2-unknown-tlv", ("ospfv2_unknown_tlv", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv)), ("ospfv3-lsa-val", ("ospfv3_lsa_val", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3Link)), ("ospfv3-prefix-list", ("ospfv3_prefix_list", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix)), ("multi-topology", ("multi_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.MultiTopology)), ("tlv", ("tlv", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv)), ("unknown-sub-tlv", ("unknown_sub_tlv", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.UnknownSubTlv))])
                        self._leafs = OrderedDict([
                            ('lsa_id', (YLeaf(YType.uint32, 'lsa-id'), ['int'])),
                            ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str','str'])),
                            ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                            ('raw_data', (YLeafList(YType.uint8, 'raw-data'), ['int'])),
                            ('version', (YLeaf(YType.uint32, 'version'), ['int'])),
                            ('router_address', (YLeaf(YType.str, 'router-address'), ['str','str'])),
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

                        self.ospfv3_lsa_val = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal()
                        self.ospfv3_lsa_val.parent = self
                        self._children_name_map["ospfv3_lsa_val"] = "ospfv3-lsa-val"

                        self.tlv = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv()
                        self.tlv.parent = self
                        self._children_name_map["tlv"] = "tlv"

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
                        self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa, self).__init__()

                            self.yang_name = "ospfv2-lsa"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody))])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._segment_path = lambda: "ospfv2-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa, [], name, value)


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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                    ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                    ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                    ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                    ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                    ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                    ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                    ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                    ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                    ('flag_options', (YLeaf(YType.bits, 'flag-options'), ['Bits'])),
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
                                self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                self._leafs = OrderedDict([
                                    ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                    ('summary_mask', (YLeaf(YType.str, 'summary-mask'), ['str','str'])),
                                    ('external_mask', (YLeaf(YType.str, 'external-mask'), ['str','str'])),
                                    ('body_flag_options', (YLeaf(YType.bits, 'body-flag-options'), ['Bits'])),
                                ])
                                self.num_of_links = None
                                self.summary_mask = None
                                self.external_mask = None
                                self.body_flag_options = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"
                                self._segment_path = lambda: "lsa-body"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str','str'])),
                                        ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                    ])
                                    self.network_mask = None
                                    self.attached_router = []
                                    self._segment_path = lambda: "network"
                                    self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link, self).__init__()

                            self.yang_name = "ospfv2-link"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['link_id','link_data']
                            self._child_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology))])
                            self._leafs = OrderedDict([
                                ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                                ('link_data', (YLeaf(YType.uint32, 'link-data'), ['int'])),
                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                            ])
                            self.link_id = None
                            self.link_data = None
                            self.type = None

                            self.ospfv2_topology = YList(self)
                            self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                            self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                self.yang_name = "ospfv2-topology"
                                self.yang_parent_name = "ospfv2-link"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                    ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2Topology, self).__init__()

                            self.yang_name = "ospfv2-topology"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2External, self).__init__()

                            self.yang_name = "ospfv2-external"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self.forwarding_address = None
                            self.external_route_tag = None
                            self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv2UnknownTlv, self).__init__()

                            self.yang_name = "ospfv2-unknown-tlv"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                ('value', (YLeafList(YType.uint8, 'value'), ['int'])),
                            ])
                            self.type = None
                            self.length = None
                            self.value = []
                            self._segment_path = lambda: "ospfv2-unknown-tlv" + "[type='" + str(self.type) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal, self).__init__()

                            self.yang_name = "ospfv3-lsa-val"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody))])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._segment_path = lambda: "ospfv3-lsa-val"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal, [], name, value)


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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv3-lsa-val"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader))])
                                self._leafs = OrderedDict([
                                    ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                    ('lsa_hdr_options', (YLeaf(YType.bits, 'lsa-hdr-options'), ['Bits'])),
                                ])
                                self.lsa_id = None
                                self.lsa_hdr_options = Bits()

                                self.lsa_header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader()
                                self.lsa_header.parent = self
                                self._children_name_map["lsa_header"] = "lsa-header"
                                self._segment_path = lambda: "header"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.Header.LsaHeader, self).__init__()

                                    self.yang_name = "lsa-header"
                                    self.yang_parent_name = "header"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                        ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                        ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                        ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                    ])
                                    self.age = None
                                    self.type = None
                                    self.adv_router = None
                                    self.seq_num = None
                                    self.checksum = None
                                    self.length = None
                                    self._segment_path = lambda: "lsa-header"
                                    self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv3-lsa-val"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix))])
                                self._leafs = OrderedDict([
                                    ('lsa_flag_options', (YLeaf(YType.bits, 'lsa-flag-options'), ['Bits'])),
                                    ('lsa_body_flags', (YLeaf(YType.bits, 'lsa-body-flags'), ['Bits'])),
                                ])
                                self.lsa_flag_options = Bits()
                                self.lsa_body_flags = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"

                                self.prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix()
                                self.prefix.parent = self
                                self._children_name_map["prefix"] = "prefix"

                                self.ia_router = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter()
                                self.ia_router.parent = self
                                self._children_name_map["ia_router"] = "ia-router"

                                self.lsa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal()
                                self.lsa_external.parent = self
                                self._children_name_map["lsa_external"] = "lsa-external"

                                self.nssa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa()
                                self.nssa.parent = self
                                self._children_name_map["nssa"] = "nssa"

                                self.link_data = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData()
                                self.link_data.parent = self
                                self._children_name_map["link_data"] = "link-data"

                                self.ia_prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix()
                                self.ia_prefix.parent = self
                                self._children_name_map["ia_prefix"] = "ia-prefix"
                                self._segment_path = lambda: "lsa-body"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                        ('lsa_net_options', (YLeaf(YType.bits, 'lsa-net-options'), ['Bits'])),
                                    ])
                                    self.attached_router = []
                                    self.lsa_net_options = Bits()
                                    self._segment_path = lambda: "network"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('ia_prefix', (YLeaf(YType.str, 'ia-prefix'), ['str'])),
                                        ('ia_prefix_options', (YLeaf(YType.str, 'ia-prefix-options'), ['str'])),
                                    ])
                                    self.metric = None
                                    self.ia_prefix = None
                                    self.ia_prefix_options = None
                                    self._segment_path = lambda: "prefix"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaRouter, self).__init__()

                                    self.yang_name = "ia-router"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('destination_router_id', (YLeaf(YType.uint32, 'destination-router-id'), ['int'])),
                                        ('lsa_ia_options', (YLeaf(YType.bits, 'lsa-ia-options'), ['Bits'])),
                                    ])
                                    self.metric = None
                                    self.destination_router_id = None
                                    self.lsa_ia_options = Bits()
                                    self._segment_path = lambda: "ia-router"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal, self).__init__()

                                    self.yang_name = "lsa-external"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags))])
                                    self._leafs = OrderedDict([
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                        ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                        ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                        ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                        ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                        ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                    self._segment_path = lambda: "lsa-external"
                                    self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LsaExternal.Flags, self).__init__()

                                        self.yang_name = "flags"
                                        self.yang_parent_name = "lsa-external"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                        ])
                                        self.e_flag = None
                                        self._segment_path = lambda: "flags"
                                        self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa, self).__init__()

                                    self.yang_name = "nssa"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal))])
                                    self._leafs = OrderedDict()

                                    self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal()
                                    self.lsa_nssa_external.parent = self
                                    self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                    self._segment_path = lambda: "nssa"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa, [], name, value)


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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                        self.yang_name = "lsa-nssa-external"
                                        self.yang_parent_name = "nssa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                        self._leafs = OrderedDict([
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                            ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                            ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                            ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                            ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                            ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                        self._segment_path = lambda: "lsa-nssa-external"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                            self.yang_name = "flags"
                                            self.yang_parent_name = "lsa-nssa-external"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                            ])
                                            self.e_flag = None
                                            self._segment_path = lambda: "flags"
                                            self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.LinkData, self).__init__()

                                    self.yang_name = "link-data"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                        ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                        ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                        ('lsa_id_options', (YLeaf(YType.bits, 'lsa-id-options'), ['Bits'])),
                                    ])
                                    self.rtr_priority = None
                                    self.link_local_interface_address = None
                                    self.num_of_prefixes = None
                                    self.lsa_id_options = Bits()
                                    self._segment_path = lambda: "link-data"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3LsaVal.LsaBody.IaPrefix, self).__init__()

                                    self.yang_name = "ia-prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                        ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                        ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str','str'])),
                                        ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                    ])
                                    self.referenced_ls_type = None
                                    self.referenced_link_state_id = None
                                    self.referenced_adv_router = None
                                    self.num_of_prefixes = None
                                    self._segment_path = lambda: "ia-prefix"
                                    self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3Link, self).__init__()

                            self.yang_name = "ospfv3-link"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                ('neighbor_router_id', (YLeaf(YType.uint32, 'neighbor-router-id'), ['int'])),
                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                            ])
                            self.interface_id = None
                            self.neighbor_interface_id = None
                            self.neighbor_router_id = None
                            self.type = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3PrefixList, self).__init__()

                            self.yang_name = "ospfv3-prefix-list"
                            self.yang_parent_name = "link-scope-lsa"
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
                            self._segment_path = lambda: "ospfv3-prefix-list" + "[prefix='" + str(self.prefix) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Ospfv3IaPrefix, self).__init__()

                            self.yang_name = "ospfv3-ia-prefix"
                            self.yang_parent_name = "link-scope-lsa"
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
                            self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.MultiTopology, self).__init__()

                            self.yang_name = "multi-topology"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ])
                            self.name = None
                            self._segment_path = lambda: "multi-topology" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.Tlv, self).__init__()

                            self.yang_name = "tlv"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('link_type', (YLeaf(YType.uint8, 'link-type'), ['int'])),
                                ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                                ('local_if_ipv4_addr', (YLeafList(YType.str, 'local-if-ipv4-addr'), ['str','str'])),
                                ('local_remote_ipv4_addr', (YLeafList(YType.str, 'local-remote-ipv4-addr'), ['str','str'])),
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
                            self._segment_path = lambda: "tlv"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.LinkScopeLsa.UnknownSubTlv, self).__init__()

                            self.yang_name = "unknown-sub-tlv"
                            self.yang_parent_name = "link-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['type']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                ('value', (YLeafList(YType.uint8, 'value'), ['int'])),
                            ])
                            self.type = None
                            self.length = None
                            self.value = []
                            self._segment_path = lambda: "unknown-sub-tlv" + "[type='" + str(self.type) + "']"
                            self._is_frozen = True

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
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa, self).__init__()

                        self.yang_name = "area-scope-lsa"
                        self.yang_parent_name = "link-scope-lsas"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsa_type','adv_router']
                        self._child_classes = OrderedDict([("ospfv2-lsa", ("ospfv2_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa)), ("ospfv2-link", ("ospfv2_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link)), ("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Topology)), ("ospfv2-external", ("ospfv2_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2External)), ("ospfv3-lsa", ("ospfv3_lsa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa)), ("ospfv3-link", ("ospfv3_link", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Link)), ("ospfv3-prefix", ("ospfv3_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Prefix)), ("ospfv3-ia-prefix", ("ospfv3_ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix))])
                        self._leafs = OrderedDict([
                            ('lsa_type', (YLeaf(YType.uint32, 'lsa-type'), ['int'])),
                            ('adv_router', (YLeaf(YType.str, 'adv-router'), ['str','str'])),
                            ('decoded_completed', (YLeaf(YType.boolean, 'decoded-completed'), ['bool'])),
                            ('raw_data', (YLeafList(YType.uint8, 'raw-data'), ['int'])),
                        ])
                        self.lsa_type = None
                        self.adv_router = None
                        self.decoded_completed = None
                        self.raw_data = []

                        self.ospfv2_lsa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa()
                        self.ospfv2_lsa.parent = self
                        self._children_name_map["ospfv2_lsa"] = "ospfv2-lsa"

                        self.ospfv3_lsa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa()
                        self.ospfv3_lsa.parent = self
                        self._children_name_map["ospfv3_lsa"] = "ospfv3-lsa"

                        self.ospfv2_link = YList(self)
                        self.ospfv2_topology = YList(self)
                        self.ospfv2_external = YList(self)
                        self.ospfv3_link = YList(self)
                        self.ospfv3_prefix = YList(self)
                        self.ospfv3_ia_prefix = YList(self)
                        self._segment_path = lambda: "area-scope-lsa" + "[lsa-type='" + str(self.lsa_type) + "']" + "[adv-router='" + str(self.adv_router) + "']"
                        self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa, self).__init__()

                            self.yang_name = "ospfv2-lsa"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody))])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._segment_path = lambda: "ospfv2-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa, [], name, value)


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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                    ('opaque_type', (YLeaf(YType.uint8, 'opaque-type'), ['int'])),
                                    ('opaque_id', (YLeaf(YType.uint32, 'opaque-id'), ['int'])),
                                    ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                    ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                    ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                    ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                    ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                    ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                    ('flag_options', (YLeaf(YType.bits, 'flag-options'), ['Bits'])),
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
                                self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv2-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network))])
                                self._leafs = OrderedDict([
                                    ('num_of_links', (YLeaf(YType.uint16, 'num-of-links'), ['int'])),
                                    ('summary_mask', (YLeaf(YType.str, 'summary-mask'), ['str','str'])),
                                    ('external_mask', (YLeaf(YType.str, 'external-mask'), ['str','str'])),
                                    ('body_flag_options', (YLeaf(YType.bits, 'body-flag-options'), ['Bits'])),
                                ])
                                self.num_of_links = None
                                self.summary_mask = None
                                self.external_mask = None
                                self.body_flag_options = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"
                                self._segment_path = lambda: "lsa-body"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Lsa.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('network_mask', (YLeaf(YType.str, 'network-mask'), ['str','str'])),
                                        ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                    ])
                                    self.network_mask = None
                                    self.attached_router = []
                                    self._segment_path = lambda: "network"
                                    self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link, self).__init__()

                            self.yang_name = "ospfv2-link"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['link_id','link_data']
                            self._child_classes = OrderedDict([("ospfv2-topology", ("ospfv2_topology", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology))])
                            self._leafs = OrderedDict([
                                ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                                ('link_data', (YLeaf(YType.uint32, 'link-data'), ['int'])),
                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                            ])
                            self.link_id = None
                            self.link_data = None
                            self.type = None

                            self.ospfv2_topology = YList(self)
                            self._segment_path = lambda: "ospfv2-link" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                            self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Link.Ospfv2Topology, self).__init__()

                                self.yang_name = "ospfv2-topology"
                                self.yang_parent_name = "ospfv2-link"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['mt_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                    ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                                ])
                                self.mt_id = None
                                self.metric = None
                                self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                                self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2Topology, self).__init__()

                            self.yang_name = "ospfv2-topology"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv2-topology" + "[mt-id='" + str(self.mt_id) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv2External, self).__init__()

                            self.yang_name = "ospfv2-external"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mt_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint32, 'mt-id'), ['int'])),
                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                            ])
                            self.mt_id = None
                            self.metric = None
                            self.forwarding_address = None
                            self.external_route_tag = None
                            self._segment_path = lambda: "ospfv2-external" + "[mt-id='" + str(self.mt_id) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa, self).__init__()

                            self.yang_name = "ospfv3-lsa"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("header", ("header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header)), ("lsa-body", ("lsa_body", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody))])
                            self._leafs = OrderedDict()

                            self.header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header()
                            self.header.parent = self
                            self._children_name_map["header"] = "header"

                            self.lsa_body = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody()
                            self.lsa_body.parent = self
                            self._children_name_map["lsa_body"] = "lsa-body"
                            self._segment_path = lambda: "ospfv3-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa, [], name, value)


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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header, self).__init__()

                                self.yang_name = "header"
                                self.yang_parent_name = "ospfv3-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("lsa-header", ("lsa_header", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader))])
                                self._leafs = OrderedDict([
                                    ('lsa_id', (YLeaf(YType.str, 'lsa-id'), ['str','str'])),
                                    ('lsa_hdr_options', (YLeaf(YType.bits, 'lsa-hdr-options'), ['Bits'])),
                                ])
                                self.lsa_id = None
                                self.lsa_hdr_options = Bits()

                                self.lsa_header = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader()
                                self.lsa_header.parent = self
                                self._children_name_map["lsa_header"] = "lsa-header"
                                self._segment_path = lambda: "header"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.Header.LsaHeader, self).__init__()

                                    self.yang_name = "lsa-header"
                                    self.yang_parent_name = "header"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('age', (YLeaf(YType.uint16, 'age'), ['int'])),
                                        ('type', (YLeaf(YType.uint16, 'type'), ['int'])),
                                        ('adv_router', (YLeaf(YType.uint32, 'adv-router'), ['int'])),
                                        ('seq_num', (YLeaf(YType.str, 'seq-num'), ['str'])),
                                        ('checksum', (YLeaf(YType.str, 'checksum'), ['str'])),
                                        ('length', (YLeaf(YType.uint16, 'length'), ['int'])),
                                    ])
                                    self.age = None
                                    self.type = None
                                    self.adv_router = None
                                    self.seq_num = None
                                    self.checksum = None
                                    self.length = None
                                    self._segment_path = lambda: "lsa-header"
                                    self._is_frozen = True

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
                            _revision = '2018-02-01'

                            def __init__(self):
                                super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody, self).__init__()

                                self.yang_name = "lsa-body"
                                self.yang_parent_name = "ospfv3-lsa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("network", ("network", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network)), ("prefix", ("prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix)), ("ia-router", ("ia_router", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter)), ("lsa-external", ("lsa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal)), ("nssa", ("nssa", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa)), ("link-data", ("link_data", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData)), ("ia-prefix", ("ia_prefix", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix))])
                                self._leafs = OrderedDict([
                                    ('lsa_flag_options', (YLeaf(YType.bits, 'lsa-flag-options'), ['Bits'])),
                                    ('lsa_body_flags', (YLeaf(YType.bits, 'lsa-body-flags'), ['Bits'])),
                                ])
                                self.lsa_flag_options = Bits()
                                self.lsa_body_flags = Bits()

                                self.network = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network()
                                self.network.parent = self
                                self._children_name_map["network"] = "network"

                                self.prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix()
                                self.prefix.parent = self
                                self._children_name_map["prefix"] = "prefix"

                                self.ia_router = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter()
                                self.ia_router.parent = self
                                self._children_name_map["ia_router"] = "ia-router"

                                self.lsa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal()
                                self.lsa_external.parent = self
                                self._children_name_map["lsa_external"] = "lsa-external"

                                self.nssa = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa()
                                self.nssa.parent = self
                                self._children_name_map["nssa"] = "nssa"

                                self.link_data = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData()
                                self.link_data.parent = self
                                self._children_name_map["link_data"] = "link-data"

                                self.ia_prefix = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix()
                                self.ia_prefix.parent = self
                                self._children_name_map["ia_prefix"] = "ia-prefix"
                                self._segment_path = lambda: "lsa-body"
                                self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Network, self).__init__()

                                    self.yang_name = "network"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('attached_router', (YLeafList(YType.uint32, 'attached-router'), ['int'])),
                                        ('lsa_net_options', (YLeaf(YType.bits, 'lsa-net-options'), ['Bits'])),
                                    ])
                                    self.attached_router = []
                                    self.lsa_net_options = Bits()
                                    self._segment_path = lambda: "network"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('ia_prefix', (YLeaf(YType.str, 'ia-prefix'), ['str'])),
                                        ('ia_prefix_options', (YLeaf(YType.str, 'ia-prefix-options'), ['str'])),
                                    ])
                                    self.metric = None
                                    self.ia_prefix = None
                                    self.ia_prefix_options = None
                                    self._segment_path = lambda: "prefix"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaRouter, self).__init__()

                                    self.yang_name = "ia-router"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('destination_router_id', (YLeaf(YType.uint32, 'destination-router-id'), ['int'])),
                                        ('lsa_ia_options', (YLeaf(YType.bits, 'lsa-ia-options'), ['Bits'])),
                                    ])
                                    self.metric = None
                                    self.destination_router_id = None
                                    self.lsa_ia_options = Bits()
                                    self._segment_path = lambda: "ia-router"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal, self).__init__()

                                    self.yang_name = "lsa-external"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags))])
                                    self._leafs = OrderedDict([
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                        ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                        ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                        ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                        ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                        ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                    self._segment_path = lambda: "lsa-external"
                                    self._is_frozen = True

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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LsaExternal.Flags, self).__init__()

                                        self.yang_name = "flags"
                                        self.yang_parent_name = "lsa-external"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                        ])
                                        self.e_flag = None
                                        self._segment_path = lambda: "flags"
                                        self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa, self).__init__()

                                    self.yang_name = "nssa"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("lsa-nssa-external", ("lsa_nssa_external", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal))])
                                    self._leafs = OrderedDict()

                                    self.lsa_nssa_external = OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal()
                                    self.lsa_nssa_external.parent = self
                                    self._children_name_map["lsa_nssa_external"] = "lsa-nssa-external"
                                    self._segment_path = lambda: "nssa"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa, [], name, value)


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
                                    _revision = '2018-02-01'

                                    def __init__(self):
                                        super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal, self).__init__()

                                        self.yang_name = "lsa-nssa-external"
                                        self.yang_parent_name = "nssa"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("flags", ("flags", OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags))])
                                        self._leafs = OrderedDict([
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                            ('external_prefix', (YLeaf(YType.str, 'external-prefix'), ['str'])),
                                            ('external_prefix_options', (YLeaf(YType.str, 'external-prefix-options'), ['str'])),
                                            ('forwarding_address', (YLeaf(YType.str, 'forwarding-address'), ['str','str'])),
                                            ('external_route_tag', (YLeaf(YType.uint32, 'external-route-tag'), ['int'])),
                                            ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
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
                                        self._segment_path = lambda: "lsa-nssa-external"
                                        self._is_frozen = True

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
                                        _revision = '2018-02-01'

                                        def __init__(self):
                                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.Nssa.LsaNssaExternal.Flags, self).__init__()

                                            self.yang_name = "flags"
                                            self.yang_parent_name = "lsa-nssa-external"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('e_flag', (YLeaf(YType.boolean, 'e-flag'), ['bool'])),
                                            ])
                                            self.e_flag = None
                                            self._segment_path = lambda: "flags"
                                            self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.LinkData, self).__init__()

                                    self.yang_name = "link-data"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('rtr_priority', (YLeaf(YType.uint8, 'rtr-priority'), ['int'])),
                                        ('link_local_interface_address', (YLeaf(YType.str, 'link-local-interface-address'), ['str','str'])),
                                        ('num_of_prefixes', (YLeaf(YType.uint32, 'num-of-prefixes'), ['int'])),
                                        ('lsa_id_options', (YLeaf(YType.bits, 'lsa-id-options'), ['Bits'])),
                                    ])
                                    self.rtr_priority = None
                                    self.link_local_interface_address = None
                                    self.num_of_prefixes = None
                                    self.lsa_id_options = Bits()
                                    self._segment_path = lambda: "link-data"
                                    self._is_frozen = True

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
                                _revision = '2018-02-01'

                                def __init__(self):
                                    super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Lsa.LsaBody.IaPrefix, self).__init__()

                                    self.yang_name = "ia-prefix"
                                    self.yang_parent_name = "lsa-body"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('referenced_ls_type', (YLeaf(YType.uint16, 'referenced-ls-type'), ['int'])),
                                        ('referenced_link_state_id', (YLeaf(YType.uint32, 'referenced-link-state-id'), ['int'])),
                                        ('referenced_adv_router', (YLeaf(YType.str, 'referenced-adv-router'), ['str','str'])),
                                        ('num_of_prefixes', (YLeaf(YType.uint16, 'num-of-prefixes'), ['int'])),
                                    ])
                                    self.referenced_ls_type = None
                                    self.referenced_link_state_id = None
                                    self.referenced_adv_router = None
                                    self.num_of_prefixes = None
                                    self._segment_path = lambda: "ia-prefix"
                                    self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Link, self).__init__()

                            self.yang_name = "ospfv3-link"
                            self.yang_parent_name = "area-scope-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_id','neighbor_interface_id','neighbor_router_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_id', (YLeaf(YType.uint32, 'interface-id'), ['int'])),
                                ('neighbor_interface_id', (YLeaf(YType.uint32, 'neighbor-interface-id'), ['int'])),
                                ('neighbor_router_id', (YLeaf(YType.uint32, 'neighbor-router-id'), ['int'])),
                                ('type', (YLeaf(YType.uint8, 'type'), ['int'])),
                                ('metric', (YLeaf(YType.uint16, 'metric'), ['int'])),
                            ])
                            self.interface_id = None
                            self.neighbor_interface_id = None
                            self.neighbor_router_id = None
                            self.type = None
                            self.metric = None
                            self._segment_path = lambda: "ospfv3-link" + "[interface-id='" + str(self.interface_id) + "']" + "[neighbor-interface-id='" + str(self.neighbor_interface_id) + "']" + "[neighbor-router-id='" + str(self.neighbor_router_id) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3Prefix, self).__init__()

                            self.yang_name = "ospfv3-prefix"
                            self.yang_parent_name = "area-scope-lsa"
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
                            self._segment_path = lambda: "ospfv3-prefix" + "[prefix='" + str(self.prefix) + "']"
                            self._is_frozen = True

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
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.OspfState.OspfInstance.LinkScopeLsas.AreaScopeLsa.Ospfv3IaPrefix, self).__init__()

                            self.yang_name = "ospfv3-ia-prefix"
                            self.yang_parent_name = "area-scope-lsa"
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
                            self._segment_path = lambda: "ospfv3-ia-prefix" + "[prefix='" + str(self.prefix) + "']"
                            self._is_frozen = True

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
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.OspfState.OspfInstance.MultiTopology, self).__init__()

                    self.yang_name = "multi-topology"
                    self.yang_parent_name = "ospf-instance"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None
                    self._segment_path = lambda: "multi-topology" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.OspfState.OspfInstance.MultiTopology, ['name'], name, value)


    class Ospfv2Instance(Entity):
        """
        The OSPF instance
        
        .. attribute:: instance_id  (key)
        
        	The routing instance identifier assigned to the OSPF instance
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vrf_name
        
        	The name of the Virtual Routing and Forwarding instance that the OSPF instance is operating within
        	**type**\: str
        
        .. attribute:: router_id
        
        	The router identifer assigned to the OSPF instance
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ospfv2_area
        
        	The OSPF area information
        	**type**\: list of  		 :py:class:`Ospfv2Area <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area>`
        
        .. attribute:: ospfv2_lsdb_external
        
        	The external LSDB information
        	**type**\: list of  		 :py:class:`Ospfv2LsdbExternal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal>`
        
        

        """

        _prefix = 'ospf-ios-xe-oper'
        _revision = '2018-02-01'

        def __init__(self):
            super(OspfOperData.Ospfv2Instance, self).__init__()

            self.yang_name = "ospfv2-instance"
            self.yang_parent_name = "ospf-oper-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['instance_id']
            self._child_classes = OrderedDict([("ospfv2-area", ("ospfv2_area", OspfOperData.Ospfv2Instance.Ospfv2Area)), ("ospfv2-lsdb-external", ("ospfv2_lsdb_external", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal))])
            self._leafs = OrderedDict([
                ('instance_id', (YLeaf(YType.uint32, 'instance-id'), ['int'])),
                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ('router_id', (YLeaf(YType.uint32, 'router-id'), ['int'])),
            ])
            self.instance_id = None
            self.vrf_name = None
            self.router_id = None

            self.ospfv2_area = YList(self)
            self.ospfv2_lsdb_external = YList(self)
            self._segment_path = lambda: "ospfv2-instance" + "[instance-id='" + str(self.instance_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-ospf-oper:ospf-oper-data/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(OspfOperData.Ospfv2Instance, ['instance_id', 'vrf_name', 'router_id'], name, value)


        class Ospfv2Area(Entity):
            """
            The OSPF area information
            
            .. attribute:: area_id  (key)
            
            	The area identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ospfv2_lsdb_area
            
            	The OSPF Link State Database information for this area
            	**type**\: list of  		 :py:class:`Ospfv2LsdbArea <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea>`
            
            .. attribute:: ospfv2_interface
            
            	A list of interfaces that belong to the area
            	**type**\: list of  		 :py:class:`Ospfv2Interface <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface>`
            
            

            """

            _prefix = 'ospf-ios-xe-oper'
            _revision = '2018-02-01'

            def __init__(self):
                super(OspfOperData.Ospfv2Instance.Ospfv2Area, self).__init__()

                self.yang_name = "ospfv2-area"
                self.yang_parent_name = "ospfv2-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['area_id']
                self._child_classes = OrderedDict([("ospfv2-lsdb-area", ("ospfv2_lsdb_area", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea)), ("ospfv2-interface", ("ospfv2_interface", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface))])
                self._leafs = OrderedDict([
                    ('area_id', (YLeaf(YType.uint32, 'area-id'), ['int'])),
                ])
                self.area_id = None

                self.ospfv2_lsdb_area = YList(self)
                self.ospfv2_interface = YList(self)
                self._segment_path = lambda: "ospfv2-area" + "[area-id='" + str(self.area_id) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area, ['area_id'], name, value)


            class Ospfv2LsdbArea(Entity):
                """
                The OSPF Link State Database information for this area
                
                .. attribute:: lsa_type  (key)
                
                	Link State Advertisement type
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: lsa_id  (key)
                
                	Link State Advertisement Identifer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: advertising_router  (key)
                
                	Advertising router
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsa_age
                
                	The age of the Link State Advertisement
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: lsa_options
                
                	The options of the Link State Advertisement
                	**type**\:  :py:class:`Ospfv2LsaFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2LsaFlagOptions>`
                
                .. attribute:: lsa_seq_number
                
                	The sequence number for the Link State Advertisement
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: lsa_checksum
                
                	The checksum of the Link State Advertisement
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: lsa_length
                
                	The length, in bytes, of the Link State Advertisement
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: ospfv2_router_lsa_links
                
                	The router Link State Advertisement links
                	**type**\: list of  		 :py:class:`Ospfv2RouterLsaLinks <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks>`
                
                .. attribute:: unsupported_lsa
                
                	The unsupported Link State Advertisements
                	**type**\:  :py:class:`UnsupportedLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.UnsupportedLsa>`
                
                .. attribute:: router_lsa
                
                	The router Link State Advertisements
                	**type**\:  :py:class:`RouterLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterLsa>`
                
                .. attribute:: network_lsa
                
                	The network Link State Advertisements
                	**type**\:  :py:class:`NetworkLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkLsa>`
                
                .. attribute:: network_summary_lsa
                
                	The network summary Link State Advertisements
                	**type**\:  :py:class:`NetworkSummaryLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa>`
                
                .. attribute:: router_summary_lsa
                
                	The router summary Link State Advertisements
                	**type**\:  :py:class:`RouterSummaryLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa>`
                
                .. attribute:: external_lsa
                
                	The external Link State Advertisements
                	**type**\:  :py:class:`ExternalLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa>`
                
                .. attribute:: nssa_lsa
                
                	The Not So Stubby Area Link state advertisements
                	**type**\:  :py:class:`NssaLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea, self).__init__()

                    self.yang_name = "ospfv2-lsdb-area"
                    self.yang_parent_name = "ospfv2-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['lsa_type','lsa_id','advertising_router']
                    self._child_classes = OrderedDict([("ospfv2-router-lsa-links", ("ospfv2_router_lsa_links", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks)), ("unsupported-lsa", ("unsupported_lsa", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.UnsupportedLsa)), ("router-lsa", ("router_lsa", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterLsa)), ("network-lsa", ("network_lsa", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkLsa)), ("network-summary-lsa", ("network_summary_lsa", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa)), ("router-summary-lsa", ("router_summary_lsa", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa)), ("external-lsa", ("external_lsa", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa)), ("nssa-lsa", ("nssa_lsa", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa))])
                    self._leafs = OrderedDict([
                        ('lsa_type', (YLeaf(YType.uint8, 'lsa-type'), ['int'])),
                        ('lsa_id', (YLeaf(YType.uint32, 'lsa-id'), ['int'])),
                        ('advertising_router', (YLeaf(YType.uint32, 'advertising-router'), ['int'])),
                        ('lsa_age', (YLeaf(YType.uint16, 'lsa-age'), ['int'])),
                        ('lsa_options', (YLeaf(YType.bits, 'lsa-options'), ['Bits'])),
                        ('lsa_seq_number', (YLeaf(YType.uint32, 'lsa-seq-number'), ['int'])),
                        ('lsa_checksum', (YLeaf(YType.uint16, 'lsa-checksum'), ['int'])),
                        ('lsa_length', (YLeaf(YType.uint16, 'lsa-length'), ['int'])),
                    ])
                    self.lsa_type = None
                    self.lsa_id = None
                    self.advertising_router = None
                    self.lsa_age = None
                    self.lsa_options = Bits()
                    self.lsa_seq_number = None
                    self.lsa_checksum = None
                    self.lsa_length = None

                    self.unsupported_lsa = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.UnsupportedLsa()
                    self.unsupported_lsa.parent = self
                    self._children_name_map["unsupported_lsa"] = "unsupported-lsa"

                    self.router_lsa = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterLsa()
                    self.router_lsa.parent = self
                    self._children_name_map["router_lsa"] = "router-lsa"

                    self.network_lsa = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkLsa()
                    self.network_lsa.parent = self
                    self._children_name_map["network_lsa"] = "network-lsa"

                    self.network_summary_lsa = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa()
                    self.network_summary_lsa.parent = self
                    self._children_name_map["network_summary_lsa"] = "network-summary-lsa"

                    self.router_summary_lsa = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa()
                    self.router_summary_lsa.parent = self
                    self._children_name_map["router_summary_lsa"] = "router-summary-lsa"

                    self.external_lsa = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa()
                    self.external_lsa.parent = self
                    self._children_name_map["external_lsa"] = "external-lsa"

                    self.nssa_lsa = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa()
                    self.nssa_lsa.parent = self
                    self._children_name_map["nssa_lsa"] = "nssa-lsa"

                    self.ospfv2_router_lsa_links = YList(self)
                    self._segment_path = lambda: "ospfv2-lsdb-area" + "[lsa-type='" + str(self.lsa_type) + "']" + "[lsa-id='" + str(self.lsa_id) + "']" + "[advertising-router='" + str(self.advertising_router) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea, ['lsa_type', 'lsa_id', 'advertising_router', 'lsa_age', 'lsa_options', 'lsa_seq_number', 'lsa_checksum', 'lsa_length'], name, value)


                class Ospfv2RouterLsaLinks(Entity):
                    """
                    The router Link State Advertisement links
                    
                    .. attribute:: link_type  (key)
                    
                    	Link Type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: link_id  (key)
                    
                    	link Identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: link_data  (key)
                    
                    	link data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: link_topo
                    
                    	Link topology
                    	**type**\: list of  		 :py:class:`LinkTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks.LinkTopo>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks, self).__init__()

                        self.yang_name = "ospfv2-router-lsa-links"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['link_type','link_id','link_data']
                        self._child_classes = OrderedDict([("link-topo", ("link_topo", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks.LinkTopo))])
                        self._leafs = OrderedDict([
                            ('link_type', (YLeaf(YType.uint8, 'link-type'), ['int'])),
                            ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                            ('link_data', (YLeaf(YType.uint32, 'link-data'), ['int'])),
                        ])
                        self.link_type = None
                        self.link_id = None
                        self.link_data = None

                        self.link_topo = YList(self)
                        self._segment_path = lambda: "ospfv2-router-lsa-links" + "[link-type='" + str(self.link_type) + "']" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks, ['link_type', 'link_id', 'link_data'], name, value)


                    class LinkTopo(Entity):
                        """
                        Link topology
                        
                        .. attribute:: mt_id
                        
                        	Multi topology identifier
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: topo_metric
                        
                        	Topology metric
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks.LinkTopo, self).__init__()

                            self.yang_name = "link-topo"
                            self.yang_parent_name = "ospfv2-router-lsa-links"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                ('topo_metric', (YLeaf(YType.uint16, 'topo-metric'), ['int'])),
                            ])
                            self.mt_id = None
                            self.topo_metric = None
                            self._segment_path = lambda: "link-topo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.Ospfv2RouterLsaLinks.LinkTopo, ['mt_id', 'topo_metric'], name, value)


                class UnsupportedLsa(Entity):
                    """
                    The unsupported Link State Advertisements
                    
                    .. attribute:: lsa_data
                    
                    	Link State Advertisement data
                    	**type**\: list of int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.UnsupportedLsa, self).__init__()

                        self.yang_name = "unsupported-lsa"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('lsa_data', (YLeafList(YType.uint8, 'lsa-data'), ['int'])),
                        ])
                        self.lsa_data = []
                        self._segment_path = lambda: "unsupported-lsa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.UnsupportedLsa, ['lsa_data'], name, value)


                class RouterLsa(Entity):
                    """
                    The router Link State Advertisements
                    
                    .. attribute:: router_lsa_bits
                    
                    	Router Link State Advertisement bits
                    	**type**\:  :py:class:`Ospfv2RouterLsaBits <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2RouterLsaBits>`
                    
                    .. attribute:: router_lsa_number_links
                    
                    	Router Link State Advertisement number of links
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterLsa, self).__init__()

                        self.yang_name = "router-lsa"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('router_lsa_bits', (YLeaf(YType.bits, 'router-lsa-bits'), ['Bits'])),
                            ('router_lsa_number_links', (YLeaf(YType.uint16, 'router-lsa-number-links'), ['int'])),
                        ])
                        self.router_lsa_bits = Bits()
                        self.router_lsa_number_links = None
                        self._segment_path = lambda: "router-lsa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterLsa, ['router_lsa_bits', 'router_lsa_number_links'], name, value)


                class NetworkLsa(Entity):
                    """
                    The network Link State Advertisements
                    
                    .. attribute:: network_lsa_mask
                    
                    	Network Link State Advertisement mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: network_attached_routers
                    
                    	Network attached routers
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkLsa, self).__init__()

                        self.yang_name = "network-lsa"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('network_lsa_mask', (YLeaf(YType.uint32, 'network-lsa-mask'), ['int'])),
                            ('network_attached_routers', (YLeafList(YType.uint32, 'network-attached-routers'), ['int'])),
                        ])
                        self.network_lsa_mask = None
                        self.network_attached_routers = []
                        self._segment_path = lambda: "network-lsa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkLsa, ['network_lsa_mask', 'network_attached_routers'], name, value)


                class NetworkSummaryLsa(Entity):
                    """
                    The network summary Link State Advertisements
                    
                    .. attribute:: summary_lsa_mask
                    
                    	The summary Link State Advertisement mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: summary_topo
                    
                    	The summary topology
                    	**type**\: list of  		 :py:class:`SummaryTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa.SummaryTopo>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa, self).__init__()

                        self.yang_name = "network-summary-lsa"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("summary-topo", ("summary_topo", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa.SummaryTopo))])
                        self._leafs = OrderedDict([
                            ('summary_lsa_mask', (YLeaf(YType.uint32, 'summary-lsa-mask'), ['int'])),
                        ])
                        self.summary_lsa_mask = None

                        self.summary_topo = YList(self)
                        self._segment_path = lambda: "network-summary-lsa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa, ['summary_lsa_mask'], name, value)


                    class SummaryTopo(Entity):
                        """
                        The summary topology
                        
                        .. attribute:: mt_id
                        
                        	Multi topology identifier
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: topo_metric
                        
                        	Topology Metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa.SummaryTopo, self).__init__()

                            self.yang_name = "summary-topo"
                            self.yang_parent_name = "network-summary-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                            ])
                            self.mt_id = None
                            self.topo_metric = None
                            self._segment_path = lambda: "summary-topo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NetworkSummaryLsa.SummaryTopo, ['mt_id', 'topo_metric'], name, value)


                class RouterSummaryLsa(Entity):
                    """
                    The router summary Link State Advertisements
                    
                    .. attribute:: summary_lsa_mask
                    
                    	The summary Link State Advertisement mask
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: summary_topo
                    
                    	The summary topology
                    	**type**\: list of  		 :py:class:`SummaryTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa.SummaryTopo>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa, self).__init__()

                        self.yang_name = "router-summary-lsa"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("summary-topo", ("summary_topo", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa.SummaryTopo))])
                        self._leafs = OrderedDict([
                            ('summary_lsa_mask', (YLeaf(YType.uint32, 'summary-lsa-mask'), ['int'])),
                        ])
                        self.summary_lsa_mask = None

                        self.summary_topo = YList(self)
                        self._segment_path = lambda: "router-summary-lsa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa, ['summary_lsa_mask'], name, value)


                    class SummaryTopo(Entity):
                        """
                        The summary topology
                        
                        .. attribute:: mt_id
                        
                        	Multi topology identifier
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: topo_metric
                        
                        	Topology Metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa.SummaryTopo, self).__init__()

                            self.yang_name = "summary-topo"
                            self.yang_parent_name = "router-summary-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                            ])
                            self.mt_id = None
                            self.topo_metric = None
                            self._segment_path = lambda: "summary-topo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.RouterSummaryLsa.SummaryTopo, ['mt_id', 'topo_metric'], name, value)


                class ExternalLsa(Entity):
                    """
                    The external Link State Advertisements
                    
                    .. attribute:: external_lsa_mask
                    
                    	The mask for the external Link State Advertisement
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: external_topo
                    
                    	The external topology Link State Advertisement
                    	**type**\: list of  		 :py:class:`ExternalTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa.ExternalTopo>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa, self).__init__()

                        self.yang_name = "external-lsa"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("external-topo", ("external_topo", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa.ExternalTopo))])
                        self._leafs = OrderedDict([
                            ('external_lsa_mask', (YLeaf(YType.uint32, 'external-lsa-mask'), ['int'])),
                        ])
                        self.external_lsa_mask = None

                        self.external_topo = YList(self)
                        self._segment_path = lambda: "external-lsa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa, ['external_lsa_mask'], name, value)


                    class ExternalTopo(Entity):
                        """
                        The external topology Link State Advertisement
                        
                        .. attribute:: mt_id
                        
                        	The multi topology identifier
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: topo_metric_type
                        
                        	The topoligy metric type associated with the  Link State Advertisement
                        	**type**\:  :py:class:`OspfExternalMetricType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfExternalMetricType>`
                        
                        .. attribute:: topo_metric
                        
                        	The topology metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: topo_forwarding_address
                        
                        	The topology forwarding address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: topo_route_tag
                        
                        	The topology route tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa.ExternalTopo, self).__init__()

                            self.yang_name = "external-topo"
                            self.yang_parent_name = "external-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                ('topo_metric_type', (YLeaf(YType.enumeration, 'topo-metric-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'OspfExternalMetricType', '')])),
                                ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                                ('topo_forwarding_address', (YLeaf(YType.str, 'topo-forwarding-address'), ['str','str'])),
                                ('topo_route_tag', (YLeaf(YType.uint32, 'topo-route-tag'), ['int'])),
                            ])
                            self.mt_id = None
                            self.topo_metric_type = None
                            self.topo_metric = None
                            self.topo_forwarding_address = None
                            self.topo_route_tag = None
                            self._segment_path = lambda: "external-topo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.ExternalLsa.ExternalTopo, ['mt_id', 'topo_metric_type', 'topo_metric', 'topo_forwarding_address', 'topo_route_tag'], name, value)


                class NssaLsa(Entity):
                    """
                    The Not So Stubby Area Link state advertisements
                    
                    .. attribute:: external_lsa_mask
                    
                    	The mask for the external Link State Advertisement
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: external_topo
                    
                    	The external topology Link State Advertisement
                    	**type**\: list of  		 :py:class:`ExternalTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa.ExternalTopo>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa, self).__init__()

                        self.yang_name = "nssa-lsa"
                        self.yang_parent_name = "ospfv2-lsdb-area"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("external-topo", ("external_topo", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa.ExternalTopo))])
                        self._leafs = OrderedDict([
                            ('external_lsa_mask', (YLeaf(YType.uint32, 'external-lsa-mask'), ['int'])),
                        ])
                        self.external_lsa_mask = None

                        self.external_topo = YList(self)
                        self._segment_path = lambda: "nssa-lsa"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa, ['external_lsa_mask'], name, value)


                    class ExternalTopo(Entity):
                        """
                        The external topology Link State Advertisement
                        
                        .. attribute:: mt_id
                        
                        	The multi topology identifier
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: topo_metric_type
                        
                        	The topoligy metric type associated with the  Link State Advertisement
                        	**type**\:  :py:class:`OspfExternalMetricType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfExternalMetricType>`
                        
                        .. attribute:: topo_metric
                        
                        	The topology metric
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: topo_forwarding_address
                        
                        	The topology forwarding address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: topo_route_tag
                        
                        	The topology route tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa.ExternalTopo, self).__init__()

                            self.yang_name = "external-topo"
                            self.yang_parent_name = "nssa-lsa"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                                ('topo_metric_type', (YLeaf(YType.enumeration, 'topo-metric-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'OspfExternalMetricType', '')])),
                                ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                                ('topo_forwarding_address', (YLeaf(YType.str, 'topo-forwarding-address'), ['str','str'])),
                                ('topo_route_tag', (YLeaf(YType.uint32, 'topo-route-tag'), ['int'])),
                            ])
                            self.mt_id = None
                            self.topo_metric_type = None
                            self.topo_metric = None
                            self.topo_forwarding_address = None
                            self.topo_route_tag = None
                            self._segment_path = lambda: "external-topo"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2LsdbArea.NssaLsa.ExternalTopo, ['mt_id', 'topo_metric_type', 'topo_metric', 'topo_forwarding_address', 'topo_route_tag'], name, value)


            class Ospfv2Interface(Entity):
                """
                A list of interfaces that belong to the area
                
                .. attribute:: name  (key)
                
                	Name of the interface
                	**type**\: str
                
                .. attribute:: network_type
                
                	Network type
                	**type**\:  :py:class:`OspfNetworkType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfNetworkType>`
                
                .. attribute:: enable
                
                	If the interface is enabled
                	**type**\: bool
                
                .. attribute:: passive
                
                	If the interface is in passive mode
                	**type**\: bool
                
                .. attribute:: demand_circuit
                
                	If this is a demand circuit
                	**type**\: bool
                
                .. attribute:: mtu_ignore
                
                	If the MTU is being ignored
                	**type**\: bool
                
                .. attribute:: prefix_suppresion
                
                	If prefix suppression is enabled
                	**type**\: bool
                
                .. attribute:: cost
                
                	The OSPFv2 cost
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: hello_interval
                
                	The hello interval in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: dead_interval
                
                	The dead interval in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: retransmit_interval
                
                	The retransmit interval in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: transmit_delay
                
                	The delay before transmitting a keepalive in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: hello_timer
                
                	The current hello timer in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: wait_timer
                
                	The wait timer in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dr
                
                	The designated router identifier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bdr
                
                	The backup designated router identifier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dr_ip
                
                	The address of the designated router
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: bdr_ip
                
                	The address of the backup designated router
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: state
                
                	The current state of the interface
                	**type**\:  :py:class:`Ospfv2IntfState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2IntfState>`
                
                .. attribute:: ttl_security_val
                
                	The TTL security information
                	**type**\:  :py:class:`TtlSecurityVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.TtlSecurityVal>`
                
                .. attribute:: auth_val
                
                	The authentication information
                	**type**\:  :py:class:`AuthVal <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal>`
                
                .. attribute:: ospfv2_neighbor
                
                	All the neighbors on the interface
                	**type**\: list of  		 :py:class:`Ospfv2Neighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.Ospfv2Neighbor>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface, self).__init__()

                    self.yang_name = "ospfv2-interface"
                    self.yang_parent_name = "ospfv2-area"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("ttl-security-val", ("ttl_security_val", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.TtlSecurityVal)), ("auth-val", ("auth_val", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal)), ("ospfv2-neighbor", ("ospfv2_neighbor", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.Ospfv2Neighbor))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('network_type', (YLeaf(YType.enumeration, 'network-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'OspfNetworkType', '')])),
                        ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                        ('passive', (YLeaf(YType.boolean, 'passive'), ['bool'])),
                        ('demand_circuit', (YLeaf(YType.boolean, 'demand-circuit'), ['bool'])),
                        ('mtu_ignore', (YLeaf(YType.boolean, 'mtu-ignore'), ['bool'])),
                        ('prefix_suppresion', (YLeaf(YType.boolean, 'prefix-suppresion'), ['bool'])),
                        ('cost', (YLeaf(YType.uint16, 'cost'), ['int'])),
                        ('hello_interval', (YLeaf(YType.uint16, 'hello-interval'), ['int'])),
                        ('dead_interval', (YLeaf(YType.uint16, 'dead-interval'), ['int'])),
                        ('retransmit_interval', (YLeaf(YType.uint16, 'retransmit-interval'), ['int'])),
                        ('transmit_delay', (YLeaf(YType.uint16, 'transmit-delay'), ['int'])),
                        ('hello_timer', (YLeaf(YType.uint32, 'hello-timer'), ['int'])),
                        ('wait_timer', (YLeaf(YType.uint32, 'wait-timer'), ['int'])),
                        ('dr', (YLeaf(YType.uint32, 'dr'), ['int'])),
                        ('bdr', (YLeaf(YType.uint32, 'bdr'), ['int'])),
                        ('dr_ip', (YLeaf(YType.str, 'dr-ip'), ['str','str'])),
                        ('bdr_ip', (YLeaf(YType.str, 'bdr-ip'), ['str','str'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'Ospfv2IntfState', '')])),
                    ])
                    self.name = None
                    self.network_type = None
                    self.enable = None
                    self.passive = None
                    self.demand_circuit = None
                    self.mtu_ignore = None
                    self.prefix_suppresion = None
                    self.cost = None
                    self.hello_interval = None
                    self.dead_interval = None
                    self.retransmit_interval = None
                    self.transmit_delay = None
                    self.hello_timer = None
                    self.wait_timer = None
                    self.dr = None
                    self.bdr = None
                    self.dr_ip = None
                    self.bdr_ip = None
                    self.state = None

                    self.ttl_security_val = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.TtlSecurityVal()
                    self.ttl_security_val.parent = self
                    self._children_name_map["ttl_security_val"] = "ttl-security-val"

                    self.auth_val = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal()
                    self.auth_val.parent = self
                    self._children_name_map["auth_val"] = "auth-val"

                    self.ospfv2_neighbor = YList(self)
                    self._segment_path = lambda: "ospfv2-interface" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface, ['name', 'network_type', 'enable', 'passive', 'demand_circuit', 'mtu_ignore', 'prefix_suppresion', 'cost', 'hello_interval', 'dead_interval', 'retransmit_interval', 'transmit_delay', 'hello_timer', 'wait_timer', 'dr', 'bdr', 'dr_ip', 'bdr_ip', 'state'], name, value)


                class TtlSecurityVal(Entity):
                    """
                    The TTL security information
                    
                    .. attribute:: enable
                    
                    	Indicates whether time to live security is enabled
                    	**type**\: bool
                    
                    .. attribute:: hops
                    
                    	Number of hops for time to live security
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.TtlSecurityVal, self).__init__()

                        self.yang_name = "ttl-security-val"
                        self.yang_parent_name = "ospfv2-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ('hops', (YLeaf(YType.int32, 'hops'), ['int'])),
                        ])
                        self.enable = None
                        self.hops = None
                        self._segment_path = lambda: "ttl-security-val"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.TtlSecurityVal, ['enable', 'hops'], name, value)


                class AuthVal(Entity):
                    """
                    The authentication information
                    
                    .. attribute:: no_auth
                    
                    	No authentication in use
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auth_key
                    
                    	Trailer key chain information
                    	**type**\:  :py:class:`AuthKey <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.AuthKey>`
                    
                    .. attribute:: key_chain
                    
                    	Trailer key information
                    	**type**\:  :py:class:`KeyChain <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.KeyChain>`
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal, self).__init__()

                        self.yang_name = "auth-val"
                        self.yang_parent_name = "ospfv2-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("auth-key", ("auth_key", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.AuthKey)), ("key-chain", ("key_chain", OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.KeyChain))])
                        self._leafs = OrderedDict([
                            ('no_auth', (YLeaf(YType.uint32, 'no-auth'), ['int'])),
                        ])
                        self.no_auth = None

                        self.auth_key = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.AuthKey()
                        self.auth_key.parent = self
                        self._children_name_map["auth_key"] = "auth-key"

                        self.key_chain = OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.KeyChain()
                        self.key_chain.parent = self
                        self._children_name_map["key_chain"] = "key-chain"
                        self._segment_path = lambda: "auth-val"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal, ['no_auth'], name, value)


                    class AuthKey(Entity):
                        """
                        Trailer key chain information
                        
                        .. attribute:: key_id
                        
                        	The key identifier
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: key_string
                        
                        	The key string
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: crypto_algo
                        
                        	The algorithm in use
                        	**type**\:  :py:class:`Ospfv2CryptoAlgorithm <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2CryptoAlgorithm>`
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.AuthKey, self).__init__()

                            self.yang_name = "auth-key"
                            self.yang_parent_name = "auth-val"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('key_id', (YLeaf(YType.uint8, 'key-id'), ['int'])),
                                ('key_string', (YLeafList(YType.uint8, 'key-string'), ['int'])),
                                ('crypto_algo', (YLeaf(YType.enumeration, 'crypto-algo'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'Ospfv2CryptoAlgorithm', '')])),
                            ])
                            self.key_id = None
                            self.key_string = []
                            self.crypto_algo = None
                            self._segment_path = lambda: "auth-key"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.AuthKey, ['key_id', 'key_string', 'crypto_algo'], name, value)


                    class KeyChain(Entity):
                        """
                        Trailer key information
                        
                        .. attribute:: key_chain
                        
                        	The key chain
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'ospf-ios-xe-oper'
                        _revision = '2018-02-01'

                        def __init__(self):
                            super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.KeyChain, self).__init__()

                            self.yang_name = "key-chain"
                            self.yang_parent_name = "auth-val"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('key_chain', (YLeafList(YType.uint8, 'key-chain'), ['int'])),
                            ])
                            self.key_chain = []
                            self._segment_path = lambda: "key-chain"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.AuthVal.KeyChain, ['key_chain'], name, value)


                class Ospfv2Neighbor(Entity):
                    """
                    All the neighbors on the interface
                    
                    .. attribute:: nbr_id  (key)
                    
                    	The neighbor identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address
                    
                    	Neighbor address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: dr
                    
                    	The neighbor's Designated Router indentifier 
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bdr
                    
                    	The neighbor's Backup Designated Router identifier
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dr_ip
                    
                    	The designated routers' IP address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: bdr_ip
                    
                    	The backup designated routers' IP address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: event_count
                    
                    	A count of neighbor events
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: retrans_count
                    
                    	A count of the retransmission events
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: state
                    
                    	The current neighbor state
                    	**type**\:  :py:class:`NbrStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.NbrStateType>`
                    
                    .. attribute:: dead_timer
                    
                    	The dead timer in seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.Ospfv2Neighbor, self).__init__()

                        self.yang_name = "ospfv2-neighbor"
                        self.yang_parent_name = "ospfv2-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['nbr_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('nbr_id', (YLeaf(YType.uint32, 'nbr-id'), ['int'])),
                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                            ('dr', (YLeaf(YType.uint32, 'dr'), ['int'])),
                            ('bdr', (YLeaf(YType.uint32, 'bdr'), ['int'])),
                            ('dr_ip', (YLeaf(YType.str, 'dr-ip'), ['str','str'])),
                            ('bdr_ip', (YLeaf(YType.str, 'bdr-ip'), ['str','str'])),
                            ('event_count', (YLeaf(YType.uint32, 'event-count'), ['int'])),
                            ('retrans_count', (YLeaf(YType.uint32, 'retrans-count'), ['int'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'NbrStateType', '')])),
                            ('dead_timer', (YLeaf(YType.uint32, 'dead-timer'), ['int'])),
                        ])
                        self.nbr_id = None
                        self.address = None
                        self.dr = None
                        self.bdr = None
                        self.dr_ip = None
                        self.bdr_ip = None
                        self.event_count = None
                        self.retrans_count = None
                        self.state = None
                        self.dead_timer = None
                        self._segment_path = lambda: "ospfv2-neighbor" + "[nbr-id='" + str(self.nbr_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2Area.Ospfv2Interface.Ospfv2Neighbor, ['nbr_id', 'address', 'dr', 'bdr', 'dr_ip', 'bdr_ip', 'event_count', 'retrans_count', 'state', 'dead_timer'], name, value)


        class Ospfv2LsdbExternal(Entity):
            """
            The external LSDB information
            
            .. attribute:: lsa_type  (key)
            
            	Link State Advertisement type
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: lsa_id  (key)
            
            	Link State Advertisement Identifer
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: advertising_router  (key)
            
            	Advertising router
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lsa_age
            
            	The age of the Link State Advertisement
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: lsa_options
            
            	The options of the Link State Advertisement
            	**type**\:  :py:class:`Ospfv2LsaFlagOptions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2LsaFlagOptions>`
            
            .. attribute:: lsa_seq_number
            
            	The sequence number for the Link State Advertisement
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: lsa_checksum
            
            	The checksum of the Link State Advertisement
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: lsa_length
            
            	The length, in bytes, of the Link State Advertisement
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ospfv2_router_lsa_links
            
            	The router Link State Advertisement links
            	**type**\: list of  		 :py:class:`Ospfv2RouterLsaLinks <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks>`
            
            .. attribute:: unsupported_lsa
            
            	The unsupported Link State Advertisements
            	**type**\:  :py:class:`UnsupportedLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.UnsupportedLsa>`
            
            .. attribute:: router_lsa
            
            	The router Link State Advertisements
            	**type**\:  :py:class:`RouterLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterLsa>`
            
            .. attribute:: network_lsa
            
            	The network Link State Advertisements
            	**type**\:  :py:class:`NetworkLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkLsa>`
            
            .. attribute:: network_summary_lsa
            
            	The network summary Link State Advertisements
            	**type**\:  :py:class:`NetworkSummaryLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa>`
            
            .. attribute:: router_summary_lsa
            
            	The router summary Link State Advertisements
            	**type**\:  :py:class:`RouterSummaryLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa>`
            
            .. attribute:: external_lsa
            
            	The external Link State Advertisements
            	**type**\:  :py:class:`ExternalLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa>`
            
            .. attribute:: nssa_lsa
            
            	The Not So Stubby Area Link state advertisements
            	**type**\:  :py:class:`NssaLsa <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa>`
            
            

            """

            _prefix = 'ospf-ios-xe-oper'
            _revision = '2018-02-01'

            def __init__(self):
                super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal, self).__init__()

                self.yang_name = "ospfv2-lsdb-external"
                self.yang_parent_name = "ospfv2-instance"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['lsa_type','lsa_id','advertising_router']
                self._child_classes = OrderedDict([("ospfv2-router-lsa-links", ("ospfv2_router_lsa_links", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks)), ("unsupported-lsa", ("unsupported_lsa", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.UnsupportedLsa)), ("router-lsa", ("router_lsa", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterLsa)), ("network-lsa", ("network_lsa", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkLsa)), ("network-summary-lsa", ("network_summary_lsa", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa)), ("router-summary-lsa", ("router_summary_lsa", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa)), ("external-lsa", ("external_lsa", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa)), ("nssa-lsa", ("nssa_lsa", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa))])
                self._leafs = OrderedDict([
                    ('lsa_type', (YLeaf(YType.uint8, 'lsa-type'), ['int'])),
                    ('lsa_id', (YLeaf(YType.uint32, 'lsa-id'), ['int'])),
                    ('advertising_router', (YLeaf(YType.uint32, 'advertising-router'), ['int'])),
                    ('lsa_age', (YLeaf(YType.uint16, 'lsa-age'), ['int'])),
                    ('lsa_options', (YLeaf(YType.bits, 'lsa-options'), ['Bits'])),
                    ('lsa_seq_number', (YLeaf(YType.uint32, 'lsa-seq-number'), ['int'])),
                    ('lsa_checksum', (YLeaf(YType.uint16, 'lsa-checksum'), ['int'])),
                    ('lsa_length', (YLeaf(YType.uint16, 'lsa-length'), ['int'])),
                ])
                self.lsa_type = None
                self.lsa_id = None
                self.advertising_router = None
                self.lsa_age = None
                self.lsa_options = Bits()
                self.lsa_seq_number = None
                self.lsa_checksum = None
                self.lsa_length = None

                self.unsupported_lsa = OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.UnsupportedLsa()
                self.unsupported_lsa.parent = self
                self._children_name_map["unsupported_lsa"] = "unsupported-lsa"

                self.router_lsa = OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterLsa()
                self.router_lsa.parent = self
                self._children_name_map["router_lsa"] = "router-lsa"

                self.network_lsa = OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkLsa()
                self.network_lsa.parent = self
                self._children_name_map["network_lsa"] = "network-lsa"

                self.network_summary_lsa = OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa()
                self.network_summary_lsa.parent = self
                self._children_name_map["network_summary_lsa"] = "network-summary-lsa"

                self.router_summary_lsa = OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa()
                self.router_summary_lsa.parent = self
                self._children_name_map["router_summary_lsa"] = "router-summary-lsa"

                self.external_lsa = OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa()
                self.external_lsa.parent = self
                self._children_name_map["external_lsa"] = "external-lsa"

                self.nssa_lsa = OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa()
                self.nssa_lsa.parent = self
                self._children_name_map["nssa_lsa"] = "nssa-lsa"

                self.ospfv2_router_lsa_links = YList(self)
                self._segment_path = lambda: "ospfv2-lsdb-external" + "[lsa-type='" + str(self.lsa_type) + "']" + "[lsa-id='" + str(self.lsa_id) + "']" + "[advertising-router='" + str(self.advertising_router) + "']"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal, ['lsa_type', 'lsa_id', 'advertising_router', 'lsa_age', 'lsa_options', 'lsa_seq_number', 'lsa_checksum', 'lsa_length'], name, value)


            class Ospfv2RouterLsaLinks(Entity):
                """
                The router Link State Advertisement links
                
                .. attribute:: link_type  (key)
                
                	Link Type
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: link_id  (key)
                
                	link Identifier
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: link_data  (key)
                
                	link data
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: link_topo
                
                	Link topology
                	**type**\: list of  		 :py:class:`LinkTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks.LinkTopo>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks, self).__init__()

                    self.yang_name = "ospfv2-router-lsa-links"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['link_type','link_id','link_data']
                    self._child_classes = OrderedDict([("link-topo", ("link_topo", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks.LinkTopo))])
                    self._leafs = OrderedDict([
                        ('link_type', (YLeaf(YType.uint8, 'link-type'), ['int'])),
                        ('link_id', (YLeaf(YType.uint32, 'link-id'), ['int'])),
                        ('link_data', (YLeaf(YType.uint32, 'link-data'), ['int'])),
                    ])
                    self.link_type = None
                    self.link_id = None
                    self.link_data = None

                    self.link_topo = YList(self)
                    self._segment_path = lambda: "ospfv2-router-lsa-links" + "[link-type='" + str(self.link_type) + "']" + "[link-id='" + str(self.link_id) + "']" + "[link-data='" + str(self.link_data) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks, ['link_type', 'link_id', 'link_data'], name, value)


                class LinkTopo(Entity):
                    """
                    Link topology
                    
                    .. attribute:: mt_id
                    
                    	Multi topology identifier
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: topo_metric
                    
                    	Topology metric
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks.LinkTopo, self).__init__()

                        self.yang_name = "link-topo"
                        self.yang_parent_name = "ospfv2-router-lsa-links"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                            ('topo_metric', (YLeaf(YType.uint16, 'topo-metric'), ['int'])),
                        ])
                        self.mt_id = None
                        self.topo_metric = None
                        self._segment_path = lambda: "link-topo"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.Ospfv2RouterLsaLinks.LinkTopo, ['mt_id', 'topo_metric'], name, value)


            class UnsupportedLsa(Entity):
                """
                The unsupported Link State Advertisements
                
                .. attribute:: lsa_data
                
                	Link State Advertisement data
                	**type**\: list of int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.UnsupportedLsa, self).__init__()

                    self.yang_name = "unsupported-lsa"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lsa_data', (YLeafList(YType.uint8, 'lsa-data'), ['int'])),
                    ])
                    self.lsa_data = []
                    self._segment_path = lambda: "unsupported-lsa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.UnsupportedLsa, ['lsa_data'], name, value)


            class RouterLsa(Entity):
                """
                The router Link State Advertisements
                
                .. attribute:: router_lsa_bits
                
                	Router Link State Advertisement bits
                	**type**\:  :py:class:`Ospfv2RouterLsaBits <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.Ospfv2RouterLsaBits>`
                
                .. attribute:: router_lsa_number_links
                
                	Router Link State Advertisement number of links
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterLsa, self).__init__()

                    self.yang_name = "router-lsa"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('router_lsa_bits', (YLeaf(YType.bits, 'router-lsa-bits'), ['Bits'])),
                        ('router_lsa_number_links', (YLeaf(YType.uint16, 'router-lsa-number-links'), ['int'])),
                    ])
                    self.router_lsa_bits = Bits()
                    self.router_lsa_number_links = None
                    self._segment_path = lambda: "router-lsa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterLsa, ['router_lsa_bits', 'router_lsa_number_links'], name, value)


            class NetworkLsa(Entity):
                """
                The network Link State Advertisements
                
                .. attribute:: network_lsa_mask
                
                	Network Link State Advertisement mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: network_attached_routers
                
                	Network attached routers
                	**type**\: list of int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkLsa, self).__init__()

                    self.yang_name = "network-lsa"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('network_lsa_mask', (YLeaf(YType.uint32, 'network-lsa-mask'), ['int'])),
                        ('network_attached_routers', (YLeafList(YType.uint32, 'network-attached-routers'), ['int'])),
                    ])
                    self.network_lsa_mask = None
                    self.network_attached_routers = []
                    self._segment_path = lambda: "network-lsa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkLsa, ['network_lsa_mask', 'network_attached_routers'], name, value)


            class NetworkSummaryLsa(Entity):
                """
                The network summary Link State Advertisements
                
                .. attribute:: summary_lsa_mask
                
                	The summary Link State Advertisement mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: summary_topo
                
                	The summary topology
                	**type**\: list of  		 :py:class:`SummaryTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa.SummaryTopo>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa, self).__init__()

                    self.yang_name = "network-summary-lsa"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("summary-topo", ("summary_topo", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa.SummaryTopo))])
                    self._leafs = OrderedDict([
                        ('summary_lsa_mask', (YLeaf(YType.uint32, 'summary-lsa-mask'), ['int'])),
                    ])
                    self.summary_lsa_mask = None

                    self.summary_topo = YList(self)
                    self._segment_path = lambda: "network-summary-lsa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa, ['summary_lsa_mask'], name, value)


                class SummaryTopo(Entity):
                    """
                    The summary topology
                    
                    .. attribute:: mt_id
                    
                    	Multi topology identifier
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: topo_metric
                    
                    	Topology Metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa.SummaryTopo, self).__init__()

                        self.yang_name = "summary-topo"
                        self.yang_parent_name = "network-summary-lsa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                            ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                        ])
                        self.mt_id = None
                        self.topo_metric = None
                        self._segment_path = lambda: "summary-topo"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NetworkSummaryLsa.SummaryTopo, ['mt_id', 'topo_metric'], name, value)


            class RouterSummaryLsa(Entity):
                """
                The router summary Link State Advertisements
                
                .. attribute:: summary_lsa_mask
                
                	The summary Link State Advertisement mask
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: summary_topo
                
                	The summary topology
                	**type**\: list of  		 :py:class:`SummaryTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa.SummaryTopo>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa, self).__init__()

                    self.yang_name = "router-summary-lsa"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("summary-topo", ("summary_topo", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa.SummaryTopo))])
                    self._leafs = OrderedDict([
                        ('summary_lsa_mask', (YLeaf(YType.uint32, 'summary-lsa-mask'), ['int'])),
                    ])
                    self.summary_lsa_mask = None

                    self.summary_topo = YList(self)
                    self._segment_path = lambda: "router-summary-lsa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa, ['summary_lsa_mask'], name, value)


                class SummaryTopo(Entity):
                    """
                    The summary topology
                    
                    .. attribute:: mt_id
                    
                    	Multi topology identifier
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: topo_metric
                    
                    	Topology Metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa.SummaryTopo, self).__init__()

                        self.yang_name = "summary-topo"
                        self.yang_parent_name = "router-summary-lsa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                            ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                        ])
                        self.mt_id = None
                        self.topo_metric = None
                        self._segment_path = lambda: "summary-topo"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.RouterSummaryLsa.SummaryTopo, ['mt_id', 'topo_metric'], name, value)


            class ExternalLsa(Entity):
                """
                The external Link State Advertisements
                
                .. attribute:: external_lsa_mask
                
                	The mask for the external Link State Advertisement
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: external_topo
                
                	The external topology Link State Advertisement
                	**type**\: list of  		 :py:class:`ExternalTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa.ExternalTopo>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa, self).__init__()

                    self.yang_name = "external-lsa"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("external-topo", ("external_topo", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa.ExternalTopo))])
                    self._leafs = OrderedDict([
                        ('external_lsa_mask', (YLeaf(YType.uint32, 'external-lsa-mask'), ['int'])),
                    ])
                    self.external_lsa_mask = None

                    self.external_topo = YList(self)
                    self._segment_path = lambda: "external-lsa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa, ['external_lsa_mask'], name, value)


                class ExternalTopo(Entity):
                    """
                    The external topology Link State Advertisement
                    
                    .. attribute:: mt_id
                    
                    	The multi topology identifier
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: topo_metric_type
                    
                    	The topoligy metric type associated with the  Link State Advertisement
                    	**type**\:  :py:class:`OspfExternalMetricType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfExternalMetricType>`
                    
                    .. attribute:: topo_metric
                    
                    	The topology metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: topo_forwarding_address
                    
                    	The topology forwarding address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: topo_route_tag
                    
                    	The topology route tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa.ExternalTopo, self).__init__()

                        self.yang_name = "external-topo"
                        self.yang_parent_name = "external-lsa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                            ('topo_metric_type', (YLeaf(YType.enumeration, 'topo-metric-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'OspfExternalMetricType', '')])),
                            ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                            ('topo_forwarding_address', (YLeaf(YType.str, 'topo-forwarding-address'), ['str','str'])),
                            ('topo_route_tag', (YLeaf(YType.uint32, 'topo-route-tag'), ['int'])),
                        ])
                        self.mt_id = None
                        self.topo_metric_type = None
                        self.topo_metric = None
                        self.topo_forwarding_address = None
                        self.topo_route_tag = None
                        self._segment_path = lambda: "external-topo"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.ExternalLsa.ExternalTopo, ['mt_id', 'topo_metric_type', 'topo_metric', 'topo_forwarding_address', 'topo_route_tag'], name, value)


            class NssaLsa(Entity):
                """
                The Not So Stubby Area Link state advertisements
                
                .. attribute:: external_lsa_mask
                
                	The mask for the external Link State Advertisement
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: external_topo
                
                	The external topology Link State Advertisement
                	**type**\: list of  		 :py:class:`ExternalTopo <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa.ExternalTopo>`
                
                

                """

                _prefix = 'ospf-ios-xe-oper'
                _revision = '2018-02-01'

                def __init__(self):
                    super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa, self).__init__()

                    self.yang_name = "nssa-lsa"
                    self.yang_parent_name = "ospfv2-lsdb-external"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("external-topo", ("external_topo", OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa.ExternalTopo))])
                    self._leafs = OrderedDict([
                        ('external_lsa_mask', (YLeaf(YType.uint32, 'external-lsa-mask'), ['int'])),
                    ])
                    self.external_lsa_mask = None

                    self.external_topo = YList(self)
                    self._segment_path = lambda: "nssa-lsa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa, ['external_lsa_mask'], name, value)


                class ExternalTopo(Entity):
                    """
                    The external topology Link State Advertisement
                    
                    .. attribute:: mt_id
                    
                    	The multi topology identifier
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: topo_metric_type
                    
                    	The topoligy metric type associated with the  Link State Advertisement
                    	**type**\:  :py:class:`OspfExternalMetricType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper.OspfExternalMetricType>`
                    
                    .. attribute:: topo_metric
                    
                    	The topology metric
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: topo_forwarding_address
                    
                    	The topology forwarding address
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: topo_route_tag
                    
                    	The topology route tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ospf-ios-xe-oper'
                    _revision = '2018-02-01'

                    def __init__(self):
                        super(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa.ExternalTopo, self).__init__()

                        self.yang_name = "external-topo"
                        self.yang_parent_name = "nssa-lsa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mt_id', (YLeaf(YType.uint8, 'mt-id'), ['int'])),
                            ('topo_metric_type', (YLeaf(YType.enumeration, 'topo-metric-type'), [('ydk.models.cisco_ios_xe.Cisco_IOS_XE_ospf_oper', 'OspfExternalMetricType', '')])),
                            ('topo_metric', (YLeaf(YType.uint32, 'topo-metric'), ['int'])),
                            ('topo_forwarding_address', (YLeaf(YType.str, 'topo-forwarding-address'), ['str','str'])),
                            ('topo_route_tag', (YLeaf(YType.uint32, 'topo-route-tag'), ['int'])),
                        ])
                        self.mt_id = None
                        self.topo_metric_type = None
                        self.topo_metric = None
                        self.topo_forwarding_address = None
                        self.topo_route_tag = None
                        self._segment_path = lambda: "external-topo"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(OspfOperData.Ospfv2Instance.Ospfv2LsdbExternal.NssaLsa.ExternalTopo, ['mt_id', 'topo_metric_type', 'topo_metric', 'topo_forwarding_address', 'topo_route_tag'], name, value)

    def clone_ptr(self):
        self._top_entity = OspfOperData()
        return self._top_entity

