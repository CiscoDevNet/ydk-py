""" Cisco_IOS_XR_tunnel_vpdn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package operational data.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LsgStatus(Enum):
    """
    LsgStatus

    LSG Status

    .. data:: none = 0

    	Member not initialized.

    .. data:: active = 1

    	Member is active.

    .. data:: down = 2

    	Member is down, cannot create new sessions.

    .. data:: testable = 3

    	Member is ready for new sessions.

    .. data:: testing = 4

    	Member is being tested for new session

    """

    none = Enum.YLeaf(0, "none")

    active = Enum.YLeaf(1, "active")

    down = Enum.YLeaf(2, "down")

    testable = Enum.YLeaf(3, "testable")

    testing = Enum.YLeaf(4, "testing")


class SessionState(Enum):
    """
    SessionState

    Session states

    .. data:: idle = 0

    	Idle state

    .. data:: connected = 1

    	Connected state

    .. data:: established = 2

    	Established state

    """

    idle = Enum.YLeaf(0, "idle")

    connected = Enum.YLeaf(1, "connected")

    established = Enum.YLeaf(2, "established")


class TosMode(Enum):
    """
    TosMode

    TOS modes

    .. data:: default = 0

    	default

    .. data:: set = 1

    	set

    .. data:: reflect = 2

    	reflect

    """

    default = Enum.YLeaf(0, "default")

    set = Enum.YLeaf(1, "set")

    reflect = Enum.YLeaf(2, "reflect")


class VpdnFailcode(Enum):
    """
    VpdnFailcode

    VPDN failure types

    .. data:: unknown = 0

    	Unknown

    .. data:: peer_action = 1

    	Peer action

    .. data:: authentication = 2

    	Authentication

    .. data:: authentication_error = 3

    	Authentication

    .. data:: authentication_failed = 4

    	Authentication

    .. data:: authorization = 5

    	Authorization

    .. data:: authorization_failed = 6

    	Authorization

    .. data:: home_gatewayfailure = 7

    	No resources available

    .. data:: connection_termination = 8

    	Connection termination

    .. data:: no_resources_available = 9

    	No resources available

    .. data:: timer_expiry = 10

    	Timer expiry

    .. data:: session_mid_exceeded = 11

    	Session limit

    .. data:: soft_shut = 12

    	Softshut

    .. data:: session_limit_exceeded = 13

    	Session limit

    .. data:: administrative = 14

    	Administrative

    .. data:: link_failure = 15

    	Link failure

    .. data:: security = 16

    	Security

    .. data:: tunnel_in_resync = 17

    	Tunnel in HA resync

    .. data:: call_prarmeters = 18

    	Call parameters

    """

    unknown = Enum.YLeaf(0, "unknown")

    peer_action = Enum.YLeaf(1, "peer-action")

    authentication = Enum.YLeaf(2, "authentication")

    authentication_error = Enum.YLeaf(3, "authentication-error")

    authentication_failed = Enum.YLeaf(4, "authentication-failed")

    authorization = Enum.YLeaf(5, "authorization")

    authorization_failed = Enum.YLeaf(6, "authorization-failed")

    home_gatewayfailure = Enum.YLeaf(7, "home-gatewayfailure")

    connection_termination = Enum.YLeaf(8, "connection-termination")

    no_resources_available = Enum.YLeaf(9, "no-resources-available")

    timer_expiry = Enum.YLeaf(10, "timer-expiry")

    session_mid_exceeded = Enum.YLeaf(11, "session-mid-exceeded")

    soft_shut = Enum.YLeaf(12, "soft-shut")

    session_limit_exceeded = Enum.YLeaf(13, "session-limit-exceeded")

    administrative = Enum.YLeaf(14, "administrative")

    link_failure = Enum.YLeaf(15, "link-failure")

    security = Enum.YLeaf(16, "security")

    tunnel_in_resync = Enum.YLeaf(17, "tunnel-in-resync")

    call_prarmeters = Enum.YLeaf(18, "call-prarmeters")


class VpdnNasPort(Enum):
    """
    VpdnNasPort

    NAS port types

    .. data:: none = 0

    	None

    .. data:: primary = 1

    	Primary

    .. data:: bri = 2

    	BRI

    .. data:: serial = 3

    	Serial

    .. data:: asynchronous = 4

    	Asynchronous

    .. data:: vty = 5

    	VTY

    .. data:: atm = 6

    	Asynchronous transfer mode

    .. data:: ethernet = 7

    	Ethernet

    .. data:: ppp_atm = 8

    	PPP over ATM

    .. data:: pppoe_over_atm = 9

    	PPPoE over ATM

    .. data:: pppoe_over_ethernet = 10

    	PPPoE over Ethernet

    .. data:: pppoe_over_vlan = 11

    	PPPoE over VLAN

    .. data:: pppoe_over_q_in_q = 12

    	PPPoE over Q-in-Q

    .. data:: v120 = 13

    	 V120

    .. data:: v110 = 14

    	V110

    .. data:: piafs = 15

    	PIAFS

    .. data:: x75 = 16

    	X.75

    .. data:: ip_sec = 17

    	IPSec

    .. data:: other = 18

    	Other

    .. data:: virtual_pppoe_over_ethernet = 19

    	Virtual PPPoE over Ethernet

    .. data:: virtual_pppoe_over_vlan = 20

    	 Virtual PPPoE over VLAN

    .. data:: virtual_pppoe_over_q_in_q = 21

    	Virtual PPPoE over Q-in-Q

    .. data:: ipo_e_over_ethernet = 22

    	IPoE over Ethernet

    .. data:: ipo_e_over_vlan = 23

    	IPoE over VLAN

    .. data:: ipo_e_over_q_in_q = 24

    	IPoE over Q-in-Q

    .. data:: virtual_i_po_e_over_ethernet = 25

    	Virtual IPoE over ethernet

    .. data:: virtual_i_po_e_over_vlan = 26

    	Virtual IPoE over VLAN

    .. data:: virtual_i_po_e_over_q_in_q = 27

    	Virtual IPoE over Q-in-Q

    .. data:: unknown = 28

    	Unknown

    """

    none = Enum.YLeaf(0, "none")

    primary = Enum.YLeaf(1, "primary")

    bri = Enum.YLeaf(2, "bri")

    serial = Enum.YLeaf(3, "serial")

    asynchronous = Enum.YLeaf(4, "asynchronous")

    vty = Enum.YLeaf(5, "vty")

    atm = Enum.YLeaf(6, "atm")

    ethernet = Enum.YLeaf(7, "ethernet")

    ppp_atm = Enum.YLeaf(8, "ppp-atm")

    pppoe_over_atm = Enum.YLeaf(9, "pppoe-over-atm")

    pppoe_over_ethernet = Enum.YLeaf(10, "pppoe-over-ethernet")

    pppoe_over_vlan = Enum.YLeaf(11, "pppoe-over-vlan")

    pppoe_over_q_in_q = Enum.YLeaf(12, "pppoe-over-q-in-q")

    v120 = Enum.YLeaf(13, "v120")

    v110 = Enum.YLeaf(14, "v110")

    piafs = Enum.YLeaf(15, "piafs")

    x75 = Enum.YLeaf(16, "x75")

    ip_sec = Enum.YLeaf(17, "ip-sec")

    other = Enum.YLeaf(18, "other")

    virtual_pppoe_over_ethernet = Enum.YLeaf(19, "virtual-pppoe-over-ethernet")

    virtual_pppoe_over_vlan = Enum.YLeaf(20, "virtual-pppoe-over-vlan")

    virtual_pppoe_over_q_in_q = Enum.YLeaf(21, "virtual-pppoe-over-q-in-q")

    ipo_e_over_ethernet = Enum.YLeaf(22, "ipo-e-over-ethernet")

    ipo_e_over_vlan = Enum.YLeaf(23, "ipo-e-over-vlan")

    ipo_e_over_q_in_q = Enum.YLeaf(24, "ipo-e-over-q-in-q")

    virtual_i_po_e_over_ethernet = Enum.YLeaf(25, "virtual-i-po-e-over-ethernet")

    virtual_i_po_e_over_vlan = Enum.YLeaf(26, "virtual-i-po-e-over-vlan")

    virtual_i_po_e_over_q_in_q = Enum.YLeaf(27, "virtual-i-po-e-over-q-in-q")

    unknown = Enum.YLeaf(28, "unknown")


class VpdnState(Enum):
    """
    VpdnState

    Vpdn states

    .. data:: initial_state = 0

    	Initial state

    .. data:: init_sync_in_progress = 1

    	Initial Sync in progress

    .. data:: steady_state = 2

    	Initial Sync Done

    """

    initial_state = Enum.YLeaf(0, "initial-state")

    init_sync_in_progress = Enum.YLeaf(1, "init-sync-in-progress")

    steady_state = Enum.YLeaf(2, "steady-state")



class Vpdn(Entity):
    """
    VPDN operational data
    
    .. attribute:: history_failures
    
    	VPDN history failure list
    	**type**\:   :py:class:`HistoryFailures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.HistoryFailures>`
    
    .. attribute:: sessions
    
    	VPDN session list
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions>`
    
    .. attribute:: tunnel_destinations
    
    	VPDN tunnel Destinations
    	**type**\:   :py:class:`TunnelDestinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.TunnelDestinations>`
    
    .. attribute:: vpdn_mirroring
    
    	VPDN Mirroring Statistics
    	**type**\:   :py:class:`VpdnMirroring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring>`
    
    .. attribute:: vpdn_redundancy
    
    	Show VPDN Redundancy information
    	**type**\:   :py:class:`VpdnRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnRedundancy>`
    
    

    """

    _prefix = 'tunnel-vpdn-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Vpdn, self).__init__()
        self._top_entity = None

        self.yang_name = "vpdn"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-vpdn-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"history-failures" : ("history_failures", Vpdn.HistoryFailures), "sessions" : ("sessions", Vpdn.Sessions), "tunnel-destinations" : ("tunnel_destinations", Vpdn.TunnelDestinations), "vpdn-mirroring" : ("vpdn_mirroring", Vpdn.VpdnMirroring), "vpdn-redundancy" : ("vpdn_redundancy", Vpdn.VpdnRedundancy)}
        self._child_list_classes = {}

        self.history_failures = Vpdn.HistoryFailures()
        self.history_failures.parent = self
        self._children_name_map["history_failures"] = "history-failures"
        self._children_yang_names.add("history-failures")

        self.sessions = Vpdn.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")

        self.tunnel_destinations = Vpdn.TunnelDestinations()
        self.tunnel_destinations.parent = self
        self._children_name_map["tunnel_destinations"] = "tunnel-destinations"
        self._children_yang_names.add("tunnel-destinations")

        self.vpdn_mirroring = Vpdn.VpdnMirroring()
        self.vpdn_mirroring.parent = self
        self._children_name_map["vpdn_mirroring"] = "vpdn-mirroring"
        self._children_yang_names.add("vpdn-mirroring")

        self.vpdn_redundancy = Vpdn.VpdnRedundancy()
        self.vpdn_redundancy.parent = self
        self._children_name_map["vpdn_redundancy"] = "vpdn-redundancy"
        self._children_yang_names.add("vpdn-redundancy")
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn"


    class HistoryFailures(Entity):
        """
        VPDN history failure list
        
        .. attribute:: history_failure
        
        	VPDN history failure information
        	**type**\: list of    :py:class:`HistoryFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.HistoryFailures.HistoryFailure>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.HistoryFailures, self).__init__()

            self.yang_name = "history-failures"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"history-failure" : ("history_failure", Vpdn.HistoryFailures.HistoryFailure)}

            self.history_failure = YList(self)
            self._segment_path = lambda: "history-failures"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.HistoryFailures, [], name, value)


        class HistoryFailure(Entity):
            """
            VPDN history failure information
            
            .. attribute:: destination_address
            
            	NAS IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: domain_name
            
            	Domain name
            	**type**\:  str
            
            .. attribute:: error_repeat_count
            
            	Error repeat count
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: event_time
            
            	Event logged time in Ex\: Wed Aug  3 10\:28\:30 2011
            	**type**\:  str
            
            .. attribute:: failure_type
            
            	Failure type
            	**type**\:   :py:class:`VpdnFailcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnFailcode>`
            
            .. attribute:: home_gateway
            
            	Home gateway
            	**type**\:  str
            
            .. attribute:: local_client_id
            
            	Local client ID
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mid
            
            	VPDN user session ID
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: nas
            
            	Network access server
            	**type**\:  str
            
            .. attribute:: remote_client_id
            
            	Remote client ID
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: remote_name
            
            	Remote name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: source_address
            
            	Source IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: username
            
            	Username
            	**type**\:  str
            
            .. attribute:: username_xr
            
            	Authentication username
            	**type**\:  str
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.HistoryFailures.HistoryFailure, self).__init__()

                self.yang_name = "history-failure"
                self.yang_parent_name = "history-failures"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.destination_address = YLeaf(YType.str, "destination-address")

                self.domain_name = YLeaf(YType.str, "domain-name")

                self.error_repeat_count = YLeaf(YType.uint16, "error-repeat-count")

                self.event_time = YLeaf(YType.str, "event-time")

                self.failure_type = YLeaf(YType.enumeration, "failure-type")

                self.home_gateway = YLeaf(YType.str, "home-gateway")

                self.local_client_id = YLeaf(YType.uint16, "local-client-id")

                self.mid = YLeaf(YType.uint16, "mid")

                self.nas = YLeaf(YType.str, "nas")

                self.remote_client_id = YLeaf(YType.uint16, "remote-client-id")

                self.remote_name = YLeaf(YType.str, "remote-name")

                self.source_address = YLeaf(YType.str, "source-address")

                self.username = YLeaf(YType.str, "username")

                self.username_xr = YLeaf(YType.str, "username-xr")
                self._segment_path = lambda: "history-failure"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/history-failures/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.HistoryFailures.HistoryFailure, ['destination_address', 'domain_name', 'error_repeat_count', 'event_time', 'failure_type', 'home_gateway', 'local_client_id', 'mid', 'nas', 'remote_client_id', 'remote_name', 'source_address', 'username', 'username_xr'], name, value)


    class Sessions(Entity):
        """
        VPDN session list
        
        .. attribute:: session
        
        	 VPDN session information
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"session" : ("session", Vpdn.Sessions.Session)}

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.Sessions, [], name, value)


        class Session(Entity):
            """
             VPDN session information
            
            .. attribute:: session_label  <key>
            
            	Session label
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: configuration
            
            	Configuration data
            	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Configuration>`
            
            .. attribute:: l2tp
            
            	L2TP data
            	**type**\:   :py:class:`L2Tp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.L2Tp>`
            
            .. attribute:: parent_interface_name
            
            	Parent interface name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: session
            
            	Session data
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Session>`
            
            .. attribute:: setup_time
            
            	Time to setup session in sec\:msec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: subscriber
            
            	Subscriber data
            	**type**\:   :py:class:`Subscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Subscriber>`
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"configuration" : ("configuration", Vpdn.Sessions.Session.Configuration), "l2tp" : ("l2tp", Vpdn.Sessions.Session.L2Tp), "session" : ("session", Vpdn.Sessions.Session.Session), "subscriber" : ("subscriber", Vpdn.Sessions.Session.Subscriber)}
                self._child_list_classes = {}

                self.session_label = YLeaf(YType.str, "session-label")

                self.parent_interface_name = YLeaf(YType.str, "parent-interface-name")

                self.setup_time = YLeaf(YType.uint32, "setup-time")

                self.configuration = Vpdn.Sessions.Session.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
                self._children_yang_names.add("configuration")

                self.l2tp = Vpdn.Sessions.Session.L2Tp()
                self.l2tp.parent = self
                self._children_name_map["l2tp"] = "l2tp"
                self._children_yang_names.add("l2tp")

                self.session = Vpdn.Sessions.Session.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")

                self.subscriber = Vpdn.Sessions.Session.Subscriber()
                self.subscriber.parent = self
                self._children_name_map["subscriber"] = "subscriber"
                self._children_yang_names.add("subscriber")
                self._segment_path = lambda: "session" + "[session-label='" + self.session_label.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/sessions/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.Sessions.Session, ['session_label', 'parent_interface_name', 'setup_time'], name, value)


            class Configuration(Entity):
                """
                Configuration data
                
                .. attribute:: dsl_line_forwarding
                
                	True if DSL line info forwarding is enabled
                	**type**\:  bool
                
                .. attribute:: l2tp_busy_timeout
                
                	L2TP busy timeout in seconds
                	**type**\:  int
                
                	**range:** 0..65535
                
                	**units**\: second
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                .. attribute:: tos
                
                	TOS setting value
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: tos_mode
                
                	TOS mode
                	**type**\:   :py:class:`TosMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.TosMode>`
                
                .. attribute:: vpn_id
                
                	VPN ID
                	**type**\:   :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Configuration.VpnId>`
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\:  str
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"vpn-id" : ("vpn_id", Vpdn.Sessions.Session.Configuration.VpnId)}
                    self._child_list_classes = {}

                    self.dsl_line_forwarding = YLeaf(YType.boolean, "dsl-line-forwarding")

                    self.l2tp_busy_timeout = YLeaf(YType.uint16, "l2tp-busy-timeout")

                    self.template_name = YLeaf(YType.str, "template-name")

                    self.tos = YLeaf(YType.uint8, "tos")

                    self.tos_mode = YLeaf(YType.enumeration, "tos-mode")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.vpn_id = Vpdn.Sessions.Session.Configuration.VpnId()
                    self.vpn_id.parent = self
                    self._children_name_map["vpn_id"] = "vpn-id"
                    self._children_yang_names.add("vpn-id")
                    self._segment_path = lambda: "configuration"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.Configuration, ['dsl_line_forwarding', 'l2tp_busy_timeout', 'template_name', 'tos', 'tos_mode', 'vrf_name'], name, value)


                class VpnId(Entity):
                    """
                    VPN ID
                    
                    .. attribute:: index
                    
                    	Index
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: oui
                    
                    	OUI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vpdn.Sessions.Session.Configuration.VpnId, self).__init__()

                        self.yang_name = "vpn-id"
                        self.yang_parent_name = "configuration"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.index = YLeaf(YType.uint32, "index")

                        self.oui = YLeaf(YType.uint32, "oui")
                        self._segment_path = lambda: "vpn-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Sessions.Session.Configuration.VpnId, ['index', 'oui'], name, value)


            class L2Tp(Entity):
                """
                L2TP data
                
                .. attribute:: call_serial_number
                
                	Call serial number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_l2tp_class_attribute_mask_set
                
                	True if L2TP class attribute mask is set
                	**type**\:  bool
                
                .. attribute:: is_tunnel_authentication_enabled
                
                	True if tunnel authentication is enabled
                	**type**\:  bool
                
                .. attribute:: local_endpoint
                
                	Local endpoint IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: local_session_id
                
                	Local session ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: local_tunnel_id
                
                	Local tunnel ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: remote_endpoint
                
                	Remote endpoint IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_port
                
                	Remote port
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: remote_session_id
                
                	Remote session ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: remote_tunnel_id
                
                	Remote tunnel ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: tunnel_assignment_id
                
                	Tunnel assignment ID
                	**type**\:  str
                
                .. attribute:: tunnel_client_authentication_id
                
                	Tunnel client authentication ID
                	**type**\:  str
                
                .. attribute:: tunnel_server_authentication_id
                
                	Tunnel server authentication ID
                	**type**\:  str
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.L2Tp, self).__init__()

                    self.yang_name = "l2tp"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.call_serial_number = YLeaf(YType.uint32, "call-serial-number")

                    self.is_l2tp_class_attribute_mask_set = YLeaf(YType.boolean, "is-l2tp-class-attribute-mask-set")

                    self.is_tunnel_authentication_enabled = YLeaf(YType.boolean, "is-tunnel-authentication-enabled")

                    self.local_endpoint = YLeaf(YType.str, "local-endpoint")

                    self.local_session_id = YLeaf(YType.uint16, "local-session-id")

                    self.local_tunnel_id = YLeaf(YType.uint16, "local-tunnel-id")

                    self.remote_endpoint = YLeaf(YType.str, "remote-endpoint")

                    self.remote_port = YLeaf(YType.uint16, "remote-port")

                    self.remote_session_id = YLeaf(YType.uint16, "remote-session-id")

                    self.remote_tunnel_id = YLeaf(YType.uint16, "remote-tunnel-id")

                    self.tunnel_assignment_id = YLeaf(YType.str, "tunnel-assignment-id")

                    self.tunnel_client_authentication_id = YLeaf(YType.str, "tunnel-client-authentication-id")

                    self.tunnel_server_authentication_id = YLeaf(YType.str, "tunnel-server-authentication-id")
                    self._segment_path = lambda: "l2tp"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.L2Tp, ['call_serial_number', 'is_l2tp_class_attribute_mask_set', 'is_tunnel_authentication_enabled', 'local_endpoint', 'local_session_id', 'local_tunnel_id', 'remote_endpoint', 'remote_port', 'remote_session_id', 'remote_tunnel_id', 'tunnel_assignment_id', 'tunnel_client_authentication_id', 'tunnel_server_authentication_id'], name, value)


            class Session(Entity):
                """
                Session data
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\:  str
                
                .. attribute:: interface_name
                
                	Session interface name
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: l2tp_session_id
                
                	L2TP session ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: l2tp_tunnel_id
                
                	L2TP tunnel ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: last_change
                
                	Elapsed time since last change in hh\:mm\:ss format
                	**type**\:  str
                
                .. attribute:: srg_slave
                
                	Session SRG Slave
                	**type**\:  bool
                
                .. attribute:: state
                
                	Session state
                	**type**\:   :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.SessionState>`
                
                .. attribute:: username
                
                	Authentication username
                	**type**\:  str
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.domain_name = YLeaf(YType.str, "domain-name")

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.l2tp_session_id = YLeaf(YType.uint16, "l2tp-session-id")

                    self.l2tp_tunnel_id = YLeaf(YType.uint16, "l2tp-tunnel-id")

                    self.last_change = YLeaf(YType.str, "last-change")

                    self.srg_slave = YLeaf(YType.boolean, "srg-slave")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.username = YLeaf(YType.str, "username")
                    self._segment_path = lambda: "session"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.Session, ['domain_name', 'interface_name', 'l2tp_session_id', 'l2tp_tunnel_id', 'last_change', 'srg_slave', 'state', 'username'], name, value)


            class Subscriber(Entity):
                """
                Subscriber data
                
                .. attribute:: nas_port
                
                	NAS port ID
                	**type**\:  list of int
                
                	**range:** 0..255
                
                .. attribute:: nas_port_type
                
                	NAS port type
                	**type**\:   :py:class:`VpdnNasPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnNasPort>`
                
                .. attribute:: physical_channel_id
                
                	Physical channel ID
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_connect_speed
                
                	Receive connect speed in nanoseconds
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: nanosecond
                
                .. attribute:: transmit_connect_speed
                
                	Transmit connect speed in nanoseconds
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: nanosecond
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.Subscriber, self).__init__()

                    self.yang_name = "subscriber"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.nas_port = YLeafList(YType.uint8, "nas-port")

                    self.nas_port_type = YLeaf(YType.enumeration, "nas-port-type")

                    self.physical_channel_id = YLeaf(YType.uint32, "physical-channel-id")

                    self.receive_connect_speed = YLeaf(YType.uint64, "receive-connect-speed")

                    self.transmit_connect_speed = YLeaf(YType.uint64, "transmit-connect-speed")
                    self._segment_path = lambda: "subscriber"

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.Subscriber, ['nas_port', 'nas_port_type', 'physical_channel_id', 'receive_connect_speed', 'transmit_connect_speed'], name, value)


    class TunnelDestinations(Entity):
        """
        VPDN tunnel Destinations
        
        .. attribute:: tunnel_destination
        
        	VPDN tunnel destination information
        	**type**\: list of    :py:class:`TunnelDestination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.TunnelDestinations.TunnelDestination>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.TunnelDestinations, self).__init__()

            self.yang_name = "tunnel-destinations"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tunnel-destination" : ("tunnel_destination", Vpdn.TunnelDestinations.TunnelDestination)}

            self.tunnel_destination = YList(self)
            self._segment_path = lambda: "tunnel-destinations"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.TunnelDestinations, [], name, value)


        class TunnelDestination(Entity):
            """
            VPDN tunnel destination information
            
            .. attribute:: address
            
            	IP address
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: connects
            
            	Total count of tunnels connected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnects
            
            	Total count of tunnels disconnected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: load
            
            	Current load on LNS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: retry
            
            	Retries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: status
            
            	Status of LNS
            	**type**\:   :py:class:`LsgStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.LsgStatus>`
            
            .. attribute:: status_change_time
            
            	Seconds since last status change
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: vrf_name_xr
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.TunnelDestinations.TunnelDestination, self).__init__()

                self.yang_name = "tunnel-destination"
                self.yang_parent_name = "tunnel-destinations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.address = YLeaf(YType.str, "address")

                self.connects = YLeaf(YType.uint32, "connects")

                self.disconnects = YLeaf(YType.uint32, "disconnects")

                self.load = YLeaf(YType.uint32, "load")

                self.retry = YLeaf(YType.uint32, "retry")

                self.status = YLeaf(YType.enumeration, "status")

                self.status_change_time = YLeaf(YType.uint32, "status-change-time")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")
                self._segment_path = lambda: "tunnel-destination"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/tunnel-destinations/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.TunnelDestinations.TunnelDestination, ['address', 'connects', 'disconnects', 'load', 'retry', 'status', 'status_change_time', 'vrf_name', 'vrf_name_xr'], name, value)


    class VpdnMirroring(Entity):
        """
        VPDN Mirroring Statistics
        
        .. attribute:: alloc_cnt
        
        	alloc cnt
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: alloc_err_cnt
        
        	alloc err cnt
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: qad_recv_stats
        
        	qad recv stats
        	**type**\:   :py:class:`QadRecvStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadRecvStats>`
        
        .. attribute:: qad_recv_stats_last_clear
        
        	qad recv stats last clear
        	**type**\:   :py:class:`QadRecvStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadRecvStatsLastClear>`
        
        .. attribute:: qad_send_stats
        
        	qad send stats
        	**type**\:   :py:class:`QadSendStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadSendStats>`
        
        .. attribute:: qad_send_stats_last_clear
        
        	qad send stats last clear
        	**type**\:   :py:class:`QadSendStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadSendStatsLastClear>`
        
        .. attribute:: sso_batch_err_cnt
        
        	sso batch err cnt
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: sso_err_cnt
        
        	sso err cnt
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: sync_not_conn_cnt
        
        	sync not conn cnt
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.VpdnMirroring, self).__init__()

            self.yang_name = "vpdn-mirroring"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"qad-recv-stats" : ("qad_recv_stats", Vpdn.VpdnMirroring.QadRecvStats), "qad-recv-stats-last-clear" : ("qad_recv_stats_last_clear", Vpdn.VpdnMirroring.QadRecvStatsLastClear), "qad-send-stats" : ("qad_send_stats", Vpdn.VpdnMirroring.QadSendStats), "qad-send-stats-last-clear" : ("qad_send_stats_last_clear", Vpdn.VpdnMirroring.QadSendStatsLastClear)}
            self._child_list_classes = {}

            self.alloc_cnt = YLeaf(YType.uint32, "alloc-cnt")

            self.alloc_err_cnt = YLeaf(YType.uint32, "alloc-err-cnt")

            self.sso_batch_err_cnt = YLeaf(YType.uint32, "sso-batch-err-cnt")

            self.sso_err_cnt = YLeaf(YType.uint32, "sso-err-cnt")

            self.sync_not_conn_cnt = YLeaf(YType.uint32, "sync-not-conn-cnt")

            self.qad_recv_stats = Vpdn.VpdnMirroring.QadRecvStats()
            self.qad_recv_stats.parent = self
            self._children_name_map["qad_recv_stats"] = "qad-recv-stats"
            self._children_yang_names.add("qad-recv-stats")

            self.qad_recv_stats_last_clear = Vpdn.VpdnMirroring.QadRecvStatsLastClear()
            self.qad_recv_stats_last_clear.parent = self
            self._children_name_map["qad_recv_stats_last_clear"] = "qad-recv-stats-last-clear"
            self._children_yang_names.add("qad-recv-stats-last-clear")

            self.qad_send_stats = Vpdn.VpdnMirroring.QadSendStats()
            self.qad_send_stats.parent = self
            self._children_name_map["qad_send_stats"] = "qad-send-stats"
            self._children_yang_names.add("qad-send-stats")

            self.qad_send_stats_last_clear = Vpdn.VpdnMirroring.QadSendStatsLastClear()
            self.qad_send_stats_last_clear.parent = self
            self._children_name_map["qad_send_stats_last_clear"] = "qad-send-stats-last-clear"
            self._children_yang_names.add("qad-send-stats-last-clear")
            self._segment_path = lambda: "vpdn-mirroring"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.VpdnMirroring, ['alloc_cnt', 'alloc_err_cnt', 'sso_batch_err_cnt', 'sso_err_cnt', 'sync_not_conn_cnt'], name, value)


        class QadRecvStats(Entity):
            """
            qad recv stats
            
            .. attribute:: acks_recvd
            
            	acks recvd
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: init_drops
            
            	init drops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msg_drops
            
            	msg drops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msgs_recvd
            
            	msgs recvd
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ooo_drops
            
            	ooo drops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: recvd_acks_failed
            
            	recvd acks failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: stale_msgs
            
            	stale msgs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.VpdnMirroring.QadRecvStats, self).__init__()

                self.yang_name = "qad-recv-stats"
                self.yang_parent_name = "vpdn-mirroring"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.acks_recvd = YLeaf(YType.uint32, "acks-recvd")

                self.init_drops = YLeaf(YType.uint32, "init-drops")

                self.msg_drops = YLeaf(YType.uint32, "msg-drops")

                self.msgs_recvd = YLeaf(YType.uint32, "msgs-recvd")

                self.ooo_drops = YLeaf(YType.uint32, "ooo-drops")

                self.recvd_acks_failed = YLeaf(YType.uint32, "recvd-acks-failed")

                self.stale_msgs = YLeaf(YType.uint32, "stale-msgs")
                self._segment_path = lambda: "qad-recv-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadRecvStats, ['acks_recvd', 'init_drops', 'msg_drops', 'msgs_recvd', 'ooo_drops', 'recvd_acks_failed', 'stale_msgs'], name, value)


        class QadRecvStatsLastClear(Entity):
            """
            qad recv stats last clear
            
            .. attribute:: acks_recvd
            
            	acks recvd
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: init_drops
            
            	init drops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msg_drops
            
            	msg drops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msgs_recvd
            
            	msgs recvd
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ooo_drops
            
            	ooo drops
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: recvd_acks_failed
            
            	recvd acks failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: stale_msgs
            
            	stale msgs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.VpdnMirroring.QadRecvStatsLastClear, self).__init__()

                self.yang_name = "qad-recv-stats-last-clear"
                self.yang_parent_name = "vpdn-mirroring"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.acks_recvd = YLeaf(YType.uint32, "acks-recvd")

                self.init_drops = YLeaf(YType.uint32, "init-drops")

                self.msg_drops = YLeaf(YType.uint32, "msg-drops")

                self.msgs_recvd = YLeaf(YType.uint32, "msgs-recvd")

                self.ooo_drops = YLeaf(YType.uint32, "ooo-drops")

                self.recvd_acks_failed = YLeaf(YType.uint32, "recvd-acks-failed")

                self.stale_msgs = YLeaf(YType.uint32, "stale-msgs")
                self._segment_path = lambda: "qad-recv-stats-last-clear"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadRecvStatsLastClear, ['acks_recvd', 'init_drops', 'msg_drops', 'msgs_recvd', 'ooo_drops', 'recvd_acks_failed', 'stale_msgs'], name, value)


        class QadSendStats(Entity):
            """
            qad send stats
            
            .. attribute:: acks_failed
            
            	acks failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_sent
            
            	acks sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msgs_sent
            
            	msgs sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_partner
            
            	no partner
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pending_acks
            
            	pending acks
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_ack_count
            
            	qad ack count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_frag_count
            
            	qad frag count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_last_seq_number
            
            	qad last seq number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_count
            
            	qad rx count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_first_seq_number
            
            	qad rx first seq number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_count
            
            	qad rx list count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_q_size
            
            	qad rx list q size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_timeouts
            
            	qad timeouts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_unknown_acks
            
            	qad unknown acks
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: resumes
            
            	resumes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_failed
            
            	sends failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_fragment
            
            	sends fragment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: suspends
            
            	suspends
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: timeouts
            
            	timeouts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.VpdnMirroring.QadSendStats, self).__init__()

                self.yang_name = "qad-send-stats"
                self.yang_parent_name = "vpdn-mirroring"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.acks_failed = YLeaf(YType.uint32, "acks-failed")

                self.acks_sent = YLeaf(YType.uint32, "acks-sent")

                self.msgs_sent = YLeaf(YType.uint32, "msgs-sent")

                self.no_partner = YLeaf(YType.uint32, "no-partner")

                self.pending_acks = YLeaf(YType.uint32, "pending-acks")

                self.qad_ack_count = YLeaf(YType.uint32, "qad-ack-count")

                self.qad_frag_count = YLeaf(YType.uint32, "qad-frag-count")

                self.qad_last_seq_number = YLeaf(YType.uint32, "qad-last-seq-number")

                self.qad_rx_count = YLeaf(YType.uint32, "qad-rx-count")

                self.qad_rx_first_seq_number = YLeaf(YType.uint32, "qad-rx-first-seq-number")

                self.qad_rx_list_count = YLeaf(YType.uint32, "qad-rx-list-count")

                self.qad_rx_list_q_size = YLeaf(YType.uint32, "qad-rx-list-q-size")

                self.qad_timeouts = YLeaf(YType.uint32, "qad-timeouts")

                self.qad_unknown_acks = YLeaf(YType.uint32, "qad-unknown-acks")

                self.resumes = YLeaf(YType.uint32, "resumes")

                self.sends_failed = YLeaf(YType.uint32, "sends-failed")

                self.sends_fragment = YLeaf(YType.uint32, "sends-fragment")

                self.suspends = YLeaf(YType.uint32, "suspends")

                self.timeouts = YLeaf(YType.uint32, "timeouts")
                self._segment_path = lambda: "qad-send-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadSendStats, ['acks_failed', 'acks_sent', 'msgs_sent', 'no_partner', 'pending_acks', 'qad_ack_count', 'qad_frag_count', 'qad_last_seq_number', 'qad_rx_count', 'qad_rx_first_seq_number', 'qad_rx_list_count', 'qad_rx_list_q_size', 'qad_timeouts', 'qad_unknown_acks', 'resumes', 'sends_failed', 'sends_fragment', 'suspends', 'timeouts'], name, value)


        class QadSendStatsLastClear(Entity):
            """
            qad send stats last clear
            
            .. attribute:: acks_failed
            
            	acks failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_sent
            
            	acks sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msgs_sent
            
            	msgs sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_partner
            
            	no partner
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pending_acks
            
            	pending acks
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_ack_count
            
            	qad ack count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_frag_count
            
            	qad frag count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_last_seq_number
            
            	qad last seq number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_count
            
            	qad rx count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_first_seq_number
            
            	qad rx first seq number
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_count
            
            	qad rx list count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_q_size
            
            	qad rx list q size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_timeouts
            
            	qad timeouts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_unknown_acks
            
            	qad unknown acks
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: resumes
            
            	resumes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_failed
            
            	sends failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_fragment
            
            	sends fragment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: suspends
            
            	suspends
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: timeouts
            
            	timeouts
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.VpdnMirroring.QadSendStatsLastClear, self).__init__()

                self.yang_name = "qad-send-stats-last-clear"
                self.yang_parent_name = "vpdn-mirroring"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.acks_failed = YLeaf(YType.uint32, "acks-failed")

                self.acks_sent = YLeaf(YType.uint32, "acks-sent")

                self.msgs_sent = YLeaf(YType.uint32, "msgs-sent")

                self.no_partner = YLeaf(YType.uint32, "no-partner")

                self.pending_acks = YLeaf(YType.uint32, "pending-acks")

                self.qad_ack_count = YLeaf(YType.uint32, "qad-ack-count")

                self.qad_frag_count = YLeaf(YType.uint32, "qad-frag-count")

                self.qad_last_seq_number = YLeaf(YType.uint32, "qad-last-seq-number")

                self.qad_rx_count = YLeaf(YType.uint32, "qad-rx-count")

                self.qad_rx_first_seq_number = YLeaf(YType.uint32, "qad-rx-first-seq-number")

                self.qad_rx_list_count = YLeaf(YType.uint32, "qad-rx-list-count")

                self.qad_rx_list_q_size = YLeaf(YType.uint32, "qad-rx-list-q-size")

                self.qad_timeouts = YLeaf(YType.uint32, "qad-timeouts")

                self.qad_unknown_acks = YLeaf(YType.uint32, "qad-unknown-acks")

                self.resumes = YLeaf(YType.uint32, "resumes")

                self.sends_failed = YLeaf(YType.uint32, "sends-failed")

                self.sends_fragment = YLeaf(YType.uint32, "sends-fragment")

                self.suspends = YLeaf(YType.uint32, "suspends")

                self.timeouts = YLeaf(YType.uint32, "timeouts")
                self._segment_path = lambda: "qad-send-stats-last-clear"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadSendStatsLastClear, ['acks_failed', 'acks_sent', 'msgs_sent', 'no_partner', 'pending_acks', 'qad_ack_count', 'qad_frag_count', 'qad_last_seq_number', 'qad_rx_count', 'qad_rx_first_seq_number', 'qad_rx_list_count', 'qad_rx_list_q_size', 'qad_timeouts', 'qad_unknown_acks', 'resumes', 'sends_failed', 'sends_fragment', 'suspends', 'timeouts'], name, value)


    class VpdnRedundancy(Entity):
        """
        Show VPDN Redundancy information
        
        .. attribute:: abort_time
        
        	abort time
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: finish_time
        
        	finish time
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: session_synced
        
        	session synced
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: session_total
        
        	session total
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: start_time
        
        	start time
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: state
        
        	state
        	**type**\:   :py:class:`VpdnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnState>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.VpdnRedundancy, self).__init__()

            self.yang_name = "vpdn-redundancy"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.abort_time = YLeaf(YType.uint64, "abort-time")

            self.finish_time = YLeaf(YType.uint64, "finish-time")

            self.session_synced = YLeaf(YType.uint32, "session-synced")

            self.session_total = YLeaf(YType.uint32, "session-total")

            self.start_time = YLeaf(YType.uint64, "start-time")

            self.state = YLeaf(YType.enumeration, "state")
            self._segment_path = lambda: "vpdn-redundancy"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.VpdnRedundancy, ['abort_time', 'finish_time', 'session_synced', 'session_total', 'start_time', 'state'], name, value)

    def clone_ptr(self):
        self._top_entity = Vpdn()
        return self._top_entity

