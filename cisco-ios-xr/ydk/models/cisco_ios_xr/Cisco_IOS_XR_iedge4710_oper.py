""" Cisco_IOS_XR_iedge4710_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR iedge4710 package operational data.

This module contains definitions
for the following management objects\:
  subscriber\: Subscriber operational data
  iedge\-license\-manager\: iedge license manager

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AaaAuthService(Enum):
    """
    AaaAuthService

    AAA authorization service types

    .. data:: none = 0

    	None

    .. data:: login = 1

    	Login

    .. data:: framed = 2

    	Framed

    .. data:: callback_login = 3

    	Callback login

    .. data:: callback_framed = 4

    	Callback framed

    .. data:: outbound = 5

    	Outbound

    .. data:: administrator = 6

    	Administrator

    .. data:: prompt = 7

    	Prompt

    .. data:: authentication_only = 8

    	Authentication only

    .. data:: callback_nas_prompt = 9

    	Callback NAS prompt

    .. data:: call_check = 10

    	Call check

    .. data:: callback_administrator = 11

    	Callback administrator

    .. data:: voice = 12

    	Voice

    .. data:: fax = 13

    	Fax

    .. data:: modem_relay = 14

    	Modem relay

    .. data:: eap_over_udp = 15

    	EAP over UDP

    """

    none = Enum.YLeaf(0, "none")

    login = Enum.YLeaf(1, "login")

    framed = Enum.YLeaf(2, "framed")

    callback_login = Enum.YLeaf(3, "callback-login")

    callback_framed = Enum.YLeaf(4, "callback-framed")

    outbound = Enum.YLeaf(5, "outbound")

    administrator = Enum.YLeaf(6, "administrator")

    prompt = Enum.YLeaf(7, "prompt")

    authentication_only = Enum.YLeaf(8, "authentication-only")

    callback_nas_prompt = Enum.YLeaf(9, "callback-nas-prompt")

    call_check = Enum.YLeaf(10, "call-check")

    callback_administrator = Enum.YLeaf(11, "callback-administrator")

    voice = Enum.YLeaf(12, "voice")

    fax = Enum.YLeaf(13, "fax")

    modem_relay = Enum.YLeaf(14, "modem-relay")

    eap_over_udp = Enum.YLeaf(15, "eap-over-udp")


class AaaInterface(Enum):
    """
    AaaInterface

    AAA interface types

    .. data:: none = 0

    	None

    .. data:: primary_rate = 1

    	Primary rate

    .. data:: basic_rate = 2

    	Basic rate

    .. data:: serial = 3

    	Serial

    .. data:: asynchronous = 4

    	Asynchronous

    .. data:: vty = 5

    	VTY

    .. data:: atm = 6

    	ATM

    .. data:: ethernet = 7

    	Ethernet

    .. data:: ppp_over_atm = 8

    	PPP over ATM

    .. data:: pppoe_over_atm = 9

    	PPPoE over ATM

    .. data:: pppoe_over_ethernet = 10

    	PPPoE over ethernet

    .. data:: ppp_over_vlan = 11

    	PPP over VLAN

    .. data:: ppp_over_qinq = 12

    	PPP over Q in Q

    .. data:: v120 = 13

    	V120

    .. data:: v110 = 14

    	V110

    .. data:: piafs = 15

    	PHS internet access forum standard

    .. data:: x75 = 16

    	X75

    .. data:: ip_sec = 17

    	IP sec

    .. data:: other = 18

    	Other

    .. data:: virtual_pppoe_over_ethernet = 19

    	Virtual PPPoE over ethernet

    .. data:: virtual_pppoe_over_vlan = 20

    	Virtual PPPoE over VLAN

    .. data:: virtual_pppoe_over_qinq = 21

    	Virtual PPPoE over Q in Q

    .. data:: ipo_e_over_ethernet = 22

    	IPoE over ethernet

    .. data:: ipo_e_over_vlan = 23

    	IPoE over VLAN

    .. data:: ipo_e_over_qinq = 24

    	IPoE over Q in Q

    .. data:: virtual_i_po_e_over_ethernet = 25

    	Virtual IPoE over ethernet

    .. data:: virtual_i_po_e_over_vlan = 26

    	Virtual IPoE over VLAN

    .. data:: virtual_i_po_e_over_qinq = 27

    	Virtual IPoE over Q in Q

    """

    none = Enum.YLeaf(0, "none")

    primary_rate = Enum.YLeaf(1, "primary-rate")

    basic_rate = Enum.YLeaf(2, "basic-rate")

    serial = Enum.YLeaf(3, "serial")

    asynchronous = Enum.YLeaf(4, "asynchronous")

    vty = Enum.YLeaf(5, "vty")

    atm = Enum.YLeaf(6, "atm")

    ethernet = Enum.YLeaf(7, "ethernet")

    ppp_over_atm = Enum.YLeaf(8, "ppp-over-atm")

    pppoe_over_atm = Enum.YLeaf(9, "pppoe-over-atm")

    pppoe_over_ethernet = Enum.YLeaf(10, "pppoe-over-ethernet")

    ppp_over_vlan = Enum.YLeaf(11, "ppp-over-vlan")

    ppp_over_qinq = Enum.YLeaf(12, "ppp-over-qinq")

    v120 = Enum.YLeaf(13, "v120")

    v110 = Enum.YLeaf(14, "v110")

    piafs = Enum.YLeaf(15, "piafs")

    x75 = Enum.YLeaf(16, "x75")

    ip_sec = Enum.YLeaf(17, "ip-sec")

    other = Enum.YLeaf(18, "other")

    virtual_pppoe_over_ethernet = Enum.YLeaf(19, "virtual-pppoe-over-ethernet")

    virtual_pppoe_over_vlan = Enum.YLeaf(20, "virtual-pppoe-over-vlan")

    virtual_pppoe_over_qinq = Enum.YLeaf(21, "virtual-pppoe-over-qinq")

    ipo_e_over_ethernet = Enum.YLeaf(22, "ipo-e-over-ethernet")

    ipo_e_over_vlan = Enum.YLeaf(23, "ipo-e-over-vlan")

    ipo_e_over_qinq = Enum.YLeaf(24, "ipo-e-over-qinq")

    virtual_i_po_e_over_ethernet = Enum.YLeaf(25, "virtual-i-po-e-over-ethernet")

    virtual_i_po_e_over_vlan = Enum.YLeaf(26, "virtual-i-po-e-over-vlan")

    virtual_i_po_e_over_qinq = Enum.YLeaf(27, "virtual-i-po-e-over-qinq")


class AaaTerminateCause(Enum):
    """
    AaaTerminateCause

    AAA terminate cause types

    .. data:: none = 0

    	None

    .. data:: user_request = 1

    	User request

    .. data:: lost_carrier = 2

    	Lost carrier

    .. data:: lost_service = 3

    	Lost service

    .. data:: idle_timeout = 4

    	Idle timeout

    .. data:: session_timeout = 5

    	Session timeout

    .. data:: admin_reset = 6

    	Admin reset

    .. data:: admin_reboot = 7

    	Admin reboot

    .. data:: port_error = 8

    	Port error

    .. data:: nas_error = 9

    	NAS error

    .. data:: nas_request = 10

    	NAS request

    .. data:: nas_reboot = 11

    	NAS reboot

    .. data:: port_unneeded = 12

    	Port unneeded

    .. data:: port_preempted = 13

    	Port preempted

    .. data:: port_suspended = 14

    	Port suspended

    .. data:: service_unavailable = 15

    	Service unavailable

    .. data:: callback = 16

    	Callback

    .. data:: user_error = 17

    	User error

    .. data:: host_request = 18

    	Host request

    .. data:: supplicant_restart = 19

    	Supplicant restart

    .. data:: reauthorization_failure = 20

    	Reauthorization failure

    .. data:: port_reinitialized = 21

    	Port reinitialized

    .. data:: admin_disabled = 22

    	Admin disabled

    """

    none = Enum.YLeaf(0, "none")

    user_request = Enum.YLeaf(1, "user-request")

    lost_carrier = Enum.YLeaf(2, "lost-carrier")

    lost_service = Enum.YLeaf(3, "lost-service")

    idle_timeout = Enum.YLeaf(4, "idle-timeout")

    session_timeout = Enum.YLeaf(5, "session-timeout")

    admin_reset = Enum.YLeaf(6, "admin-reset")

    admin_reboot = Enum.YLeaf(7, "admin-reboot")

    port_error = Enum.YLeaf(8, "port-error")

    nas_error = Enum.YLeaf(9, "nas-error")

    nas_request = Enum.YLeaf(10, "nas-request")

    nas_reboot = Enum.YLeaf(11, "nas-reboot")

    port_unneeded = Enum.YLeaf(12, "port-unneeded")

    port_preempted = Enum.YLeaf(13, "port-preempted")

    port_suspended = Enum.YLeaf(14, "port-suspended")

    service_unavailable = Enum.YLeaf(15, "service-unavailable")

    callback = Enum.YLeaf(16, "callback")

    user_error = Enum.YLeaf(17, "user-error")

    host_request = Enum.YLeaf(18, "host-request")

    supplicant_restart = Enum.YLeaf(19, "supplicant-restart")

    reauthorization_failure = Enum.YLeaf(20, "reauthorization-failure")

    port_reinitialized = Enum.YLeaf(21, "port-reinitialized")

    admin_disabled = Enum.YLeaf(22, "admin-disabled")


class AaaTunnelMedium(Enum):
    """
    AaaTunnelMedium

    Tunnel medium types

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    .. data:: nsap = 3

    	NSAP

    .. data:: hdlc = 4

    	HDLC

    .. data:: bbn = 5

    	BBN

    .. data:: all802 = 6

    	ALL 802

    """

    none = Enum.YLeaf(0, "none")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    nsap = Enum.YLeaf(3, "nsap")

    hdlc = Enum.YLeaf(4, "hdlc")

    bbn = Enum.YLeaf(5, "bbn")

    all802 = Enum.YLeaf(6, "all802")


class AaaTunnelProto(Enum):
    """
    AaaTunnelProto

    Tunnel protocol types

    .. data:: none = 0

    	None

    .. data:: pptp = 1

    	Point-to-point tunneling protocol

    .. data:: l2f = 2

    	Layer 2 forwarding

    .. data:: l2tp = 3

    	Layer 2 tunneling protocol

    .. data:: atmp = 4

    	Ascend tunnel management protocol

    .. data:: vtp = 5

    	VLAN trunk protocol

    .. data:: ah = 6

    	Authentication header

    .. data:: ip_over_ip = 7

    	IP over IP

    .. data:: minimum_ip_over_ip = 8

    	Minimum IP over IP

    .. data:: esp = 9

    	Encapsulating security payload

    .. data:: gre = 10

    	Generic routing encapsulation

    .. data:: bay_dvs = 11

    	Bay dial virtual services

    .. data:: ip_in_ip = 12

    	IP in IP

    .. data:: vlan = 13

    	VLAN

    """

    none = Enum.YLeaf(0, "none")

    pptp = Enum.YLeaf(1, "pptp")

    l2f = Enum.YLeaf(2, "l2f")

    l2tp = Enum.YLeaf(3, "l2tp")

    atmp = Enum.YLeaf(4, "atmp")

    vtp = Enum.YLeaf(5, "vtp")

    ah = Enum.YLeaf(6, "ah")

    ip_over_ip = Enum.YLeaf(7, "ip-over-ip")

    minimum_ip_over_ip = Enum.YLeaf(8, "minimum-ip-over-ip")

    esp = Enum.YLeaf(9, "esp")

    gre = Enum.YLeaf(10, "gre")

    bay_dvs = Enum.YLeaf(11, "bay-dvs")

    ip_in_ip = Enum.YLeaf(12, "ip-in-ip")

    vlan = Enum.YLeaf(13, "vlan")


class IedgeOperSession(Enum):
    """
    IedgeOperSession

    Subscriber session types

    .. data:: unknown = 0

    	Unknown

    .. data:: pppoe = 1

    	PPPoE/PPP client

    .. data:: ppp = 2

    	PPP serial client

    .. data:: ip_packet_trigger = 3

    	IP subscriber - packet trigger

    .. data:: ip_packet_dhcp_trigger = 4

    	IP subscriber - DHCP trigger

    """

    unknown = Enum.YLeaf(0, "unknown")

    pppoe = Enum.YLeaf(1, "pppoe")

    ppp = Enum.YLeaf(2, "ppp")

    ip_packet_trigger = Enum.YLeaf(3, "ip-packet-trigger")

    ip_packet_dhcp_trigger = Enum.YLeaf(4, "ip-packet-dhcp-trigger")


class IedgeOperSessionAfState(Enum):
    """
    IedgeOperSessionAfState

    Subscriber session address family state

    .. data:: not_started = 0

    	Not started

    .. data:: down = 1

    	Down

    .. data:: up_pending = 2

    	Up Pending

    .. data:: up = 3

    	Up

    """

    not_started = Enum.YLeaf(0, "not-started")

    down = Enum.YLeaf(1, "down")

    up_pending = Enum.YLeaf(2, "up-pending")

    up = Enum.YLeaf(3, "up")


class IedgeOperSessionState(Enum):
    """
    IedgeOperSessionState

    Subscriber session states

    .. data:: initialize = 0

    	Initialize

    .. data:: connecting = 1

    	Connecting

    .. data:: connected = 2

    	Connected

    .. data:: activated = 3

    	Activated

    .. data:: idle = 4

    	Idle

    .. data:: disconnecting = 5

    	Disconnecting

    .. data:: end = 6

    	End

    """

    initialize = Enum.YLeaf(0, "initialize")

    connecting = Enum.YLeaf(1, "connecting")

    connected = Enum.YLeaf(2, "connected")

    activated = Enum.YLeaf(3, "activated")

    idle = Enum.YLeaf(4, "idle")

    disconnecting = Enum.YLeaf(5, "disconnecting")

    end = Enum.YLeaf(6, "end")


class IedgePppSub(Enum):
    """
    IedgePppSub

    PPPoE sub types

    .. data:: pta = 0

    	PPP termination and aggregation

    .. data:: lac = 1

    	L2TP access controller

    """

    pta = Enum.YLeaf(0, "pta")

    lac = Enum.YLeaf(1, "lac")


class SubscriberAddressFamilyFilterFlag(Enum):
    """
    SubscriberAddressFamilyFilterFlag

    Subscriber address family filter flag

    .. data:: ipv4_only = 0

    	IPv4 only

    .. data:: ipv6_only = 1

    	IPv6 only

    .. data:: ipv4_all = 2

    	IPv4 all

    .. data:: ipv6_all = 3

    	IPv6 all

    .. data:: dual_all = 4

    	Dual all

    .. data:: dual_part_up = 5

    	Dual part up

    .. data:: dual_up = 6

    	Dual up

    .. data:: lac = 7

    	LAC

    """

    ipv4_only = Enum.YLeaf(0, "ipv4-only")

    ipv6_only = Enum.YLeaf(1, "ipv6-only")

    ipv4_all = Enum.YLeaf(2, "ipv4-all")

    ipv6_all = Enum.YLeaf(3, "ipv6-all")

    dual_all = Enum.YLeaf(4, "dual-all")

    dual_part_up = Enum.YLeaf(5, "dual-part-up")

    dual_up = Enum.YLeaf(6, "dual-up")

    lac = Enum.YLeaf(7, "lac")


class SubscriberAuthenStateFilterFlag(Enum):
    """
    SubscriberAuthenStateFilterFlag

    Subscriber authen state filter flag

    .. data:: un_authenticated = 0

    	UnAuthenticated

    .. data:: authenticated = 1

    	Authenticated

    """

    un_authenticated = Enum.YLeaf(0, "un-authenticated")

    authenticated = Enum.YLeaf(1, "authenticated")


class SubscriberAuthorStateFilterFlag(Enum):
    """
    SubscriberAuthorStateFilterFlag

    Subscriber author state filter flag

    .. data:: un_authorized = 0

    	UnAuthorized

    .. data:: authorized = 1

    	Authorized

    """

    un_authorized = Enum.YLeaf(0, "un-authorized")

    authorized = Enum.YLeaf(1, "authorized")


class SubscriberStateFilterFlag(Enum):
    """
    SubscriberStateFilterFlag

    Subscriber state filter flag

    .. data:: initializing = 0

    	Initializing

    .. data:: connecting = 1

    	Connecting

    .. data:: connected = 2

    	Connected

    .. data:: activated = 3

    	Activated

    .. data:: idle = 4

    	Idle

    .. data:: disconnecting = 5

    	Disconnecting

    .. data:: end = 6

    	End

    """

    initializing = Enum.YLeaf(0, "initializing")

    connecting = Enum.YLeaf(1, "connecting")

    connected = Enum.YLeaf(2, "connected")

    activated = Enum.YLeaf(3, "activated")

    idle = Enum.YLeaf(4, "idle")

    disconnecting = Enum.YLeaf(5, "disconnecting")

    end = Enum.YLeaf(6, "end")



class Subscriber(Entity):
    """
    Subscriber operational data
    
    .. attribute:: manager
    
    	Subscriber manager operational data
    	**type**\:  :py:class:`Manager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager>`
    
    .. attribute:: session
    
    	Subscriber session operational data
    	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session>`
    
    

    """

    _prefix = 'iedge4710-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Subscriber, self).__init__()
        self._top_entity = None

        self.yang_name = "subscriber"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"manager" : ("manager", Subscriber.Manager), "session" : ("session", Subscriber.Session)}
        self._child_list_classes = {}

        self.manager = Subscriber.Manager()
        self.manager.parent = self
        self._children_name_map["manager"] = "manager"
        self._children_yang_names.add("manager")

        self.session = Subscriber.Session()
        self.session.parent = self
        self._children_name_map["session"] = "session"
        self._children_yang_names.add("session")
        self._segment_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber"


    class Manager(Entity):
        """
        Subscriber manager operational data
        
        .. attribute:: nodes
        
        	Subscriber manager list of nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes>`
        
        

        """

        _prefix = 'iedge4710-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Subscriber.Manager, self).__init__()

            self.yang_name = "manager"
            self.yang_parent_name = "subscriber"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"nodes" : ("nodes", Subscriber.Manager.Nodes)}
            self._child_list_classes = {}

            self.nodes = Subscriber.Manager.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")
            self._segment_path = lambda: "manager"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber/%s" % self._segment_path()


        class Nodes(Entity):
            """
            Subscriber manager list of nodes
            
            .. attribute:: node
            
            	Subscriber manager operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node>`
            
            

            """

            _prefix = 'iedge4710-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Subscriber.Manager.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "manager"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"node" : ("node", Subscriber.Manager.Nodes.Node)}

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber/manager/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Subscriber.Manager.Nodes, [], name, value)


            class Node(Entity):
                """
                Subscriber manager operational data for a
                particular node
                
                .. attribute:: node_name  <key>
                
                	Node name
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: statistics
                
                	Subscriber manager statistics
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics>`
                
                

                """

                _prefix = 'iedge4710-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Subscriber.Manager.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"statistics" : ("statistics", Subscriber.Manager.Nodes.Node.Statistics)}
                    self._child_list_classes = {}

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.statistics = Subscriber.Manager.Nodes.Node.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")
                    self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber/manager/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Subscriber.Manager.Nodes.Node, ['node_name'], name, value)


                class Statistics(Entity):
                    """
                    Subscriber manager statistics
                    
                    .. attribute:: aaa
                    
                    	AAA statistics
                    	**type**\:  :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa>`
                    
                    .. attribute:: aggregate_summary
                    
                    	Aggregate summary of statistics
                    	**type**\:  :py:class:`AggregateSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary>`
                    
                    .. attribute:: srg
                    
                    	Geo Redundancy statistics
                    	**type**\:  :py:class:`Srg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Srg>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Manager.Nodes.Node.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"aaa" : ("aaa", Subscriber.Manager.Nodes.Node.Statistics.Aaa), "aggregate-summary" : ("aggregate_summary", Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary), "srg" : ("srg", Subscriber.Manager.Nodes.Node.Statistics.Srg)}
                        self._child_list_classes = {}

                        self.aaa = Subscriber.Manager.Nodes.Node.Statistics.Aaa()
                        self.aaa.parent = self
                        self._children_name_map["aaa"] = "aaa"
                        self._children_yang_names.add("aaa")

                        self.aggregate_summary = Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary()
                        self.aggregate_summary.parent = self
                        self._children_name_map["aggregate_summary"] = "aggregate-summary"
                        self._children_yang_names.add("aggregate-summary")

                        self.srg = Subscriber.Manager.Nodes.Node.Statistics.Srg()
                        self.srg.parent = self
                        self._children_name_map["srg"] = "srg"
                        self._children_yang_names.add("srg")
                        self._segment_path = lambda: "statistics"


                    class Aaa(Entity):
                        """
                        AAA statistics
                        
                        .. attribute:: aggregate_accounting
                        
                        	Aggregate accounting statistics
                        	**type**\:  :py:class:`AggregateAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting>`
                        
                        .. attribute:: authentication
                        
                        	Authentication statistics
                        	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication>`
                        
                        .. attribute:: aggregate_mobility
                        
                        	Aggregate mobility statistics
                        	**type**\:  :py:class:`AggregateMobility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility>`
                        
                        .. attribute:: aggregate_authentication
                        
                        	Aggregate authentication statistics
                        	**type**\:  :py:class:`AggregateAuthentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication>`
                        
                        .. attribute:: accounting_stats_all
                        
                        	Display all subscriber management statistics
                        	**type**\:  :py:class:`AccountingStatsAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll>`
                        
                        .. attribute:: change_of_authorization
                        
                        	Change of authorization (COA) statistics
                        	**type**\:  :py:class:`ChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization>`
                        
                        .. attribute:: authorization
                        
                        	Authorization statistics
                        	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization>`
                        
                        .. attribute:: aggregate_authorization
                        
                        	Aggregate authorization statistics
                        	**type**\:  :py:class:`AggregateAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization>`
                        
                        .. attribute:: aggregate_accounting_stats_all
                        
                        	Display all subscriber management total statistics
                        	**type**\:  :py:class:`AggregateAccountingStatsAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll>`
                        
                        .. attribute:: accounting
                        
                        	Accounting statistics
                        	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting>`
                        
                        .. attribute:: mobility
                        
                        	Mobility statistics
                        	**type**\:  :py:class:`Mobility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility>`
                        
                        .. attribute:: aggregate_change_of_authorization
                        
                        	Aggregate change of authorization (COA) statistics
                        	**type**\:  :py:class:`AggregateChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Manager.Nodes.Node.Statistics.Aaa, self).__init__()

                            self.yang_name = "aaa"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"aggregate-accounting" : ("aggregate_accounting", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting), "authentication" : ("authentication", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication), "aggregate-mobility" : ("aggregate_mobility", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility), "aggregate-authentication" : ("aggregate_authentication", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication), "accounting-stats-all" : ("accounting_stats_all", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll), "change-of-authorization" : ("change_of_authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization), "authorization" : ("authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization), "aggregate-authorization" : ("aggregate_authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization), "aggregate-accounting-stats-all" : ("aggregate_accounting_stats_all", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll), "accounting" : ("accounting", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting), "mobility" : ("mobility", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility), "aggregate-change-of-authorization" : ("aggregate_change_of_authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization)}
                            self._child_list_classes = {}

                            self.aggregate_accounting = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting()
                            self.aggregate_accounting.parent = self
                            self._children_name_map["aggregate_accounting"] = "aggregate-accounting"
                            self._children_yang_names.add("aggregate-accounting")

                            self.authentication = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"
                            self._children_yang_names.add("authentication")

                            self.aggregate_mobility = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility()
                            self.aggregate_mobility.parent = self
                            self._children_name_map["aggregate_mobility"] = "aggregate-mobility"
                            self._children_yang_names.add("aggregate-mobility")

                            self.aggregate_authentication = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication()
                            self.aggregate_authentication.parent = self
                            self._children_name_map["aggregate_authentication"] = "aggregate-authentication"
                            self._children_yang_names.add("aggregate-authentication")

                            self.accounting_stats_all = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll()
                            self.accounting_stats_all.parent = self
                            self._children_name_map["accounting_stats_all"] = "accounting-stats-all"
                            self._children_yang_names.add("accounting-stats-all")

                            self.change_of_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization()
                            self.change_of_authorization.parent = self
                            self._children_name_map["change_of_authorization"] = "change-of-authorization"
                            self._children_yang_names.add("change-of-authorization")

                            self.authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization()
                            self.authorization.parent = self
                            self._children_name_map["authorization"] = "authorization"
                            self._children_yang_names.add("authorization")

                            self.aggregate_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization()
                            self.aggregate_authorization.parent = self
                            self._children_name_map["aggregate_authorization"] = "aggregate-authorization"
                            self._children_yang_names.add("aggregate-authorization")

                            self.aggregate_accounting_stats_all = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll()
                            self.aggregate_accounting_stats_all.parent = self
                            self._children_name_map["aggregate_accounting_stats_all"] = "aggregate-accounting-stats-all"
                            self._children_yang_names.add("aggregate-accounting-stats-all")

                            self.accounting = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                            self._children_yang_names.add("accounting")

                            self.mobility = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility()
                            self.mobility.parent = self
                            self._children_name_map["mobility"] = "mobility"
                            self._children_yang_names.add("mobility")

                            self.aggregate_change_of_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization()
                            self.aggregate_change_of_authorization.parent = self
                            self._children_name_map["aggregate_change_of_authorization"] = "aggregate-change-of-authorization"
                            self._children_yang_names.add("aggregate-change-of-authorization")
                            self._segment_path = lambda: "aaa"


                        class AggregateAccounting(Entity):
                            """
                            Aggregate accounting statistics
                            
                            .. attribute:: start
                            
                            	Start statistics
                            	**type**\:  :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start>`
                            
                            .. attribute:: stop
                            
                            	Stop statistics
                            	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop>`
                            
                            .. attribute:: interim
                            
                            	Interim statistics
                            	**type**\:  :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim>`
                            
                            .. attribute:: pass_through
                            
                            	Pass\-through statistics
                            	**type**\:  :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough>`
                            
                            .. attribute:: update
                            
                            	Update statistics
                            	**type**\:  :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update>`
                            
                            .. attribute:: interim_inflight
                            
                            	Interim inflight details
                            	**type**\:  :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight>`
                            
                            .. attribute:: active_sessions
                            
                            	Active sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: started_sessions
                            
                            	Started sessions
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stopped_sessions
                            
                            	Stopped sessions
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_errored_requests
                            
                            	Policy plane errored requests
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_unknown_requests
                            
                            	Policy plane unknown requests
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting, self).__init__()

                                self.yang_name = "aggregate-accounting"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop), "interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight)}
                                self._child_list_classes = {}

                                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start()
                                self.start.parent = self
                                self._children_name_map["start"] = "start"
                                self._children_yang_names.add("start")

                                self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop()
                                self.stop.parent = self
                                self._children_name_map["stop"] = "stop"
                                self._children_yang_names.add("stop")

                                self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim()
                                self.interim.parent = self
                                self._children_name_map["interim"] = "interim"
                                self._children_yang_names.add("interim")

                                self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough()
                                self.pass_through.parent = self
                                self._children_name_map["pass_through"] = "pass-through"
                                self._children_yang_names.add("pass-through")

                                self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update()
                                self.update.parent = self
                                self._children_name_map["update"] = "update"
                                self._children_yang_names.add("update")

                                self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight()
                                self.interim_inflight.parent = self
                                self._children_name_map["interim_inflight"] = "interim-inflight"
                                self._children_yang_names.add("interim-inflight")
                                self._segment_path = lambda: "aggregate-accounting"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting, ['active_sessions', 'started_sessions', 'stopped_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests'], name, value)


                            class Start(Entity):
                                """
                                Start statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start, self).__init__()

                                    self.yang_name = "start"
                                    self.yang_parent_name = "aggregate-accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "start"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class Stop(Entity):
                                """
                                Stop statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop, self).__init__()

                                    self.yang_name = "stop"
                                    self.yang_parent_name = "aggregate-accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "stop"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class Interim(Entity):
                                """
                                Interim statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim, self).__init__()

                                    self.yang_name = "interim"
                                    self.yang_parent_name = "aggregate-accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "interim"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class PassThrough(Entity):
                                """
                                Pass\-through statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough, self).__init__()

                                    self.yang_name = "pass-through"
                                    self.yang_parent_name = "aggregate-accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "pass-through"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class Update(Entity):
                                """
                                Update statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update, self).__init__()

                                    self.yang_name = "update"
                                    self.yang_parent_name = "aggregate-accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class InterimInflight(Entity):
                                """
                                Interim inflight details
                                
                                .. attribute:: quota_exhausts
                                
                                	Quota exhausts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: denied_requests
                                
                                	Denied requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: accepted_requests
                                
                                	Accepted requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: total_quota_of_requests
                                
                                	Total quota of requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: remaining_quota_of_requests
                                
                                	Remaining quota of requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_water_mark_quota_of_requests
                                
                                	Low water mark quota of requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight, self).__init__()

                                    self.yang_name = "interim-inflight"
                                    self.yang_parent_name = "aggregate-accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                    self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                    self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                    self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")

                                    self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                    self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")
                                    self._segment_path = lambda: "interim-inflight"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight, ['quota_exhausts', 'denied_requests', 'accepted_requests', 'total_quota_of_requests', 'remaining_quota_of_requests', 'low_water_mark_quota_of_requests'], name, value)


                        class Authentication(Entity):
                            """
                            Authentication statistics
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication, self).__init__()

                                self.yang_name = "authentication"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                self._segment_path = lambda: "authentication"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                        class AggregateMobility(Entity):
                            """
                            Aggregate mobility statistics
                            
                            .. attribute:: send_request_successes
                            
                            	Request send success
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_failures
                            
                            	Request send failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_successes
                            
                            	Response receive success
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_failures
                            
                            	Response receive failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility, self).__init__()

                                self.yang_name = "aggregate-mobility"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")

                                self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")
                                self._segment_path = lambda: "aggregate-mobility"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility, ['send_request_successes', 'send_request_failures', 'receive_response_successes', 'receive_response_failures'], name, value)


                        class AggregateAuthentication(Entity):
                            """
                            Aggregate authentication statistics
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication, self).__init__()

                                self.yang_name = "aggregate-authentication"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                self._segment_path = lambda: "aggregate-authentication"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                        class AccountingStatsAll(Entity):
                            """
                            Display all subscriber management
                            statistics
                            
                            .. attribute:: accounting_statistics
                            
                            	List of stats for accounting
                            	**type**\:  :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics>`
                            
                            .. attribute:: authentication_statistics
                            
                            	List of stats for authentication
                            	**type**\:  :py:class:`AuthenticationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics>`
                            
                            .. attribute:: authorization_statistics
                            
                            	List of stats for authorization
                            	**type**\:  :py:class:`AuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics>`
                            
                            .. attribute:: change_of_authorization_statistics
                            
                            	List of stats for COA
                            	**type**\:  :py:class:`ChangeOfAuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics>`
                            
                            .. attribute:: mobility_statistics
                            
                            	List of stats for Mobility
                            	**type**\:  :py:class:`MobilityStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll, self).__init__()

                                self.yang_name = "accounting-stats-all"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"accounting-statistics" : ("accounting_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics), "authentication-statistics" : ("authentication_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics), "authorization-statistics" : ("authorization_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics), "change-of-authorization-statistics" : ("change_of_authorization_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics), "mobility-statistics" : ("mobility_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics)}
                                self._child_list_classes = {}

                                self.accounting_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics()
                                self.accounting_statistics.parent = self
                                self._children_name_map["accounting_statistics"] = "accounting-statistics"
                                self._children_yang_names.add("accounting-statistics")

                                self.authentication_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics()
                                self.authentication_statistics.parent = self
                                self._children_name_map["authentication_statistics"] = "authentication-statistics"
                                self._children_yang_names.add("authentication-statistics")

                                self.authorization_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics()
                                self.authorization_statistics.parent = self
                                self._children_name_map["authorization_statistics"] = "authorization-statistics"
                                self._children_yang_names.add("authorization-statistics")

                                self.change_of_authorization_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics()
                                self.change_of_authorization_statistics.parent = self
                                self._children_name_map["change_of_authorization_statistics"] = "change-of-authorization-statistics"
                                self._children_yang_names.add("change-of-authorization-statistics")

                                self.mobility_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics()
                                self.mobility_statistics.parent = self
                                self._children_name_map["mobility_statistics"] = "mobility-statistics"
                                self._children_yang_names.add("mobility-statistics")
                                self._segment_path = lambda: "accounting-stats-all"


                            class AccountingStatistics(Entity):
                                """
                                List of stats for accounting
                                
                                .. attribute:: start
                                
                                	Start statistics
                                	**type**\:  :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start>`
                                
                                .. attribute:: stop
                                
                                	Stop statistics
                                	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop>`
                                
                                .. attribute:: interim
                                
                                	Interim statistics
                                	**type**\:  :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim>`
                                
                                .. attribute:: pass_through
                                
                                	Pass\-through statistics
                                	**type**\:  :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough>`
                                
                                .. attribute:: update
                                
                                	Update statistics
                                	**type**\:  :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update>`
                                
                                .. attribute:: interim_inflight
                                
                                	Interim inflight details
                                	**type**\:  :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight>`
                                
                                .. attribute:: active_sessions
                                
                                	Active sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: started_sessions
                                
                                	Started sessions
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: stopped_sessions
                                
                                	Stopped sessions
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: policy_plane_errored_requests
                                
                                	Policy plane errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: policy_plane_unknown_requests
                                
                                	Policy plane unknown requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics, self).__init__()

                                    self.yang_name = "accounting-statistics"
                                    self.yang_parent_name = "accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop), "interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight)}
                                    self._child_list_classes = {}

                                    self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                    self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                    self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                    self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                    self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                    self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start()
                                    self.start.parent = self
                                    self._children_name_map["start"] = "start"
                                    self._children_yang_names.add("start")

                                    self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop()
                                    self.stop.parent = self
                                    self._children_name_map["stop"] = "stop"
                                    self._children_yang_names.add("stop")

                                    self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim()
                                    self.interim.parent = self
                                    self._children_name_map["interim"] = "interim"
                                    self._children_yang_names.add("interim")

                                    self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough()
                                    self.pass_through.parent = self
                                    self._children_name_map["pass_through"] = "pass-through"
                                    self._children_yang_names.add("pass-through")

                                    self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update()
                                    self.update.parent = self
                                    self._children_name_map["update"] = "update"
                                    self._children_yang_names.add("update")

                                    self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight()
                                    self.interim_inflight.parent = self
                                    self._children_name_map["interim_inflight"] = "interim-inflight"
                                    self._children_yang_names.add("interim-inflight")
                                    self._segment_path = lambda: "accounting-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics, ['active_sessions', 'started_sessions', 'stopped_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests'], name, value)


                                class Start(Entity):
                                    """
                                    Start statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start, self).__init__()

                                        self.yang_name = "start"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "start"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class Stop(Entity):
                                    """
                                    Stop statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop, self).__init__()

                                        self.yang_name = "stop"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "stop"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class Interim(Entity):
                                    """
                                    Interim statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim, self).__init__()

                                        self.yang_name = "interim"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "interim"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class PassThrough(Entity):
                                    """
                                    Pass\-through statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough, self).__init__()

                                        self.yang_name = "pass-through"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "pass-through"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class Update(Entity):
                                    """
                                    Update statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update, self).__init__()

                                        self.yang_name = "update"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class InterimInflight(Entity):
                                    """
                                    Interim inflight details
                                    
                                    .. attribute:: quota_exhausts
                                    
                                    	Quota exhausts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: denied_requests
                                    
                                    	Denied requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: accepted_requests
                                    
                                    	Accepted requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_quota_of_requests
                                    
                                    	Total quota of requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: remaining_quota_of_requests
                                    
                                    	Remaining quota of requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: low_water_mark_quota_of_requests
                                    
                                    	Low water mark quota of requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight, self).__init__()

                                        self.yang_name = "interim-inflight"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                        self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                        self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                        self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")

                                        self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                        self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")
                                        self._segment_path = lambda: "interim-inflight"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight, ['quota_exhausts', 'denied_requests', 'accepted_requests', 'total_quota_of_requests', 'remaining_quota_of_requests', 'low_water_mark_quota_of_requests'], name, value)


                            class AuthenticationStatistics(Entity):
                                """
                                List of stats for authentication
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics, self).__init__()

                                    self.yang_name = "authentication-statistics"
                                    self.yang_parent_name = "accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                    self._segment_path = lambda: "authentication-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                            class AuthorizationStatistics(Entity):
                                """
                                List of stats for authorization
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics, self).__init__()

                                    self.yang_name = "authorization-statistics"
                                    self.yang_parent_name = "accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                    self._segment_path = lambda: "authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                            class ChangeOfAuthorizationStatistics(Entity):
                                """
                                List of stats for COA
                                
                                .. attribute:: account_logon
                                
                                	Account logon request statistics
                                	**type**\:  :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon>`
                                
                                .. attribute:: account_logoff
                                
                                	Account logoff request statistics
                                	**type**\:  :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff>`
                                
                                .. attribute:: account_update
                                
                                	Account update request statistics
                                	**type**\:  :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate>`
                                
                                .. attribute:: session_disconnect
                                
                                	Session disconnect request statistics
                                	**type**\:  :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect>`
                                
                                .. attribute:: single_service_logon
                                
                                	Service logon request statistics
                                	**type**\:  :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon>`
                                
                                .. attribute:: single_service_logoff
                                
                                	Single Service logoff request statistics
                                	**type**\:  :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff>`
                                
                                .. attribute:: single_service_modify
                                
                                	Single Service Modify request statistics
                                	**type**\:  :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify>`
                                
                                .. attribute:: service_multi
                                
                                	MA\-CoA Service request statistics
                                	**type**\:  :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti>`
                                
                                .. attribute:: unknown_account_cmd_resps
                                
                                	Responses to unknown account command
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_service_cmd_resps
                                
                                	Responses to unknown service command
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_cmd_resps
                                
                                	Responses to unknown command
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: attr_list_retrieve_failure_resps
                                
                                	Responses to attribute list failure errors
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: resp_send_failure
                                
                                	Response send failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: internal_err_resps
                                
                                	Responses to internal error
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: service_profile_push_failure_resps
                                
                                	Responses to service profile push failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_cmd_resps
                                
                                	Responses empty (no command) COA request
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_found_resps
                                
                                	Responses to COA with unknown session identifier
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_peer_resps
                                
                                	Responses to session peer not found error
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics, self).__init__()

                                    self.yang_name = "change-of-authorization-statistics"
                                    self.yang_parent_name = "accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon), "account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti)}
                                    self._child_list_classes = {}

                                    self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                    self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                    self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                    self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                    self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                    self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                    self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                    self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                    self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                    self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                    self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon()
                                    self.account_logon.parent = self
                                    self._children_name_map["account_logon"] = "account-logon"
                                    self._children_yang_names.add("account-logon")

                                    self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff()
                                    self.account_logoff.parent = self
                                    self._children_name_map["account_logoff"] = "account-logoff"
                                    self._children_yang_names.add("account-logoff")

                                    self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate()
                                    self.account_update.parent = self
                                    self._children_name_map["account_update"] = "account-update"
                                    self._children_yang_names.add("account-update")

                                    self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect()
                                    self.session_disconnect.parent = self
                                    self._children_name_map["session_disconnect"] = "session-disconnect"
                                    self._children_yang_names.add("session-disconnect")

                                    self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon()
                                    self.single_service_logon.parent = self
                                    self._children_name_map["single_service_logon"] = "single-service-logon"
                                    self._children_yang_names.add("single-service-logon")

                                    self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff()
                                    self.single_service_logoff.parent = self
                                    self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                    self._children_yang_names.add("single-service-logoff")

                                    self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify()
                                    self.single_service_modify.parent = self
                                    self._children_name_map["single_service_modify"] = "single-service-modify"
                                    self._children_yang_names.add("single-service-modify")

                                    self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti()
                                    self.service_multi.parent = self
                                    self._children_name_map["service_multi"] = "service-multi"
                                    self._children_yang_names.add("service-multi")
                                    self._segment_path = lambda: "change-of-authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics, ['unknown_account_cmd_resps', 'unknown_service_cmd_resps', 'unknown_cmd_resps', 'attr_list_retrieve_failure_resps', 'resp_send_failure', 'internal_err_resps', 'service_profile_push_failure_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps'], name, value)


                                class AccountLogon(Entity):
                                    """
                                    Account logon request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon, self).__init__()

                                        self.yang_name = "account-logon"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "account-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class AccountLogoff(Entity):
                                    """
                                    Account logoff request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff, self).__init__()

                                        self.yang_name = "account-logoff"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "account-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class AccountUpdate(Entity):
                                    """
                                    Account update request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate, self).__init__()

                                        self.yang_name = "account-update"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "account-update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SessionDisconnect(Entity):
                                    """
                                    Session disconnect request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect, self).__init__()

                                        self.yang_name = "session-disconnect"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "session-disconnect"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SingleServiceLogon(Entity):
                                    """
                                    Service logon request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon, self).__init__()

                                        self.yang_name = "single-service-logon"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "single-service-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SingleServiceLogoff(Entity):
                                    """
                                    Single Service logoff request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff, self).__init__()

                                        self.yang_name = "single-service-logoff"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "single-service-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SingleServiceModify(Entity):
                                    """
                                    Single Service Modify request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify, self).__init__()

                                        self.yang_name = "single-service-modify"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "single-service-modify"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class ServiceMulti(Entity):
                                    """
                                    MA\-CoA Service request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti, self).__init__()

                                        self.yang_name = "service-multi"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "service-multi"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class MobilityStatistics(Entity):
                                """
                                List of stats for Mobility
                                
                                .. attribute:: send_request_successes
                                
                                	Request send success
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: send_request_failures
                                
                                	Request send failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: receive_response_successes
                                
                                	Response receive success
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: receive_response_failures
                                
                                	Response receive failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics, self).__init__()

                                    self.yang_name = "mobility-statistics"
                                    self.yang_parent_name = "accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")

                                    self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                    self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                    self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")
                                    self._segment_path = lambda: "mobility-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics, ['send_request_successes', 'send_request_failures', 'receive_response_successes', 'receive_response_failures'], name, value)


                        class ChangeOfAuthorization(Entity):
                            """
                            Change of authorization (COA) statistics
                            
                            .. attribute:: account_logon
                            
                            	Account logon request statistics
                            	**type**\:  :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon>`
                            
                            .. attribute:: account_logoff
                            
                            	Account logoff request statistics
                            	**type**\:  :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff>`
                            
                            .. attribute:: account_update
                            
                            	Account update request statistics
                            	**type**\:  :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate>`
                            
                            .. attribute:: session_disconnect
                            
                            	Session disconnect request statistics
                            	**type**\:  :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect>`
                            
                            .. attribute:: single_service_logon
                            
                            	Service logon request statistics
                            	**type**\:  :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon>`
                            
                            .. attribute:: single_service_logoff
                            
                            	Single Service logoff request statistics
                            	**type**\:  :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff>`
                            
                            .. attribute:: single_service_modify
                            
                            	Single Service Modify request statistics
                            	**type**\:  :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify>`
                            
                            .. attribute:: service_multi
                            
                            	MA\-CoA Service request statistics
                            	**type**\:  :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti>`
                            
                            .. attribute:: unknown_account_cmd_resps
                            
                            	Responses to unknown account command
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_service_cmd_resps
                            
                            	Responses to unknown service command
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_cmd_resps
                            
                            	Responses to unknown command
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: attr_list_retrieve_failure_resps
                            
                            	Responses to attribute list failure errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: resp_send_failure
                            
                            	Response send failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: internal_err_resps
                            
                            	Responses to internal error
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_profile_push_failure_resps
                            
                            	Responses to service profile push failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_cmd_resps
                            
                            	Responses empty (no command) COA request
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_found_resps
                            
                            	Responses to COA with unknown session identifier
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_peer_resps
                            
                            	Responses to session peer not found error
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization, self).__init__()

                                self.yang_name = "change-of-authorization"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon), "account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti)}
                                self._child_list_classes = {}

                                self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon()
                                self.account_logon.parent = self
                                self._children_name_map["account_logon"] = "account-logon"
                                self._children_yang_names.add("account-logon")

                                self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff()
                                self.account_logoff.parent = self
                                self._children_name_map["account_logoff"] = "account-logoff"
                                self._children_yang_names.add("account-logoff")

                                self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate()
                                self.account_update.parent = self
                                self._children_name_map["account_update"] = "account-update"
                                self._children_yang_names.add("account-update")

                                self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect()
                                self.session_disconnect.parent = self
                                self._children_name_map["session_disconnect"] = "session-disconnect"
                                self._children_yang_names.add("session-disconnect")

                                self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon()
                                self.single_service_logon.parent = self
                                self._children_name_map["single_service_logon"] = "single-service-logon"
                                self._children_yang_names.add("single-service-logon")

                                self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff()
                                self.single_service_logoff.parent = self
                                self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                self._children_yang_names.add("single-service-logoff")

                                self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify()
                                self.single_service_modify.parent = self
                                self._children_name_map["single_service_modify"] = "single-service-modify"
                                self._children_yang_names.add("single-service-modify")

                                self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti()
                                self.service_multi.parent = self
                                self._children_name_map["service_multi"] = "service-multi"
                                self._children_yang_names.add("service-multi")
                                self._segment_path = lambda: "change-of-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization, ['unknown_account_cmd_resps', 'unknown_service_cmd_resps', 'unknown_cmd_resps', 'attr_list_retrieve_failure_resps', 'resp_send_failure', 'internal_err_resps', 'service_profile_push_failure_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps'], name, value)


                            class AccountLogon(Entity):
                                """
                                Account logon request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon, self).__init__()

                                    self.yang_name = "account-logon"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "account-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class AccountLogoff(Entity):
                                """
                                Account logoff request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff, self).__init__()

                                    self.yang_name = "account-logoff"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "account-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class AccountUpdate(Entity):
                                """
                                Account update request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate, self).__init__()

                                    self.yang_name = "account-update"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "account-update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SessionDisconnect(Entity):
                                """
                                Session disconnect request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect, self).__init__()

                                    self.yang_name = "session-disconnect"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "session-disconnect"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SingleServiceLogon(Entity):
                                """
                                Service logon request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon, self).__init__()

                                    self.yang_name = "single-service-logon"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "single-service-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SingleServiceLogoff(Entity):
                                """
                                Single Service logoff request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff, self).__init__()

                                    self.yang_name = "single-service-logoff"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "single-service-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SingleServiceModify(Entity):
                                """
                                Single Service Modify request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify, self).__init__()

                                    self.yang_name = "single-service-modify"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "single-service-modify"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class ServiceMulti(Entity):
                                """
                                MA\-CoA Service request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti, self).__init__()

                                    self.yang_name = "service-multi"
                                    self.yang_parent_name = "change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "service-multi"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                        class Authorization(Entity):
                            """
                            Authorization statistics
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization, self).__init__()

                                self.yang_name = "authorization"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                self._segment_path = lambda: "authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                        class AggregateAuthorization(Entity):
                            """
                            Aggregate authorization statistics
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization, self).__init__()

                                self.yang_name = "aggregate-authorization"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                self._segment_path = lambda: "aggregate-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                        class AggregateAccountingStatsAll(Entity):
                            """
                            Display all subscriber management total
                            statistics
                            
                            .. attribute:: accounting_statistics
                            
                            	List of stats for accounting
                            	**type**\:  :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics>`
                            
                            .. attribute:: authentication_statistics
                            
                            	List of stats for authentication
                            	**type**\:  :py:class:`AuthenticationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics>`
                            
                            .. attribute:: authorization_statistics
                            
                            	List of stats for authorization
                            	**type**\:  :py:class:`AuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics>`
                            
                            .. attribute:: change_of_authorization_statistics
                            
                            	List of stats for COA
                            	**type**\:  :py:class:`ChangeOfAuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics>`
                            
                            .. attribute:: mobility_statistics
                            
                            	List of stats for Mobility
                            	**type**\:  :py:class:`MobilityStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll, self).__init__()

                                self.yang_name = "aggregate-accounting-stats-all"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"accounting-statistics" : ("accounting_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics), "authentication-statistics" : ("authentication_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics), "authorization-statistics" : ("authorization_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics), "change-of-authorization-statistics" : ("change_of_authorization_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics), "mobility-statistics" : ("mobility_statistics", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics)}
                                self._child_list_classes = {}

                                self.accounting_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics()
                                self.accounting_statistics.parent = self
                                self._children_name_map["accounting_statistics"] = "accounting-statistics"
                                self._children_yang_names.add("accounting-statistics")

                                self.authentication_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics()
                                self.authentication_statistics.parent = self
                                self._children_name_map["authentication_statistics"] = "authentication-statistics"
                                self._children_yang_names.add("authentication-statistics")

                                self.authorization_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics()
                                self.authorization_statistics.parent = self
                                self._children_name_map["authorization_statistics"] = "authorization-statistics"
                                self._children_yang_names.add("authorization-statistics")

                                self.change_of_authorization_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics()
                                self.change_of_authorization_statistics.parent = self
                                self._children_name_map["change_of_authorization_statistics"] = "change-of-authorization-statistics"
                                self._children_yang_names.add("change-of-authorization-statistics")

                                self.mobility_statistics = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics()
                                self.mobility_statistics.parent = self
                                self._children_name_map["mobility_statistics"] = "mobility-statistics"
                                self._children_yang_names.add("mobility-statistics")
                                self._segment_path = lambda: "aggregate-accounting-stats-all"


                            class AccountingStatistics(Entity):
                                """
                                List of stats for accounting
                                
                                .. attribute:: start
                                
                                	Start statistics
                                	**type**\:  :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start>`
                                
                                .. attribute:: stop
                                
                                	Stop statistics
                                	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop>`
                                
                                .. attribute:: interim
                                
                                	Interim statistics
                                	**type**\:  :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim>`
                                
                                .. attribute:: pass_through
                                
                                	Pass\-through statistics
                                	**type**\:  :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough>`
                                
                                .. attribute:: update
                                
                                	Update statistics
                                	**type**\:  :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update>`
                                
                                .. attribute:: interim_inflight
                                
                                	Interim inflight details
                                	**type**\:  :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight>`
                                
                                .. attribute:: active_sessions
                                
                                	Active sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: started_sessions
                                
                                	Started sessions
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: stopped_sessions
                                
                                	Stopped sessions
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: policy_plane_errored_requests
                                
                                	Policy plane errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: policy_plane_unknown_requests
                                
                                	Policy plane unknown requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics, self).__init__()

                                    self.yang_name = "accounting-statistics"
                                    self.yang_parent_name = "aggregate-accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop), "interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight)}
                                    self._child_list_classes = {}

                                    self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                    self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                    self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                    self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                    self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                    self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start()
                                    self.start.parent = self
                                    self._children_name_map["start"] = "start"
                                    self._children_yang_names.add("start")

                                    self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop()
                                    self.stop.parent = self
                                    self._children_name_map["stop"] = "stop"
                                    self._children_yang_names.add("stop")

                                    self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim()
                                    self.interim.parent = self
                                    self._children_name_map["interim"] = "interim"
                                    self._children_yang_names.add("interim")

                                    self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough()
                                    self.pass_through.parent = self
                                    self._children_name_map["pass_through"] = "pass-through"
                                    self._children_yang_names.add("pass-through")

                                    self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update()
                                    self.update.parent = self
                                    self._children_name_map["update"] = "update"
                                    self._children_yang_names.add("update")

                                    self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight()
                                    self.interim_inflight.parent = self
                                    self._children_name_map["interim_inflight"] = "interim-inflight"
                                    self._children_yang_names.add("interim-inflight")
                                    self._segment_path = lambda: "accounting-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics, ['active_sessions', 'started_sessions', 'stopped_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests'], name, value)


                                class Start(Entity):
                                    """
                                    Start statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start, self).__init__()

                                        self.yang_name = "start"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "start"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class Stop(Entity):
                                    """
                                    Stop statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop, self).__init__()

                                        self.yang_name = "stop"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "stop"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class Interim(Entity):
                                    """
                                    Interim statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim, self).__init__()

                                        self.yang_name = "interim"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "interim"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class PassThrough(Entity):
                                    """
                                    Pass\-through statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough, self).__init__()

                                        self.yang_name = "pass-through"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "pass-through"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class Update(Entity):
                                    """
                                    Update statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update, self).__init__()

                                        self.yang_name = "update"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                        self._segment_path = lambda: "update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                                class InterimInflight(Entity):
                                    """
                                    Interim inflight details
                                    
                                    .. attribute:: quota_exhausts
                                    
                                    	Quota exhausts
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: denied_requests
                                    
                                    	Denied requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: accepted_requests
                                    
                                    	Accepted requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_quota_of_requests
                                    
                                    	Total quota of requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: remaining_quota_of_requests
                                    
                                    	Remaining quota of requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: low_water_mark_quota_of_requests
                                    
                                    	Low water mark quota of requests
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight, self).__init__()

                                        self.yang_name = "interim-inflight"
                                        self.yang_parent_name = "accounting-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                        self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                        self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                        self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")

                                        self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                        self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")
                                        self._segment_path = lambda: "interim-inflight"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight, ['quota_exhausts', 'denied_requests', 'accepted_requests', 'total_quota_of_requests', 'remaining_quota_of_requests', 'low_water_mark_quota_of_requests'], name, value)


                            class AuthenticationStatistics(Entity):
                                """
                                List of stats for authentication
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics, self).__init__()

                                    self.yang_name = "authentication-statistics"
                                    self.yang_parent_name = "aggregate-accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                    self._segment_path = lambda: "authentication-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                            class AuthorizationStatistics(Entity):
                                """
                                List of stats for authorization
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics, self).__init__()

                                    self.yang_name = "authorization-statistics"
                                    self.yang_parent_name = "aggregate-accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")
                                    self._segment_path = lambda: "authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics, ['sent_requests', 'accepted_requests', 'successful_requests', 'rejected_requests', 'unreachable_requests', 'errored_requests', 'incomplete_requests', 'terminated_requests'], name, value)


                            class ChangeOfAuthorizationStatistics(Entity):
                                """
                                List of stats for COA
                                
                                .. attribute:: account_logon
                                
                                	Account logon request statistics
                                	**type**\:  :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon>`
                                
                                .. attribute:: account_logoff
                                
                                	Account logoff request statistics
                                	**type**\:  :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff>`
                                
                                .. attribute:: account_update
                                
                                	Account update request statistics
                                	**type**\:  :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate>`
                                
                                .. attribute:: session_disconnect
                                
                                	Session disconnect request statistics
                                	**type**\:  :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect>`
                                
                                .. attribute:: single_service_logon
                                
                                	Service logon request statistics
                                	**type**\:  :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon>`
                                
                                .. attribute:: single_service_logoff
                                
                                	Single Service logoff request statistics
                                	**type**\:  :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff>`
                                
                                .. attribute:: single_service_modify
                                
                                	Single Service Modify request statistics
                                	**type**\:  :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify>`
                                
                                .. attribute:: service_multi
                                
                                	MA\-CoA Service request statistics
                                	**type**\:  :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti>`
                                
                                .. attribute:: unknown_account_cmd_resps
                                
                                	Responses to unknown account command
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_service_cmd_resps
                                
                                	Responses to unknown service command
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_cmd_resps
                                
                                	Responses to unknown command
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: attr_list_retrieve_failure_resps
                                
                                	Responses to attribute list failure errors
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: resp_send_failure
                                
                                	Response send failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: internal_err_resps
                                
                                	Responses to internal error
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: service_profile_push_failure_resps
                                
                                	Responses to service profile push failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_cmd_resps
                                
                                	Responses empty (no command) COA request
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_found_resps
                                
                                	Responses to COA with unknown session identifier
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_peer_resps
                                
                                	Responses to session peer not found error
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics, self).__init__()

                                    self.yang_name = "change-of-authorization-statistics"
                                    self.yang_parent_name = "aggregate-accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon), "account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti)}
                                    self._child_list_classes = {}

                                    self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                    self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                    self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                    self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                    self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                    self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                    self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                    self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                    self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                    self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                    self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon()
                                    self.account_logon.parent = self
                                    self._children_name_map["account_logon"] = "account-logon"
                                    self._children_yang_names.add("account-logon")

                                    self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff()
                                    self.account_logoff.parent = self
                                    self._children_name_map["account_logoff"] = "account-logoff"
                                    self._children_yang_names.add("account-logoff")

                                    self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate()
                                    self.account_update.parent = self
                                    self._children_name_map["account_update"] = "account-update"
                                    self._children_yang_names.add("account-update")

                                    self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect()
                                    self.session_disconnect.parent = self
                                    self._children_name_map["session_disconnect"] = "session-disconnect"
                                    self._children_yang_names.add("session-disconnect")

                                    self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon()
                                    self.single_service_logon.parent = self
                                    self._children_name_map["single_service_logon"] = "single-service-logon"
                                    self._children_yang_names.add("single-service-logon")

                                    self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff()
                                    self.single_service_logoff.parent = self
                                    self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                    self._children_yang_names.add("single-service-logoff")

                                    self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify()
                                    self.single_service_modify.parent = self
                                    self._children_name_map["single_service_modify"] = "single-service-modify"
                                    self._children_yang_names.add("single-service-modify")

                                    self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti()
                                    self.service_multi.parent = self
                                    self._children_name_map["service_multi"] = "service-multi"
                                    self._children_yang_names.add("service-multi")
                                    self._segment_path = lambda: "change-of-authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics, ['unknown_account_cmd_resps', 'unknown_service_cmd_resps', 'unknown_cmd_resps', 'attr_list_retrieve_failure_resps', 'resp_send_failure', 'internal_err_resps', 'service_profile_push_failure_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps'], name, value)


                                class AccountLogon(Entity):
                                    """
                                    Account logon request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon, self).__init__()

                                        self.yang_name = "account-logon"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "account-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class AccountLogoff(Entity):
                                    """
                                    Account logoff request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff, self).__init__()

                                        self.yang_name = "account-logoff"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "account-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class AccountUpdate(Entity):
                                    """
                                    Account update request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate, self).__init__()

                                        self.yang_name = "account-update"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "account-update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SessionDisconnect(Entity):
                                    """
                                    Session disconnect request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect, self).__init__()

                                        self.yang_name = "session-disconnect"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "session-disconnect"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SingleServiceLogon(Entity):
                                    """
                                    Service logon request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon, self).__init__()

                                        self.yang_name = "single-service-logon"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "single-service-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SingleServiceLogoff(Entity):
                                    """
                                    Single Service logoff request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff, self).__init__()

                                        self.yang_name = "single-service-logoff"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "single-service-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class SingleServiceModify(Entity):
                                    """
                                    Single Service Modify request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify, self).__init__()

                                        self.yang_name = "single-service-modify"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "single-service-modify"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                                class ServiceMulti(Entity):
                                    """
                                    MA\-CoA Service request statistics
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'iedge4710-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti, self).__init__()

                                        self.yang_name = "service-multi"
                                        self.yang_parent_name = "change-of-authorization-statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                        self._segment_path = lambda: "service-multi"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class MobilityStatistics(Entity):
                                """
                                List of stats for Mobility
                                
                                .. attribute:: send_request_successes
                                
                                	Request send success
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: send_request_failures
                                
                                	Request send failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: receive_response_successes
                                
                                	Response receive success
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: receive_response_failures
                                
                                	Response receive failures
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics, self).__init__()

                                    self.yang_name = "mobility-statistics"
                                    self.yang_parent_name = "aggregate-accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")

                                    self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                    self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                    self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")
                                    self._segment_path = lambda: "mobility-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics, ['send_request_successes', 'send_request_failures', 'receive_response_successes', 'receive_response_failures'], name, value)


                        class Accounting(Entity):
                            """
                            Accounting statistics
                            
                            .. attribute:: start
                            
                            	Start statistics
                            	**type**\:  :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start>`
                            
                            .. attribute:: stop
                            
                            	Stop statistics
                            	**type**\:  :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop>`
                            
                            .. attribute:: interim
                            
                            	Interim statistics
                            	**type**\:  :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim>`
                            
                            .. attribute:: pass_through
                            
                            	Pass\-through statistics
                            	**type**\:  :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough>`
                            
                            .. attribute:: update
                            
                            	Update statistics
                            	**type**\:  :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update>`
                            
                            .. attribute:: interim_inflight
                            
                            	Interim inflight details
                            	**type**\:  :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight>`
                            
                            .. attribute:: active_sessions
                            
                            	Active sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: started_sessions
                            
                            	Started sessions
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stopped_sessions
                            
                            	Stopped sessions
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_errored_requests
                            
                            	Policy plane errored requests
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_unknown_requests
                            
                            	Policy plane unknown requests
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting, self).__init__()

                                self.yang_name = "accounting"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop), "interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight)}
                                self._child_list_classes = {}

                                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start()
                                self.start.parent = self
                                self._children_name_map["start"] = "start"
                                self._children_yang_names.add("start")

                                self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop()
                                self.stop.parent = self
                                self._children_name_map["stop"] = "stop"
                                self._children_yang_names.add("stop")

                                self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim()
                                self.interim.parent = self
                                self._children_name_map["interim"] = "interim"
                                self._children_yang_names.add("interim")

                                self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough()
                                self.pass_through.parent = self
                                self._children_name_map["pass_through"] = "pass-through"
                                self._children_yang_names.add("pass-through")

                                self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update()
                                self.update.parent = self
                                self._children_name_map["update"] = "update"
                                self._children_yang_names.add("update")

                                self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight()
                                self.interim_inflight.parent = self
                                self._children_name_map["interim_inflight"] = "interim-inflight"
                                self._children_yang_names.add("interim-inflight")
                                self._segment_path = lambda: "accounting"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting, ['active_sessions', 'started_sessions', 'stopped_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests'], name, value)


                            class Start(Entity):
                                """
                                Start statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start, self).__init__()

                                    self.yang_name = "start"
                                    self.yang_parent_name = "accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "start"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class Stop(Entity):
                                """
                                Stop statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop, self).__init__()

                                    self.yang_name = "stop"
                                    self.yang_parent_name = "accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "stop"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class Interim(Entity):
                                """
                                Interim statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim, self).__init__()

                                    self.yang_name = "interim"
                                    self.yang_parent_name = "accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "interim"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class PassThrough(Entity):
                                """
                                Pass\-through statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough, self).__init__()

                                    self.yang_name = "pass-through"
                                    self.yang_parent_name = "accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "pass-through"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class Update(Entity):
                                """
                                Update statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update, self).__init__()

                                    self.yang_name = "update"
                                    self.yang_parent_name = "accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")
                                    self._segment_path = lambda: "update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update, ['received_requests', 'errored_requests', 'aaa_errored_requests', 'aaa_sent_requests', 'aaa_succeeded_responses', 'aaa_failed_responses'], name, value)


                            class InterimInflight(Entity):
                                """
                                Interim inflight details
                                
                                .. attribute:: quota_exhausts
                                
                                	Quota exhausts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: denied_requests
                                
                                	Denied requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: accepted_requests
                                
                                	Accepted requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: total_quota_of_requests
                                
                                	Total quota of requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: remaining_quota_of_requests
                                
                                	Remaining quota of requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_water_mark_quota_of_requests
                                
                                	Low water mark quota of requests
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight, self).__init__()

                                    self.yang_name = "interim-inflight"
                                    self.yang_parent_name = "accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                    self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                    self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                    self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")

                                    self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                    self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")
                                    self._segment_path = lambda: "interim-inflight"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight, ['quota_exhausts', 'denied_requests', 'accepted_requests', 'total_quota_of_requests', 'remaining_quota_of_requests', 'low_water_mark_quota_of_requests'], name, value)


                        class Mobility(Entity):
                            """
                            Mobility statistics
                            
                            .. attribute:: send_request_successes
                            
                            	Request send success
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_failures
                            
                            	Request send failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_successes
                            
                            	Response receive success
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_failures
                            
                            	Response receive failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility, self).__init__()

                                self.yang_name = "mobility"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")

                                self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")
                                self._segment_path = lambda: "mobility"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility, ['send_request_successes', 'send_request_failures', 'receive_response_successes', 'receive_response_failures'], name, value)


                        class AggregateChangeOfAuthorization(Entity):
                            """
                            Aggregate change of authorization (COA)
                            statistics
                            
                            .. attribute:: account_logon
                            
                            	Account logon request statistics
                            	**type**\:  :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon>`
                            
                            .. attribute:: account_logoff
                            
                            	Account logoff request statistics
                            	**type**\:  :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff>`
                            
                            .. attribute:: account_update
                            
                            	Account update request statistics
                            	**type**\:  :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate>`
                            
                            .. attribute:: session_disconnect
                            
                            	Session disconnect request statistics
                            	**type**\:  :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect>`
                            
                            .. attribute:: single_service_logon
                            
                            	Service logon request statistics
                            	**type**\:  :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon>`
                            
                            .. attribute:: single_service_logoff
                            
                            	Single Service logoff request statistics
                            	**type**\:  :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff>`
                            
                            .. attribute:: single_service_modify
                            
                            	Single Service Modify request statistics
                            	**type**\:  :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify>`
                            
                            .. attribute:: service_multi
                            
                            	MA\-CoA Service request statistics
                            	**type**\:  :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti>`
                            
                            .. attribute:: unknown_account_cmd_resps
                            
                            	Responses to unknown account command
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_service_cmd_resps
                            
                            	Responses to unknown service command
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_cmd_resps
                            
                            	Responses to unknown command
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: attr_list_retrieve_failure_resps
                            
                            	Responses to attribute list failure errors
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: resp_send_failure
                            
                            	Response send failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: internal_err_resps
                            
                            	Responses to internal error
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_profile_push_failure_resps
                            
                            	Responses to service profile push failures
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_cmd_resps
                            
                            	Responses empty (no command) COA request
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_found_resps
                            
                            	Responses to COA with unknown session identifier
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_peer_resps
                            
                            	Responses to session peer not found error
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization, self).__init__()

                                self.yang_name = "aggregate-change-of-authorization"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon), "account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti)}
                                self._child_list_classes = {}

                                self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon()
                                self.account_logon.parent = self
                                self._children_name_map["account_logon"] = "account-logon"
                                self._children_yang_names.add("account-logon")

                                self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff()
                                self.account_logoff.parent = self
                                self._children_name_map["account_logoff"] = "account-logoff"
                                self._children_yang_names.add("account-logoff")

                                self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate()
                                self.account_update.parent = self
                                self._children_name_map["account_update"] = "account-update"
                                self._children_yang_names.add("account-update")

                                self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect()
                                self.session_disconnect.parent = self
                                self._children_name_map["session_disconnect"] = "session-disconnect"
                                self._children_yang_names.add("session-disconnect")

                                self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon()
                                self.single_service_logon.parent = self
                                self._children_name_map["single_service_logon"] = "single-service-logon"
                                self._children_yang_names.add("single-service-logon")

                                self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff()
                                self.single_service_logoff.parent = self
                                self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                self._children_yang_names.add("single-service-logoff")

                                self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify()
                                self.single_service_modify.parent = self
                                self._children_name_map["single_service_modify"] = "single-service-modify"
                                self._children_yang_names.add("single-service-modify")

                                self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti()
                                self.service_multi.parent = self
                                self._children_name_map["service_multi"] = "service-multi"
                                self._children_yang_names.add("service-multi")
                                self._segment_path = lambda: "aggregate-change-of-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization, ['unknown_account_cmd_resps', 'unknown_service_cmd_resps', 'unknown_cmd_resps', 'attr_list_retrieve_failure_resps', 'resp_send_failure', 'internal_err_resps', 'service_profile_push_failure_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps'], name, value)


                            class AccountLogon(Entity):
                                """
                                Account logon request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon, self).__init__()

                                    self.yang_name = "account-logon"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "account-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class AccountLogoff(Entity):
                                """
                                Account logoff request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff, self).__init__()

                                    self.yang_name = "account-logoff"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "account-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class AccountUpdate(Entity):
                                """
                                Account update request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate, self).__init__()

                                    self.yang_name = "account-update"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "account-update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SessionDisconnect(Entity):
                                """
                                Session disconnect request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect, self).__init__()

                                    self.yang_name = "session-disconnect"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "session-disconnect"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SingleServiceLogon(Entity):
                                """
                                Service logon request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon, self).__init__()

                                    self.yang_name = "single-service-logon"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "single-service-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SingleServiceLogoff(Entity):
                                """
                                Single Service logoff request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff, self).__init__()

                                    self.yang_name = "single-service-logoff"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "single-service-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class SingleServiceModify(Entity):
                                """
                                Single Service Modify request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify, self).__init__()

                                    self.yang_name = "single-service-modify"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "single-service-modify"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                            class ServiceMulti(Entity):
                                """
                                MA\-CoA Service request statistics
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti, self).__init__()

                                    self.yang_name = "service-multi"
                                    self.yang_parent_name = "aggregate-change-of-authorization"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")
                                    self._segment_path = lambda: "service-multi"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti, ['received_requests', 'acknowledged_requests', 'non_acknowledged_requests'], name, value)


                    class AggregateSummary(Entity):
                        """
                        Aggregate summary of statistics
                        
                        .. attribute:: no_subscriber_control_policy_on_interface
                        
                        	Subscriber control policy not applied on interface
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: no_class_match_in_start_request
                        
                        	No control policy class match during subscriber start
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: nas_port_attribute_format_warnings
                        
                        	NAS port attribute format warnings
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: nas_port_id_attribute_format_warnings
                        
                        	NAS port ID attribute format warnings
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: destination_station_id_attribute_format_warnings
                        
                        	Destination station ID attribute format warnings
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: calling_station_id_attribute_format_warnings
                        
                        	Calling station ID attribute format warnings
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: username_attribute_format_warnings
                        
                        	Username attribute format warnings
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: install_user_profiles
                        
                        	User profiles installed
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_install_errors
                        
                        	User profile install errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_removals
                        
                        	User profile removals
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_errors
                        
                        	User profile errors
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_quota_exhausts
                        
                        	Session Disconnect Quota Exhausts
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_no_quota
                        
                        	Session Disconnect Request Queued, no quota
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_quota_avail
                        
                        	Session Disconnect Request Accepted, quota available
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_recon_ip
                        
                        	Session Disconnect Requests not Dequeued, reconciliation in progress
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_none_started
                        
                        	Session Disconnect Requests not Dequeued, no quota
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_quota
                        
                        	Session Disconnect Quota
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_quota_remaining
                        
                        	Session Disconnect Quota Remaining
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_q_count
                        
                        	Session Disconnect Requests Queued
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary, self).__init__()

                            self.yang_name = "aggregate-summary"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.no_subscriber_control_policy_on_interface = YLeaf(YType.uint64, "no-subscriber-control-policy-on-interface")

                            self.no_class_match_in_start_request = YLeaf(YType.uint64, "no-class-match-in-start-request")

                            self.nas_port_attribute_format_warnings = YLeaf(YType.uint64, "nas-port-attribute-format-warnings")

                            self.nas_port_id_attribute_format_warnings = YLeaf(YType.uint64, "nas-port-id-attribute-format-warnings")

                            self.destination_station_id_attribute_format_warnings = YLeaf(YType.uint64, "destination-station-id-attribute-format-warnings")

                            self.calling_station_id_attribute_format_warnings = YLeaf(YType.uint64, "calling-station-id-attribute-format-warnings")

                            self.username_attribute_format_warnings = YLeaf(YType.uint64, "username-attribute-format-warnings")

                            self.install_user_profiles = YLeaf(YType.uint64, "install-user-profiles")

                            self.user_profile_install_errors = YLeaf(YType.uint64, "user-profile-install-errors")

                            self.user_profile_removals = YLeaf(YType.uint64, "user-profile-removals")

                            self.user_profile_errors = YLeaf(YType.uint64, "user-profile-errors")

                            self.sess_disc_quota_exhausts = YLeaf(YType.uint64, "sess-disc-quota-exhausts")

                            self.sess_disc_no_quota = YLeaf(YType.uint64, "sess-disc-no-quota")

                            self.sess_disc_quota_avail = YLeaf(YType.uint64, "sess-disc-quota-avail")

                            self.sess_disc_recon_ip = YLeaf(YType.uint64, "sess-disc-recon-ip")

                            self.sess_disc_none_started = YLeaf(YType.uint64, "sess-disc-none-started")

                            self.sess_disc_quota = YLeaf(YType.uint32, "sess-disc-quota")

                            self.sess_disc_quota_remaining = YLeaf(YType.uint32, "sess-disc-quota-remaining")

                            self.sess_disc_q_count = YLeaf(YType.uint32, "sess-disc-q-count")
                            self._segment_path = lambda: "aggregate-summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary, ['no_subscriber_control_policy_on_interface', 'no_class_match_in_start_request', 'nas_port_attribute_format_warnings', 'nas_port_id_attribute_format_warnings', 'destination_station_id_attribute_format_warnings', 'calling_station_id_attribute_format_warnings', 'username_attribute_format_warnings', 'install_user_profiles', 'user_profile_install_errors', 'user_profile_removals', 'user_profile_errors', 'sess_disc_quota_exhausts', 'sess_disc_no_quota', 'sess_disc_quota_avail', 'sess_disc_recon_ip', 'sess_disc_none_started', 'sess_disc_quota', 'sess_disc_quota_remaining', 'sess_disc_q_count'], name, value)


                    class Srg(Entity):
                        """
                        Geo Redundancy statistics
                        
                        .. attribute:: txlist_send_triggered
                        
                        	Txlist Send Triggered
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_failed
                        
                        	Txlist Send Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_failed_notactive
                        
                        	Txlist send failed due to not active
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: actual_txlist_sent
                        
                        	Txlist Send Success
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: alreadyin_txlist
                        
                        	Element already in Txlist
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_encode
                        
                        	Txlist Encode
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_encode_fail
                        
                        	Txlist encode Failed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_update_encode
                        
                        	Txlist Create Update Encode
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delete_encode
                        
                        	Txlist Delete Encode
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_upd_clean_callback
                        
                        	Txlist Create/update clean callback
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delete_clean_callback
                        
                        	Txlist Delete clean callback
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_recv_entry
                        
                        	Slave Recieved Sync
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_decode_fail
                        
                        	Decode failed on Slave
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_create_update
                        
                        	Create Update received on slave
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_delete
                        
                        	Delete received on slave
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_context_malloc
                        
                        	SRG context allocated
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_context_free
                        
                        	SRG context freed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_count
                        
                        	Number of SODs Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: eod_count
                        
                        	Number of EODs Received
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_replay_req_count
                        
                        	Number of Replay Requests Within SOD EOD Window
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_dirty_mark_count
                        
                        	Number of Sessions Marked as Invalid Within SOD EOD Window
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_dirty_delete_count
                        
                        	Number of Sessions Invalid Deletes Within SOD EOD Window
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ack_to_srg
                        
                        	Number of ACKs sent to Srg
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nack_to_srg
                        
                        	Number of NACKs sent to Srg
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nack_to_srg_fail_cnt
                        
                        	Number of NACKs Failed to send to Srg
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_remove_all
                        
                        	Number of Txlist remove all calls
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_sync
                        
                        	Number for Txlist delete for sync msg
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_sync_notlinked
                        
                        	Number of Txlist delete for sync which are not linked
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_app
                        
                        	Number of Txlist delete for App msg
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_app_notlinked
                        
                        	Number of Txlist delete for App which are not linked
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_clean_invalid_state
                        
                        	Number of Txlist Cleanup called on Invalid subscriber srg state
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_remove_all_internal_error
                        
                        	Number of Internal errors upon Master Txlist remove all call
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_srg_flow_control_enabled
                        
                        	Flag indicating SRG Flow control enabled or not
                        	**type**\: bool
                        
                        .. attribute:: max_inflight_sessoin_count
                        
                        	Maximum no.of inflight sessions allowed
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_control_resume_threshold
                        
                        	Threshold Limit to resume the flow control
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_session_count
                        
                        	No.of Sessions inflight at given time
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_add_count
                        
                        	No.of inflight sessions added
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_under_run_count
                        
                        	Inflight Underrun Counter
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_alloc_fails
                        
                        	Memory Alloc Failures for Inflight Entry
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_insert_failures
                        
                        	Inflight Entry Insert Failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_deletes
                        
                        	Inflight Deletes Count
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_not_found
                        
                        	Inflight Entries not found during delete
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_delete_failures
                        
                        	Inflight Entry Delete Failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_pause_count
                        
                        	Total No.of times Pause is Enabled
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_resume_count
                        
                        	Total No.of times Resume is triggered
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_dont_send_to_txlist
                        
                        	Total No of times Dont send to Txlist
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_srg_not_master
                        
                        	Total No of times SRG Not Master
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_master_eoms_pending
                        
                        	Total No of times Master EOMS Pending
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_pause_period
                        
                        	Amount of time paused during last flow control window
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_pause_time
                        
                        	Total Amount of time paused during all flow control windows
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_pause_time
                        
                        	Timestamp of recent Pause Event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_resume_time
                        
                        	Timestamp of recent Resume Event
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Manager.Nodes.Node.Statistics.Srg, self).__init__()

                            self.yang_name = "srg"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.txlist_send_triggered = YLeaf(YType.uint32, "txlist-send-triggered")

                            self.txlist_send_failed = YLeaf(YType.uint32, "txlist-send-failed")

                            self.txlist_send_failed_notactive = YLeaf(YType.uint32, "txlist-send-failed-notactive")

                            self.actual_txlist_sent = YLeaf(YType.uint32, "actual-txlist-sent")

                            self.alreadyin_txlist = YLeaf(YType.uint32, "alreadyin-txlist")

                            self.txlist_encode = YLeaf(YType.uint32, "txlist-encode")

                            self.txlist_encode_fail = YLeaf(YType.uint32, "txlist-encode-fail")

                            self.create_update_encode = YLeaf(YType.uint32, "create-update-encode")

                            self.delete_encode = YLeaf(YType.uint32, "delete-encode")

                            self.create_upd_clean_callback = YLeaf(YType.uint32, "create-upd-clean-callback")

                            self.delete_clean_callback = YLeaf(YType.uint32, "delete-clean-callback")

                            self.slave_recv_entry = YLeaf(YType.uint32, "slave-recv-entry")

                            self.slave_decode_fail = YLeaf(YType.uint32, "slave-decode-fail")

                            self.slave_create_update = YLeaf(YType.uint32, "slave-create-update")

                            self.slave_delete = YLeaf(YType.uint32, "slave-delete")

                            self.srg_context_malloc = YLeaf(YType.uint32, "srg-context-malloc")

                            self.srg_context_free = YLeaf(YType.uint32, "srg-context-free")

                            self.sod_count = YLeaf(YType.uint32, "sod-count")

                            self.eod_count = YLeaf(YType.uint32, "eod-count")

                            self.sod_eod_replay_req_count = YLeaf(YType.uint32, "sod-eod-replay-req-count")

                            self.sod_eod_dirty_mark_count = YLeaf(YType.uint32, "sod-eod-dirty-mark-count")

                            self.sod_eod_dirty_delete_count = YLeaf(YType.uint32, "sod-eod-dirty-delete-count")

                            self.ack_to_srg = YLeaf(YType.uint32, "ack-to-srg")

                            self.nack_to_srg = YLeaf(YType.uint32, "nack-to-srg")

                            self.nack_to_srg_fail_cnt = YLeaf(YType.uint32, "nack-to-srg-fail-cnt")

                            self.txlist_remove_all = YLeaf(YType.uint32, "txlist-remove-all")

                            self.txlist_del_sync = YLeaf(YType.uint32, "txlist-del-sync")

                            self.txlist_del_sync_notlinked = YLeaf(YType.uint32, "txlist-del-sync-notlinked")

                            self.txlist_del_app = YLeaf(YType.uint32, "txlist-del-app")

                            self.txlist_del_app_notlinked = YLeaf(YType.uint32, "txlist-del-app-notlinked")

                            self.txlist_clean_invalid_state = YLeaf(YType.uint32, "txlist-clean-invalid-state")

                            self.txlist_remove_all_internal_error = YLeaf(YType.uint32, "txlist-remove-all-internal-error")

                            self.is_srg_flow_control_enabled = YLeaf(YType.boolean, "is-srg-flow-control-enabled")

                            self.max_inflight_sessoin_count = YLeaf(YType.uint32, "max-inflight-sessoin-count")

                            self.flow_control_resume_threshold = YLeaf(YType.uint32, "flow-control-resume-threshold")

                            self.inflight_session_count = YLeaf(YType.uint32, "inflight-session-count")

                            self.inflight_add_count = YLeaf(YType.uint32, "inflight-add-count")

                            self.inflight_under_run_count = YLeaf(YType.uint32, "inflight-under-run-count")

                            self.inflight_alloc_fails = YLeaf(YType.uint32, "inflight-alloc-fails")

                            self.inflight_insert_failures = YLeaf(YType.uint32, "inflight-insert-failures")

                            self.inflight_deletes = YLeaf(YType.uint32, "inflight-deletes")

                            self.inflight_not_found = YLeaf(YType.uint32, "inflight-not-found")

                            self.inflight_delete_failures = YLeaf(YType.uint32, "inflight-delete-failures")

                            self.total_pause_count = YLeaf(YType.uint32, "total-pause-count")

                            self.total_resume_count = YLeaf(YType.uint32, "total-resume-count")

                            self.total_dont_send_to_txlist = YLeaf(YType.uint32, "total-dont-send-to-txlist")

                            self.total_srg_not_master = YLeaf(YType.uint32, "total-srg-not-master")

                            self.total_master_eoms_pending = YLeaf(YType.uint32, "total-master-eoms-pending")

                            self.last_pause_period = YLeaf(YType.uint64, "last-pause-period")

                            self.total_pause_time = YLeaf(YType.uint64, "total-pause-time")

                            self.last_pause_time = YLeaf(YType.uint64, "last-pause-time")

                            self.last_resume_time = YLeaf(YType.uint64, "last-resume-time")
                            self._segment_path = lambda: "srg"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Srg, ['txlist_send_triggered', 'txlist_send_failed', 'txlist_send_failed_notactive', 'actual_txlist_sent', 'alreadyin_txlist', 'txlist_encode', 'txlist_encode_fail', 'create_update_encode', 'delete_encode', 'create_upd_clean_callback', 'delete_clean_callback', 'slave_recv_entry', 'slave_decode_fail', 'slave_create_update', 'slave_delete', 'srg_context_malloc', 'srg_context_free', 'sod_count', 'eod_count', 'sod_eod_replay_req_count', 'sod_eod_dirty_mark_count', 'sod_eod_dirty_delete_count', 'ack_to_srg', 'nack_to_srg', 'nack_to_srg_fail_cnt', 'txlist_remove_all', 'txlist_del_sync', 'txlist_del_sync_notlinked', 'txlist_del_app', 'txlist_del_app_notlinked', 'txlist_clean_invalid_state', 'txlist_remove_all_internal_error', 'is_srg_flow_control_enabled', 'max_inflight_sessoin_count', 'flow_control_resume_threshold', 'inflight_session_count', 'inflight_add_count', 'inflight_under_run_count', 'inflight_alloc_fails', 'inflight_insert_failures', 'inflight_deletes', 'inflight_not_found', 'inflight_delete_failures', 'total_pause_count', 'total_resume_count', 'total_dont_send_to_txlist', 'total_srg_not_master', 'total_master_eoms_pending', 'last_pause_period', 'total_pause_time', 'last_pause_time', 'last_resume_time'], name, value)


    class Session(Entity):
        """
        Subscriber session operational data
        
        .. attribute:: nodes
        
        	List of subscriber session supported nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes>`
        
        

        """

        _prefix = 'iedge4710-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Subscriber.Session, self).__init__()

            self.yang_name = "session"
            self.yang_parent_name = "subscriber"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"nodes" : ("nodes", Subscriber.Session.Nodes)}
            self._child_list_classes = {}

            self.nodes = Subscriber.Session.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")
            self._segment_path = lambda: "session"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber/%s" % self._segment_path()


        class Nodes(Entity):
            """
            List of subscriber session supported nodes
            
            .. attribute:: node
            
            	Subscriber session operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node>`
            
            

            """

            _prefix = 'iedge4710-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Subscriber.Session.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "session"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"node" : ("node", Subscriber.Session.Nodes.Node)}

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber/session/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Subscriber.Session.Nodes, [], name, value)


            class Node(Entity):
                """
                Subscriber session operational data for a
                particular node
                
                .. attribute:: node_name  <key>
                
                	Node name
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: author_summaries
                
                	Summary information filtered by authorization state
                	**type**\:  :py:class:`AuthorSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries>`
                
                .. attribute:: summary
                
                	Subscriber session summary information
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary>`
                
                .. attribute:: mac_summaries
                
                	Summary information filtered by MAC address
                	**type**\:  :py:class:`MacSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries>`
                
                .. attribute:: interface_summaries
                
                	Summary information filtered by interface
                	**type**\:  :py:class:`InterfaceSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries>`
                
                .. attribute:: authentication_summaries
                
                	Summary information filtered by authentication state
                	**type**\:  :py:class:`AuthenticationSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries>`
                
                .. attribute:: state_summaries
                
                	Summary information filtered by session state
                	**type**\:  :py:class:`StateSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries>`
                
                .. attribute:: ipv4_address_vrf_summaries
                
                	Summary information filtered by IPv4 address and VRF
                	**type**\:  :py:class:`Ipv4AddressVrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries>`
                
                .. attribute:: address_family_summaries
                
                	Summary information filtered by address family
                	**type**\:  :py:class:`AddressFamilySummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries>`
                
                .. attribute:: username_summaries
                
                	Summary information filtered by username
                	**type**\:  :py:class:`UsernameSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries>`
                
                .. attribute:: access_interface_summaries
                
                	Summary information filtered by access interface
                	**type**\:  :py:class:`AccessInterfaceSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries>`
                
                .. attribute:: ipv4_address_summaries
                
                	Summary information filtered by subscriber IPv4 address
                	**type**\:  :py:class:`Ipv4AddressSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries>`
                
                .. attribute:: vrf_summaries
                
                	Summary information filtered by VRF
                	**type**\:  :py:class:`VrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries>`
                
                .. attribute:: sessions
                
                	IP subscriber sessions
                	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions>`
                
                

                """

                _prefix = 'iedge4710-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Subscriber.Session.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"author-summaries" : ("author_summaries", Subscriber.Session.Nodes.Node.AuthorSummaries), "summary" : ("summary", Subscriber.Session.Nodes.Node.Summary), "mac-summaries" : ("mac_summaries", Subscriber.Session.Nodes.Node.MacSummaries), "interface-summaries" : ("interface_summaries", Subscriber.Session.Nodes.Node.InterfaceSummaries), "authentication-summaries" : ("authentication_summaries", Subscriber.Session.Nodes.Node.AuthenticationSummaries), "state-summaries" : ("state_summaries", Subscriber.Session.Nodes.Node.StateSummaries), "ipv4-address-vrf-summaries" : ("ipv4_address_vrf_summaries", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries), "address-family-summaries" : ("address_family_summaries", Subscriber.Session.Nodes.Node.AddressFamilySummaries), "username-summaries" : ("username_summaries", Subscriber.Session.Nodes.Node.UsernameSummaries), "access-interface-summaries" : ("access_interface_summaries", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries), "ipv4-address-summaries" : ("ipv4_address_summaries", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries), "vrf-summaries" : ("vrf_summaries", Subscriber.Session.Nodes.Node.VrfSummaries), "sessions" : ("sessions", Subscriber.Session.Nodes.Node.Sessions)}
                    self._child_list_classes = {}

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.author_summaries = Subscriber.Session.Nodes.Node.AuthorSummaries()
                    self.author_summaries.parent = self
                    self._children_name_map["author_summaries"] = "author-summaries"
                    self._children_yang_names.add("author-summaries")

                    self.summary = Subscriber.Session.Nodes.Node.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")

                    self.mac_summaries = Subscriber.Session.Nodes.Node.MacSummaries()
                    self.mac_summaries.parent = self
                    self._children_name_map["mac_summaries"] = "mac-summaries"
                    self._children_yang_names.add("mac-summaries")

                    self.interface_summaries = Subscriber.Session.Nodes.Node.InterfaceSummaries()
                    self.interface_summaries.parent = self
                    self._children_name_map["interface_summaries"] = "interface-summaries"
                    self._children_yang_names.add("interface-summaries")

                    self.authentication_summaries = Subscriber.Session.Nodes.Node.AuthenticationSummaries()
                    self.authentication_summaries.parent = self
                    self._children_name_map["authentication_summaries"] = "authentication-summaries"
                    self._children_yang_names.add("authentication-summaries")

                    self.state_summaries = Subscriber.Session.Nodes.Node.StateSummaries()
                    self.state_summaries.parent = self
                    self._children_name_map["state_summaries"] = "state-summaries"
                    self._children_yang_names.add("state-summaries")

                    self.ipv4_address_vrf_summaries = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries()
                    self.ipv4_address_vrf_summaries.parent = self
                    self._children_name_map["ipv4_address_vrf_summaries"] = "ipv4-address-vrf-summaries"
                    self._children_yang_names.add("ipv4-address-vrf-summaries")

                    self.address_family_summaries = Subscriber.Session.Nodes.Node.AddressFamilySummaries()
                    self.address_family_summaries.parent = self
                    self._children_name_map["address_family_summaries"] = "address-family-summaries"
                    self._children_yang_names.add("address-family-summaries")

                    self.username_summaries = Subscriber.Session.Nodes.Node.UsernameSummaries()
                    self.username_summaries.parent = self
                    self._children_name_map["username_summaries"] = "username-summaries"
                    self._children_yang_names.add("username-summaries")

                    self.access_interface_summaries = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries()
                    self.access_interface_summaries.parent = self
                    self._children_name_map["access_interface_summaries"] = "access-interface-summaries"
                    self._children_yang_names.add("access-interface-summaries")

                    self.ipv4_address_summaries = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries()
                    self.ipv4_address_summaries.parent = self
                    self._children_name_map["ipv4_address_summaries"] = "ipv4-address-summaries"
                    self._children_yang_names.add("ipv4-address-summaries")

                    self.vrf_summaries = Subscriber.Session.Nodes.Node.VrfSummaries()
                    self.vrf_summaries.parent = self
                    self._children_name_map["vrf_summaries"] = "vrf-summaries"
                    self._children_yang_names.add("vrf-summaries")

                    self.sessions = Subscriber.Session.Nodes.Node.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")
                    self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber/session/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Subscriber.Session.Nodes.Node, ['node_name'], name, value)


                class AuthorSummaries(Entity):
                    """
                    Summary information filtered by authorization
                    state
                    
                    .. attribute:: author_summary
                    
                    	authorization summary
                    	**type**\: list of  		 :py:class:`AuthorSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.AuthorSummaries, self).__init__()

                        self.yang_name = "author-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"author-summary" : ("author_summary", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary)}

                        self.author_summary = YList(self)
                        self._segment_path = lambda: "author-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries, [], name, value)


                    class AuthorSummary(Entity):
                        """
                        authorization summary
                        
                        .. attribute:: author_state  <key>
                        
                        	Authorization state
                        	**type**\:  :py:class:`SubscriberAuthorStateFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAuthorStateFilterFlag>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary, self).__init__()

                            self.yang_name = "author-summary"
                            self.yang_parent_name = "author-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.author_state = YLeaf(YType.enumeration, "author-state")

                            self.state_xr = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "author-summary" + "[author-state='" + self.author_state.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary, ['author_state'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "author-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "author-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class Summary(Entity):
                    """
                    Subscriber session summary information
                    
                    .. attribute:: state_xr
                    
                    	State summary
                    	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr>`
                    
                    .. attribute:: address_family_xr
                    
                    	Address family summary
                    	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.Summary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr)}
                        self._child_list_classes = {}

                        self.state_xr = Subscriber.Session.Nodes.Node.Summary.StateXr()
                        self.state_xr.parent = self
                        self._children_name_map["state_xr"] = "state-xr"
                        self._children_yang_names.add("state-xr")

                        self.address_family_xr = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr()
                        self.address_family_xr.parent = self
                        self._children_name_map["address_family_xr"] = "address-family-xr"
                        self._children_yang_names.add("address-family-xr")
                        self._segment_path = lambda: "summary"


                    class StateXr(Entity):
                        """
                        State summary
                        
                        .. attribute:: pppoe
                        
                        	PPPoE summary
                        	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe>`
                        
                        .. attribute:: ip_subscriber_dhcp
                        
                        	IP subscriber DHCP summary
                        	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp>`
                        
                        .. attribute:: ip_subscriber_packet
                        
                        	IP subscriber packet summary
                        	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Summary.StateXr, self).__init__()

                            self.yang_name = "state-xr"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket)}
                            self._child_list_classes = {}

                            self.pppoe = Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe()
                            self.pppoe.parent = self
                            self._children_name_map["pppoe"] = "pppoe"
                            self._children_yang_names.add("pppoe")

                            self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp()
                            self.ip_subscriber_dhcp.parent = self
                            self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                            self._children_yang_names.add("ip-subscriber-dhcp")

                            self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket()
                            self.ip_subscriber_packet.parent = self
                            self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                            self._children_yang_names.add("ip-subscriber-packet")
                            self._segment_path = lambda: "state-xr"


                        class Pppoe(Entity):
                            """
                            PPPoE summary
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe, self).__init__()

                                self.yang_name = "pppoe"
                                self.yang_parent_name = "state-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                self._segment_path = lambda: "pppoe"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class IpSubscriberDhcp(Entity):
                            """
                            IP subscriber DHCP summary
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp, self).__init__()

                                self.yang_name = "ip-subscriber-dhcp"
                                self.yang_parent_name = "state-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                self._segment_path = lambda: "ip-subscriber-dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class IpSubscriberPacket(Entity):
                            """
                            IP subscriber packet summary
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket, self).__init__()

                                self.yang_name = "ip-subscriber-packet"
                                self.yang_parent_name = "state-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                self._segment_path = lambda: "ip-subscriber-packet"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                    class AddressFamilyXr(Entity):
                        """
                        Address family summary
                        
                        .. attribute:: pppoe
                        
                        	PPPoE summary
                        	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe>`
                        
                        .. attribute:: ip_subscriber_dhcp
                        
                        	IP subscriber DHCP summary
                        	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp>`
                        
                        .. attribute:: ip_subscriber_packet
                        
                        	IP subscriber packet summary
                        	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr, self).__init__()

                            self.yang_name = "address-family-xr"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket)}
                            self._child_list_classes = {}

                            self.pppoe = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe()
                            self.pppoe.parent = self
                            self._children_name_map["pppoe"] = "pppoe"
                            self._children_yang_names.add("pppoe")

                            self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp()
                            self.ip_subscriber_dhcp.parent = self
                            self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                            self._children_yang_names.add("ip-subscriber-dhcp")

                            self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket()
                            self.ip_subscriber_packet.parent = self
                            self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                            self._children_yang_names.add("ip-subscriber-packet")
                            self._segment_path = lambda: "address-family-xr"


                        class Pppoe(Entity):
                            """
                            PPPoE summary
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe, self).__init__()

                                self.yang_name = "pppoe"
                                self.yang_parent_name = "address-family-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                self._segment_path = lambda: "pppoe"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                        class IpSubscriberDhcp(Entity):
                            """
                            IP subscriber DHCP summary
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                self.yang_name = "ip-subscriber-dhcp"
                                self.yang_parent_name = "address-family-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                self._segment_path = lambda: "ip-subscriber-dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                        class IpSubscriberPacket(Entity):
                            """
                            IP subscriber packet summary
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                self.yang_name = "ip-subscriber-packet"
                                self.yang_parent_name = "address-family-xr"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                self._segment_path = lambda: "ip-subscriber-packet"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class MacSummaries(Entity):
                    """
                    Summary information filtered by MAC address
                    
                    .. attribute:: mac_summary
                    
                    	MAC address summary
                    	**type**\: list of  		 :py:class:`MacSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.MacSummaries, self).__init__()

                        self.yang_name = "mac-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"mac-summary" : ("mac_summary", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary)}

                        self.mac_summary = YList(self)
                        self._segment_path = lambda: "mac-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries, [], name, value)


                    class MacSummary(Entity):
                        """
                        MAC address summary
                        
                        .. attribute:: mac_address  <key>
                        
                        	Subscriber MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary, self).__init__()

                            self.yang_name = "mac-summary"
                            self.yang_parent_name = "mac-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.state_xr = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "mac-summary" + "[mac-address='" + self.mac_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary, ['mac_address'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "mac-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "mac-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class InterfaceSummaries(Entity):
                    """
                    Summary information filtered by interface
                    
                    .. attribute:: interface_summary
                    
                    	Interface summary
                    	**type**\: list of  		 :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.InterfaceSummaries, self).__init__()

                        self.yang_name = "interface-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"interface-summary" : ("interface_summary", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary)}

                        self.interface_summary = YList(self)
                        self._segment_path = lambda: "interface-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries, [], name, value)


                    class InterfaceSummary(Entity):
                        """
                        Interface summary
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary, self).__init__()

                            self.yang_name = "interface-summary"
                            self.yang_parent_name = "interface-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.state_xr = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "interface-summary" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary, ['interface_name'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class AuthenticationSummaries(Entity):
                    """
                    Summary information filtered by
                    authentication state
                    
                    .. attribute:: authentication_summary
                    
                    	authentication summary
                    	**type**\: list of  		 :py:class:`AuthenticationSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.AuthenticationSummaries, self).__init__()

                        self.yang_name = "authentication-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"authentication-summary" : ("authentication_summary", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary)}

                        self.authentication_summary = YList(self)
                        self._segment_path = lambda: "authentication-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries, [], name, value)


                    class AuthenticationSummary(Entity):
                        """
                        authentication summary
                        
                        .. attribute:: authentication_state  <key>
                        
                        	Authentication state
                        	**type**\:  :py:class:`SubscriberAuthenStateFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAuthenStateFilterFlag>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary, self).__init__()

                            self.yang_name = "authentication-summary"
                            self.yang_parent_name = "authentication-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.authentication_state = YLeaf(YType.enumeration, "authentication-state")

                            self.state_xr = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "authentication-summary" + "[authentication-state='" + self.authentication_state.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary, ['authentication_state'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "authentication-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "authentication-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class StateSummaries(Entity):
                    """
                    Summary information filtered by session state
                    
                    .. attribute:: state_summary
                    
                    	State summary
                    	**type**\: list of  		 :py:class:`StateSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.StateSummaries, self).__init__()

                        self.yang_name = "state-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"state-summary" : ("state_summary", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary)}

                        self.state_summary = YList(self)
                        self._segment_path = lambda: "state-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries, [], name, value)


                    class StateSummary(Entity):
                        """
                        State summary
                        
                        .. attribute:: state  <key>
                        
                        	Subscriber state
                        	**type**\:  :py:class:`SubscriberStateFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberStateFilterFlag>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary, self).__init__()

                            self.yang_name = "state-summary"
                            self.yang_parent_name = "state-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.state = YLeaf(YType.enumeration, "state")

                            self.state_xr = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "state-summary" + "[state='" + self.state.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary, ['state'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "state-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "state-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class Ipv4AddressVrfSummaries(Entity):
                    """
                    Summary information filtered by IPv4 address
                    and VRF
                    
                    .. attribute:: ipv4_address_vrf_summary
                    
                    	IPv4 address and VRF summary
                    	**type**\: list of  		 :py:class:`Ipv4AddressVrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries, self).__init__()

                        self.yang_name = "ipv4-address-vrf-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"ipv4-address-vrf-summary" : ("ipv4_address_vrf_summary", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary)}

                        self.ipv4_address_vrf_summary = YList(self)
                        self._segment_path = lambda: "ipv4-address-vrf-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries, [], name, value)


                    class Ipv4AddressVrfSummary(Entity):
                        """
                        IPv4 address and VRF summary
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: address
                        
                        	Subscriber IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary, self).__init__()

                            self.yang_name = "ipv4-address-vrf-summary"
                            self.yang_parent_name = "ipv4-address-vrf-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.address = YLeaf(YType.str, "address")

                            self.state_xr = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "ipv4-address-vrf-summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary, ['vrf_name', 'address'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "ipv4-address-vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "ipv4-address-vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class AddressFamilySummaries(Entity):
                    """
                    Summary information filtered by address
                    family
                    
                    .. attribute:: address_family_summary
                    
                    	Address family summary
                    	**type**\: list of  		 :py:class:`AddressFamilySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.AddressFamilySummaries, self).__init__()

                        self.yang_name = "address-family-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"address-family-summary" : ("address_family_summary", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary)}

                        self.address_family_summary = YList(self)
                        self._segment_path = lambda: "address-family-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries, [], name, value)


                    class AddressFamilySummary(Entity):
                        """
                        Address family summary
                        
                        .. attribute:: address_family  <key>
                        
                        	Address family
                        	**type**\:  :py:class:`SubscriberAddressFamilyFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAddressFamilyFilterFlag>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary, self).__init__()

                            self.yang_name = "address-family-summary"
                            self.yang_parent_name = "address-family-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.address_family = YLeaf(YType.enumeration, "address-family")

                            self.state_xr = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "address-family-summary" + "[address-family='" + self.address_family.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary, ['address_family'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "address-family-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "address-family-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class UsernameSummaries(Entity):
                    """
                    Summary information filtered by username
                    
                    .. attribute:: username_summary
                    
                    	Username summary
                    	**type**\: list of  		 :py:class:`UsernameSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.UsernameSummaries, self).__init__()

                        self.yang_name = "username-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"username-summary" : ("username_summary", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary)}

                        self.username_summary = YList(self)
                        self._segment_path = lambda: "username-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries, [], name, value)


                    class UsernameSummary(Entity):
                        """
                        Username summary
                        
                        .. attribute:: username  <key>
                        
                        	Subscriber username
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary, self).__init__()

                            self.yang_name = "username-summary"
                            self.yang_parent_name = "username-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.username = YLeaf(YType.str, "username")

                            self.state_xr = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "username-summary" + "[username='" + self.username.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary, ['username'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "username-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "username-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class AccessInterfaceSummaries(Entity):
                    """
                    Summary information filtered by access
                    interface
                    
                    .. attribute:: access_interface_summary
                    
                    	Access interface summary
                    	**type**\: list of  		 :py:class:`AccessInterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries, self).__init__()

                        self.yang_name = "access-interface-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"access-interface-summary" : ("access_interface_summary", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary)}

                        self.access_interface_summary = YList(self)
                        self._segment_path = lambda: "access-interface-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries, [], name, value)


                    class AccessInterfaceSummary(Entity):
                        """
                        Access interface summary
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary, self).__init__()

                            self.yang_name = "access-interface-summary"
                            self.yang_parent_name = "access-interface-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.state_xr = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "access-interface-summary" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary, ['interface_name'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "access-interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "access-interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class Ipv4AddressSummaries(Entity):
                    """
                    Summary information filtered by subscriber
                    IPv4 address
                    
                    .. attribute:: ipv4_address_summary
                    
                    	IPv4 address summary
                    	**type**\: list of  		 :py:class:`Ipv4AddressSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries, self).__init__()

                        self.yang_name = "ipv4-address-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"ipv4-address-summary" : ("ipv4_address_summary", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary)}

                        self.ipv4_address_summary = YList(self)
                        self._segment_path = lambda: "ipv4-address-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries, [], name, value)


                    class Ipv4AddressSummary(Entity):
                        """
                        IPv4 address summary
                        
                        .. attribute:: address  <key>
                        
                        	Subscriber IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary, self).__init__()

                            self.yang_name = "ipv4-address-summary"
                            self.yang_parent_name = "ipv4-address-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.state_xr = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "ipv4-address-summary" + "[address='" + self.address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary, ['address'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "ipv4-address-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "ipv4-address-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class VrfSummaries(Entity):
                    """
                    Summary information filtered by VRF
                    
                    .. attribute:: vrf_summary
                    
                    	VRF summary
                    	**type**\: list of  		 :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.VrfSummaries, self).__init__()

                        self.yang_name = "vrf-summaries"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"vrf-summary" : ("vrf_summary", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary)}

                        self.vrf_summary = YList(self)
                        self._segment_path = lambda: "vrf-summaries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries, [], name, value)


                    class VrfSummary(Entity):
                        """
                        VRF summary
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:  :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:  :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary, self).__init__()

                            self.yang_name = "vrf-summary"
                            self.yang_parent_name = "vrf-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr), "address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr)}
                            self._child_list_classes = {}

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.state_xr = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")
                            self._segment_path = lambda: "vrf-summary" + "[vrf-name='" + self.vrf_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary, ['vrf_name'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "state-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "state-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket, ['initialized_sessions', 'connecting_sessions', 'connected_sessions', 'activated_sessions', 'idle_sessions', 'disconnecting_sessions', 'end_sessions'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:  :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe>`
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:  :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:  :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe), "ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket)}
                                self._child_list_classes = {}

                                self.pppoe = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")
                                self._segment_path = lambda: "address-family-xr"


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe, self).__init__()

                                    self.yang_name = "pppoe"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp, self).__init__()

                                    self.yang_name = "ip-subscriber-dhcp"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket, self).__init__()

                                    self.yang_name = "ip-subscriber-packet"
                                    self.yang_parent_name = "address-family-xr"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket, ['in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'dual_part_up_sessions', 'dual_up_sessions', 'lac_sessions'], name, value)


                class Sessions(Entity):
                    """
                    IP subscriber sessions
                    
                    .. attribute:: session
                    
                    	Subscriber session information
                    	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"session" : ("session", Subscriber.Session.Nodes.Node.Sessions.Session)}

                        self.session = YList(self)
                        self._segment_path = lambda: "sessions"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions, [], name, value)


                    class Session(Entity):
                        """
                        Subscriber session information
                        
                        .. attribute:: session_id  <key>
                        
                        	Session ID
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: accounting
                        
                        	Accounting information
                        	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.Accounting>`
                        
                        .. attribute:: user_profile_attributes
                        
                        	List of user profile attributes collected for subscriber session
                        	**type**\:  :py:class:`UserProfileAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes>`
                        
                        .. attribute:: mobility_attributes
                        
                        	List of mobility attributes collected for subscriber session
                        	**type**\:  :py:class:`MobilityAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes>`
                        
                        .. attribute:: session_type
                        
                        	Subscriber session type
                        	**type**\:  :py:class:`IedgeOperSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSession>`
                        
                        .. attribute:: pppoe_sub_type
                        
                        	PPPoE sub type
                        	**type**\:  :py:class:`IedgePppSub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgePppSub>`
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\: str
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\: str
                        
                        .. attribute:: lns_address
                        
                        	PPPoE LNS address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: lac_address
                        
                        	PPPoE LAC address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: tunnel_client_authentication_id
                        
                        	PPPoE LAC tunnel client authentication ID
                        	**type**\: str
                        
                        .. attribute:: tunnel_server_authentication_id
                        
                        	PPPoE LAC tunnel server authentication ID
                        	**type**\: str
                        
                        .. attribute:: session_ip_address
                        
                        	Session ip address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: session_ipv6_address
                        
                        	Session IPv6 address
                        	**type**\: str
                        
                        .. attribute:: session_ipv6_prefix
                        
                        	Session IPv6 prefix
                        	**type**\: str
                        
                        .. attribute:: delegated_ipv6_prefix
                        
                        	Session delegated IPv6 prefix
                        	**type**\: str
                        
                        .. attribute:: ipv6_interface_id
                        
                        	IPv6 Interface ID
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: account_session_id
                        
                        	Accounting session ID
                        	**type**\: str
                        
                        .. attribute:: nas_port
                        
                        	NAS port
                        	**type**\: str
                        
                        .. attribute:: username
                        
                        	Username
                        	**type**\: str
                        
                        .. attribute:: clientname
                        
                        	Client Username
                        	**type**\: str
                        
                        .. attribute:: formattedname
                        
                        	Formatted Username
                        	**type**\: str
                        
                        .. attribute:: is_session_authentic
                        
                        	If true, session is authentic
                        	**type**\: bool
                        
                        .. attribute:: is_session_author
                        
                        	If true, session is authorized
                        	**type**\: bool
                        
                        .. attribute:: session_state
                        
                        	Session state
                        	**type**\:  :py:class:`IedgeOperSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionState>`
                        
                        .. attribute:: session_creation_time
                        
                        	Session creation time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                        	**type**\: str
                        
                        .. attribute:: idle_state_change_time
                        
                        	Time when idle state change occurred in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                        	**type**\: str
                        
                        .. attribute:: total_session_idle_time
                        
                        	Total session idle time (in seconds)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: access_interface_name
                        
                        	Access interface name associated with the session
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: pending_callbacks
                        
                        	Active pending callbacks bitmask
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: af_up_status
                        
                        	AF status per Subscriber Session
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: session_ipv4_state
                        
                        	Session IPv4 state
                        	**type**\:  :py:class:`IedgeOperSessionAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionAfState>`
                        
                        .. attribute:: session_ipv6_state
                        
                        	Session IPv6 state
                        	**type**\:  :py:class:`IedgeOperSessionAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionAfState>`
                        
                        .. attribute:: session_change_of_authorization
                        
                        	Subscriber change of authorization information
                        	**type**\: list of  		 :py:class:`SessionChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.SessionChangeOfAuthorization>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Sessions.Session, self).__init__()

                            self.yang_name = "session"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"accounting" : ("accounting", Subscriber.Session.Nodes.Node.Sessions.Session.Accounting), "user-profile-attributes" : ("user_profile_attributes", Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes), "mobility-attributes" : ("mobility_attributes", Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes)}
                            self._child_list_classes = {"session-change-of-authorization" : ("session_change_of_authorization", Subscriber.Session.Nodes.Node.Sessions.Session.SessionChangeOfAuthorization)}

                            self.session_id = YLeaf(YType.str, "session-id")

                            self.session_type = YLeaf(YType.enumeration, "session-type")

                            self.pppoe_sub_type = YLeaf(YType.enumeration, "pppoe-sub-type")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.circuit_id = YLeaf(YType.str, "circuit-id")

                            self.remote_id = YLeaf(YType.str, "remote-id")

                            self.lns_address = YLeaf(YType.str, "lns-address")

                            self.lac_address = YLeaf(YType.str, "lac-address")

                            self.tunnel_client_authentication_id = YLeaf(YType.str, "tunnel-client-authentication-id")

                            self.tunnel_server_authentication_id = YLeaf(YType.str, "tunnel-server-authentication-id")

                            self.session_ip_address = YLeaf(YType.str, "session-ip-address")

                            self.session_ipv6_address = YLeaf(YType.str, "session-ipv6-address")

                            self.session_ipv6_prefix = YLeaf(YType.str, "session-ipv6-prefix")

                            self.delegated_ipv6_prefix = YLeaf(YType.str, "delegated-ipv6-prefix")

                            self.ipv6_interface_id = YLeaf(YType.str, "ipv6-interface-id")

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.account_session_id = YLeaf(YType.str, "account-session-id")

                            self.nas_port = YLeaf(YType.str, "nas-port")

                            self.username = YLeaf(YType.str, "username")

                            self.clientname = YLeaf(YType.str, "clientname")

                            self.formattedname = YLeaf(YType.str, "formattedname")

                            self.is_session_authentic = YLeaf(YType.boolean, "is-session-authentic")

                            self.is_session_author = YLeaf(YType.boolean, "is-session-author")

                            self.session_state = YLeaf(YType.enumeration, "session-state")

                            self.session_creation_time = YLeaf(YType.str, "session-creation-time")

                            self.idle_state_change_time = YLeaf(YType.str, "idle-state-change-time")

                            self.total_session_idle_time = YLeaf(YType.uint32, "total-session-idle-time")

                            self.access_interface_name = YLeaf(YType.str, "access-interface-name")

                            self.pending_callbacks = YLeaf(YType.uint64, "pending-callbacks")

                            self.af_up_status = YLeaf(YType.uint32, "af-up-status")

                            self.session_ipv4_state = YLeaf(YType.enumeration, "session-ipv4-state")

                            self.session_ipv6_state = YLeaf(YType.enumeration, "session-ipv6-state")

                            self.accounting = Subscriber.Session.Nodes.Node.Sessions.Session.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                            self._children_yang_names.add("accounting")

                            self.user_profile_attributes = Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes()
                            self.user_profile_attributes.parent = self
                            self._children_name_map["user_profile_attributes"] = "user-profile-attributes"
                            self._children_yang_names.add("user-profile-attributes")

                            self.mobility_attributes = Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes()
                            self.mobility_attributes.parent = self
                            self._children_name_map["mobility_attributes"] = "mobility-attributes"
                            self._children_yang_names.add("mobility-attributes")

                            self.session_change_of_authorization = YList(self)
                            self._segment_path = lambda: "session" + "[session-id='" + self.session_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session, ['session_id', 'session_type', 'pppoe_sub_type', 'interface_name', 'vrf_name', 'circuit_id', 'remote_id', 'lns_address', 'lac_address', 'tunnel_client_authentication_id', 'tunnel_server_authentication_id', 'session_ip_address', 'session_ipv6_address', 'session_ipv6_prefix', 'delegated_ipv6_prefix', 'ipv6_interface_id', 'mac_address', 'account_session_id', 'nas_port', 'username', 'clientname', 'formattedname', 'is_session_authentic', 'is_session_author', 'session_state', 'session_creation_time', 'idle_state_change_time', 'total_session_idle_time', 'access_interface_name', 'pending_callbacks', 'af_up_status', 'session_ipv4_state', 'session_ipv6_state'], name, value)


                        class Accounting(Entity):
                            """
                            Accounting information
                            
                            .. attribute:: accounting_session
                            
                            	Accounting information
                            	**type**\: list of  		 :py:class:`AccountingSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.Accounting.AccountingSession>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Sessions.Session.Accounting, self).__init__()

                                self.yang_name = "accounting"
                                self.yang_parent_name = "session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"accounting-session" : ("accounting_session", Subscriber.Session.Nodes.Node.Sessions.Session.Accounting.AccountingSession)}

                                self.accounting_session = YList(self)
                                self._segment_path = lambda: "accounting"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.Accounting, [], name, value)


                            class AccountingSession(Entity):
                                """
                                Accounting information
                                
                                .. attribute:: accounting_state_rc
                                
                                	Accounting State Error Code for Accounting Session
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: accounting_stop_state
                                
                                	Accounting Stop State
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: record_context_name
                                
                                	Accounting record context name
                                	**type**\: str
                                
                                .. attribute:: method_list_name
                                
                                	AAA method list name used to perform accounting
                                	**type**\: str
                                
                                .. attribute:: account_session_id
                                
                                	Accounting session ID
                                	**type**\: str
                                
                                .. attribute:: accounting_start_time
                                
                                	Accounting start time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Feb 15 15\:12\:49 2011
                                	**type**\: str
                                
                                .. attribute:: is_interim_accounting_enabled
                                
                                	True if interim accounting is enabled
                                	**type**\: bool
                                
                                .. attribute:: interim_interval
                                
                                	Interim accounting interval (in minutes)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: minute
                                
                                .. attribute:: last_successful_interim_update_time
                                
                                	Time of last successful interim update in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30 \:47 2011
                                	**type**\: str
                                
                                .. attribute:: next_interim_update_attempt_time
                                
                                	Time of next interim update attempt (in seconds)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: last_interim_update_attempt_time
                                
                                	Time of last interim update attempt in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                                	**type**\: str
                                
                                .. attribute:: sent_interim_updates
                                
                                	Number of interim updates sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: accepted_interim_updates
                                
                                	Number of interim updates accepted
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rejected_interim_updates
                                
                                	Number of interim updates rejected
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sent_interim_update_failures
                                
                                	Number of interim update send failures
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Session.Nodes.Node.Sessions.Session.Accounting.AccountingSession, self).__init__()

                                    self.yang_name = "accounting-session"
                                    self.yang_parent_name = "accounting"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.accounting_state_rc = YLeaf(YType.uint32, "accounting-state-rc")

                                    self.accounting_stop_state = YLeaf(YType.uint32, "accounting-stop-state")

                                    self.record_context_name = YLeaf(YType.str, "record-context-name")

                                    self.method_list_name = YLeaf(YType.str, "method-list-name")

                                    self.account_session_id = YLeaf(YType.str, "account-session-id")

                                    self.accounting_start_time = YLeaf(YType.str, "accounting-start-time")

                                    self.is_interim_accounting_enabled = YLeaf(YType.boolean, "is-interim-accounting-enabled")

                                    self.interim_interval = YLeaf(YType.uint32, "interim-interval")

                                    self.last_successful_interim_update_time = YLeaf(YType.str, "last-successful-interim-update-time")

                                    self.next_interim_update_attempt_time = YLeaf(YType.uint32, "next-interim-update-attempt-time")

                                    self.last_interim_update_attempt_time = YLeaf(YType.str, "last-interim-update-attempt-time")

                                    self.sent_interim_updates = YLeaf(YType.uint32, "sent-interim-updates")

                                    self.accepted_interim_updates = YLeaf(YType.uint32, "accepted-interim-updates")

                                    self.rejected_interim_updates = YLeaf(YType.uint32, "rejected-interim-updates")

                                    self.sent_interim_update_failures = YLeaf(YType.uint32, "sent-interim-update-failures")
                                    self._segment_path = lambda: "accounting-session"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.Accounting.AccountingSession, ['accounting_state_rc', 'accounting_stop_state', 'record_context_name', 'method_list_name', 'account_session_id', 'accounting_start_time', 'is_interim_accounting_enabled', 'interim_interval', 'last_successful_interim_update_time', 'next_interim_update_attempt_time', 'last_interim_update_attempt_time', 'sent_interim_updates', 'accepted_interim_updates', 'rejected_interim_updates', 'sent_interim_update_failures'], name, value)


                        class UserProfileAttributes(Entity):
                            """
                            List of user profile attributes collected for
                            subscriber session
                            
                            .. attribute:: ipv4mtu
                            
                            	IPv4 maximum transmission unit
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_unnumbered
                            
                            	IPv4 unnumbered
                            	**type**\: str
                            
                            .. attribute:: authorization_service_type
                            
                            	Authorization service type
                            	**type**\:  :py:class:`AaaAuthService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaAuthService>`
                            
                            .. attribute:: tunnel_client_endpoint
                            
                            	Tunnel client endpoint
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tunnel_server_endpoint
                            
                            	Tunnel server endpoint
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tunnel_tos_setting
                            
                            	Tunnel TOS setting
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tunnel_medium
                            
                            	Tunnel medium
                            	**type**\:  :py:class:`AaaTunnelMedium <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTunnelMedium>`
                            
                            .. attribute:: tunnel_preference
                            
                            	Tunnel preference
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tunnel_client_authentication_id
                            
                            	Tunnel client authentication ID
                            	**type**\: str
                            
                            .. attribute:: tunnel_protocol
                            
                            	Tunnel protocol
                            	**type**\:  :py:class:`AaaTunnelProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTunnelProto>`
                            
                            .. attribute:: actual_data_rate_upstream
                            
                            	Actual data rate upstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: actual_data_rate_downstream
                            
                            	Actual data rate downstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: attainable_data_rate_upstream
                            
                            	Attainable data rate upstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: attainable_data_rate_downstream
                            
                            	Attainable data rate downstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: pool_address
                            
                            	IP address pool
                            	**type**\: str
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\: str
                            
                            .. attribute:: connection_receive_speed
                            
                            	Connection receive speed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connection_transmission_speed
                            
                            	Connection transmission speed
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: destination_station_id
                            
                            	Destination station ID
                            	**type**\: str
                            
                            .. attribute:: primary_dns_server_address
                            
                            	Primary DNS server address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary_dns_server_address
                            
                            	Secondary DNS server address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: formatted_calling_station_id
                            
                            	Formatted calling station id
                            	**type**\: str
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\: str
                            
                            .. attribute:: interface_type
                            
                            	Interface type
                            	**type**\:  :py:class:`AaaInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaInterface>`
                            
                            .. attribute:: interim_accounting_interval
                            
                            	Interim accounting interval
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ingress_access_list
                            
                            	Ingress access list
                            	**type**\: str
                            
                            .. attribute:: egress_access_list
                            
                            	Egress access list
                            	**type**\: str
                            
                            .. attribute:: ip_netmask
                            
                            	IP netmask for the user
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: is_interworking_functionality
                            
                            	True, if interworking functionality
                            	**type**\: bool
                            
                            .. attribute:: max_interleaving_delay_downstream
                            
                            	Maximum interleaving delay downstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_interleaving_delay_upstream
                            
                            	Maximum interleaving delay upstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_data_rate_upstream
                            
                            	Maximum data rate upstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_data_rate_downstream
                            
                            	Maximum data rate downstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_downstream
                            
                            	Minimum data rate downstream (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_downstream_low_power
                            
                            	Minimum data rate downstream low power (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_upstream_low_power
                            
                            	Minimum data rate upstream low power (in Mbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: primary_net_bios_server_address
                            
                            	Primary net bios server address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary_net_bios_server_address
                            
                            	Secondary net bios server address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: parent_interface_name
                            
                            	Parent interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            .. attribute:: route
                            
                            	Route information for a user session
                            	**type**\: str
                            
                            .. attribute:: session_timeout
                            
                            	Session timeout (in seconds)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: strict_rpf_packets
                            
                            	Strict RPF packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accounting_session_id
                            
                            	Accounting session ID
                            	**type**\: str
                            
                            .. attribute:: upstream_parameterized_qos_policy
                            
                            	Upstream parameterized QoS policy to be applied on the subscriber side
                            	**type**\: str
                            
                            .. attribute:: downstream_parameterized_qos_policy
                            
                            	Downstream parameterized QoS policy to be applied on the subscriber side
                            	**type**\: str
                            
                            .. attribute:: upstream_qos_policy
                            
                            	Upstream QoS policy to be applied on the subscriber side
                            	**type**\: str
                            
                            .. attribute:: downstream_qos_policy
                            
                            	Downstream QoS policy to be applied on the subscriber side
                            	**type**\: str
                            
                            .. attribute:: session_termination_cause
                            
                            	Session termination cause
                            	**type**\:  :py:class:`AaaTerminateCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTerminateCause>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes, self).__init__()

                                self.yang_name = "user-profile-attributes"
                                self.yang_parent_name = "session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv4mtu = YLeaf(YType.uint32, "ipv4mtu")

                                self.ipv4_unnumbered = YLeaf(YType.str, "ipv4-unnumbered")

                                self.authorization_service_type = YLeaf(YType.enumeration, "authorization-service-type")

                                self.tunnel_client_endpoint = YLeaf(YType.str, "tunnel-client-endpoint")

                                self.tunnel_server_endpoint = YLeaf(YType.str, "tunnel-server-endpoint")

                                self.tunnel_tos_setting = YLeaf(YType.uint32, "tunnel-tos-setting")

                                self.tunnel_medium = YLeaf(YType.enumeration, "tunnel-medium")

                                self.tunnel_preference = YLeaf(YType.uint32, "tunnel-preference")

                                self.tunnel_client_authentication_id = YLeaf(YType.str, "tunnel-client-authentication-id")

                                self.tunnel_protocol = YLeaf(YType.enumeration, "tunnel-protocol")

                                self.actual_data_rate_upstream = YLeaf(YType.uint32, "actual-data-rate-upstream")

                                self.actual_data_rate_downstream = YLeaf(YType.uint32, "actual-data-rate-downstream")

                                self.attainable_data_rate_upstream = YLeaf(YType.uint32, "attainable-data-rate-upstream")

                                self.attainable_data_rate_downstream = YLeaf(YType.uint32, "attainable-data-rate-downstream")

                                self.pool_address = YLeaf(YType.str, "pool-address")

                                self.circuit_id = YLeaf(YType.str, "circuit-id")

                                self.connection_receive_speed = YLeaf(YType.uint32, "connection-receive-speed")

                                self.connection_transmission_speed = YLeaf(YType.uint32, "connection-transmission-speed")

                                self.destination_station_id = YLeaf(YType.str, "destination-station-id")

                                self.primary_dns_server_address = YLeaf(YType.str, "primary-dns-server-address")

                                self.secondary_dns_server_address = YLeaf(YType.str, "secondary-dns-server-address")

                                self.formatted_calling_station_id = YLeaf(YType.str, "formatted-calling-station-id")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.interface_type = YLeaf(YType.enumeration, "interface-type")

                                self.interim_accounting_interval = YLeaf(YType.uint32, "interim-accounting-interval")

                                self.ingress_access_list = YLeaf(YType.str, "ingress-access-list")

                                self.egress_access_list = YLeaf(YType.str, "egress-access-list")

                                self.ip_netmask = YLeaf(YType.str, "ip-netmask")

                                self.is_interworking_functionality = YLeaf(YType.boolean, "is-interworking-functionality")

                                self.max_interleaving_delay_downstream = YLeaf(YType.uint32, "max-interleaving-delay-downstream")

                                self.max_interleaving_delay_upstream = YLeaf(YType.uint32, "max-interleaving-delay-upstream")

                                self.max_data_rate_upstream = YLeaf(YType.uint32, "max-data-rate-upstream")

                                self.max_data_rate_downstream = YLeaf(YType.uint32, "max-data-rate-downstream")

                                self.min_data_rate_downstream = YLeaf(YType.uint32, "min-data-rate-downstream")

                                self.min_data_rate_downstream_low_power = YLeaf(YType.uint32, "min-data-rate-downstream-low-power")

                                self.min_data_rate_upstream_low_power = YLeaf(YType.uint32, "min-data-rate-upstream-low-power")

                                self.primary_net_bios_server_address = YLeaf(YType.str, "primary-net-bios-server-address")

                                self.secondary_net_bios_server_address = YLeaf(YType.str, "secondary-net-bios-server-address")

                                self.parent_interface_name = YLeaf(YType.str, "parent-interface-name")

                                self.remote_id = YLeaf(YType.str, "remote-id")

                                self.route = YLeaf(YType.str, "route")

                                self.session_timeout = YLeaf(YType.uint32, "session-timeout")

                                self.strict_rpf_packets = YLeaf(YType.uint32, "strict-rpf-packets")

                                self.accounting_session_id = YLeaf(YType.str, "accounting-session-id")

                                self.upstream_parameterized_qos_policy = YLeaf(YType.str, "upstream-parameterized-qos-policy")

                                self.downstream_parameterized_qos_policy = YLeaf(YType.str, "downstream-parameterized-qos-policy")

                                self.upstream_qos_policy = YLeaf(YType.str, "upstream-qos-policy")

                                self.downstream_qos_policy = YLeaf(YType.str, "downstream-qos-policy")

                                self.session_termination_cause = YLeaf(YType.enumeration, "session-termination-cause")
                                self._segment_path = lambda: "user-profile-attributes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes, ['ipv4mtu', 'ipv4_unnumbered', 'authorization_service_type', 'tunnel_client_endpoint', 'tunnel_server_endpoint', 'tunnel_tos_setting', 'tunnel_medium', 'tunnel_preference', 'tunnel_client_authentication_id', 'tunnel_protocol', 'actual_data_rate_upstream', 'actual_data_rate_downstream', 'attainable_data_rate_upstream', 'attainable_data_rate_downstream', 'pool_address', 'circuit_id', 'connection_receive_speed', 'connection_transmission_speed', 'destination_station_id', 'primary_dns_server_address', 'secondary_dns_server_address', 'formatted_calling_station_id', 'interface_name', 'interface_type', 'interim_accounting_interval', 'ingress_access_list', 'egress_access_list', 'ip_netmask', 'is_interworking_functionality', 'max_interleaving_delay_downstream', 'max_interleaving_delay_upstream', 'max_data_rate_upstream', 'max_data_rate_downstream', 'min_data_rate_downstream', 'min_data_rate_downstream_low_power', 'min_data_rate_upstream_low_power', 'primary_net_bios_server_address', 'secondary_net_bios_server_address', 'parent_interface_name', 'remote_id', 'route', 'session_timeout', 'strict_rpf_packets', 'accounting_session_id', 'upstream_parameterized_qos_policy', 'downstream_parameterized_qos_policy', 'upstream_qos_policy', 'downstream_qos_policy', 'session_termination_cause'], name, value)


                        class MobilityAttributes(Entity):
                            """
                            List of mobility attributes collected for
                            subscriber session
                            
                            .. attribute:: mpc_protocol
                            
                            	Cisco MPC Protocol
                            	**type**\: bool
                            
                            .. attribute:: mobility_ipv4_address
                            
                            	IPv4 address of Mobility Node
                            	**type**\: str
                            
                            .. attribute:: mobility_default_ipv4_gateway
                            
                            	Default Gateway IPv4 Address
                            	**type**\: str
                            
                            .. attribute:: mobility_dns_server
                            
                            	DNS Server Primary
                            	**type**\: str
                            
                            .. attribute:: mobility_dhcp_server
                            
                            	DHCP Server
                            	**type**\: str
                            
                            .. attribute:: mobility_ipv4_netmask
                            
                            	IPv4 Netmask
                            	**type**\: str
                            
                            .. attribute:: domain_name
                            
                            	Domain Name
                            	**type**\: str
                            
                            .. attribute:: uplink_gre_key
                            
                            	Uplink GRE Key
                            	**type**\: str
                            
                            .. attribute:: downlink_gre_key
                            
                            	Downlink GRE Key
                            	**type**\: str
                            
                            .. attribute:: lease_time
                            
                            	Duration of lease in seconds
                            	**type**\: str
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes, self).__init__()

                                self.yang_name = "mobility-attributes"
                                self.yang_parent_name = "session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.mpc_protocol = YLeaf(YType.boolean, "mpc-protocol")

                                self.mobility_ipv4_address = YLeaf(YType.str, "mobility-ipv4-address")

                                self.mobility_default_ipv4_gateway = YLeaf(YType.str, "mobility-default-ipv4-gateway")

                                self.mobility_dns_server = YLeaf(YType.str, "mobility-dns-server")

                                self.mobility_dhcp_server = YLeaf(YType.str, "mobility-dhcp-server")

                                self.mobility_ipv4_netmask = YLeaf(YType.str, "mobility-ipv4-netmask")

                                self.domain_name = YLeaf(YType.str, "domain-name")

                                self.uplink_gre_key = YLeaf(YType.str, "uplink-gre-key")

                                self.downlink_gre_key = YLeaf(YType.str, "downlink-gre-key")

                                self.lease_time = YLeaf(YType.str, "lease-time")
                                self._segment_path = lambda: "mobility-attributes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes, ['mpc_protocol', 'mobility_ipv4_address', 'mobility_default_ipv4_gateway', 'mobility_dns_server', 'mobility_dhcp_server', 'mobility_ipv4_netmask', 'domain_name', 'uplink_gre_key', 'downlink_gre_key', 'lease_time'], name, value)


                        class SessionChangeOfAuthorization(Entity):
                            """
                            Subscriber change of authorization information
                            
                            .. attribute:: request_acked
                            
                            	Coa Request Acked
                            	**type**\: bool
                            
                            .. attribute:: request_time
                            
                            	Request time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                            	**type**\: str
                            
                            .. attribute:: coa_request_attributes
                            
                            	List of Request Attributes collected in COA response
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: reply_time
                            
                            	Reply time in DDD MMM DD HH\:MM\:SS YYYY format eg \: Tue Apr 11 21\:30\:47 2011
                            	**type**\: str
                            
                            .. attribute:: coa_reply_attributes
                            
                            	List of Reply Attributes collected in COA response
                            	**type**\: str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Sessions.Session.SessionChangeOfAuthorization, self).__init__()

                                self.yang_name = "session-change-of-authorization"
                                self.yang_parent_name = "session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.request_acked = YLeaf(YType.boolean, "request-acked")

                                self.request_time = YLeaf(YType.str, "request-time")

                                self.coa_request_attributes = YLeaf(YType.str, "coa-request-attributes")

                                self.reply_time = YLeaf(YType.str, "reply-time")

                                self.coa_reply_attributes = YLeaf(YType.str, "coa-reply-attributes")
                                self._segment_path = lambda: "session-change-of-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.SessionChangeOfAuthorization, ['request_acked', 'request_time', 'coa_request_attributes', 'reply_time', 'coa_reply_attributes'], name, value)

    def clone_ptr(self):
        self._top_entity = Subscriber()
        return self._top_entity

