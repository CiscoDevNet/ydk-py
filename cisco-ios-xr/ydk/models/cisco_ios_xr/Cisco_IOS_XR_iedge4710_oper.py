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



class IedgeLicenseManager(Entity):
    """
    iedge license manager
    
    .. attribute:: nodes
    
    	Session License Manager operational data for a location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes>`
    
    

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
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes.Node>`
        
        

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
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: iedge_license_manager_summary
            
            	Display Session License Manager summary data
            	**type**\:   :py:class:`IedgeLicenseManagerSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary>`
            
            

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
                
                .. attribute:: session_count
                
                	number of sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_license_count
                
                	number of license
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_limit
                
                	configured session limit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_threshold
                
                	configured session threshold
                	**type**\:  int
                
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

                    self.session_count = YLeaf(YType.uint32, "session-count")

                    self.session_license_count = YLeaf(YType.uint32, "session-license-count")

                    self.session_limit = YLeaf(YType.uint32, "session-limit")

                    self.session_threshold = YLeaf(YType.uint32, "session-threshold")
                    self._segment_path = lambda: "iedge-license-manager-summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary, ['session_count', 'session_license_count', 'session_limit', 'session_threshold'], name, value)

    def clone_ptr(self):
        self._top_entity = IedgeLicenseManager()
        return self._top_entity

class Subscriber(Entity):
    """
    Subscriber operational data
    
    .. attribute:: manager
    
    	Subscriber manager operational data
    	**type**\:   :py:class:`Manager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager>`
    
    .. attribute:: session
    
    	Subscriber session operational data
    	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session>`
    
    

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
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes>`
        
        

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
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node>`
            
            

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
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: statistics
                
                	Subscriber manager statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics>`
                
                

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
                    	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa>`
                    
                    .. attribute:: aggregate_summary
                    
                    	Aggregate summary of statistics
                    	**type**\:   :py:class:`AggregateSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary>`
                    
                    .. attribute:: srg
                    
                    	Geo Redundancy statistics
                    	**type**\:   :py:class:`Srg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Srg>`
                    
                    

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
                        
                        .. attribute:: accounting
                        
                        	Accounting statistics
                        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting>`
                        
                        .. attribute:: accounting_stats_all
                        
                        	Display all subscriber management statistics
                        	**type**\:   :py:class:`AccountingStatsAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll>`
                        
                        .. attribute:: aggregate_accounting
                        
                        	Aggregate accounting statistics
                        	**type**\:   :py:class:`AggregateAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting>`
                        
                        .. attribute:: aggregate_accounting_stats_all
                        
                        	Display all subscriber management total statistics
                        	**type**\:   :py:class:`AggregateAccountingStatsAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll>`
                        
                        .. attribute:: aggregate_authentication
                        
                        	Aggregate authentication statistics
                        	**type**\:   :py:class:`AggregateAuthentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication>`
                        
                        .. attribute:: aggregate_authorization
                        
                        	Aggregate authorization statistics
                        	**type**\:   :py:class:`AggregateAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization>`
                        
                        .. attribute:: aggregate_change_of_authorization
                        
                        	Aggregate change of authorization (COA) statistics
                        	**type**\:   :py:class:`AggregateChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization>`
                        
                        .. attribute:: aggregate_mobility
                        
                        	Aggregate mobility statistics
                        	**type**\:   :py:class:`AggregateMobility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility>`
                        
                        .. attribute:: authentication
                        
                        	Authentication statistics
                        	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication>`
                        
                        .. attribute:: authorization
                        
                        	Authorization statistics
                        	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization>`
                        
                        .. attribute:: change_of_authorization
                        
                        	Change of authorization (COA) statistics
                        	**type**\:   :py:class:`ChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization>`
                        
                        .. attribute:: mobility
                        
                        	Mobility statistics
                        	**type**\:   :py:class:`Mobility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Manager.Nodes.Node.Statistics.Aaa, self).__init__()

                            self.yang_name = "aaa"
                            self.yang_parent_name = "statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"accounting" : ("accounting", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting), "accounting-stats-all" : ("accounting_stats_all", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll), "aggregate-accounting" : ("aggregate_accounting", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting), "aggregate-accounting-stats-all" : ("aggregate_accounting_stats_all", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll), "aggregate-authentication" : ("aggregate_authentication", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication), "aggregate-authorization" : ("aggregate_authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization), "aggregate-change-of-authorization" : ("aggregate_change_of_authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization), "aggregate-mobility" : ("aggregate_mobility", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility), "authentication" : ("authentication", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication), "authorization" : ("authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization), "change-of-authorization" : ("change_of_authorization", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization), "mobility" : ("mobility", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility)}
                            self._child_list_classes = {}

                            self.accounting = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                            self._children_yang_names.add("accounting")

                            self.accounting_stats_all = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll()
                            self.accounting_stats_all.parent = self
                            self._children_name_map["accounting_stats_all"] = "accounting-stats-all"
                            self._children_yang_names.add("accounting-stats-all")

                            self.aggregate_accounting = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting()
                            self.aggregate_accounting.parent = self
                            self._children_name_map["aggregate_accounting"] = "aggregate-accounting"
                            self._children_yang_names.add("aggregate-accounting")

                            self.aggregate_accounting_stats_all = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll()
                            self.aggregate_accounting_stats_all.parent = self
                            self._children_name_map["aggregate_accounting_stats_all"] = "aggregate-accounting-stats-all"
                            self._children_yang_names.add("aggregate-accounting-stats-all")

                            self.aggregate_authentication = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication()
                            self.aggregate_authentication.parent = self
                            self._children_name_map["aggregate_authentication"] = "aggregate-authentication"
                            self._children_yang_names.add("aggregate-authentication")

                            self.aggregate_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization()
                            self.aggregate_authorization.parent = self
                            self._children_name_map["aggregate_authorization"] = "aggregate-authorization"
                            self._children_yang_names.add("aggregate-authorization")

                            self.aggregate_change_of_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization()
                            self.aggregate_change_of_authorization.parent = self
                            self._children_name_map["aggregate_change_of_authorization"] = "aggregate-change-of-authorization"
                            self._children_yang_names.add("aggregate-change-of-authorization")

                            self.aggregate_mobility = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility()
                            self.aggregate_mobility.parent = self
                            self._children_name_map["aggregate_mobility"] = "aggregate-mobility"
                            self._children_yang_names.add("aggregate-mobility")

                            self.authentication = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"
                            self._children_yang_names.add("authentication")

                            self.authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization()
                            self.authorization.parent = self
                            self._children_name_map["authorization"] = "authorization"
                            self._children_yang_names.add("authorization")

                            self.change_of_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization()
                            self.change_of_authorization.parent = self
                            self._children_name_map["change_of_authorization"] = "change-of-authorization"
                            self._children_yang_names.add("change-of-authorization")

                            self.mobility = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility()
                            self.mobility.parent = self
                            self._children_name_map["mobility"] = "mobility"
                            self._children_yang_names.add("mobility")
                            self._segment_path = lambda: "aaa"


                        class Accounting(Entity):
                            """
                            Accounting statistics
                            
                            .. attribute:: active_sessions
                            
                            	Active sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interim
                            
                            	Interim statistics
                            	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim>`
                            
                            .. attribute:: interim_inflight
                            
                            	Interim inflight details
                            	**type**\:   :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight>`
                            
                            .. attribute:: pass_through
                            
                            	Pass\-through statistics
                            	**type**\:   :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough>`
                            
                            .. attribute:: policy_plane_errored_requests
                            
                            	Policy plane errored requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_unknown_requests
                            
                            	Policy plane unknown requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: start
                            
                            	Start statistics
                            	**type**\:   :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start>`
                            
                            .. attribute:: started_sessions
                            
                            	Started sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop
                            
                            	Stop statistics
                            	**type**\:   :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop>`
                            
                            .. attribute:: stopped_sessions
                            
                            	Stopped sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: update
                            
                            	Update statistics
                            	**type**\:   :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting, self).__init__()

                                self.yang_name = "accounting"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough), "start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update)}
                                self._child_list_classes = {}

                                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim()
                                self.interim.parent = self
                                self._children_name_map["interim"] = "interim"
                                self._children_yang_names.add("interim")

                                self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight()
                                self.interim_inflight.parent = self
                                self._children_name_map["interim_inflight"] = "interim-inflight"
                                self._children_yang_names.add("interim-inflight")

                                self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough()
                                self.pass_through.parent = self
                                self._children_name_map["pass_through"] = "pass-through"
                                self._children_yang_names.add("pass-through")

                                self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start()
                                self.start.parent = self
                                self._children_name_map["start"] = "start"
                                self._children_yang_names.add("start")

                                self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop()
                                self.stop.parent = self
                                self._children_name_map["stop"] = "stop"
                                self._children_yang_names.add("stop")

                                self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update()
                                self.update.parent = self
                                self._children_name_map["update"] = "update"
                                self._children_yang_names.add("update")
                                self._segment_path = lambda: "accounting"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting, ['active_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests', 'started_sessions', 'stopped_sessions'], name, value)


                            class Interim(Entity):
                                """
                                Interim statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "interim"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class InterimInflight(Entity):
                                """
                                Interim inflight details
                                
                                .. attribute:: accepted_requests
                                
                                	Accepted requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: denied_requests
                                
                                	Denied requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_water_mark_quota_of_requests
                                
                                	Low water mark quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: quota_exhausts
                                
                                	Quota exhausts
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: remaining_quota_of_requests
                                
                                	Remaining quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: total_quota_of_requests
                                
                                	Total quota of requests
                                	**type**\:  int
                                
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

                                    self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                    self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                    self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")

                                    self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                    self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                    self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")
                                    self._segment_path = lambda: "interim-inflight"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight, ['accepted_requests', 'denied_requests', 'low_water_mark_quota_of_requests', 'quota_exhausts', 'remaining_quota_of_requests', 'total_quota_of_requests'], name, value)


                            class PassThrough(Entity):
                                """
                                Pass\-through statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "pass-through"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class Start(Entity):
                                """
                                Start statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "start"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class Stop(Entity):
                                """
                                Stop statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "stop"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class Update(Entity):
                                """
                                Update statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                        class AccountingStatsAll(Entity):
                            """
                            Display all subscriber management
                            statistics
                            
                            .. attribute:: accounting_statistics
                            
                            	List of stats for accounting
                            	**type**\:   :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics>`
                            
                            .. attribute:: authentication_statistics
                            
                            	List of stats for authentication
                            	**type**\:   :py:class:`AuthenticationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics>`
                            
                            .. attribute:: authorization_statistics
                            
                            	List of stats for authorization
                            	**type**\:   :py:class:`AuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics>`
                            
                            .. attribute:: change_of_authorization_statistics
                            
                            	List of stats for COA
                            	**type**\:   :py:class:`ChangeOfAuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics>`
                            
                            .. attribute:: mobility_statistics
                            
                            	List of stats for Mobility
                            	**type**\:   :py:class:`MobilityStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics>`
                            
                            

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
                                
                                .. attribute:: active_sessions
                                
                                	Active sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interim
                                
                                	Interim statistics
                                	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim>`
                                
                                .. attribute:: interim_inflight
                                
                                	Interim inflight details
                                	**type**\:   :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight>`
                                
                                .. attribute:: pass_through
                                
                                	Pass\-through statistics
                                	**type**\:   :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough>`
                                
                                .. attribute:: policy_plane_errored_requests
                                
                                	Policy plane errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: policy_plane_unknown_requests
                                
                                	Policy plane unknown requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: start
                                
                                	Start statistics
                                	**type**\:   :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start>`
                                
                                .. attribute:: started_sessions
                                
                                	Started sessions
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: stop
                                
                                	Stop statistics
                                	**type**\:   :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop>`
                                
                                .. attribute:: stopped_sessions
                                
                                	Stopped sessions
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: update
                                
                                	Update statistics
                                	**type**\:   :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update>`
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics, self).__init__()

                                    self.yang_name = "accounting-statistics"
                                    self.yang_parent_name = "accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough), "start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update)}
                                    self._child_list_classes = {}

                                    self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                    self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                    self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                    self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                    self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                    self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim()
                                    self.interim.parent = self
                                    self._children_name_map["interim"] = "interim"
                                    self._children_yang_names.add("interim")

                                    self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight()
                                    self.interim_inflight.parent = self
                                    self._children_name_map["interim_inflight"] = "interim-inflight"
                                    self._children_yang_names.add("interim-inflight")

                                    self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough()
                                    self.pass_through.parent = self
                                    self._children_name_map["pass_through"] = "pass-through"
                                    self._children_yang_names.add("pass-through")

                                    self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start()
                                    self.start.parent = self
                                    self._children_name_map["start"] = "start"
                                    self._children_yang_names.add("start")

                                    self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop()
                                    self.stop.parent = self
                                    self._children_name_map["stop"] = "stop"
                                    self._children_yang_names.add("stop")

                                    self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update()
                                    self.update.parent = self
                                    self._children_name_map["update"] = "update"
                                    self._children_yang_names.add("update")
                                    self._segment_path = lambda: "accounting-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics, ['active_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests', 'started_sessions', 'stopped_sessions'], name, value)


                                class Interim(Entity):
                                    """
                                    Interim statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "interim"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Interim, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class InterimInflight(Entity):
                                    """
                                    Interim inflight details
                                    
                                    .. attribute:: accepted_requests
                                    
                                    	Accepted requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: denied_requests
                                    
                                    	Denied requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: low_water_mark_quota_of_requests
                                    
                                    	Low water mark quota of requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: quota_exhausts
                                    
                                    	Quota exhausts
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: remaining_quota_of_requests
                                    
                                    	Remaining quota of requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_quota_of_requests
                                    
                                    	Total quota of requests
                                    	**type**\:  int
                                    
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

                                        self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                        self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                        self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")

                                        self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                        self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                        self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")
                                        self._segment_path = lambda: "interim-inflight"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.InterimInflight, ['accepted_requests', 'denied_requests', 'low_water_mark_quota_of_requests', 'quota_exhausts', 'remaining_quota_of_requests', 'total_quota_of_requests'], name, value)


                                class PassThrough(Entity):
                                    """
                                    Pass\-through statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "pass-through"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.PassThrough, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class Start(Entity):
                                    """
                                    Start statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "start"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Start, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class Stop(Entity):
                                    """
                                    Stop statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "stop"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Stop, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class Update(Entity):
                                    """
                                    Update statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AccountingStatistics.Update, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class AuthenticationStatistics(Entity):
                                """
                                List of stats for authentication
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\:  int
                                
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

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                    self._segment_path = lambda: "authentication-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthenticationStatistics, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                            class AuthorizationStatistics(Entity):
                                """
                                List of stats for authorization
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\:  int
                                
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

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                    self._segment_path = lambda: "authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.AuthorizationStatistics, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                            class ChangeOfAuthorizationStatistics(Entity):
                                """
                                List of stats for COA
                                
                                .. attribute:: account_logoff
                                
                                	Account logoff request statistics
                                	**type**\:   :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff>`
                                
                                .. attribute:: account_logon
                                
                                	Account logon request statistics
                                	**type**\:   :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon>`
                                
                                .. attribute:: account_update
                                
                                	Account update request statistics
                                	**type**\:   :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate>`
                                
                                .. attribute:: attr_list_retrieve_failure_resps
                                
                                	Responses to attribute list failure errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: internal_err_resps
                                
                                	Responses to internal error
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_cmd_resps
                                
                                	Responses empty (no command) COA request
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_found_resps
                                
                                	Responses to COA with unknown session identifier
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_peer_resps
                                
                                	Responses to session peer not found error
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: resp_send_failure
                                
                                	Response send failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: service_multi
                                
                                	MA\-CoA Service request statistics
                                	**type**\:   :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti>`
                                
                                .. attribute:: service_profile_push_failure_resps
                                
                                	Responses to service profile push failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: session_disconnect
                                
                                	Session disconnect request statistics
                                	**type**\:   :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect>`
                                
                                .. attribute:: single_service_logoff
                                
                                	Single Service logoff request statistics
                                	**type**\:   :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff>`
                                
                                .. attribute:: single_service_logon
                                
                                	Service logon request statistics
                                	**type**\:   :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon>`
                                
                                .. attribute:: single_service_modify
                                
                                	Single Service Modify request statistics
                                	**type**\:   :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify>`
                                
                                .. attribute:: unknown_account_cmd_resps
                                
                                	Responses to unknown account command
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_cmd_resps
                                
                                	Responses to unknown command
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_service_cmd_resps
                                
                                	Responses to unknown service command
                                	**type**\:  int
                                
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
                                    self._child_container_classes = {"account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff), "account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify)}
                                    self._child_list_classes = {}

                                    self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                    self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                    self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                    self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                    self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                    self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                    self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                    self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                    self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                    self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                    self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff()
                                    self.account_logoff.parent = self
                                    self._children_name_map["account_logoff"] = "account-logoff"
                                    self._children_yang_names.add("account-logoff")

                                    self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon()
                                    self.account_logon.parent = self
                                    self._children_name_map["account_logon"] = "account-logon"
                                    self._children_yang_names.add("account-logon")

                                    self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate()
                                    self.account_update.parent = self
                                    self._children_name_map["account_update"] = "account-update"
                                    self._children_yang_names.add("account-update")

                                    self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti()
                                    self.service_multi.parent = self
                                    self._children_name_map["service_multi"] = "service-multi"
                                    self._children_yang_names.add("service-multi")

                                    self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect()
                                    self.session_disconnect.parent = self
                                    self._children_name_map["session_disconnect"] = "session-disconnect"
                                    self._children_yang_names.add("session-disconnect")

                                    self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff()
                                    self.single_service_logoff.parent = self
                                    self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                    self._children_yang_names.add("single-service-logoff")

                                    self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon()
                                    self.single_service_logon.parent = self
                                    self._children_name_map["single_service_logon"] = "single-service-logon"
                                    self._children_yang_names.add("single-service-logon")

                                    self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify()
                                    self.single_service_modify.parent = self
                                    self._children_name_map["single_service_modify"] = "single-service-modify"
                                    self._children_yang_names.add("single-service-modify")
                                    self._segment_path = lambda: "change-of-authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics, ['attr_list_retrieve_failure_resps', 'internal_err_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps', 'resp_send_failure', 'service_profile_push_failure_resps', 'unknown_account_cmd_resps', 'unknown_cmd_resps', 'unknown_service_cmd_resps'], name, value)


                                class AccountLogoff(Entity):
                                    """
                                    Account logoff request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "account-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class AccountLogon(Entity):
                                    """
                                    Account logon request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "account-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class AccountUpdate(Entity):
                                    """
                                    Account update request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "account-update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class ServiceMulti(Entity):
                                    """
                                    MA\-CoA Service request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "service-multi"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SessionDisconnect(Entity):
                                    """
                                    Session disconnect request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "session-disconnect"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SingleServiceLogoff(Entity):
                                    """
                                    Single Service logoff request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "single-service-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SingleServiceLogon(Entity):
                                    """
                                    Service logon request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "single-service-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SingleServiceModify(Entity):
                                    """
                                    Single Service Modify request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "single-service-modify"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class MobilityStatistics(Entity):
                                """
                                List of stats for Mobility
                                
                                .. attribute:: receive_response_failures
                                
                                	Response receive failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: receive_response_successes
                                
                                	Response receive success
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: send_request_failures
                                
                                	Request send failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: send_request_successes
                                
                                	Request send success
                                	**type**\:  int
                                
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

                                    self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")

                                    self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                    self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                    self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")
                                    self._segment_path = lambda: "mobility-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AccountingStatsAll.MobilityStatistics, ['receive_response_failures', 'receive_response_successes', 'send_request_failures', 'send_request_successes'], name, value)


                        class AggregateAccounting(Entity):
                            """
                            Aggregate accounting statistics
                            
                            .. attribute:: active_sessions
                            
                            	Active sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interim
                            
                            	Interim statistics
                            	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim>`
                            
                            .. attribute:: interim_inflight
                            
                            	Interim inflight details
                            	**type**\:   :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight>`
                            
                            .. attribute:: pass_through
                            
                            	Pass\-through statistics
                            	**type**\:   :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough>`
                            
                            .. attribute:: policy_plane_errored_requests
                            
                            	Policy plane errored requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_unknown_requests
                            
                            	Policy plane unknown requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: start
                            
                            	Start statistics
                            	**type**\:   :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start>`
                            
                            .. attribute:: started_sessions
                            
                            	Started sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop
                            
                            	Stop statistics
                            	**type**\:   :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop>`
                            
                            .. attribute:: stopped_sessions
                            
                            	Stopped sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: update
                            
                            	Update statistics
                            	**type**\:   :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting, self).__init__()

                                self.yang_name = "aggregate-accounting"
                                self.yang_parent_name = "aaa"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough), "start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update)}
                                self._child_list_classes = {}

                                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim()
                                self.interim.parent = self
                                self._children_name_map["interim"] = "interim"
                                self._children_yang_names.add("interim")

                                self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight()
                                self.interim_inflight.parent = self
                                self._children_name_map["interim_inflight"] = "interim-inflight"
                                self._children_yang_names.add("interim-inflight")

                                self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough()
                                self.pass_through.parent = self
                                self._children_name_map["pass_through"] = "pass-through"
                                self._children_yang_names.add("pass-through")

                                self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start()
                                self.start.parent = self
                                self._children_name_map["start"] = "start"
                                self._children_yang_names.add("start")

                                self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop()
                                self.stop.parent = self
                                self._children_name_map["stop"] = "stop"
                                self._children_yang_names.add("stop")

                                self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update()
                                self.update.parent = self
                                self._children_name_map["update"] = "update"
                                self._children_yang_names.add("update")
                                self._segment_path = lambda: "aggregate-accounting"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting, ['active_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests', 'started_sessions', 'stopped_sessions'], name, value)


                            class Interim(Entity):
                                """
                                Interim statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "interim"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class InterimInflight(Entity):
                                """
                                Interim inflight details
                                
                                .. attribute:: accepted_requests
                                
                                	Accepted requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: denied_requests
                                
                                	Denied requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_water_mark_quota_of_requests
                                
                                	Low water mark quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: quota_exhausts
                                
                                	Quota exhausts
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: remaining_quota_of_requests
                                
                                	Remaining quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: total_quota_of_requests
                                
                                	Total quota of requests
                                	**type**\:  int
                                
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

                                    self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                    self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                    self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")

                                    self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                    self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                    self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")
                                    self._segment_path = lambda: "interim-inflight"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight, ['accepted_requests', 'denied_requests', 'low_water_mark_quota_of_requests', 'quota_exhausts', 'remaining_quota_of_requests', 'total_quota_of_requests'], name, value)


                            class PassThrough(Entity):
                                """
                                Pass\-through statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "pass-through"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class Start(Entity):
                                """
                                Start statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "start"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class Stop(Entity):
                                """
                                Stop statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "stop"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class Update(Entity):
                                """
                                Update statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                    self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                    self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                    self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                        class AggregateAccountingStatsAll(Entity):
                            """
                            Display all subscriber management total
                            statistics
                            
                            .. attribute:: accounting_statistics
                            
                            	List of stats for accounting
                            	**type**\:   :py:class:`AccountingStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics>`
                            
                            .. attribute:: authentication_statistics
                            
                            	List of stats for authentication
                            	**type**\:   :py:class:`AuthenticationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics>`
                            
                            .. attribute:: authorization_statistics
                            
                            	List of stats for authorization
                            	**type**\:   :py:class:`AuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics>`
                            
                            .. attribute:: change_of_authorization_statistics
                            
                            	List of stats for COA
                            	**type**\:   :py:class:`ChangeOfAuthorizationStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics>`
                            
                            .. attribute:: mobility_statistics
                            
                            	List of stats for Mobility
                            	**type**\:   :py:class:`MobilityStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics>`
                            
                            

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
                                
                                .. attribute:: active_sessions
                                
                                	Active sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interim
                                
                                	Interim statistics
                                	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim>`
                                
                                .. attribute:: interim_inflight
                                
                                	Interim inflight details
                                	**type**\:   :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight>`
                                
                                .. attribute:: pass_through
                                
                                	Pass\-through statistics
                                	**type**\:   :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough>`
                                
                                .. attribute:: policy_plane_errored_requests
                                
                                	Policy plane errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: policy_plane_unknown_requests
                                
                                	Policy plane unknown requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: start
                                
                                	Start statistics
                                	**type**\:   :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start>`
                                
                                .. attribute:: started_sessions
                                
                                	Started sessions
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: stop
                                
                                	Stop statistics
                                	**type**\:   :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop>`
                                
                                .. attribute:: stopped_sessions
                                
                                	Stopped sessions
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: update
                                
                                	Update statistics
                                	**type**\:   :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update>`
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics, self).__init__()

                                    self.yang_name = "accounting-statistics"
                                    self.yang_parent_name = "aggregate-accounting-stats-all"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"interim" : ("interim", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim), "interim-inflight" : ("interim_inflight", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight), "pass-through" : ("pass_through", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough), "start" : ("start", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start), "stop" : ("stop", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop), "update" : ("update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update)}
                                    self._child_list_classes = {}

                                    self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                                    self.policy_plane_errored_requests = YLeaf(YType.uint64, "policy-plane-errored-requests")

                                    self.policy_plane_unknown_requests = YLeaf(YType.uint64, "policy-plane-unknown-requests")

                                    self.started_sessions = YLeaf(YType.uint64, "started-sessions")

                                    self.stopped_sessions = YLeaf(YType.uint64, "stopped-sessions")

                                    self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim()
                                    self.interim.parent = self
                                    self._children_name_map["interim"] = "interim"
                                    self._children_yang_names.add("interim")

                                    self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight()
                                    self.interim_inflight.parent = self
                                    self._children_name_map["interim_inflight"] = "interim-inflight"
                                    self._children_yang_names.add("interim-inflight")

                                    self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough()
                                    self.pass_through.parent = self
                                    self._children_name_map["pass_through"] = "pass-through"
                                    self._children_yang_names.add("pass-through")

                                    self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start()
                                    self.start.parent = self
                                    self._children_name_map["start"] = "start"
                                    self._children_yang_names.add("start")

                                    self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop()
                                    self.stop.parent = self
                                    self._children_name_map["stop"] = "stop"
                                    self._children_yang_names.add("stop")

                                    self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update()
                                    self.update.parent = self
                                    self._children_name_map["update"] = "update"
                                    self._children_yang_names.add("update")
                                    self._segment_path = lambda: "accounting-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics, ['active_sessions', 'policy_plane_errored_requests', 'policy_plane_unknown_requests', 'started_sessions', 'stopped_sessions'], name, value)


                                class Interim(Entity):
                                    """
                                    Interim statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "interim"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Interim, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class InterimInflight(Entity):
                                    """
                                    Interim inflight details
                                    
                                    .. attribute:: accepted_requests
                                    
                                    	Accepted requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: denied_requests
                                    
                                    	Denied requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: low_water_mark_quota_of_requests
                                    
                                    	Low water mark quota of requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: quota_exhausts
                                    
                                    	Quota exhausts
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: remaining_quota_of_requests
                                    
                                    	Remaining quota of requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: total_quota_of_requests
                                    
                                    	Total quota of requests
                                    	**type**\:  int
                                    
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

                                        self.accepted_requests = YLeaf(YType.uint32, "accepted-requests")

                                        self.denied_requests = YLeaf(YType.uint32, "denied-requests")

                                        self.low_water_mark_quota_of_requests = YLeaf(YType.uint32, "low-water-mark-quota-of-requests")

                                        self.quota_exhausts = YLeaf(YType.uint32, "quota-exhausts")

                                        self.remaining_quota_of_requests = YLeaf(YType.uint32, "remaining-quota-of-requests")

                                        self.total_quota_of_requests = YLeaf(YType.uint32, "total-quota-of-requests")
                                        self._segment_path = lambda: "interim-inflight"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.InterimInflight, ['accepted_requests', 'denied_requests', 'low_water_mark_quota_of_requests', 'quota_exhausts', 'remaining_quota_of_requests', 'total_quota_of_requests'], name, value)


                                class PassThrough(Entity):
                                    """
                                    Pass\-through statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "pass-through"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.PassThrough, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class Start(Entity):
                                    """
                                    Start statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "start"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Start, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class Stop(Entity):
                                    """
                                    Stop statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "stop"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Stop, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                                class Update(Entity):
                                    """
                                    Update statistics
                                    
                                    .. attribute:: aaa_errored_requests
                                    
                                    	AAA errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_failed_responses
                                    
                                    	AAA failed responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_sent_requests
                                    
                                    	AAA requests sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: aaa_succeeded_responses
                                    
                                    	AAA succeeded responses
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: errored_requests
                                    
                                    	Errored requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.aaa_errored_requests = YLeaf(YType.uint64, "aaa-errored-requests")

                                        self.aaa_failed_responses = YLeaf(YType.uint64, "aaa-failed-responses")

                                        self.aaa_sent_requests = YLeaf(YType.uint64, "aaa-sent-requests")

                                        self.aaa_succeeded_responses = YLeaf(YType.uint64, "aaa-succeeded-responses")

                                        self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AccountingStatistics.Update, ['aaa_errored_requests', 'aaa_failed_responses', 'aaa_sent_requests', 'aaa_succeeded_responses', 'errored_requests', 'received_requests'], name, value)


                            class AuthenticationStatistics(Entity):
                                """
                                List of stats for authentication
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\:  int
                                
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

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                    self._segment_path = lambda: "authentication-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthenticationStatistics, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                            class AuthorizationStatistics(Entity):
                                """
                                List of stats for authorization
                                
                                .. attribute:: accepted_requests
                                
                                	Request accepted by Radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Unexpected errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: incomplete_requests
                                
                                	Incomplete requests \- missing attributes
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: rejected_requests
                                
                                	Requests rejected by radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: sent_requests
                                
                                	Requests sent to radius server
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: successful_requests
                                
                                	Requests which are successful
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: terminated_requests
                                
                                	Requests terminated by disconnect
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unreachable_requests
                                
                                	Radius server not available
                                	**type**\:  int
                                
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

                                    self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                    self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                    self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                    self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                    self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                    self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                    self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                    self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                    self._segment_path = lambda: "authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.AuthorizationStatistics, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                            class ChangeOfAuthorizationStatistics(Entity):
                                """
                                List of stats for COA
                                
                                .. attribute:: account_logoff
                                
                                	Account logoff request statistics
                                	**type**\:   :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff>`
                                
                                .. attribute:: account_logon
                                
                                	Account logon request statistics
                                	**type**\:   :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon>`
                                
                                .. attribute:: account_update
                                
                                	Account update request statistics
                                	**type**\:   :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate>`
                                
                                .. attribute:: attr_list_retrieve_failure_resps
                                
                                	Responses to attribute list failure errors
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: internal_err_resps
                                
                                	Responses to internal error
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_cmd_resps
                                
                                	Responses empty (no command) COA request
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_found_resps
                                
                                	Responses to COA with unknown session identifier
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: no_session_peer_resps
                                
                                	Responses to session peer not found error
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: resp_send_failure
                                
                                	Response send failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: service_multi
                                
                                	MA\-CoA Service request statistics
                                	**type**\:   :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti>`
                                
                                .. attribute:: service_profile_push_failure_resps
                                
                                	Responses to service profile push failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: session_disconnect
                                
                                	Session disconnect request statistics
                                	**type**\:   :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect>`
                                
                                .. attribute:: single_service_logoff
                                
                                	Single Service logoff request statistics
                                	**type**\:   :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff>`
                                
                                .. attribute:: single_service_logon
                                
                                	Service logon request statistics
                                	**type**\:   :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon>`
                                
                                .. attribute:: single_service_modify
                                
                                	Single Service Modify request statistics
                                	**type**\:   :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify>`
                                
                                .. attribute:: unknown_account_cmd_resps
                                
                                	Responses to unknown account command
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_cmd_resps
                                
                                	Responses to unknown command
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: unknown_service_cmd_resps
                                
                                	Responses to unknown service command
                                	**type**\:  int
                                
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
                                    self._child_container_classes = {"account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff), "account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify)}
                                    self._child_list_classes = {}

                                    self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                    self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                    self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                    self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                    self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                    self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                    self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                    self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                    self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                    self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                    self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff()
                                    self.account_logoff.parent = self
                                    self._children_name_map["account_logoff"] = "account-logoff"
                                    self._children_yang_names.add("account-logoff")

                                    self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon()
                                    self.account_logon.parent = self
                                    self._children_name_map["account_logon"] = "account-logon"
                                    self._children_yang_names.add("account-logon")

                                    self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate()
                                    self.account_update.parent = self
                                    self._children_name_map["account_update"] = "account-update"
                                    self._children_yang_names.add("account-update")

                                    self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti()
                                    self.service_multi.parent = self
                                    self._children_name_map["service_multi"] = "service-multi"
                                    self._children_yang_names.add("service-multi")

                                    self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect()
                                    self.session_disconnect.parent = self
                                    self._children_name_map["session_disconnect"] = "session-disconnect"
                                    self._children_yang_names.add("session-disconnect")

                                    self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff()
                                    self.single_service_logoff.parent = self
                                    self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                    self._children_yang_names.add("single-service-logoff")

                                    self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon()
                                    self.single_service_logon.parent = self
                                    self._children_name_map["single_service_logon"] = "single-service-logon"
                                    self._children_yang_names.add("single-service-logon")

                                    self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify()
                                    self.single_service_modify.parent = self
                                    self._children_name_map["single_service_modify"] = "single-service-modify"
                                    self._children_yang_names.add("single-service-modify")
                                    self._segment_path = lambda: "change-of-authorization-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics, ['attr_list_retrieve_failure_resps', 'internal_err_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps', 'resp_send_failure', 'service_profile_push_failure_resps', 'unknown_account_cmd_resps', 'unknown_cmd_resps', 'unknown_service_cmd_resps'], name, value)


                                class AccountLogoff(Entity):
                                    """
                                    Account logoff request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "account-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class AccountLogon(Entity):
                                    """
                                    Account logon request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "account-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class AccountUpdate(Entity):
                                    """
                                    Account update request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "account-update"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.AccountUpdate, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class ServiceMulti(Entity):
                                    """
                                    MA\-CoA Service request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "service-multi"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.ServiceMulti, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SessionDisconnect(Entity):
                                    """
                                    Session disconnect request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "session-disconnect"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SessionDisconnect, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SingleServiceLogoff(Entity):
                                    """
                                    Single Service logoff request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "single-service-logoff"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SingleServiceLogon(Entity):
                                    """
                                    Service logon request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "single-service-logon"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                                class SingleServiceModify(Entity):
                                    """
                                    Single Service Modify request statistics
                                    
                                    .. attribute:: acknowledged_requests
                                    
                                    	Acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: non_acknowledged_requests
                                    
                                    	Non acknowledged requests
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_requests
                                    
                                    	Received requests
                                    	**type**\:  int
                                    
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

                                        self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                        self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                        self.received_requests = YLeaf(YType.uint64, "received-requests")
                                        self._segment_path = lambda: "single-service-modify"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.ChangeOfAuthorizationStatistics.SingleServiceModify, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class MobilityStatistics(Entity):
                                """
                                List of stats for Mobility
                                
                                .. attribute:: receive_response_failures
                                
                                	Response receive failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: receive_response_successes
                                
                                	Response receive success
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: send_request_failures
                                
                                	Request send failures
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: send_request_successes
                                
                                	Request send success
                                	**type**\:  int
                                
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

                                    self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")

                                    self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                    self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                    self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")
                                    self._segment_path = lambda: "mobility-statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccountingStatsAll.MobilityStatistics, ['receive_response_failures', 'receive_response_successes', 'send_request_failures', 'send_request_successes'], name, value)


                        class AggregateAuthentication(Entity):
                            """
                            Aggregate authentication statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
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

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                self._segment_path = lambda: "aggregate-authentication"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                        class AggregateAuthorization(Entity):
                            """
                            Aggregate authorization statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
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

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                self._segment_path = lambda: "aggregate-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                        class AggregateChangeOfAuthorization(Entity):
                            """
                            Aggregate change of authorization (COA)
                            statistics
                            
                            .. attribute:: account_logoff
                            
                            	Account logoff request statistics
                            	**type**\:   :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff>`
                            
                            .. attribute:: account_logon
                            
                            	Account logon request statistics
                            	**type**\:   :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon>`
                            
                            .. attribute:: account_update
                            
                            	Account update request statistics
                            	**type**\:   :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate>`
                            
                            .. attribute:: attr_list_retrieve_failure_resps
                            
                            	Responses to attribute list failure errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: internal_err_resps
                            
                            	Responses to internal error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_cmd_resps
                            
                            	Responses empty (no command) COA request
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_found_resps
                            
                            	Responses to COA with unknown session identifier
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_peer_resps
                            
                            	Responses to session peer not found error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: resp_send_failure
                            
                            	Response send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_multi
                            
                            	MA\-CoA Service request statistics
                            	**type**\:   :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti>`
                            
                            .. attribute:: service_profile_push_failure_resps
                            
                            	Responses to service profile push failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: session_disconnect
                            
                            	Session disconnect request statistics
                            	**type**\:   :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect>`
                            
                            .. attribute:: single_service_logoff
                            
                            	Single Service logoff request statistics
                            	**type**\:   :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff>`
                            
                            .. attribute:: single_service_logon
                            
                            	Service logon request statistics
                            	**type**\:   :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon>`
                            
                            .. attribute:: single_service_modify
                            
                            	Single Service Modify request statistics
                            	**type**\:   :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify>`
                            
                            .. attribute:: unknown_account_cmd_resps
                            
                            	Responses to unknown account command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_cmd_resps
                            
                            	Responses to unknown command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_service_cmd_resps
                            
                            	Responses to unknown service command
                            	**type**\:  int
                            
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
                                self._child_container_classes = {"account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff), "account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify)}
                                self._child_list_classes = {}

                                self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff()
                                self.account_logoff.parent = self
                                self._children_name_map["account_logoff"] = "account-logoff"
                                self._children_yang_names.add("account-logoff")

                                self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon()
                                self.account_logon.parent = self
                                self._children_name_map["account_logon"] = "account-logon"
                                self._children_yang_names.add("account-logon")

                                self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate()
                                self.account_update.parent = self
                                self._children_name_map["account_update"] = "account-update"
                                self._children_yang_names.add("account-update")

                                self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti()
                                self.service_multi.parent = self
                                self._children_name_map["service_multi"] = "service-multi"
                                self._children_yang_names.add("service-multi")

                                self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect()
                                self.session_disconnect.parent = self
                                self._children_name_map["session_disconnect"] = "session-disconnect"
                                self._children_yang_names.add("session-disconnect")

                                self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff()
                                self.single_service_logoff.parent = self
                                self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                self._children_yang_names.add("single-service-logoff")

                                self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon()
                                self.single_service_logon.parent = self
                                self._children_name_map["single_service_logon"] = "single-service-logon"
                                self._children_yang_names.add("single-service-logon")

                                self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify()
                                self.single_service_modify.parent = self
                                self._children_name_map["single_service_modify"] = "single-service-modify"
                                self._children_yang_names.add("single-service-modify")
                                self._segment_path = lambda: "aggregate-change-of-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization, ['attr_list_retrieve_failure_resps', 'internal_err_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps', 'resp_send_failure', 'service_profile_push_failure_resps', 'unknown_account_cmd_resps', 'unknown_cmd_resps', 'unknown_service_cmd_resps'], name, value)


                            class AccountLogoff(Entity):
                                """
                                Account logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "account-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class AccountLogon(Entity):
                                """
                                Account logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "account-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class AccountUpdate(Entity):
                                """
                                Account update request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "account-update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class ServiceMulti(Entity):
                                """
                                MA\-CoA Service request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "service-multi"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SessionDisconnect(Entity):
                                """
                                Session disconnect request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "session-disconnect"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SingleServiceLogoff(Entity):
                                """
                                Single Service logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "single-service-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SingleServiceLogon(Entity):
                                """
                                Service logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "single-service-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SingleServiceModify(Entity):
                                """
                                Single Service Modify request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "single-service-modify"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                        class AggregateMobility(Entity):
                            """
                            Aggregate mobility statistics
                            
                            .. attribute:: receive_response_failures
                            
                            	Response receive failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_successes
                            
                            	Response receive success
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_failures
                            
                            	Request send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_successes
                            
                            	Request send success
                            	**type**\:  int
                            
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

                                self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")

                                self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")
                                self._segment_path = lambda: "aggregate-mobility"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility, ['receive_response_failures', 'receive_response_successes', 'send_request_failures', 'send_request_successes'], name, value)


                        class Authentication(Entity):
                            """
                            Authentication statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
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

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                self._segment_path = lambda: "authentication"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                        class Authorization(Entity):
                            """
                            Authorization statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
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

                                self.accepted_requests = YLeaf(YType.uint64, "accepted-requests")

                                self.errored_requests = YLeaf(YType.uint64, "errored-requests")

                                self.incomplete_requests = YLeaf(YType.uint64, "incomplete-requests")

                                self.rejected_requests = YLeaf(YType.uint64, "rejected-requests")

                                self.sent_requests = YLeaf(YType.uint64, "sent-requests")

                                self.successful_requests = YLeaf(YType.uint64, "successful-requests")

                                self.terminated_requests = YLeaf(YType.uint64, "terminated-requests")

                                self.unreachable_requests = YLeaf(YType.uint64, "unreachable-requests")
                                self._segment_path = lambda: "authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization, ['accepted_requests', 'errored_requests', 'incomplete_requests', 'rejected_requests', 'sent_requests', 'successful_requests', 'terminated_requests', 'unreachable_requests'], name, value)


                        class ChangeOfAuthorization(Entity):
                            """
                            Change of authorization (COA) statistics
                            
                            .. attribute:: account_logoff
                            
                            	Account logoff request statistics
                            	**type**\:   :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff>`
                            
                            .. attribute:: account_logon
                            
                            	Account logon request statistics
                            	**type**\:   :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon>`
                            
                            .. attribute:: account_update
                            
                            	Account update request statistics
                            	**type**\:   :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate>`
                            
                            .. attribute:: attr_list_retrieve_failure_resps
                            
                            	Responses to attribute list failure errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: internal_err_resps
                            
                            	Responses to internal error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_cmd_resps
                            
                            	Responses empty (no command) COA request
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_found_resps
                            
                            	Responses to COA with unknown session identifier
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_peer_resps
                            
                            	Responses to session peer not found error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: resp_send_failure
                            
                            	Response send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_multi
                            
                            	MA\-CoA Service request statistics
                            	**type**\:   :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti>`
                            
                            .. attribute:: service_profile_push_failure_resps
                            
                            	Responses to service profile push failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: session_disconnect
                            
                            	Session disconnect request statistics
                            	**type**\:   :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect>`
                            
                            .. attribute:: single_service_logoff
                            
                            	Single Service logoff request statistics
                            	**type**\:   :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff>`
                            
                            .. attribute:: single_service_logon
                            
                            	Service logon request statistics
                            	**type**\:   :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon>`
                            
                            .. attribute:: single_service_modify
                            
                            	Single Service Modify request statistics
                            	**type**\:   :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify>`
                            
                            .. attribute:: unknown_account_cmd_resps
                            
                            	Responses to unknown account command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_cmd_resps
                            
                            	Responses to unknown command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_service_cmd_resps
                            
                            	Responses to unknown service command
                            	**type**\:  int
                            
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
                                self._child_container_classes = {"account-logoff" : ("account_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff), "account-logon" : ("account_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon), "account-update" : ("account_update", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate), "service-multi" : ("service_multi", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti), "session-disconnect" : ("session_disconnect", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect), "single-service-logoff" : ("single_service_logoff", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff), "single-service-logon" : ("single_service_logon", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon), "single-service-modify" : ("single_service_modify", Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify)}
                                self._child_list_classes = {}

                                self.attr_list_retrieve_failure_resps = YLeaf(YType.uint64, "attr-list-retrieve-failure-resps")

                                self.internal_err_resps = YLeaf(YType.uint64, "internal-err-resps")

                                self.no_cmd_resps = YLeaf(YType.uint64, "no-cmd-resps")

                                self.no_session_found_resps = YLeaf(YType.uint64, "no-session-found-resps")

                                self.no_session_peer_resps = YLeaf(YType.uint64, "no-session-peer-resps")

                                self.resp_send_failure = YLeaf(YType.uint64, "resp-send-failure")

                                self.service_profile_push_failure_resps = YLeaf(YType.uint64, "service-profile-push-failure-resps")

                                self.unknown_account_cmd_resps = YLeaf(YType.uint64, "unknown-account-cmd-resps")

                                self.unknown_cmd_resps = YLeaf(YType.uint64, "unknown-cmd-resps")

                                self.unknown_service_cmd_resps = YLeaf(YType.uint64, "unknown-service-cmd-resps")

                                self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff()
                                self.account_logoff.parent = self
                                self._children_name_map["account_logoff"] = "account-logoff"
                                self._children_yang_names.add("account-logoff")

                                self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon()
                                self.account_logon.parent = self
                                self._children_name_map["account_logon"] = "account-logon"
                                self._children_yang_names.add("account-logon")

                                self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate()
                                self.account_update.parent = self
                                self._children_name_map["account_update"] = "account-update"
                                self._children_yang_names.add("account-update")

                                self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti()
                                self.service_multi.parent = self
                                self._children_name_map["service_multi"] = "service-multi"
                                self._children_yang_names.add("service-multi")

                                self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect()
                                self.session_disconnect.parent = self
                                self._children_name_map["session_disconnect"] = "session-disconnect"
                                self._children_yang_names.add("session-disconnect")

                                self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff()
                                self.single_service_logoff.parent = self
                                self._children_name_map["single_service_logoff"] = "single-service-logoff"
                                self._children_yang_names.add("single-service-logoff")

                                self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon()
                                self.single_service_logon.parent = self
                                self._children_name_map["single_service_logon"] = "single-service-logon"
                                self._children_yang_names.add("single-service-logon")

                                self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify()
                                self.single_service_modify.parent = self
                                self._children_name_map["single_service_modify"] = "single-service-modify"
                                self._children_yang_names.add("single-service-modify")
                                self._segment_path = lambda: "change-of-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization, ['attr_list_retrieve_failure_resps', 'internal_err_resps', 'no_cmd_resps', 'no_session_found_resps', 'no_session_peer_resps', 'resp_send_failure', 'service_profile_push_failure_resps', 'unknown_account_cmd_resps', 'unknown_cmd_resps', 'unknown_service_cmd_resps'], name, value)


                            class AccountLogoff(Entity):
                                """
                                Account logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "account-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class AccountLogon(Entity):
                                """
                                Account logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "account-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class AccountUpdate(Entity):
                                """
                                Account update request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "account-update"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class ServiceMulti(Entity):
                                """
                                MA\-CoA Service request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "service-multi"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SessionDisconnect(Entity):
                                """
                                Session disconnect request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "session-disconnect"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SingleServiceLogoff(Entity):
                                """
                                Single Service logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "single-service-logoff"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SingleServiceLogon(Entity):
                                """
                                Service logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "single-service-logon"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                            class SingleServiceModify(Entity):
                                """
                                Single Service Modify request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
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

                                    self.acknowledged_requests = YLeaf(YType.uint64, "acknowledged-requests")

                                    self.non_acknowledged_requests = YLeaf(YType.uint64, "non-acknowledged-requests")

                                    self.received_requests = YLeaf(YType.uint64, "received-requests")
                                    self._segment_path = lambda: "single-service-modify"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify, ['acknowledged_requests', 'non_acknowledged_requests', 'received_requests'], name, value)


                        class Mobility(Entity):
                            """
                            Mobility statistics
                            
                            .. attribute:: receive_response_failures
                            
                            	Response receive failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_successes
                            
                            	Response receive success
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_failures
                            
                            	Request send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_successes
                            
                            	Request send success
                            	**type**\:  int
                            
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

                                self.receive_response_failures = YLeaf(YType.uint64, "receive-response-failures")

                                self.receive_response_successes = YLeaf(YType.uint64, "receive-response-successes")

                                self.send_request_failures = YLeaf(YType.uint64, "send-request-failures")

                                self.send_request_successes = YLeaf(YType.uint64, "send-request-successes")
                                self._segment_path = lambda: "mobility"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility, ['receive_response_failures', 'receive_response_successes', 'send_request_failures', 'send_request_successes'], name, value)


                    class AggregateSummary(Entity):
                        """
                        Aggregate summary of statistics
                        
                        .. attribute:: calling_station_id_attribute_format_warnings
                        
                        	Calling station ID attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: destination_station_id_attribute_format_warnings
                        
                        	Destination station ID attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: install_user_profiles
                        
                        	User profiles installed
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: nas_port_attribute_format_warnings
                        
                        	NAS port attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: nas_port_id_attribute_format_warnings
                        
                        	NAS port ID attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: no_class_match_in_start_request
                        
                        	No control policy class match during subscriber start
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: no_subscriber_control_policy_on_interface
                        
                        	Subscriber control policy not applied on interface
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_no_quota
                        
                        	Session Disconnect Request Queued, no quota
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_none_started
                        
                        	Session Disconnect Requests not Dequeued, no quota
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_q_count
                        
                        	Session Disconnect Requests Queued
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_quota
                        
                        	Session Disconnect Quota
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_quota_avail
                        
                        	Session Disconnect Request Accepted, quota available
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_quota_exhausts
                        
                        	Session Disconnect Quota Exhausts
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_quota_remaining
                        
                        	Session Disconnect Quota Remaining
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_recon_ip
                        
                        	Session Disconnect Requests not Dequeued, reconciliation in progress
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_errors
                        
                        	User profile errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_install_errors
                        
                        	User profile install errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_removals
                        
                        	User profile removals
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: username_attribute_format_warnings
                        
                        	Username attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

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

                            self.calling_station_id_attribute_format_warnings = YLeaf(YType.uint64, "calling-station-id-attribute-format-warnings")

                            self.destination_station_id_attribute_format_warnings = YLeaf(YType.uint64, "destination-station-id-attribute-format-warnings")

                            self.install_user_profiles = YLeaf(YType.uint64, "install-user-profiles")

                            self.nas_port_attribute_format_warnings = YLeaf(YType.uint64, "nas-port-attribute-format-warnings")

                            self.nas_port_id_attribute_format_warnings = YLeaf(YType.uint64, "nas-port-id-attribute-format-warnings")

                            self.no_class_match_in_start_request = YLeaf(YType.uint64, "no-class-match-in-start-request")

                            self.no_subscriber_control_policy_on_interface = YLeaf(YType.uint64, "no-subscriber-control-policy-on-interface")

                            self.sess_disc_no_quota = YLeaf(YType.uint64, "sess-disc-no-quota")

                            self.sess_disc_none_started = YLeaf(YType.uint64, "sess-disc-none-started")

                            self.sess_disc_q_count = YLeaf(YType.uint32, "sess-disc-q-count")

                            self.sess_disc_quota = YLeaf(YType.uint32, "sess-disc-quota")

                            self.sess_disc_quota_avail = YLeaf(YType.uint64, "sess-disc-quota-avail")

                            self.sess_disc_quota_exhausts = YLeaf(YType.uint64, "sess-disc-quota-exhausts")

                            self.sess_disc_quota_remaining = YLeaf(YType.uint32, "sess-disc-quota-remaining")

                            self.sess_disc_recon_ip = YLeaf(YType.uint64, "sess-disc-recon-ip")

                            self.user_profile_errors = YLeaf(YType.uint64, "user-profile-errors")

                            self.user_profile_install_errors = YLeaf(YType.uint64, "user-profile-install-errors")

                            self.user_profile_removals = YLeaf(YType.uint64, "user-profile-removals")

                            self.username_attribute_format_warnings = YLeaf(YType.uint64, "username-attribute-format-warnings")
                            self._segment_path = lambda: "aggregate-summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary, ['calling_station_id_attribute_format_warnings', 'destination_station_id_attribute_format_warnings', 'install_user_profiles', 'nas_port_attribute_format_warnings', 'nas_port_id_attribute_format_warnings', 'no_class_match_in_start_request', 'no_subscriber_control_policy_on_interface', 'sess_disc_no_quota', 'sess_disc_none_started', 'sess_disc_q_count', 'sess_disc_quota', 'sess_disc_quota_avail', 'sess_disc_quota_exhausts', 'sess_disc_quota_remaining', 'sess_disc_recon_ip', 'user_profile_errors', 'user_profile_install_errors', 'user_profile_removals', 'username_attribute_format_warnings'], name, value)


                    class Srg(Entity):
                        """
                        Geo Redundancy statistics
                        
                        .. attribute:: ack_to_srg
                        
                        	Number of ACKs sent to Srg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: actual_txlist_sent
                        
                        	Txlist Send Success
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: alreadyin_txlist
                        
                        	Element already in Txlist
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_upd_clean_callback
                        
                        	Txlist Create/update clean callback
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_update_encode
                        
                        	Txlist Create Update Encode
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delete_clean_callback
                        
                        	Txlist Delete clean callback
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delete_encode
                        
                        	Txlist Delete Encode
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: eod_count
                        
                        	Number of EODs Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_control_resume_threshold
                        
                        	Threshold Limit to resume the flow control
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_add_count
                        
                        	No.of inflight sessions added
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_alloc_fails
                        
                        	Memory Alloc Failures for Inflight Entry
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_delete_failures
                        
                        	Inflight Entry Delete Failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_deletes
                        
                        	Inflight Deletes Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_insert_failures
                        
                        	Inflight Entry Insert Failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_not_found
                        
                        	Inflight Entries not found during delete
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_session_count
                        
                        	No.of Sessions inflight at given time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_under_run_count
                        
                        	Inflight Underrun Counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_srg_flow_control_enabled
                        
                        	Flag indicating SRG Flow control enabled or not
                        	**type**\:  bool
                        
                        .. attribute:: last_pause_period
                        
                        	Amount of time paused during last flow control window
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_pause_time
                        
                        	Timestamp of recent Pause Event
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_resume_time
                        
                        	Timestamp of recent Resume Event
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: max_inflight_sessoin_count
                        
                        	Maximum no.of inflight sessions allowed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nack_to_srg
                        
                        	Number of NACKs sent to Srg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nack_to_srg_fail_cnt
                        
                        	Number of NACKs Failed to send to Srg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_create_update
                        
                        	Create Update received on slave
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_decode_fail
                        
                        	Decode failed on Slave
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_delete
                        
                        	Delete received on slave
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_recv_entry
                        
                        	Slave Recieved Sync
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_count
                        
                        	Number of SODs Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_dirty_delete_count
                        
                        	Number of Sessions Invalid Deletes Within SOD EOD Window
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_dirty_mark_count
                        
                        	Number of Sessions Marked as Invalid Within SOD EOD Window
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_replay_req_count
                        
                        	Number of Replay Requests Within SOD EOD Window
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_context_free
                        
                        	SRG context freed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_context_malloc
                        
                        	SRG context allocated
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_dont_send_to_txlist
                        
                        	Total No of times Dont send to Txlist
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_master_eoms_pending
                        
                        	Total No of times Master EOMS Pending
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_pause_count
                        
                        	Total No.of times Pause is Enabled
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_pause_time
                        
                        	Total Amount of time paused during all flow control windows
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_resume_count
                        
                        	Total No.of times Resume is triggered
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_srg_not_master
                        
                        	Total No of times SRG Not Master
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_clean_invalid_state
                        
                        	Number of Txlist Cleanup called on Invalid subscriber srg state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_app
                        
                        	Number of Txlist delete for App msg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_app_notlinked
                        
                        	Number of Txlist delete for App which are not linked
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_sync
                        
                        	Number for Txlist delete for sync msg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_sync_notlinked
                        
                        	Number of Txlist delete for sync which are not linked
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_encode
                        
                        	Txlist Encode
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_encode_fail
                        
                        	Txlist encode Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_remove_all
                        
                        	Number of Txlist remove all calls
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_remove_all_internal_error
                        
                        	Number of Internal errors upon Master Txlist remove all call
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_failed
                        
                        	Txlist Send Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_failed_notactive
                        
                        	Txlist send failed due to not active
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_triggered
                        
                        	Txlist Send Triggered
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

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

                            self.ack_to_srg = YLeaf(YType.uint32, "ack-to-srg")

                            self.actual_txlist_sent = YLeaf(YType.uint32, "actual-txlist-sent")

                            self.alreadyin_txlist = YLeaf(YType.uint32, "alreadyin-txlist")

                            self.create_upd_clean_callback = YLeaf(YType.uint32, "create-upd-clean-callback")

                            self.create_update_encode = YLeaf(YType.uint32, "create-update-encode")

                            self.delete_clean_callback = YLeaf(YType.uint32, "delete-clean-callback")

                            self.delete_encode = YLeaf(YType.uint32, "delete-encode")

                            self.eod_count = YLeaf(YType.uint32, "eod-count")

                            self.flow_control_resume_threshold = YLeaf(YType.uint32, "flow-control-resume-threshold")

                            self.inflight_add_count = YLeaf(YType.uint32, "inflight-add-count")

                            self.inflight_alloc_fails = YLeaf(YType.uint32, "inflight-alloc-fails")

                            self.inflight_delete_failures = YLeaf(YType.uint32, "inflight-delete-failures")

                            self.inflight_deletes = YLeaf(YType.uint32, "inflight-deletes")

                            self.inflight_insert_failures = YLeaf(YType.uint32, "inflight-insert-failures")

                            self.inflight_not_found = YLeaf(YType.uint32, "inflight-not-found")

                            self.inflight_session_count = YLeaf(YType.uint32, "inflight-session-count")

                            self.inflight_under_run_count = YLeaf(YType.uint32, "inflight-under-run-count")

                            self.is_srg_flow_control_enabled = YLeaf(YType.boolean, "is-srg-flow-control-enabled")

                            self.last_pause_period = YLeaf(YType.uint64, "last-pause-period")

                            self.last_pause_time = YLeaf(YType.uint64, "last-pause-time")

                            self.last_resume_time = YLeaf(YType.uint64, "last-resume-time")

                            self.max_inflight_sessoin_count = YLeaf(YType.uint32, "max-inflight-sessoin-count")

                            self.nack_to_srg = YLeaf(YType.uint32, "nack-to-srg")

                            self.nack_to_srg_fail_cnt = YLeaf(YType.uint32, "nack-to-srg-fail-cnt")

                            self.slave_create_update = YLeaf(YType.uint32, "slave-create-update")

                            self.slave_decode_fail = YLeaf(YType.uint32, "slave-decode-fail")

                            self.slave_delete = YLeaf(YType.uint32, "slave-delete")

                            self.slave_recv_entry = YLeaf(YType.uint32, "slave-recv-entry")

                            self.sod_count = YLeaf(YType.uint32, "sod-count")

                            self.sod_eod_dirty_delete_count = YLeaf(YType.uint32, "sod-eod-dirty-delete-count")

                            self.sod_eod_dirty_mark_count = YLeaf(YType.uint32, "sod-eod-dirty-mark-count")

                            self.sod_eod_replay_req_count = YLeaf(YType.uint32, "sod-eod-replay-req-count")

                            self.srg_context_free = YLeaf(YType.uint32, "srg-context-free")

                            self.srg_context_malloc = YLeaf(YType.uint32, "srg-context-malloc")

                            self.total_dont_send_to_txlist = YLeaf(YType.uint32, "total-dont-send-to-txlist")

                            self.total_master_eoms_pending = YLeaf(YType.uint32, "total-master-eoms-pending")

                            self.total_pause_count = YLeaf(YType.uint32, "total-pause-count")

                            self.total_pause_time = YLeaf(YType.uint64, "total-pause-time")

                            self.total_resume_count = YLeaf(YType.uint32, "total-resume-count")

                            self.total_srg_not_master = YLeaf(YType.uint32, "total-srg-not-master")

                            self.txlist_clean_invalid_state = YLeaf(YType.uint32, "txlist-clean-invalid-state")

                            self.txlist_del_app = YLeaf(YType.uint32, "txlist-del-app")

                            self.txlist_del_app_notlinked = YLeaf(YType.uint32, "txlist-del-app-notlinked")

                            self.txlist_del_sync = YLeaf(YType.uint32, "txlist-del-sync")

                            self.txlist_del_sync_notlinked = YLeaf(YType.uint32, "txlist-del-sync-notlinked")

                            self.txlist_encode = YLeaf(YType.uint32, "txlist-encode")

                            self.txlist_encode_fail = YLeaf(YType.uint32, "txlist-encode-fail")

                            self.txlist_remove_all = YLeaf(YType.uint32, "txlist-remove-all")

                            self.txlist_remove_all_internal_error = YLeaf(YType.uint32, "txlist-remove-all-internal-error")

                            self.txlist_send_failed = YLeaf(YType.uint32, "txlist-send-failed")

                            self.txlist_send_failed_notactive = YLeaf(YType.uint32, "txlist-send-failed-notactive")

                            self.txlist_send_triggered = YLeaf(YType.uint32, "txlist-send-triggered")
                            self._segment_path = lambda: "srg"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Manager.Nodes.Node.Statistics.Srg, ['ack_to_srg', 'actual_txlist_sent', 'alreadyin_txlist', 'create_upd_clean_callback', 'create_update_encode', 'delete_clean_callback', 'delete_encode', 'eod_count', 'flow_control_resume_threshold', 'inflight_add_count', 'inflight_alloc_fails', 'inflight_delete_failures', 'inflight_deletes', 'inflight_insert_failures', 'inflight_not_found', 'inflight_session_count', 'inflight_under_run_count', 'is_srg_flow_control_enabled', 'last_pause_period', 'last_pause_time', 'last_resume_time', 'max_inflight_sessoin_count', 'nack_to_srg', 'nack_to_srg_fail_cnt', 'slave_create_update', 'slave_decode_fail', 'slave_delete', 'slave_recv_entry', 'sod_count', 'sod_eod_dirty_delete_count', 'sod_eod_dirty_mark_count', 'sod_eod_replay_req_count', 'srg_context_free', 'srg_context_malloc', 'total_dont_send_to_txlist', 'total_master_eoms_pending', 'total_pause_count', 'total_pause_time', 'total_resume_count', 'total_srg_not_master', 'txlist_clean_invalid_state', 'txlist_del_app', 'txlist_del_app_notlinked', 'txlist_del_sync', 'txlist_del_sync_notlinked', 'txlist_encode', 'txlist_encode_fail', 'txlist_remove_all', 'txlist_remove_all_internal_error', 'txlist_send_failed', 'txlist_send_failed_notactive', 'txlist_send_triggered'], name, value)


    class Session(Entity):
        """
        Subscriber session operational data
        
        .. attribute:: nodes
        
        	List of subscriber session supported nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes>`
        
        

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
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node>`
            
            

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
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: access_interface_summaries
                
                	Summary information filtered by access interface
                	**type**\:   :py:class:`AccessInterfaceSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries>`
                
                .. attribute:: address_family_summaries
                
                	Summary information filtered by address family
                	**type**\:   :py:class:`AddressFamilySummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries>`
                
                .. attribute:: authentication_summaries
                
                	Summary information filtered by authentication state
                	**type**\:   :py:class:`AuthenticationSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries>`
                
                .. attribute:: author_summaries
                
                	Summary information filtered by authorization state
                	**type**\:   :py:class:`AuthorSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries>`
                
                .. attribute:: interface_summaries
                
                	Summary information filtered by interface
                	**type**\:   :py:class:`InterfaceSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries>`
                
                .. attribute:: ipv4_address_summaries
                
                	Summary information filtered by subscriber IPv4 address
                	**type**\:   :py:class:`Ipv4AddressSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries>`
                
                .. attribute:: ipv4_address_vrf_summaries
                
                	Summary information filtered by IPv4 address and VRF
                	**type**\:   :py:class:`Ipv4AddressVrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries>`
                
                .. attribute:: mac_summaries
                
                	Summary information filtered by MAC address
                	**type**\:   :py:class:`MacSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries>`
                
                .. attribute:: sessions
                
                	IP subscriber sessions
                	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions>`
                
                .. attribute:: state_summaries
                
                	Summary information filtered by session state
                	**type**\:   :py:class:`StateSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries>`
                
                .. attribute:: summary
                
                	Subscriber session summary information
                	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary>`
                
                .. attribute:: username_summaries
                
                	Summary information filtered by username
                	**type**\:   :py:class:`UsernameSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries>`
                
                .. attribute:: vrf_summaries
                
                	Summary information filtered by VRF
                	**type**\:   :py:class:`VrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries>`
                
                

                """

                _prefix = 'iedge4710-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Subscriber.Session.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"access-interface-summaries" : ("access_interface_summaries", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries), "address-family-summaries" : ("address_family_summaries", Subscriber.Session.Nodes.Node.AddressFamilySummaries), "authentication-summaries" : ("authentication_summaries", Subscriber.Session.Nodes.Node.AuthenticationSummaries), "author-summaries" : ("author_summaries", Subscriber.Session.Nodes.Node.AuthorSummaries), "interface-summaries" : ("interface_summaries", Subscriber.Session.Nodes.Node.InterfaceSummaries), "ipv4-address-summaries" : ("ipv4_address_summaries", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries), "ipv4-address-vrf-summaries" : ("ipv4_address_vrf_summaries", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries), "mac-summaries" : ("mac_summaries", Subscriber.Session.Nodes.Node.MacSummaries), "sessions" : ("sessions", Subscriber.Session.Nodes.Node.Sessions), "state-summaries" : ("state_summaries", Subscriber.Session.Nodes.Node.StateSummaries), "summary" : ("summary", Subscriber.Session.Nodes.Node.Summary), "username-summaries" : ("username_summaries", Subscriber.Session.Nodes.Node.UsernameSummaries), "vrf-summaries" : ("vrf_summaries", Subscriber.Session.Nodes.Node.VrfSummaries)}
                    self._child_list_classes = {}

                    self.node_name = YLeaf(YType.str, "node-name")

                    self.access_interface_summaries = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries()
                    self.access_interface_summaries.parent = self
                    self._children_name_map["access_interface_summaries"] = "access-interface-summaries"
                    self._children_yang_names.add("access-interface-summaries")

                    self.address_family_summaries = Subscriber.Session.Nodes.Node.AddressFamilySummaries()
                    self.address_family_summaries.parent = self
                    self._children_name_map["address_family_summaries"] = "address-family-summaries"
                    self._children_yang_names.add("address-family-summaries")

                    self.authentication_summaries = Subscriber.Session.Nodes.Node.AuthenticationSummaries()
                    self.authentication_summaries.parent = self
                    self._children_name_map["authentication_summaries"] = "authentication-summaries"
                    self._children_yang_names.add("authentication-summaries")

                    self.author_summaries = Subscriber.Session.Nodes.Node.AuthorSummaries()
                    self.author_summaries.parent = self
                    self._children_name_map["author_summaries"] = "author-summaries"
                    self._children_yang_names.add("author-summaries")

                    self.interface_summaries = Subscriber.Session.Nodes.Node.InterfaceSummaries()
                    self.interface_summaries.parent = self
                    self._children_name_map["interface_summaries"] = "interface-summaries"
                    self._children_yang_names.add("interface-summaries")

                    self.ipv4_address_summaries = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries()
                    self.ipv4_address_summaries.parent = self
                    self._children_name_map["ipv4_address_summaries"] = "ipv4-address-summaries"
                    self._children_yang_names.add("ipv4-address-summaries")

                    self.ipv4_address_vrf_summaries = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries()
                    self.ipv4_address_vrf_summaries.parent = self
                    self._children_name_map["ipv4_address_vrf_summaries"] = "ipv4-address-vrf-summaries"
                    self._children_yang_names.add("ipv4-address-vrf-summaries")

                    self.mac_summaries = Subscriber.Session.Nodes.Node.MacSummaries()
                    self.mac_summaries.parent = self
                    self._children_name_map["mac_summaries"] = "mac-summaries"
                    self._children_yang_names.add("mac-summaries")

                    self.sessions = Subscriber.Session.Nodes.Node.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._children_yang_names.add("sessions")

                    self.state_summaries = Subscriber.Session.Nodes.Node.StateSummaries()
                    self.state_summaries.parent = self
                    self._children_name_map["state_summaries"] = "state-summaries"
                    self._children_yang_names.add("state-summaries")

                    self.summary = Subscriber.Session.Nodes.Node.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")

                    self.username_summaries = Subscriber.Session.Nodes.Node.UsernameSummaries()
                    self.username_summaries.parent = self
                    self._children_name_map["username_summaries"] = "username-summaries"
                    self._children_yang_names.add("username-summaries")

                    self.vrf_summaries = Subscriber.Session.Nodes.Node.VrfSummaries()
                    self.vrf_summaries.parent = self
                    self._children_name_map["vrf_summaries"] = "vrf-summaries"
                    self._children_yang_names.add("vrf-summaries")
                    self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-iedge4710-oper:subscriber/session/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Subscriber.Session.Nodes.Node, ['node_name'], name, value)


                class AccessInterfaceSummaries(Entity):
                    """
                    Summary information filtered by access
                    interface
                    
                    .. attribute:: access_interface_summary
                    
                    	Access interface summary
                    	**type**\: list of    :py:class:`AccessInterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary>`
                    
                    

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
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary, self).__init__()

                            self.yang_name = "access-interface-summary"
                            self.yang_parent_name = "access-interface-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr)}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "access-interface-summary" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary, ['interface_name'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "access-interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "access-interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class AddressFamilySummaries(Entity):
                    """
                    Summary information filtered by address
                    family
                    
                    .. attribute:: address_family_summary
                    
                    	Address family summary
                    	**type**\: list of    :py:class:`AddressFamilySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary>`
                    
                    

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
                        	**type**\:   :py:class:`SubscriberAddressFamilyFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAddressFamilyFilterFlag>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary, self).__init__()

                            self.yang_name = "address-family-summary"
                            self.yang_parent_name = "address-family-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr)}
                            self._child_list_classes = {}

                            self.address_family = YLeaf(YType.enumeration, "address-family")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "address-family-summary" + "[address-family='" + self.address_family.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary, ['address_family'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "address-family-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "address-family-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class AuthenticationSummaries(Entity):
                    """
                    Summary information filtered by
                    authentication state
                    
                    .. attribute:: authentication_summary
                    
                    	authentication summary
                    	**type**\: list of    :py:class:`AuthenticationSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary>`
                    
                    

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
                        	**type**\:   :py:class:`SubscriberAuthenStateFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAuthenStateFilterFlag>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary, self).__init__()

                            self.yang_name = "authentication-summary"
                            self.yang_parent_name = "authentication-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr)}
                            self._child_list_classes = {}

                            self.authentication_state = YLeaf(YType.enumeration, "authentication-state")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "authentication-summary" + "[authentication-state='" + self.authentication_state.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary, ['authentication_state'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "authentication-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "authentication-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class AuthorSummaries(Entity):
                    """
                    Summary information filtered by authorization
                    state
                    
                    .. attribute:: author_summary
                    
                    	authorization summary
                    	**type**\: list of    :py:class:`AuthorSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary>`
                    
                    

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
                        	**type**\:   :py:class:`SubscriberAuthorStateFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAuthorStateFilterFlag>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary, self).__init__()

                            self.yang_name = "author-summary"
                            self.yang_parent_name = "author-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr)}
                            self._child_list_classes = {}

                            self.author_state = YLeaf(YType.enumeration, "author-state")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "author-summary" + "[author-state='" + self.author_state.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary, ['author_state'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "author-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "author-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class InterfaceSummaries(Entity):
                    """
                    Summary information filtered by interface
                    
                    .. attribute:: interface_summary
                    
                    	Interface summary
                    	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary>`
                    
                    

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
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary, self).__init__()

                            self.yang_name = "interface-summary"
                            self.yang_parent_name = "interface-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr)}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "interface-summary" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary, ['interface_name'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "interface-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class Ipv4AddressSummaries(Entity):
                    """
                    Summary information filtered by subscriber
                    IPv4 address
                    
                    .. attribute:: ipv4_address_summary
                    
                    	IPv4 address summary
                    	**type**\: list of    :py:class:`Ipv4AddressSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary>`
                    
                    

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
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary, self).__init__()

                            self.yang_name = "ipv4-address-summary"
                            self.yang_parent_name = "ipv4-address-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr)}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "ipv4-address-summary" + "[address='" + self.address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary, ['address'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "ipv4-address-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "ipv4-address-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class Ipv4AddressVrfSummaries(Entity):
                    """
                    Summary information filtered by IPv4 address
                    and VRF
                    
                    .. attribute:: ipv4_address_vrf_summary
                    
                    	IPv4 address and VRF summary
                    	**type**\: list of    :py:class:`Ipv4AddressVrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary>`
                    
                    

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
                        
                        .. attribute:: address
                        
                        	Subscriber IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr>`
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary, self).__init__()

                            self.yang_name = "ipv4-address-vrf-summary"
                            self.yang_parent_name = "ipv4-address-vrf-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr)}
                            self._child_list_classes = {}

                            self.address = YLeaf(YType.str, "address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "ipv4-address-vrf-summary"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary, ['address', 'vrf_name'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "ipv4-address-vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "ipv4-address-vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class MacSummaries(Entity):
                    """
                    Summary information filtered by MAC address
                    
                    .. attribute:: mac_summary
                    
                    	MAC address summary
                    	**type**\: list of    :py:class:`MacSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary>`
                    
                    

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
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary, self).__init__()

                            self.yang_name = "mac-summary"
                            self.yang_parent_name = "mac-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr)}
                            self._child_list_classes = {}

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "mac-summary" + "[mac-address='" + self.mac_address.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary, ['mac_address'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "mac-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "mac-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class Sessions(Entity):
                    """
                    IP subscriber sessions
                    
                    .. attribute:: session
                    
                    	Subscriber session information
                    	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session>`
                    
                    

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
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: access_interface_name
                        
                        	Access interface name associated with the session
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: account_session_id
                        
                        	Accounting session ID
                        	**type**\:  str
                        
                        .. attribute:: accounting
                        
                        	Accounting information
                        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.Accounting>`
                        
                        .. attribute:: af_up_status
                        
                        	AF status per Subscriber Session
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  str
                        
                        .. attribute:: clientname
                        
                        	Client Username
                        	**type**\:  str
                        
                        .. attribute:: delegated_ipv6_prefix
                        
                        	Session delegated IPv6 prefix
                        	**type**\:  str
                        
                        .. attribute:: formattedname
                        
                        	Formatted Username
                        	**type**\:  str
                        
                        .. attribute:: idle_state_change_time
                        
                        	Time when idle state change occurred in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: ipv6_interface_id
                        
                        	IPv6 Interface ID
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: is_session_authentic
                        
                        	If true, session is authentic
                        	**type**\:  bool
                        
                        .. attribute:: is_session_author
                        
                        	If true, session is authorized
                        	**type**\:  bool
                        
                        .. attribute:: lac_address
                        
                        	PPPoE LAC address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: lns_address
                        
                        	PPPoE LNS address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mobility_attributes
                        
                        	List of mobility attributes collected for subscriber session
                        	**type**\:   :py:class:`MobilityAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes>`
                        
                        .. attribute:: nas_port
                        
                        	NAS port
                        	**type**\:  str
                        
                        .. attribute:: pending_callbacks
                        
                        	Active pending callbacks bitmask
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pppoe_sub_type
                        
                        	PPPoE sub type
                        	**type**\:   :py:class:`IedgePppSub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgePppSub>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  str
                        
                        .. attribute:: session_change_of_authorization
                        
                        	Subscriber change of authorization information
                        	**type**\: list of    :py:class:`SessionChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.SessionChangeOfAuthorization>`
                        
                        .. attribute:: session_creation_time
                        
                        	Session creation time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                        	**type**\:  str
                        
                        .. attribute:: session_ip_address
                        
                        	Session ip address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: session_ipv4_state
                        
                        	Session IPv4 state
                        	**type**\:   :py:class:`IedgeOperSessionAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionAfState>`
                        
                        .. attribute:: session_ipv6_address
                        
                        	Session IPv6 address
                        	**type**\:  str
                        
                        .. attribute:: session_ipv6_prefix
                        
                        	Session IPv6 prefix
                        	**type**\:  str
                        
                        .. attribute:: session_ipv6_state
                        
                        	Session IPv6 state
                        	**type**\:   :py:class:`IedgeOperSessionAfState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionAfState>`
                        
                        .. attribute:: session_state
                        
                        	Session state
                        	**type**\:   :py:class:`IedgeOperSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionState>`
                        
                        .. attribute:: session_type
                        
                        	Subscriber session type
                        	**type**\:   :py:class:`IedgeOperSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSession>`
                        
                        .. attribute:: total_session_idle_time
                        
                        	Total session idle time (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: tunnel_client_authentication_id
                        
                        	PPPoE LAC tunnel client authentication ID
                        	**type**\:  str
                        
                        .. attribute:: tunnel_server_authentication_id
                        
                        	PPPoE LAC tunnel server authentication ID
                        	**type**\:  str
                        
                        .. attribute:: user_profile_attributes
                        
                        	List of user profile attributes collected for subscriber session
                        	**type**\:   :py:class:`UserProfileAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes>`
                        
                        .. attribute:: username
                        
                        	Username
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Sessions.Session, self).__init__()

                            self.yang_name = "session"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"accounting" : ("accounting", Subscriber.Session.Nodes.Node.Sessions.Session.Accounting), "mobility-attributes" : ("mobility_attributes", Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes), "user-profile-attributes" : ("user_profile_attributes", Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes)}
                            self._child_list_classes = {"session-change-of-authorization" : ("session_change_of_authorization", Subscriber.Session.Nodes.Node.Sessions.Session.SessionChangeOfAuthorization)}

                            self.session_id = YLeaf(YType.str, "session-id")

                            self.access_interface_name = YLeaf(YType.str, "access-interface-name")

                            self.account_session_id = YLeaf(YType.str, "account-session-id")

                            self.af_up_status = YLeaf(YType.uint32, "af-up-status")

                            self.circuit_id = YLeaf(YType.str, "circuit-id")

                            self.clientname = YLeaf(YType.str, "clientname")

                            self.delegated_ipv6_prefix = YLeaf(YType.str, "delegated-ipv6-prefix")

                            self.formattedname = YLeaf(YType.str, "formattedname")

                            self.idle_state_change_time = YLeaf(YType.str, "idle-state-change-time")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.ipv6_interface_id = YLeaf(YType.str, "ipv6-interface-id")

                            self.is_session_authentic = YLeaf(YType.boolean, "is-session-authentic")

                            self.is_session_author = YLeaf(YType.boolean, "is-session-author")

                            self.lac_address = YLeaf(YType.str, "lac-address")

                            self.lns_address = YLeaf(YType.str, "lns-address")

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.nas_port = YLeaf(YType.str, "nas-port")

                            self.pending_callbacks = YLeaf(YType.uint64, "pending-callbacks")

                            self.pppoe_sub_type = YLeaf(YType.enumeration, "pppoe-sub-type")

                            self.remote_id = YLeaf(YType.str, "remote-id")

                            self.session_creation_time = YLeaf(YType.str, "session-creation-time")

                            self.session_ip_address = YLeaf(YType.str, "session-ip-address")

                            self.session_ipv4_state = YLeaf(YType.enumeration, "session-ipv4-state")

                            self.session_ipv6_address = YLeaf(YType.str, "session-ipv6-address")

                            self.session_ipv6_prefix = YLeaf(YType.str, "session-ipv6-prefix")

                            self.session_ipv6_state = YLeaf(YType.enumeration, "session-ipv6-state")

                            self.session_state = YLeaf(YType.enumeration, "session-state")

                            self.session_type = YLeaf(YType.enumeration, "session-type")

                            self.total_session_idle_time = YLeaf(YType.uint32, "total-session-idle-time")

                            self.tunnel_client_authentication_id = YLeaf(YType.str, "tunnel-client-authentication-id")

                            self.tunnel_server_authentication_id = YLeaf(YType.str, "tunnel-server-authentication-id")

                            self.username = YLeaf(YType.str, "username")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.accounting = Subscriber.Session.Nodes.Node.Sessions.Session.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                            self._children_yang_names.add("accounting")

                            self.mobility_attributes = Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes()
                            self.mobility_attributes.parent = self
                            self._children_name_map["mobility_attributes"] = "mobility-attributes"
                            self._children_yang_names.add("mobility-attributes")

                            self.user_profile_attributes = Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes()
                            self.user_profile_attributes.parent = self
                            self._children_name_map["user_profile_attributes"] = "user-profile-attributes"
                            self._children_yang_names.add("user-profile-attributes")

                            self.session_change_of_authorization = YList(self)
                            self._segment_path = lambda: "session" + "[session-id='" + self.session_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session, ['session_id', 'access_interface_name', 'account_session_id', 'af_up_status', 'circuit_id', 'clientname', 'delegated_ipv6_prefix', 'formattedname', 'idle_state_change_time', 'interface_name', 'ipv6_interface_id', 'is_session_authentic', 'is_session_author', 'lac_address', 'lns_address', 'mac_address', 'nas_port', 'pending_callbacks', 'pppoe_sub_type', 'remote_id', 'session_creation_time', 'session_ip_address', 'session_ipv4_state', 'session_ipv6_address', 'session_ipv6_prefix', 'session_ipv6_state', 'session_state', 'session_type', 'total_session_idle_time', 'tunnel_client_authentication_id', 'tunnel_server_authentication_id', 'username', 'vrf_name'], name, value)


                        class Accounting(Entity):
                            """
                            Accounting information
                            
                            .. attribute:: accounting_session
                            
                            	Accounting information
                            	**type**\: list of    :py:class:`AccountingSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session.Accounting.AccountingSession>`
                            
                            

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
                                
                                .. attribute:: accepted_interim_updates
                                
                                	Number of interim updates accepted
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: account_session_id
                                
                                	Accounting session ID
                                	**type**\:  str
                                
                                .. attribute:: accounting_start_time
                                
                                	Accounting start time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Feb 15 15\:12\:49 2011
                                	**type**\:  str
                                
                                .. attribute:: accounting_state_rc
                                
                                	Accounting State Error Code for Accounting Session
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: accounting_stop_state
                                
                                	Accounting Stop State
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interim_interval
                                
                                	Interim accounting interval (in minutes)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: minute
                                
                                .. attribute:: is_interim_accounting_enabled
                                
                                	True if interim accounting is enabled
                                	**type**\:  bool
                                
                                .. attribute:: last_interim_update_attempt_time
                                
                                	Time of last interim update attempt in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                                	**type**\:  str
                                
                                .. attribute:: last_successful_interim_update_time
                                
                                	Time of last successful interim update in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30 \:47 2011
                                	**type**\:  str
                                
                                .. attribute:: method_list_name
                                
                                	AAA method list name used to perform accounting
                                	**type**\:  str
                                
                                .. attribute:: next_interim_update_attempt_time
                                
                                	Time of next interim update attempt (in seconds)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: record_context_name
                                
                                	Accounting record context name
                                	**type**\:  str
                                
                                .. attribute:: rejected_interim_updates
                                
                                	Number of interim updates rejected
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sent_interim_update_failures
                                
                                	Number of interim update send failures
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sent_interim_updates
                                
                                	Number of interim updates sent
                                	**type**\:  int
                                
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

                                    self.accepted_interim_updates = YLeaf(YType.uint32, "accepted-interim-updates")

                                    self.account_session_id = YLeaf(YType.str, "account-session-id")

                                    self.accounting_start_time = YLeaf(YType.str, "accounting-start-time")

                                    self.accounting_state_rc = YLeaf(YType.uint32, "accounting-state-rc")

                                    self.accounting_stop_state = YLeaf(YType.uint32, "accounting-stop-state")

                                    self.interim_interval = YLeaf(YType.uint32, "interim-interval")

                                    self.is_interim_accounting_enabled = YLeaf(YType.boolean, "is-interim-accounting-enabled")

                                    self.last_interim_update_attempt_time = YLeaf(YType.str, "last-interim-update-attempt-time")

                                    self.last_successful_interim_update_time = YLeaf(YType.str, "last-successful-interim-update-time")

                                    self.method_list_name = YLeaf(YType.str, "method-list-name")

                                    self.next_interim_update_attempt_time = YLeaf(YType.uint32, "next-interim-update-attempt-time")

                                    self.record_context_name = YLeaf(YType.str, "record-context-name")

                                    self.rejected_interim_updates = YLeaf(YType.uint32, "rejected-interim-updates")

                                    self.sent_interim_update_failures = YLeaf(YType.uint32, "sent-interim-update-failures")

                                    self.sent_interim_updates = YLeaf(YType.uint32, "sent-interim-updates")
                                    self._segment_path = lambda: "accounting-session"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.Accounting.AccountingSession, ['accepted_interim_updates', 'account_session_id', 'accounting_start_time', 'accounting_state_rc', 'accounting_stop_state', 'interim_interval', 'is_interim_accounting_enabled', 'last_interim_update_attempt_time', 'last_successful_interim_update_time', 'method_list_name', 'next_interim_update_attempt_time', 'record_context_name', 'rejected_interim_updates', 'sent_interim_update_failures', 'sent_interim_updates'], name, value)


                        class MobilityAttributes(Entity):
                            """
                            List of mobility attributes collected for
                            subscriber session
                            
                            .. attribute:: domain_name
                            
                            	Domain Name
                            	**type**\:  str
                            
                            .. attribute:: downlink_gre_key
                            
                            	Downlink GRE Key
                            	**type**\:  str
                            
                            .. attribute:: lease_time
                            
                            	Duration of lease in seconds
                            	**type**\:  str
                            
                            	**units**\: second
                            
                            .. attribute:: mobility_default_ipv4_gateway
                            
                            	Default Gateway IPv4 Address
                            	**type**\:  str
                            
                            .. attribute:: mobility_dhcp_server
                            
                            	DHCP Server
                            	**type**\:  str
                            
                            .. attribute:: mobility_dns_server
                            
                            	DNS Server Primary
                            	**type**\:  str
                            
                            .. attribute:: mobility_ipv4_address
                            
                            	IPv4 address of Mobility Node
                            	**type**\:  str
                            
                            .. attribute:: mobility_ipv4_netmask
                            
                            	IPv4 Netmask
                            	**type**\:  str
                            
                            .. attribute:: mpc_protocol
                            
                            	Cisco MPC Protocol
                            	**type**\:  bool
                            
                            .. attribute:: uplink_gre_key
                            
                            	Uplink GRE Key
                            	**type**\:  str
                            
                            

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

                                self.domain_name = YLeaf(YType.str, "domain-name")

                                self.downlink_gre_key = YLeaf(YType.str, "downlink-gre-key")

                                self.lease_time = YLeaf(YType.str, "lease-time")

                                self.mobility_default_ipv4_gateway = YLeaf(YType.str, "mobility-default-ipv4-gateway")

                                self.mobility_dhcp_server = YLeaf(YType.str, "mobility-dhcp-server")

                                self.mobility_dns_server = YLeaf(YType.str, "mobility-dns-server")

                                self.mobility_ipv4_address = YLeaf(YType.str, "mobility-ipv4-address")

                                self.mobility_ipv4_netmask = YLeaf(YType.str, "mobility-ipv4-netmask")

                                self.mpc_protocol = YLeaf(YType.boolean, "mpc-protocol")

                                self.uplink_gre_key = YLeaf(YType.str, "uplink-gre-key")
                                self._segment_path = lambda: "mobility-attributes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.MobilityAttributes, ['domain_name', 'downlink_gre_key', 'lease_time', 'mobility_default_ipv4_gateway', 'mobility_dhcp_server', 'mobility_dns_server', 'mobility_ipv4_address', 'mobility_ipv4_netmask', 'mpc_protocol', 'uplink_gre_key'], name, value)


                        class SessionChangeOfAuthorization(Entity):
                            """
                            Subscriber change of authorization information
                            
                            .. attribute:: coa_reply_attributes
                            
                            	List of Reply Attributes collected in COA response
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: coa_request_attributes
                            
                            	List of Request Attributes collected in COA response
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: reply_time
                            
                            	Reply time in DDD MMM DD HH\:MM\:SS YYYY format eg \: Tue Apr 11 21\:30\:47 2011
                            	**type**\:  str
                            
                            .. attribute:: request_acked
                            
                            	Coa Request Acked
                            	**type**\:  bool
                            
                            .. attribute:: request_time
                            
                            	Request time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                            	**type**\:  str
                            
                            

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

                                self.coa_reply_attributes = YLeaf(YType.str, "coa-reply-attributes")

                                self.coa_request_attributes = YLeaf(YType.str, "coa-request-attributes")

                                self.reply_time = YLeaf(YType.str, "reply-time")

                                self.request_acked = YLeaf(YType.boolean, "request-acked")

                                self.request_time = YLeaf(YType.str, "request-time")
                                self._segment_path = lambda: "session-change-of-authorization"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.SessionChangeOfAuthorization, ['coa_reply_attributes', 'coa_request_attributes', 'reply_time', 'request_acked', 'request_time'], name, value)


                        class UserProfileAttributes(Entity):
                            """
                            List of user profile attributes collected for
                            subscriber session
                            
                            .. attribute:: accounting_session_id
                            
                            	Accounting session ID
                            	**type**\:  str
                            
                            .. attribute:: actual_data_rate_downstream
                            
                            	Actual data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: actual_data_rate_upstream
                            
                            	Actual data rate upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: attainable_data_rate_downstream
                            
                            	Attainable data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: attainable_data_rate_upstream
                            
                            	Attainable data rate upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: authorization_service_type
                            
                            	Authorization service type
                            	**type**\:   :py:class:`AaaAuthService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaAuthService>`
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\:  str
                            
                            .. attribute:: connection_receive_speed
                            
                            	Connection receive speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connection_transmission_speed
                            
                            	Connection transmission speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: destination_station_id
                            
                            	Destination station ID
                            	**type**\:  str
                            
                            .. attribute:: downstream_parameterized_qos_policy
                            
                            	Downstream parameterized QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            .. attribute:: downstream_qos_policy
                            
                            	Downstream QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            .. attribute:: egress_access_list
                            
                            	Egress access list
                            	**type**\:  str
                            
                            .. attribute:: formatted_calling_station_id
                            
                            	Formatted calling station id
                            	**type**\:  str
                            
                            .. attribute:: ingress_access_list
                            
                            	Ingress access list
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\:  str
                            
                            .. attribute:: interface_type
                            
                            	Interface type
                            	**type**\:   :py:class:`AaaInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaInterface>`
                            
                            .. attribute:: interim_accounting_interval
                            
                            	Interim accounting interval
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_netmask
                            
                            	IP netmask for the user
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv4_unnumbered
                            
                            	IPv4 unnumbered
                            	**type**\:  str
                            
                            .. attribute:: ipv4mtu
                            
                            	IPv4 maximum transmission unit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_interworking_functionality
                            
                            	True, if interworking functionality
                            	**type**\:  bool
                            
                            .. attribute:: max_data_rate_downstream
                            
                            	Maximum data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_data_rate_upstream
                            
                            	Maximum data rate upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_interleaving_delay_downstream
                            
                            	Maximum interleaving delay downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_interleaving_delay_upstream
                            
                            	Maximum interleaving delay upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_downstream
                            
                            	Minimum data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_downstream_low_power
                            
                            	Minimum data rate downstream low power (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_upstream_low_power
                            
                            	Minimum data rate upstream low power (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: parent_interface_name
                            
                            	Parent interface name
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: pool_address
                            
                            	IP address pool
                            	**type**\:  str
                            
                            .. attribute:: primary_dns_server_address
                            
                            	Primary DNS server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: primary_net_bios_server_address
                            
                            	Primary net bios server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            .. attribute:: route
                            
                            	Route information for a user session
                            	**type**\:  str
                            
                            .. attribute:: secondary_dns_server_address
                            
                            	Secondary DNS server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary_net_bios_server_address
                            
                            	Secondary net bios server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: session_termination_cause
                            
                            	Session termination cause
                            	**type**\:   :py:class:`AaaTerminateCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTerminateCause>`
                            
                            .. attribute:: session_timeout
                            
                            	Session timeout (in seconds)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: strict_rpf_packets
                            
                            	Strict RPF packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tunnel_client_authentication_id
                            
                            	Tunnel client authentication ID
                            	**type**\:  str
                            
                            .. attribute:: tunnel_client_endpoint
                            
                            	Tunnel client endpoint
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tunnel_medium
                            
                            	Tunnel medium
                            	**type**\:   :py:class:`AaaTunnelMedium <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTunnelMedium>`
                            
                            .. attribute:: tunnel_preference
                            
                            	Tunnel preference
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tunnel_protocol
                            
                            	Tunnel protocol
                            	**type**\:   :py:class:`AaaTunnelProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTunnelProto>`
                            
                            .. attribute:: tunnel_server_endpoint
                            
                            	Tunnel server endpoint
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tunnel_tos_setting
                            
                            	Tunnel TOS setting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: upstream_parameterized_qos_policy
                            
                            	Upstream parameterized QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            .. attribute:: upstream_qos_policy
                            
                            	Upstream QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            

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

                                self.accounting_session_id = YLeaf(YType.str, "accounting-session-id")

                                self.actual_data_rate_downstream = YLeaf(YType.uint32, "actual-data-rate-downstream")

                                self.actual_data_rate_upstream = YLeaf(YType.uint32, "actual-data-rate-upstream")

                                self.attainable_data_rate_downstream = YLeaf(YType.uint32, "attainable-data-rate-downstream")

                                self.attainable_data_rate_upstream = YLeaf(YType.uint32, "attainable-data-rate-upstream")

                                self.authorization_service_type = YLeaf(YType.enumeration, "authorization-service-type")

                                self.circuit_id = YLeaf(YType.str, "circuit-id")

                                self.connection_receive_speed = YLeaf(YType.uint32, "connection-receive-speed")

                                self.connection_transmission_speed = YLeaf(YType.uint32, "connection-transmission-speed")

                                self.destination_station_id = YLeaf(YType.str, "destination-station-id")

                                self.downstream_parameterized_qos_policy = YLeaf(YType.str, "downstream-parameterized-qos-policy")

                                self.downstream_qos_policy = YLeaf(YType.str, "downstream-qos-policy")

                                self.egress_access_list = YLeaf(YType.str, "egress-access-list")

                                self.formatted_calling_station_id = YLeaf(YType.str, "formatted-calling-station-id")

                                self.ingress_access_list = YLeaf(YType.str, "ingress-access-list")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.interface_type = YLeaf(YType.enumeration, "interface-type")

                                self.interim_accounting_interval = YLeaf(YType.uint32, "interim-accounting-interval")

                                self.ip_netmask = YLeaf(YType.str, "ip-netmask")

                                self.ipv4_unnumbered = YLeaf(YType.str, "ipv4-unnumbered")

                                self.ipv4mtu = YLeaf(YType.uint32, "ipv4mtu")

                                self.is_interworking_functionality = YLeaf(YType.boolean, "is-interworking-functionality")

                                self.max_data_rate_downstream = YLeaf(YType.uint32, "max-data-rate-downstream")

                                self.max_data_rate_upstream = YLeaf(YType.uint32, "max-data-rate-upstream")

                                self.max_interleaving_delay_downstream = YLeaf(YType.uint32, "max-interleaving-delay-downstream")

                                self.max_interleaving_delay_upstream = YLeaf(YType.uint32, "max-interleaving-delay-upstream")

                                self.min_data_rate_downstream = YLeaf(YType.uint32, "min-data-rate-downstream")

                                self.min_data_rate_downstream_low_power = YLeaf(YType.uint32, "min-data-rate-downstream-low-power")

                                self.min_data_rate_upstream_low_power = YLeaf(YType.uint32, "min-data-rate-upstream-low-power")

                                self.parent_interface_name = YLeaf(YType.str, "parent-interface-name")

                                self.pool_address = YLeaf(YType.str, "pool-address")

                                self.primary_dns_server_address = YLeaf(YType.str, "primary-dns-server-address")

                                self.primary_net_bios_server_address = YLeaf(YType.str, "primary-net-bios-server-address")

                                self.remote_id = YLeaf(YType.str, "remote-id")

                                self.route = YLeaf(YType.str, "route")

                                self.secondary_dns_server_address = YLeaf(YType.str, "secondary-dns-server-address")

                                self.secondary_net_bios_server_address = YLeaf(YType.str, "secondary-net-bios-server-address")

                                self.session_termination_cause = YLeaf(YType.enumeration, "session-termination-cause")

                                self.session_timeout = YLeaf(YType.uint32, "session-timeout")

                                self.strict_rpf_packets = YLeaf(YType.uint32, "strict-rpf-packets")

                                self.tunnel_client_authentication_id = YLeaf(YType.str, "tunnel-client-authentication-id")

                                self.tunnel_client_endpoint = YLeaf(YType.str, "tunnel-client-endpoint")

                                self.tunnel_medium = YLeaf(YType.enumeration, "tunnel-medium")

                                self.tunnel_preference = YLeaf(YType.uint32, "tunnel-preference")

                                self.tunnel_protocol = YLeaf(YType.enumeration, "tunnel-protocol")

                                self.tunnel_server_endpoint = YLeaf(YType.str, "tunnel-server-endpoint")

                                self.tunnel_tos_setting = YLeaf(YType.uint32, "tunnel-tos-setting")

                                self.upstream_parameterized_qos_policy = YLeaf(YType.str, "upstream-parameterized-qos-policy")

                                self.upstream_qos_policy = YLeaf(YType.str, "upstream-qos-policy")
                                self._segment_path = lambda: "user-profile-attributes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Sessions.Session.UserProfileAttributes, ['accounting_session_id', 'actual_data_rate_downstream', 'actual_data_rate_upstream', 'attainable_data_rate_downstream', 'attainable_data_rate_upstream', 'authorization_service_type', 'circuit_id', 'connection_receive_speed', 'connection_transmission_speed', 'destination_station_id', 'downstream_parameterized_qos_policy', 'downstream_qos_policy', 'egress_access_list', 'formatted_calling_station_id', 'ingress_access_list', 'interface_name', 'interface_type', 'interim_accounting_interval', 'ip_netmask', 'ipv4_unnumbered', 'ipv4mtu', 'is_interworking_functionality', 'max_data_rate_downstream', 'max_data_rate_upstream', 'max_interleaving_delay_downstream', 'max_interleaving_delay_upstream', 'min_data_rate_downstream', 'min_data_rate_downstream_low_power', 'min_data_rate_upstream_low_power', 'parent_interface_name', 'pool_address', 'primary_dns_server_address', 'primary_net_bios_server_address', 'remote_id', 'route', 'secondary_dns_server_address', 'secondary_net_bios_server_address', 'session_termination_cause', 'session_timeout', 'strict_rpf_packets', 'tunnel_client_authentication_id', 'tunnel_client_endpoint', 'tunnel_medium', 'tunnel_preference', 'tunnel_protocol', 'tunnel_server_endpoint', 'tunnel_tos_setting', 'upstream_parameterized_qos_policy', 'upstream_qos_policy'], name, value)


                class StateSummaries(Entity):
                    """
                    Summary information filtered by session state
                    
                    .. attribute:: state_summary
                    
                    	State summary
                    	**type**\: list of    :py:class:`StateSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary>`
                    
                    

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
                        	**type**\:   :py:class:`SubscriberStateFilterFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberStateFilterFlag>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary, self).__init__()

                            self.yang_name = "state-summary"
                            self.yang_parent_name = "state-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr)}
                            self._child_list_classes = {}

                            self.state = YLeaf(YType.enumeration, "state")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "state-summary" + "[state='" + self.state.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary, ['state'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "state-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "state-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class Summary(Entity):
                    """
                    Subscriber session summary information
                    
                    .. attribute:: address_family_xr
                    
                    	Address family summary
                    	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr>`
                    
                    .. attribute:: state_xr
                    
                    	State summary
                    	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Subscriber.Session.Nodes.Node.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.Summary.StateXr)}
                        self._child_list_classes = {}

                        self.address_family_xr = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr()
                        self.address_family_xr.parent = self
                        self._children_name_map["address_family_xr"] = "address-family-xr"
                        self._children_yang_names.add("address-family-xr")

                        self.state_xr = Subscriber.Session.Nodes.Node.Summary.StateXr()
                        self.state_xr.parent = self
                        self._children_name_map["state_xr"] = "state-xr"
                        self._children_yang_names.add("state-xr")
                        self._segment_path = lambda: "summary"


                    class AddressFamilyXr(Entity):
                        """
                        Address family summary
                        
                        .. attribute:: ip_subscriber_dhcp
                        
                        	IP subscriber DHCP summary
                        	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp>`
                        
                        .. attribute:: ip_subscriber_packet
                        
                        	IP subscriber packet summary
                        	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket>`
                        
                        .. attribute:: pppoe
                        
                        	PPPoE summary
                        	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr, self).__init__()

                            self.yang_name = "address-family-xr"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe)}
                            self._child_list_classes = {}

                            self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp()
                            self.ip_subscriber_dhcp.parent = self
                            self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                            self._children_yang_names.add("ip-subscriber-dhcp")

                            self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket()
                            self.ip_subscriber_packet.parent = self
                            self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                            self._children_yang_names.add("ip-subscriber-packet")

                            self.pppoe = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe()
                            self.pppoe.parent = self
                            self._children_name_map["pppoe"] = "pppoe"
                            self._children_yang_names.add("pppoe")
                            self._segment_path = lambda: "address-family-xr"


                        class IpSubscriberDhcp(Entity):
                            """
                            IP subscriber DHCP summary
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\:  int
                            
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

                                self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                self._segment_path = lambda: "ip-subscriber-dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class IpSubscriberPacket(Entity):
                            """
                            IP subscriber packet summary
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\:  int
                            
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

                                self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                self._segment_path = lambda: "ip-subscriber-packet"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class Pppoe(Entity):
                            """
                            PPPoE summary
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\:  int
                            
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

                                self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                self._segment_path = lambda: "pppoe"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                    class StateXr(Entity):
                        """
                        State summary
                        
                        .. attribute:: ip_subscriber_dhcp
                        
                        	IP subscriber DHCP summary
                        	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp>`
                        
                        .. attribute:: ip_subscriber_packet
                        
                        	IP subscriber packet summary
                        	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket>`
                        
                        .. attribute:: pppoe
                        
                        	PPPoE summary
                        	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.Summary.StateXr, self).__init__()

                            self.yang_name = "state-xr"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe)}
                            self._child_list_classes = {}

                            self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp()
                            self.ip_subscriber_dhcp.parent = self
                            self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                            self._children_yang_names.add("ip-subscriber-dhcp")

                            self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket()
                            self.ip_subscriber_packet.parent = self
                            self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                            self._children_yang_names.add("ip-subscriber-packet")

                            self.pppoe = Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe()
                            self.pppoe.parent = self
                            self._children_name_map["pppoe"] = "pppoe"
                            self._children_yang_names.add("pppoe")
                            self._segment_path = lambda: "state-xr"


                        class IpSubscriberDhcp(Entity):
                            """
                            IP subscriber DHCP summary
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\:  int
                            
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

                                self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                self._segment_path = lambda: "ip-subscriber-dhcp"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                        class IpSubscriberPacket(Entity):
                            """
                            IP subscriber packet summary
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\:  int
                            
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

                                self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                self._segment_path = lambda: "ip-subscriber-packet"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                        class Pppoe(Entity):
                            """
                            PPPoE summary
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\:  int
                            
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

                                self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                self._segment_path = lambda: "pppoe"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class UsernameSummaries(Entity):
                    """
                    Summary information filtered by username
                    
                    .. attribute:: username_summary
                    
                    	Username summary
                    	**type**\: list of    :py:class:`UsernameSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary>`
                    
                    

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
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary, self).__init__()

                            self.yang_name = "username-summary"
                            self.yang_parent_name = "username-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr)}
                            self._child_list_classes = {}

                            self.username = YLeaf(YType.str, "username")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "username-summary" + "[username='" + self.username.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary, ['username'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "username-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "username-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                class VrfSummaries(Entity):
                    """
                    Summary information filtered by VRF
                    
                    .. attribute:: vrf_summary
                    
                    	VRF summary
                    	**type**\: list of    :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary>`
                    
                    

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
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary, self).__init__()

                            self.yang_name = "vrf-summary"
                            self.yang_parent_name = "vrf-summaries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"address-family-xr" : ("address_family_xr", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr), "state-xr" : ("state_xr", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr)}
                            self._child_list_classes = {}

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.address_family_xr = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self._children_name_map["address_family_xr"] = "address-family-xr"
                            self._children_yang_names.add("address-family-xr")

                            self.state_xr = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr()
                            self.state_xr.parent = self
                            self._children_name_map["state_xr"] = "state-xr"
                            self._children_yang_names.add("state-xr")
                            self._segment_path = lambda: "vrf-summary" + "[vrf-name='" + self.vrf_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary, ['vrf_name'], name, value)


                        class AddressFamilyXr(Entity):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr, self).__init__()

                                self.yang_name = "address-family-xr"
                                self.yang_parent_name = "vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "address-family-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
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

                                    self.dual_part_up_sessions = YLeaf(YType.uint32, "dual-part-up-sessions")

                                    self.dual_up_sessions = YLeaf(YType.uint32, "dual-up-sessions")

                                    self.in_progress_sessions = YLeaf(YType.uint32, "in-progress-sessions")

                                    self.ipv4_only_sessions = YLeaf(YType.uint32, "ipv4-only-sessions")

                                    self.ipv6_only_sessions = YLeaf(YType.uint32, "ipv6-only-sessions")

                                    self.lac_sessions = YLeaf(YType.uint32, "lac-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe, ['dual_part_up_sessions', 'dual_up_sessions', 'in_progress_sessions', 'ipv4_only_sessions', 'ipv6_only_sessions', 'lac_sessions'], name, value)


                        class StateXr(Entity):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr, self).__init__()

                                self.yang_name = "state-xr"
                                self.yang_parent_name = "vrf-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ip-subscriber-dhcp" : ("ip_subscriber_dhcp", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp), "ip-subscriber-packet" : ("ip_subscriber_packet", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket), "pppoe" : ("pppoe", Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe)}
                                self._child_list_classes = {}

                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self._children_name_map["ip_subscriber_dhcp"] = "ip-subscriber-dhcp"
                                self._children_yang_names.add("ip-subscriber-dhcp")

                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self._children_name_map["ip_subscriber_packet"] = "ip-subscriber-packet"
                                self._children_yang_names.add("ip-subscriber-packet")

                                self.pppoe = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe()
                                self.pppoe.parent = self
                                self._children_name_map["pppoe"] = "pppoe"
                                self._children_yang_names.add("pppoe")
                                self._segment_path = lambda: "state-xr"


                            class IpSubscriberDhcp(Entity):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-dhcp"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class IpSubscriberPacket(Entity):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "ip-subscriber-packet"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)


                            class Pppoe(Entity):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
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

                                    self.activated_sessions = YLeaf(YType.uint32, "activated-sessions")

                                    self.connected_sessions = YLeaf(YType.uint32, "connected-sessions")

                                    self.connecting_sessions = YLeaf(YType.uint32, "connecting-sessions")

                                    self.disconnecting_sessions = YLeaf(YType.uint32, "disconnecting-sessions")

                                    self.end_sessions = YLeaf(YType.uint32, "end-sessions")

                                    self.idle_sessions = YLeaf(YType.uint32, "idle-sessions")

                                    self.initialized_sessions = YLeaf(YType.uint32, "initialized-sessions")
                                    self._segment_path = lambda: "pppoe"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe, ['activated_sessions', 'connected_sessions', 'connecting_sessions', 'disconnecting_sessions', 'end_sessions', 'idle_sessions', 'initialized_sessions'], name, value)

    def clone_ptr(self):
        self._top_entity = Subscriber()
        return self._top_entity

