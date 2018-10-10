""" Cisco_IOS_XR_tunnel_vpdn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package operational data.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LsgStatus(Enum):
    """
    LsgStatus (Enum Class)

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
    SessionState (Enum Class)

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
    TosMode (Enum Class)

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
    VpdnFailcode (Enum Class)

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
    VpdnNasPort (Enum Class)

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
    VpdnState (Enum Class)

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
    
    .. attribute:: sessions
    
    	VPDN session list
    	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions>`
    
    .. attribute:: tunnel_destinations
    
    	VPDN tunnel Destinations
    	**type**\:  :py:class:`TunnelDestinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.TunnelDestinations>`
    
    .. attribute:: vpdn_mirroring
    
    	VPDN Mirroring Statistics
    	**type**\:  :py:class:`VpdnMirroring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring>`
    
    .. attribute:: vpdn_redundancy
    
    	Show VPDN Redundancy information
    	**type**\:  :py:class:`VpdnRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnRedundancy>`
    
    .. attribute:: history_failures
    
    	VPDN history failure list
    	**type**\:  :py:class:`HistoryFailures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.HistoryFailures>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("sessions", ("sessions", Vpdn.Sessions)), ("tunnel-destinations", ("tunnel_destinations", Vpdn.TunnelDestinations)), ("vpdn-mirroring", ("vpdn_mirroring", Vpdn.VpdnMirroring)), ("vpdn-redundancy", ("vpdn_redundancy", Vpdn.VpdnRedundancy)), ("history-failures", ("history_failures", Vpdn.HistoryFailures))])
        self._leafs = OrderedDict()

        self.sessions = Vpdn.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"

        self.tunnel_destinations = Vpdn.TunnelDestinations()
        self.tunnel_destinations.parent = self
        self._children_name_map["tunnel_destinations"] = "tunnel-destinations"

        self.vpdn_mirroring = Vpdn.VpdnMirroring()
        self.vpdn_mirroring.parent = self
        self._children_name_map["vpdn_mirroring"] = "vpdn-mirroring"

        self.vpdn_redundancy = Vpdn.VpdnRedundancy()
        self.vpdn_redundancy.parent = self
        self._children_name_map["vpdn_redundancy"] = "vpdn-redundancy"

        self.history_failures = Vpdn.HistoryFailures()
        self.history_failures.parent = self
        self._children_name_map["history_failures"] = "history-failures"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vpdn, [], name, value)


    class Sessions(Entity):
        """
        VPDN session list
        
        .. attribute:: session
        
        	 VPDN session information
        	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("session", ("session", Vpdn.Sessions.Session))])
            self._leafs = OrderedDict()

            self.session = YList(self)
            self._segment_path = lambda: "sessions"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.Sessions, [], name, value)


        class Session(Entity):
            """
             VPDN session information
            
            .. attribute:: session_label  (key)
            
            	Session label
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{1,8}
            
            .. attribute:: session
            
            	Session data
            	**type**\:  :py:class:`Session_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Session_>`
            
            .. attribute:: l2tp
            
            	L2TP data
            	**type**\:  :py:class:`L2tp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.L2tp>`
            
            .. attribute:: subscriber
            
            	Subscriber data
            	**type**\:  :py:class:`Subscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Subscriber>`
            
            .. attribute:: configuration
            
            	Configuration data
            	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Configuration>`
            
            .. attribute:: setup_time
            
            	Time to setup session in sec\:msec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: parent_interface_name
            
            	Parent interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['session_label']
                self._child_classes = OrderedDict([("session", ("session", Vpdn.Sessions.Session.Session_)), ("l2tp", ("l2tp", Vpdn.Sessions.Session.L2tp)), ("subscriber", ("subscriber", Vpdn.Sessions.Session.Subscriber)), ("configuration", ("configuration", Vpdn.Sessions.Session.Configuration))])
                self._leafs = OrderedDict([
                    ('session_label', (YLeaf(YType.str, 'session-label'), ['str'])),
                    ('setup_time', (YLeaf(YType.uint32, 'setup-time'), ['int'])),
                    ('parent_interface_name', (YLeaf(YType.str, 'parent-interface-name'), ['str'])),
                ])
                self.session_label = None
                self.setup_time = None
                self.parent_interface_name = None

                self.session = Vpdn.Sessions.Session.Session_()
                self.session.parent = self
                self._children_name_map["session"] = "session"

                self.l2tp = Vpdn.Sessions.Session.L2tp()
                self.l2tp.parent = self
                self._children_name_map["l2tp"] = "l2tp"

                self.subscriber = Vpdn.Sessions.Session.Subscriber()
                self.subscriber.parent = self
                self._children_name_map["subscriber"] = "subscriber"

                self.configuration = Vpdn.Sessions.Session.Configuration()
                self.configuration.parent = self
                self._children_name_map["configuration"] = "configuration"
                self._segment_path = lambda: "session" + "[session-label='" + str(self.session_label) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/sessions/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.Sessions.Session, ['session_label', u'setup_time', u'parent_interface_name'], name, value)


            class Session_(Entity):
                """
                Session data
                
                .. attribute:: last_change
                
                	Elapsed time since last change in hh\:mm\:ss format
                	**type**\: str
                
                .. attribute:: interface_name
                
                	Session interface name
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: username
                
                	Authentication username
                	**type**\: str
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\: str
                
                .. attribute:: state
                
                	Session state
                	**type**\:  :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.SessionState>`
                
                .. attribute:: l2tp_session_id
                
                	L2TP session ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: l2tp_tunnel_id
                
                	L2TP tunnel ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: srg_slave
                
                	Session SRG Slave
                	**type**\: bool
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.Session_, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('last_change', (YLeaf(YType.str, 'last-change'), ['str'])),
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('username', (YLeaf(YType.str, 'username'), ['str'])),
                        ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'SessionState', '')])),
                        ('l2tp_session_id', (YLeaf(YType.uint16, 'l2tp-session-id'), ['int'])),
                        ('l2tp_tunnel_id', (YLeaf(YType.uint16, 'l2tp-tunnel-id'), ['int'])),
                        ('srg_slave', (YLeaf(YType.boolean, 'srg-slave'), ['bool'])),
                    ])
                    self.last_change = None
                    self.interface_name = None
                    self.username = None
                    self.domain_name = None
                    self.state = None
                    self.l2tp_session_id = None
                    self.l2tp_tunnel_id = None
                    self.srg_slave = None
                    self._segment_path = lambda: "session"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.Session_, [u'last_change', u'interface_name', u'username', u'domain_name', u'state', u'l2tp_session_id', u'l2tp_tunnel_id', u'srg_slave'], name, value)


            class L2tp(Entity):
                """
                L2TP data
                
                .. attribute:: local_endpoint
                
                	Local endpoint IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: remote_endpoint
                
                	Remote endpoint IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: call_serial_number
                
                	Call serial number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_l2tp_class_attribute_mask_set
                
                	True if L2TP class attribute mask is set
                	**type**\: bool
                
                .. attribute:: local_tunnel_id
                
                	Local tunnel ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: remote_tunnel_id
                
                	Remote tunnel ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: local_session_id
                
                	Local session ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: remote_session_id
                
                	Remote session ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: remote_port
                
                	Remote port
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: tunnel_client_authentication_id
                
                	Tunnel client authentication ID
                	**type**\: str
                
                .. attribute:: tunnel_server_authentication_id
                
                	Tunnel server authentication ID
                	**type**\: str
                
                .. attribute:: tunnel_assignment_id
                
                	Tunnel assignment ID
                	**type**\: str
                
                .. attribute:: is_tunnel_authentication_enabled
                
                	True if tunnel authentication is enabled
                	**type**\: bool
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.L2tp, self).__init__()

                    self.yang_name = "l2tp"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('local_endpoint', (YLeaf(YType.str, 'local-endpoint'), ['str'])),
                        ('remote_endpoint', (YLeaf(YType.str, 'remote-endpoint'), ['str'])),
                        ('call_serial_number', (YLeaf(YType.uint32, 'call-serial-number'), ['int'])),
                        ('is_l2tp_class_attribute_mask_set', (YLeaf(YType.boolean, 'is-l2tp-class-attribute-mask-set'), ['bool'])),
                        ('local_tunnel_id', (YLeaf(YType.uint16, 'local-tunnel-id'), ['int'])),
                        ('remote_tunnel_id', (YLeaf(YType.uint16, 'remote-tunnel-id'), ['int'])),
                        ('local_session_id', (YLeaf(YType.uint16, 'local-session-id'), ['int'])),
                        ('remote_session_id', (YLeaf(YType.uint16, 'remote-session-id'), ['int'])),
                        ('remote_port', (YLeaf(YType.uint16, 'remote-port'), ['int'])),
                        ('tunnel_client_authentication_id', (YLeaf(YType.str, 'tunnel-client-authentication-id'), ['str'])),
                        ('tunnel_server_authentication_id', (YLeaf(YType.str, 'tunnel-server-authentication-id'), ['str'])),
                        ('tunnel_assignment_id', (YLeaf(YType.str, 'tunnel-assignment-id'), ['str'])),
                        ('is_tunnel_authentication_enabled', (YLeaf(YType.boolean, 'is-tunnel-authentication-enabled'), ['bool'])),
                    ])
                    self.local_endpoint = None
                    self.remote_endpoint = None
                    self.call_serial_number = None
                    self.is_l2tp_class_attribute_mask_set = None
                    self.local_tunnel_id = None
                    self.remote_tunnel_id = None
                    self.local_session_id = None
                    self.remote_session_id = None
                    self.remote_port = None
                    self.tunnel_client_authentication_id = None
                    self.tunnel_server_authentication_id = None
                    self.tunnel_assignment_id = None
                    self.is_tunnel_authentication_enabled = None
                    self._segment_path = lambda: "l2tp"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.L2tp, [u'local_endpoint', u'remote_endpoint', u'call_serial_number', u'is_l2tp_class_attribute_mask_set', u'local_tunnel_id', u'remote_tunnel_id', u'local_session_id', u'remote_session_id', u'remote_port', u'tunnel_client_authentication_id', u'tunnel_server_authentication_id', u'tunnel_assignment_id', u'is_tunnel_authentication_enabled'], name, value)


            class Subscriber(Entity):
                """
                Subscriber data
                
                .. attribute:: nas_port_type
                
                	NAS port type
                	**type**\:  :py:class:`VpdnNasPort <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnNasPort>`
                
                .. attribute:: physical_channel_id
                
                	Physical channel ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: receive_connect_speed
                
                	Receive connect speed in nanoseconds
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: nanosecond
                
                .. attribute:: transmit_connect_speed
                
                	Transmit connect speed in nanoseconds
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: nanosecond
                
                .. attribute:: nas_port
                
                	NAS port ID
                	**type**\: list of int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.Subscriber, self).__init__()

                    self.yang_name = "subscriber"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('nas_port_type', (YLeaf(YType.enumeration, 'nas-port-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'VpdnNasPort', '')])),
                        ('physical_channel_id', (YLeaf(YType.uint32, 'physical-channel-id'), ['int'])),
                        ('receive_connect_speed', (YLeaf(YType.uint64, 'receive-connect-speed'), ['int'])),
                        ('transmit_connect_speed', (YLeaf(YType.uint64, 'transmit-connect-speed'), ['int'])),
                        ('nas_port', (YLeafList(YType.uint8, 'nas-port'), ['int'])),
                    ])
                    self.nas_port_type = None
                    self.physical_channel_id = None
                    self.receive_connect_speed = None
                    self.transmit_connect_speed = None
                    self.nas_port = []
                    self._segment_path = lambda: "subscriber"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.Subscriber, [u'nas_port_type', u'physical_channel_id', u'receive_connect_speed', u'transmit_connect_speed', u'nas_port'], name, value)


            class Configuration(Entity):
                """
                Configuration data
                
                .. attribute:: vpn_id
                
                	VPN ID
                	**type**\:  :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Configuration.VpnId>`
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\: str
                
                .. attribute:: l2tp_busy_timeout
                
                	L2TP busy timeout in seconds
                	**type**\: int
                
                	**range:** 0..65535
                
                	**units**\: second
                
                .. attribute:: tos_mode
                
                	TOS mode
                	**type**\:  :py:class:`TosMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.TosMode>`
                
                .. attribute:: tos
                
                	TOS setting value
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: dsl_line_forwarding
                
                	True if DSL line info forwarding is enabled
                	**type**\: bool
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Sessions.Session.Configuration, self).__init__()

                    self.yang_name = "configuration"
                    self.yang_parent_name = "session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vpn-id", ("vpn_id", Vpdn.Sessions.Session.Configuration.VpnId))])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('l2tp_busy_timeout', (YLeaf(YType.uint16, 'l2tp-busy-timeout'), ['int'])),
                        ('tos_mode', (YLeaf(YType.enumeration, 'tos-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'TosMode', '')])),
                        ('tos', (YLeaf(YType.uint8, 'tos'), ['int'])),
                        ('dsl_line_forwarding', (YLeaf(YType.boolean, 'dsl-line-forwarding'), ['bool'])),
                    ])
                    self.template_name = None
                    self.vrf_name = None
                    self.l2tp_busy_timeout = None
                    self.tos_mode = None
                    self.tos = None
                    self.dsl_line_forwarding = None

                    self.vpn_id = Vpdn.Sessions.Session.Configuration.VpnId()
                    self.vpn_id.parent = self
                    self._children_name_map["vpn_id"] = "vpn-id"
                    self._segment_path = lambda: "configuration"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Sessions.Session.Configuration, [u'template_name', u'vrf_name', u'l2tp_busy_timeout', u'tos_mode', u'tos', u'dsl_line_forwarding'], name, value)


                class VpnId(Entity):
                    """
                    VPN ID
                    
                    .. attribute:: oui
                    
                    	OUI
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: index
                    
                    	Index
                    	**type**\: int
                    
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
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('oui', (YLeaf(YType.uint32, 'oui'), ['int'])),
                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                        ])
                        self.oui = None
                        self.index = None
                        self._segment_path = lambda: "vpn-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Sessions.Session.Configuration.VpnId, [u'oui', u'index'], name, value)


    class TunnelDestinations(Entity):
        """
        VPDN tunnel Destinations
        
        .. attribute:: tunnel_destination
        
        	VPDN tunnel destination information
        	**type**\: list of  		 :py:class:`TunnelDestination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.TunnelDestinations.TunnelDestination>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.TunnelDestinations, self).__init__()

            self.yang_name = "tunnel-destinations"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tunnel-destination", ("tunnel_destination", Vpdn.TunnelDestinations.TunnelDestination))])
            self._leafs = OrderedDict()

            self.tunnel_destination = YList(self)
            self._segment_path = lambda: "tunnel-destinations"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.TunnelDestinations, [], name, value)


        class TunnelDestination(Entity):
            """
            VPDN tunnel destination information
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: vrf_name_xr
            
            	VRF name
            	**type**\: str
            
            .. attribute:: load
            
            	Current load on LNS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: status
            
            	Status of LNS
            	**type**\:  :py:class:`LsgStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.LsgStatus>`
            
            .. attribute:: connects
            
            	Total count of tunnels connected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnects
            
            	Total count of tunnels disconnected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: retry
            
            	Retries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: status_change_time
            
            	Seconds since last status change
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.TunnelDestinations.TunnelDestination, self).__init__()

                self.yang_name = "tunnel-destination"
                self.yang_parent_name = "tunnel-destinations"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('address', (YLeaf(YType.str, 'address'), ['str'])),
                    ('vrf_name_xr', (YLeaf(YType.str, 'vrf-name-xr'), ['str'])),
                    ('load', (YLeaf(YType.uint32, 'load'), ['int'])),
                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'LsgStatus', '')])),
                    ('connects', (YLeaf(YType.uint32, 'connects'), ['int'])),
                    ('disconnects', (YLeaf(YType.uint32, 'disconnects'), ['int'])),
                    ('retry', (YLeaf(YType.uint32, 'retry'), ['int'])),
                    ('status_change_time', (YLeaf(YType.uint32, 'status-change-time'), ['int'])),
                ])
                self.vrf_name = None
                self.address = None
                self.vrf_name_xr = None
                self.load = None
                self.status = None
                self.connects = None
                self.disconnects = None
                self.retry = None
                self.status_change_time = None
                self._segment_path = lambda: "tunnel-destination"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/tunnel-destinations/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.TunnelDestinations.TunnelDestination, ['vrf_name', 'address', u'vrf_name_xr', u'load', u'status', u'connects', u'disconnects', u'retry', u'status_change_time'], name, value)


    class VpdnMirroring(Entity):
        """
        VPDN Mirroring Statistics
        
        .. attribute:: qad_send_stats
        
        	qad send stats
        	**type**\:  :py:class:`QadSendStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadSendStats>`
        
        .. attribute:: qad_recv_stats
        
        	qad recv stats
        	**type**\:  :py:class:`QadRecvStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadRecvStats>`
        
        .. attribute:: qad_send_stats_last_clear
        
        	qad send stats last clear
        	**type**\:  :py:class:`QadSendStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadSendStatsLastClear>`
        
        .. attribute:: qad_recv_stats_last_clear
        
        	qad recv stats last clear
        	**type**\:  :py:class:`QadRecvStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.VpdnMirroring.QadRecvStatsLastClear>`
        
        .. attribute:: sync_not_conn_cnt
        
        	sync not conn cnt
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sso_err_cnt
        
        	sso err cnt
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: sso_batch_err_cnt
        
        	sso batch err cnt
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: alloc_err_cnt
        
        	alloc err cnt
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: alloc_cnt
        
        	alloc cnt
        	**type**\: int
        
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
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("qad-send-stats", ("qad_send_stats", Vpdn.VpdnMirroring.QadSendStats)), ("qad-recv-stats", ("qad_recv_stats", Vpdn.VpdnMirroring.QadRecvStats)), ("qad-send-stats-last-clear", ("qad_send_stats_last_clear", Vpdn.VpdnMirroring.QadSendStatsLastClear)), ("qad-recv-stats-last-clear", ("qad_recv_stats_last_clear", Vpdn.VpdnMirroring.QadRecvStatsLastClear))])
            self._leafs = OrderedDict([
                ('sync_not_conn_cnt', (YLeaf(YType.uint32, 'sync-not-conn-cnt'), ['int'])),
                ('sso_err_cnt', (YLeaf(YType.uint32, 'sso-err-cnt'), ['int'])),
                ('sso_batch_err_cnt', (YLeaf(YType.uint32, 'sso-batch-err-cnt'), ['int'])),
                ('alloc_err_cnt', (YLeaf(YType.uint32, 'alloc-err-cnt'), ['int'])),
                ('alloc_cnt', (YLeaf(YType.uint32, 'alloc-cnt'), ['int'])),
            ])
            self.sync_not_conn_cnt = None
            self.sso_err_cnt = None
            self.sso_batch_err_cnt = None
            self.alloc_err_cnt = None
            self.alloc_cnt = None

            self.qad_send_stats = Vpdn.VpdnMirroring.QadSendStats()
            self.qad_send_stats.parent = self
            self._children_name_map["qad_send_stats"] = "qad-send-stats"

            self.qad_recv_stats = Vpdn.VpdnMirroring.QadRecvStats()
            self.qad_recv_stats.parent = self
            self._children_name_map["qad_recv_stats"] = "qad-recv-stats"

            self.qad_send_stats_last_clear = Vpdn.VpdnMirroring.QadSendStatsLastClear()
            self.qad_send_stats_last_clear.parent = self
            self._children_name_map["qad_send_stats_last_clear"] = "qad-send-stats-last-clear"

            self.qad_recv_stats_last_clear = Vpdn.VpdnMirroring.QadRecvStatsLastClear()
            self.qad_recv_stats_last_clear.parent = self
            self._children_name_map["qad_recv_stats_last_clear"] = "qad-recv-stats-last-clear"
            self._segment_path = lambda: "vpdn-mirroring"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.VpdnMirroring, [u'sync_not_conn_cnt', u'sso_err_cnt', u'sso_batch_err_cnt', u'alloc_err_cnt', u'alloc_cnt'], name, value)


        class QadSendStats(Entity):
            """
            qad send stats
            
            .. attribute:: msgs_sent
            
            	msgs sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_sent
            
            	acks sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_partner
            
            	no partner
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_failed
            
            	sends failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_failed
            
            	acks failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pending_acks
            
            	pending acks
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: timeouts
            
            	timeouts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: suspends
            
            	suspends
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: resumes
            
            	resumes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_fragment
            
            	sends fragment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_last_seq_number
            
            	qad last seq number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_frag_count
            
            	qad frag count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_ack_count
            
            	qad ack count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_unknown_acks
            
            	qad unknown acks
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_timeouts
            
            	qad timeouts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_count
            
            	qad rx count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_count
            
            	qad rx list count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_q_size
            
            	qad rx list q size
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_first_seq_number
            
            	qad rx first seq number
            	**type**\: int
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('msgs_sent', (YLeaf(YType.uint32, 'msgs-sent'), ['int'])),
                    ('acks_sent', (YLeaf(YType.uint32, 'acks-sent'), ['int'])),
                    ('no_partner', (YLeaf(YType.uint32, 'no-partner'), ['int'])),
                    ('sends_failed', (YLeaf(YType.uint32, 'sends-failed'), ['int'])),
                    ('acks_failed', (YLeaf(YType.uint32, 'acks-failed'), ['int'])),
                    ('pending_acks', (YLeaf(YType.uint32, 'pending-acks'), ['int'])),
                    ('timeouts', (YLeaf(YType.uint32, 'timeouts'), ['int'])),
                    ('suspends', (YLeaf(YType.uint32, 'suspends'), ['int'])),
                    ('resumes', (YLeaf(YType.uint32, 'resumes'), ['int'])),
                    ('sends_fragment', (YLeaf(YType.uint32, 'sends-fragment'), ['int'])),
                    ('qad_last_seq_number', (YLeaf(YType.uint32, 'qad-last-seq-number'), ['int'])),
                    ('qad_frag_count', (YLeaf(YType.uint32, 'qad-frag-count'), ['int'])),
                    ('qad_ack_count', (YLeaf(YType.uint32, 'qad-ack-count'), ['int'])),
                    ('qad_unknown_acks', (YLeaf(YType.uint32, 'qad-unknown-acks'), ['int'])),
                    ('qad_timeouts', (YLeaf(YType.uint32, 'qad-timeouts'), ['int'])),
                    ('qad_rx_count', (YLeaf(YType.uint32, 'qad-rx-count'), ['int'])),
                    ('qad_rx_list_count', (YLeaf(YType.uint32, 'qad-rx-list-count'), ['int'])),
                    ('qad_rx_list_q_size', (YLeaf(YType.uint32, 'qad-rx-list-q-size'), ['int'])),
                    ('qad_rx_first_seq_number', (YLeaf(YType.uint32, 'qad-rx-first-seq-number'), ['int'])),
                ])
                self.msgs_sent = None
                self.acks_sent = None
                self.no_partner = None
                self.sends_failed = None
                self.acks_failed = None
                self.pending_acks = None
                self.timeouts = None
                self.suspends = None
                self.resumes = None
                self.sends_fragment = None
                self.qad_last_seq_number = None
                self.qad_frag_count = None
                self.qad_ack_count = None
                self.qad_unknown_acks = None
                self.qad_timeouts = None
                self.qad_rx_count = None
                self.qad_rx_list_count = None
                self.qad_rx_list_q_size = None
                self.qad_rx_first_seq_number = None
                self._segment_path = lambda: "qad-send-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadSendStats, [u'msgs_sent', u'acks_sent', u'no_partner', u'sends_failed', u'acks_failed', u'pending_acks', u'timeouts', u'suspends', u'resumes', u'sends_fragment', u'qad_last_seq_number', u'qad_frag_count', u'qad_ack_count', u'qad_unknown_acks', u'qad_timeouts', u'qad_rx_count', u'qad_rx_list_count', u'qad_rx_list_q_size', u'qad_rx_first_seq_number'], name, value)


        class QadRecvStats(Entity):
            """
            qad recv stats
            
            .. attribute:: msgs_recvd
            
            	msgs recvd
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_recvd
            
            	acks recvd
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: recvd_acks_failed
            
            	recvd acks failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: init_drops
            
            	init drops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msg_drops
            
            	msg drops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ooo_drops
            
            	ooo drops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stale_msgs
            
            	stale msgs
            	**type**\: int
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('msgs_recvd', (YLeaf(YType.uint32, 'msgs-recvd'), ['int'])),
                    ('acks_recvd', (YLeaf(YType.uint32, 'acks-recvd'), ['int'])),
                    ('recvd_acks_failed', (YLeaf(YType.uint32, 'recvd-acks-failed'), ['int'])),
                    ('init_drops', (YLeaf(YType.uint32, 'init-drops'), ['int'])),
                    ('msg_drops', (YLeaf(YType.uint32, 'msg-drops'), ['int'])),
                    ('ooo_drops', (YLeaf(YType.uint32, 'ooo-drops'), ['int'])),
                    ('stale_msgs', (YLeaf(YType.uint32, 'stale-msgs'), ['int'])),
                ])
                self.msgs_recvd = None
                self.acks_recvd = None
                self.recvd_acks_failed = None
                self.init_drops = None
                self.msg_drops = None
                self.ooo_drops = None
                self.stale_msgs = None
                self._segment_path = lambda: "qad-recv-stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadRecvStats, [u'msgs_recvd', u'acks_recvd', u'recvd_acks_failed', u'init_drops', u'msg_drops', u'ooo_drops', u'stale_msgs'], name, value)


        class QadSendStatsLastClear(Entity):
            """
            qad send stats last clear
            
            .. attribute:: msgs_sent
            
            	msgs sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_sent
            
            	acks sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: no_partner
            
            	no partner
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_failed
            
            	sends failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_failed
            
            	acks failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pending_acks
            
            	pending acks
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: timeouts
            
            	timeouts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: suspends
            
            	suspends
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: resumes
            
            	resumes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sends_fragment
            
            	sends fragment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_last_seq_number
            
            	qad last seq number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_frag_count
            
            	qad frag count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_ack_count
            
            	qad ack count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_unknown_acks
            
            	qad unknown acks
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_timeouts
            
            	qad timeouts
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_count
            
            	qad rx count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_count
            
            	qad rx list count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_list_q_size
            
            	qad rx list q size
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: qad_rx_first_seq_number
            
            	qad rx first seq number
            	**type**\: int
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('msgs_sent', (YLeaf(YType.uint32, 'msgs-sent'), ['int'])),
                    ('acks_sent', (YLeaf(YType.uint32, 'acks-sent'), ['int'])),
                    ('no_partner', (YLeaf(YType.uint32, 'no-partner'), ['int'])),
                    ('sends_failed', (YLeaf(YType.uint32, 'sends-failed'), ['int'])),
                    ('acks_failed', (YLeaf(YType.uint32, 'acks-failed'), ['int'])),
                    ('pending_acks', (YLeaf(YType.uint32, 'pending-acks'), ['int'])),
                    ('timeouts', (YLeaf(YType.uint32, 'timeouts'), ['int'])),
                    ('suspends', (YLeaf(YType.uint32, 'suspends'), ['int'])),
                    ('resumes', (YLeaf(YType.uint32, 'resumes'), ['int'])),
                    ('sends_fragment', (YLeaf(YType.uint32, 'sends-fragment'), ['int'])),
                    ('qad_last_seq_number', (YLeaf(YType.uint32, 'qad-last-seq-number'), ['int'])),
                    ('qad_frag_count', (YLeaf(YType.uint32, 'qad-frag-count'), ['int'])),
                    ('qad_ack_count', (YLeaf(YType.uint32, 'qad-ack-count'), ['int'])),
                    ('qad_unknown_acks', (YLeaf(YType.uint32, 'qad-unknown-acks'), ['int'])),
                    ('qad_timeouts', (YLeaf(YType.uint32, 'qad-timeouts'), ['int'])),
                    ('qad_rx_count', (YLeaf(YType.uint32, 'qad-rx-count'), ['int'])),
                    ('qad_rx_list_count', (YLeaf(YType.uint32, 'qad-rx-list-count'), ['int'])),
                    ('qad_rx_list_q_size', (YLeaf(YType.uint32, 'qad-rx-list-q-size'), ['int'])),
                    ('qad_rx_first_seq_number', (YLeaf(YType.uint32, 'qad-rx-first-seq-number'), ['int'])),
                ])
                self.msgs_sent = None
                self.acks_sent = None
                self.no_partner = None
                self.sends_failed = None
                self.acks_failed = None
                self.pending_acks = None
                self.timeouts = None
                self.suspends = None
                self.resumes = None
                self.sends_fragment = None
                self.qad_last_seq_number = None
                self.qad_frag_count = None
                self.qad_ack_count = None
                self.qad_unknown_acks = None
                self.qad_timeouts = None
                self.qad_rx_count = None
                self.qad_rx_list_count = None
                self.qad_rx_list_q_size = None
                self.qad_rx_first_seq_number = None
                self._segment_path = lambda: "qad-send-stats-last-clear"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadSendStatsLastClear, [u'msgs_sent', u'acks_sent', u'no_partner', u'sends_failed', u'acks_failed', u'pending_acks', u'timeouts', u'suspends', u'resumes', u'sends_fragment', u'qad_last_seq_number', u'qad_frag_count', u'qad_ack_count', u'qad_unknown_acks', u'qad_timeouts', u'qad_rx_count', u'qad_rx_list_count', u'qad_rx_list_q_size', u'qad_rx_first_seq_number'], name, value)


        class QadRecvStatsLastClear(Entity):
            """
            qad recv stats last clear
            
            .. attribute:: msgs_recvd
            
            	msgs recvd
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: acks_recvd
            
            	acks recvd
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: recvd_acks_failed
            
            	recvd acks failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: init_drops
            
            	init drops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: msg_drops
            
            	msg drops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ooo_drops
            
            	ooo drops
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: stale_msgs
            
            	stale msgs
            	**type**\: int
            
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
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('msgs_recvd', (YLeaf(YType.uint32, 'msgs-recvd'), ['int'])),
                    ('acks_recvd', (YLeaf(YType.uint32, 'acks-recvd'), ['int'])),
                    ('recvd_acks_failed', (YLeaf(YType.uint32, 'recvd-acks-failed'), ['int'])),
                    ('init_drops', (YLeaf(YType.uint32, 'init-drops'), ['int'])),
                    ('msg_drops', (YLeaf(YType.uint32, 'msg-drops'), ['int'])),
                    ('ooo_drops', (YLeaf(YType.uint32, 'ooo-drops'), ['int'])),
                    ('stale_msgs', (YLeaf(YType.uint32, 'stale-msgs'), ['int'])),
                ])
                self.msgs_recvd = None
                self.acks_recvd = None
                self.recvd_acks_failed = None
                self.init_drops = None
                self.msg_drops = None
                self.ooo_drops = None
                self.stale_msgs = None
                self._segment_path = lambda: "qad-recv-stats-last-clear"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.VpdnMirroring.QadRecvStatsLastClear, [u'msgs_recvd', u'acks_recvd', u'recvd_acks_failed', u'init_drops', u'msg_drops', u'ooo_drops', u'stale_msgs'], name, value)


    class VpdnRedundancy(Entity):
        """
        Show VPDN Redundancy information
        
        .. attribute:: session_total
        
        	session total
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: session_synced
        
        	session synced
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: state
        
        	state
        	**type**\:  :py:class:`VpdnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnState>`
        
        .. attribute:: start_time
        
        	start time
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: finish_time
        
        	finish time
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: abort_time
        
        	abort time
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.VpdnRedundancy, self).__init__()

            self.yang_name = "vpdn-redundancy"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('session_total', (YLeaf(YType.uint32, 'session-total'), ['int'])),
                ('session_synced', (YLeaf(YType.uint32, 'session-synced'), ['int'])),
                ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'VpdnState', '')])),
                ('start_time', (YLeaf(YType.uint64, 'start-time'), ['int'])),
                ('finish_time', (YLeaf(YType.uint64, 'finish-time'), ['int'])),
                ('abort_time', (YLeaf(YType.uint64, 'abort-time'), ['int'])),
            ])
            self.session_total = None
            self.session_synced = None
            self.state = None
            self.start_time = None
            self.finish_time = None
            self.abort_time = None
            self._segment_path = lambda: "vpdn-redundancy"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.VpdnRedundancy, [u'session_total', u'session_synced', u'state', u'start_time', u'finish_time', u'abort_time'], name, value)


    class HistoryFailures(Entity):
        """
        VPDN history failure list
        
        .. attribute:: history_failure
        
        	VPDN history failure information
        	**type**\: list of  		 :py:class:`HistoryFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.HistoryFailures.HistoryFailure>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.HistoryFailures, self).__init__()

            self.yang_name = "history-failures"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("history-failure", ("history_failure", Vpdn.HistoryFailures.HistoryFailure))])
            self._leafs = OrderedDict()

            self.history_failure = YList(self)
            self._segment_path = lambda: "history-failures"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.HistoryFailures, [], name, value)


        class HistoryFailure(Entity):
            """
            VPDN history failure information
            
            .. attribute:: username
            
            	Username
            	**type**\: str
            
            .. attribute:: remote_name
            
            	Remote name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: username_xr
            
            	Authentication username
            	**type**\: str
            
            .. attribute:: domain_name
            
            	Domain name
            	**type**\: str
            
            .. attribute:: mid
            
            	VPDN user session ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nas
            
            	Network access server
            	**type**\: str
            
            .. attribute:: destination_address
            
            	NAS IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: remote_client_id
            
            	Remote client ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: home_gateway
            
            	Home gateway
            	**type**\: str
            
            .. attribute:: source_address
            
            	Source IP address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_client_id
            
            	Local client ID
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: event_time
            
            	Event logged time in Ex\: Wed Aug  3 10\:28\:30 2011
            	**type**\: str
            
            .. attribute:: error_repeat_count
            
            	Error repeat count
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: failure_type
            
            	Failure type
            	**type**\:  :py:class:`VpdnFailcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnFailcode>`
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.HistoryFailures.HistoryFailure, self).__init__()

                self.yang_name = "history-failure"
                self.yang_parent_name = "history-failures"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('username', (YLeaf(YType.str, 'username'), ['str'])),
                    ('remote_name', (YLeaf(YType.str, 'remote-name'), ['str'])),
                    ('username_xr', (YLeaf(YType.str, 'username-xr'), ['str'])),
                    ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                    ('mid', (YLeaf(YType.uint16, 'mid'), ['int'])),
                    ('nas', (YLeaf(YType.str, 'nas'), ['str'])),
                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                    ('remote_client_id', (YLeaf(YType.uint16, 'remote-client-id'), ['int'])),
                    ('home_gateway', (YLeaf(YType.str, 'home-gateway'), ['str'])),
                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                    ('local_client_id', (YLeaf(YType.uint16, 'local-client-id'), ['int'])),
                    ('event_time', (YLeaf(YType.str, 'event-time'), ['str'])),
                    ('error_repeat_count', (YLeaf(YType.uint16, 'error-repeat-count'), ['int'])),
                    ('failure_type', (YLeaf(YType.enumeration, 'failure-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper', 'VpdnFailcode', '')])),
                ])
                self.username = None
                self.remote_name = None
                self.username_xr = None
                self.domain_name = None
                self.mid = None
                self.nas = None
                self.destination_address = None
                self.remote_client_id = None
                self.home_gateway = None
                self.source_address = None
                self.local_client_id = None
                self.event_time = None
                self.error_repeat_count = None
                self.failure_type = None
                self._segment_path = lambda: "history-failure"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/history-failures/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.HistoryFailures.HistoryFailure, ['username', 'remote_name', u'username_xr', u'domain_name', u'mid', u'nas', u'destination_address', u'remote_client_id', u'home_gateway', u'source_address', u'local_client_id', u'event_time', u'error_repeat_count', u'failure_type'], name, value)

    def clone_ptr(self):
        self._top_entity = Vpdn()
        return self._top_entity