class IedgeLicenseManager(Entity):
    """
    iedge license manager
    
    .. attribute:: nodes
    
    	Session License Manager operational data for a location
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes>`
    
    

    """

    _prefix = 'iedge4710-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(IedgeLicenseManager, self).__init__()
        self._top_entity = None

        self.yang_name = "iedge-license-manager"
        self.yang_parent_name = "Cisco-IOS-XR-iedge4710-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", IedgeLicenseManager.Nodes)}
        self._child_list_classes = {}

        self.nodes = IedgeLicenseManager.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-iedge4710-oper:iedge-license-manager"


    class Nodes(Entity):
        """
        Session License Manager operational data for a
        location
        
        .. attribute:: node
        
        	Location. For example, 0/1/CPU0
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes.Node>`
        
        

        """

        _prefix = 'iedge4710-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(IedgeLicenseManager.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "iedge-license-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", IedgeLicenseManager.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:iedge-license-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IedgeLicenseManager.Nodes, [], name, value)


        class Node(Entity):
            """
            Location. For example, 0/1/CPU0
            
            .. attribute:: nodeid  <key>
            
            	The node id to filter on. For example, 0/1/CPU0
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: iedge_license_manager_summary
            
            	Display Session License Manager summary data
            	**type**\:  :py:class:`IedgeLicenseManagerSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary>`
            
            

            """

            _prefix = 'iedge4710-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(IedgeLicenseManager.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"iedge-license-manager-summary" : ("iedge_license_manager_summary", IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary)}
                self._child_list_classes = {}

                self.nodeid = YLeaf(YType.str, "nodeid")

                self.iedge_license_manager_summary = IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary()
                self.iedge_license_manager_summary.parent = self
                self._children_name_map["iedge_license_manager_summary"] = "iedge-license-manager-summary"
                self._children_yang_names.add("iedge-license-manager-summary")
                self._segment_path = lambda: "node" + "[nodeid='" + self.nodeid.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:iedge-license-manager/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IedgeLicenseManager.Nodes.Node, ['nodeid'], name, value)


            class IedgeLicenseManagerSummary(Entity):
                """
                Display Session License Manager summary data
                
                .. attribute:: session_limit
                
                	configured session limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_threshold
                
                	configured session threshold
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_license_count
                
                	number of license
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_count
                
                	number of sessions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'iedge4710-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary, self).__init__()

                    self.yang_name = "iedge-license-manager-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.session_limit = YLeaf(YType.uint32, "session-limit")

                    self.session_threshold = YLeaf(YType.uint32, "session-threshold")

                    self.session_license_count = YLeaf(YType.uint32, "session-license-count")

                    self.session_count = YLeaf(YType.uint32, "session-count")
                    self._segment_path = lambda: "iedge-license-manager-summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary, ['session_limit', 'session_threshold', 'session_license_count', 'session_count'], name, value)

    def clone_ptr(self):
        self._top_entity = IedgeLicenseManager()
        return self._top_entity

