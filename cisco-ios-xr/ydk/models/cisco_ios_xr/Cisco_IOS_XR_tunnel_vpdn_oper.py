""" Cisco_IOS_XR_tunnel_vpdn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package operational data.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

            self.session = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.Sessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.Sessions, self).__setattr__(name, value)


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
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("session_label",
                                "parent_interface_name",
                                "setup_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.Sessions.Session, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.Sessions.Session, self).__setattr__(name, value)


            class Session(Entity):
                """
                Session data
                
                .. attribute:: domain_name
                
                	Domain name
                	**type**\:  str
                
                .. attribute:: interface_name
                
                	Session interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
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

                    self.domain_name = YLeaf(YType.str, "domain-name")

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.l2tp_session_id = YLeaf(YType.uint16, "l2tp-session-id")

                    self.l2tp_tunnel_id = YLeaf(YType.uint16, "l2tp-tunnel-id")

                    self.last_change = YLeaf(YType.str, "last-change")

                    self.srg_slave = YLeaf(YType.boolean, "srg-slave")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.username = YLeaf(YType.str, "username")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("domain_name",
                                    "interface_name",
                                    "l2tp_session_id",
                                    "l2tp_tunnel_id",
                                    "last_change",
                                    "srg_slave",
                                    "state",
                                    "username") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Sessions.Session.Session, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Sessions.Session.Session, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.domain_name.is_set or
                        self.interface_name.is_set or
                        self.l2tp_session_id.is_set or
                        self.l2tp_tunnel_id.is_set or
                        self.last_change.is_set or
                        self.srg_slave.is_set or
                        self.state.is_set or
                        self.username.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.domain_name.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.l2tp_session_id.yfilter != YFilter.not_set or
                        self.l2tp_tunnel_id.yfilter != YFilter.not_set or
                        self.last_change.yfilter != YFilter.not_set or
                        self.srg_slave.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.username.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "session" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.domain_name.get_name_leafdata())
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.l2tp_session_id.is_set or self.l2tp_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.l2tp_session_id.get_name_leafdata())
                    if (self.l2tp_tunnel_id.is_set or self.l2tp_tunnel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.l2tp_tunnel_id.get_name_leafdata())
                    if (self.last_change.is_set or self.last_change.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_change.get_name_leafdata())
                    if (self.srg_slave.is_set or self.srg_slave.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.srg_slave.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.username.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "domain-name" or name == "interface-name" or name == "l2tp-session-id" or name == "l2tp-tunnel-id" or name == "last-change" or name == "srg-slave" or name == "state" or name == "username"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "domain-name"):
                        self.domain_name = value
                        self.domain_name.value_namespace = name_space
                        self.domain_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "l2tp-session-id"):
                        self.l2tp_session_id = value
                        self.l2tp_session_id.value_namespace = name_space
                        self.l2tp_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "l2tp-tunnel-id"):
                        self.l2tp_tunnel_id = value
                        self.l2tp_tunnel_id.value_namespace = name_space
                        self.l2tp_tunnel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-change"):
                        self.last_change = value
                        self.last_change.value_namespace = name_space
                        self.last_change.value_namespace_prefix = name_space_prefix
                    if(value_path == "srg-slave"):
                        self.srg_slave = value
                        self.srg_slave.value_namespace = name_space
                        self.srg_slave.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "username"):
                        self.username = value
                        self.username.value_namespace = name_space
                        self.username.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("call_serial_number",
                                    "is_l2tp_class_attribute_mask_set",
                                    "is_tunnel_authentication_enabled",
                                    "local_endpoint",
                                    "local_session_id",
                                    "local_tunnel_id",
                                    "remote_endpoint",
                                    "remote_port",
                                    "remote_session_id",
                                    "remote_tunnel_id",
                                    "tunnel_assignment_id",
                                    "tunnel_client_authentication_id",
                                    "tunnel_server_authentication_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Sessions.Session.L2Tp, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Sessions.Session.L2Tp, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.call_serial_number.is_set or
                        self.is_l2tp_class_attribute_mask_set.is_set or
                        self.is_tunnel_authentication_enabled.is_set or
                        self.local_endpoint.is_set or
                        self.local_session_id.is_set or
                        self.local_tunnel_id.is_set or
                        self.remote_endpoint.is_set or
                        self.remote_port.is_set or
                        self.remote_session_id.is_set or
                        self.remote_tunnel_id.is_set or
                        self.tunnel_assignment_id.is_set or
                        self.tunnel_client_authentication_id.is_set or
                        self.tunnel_server_authentication_id.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.call_serial_number.yfilter != YFilter.not_set or
                        self.is_l2tp_class_attribute_mask_set.yfilter != YFilter.not_set or
                        self.is_tunnel_authentication_enabled.yfilter != YFilter.not_set or
                        self.local_endpoint.yfilter != YFilter.not_set or
                        self.local_session_id.yfilter != YFilter.not_set or
                        self.local_tunnel_id.yfilter != YFilter.not_set or
                        self.remote_endpoint.yfilter != YFilter.not_set or
                        self.remote_port.yfilter != YFilter.not_set or
                        self.remote_session_id.yfilter != YFilter.not_set or
                        self.remote_tunnel_id.yfilter != YFilter.not_set or
                        self.tunnel_assignment_id.yfilter != YFilter.not_set or
                        self.tunnel_client_authentication_id.yfilter != YFilter.not_set or
                        self.tunnel_server_authentication_id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "l2tp" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.call_serial_number.is_set or self.call_serial_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.call_serial_number.get_name_leafdata())
                    if (self.is_l2tp_class_attribute_mask_set.is_set or self.is_l2tp_class_attribute_mask_set.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_l2tp_class_attribute_mask_set.get_name_leafdata())
                    if (self.is_tunnel_authentication_enabled.is_set or self.is_tunnel_authentication_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_tunnel_authentication_enabled.get_name_leafdata())
                    if (self.local_endpoint.is_set or self.local_endpoint.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_endpoint.get_name_leafdata())
                    if (self.local_session_id.is_set or self.local_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_session_id.get_name_leafdata())
                    if (self.local_tunnel_id.is_set or self.local_tunnel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_tunnel_id.get_name_leafdata())
                    if (self.remote_endpoint.is_set or self.remote_endpoint.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_endpoint.get_name_leafdata())
                    if (self.remote_port.is_set or self.remote_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_port.get_name_leafdata())
                    if (self.remote_session_id.is_set or self.remote_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_session_id.get_name_leafdata())
                    if (self.remote_tunnel_id.is_set or self.remote_tunnel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.remote_tunnel_id.get_name_leafdata())
                    if (self.tunnel_assignment_id.is_set or self.tunnel_assignment_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tunnel_assignment_id.get_name_leafdata())
                    if (self.tunnel_client_authentication_id.is_set or self.tunnel_client_authentication_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tunnel_client_authentication_id.get_name_leafdata())
                    if (self.tunnel_server_authentication_id.is_set or self.tunnel_server_authentication_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tunnel_server_authentication_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "call-serial-number" or name == "is-l2tp-class-attribute-mask-set" or name == "is-tunnel-authentication-enabled" or name == "local-endpoint" or name == "local-session-id" or name == "local-tunnel-id" or name == "remote-endpoint" or name == "remote-port" or name == "remote-session-id" or name == "remote-tunnel-id" or name == "tunnel-assignment-id" or name == "tunnel-client-authentication-id" or name == "tunnel-server-authentication-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "call-serial-number"):
                        self.call_serial_number = value
                        self.call_serial_number.value_namespace = name_space
                        self.call_serial_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-l2tp-class-attribute-mask-set"):
                        self.is_l2tp_class_attribute_mask_set = value
                        self.is_l2tp_class_attribute_mask_set.value_namespace = name_space
                        self.is_l2tp_class_attribute_mask_set.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-tunnel-authentication-enabled"):
                        self.is_tunnel_authentication_enabled = value
                        self.is_tunnel_authentication_enabled.value_namespace = name_space
                        self.is_tunnel_authentication_enabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-endpoint"):
                        self.local_endpoint = value
                        self.local_endpoint.value_namespace = name_space
                        self.local_endpoint.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-session-id"):
                        self.local_session_id = value
                        self.local_session_id.value_namespace = name_space
                        self.local_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-tunnel-id"):
                        self.local_tunnel_id = value
                        self.local_tunnel_id.value_namespace = name_space
                        self.local_tunnel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-endpoint"):
                        self.remote_endpoint = value
                        self.remote_endpoint.value_namespace = name_space
                        self.remote_endpoint.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-port"):
                        self.remote_port = value
                        self.remote_port.value_namespace = name_space
                        self.remote_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-session-id"):
                        self.remote_session_id = value
                        self.remote_session_id.value_namespace = name_space
                        self.remote_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "remote-tunnel-id"):
                        self.remote_tunnel_id = value
                        self.remote_tunnel_id.value_namespace = name_space
                        self.remote_tunnel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "tunnel-assignment-id"):
                        self.tunnel_assignment_id = value
                        self.tunnel_assignment_id.value_namespace = name_space
                        self.tunnel_assignment_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "tunnel-client-authentication-id"):
                        self.tunnel_client_authentication_id = value
                        self.tunnel_client_authentication_id.value_namespace = name_space
                        self.tunnel_client_authentication_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "tunnel-server-authentication-id"):
                        self.tunnel_server_authentication_id = value
                        self.tunnel_server_authentication_id.value_namespace = name_space
                        self.tunnel_server_authentication_id.value_namespace_prefix = name_space_prefix


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

                    self.nas_port = YLeafList(YType.uint8, "nas-port")

                    self.nas_port_type = YLeaf(YType.enumeration, "nas-port-type")

                    self.physical_channel_id = YLeaf(YType.uint32, "physical-channel-id")

                    self.receive_connect_speed = YLeaf(YType.uint64, "receive-connect-speed")

                    self.transmit_connect_speed = YLeaf(YType.uint64, "transmit-connect-speed")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("nas_port",
                                    "nas_port_type",
                                    "physical_channel_id",
                                    "receive_connect_speed",
                                    "transmit_connect_speed") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Sessions.Session.Subscriber, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Sessions.Session.Subscriber, self).__setattr__(name, value)

                def has_data(self):
                    for leaf in self.nas_port.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.nas_port_type.is_set or
                        self.physical_channel_id.is_set or
                        self.receive_connect_speed.is_set or
                        self.transmit_connect_speed.is_set)

                def has_operation(self):
                    for leaf in self.nas_port.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.nas_port.yfilter != YFilter.not_set or
                        self.nas_port_type.yfilter != YFilter.not_set or
                        self.physical_channel_id.yfilter != YFilter.not_set or
                        self.receive_connect_speed.yfilter != YFilter.not_set or
                        self.transmit_connect_speed.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "subscriber" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.nas_port_type.is_set or self.nas_port_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nas_port_type.get_name_leafdata())
                    if (self.physical_channel_id.is_set or self.physical_channel_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.physical_channel_id.get_name_leafdata())
                    if (self.receive_connect_speed.is_set or self.receive_connect_speed.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.receive_connect_speed.get_name_leafdata())
                    if (self.transmit_connect_speed.is_set or self.transmit_connect_speed.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transmit_connect_speed.get_name_leafdata())

                    leaf_name_data.extend(self.nas_port.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nas-port" or name == "nas-port-type" or name == "physical-channel-id" or name == "receive-connect-speed" or name == "transmit-connect-speed"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "nas-port"):
                        self.nas_port.append(value)
                    if(value_path == "nas-port-type"):
                        self.nas_port_type = value
                        self.nas_port_type.value_namespace = name_space
                        self.nas_port_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "physical-channel-id"):
                        self.physical_channel_id = value
                        self.physical_channel_id.value_namespace = name_space
                        self.physical_channel_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "receive-connect-speed"):
                        self.receive_connect_speed = value
                        self.receive_connect_speed.value_namespace = name_space
                        self.receive_connect_speed.value_namespace_prefix = name_space_prefix
                    if(value_path == "transmit-connect-speed"):
                        self.transmit_connect_speed = value
                        self.transmit_connect_speed.value_namespace = name_space
                        self.transmit_connect_speed.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("dsl_line_forwarding",
                                    "l2tp_busy_timeout",
                                    "template_name",
                                    "tos",
                                    "tos_mode",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Sessions.Session.Configuration, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Sessions.Session.Configuration, self).__setattr__(name, value)


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

                        self.index = YLeaf(YType.uint32, "index")

                        self.oui = YLeaf(YType.uint32, "oui")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index",
                                        "oui") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vpdn.Sessions.Session.Configuration.VpnId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vpdn.Sessions.Session.Configuration.VpnId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.index.is_set or
                            self.oui.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            self.oui.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vpn-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())
                        if (self.oui.is_set or self.oui.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oui.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "index" or name == "oui"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix
                        if(value_path == "oui"):
                            self.oui = value
                            self.oui.value_namespace = name_space
                            self.oui.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.dsl_line_forwarding.is_set or
                        self.l2tp_busy_timeout.is_set or
                        self.template_name.is_set or
                        self.tos.is_set or
                        self.tos_mode.is_set or
                        self.vrf_name.is_set or
                        (self.vpn_id is not None and self.vpn_id.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.dsl_line_forwarding.yfilter != YFilter.not_set or
                        self.l2tp_busy_timeout.yfilter != YFilter.not_set or
                        self.template_name.yfilter != YFilter.not_set or
                        self.tos.yfilter != YFilter.not_set or
                        self.tos_mode.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        (self.vpn_id is not None and self.vpn_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "configuration" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.dsl_line_forwarding.is_set or self.dsl_line_forwarding.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dsl_line_forwarding.get_name_leafdata())
                    if (self.l2tp_busy_timeout.is_set or self.l2tp_busy_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.l2tp_busy_timeout.get_name_leafdata())
                    if (self.template_name.is_set or self.template_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.template_name.get_name_leafdata())
                    if (self.tos.is_set or self.tos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tos.get_name_leafdata())
                    if (self.tos_mode.is_set or self.tos_mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tos_mode.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "vpn-id"):
                        if (self.vpn_id is None):
                            self.vpn_id = Vpdn.Sessions.Session.Configuration.VpnId()
                            self.vpn_id.parent = self
                            self._children_name_map["vpn_id"] = "vpn-id"
                        return self.vpn_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vpn-id" or name == "dsl-line-forwarding" or name == "l2tp-busy-timeout" or name == "template-name" or name == "tos" or name == "tos-mode" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "dsl-line-forwarding"):
                        self.dsl_line_forwarding = value
                        self.dsl_line_forwarding.value_namespace = name_space
                        self.dsl_line_forwarding.value_namespace_prefix = name_space_prefix
                    if(value_path == "l2tp-busy-timeout"):
                        self.l2tp_busy_timeout = value
                        self.l2tp_busy_timeout.value_namespace = name_space
                        self.l2tp_busy_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "template-name"):
                        self.template_name = value
                        self.template_name.value_namespace = name_space
                        self.template_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "tos"):
                        self.tos = value
                        self.tos.value_namespace = name_space
                        self.tos.value_namespace_prefix = name_space_prefix
                    if(value_path == "tos-mode"):
                        self.tos_mode = value
                        self.tos_mode.value_namespace = name_space
                        self.tos_mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.session_label.is_set or
                    self.parent_interface_name.is_set or
                    self.setup_time.is_set or
                    (self.configuration is not None and self.configuration.has_data()) or
                    (self.l2tp is not None and self.l2tp.has_data()) or
                    (self.session is not None and self.session.has_data()) or
                    (self.subscriber is not None and self.subscriber.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.session_label.yfilter != YFilter.not_set or
                    self.parent_interface_name.yfilter != YFilter.not_set or
                    self.setup_time.yfilter != YFilter.not_set or
                    (self.configuration is not None and self.configuration.has_operation()) or
                    (self.l2tp is not None and self.l2tp.has_operation()) or
                    (self.session is not None and self.session.has_operation()) or
                    (self.subscriber is not None and self.subscriber.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session" + "[session-label='" + self.session_label.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/sessions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.session_label.is_set or self.session_label.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_label.get_name_leafdata())
                if (self.parent_interface_name.is_set or self.parent_interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.parent_interface_name.get_name_leafdata())
                if (self.setup_time.is_set or self.setup_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.setup_time.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "configuration"):
                    if (self.configuration is None):
                        self.configuration = Vpdn.Sessions.Session.Configuration()
                        self.configuration.parent = self
                        self._children_name_map["configuration"] = "configuration"
                    return self.configuration

                if (child_yang_name == "l2tp"):
                    if (self.l2tp is None):
                        self.l2tp = Vpdn.Sessions.Session.L2Tp()
                        self.l2tp.parent = self
                        self._children_name_map["l2tp"] = "l2tp"
                    return self.l2tp

                if (child_yang_name == "session"):
                    if (self.session is None):
                        self.session = Vpdn.Sessions.Session.Session()
                        self.session.parent = self
                        self._children_name_map["session"] = "session"
                    return self.session

                if (child_yang_name == "subscriber"):
                    if (self.subscriber is None):
                        self.subscriber = Vpdn.Sessions.Session.Subscriber()
                        self.subscriber.parent = self
                        self._children_name_map["subscriber"] = "subscriber"
                    return self.subscriber

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "configuration" or name == "l2tp" or name == "session" or name == "subscriber" or name == "session-label" or name == "parent-interface-name" or name == "setup-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "session-label"):
                    self.session_label = value
                    self.session_label.value_namespace = name_space
                    self.session_label.value_namespace_prefix = name_space_prefix
                if(value_path == "parent-interface-name"):
                    self.parent_interface_name = value
                    self.parent_interface_name.value_namespace = name_space
                    self.parent_interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "setup-time"):
                    self.setup_time = value
                    self.setup_time.value_namespace = name_space
                    self.setup_time.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.session:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.session:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "sessions" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "session"):
                for c in self.session:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vpdn.Sessions.Session()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.session.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "session"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.tunnel_destination = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.TunnelDestinations, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.TunnelDestinations, self).__setattr__(name, value)


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

                self.address = YLeaf(YType.str, "address")

                self.connects = YLeaf(YType.uint32, "connects")

                self.disconnects = YLeaf(YType.uint32, "disconnects")

                self.load = YLeaf(YType.uint32, "load")

                self.retry = YLeaf(YType.uint32, "retry")

                self.status = YLeaf(YType.enumeration, "status")

                self.status_change_time = YLeaf(YType.uint32, "status-change-time")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.vrf_name_xr = YLeaf(YType.str, "vrf-name-xr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("address",
                                "connects",
                                "disconnects",
                                "load",
                                "retry",
                                "status",
                                "status_change_time",
                                "vrf_name",
                                "vrf_name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.TunnelDestinations.TunnelDestination, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.TunnelDestinations.TunnelDestination, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.address.is_set or
                    self.connects.is_set or
                    self.disconnects.is_set or
                    self.load.is_set or
                    self.retry.is_set or
                    self.status.is_set or
                    self.status_change_time.is_set or
                    self.vrf_name.is_set or
                    self.vrf_name_xr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.address.yfilter != YFilter.not_set or
                    self.connects.yfilter != YFilter.not_set or
                    self.disconnects.yfilter != YFilter.not_set or
                    self.load.yfilter != YFilter.not_set or
                    self.retry.yfilter != YFilter.not_set or
                    self.status.yfilter != YFilter.not_set or
                    self.status_change_time.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.vrf_name_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tunnel-destination" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/tunnel-destinations/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.address.get_name_leafdata())
                if (self.connects.is_set or self.connects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.connects.get_name_leafdata())
                if (self.disconnects.is_set or self.disconnects.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disconnects.get_name_leafdata())
                if (self.load.is_set or self.load.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.load.get_name_leafdata())
                if (self.retry.is_set or self.retry.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.retry.get_name_leafdata())
                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.status.get_name_leafdata())
                if (self.status_change_time.is_set or self.status_change_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.status_change_time.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.vrf_name_xr.is_set or self.vrf_name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "connects" or name == "disconnects" or name == "load" or name == "retry" or name == "status" or name == "status-change-time" or name == "vrf-name" or name == "vrf-name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "address"):
                    self.address = value
                    self.address.value_namespace = name_space
                    self.address.value_namespace_prefix = name_space_prefix
                if(value_path == "connects"):
                    self.connects = value
                    self.connects.value_namespace = name_space
                    self.connects.value_namespace_prefix = name_space_prefix
                if(value_path == "disconnects"):
                    self.disconnects = value
                    self.disconnects.value_namespace = name_space
                    self.disconnects.value_namespace_prefix = name_space_prefix
                if(value_path == "load"):
                    self.load = value
                    self.load.value_namespace = name_space
                    self.load.value_namespace_prefix = name_space_prefix
                if(value_path == "retry"):
                    self.retry = value
                    self.retry.value_namespace = name_space
                    self.retry.value_namespace_prefix = name_space_prefix
                if(value_path == "status"):
                    self.status = value
                    self.status.value_namespace = name_space
                    self.status.value_namespace_prefix = name_space_prefix
                if(value_path == "status-change-time"):
                    self.status_change_time = value
                    self.status_change_time.value_namespace = name_space
                    self.status_change_time.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name-xr"):
                    self.vrf_name_xr = value
                    self.vrf_name_xr.value_namespace = name_space
                    self.vrf_name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tunnel_destination:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tunnel_destination:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tunnel-destinations" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tunnel-destination"):
                for c in self.tunnel_destination:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vpdn.TunnelDestinations.TunnelDestination()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tunnel_destination.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tunnel-destination"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("alloc_cnt",
                            "alloc_err_cnt",
                            "sso_batch_err_cnt",
                            "sso_err_cnt",
                            "sync_not_conn_cnt") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.VpdnMirroring, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.VpdnMirroring, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("acks_failed",
                                "acks_sent",
                                "msgs_sent",
                                "no_partner",
                                "pending_acks",
                                "qad_ack_count",
                                "qad_frag_count",
                                "qad_last_seq_number",
                                "qad_rx_count",
                                "qad_rx_first_seq_number",
                                "qad_rx_list_count",
                                "qad_rx_list_q_size",
                                "qad_timeouts",
                                "qad_unknown_acks",
                                "resumes",
                                "sends_failed",
                                "sends_fragment",
                                "suspends",
                                "timeouts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.VpdnMirroring.QadSendStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.VpdnMirroring.QadSendStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.acks_failed.is_set or
                    self.acks_sent.is_set or
                    self.msgs_sent.is_set or
                    self.no_partner.is_set or
                    self.pending_acks.is_set or
                    self.qad_ack_count.is_set or
                    self.qad_frag_count.is_set or
                    self.qad_last_seq_number.is_set or
                    self.qad_rx_count.is_set or
                    self.qad_rx_first_seq_number.is_set or
                    self.qad_rx_list_count.is_set or
                    self.qad_rx_list_q_size.is_set or
                    self.qad_timeouts.is_set or
                    self.qad_unknown_acks.is_set or
                    self.resumes.is_set or
                    self.sends_failed.is_set or
                    self.sends_fragment.is_set or
                    self.suspends.is_set or
                    self.timeouts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.acks_failed.yfilter != YFilter.not_set or
                    self.acks_sent.yfilter != YFilter.not_set or
                    self.msgs_sent.yfilter != YFilter.not_set or
                    self.no_partner.yfilter != YFilter.not_set or
                    self.pending_acks.yfilter != YFilter.not_set or
                    self.qad_ack_count.yfilter != YFilter.not_set or
                    self.qad_frag_count.yfilter != YFilter.not_set or
                    self.qad_last_seq_number.yfilter != YFilter.not_set or
                    self.qad_rx_count.yfilter != YFilter.not_set or
                    self.qad_rx_first_seq_number.yfilter != YFilter.not_set or
                    self.qad_rx_list_count.yfilter != YFilter.not_set or
                    self.qad_rx_list_q_size.yfilter != YFilter.not_set or
                    self.qad_timeouts.yfilter != YFilter.not_set or
                    self.qad_unknown_acks.yfilter != YFilter.not_set or
                    self.resumes.yfilter != YFilter.not_set or
                    self.sends_failed.yfilter != YFilter.not_set or
                    self.sends_fragment.yfilter != YFilter.not_set or
                    self.suspends.yfilter != YFilter.not_set or
                    self.timeouts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qad-send-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.acks_failed.is_set or self.acks_failed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.acks_failed.get_name_leafdata())
                if (self.acks_sent.is_set or self.acks_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.acks_sent.get_name_leafdata())
                if (self.msgs_sent.is_set or self.msgs_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msgs_sent.get_name_leafdata())
                if (self.no_partner.is_set or self.no_partner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no_partner.get_name_leafdata())
                if (self.pending_acks.is_set or self.pending_acks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pending_acks.get_name_leafdata())
                if (self.qad_ack_count.is_set or self.qad_ack_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_ack_count.get_name_leafdata())
                if (self.qad_frag_count.is_set or self.qad_frag_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_frag_count.get_name_leafdata())
                if (self.qad_last_seq_number.is_set or self.qad_last_seq_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_last_seq_number.get_name_leafdata())
                if (self.qad_rx_count.is_set or self.qad_rx_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_count.get_name_leafdata())
                if (self.qad_rx_first_seq_number.is_set or self.qad_rx_first_seq_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_first_seq_number.get_name_leafdata())
                if (self.qad_rx_list_count.is_set or self.qad_rx_list_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_list_count.get_name_leafdata())
                if (self.qad_rx_list_q_size.is_set or self.qad_rx_list_q_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_list_q_size.get_name_leafdata())
                if (self.qad_timeouts.is_set or self.qad_timeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_timeouts.get_name_leafdata())
                if (self.qad_unknown_acks.is_set or self.qad_unknown_acks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_unknown_acks.get_name_leafdata())
                if (self.resumes.is_set or self.resumes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.resumes.get_name_leafdata())
                if (self.sends_failed.is_set or self.sends_failed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sends_failed.get_name_leafdata())
                if (self.sends_fragment.is_set or self.sends_fragment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sends_fragment.get_name_leafdata())
                if (self.suspends.is_set or self.suspends.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.suspends.get_name_leafdata())
                if (self.timeouts.is_set or self.timeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeouts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "acks-failed" or name == "acks-sent" or name == "msgs-sent" or name == "no-partner" or name == "pending-acks" or name == "qad-ack-count" or name == "qad-frag-count" or name == "qad-last-seq-number" or name == "qad-rx-count" or name == "qad-rx-first-seq-number" or name == "qad-rx-list-count" or name == "qad-rx-list-q-size" or name == "qad-timeouts" or name == "qad-unknown-acks" or name == "resumes" or name == "sends-failed" or name == "sends-fragment" or name == "suspends" or name == "timeouts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "acks-failed"):
                    self.acks_failed = value
                    self.acks_failed.value_namespace = name_space
                    self.acks_failed.value_namespace_prefix = name_space_prefix
                if(value_path == "acks-sent"):
                    self.acks_sent = value
                    self.acks_sent.value_namespace = name_space
                    self.acks_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "msgs-sent"):
                    self.msgs_sent = value
                    self.msgs_sent.value_namespace = name_space
                    self.msgs_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "no-partner"):
                    self.no_partner = value
                    self.no_partner.value_namespace = name_space
                    self.no_partner.value_namespace_prefix = name_space_prefix
                if(value_path == "pending-acks"):
                    self.pending_acks = value
                    self.pending_acks.value_namespace = name_space
                    self.pending_acks.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-ack-count"):
                    self.qad_ack_count = value
                    self.qad_ack_count.value_namespace = name_space
                    self.qad_ack_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-frag-count"):
                    self.qad_frag_count = value
                    self.qad_frag_count.value_namespace = name_space
                    self.qad_frag_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-last-seq-number"):
                    self.qad_last_seq_number = value
                    self.qad_last_seq_number.value_namespace = name_space
                    self.qad_last_seq_number.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-count"):
                    self.qad_rx_count = value
                    self.qad_rx_count.value_namespace = name_space
                    self.qad_rx_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-first-seq-number"):
                    self.qad_rx_first_seq_number = value
                    self.qad_rx_first_seq_number.value_namespace = name_space
                    self.qad_rx_first_seq_number.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-list-count"):
                    self.qad_rx_list_count = value
                    self.qad_rx_list_count.value_namespace = name_space
                    self.qad_rx_list_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-list-q-size"):
                    self.qad_rx_list_q_size = value
                    self.qad_rx_list_q_size.value_namespace = name_space
                    self.qad_rx_list_q_size.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-timeouts"):
                    self.qad_timeouts = value
                    self.qad_timeouts.value_namespace = name_space
                    self.qad_timeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-unknown-acks"):
                    self.qad_unknown_acks = value
                    self.qad_unknown_acks.value_namespace = name_space
                    self.qad_unknown_acks.value_namespace_prefix = name_space_prefix
                if(value_path == "resumes"):
                    self.resumes = value
                    self.resumes.value_namespace = name_space
                    self.resumes.value_namespace_prefix = name_space_prefix
                if(value_path == "sends-failed"):
                    self.sends_failed = value
                    self.sends_failed.value_namespace = name_space
                    self.sends_failed.value_namespace_prefix = name_space_prefix
                if(value_path == "sends-fragment"):
                    self.sends_fragment = value
                    self.sends_fragment.value_namespace = name_space
                    self.sends_fragment.value_namespace_prefix = name_space_prefix
                if(value_path == "suspends"):
                    self.suspends = value
                    self.suspends.value_namespace = name_space
                    self.suspends.value_namespace_prefix = name_space_prefix
                if(value_path == "timeouts"):
                    self.timeouts = value
                    self.timeouts.value_namespace = name_space
                    self.timeouts.value_namespace_prefix = name_space_prefix


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

                self.acks_recvd = YLeaf(YType.uint32, "acks-recvd")

                self.init_drops = YLeaf(YType.uint32, "init-drops")

                self.msg_drops = YLeaf(YType.uint32, "msg-drops")

                self.msgs_recvd = YLeaf(YType.uint32, "msgs-recvd")

                self.ooo_drops = YLeaf(YType.uint32, "ooo-drops")

                self.recvd_acks_failed = YLeaf(YType.uint32, "recvd-acks-failed")

                self.stale_msgs = YLeaf(YType.uint32, "stale-msgs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("acks_recvd",
                                "init_drops",
                                "msg_drops",
                                "msgs_recvd",
                                "ooo_drops",
                                "recvd_acks_failed",
                                "stale_msgs") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.VpdnMirroring.QadRecvStats, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.VpdnMirroring.QadRecvStats, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.acks_recvd.is_set or
                    self.init_drops.is_set or
                    self.msg_drops.is_set or
                    self.msgs_recvd.is_set or
                    self.ooo_drops.is_set or
                    self.recvd_acks_failed.is_set or
                    self.stale_msgs.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.acks_recvd.yfilter != YFilter.not_set or
                    self.init_drops.yfilter != YFilter.not_set or
                    self.msg_drops.yfilter != YFilter.not_set or
                    self.msgs_recvd.yfilter != YFilter.not_set or
                    self.ooo_drops.yfilter != YFilter.not_set or
                    self.recvd_acks_failed.yfilter != YFilter.not_set or
                    self.stale_msgs.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qad-recv-stats" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.acks_recvd.is_set or self.acks_recvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.acks_recvd.get_name_leafdata())
                if (self.init_drops.is_set or self.init_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.init_drops.get_name_leafdata())
                if (self.msg_drops.is_set or self.msg_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msg_drops.get_name_leafdata())
                if (self.msgs_recvd.is_set or self.msgs_recvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msgs_recvd.get_name_leafdata())
                if (self.ooo_drops.is_set or self.ooo_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ooo_drops.get_name_leafdata())
                if (self.recvd_acks_failed.is_set or self.recvd_acks_failed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.recvd_acks_failed.get_name_leafdata())
                if (self.stale_msgs.is_set or self.stale_msgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stale_msgs.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "acks-recvd" or name == "init-drops" or name == "msg-drops" or name == "msgs-recvd" or name == "ooo-drops" or name == "recvd-acks-failed" or name == "stale-msgs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "acks-recvd"):
                    self.acks_recvd = value
                    self.acks_recvd.value_namespace = name_space
                    self.acks_recvd.value_namespace_prefix = name_space_prefix
                if(value_path == "init-drops"):
                    self.init_drops = value
                    self.init_drops.value_namespace = name_space
                    self.init_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "msg-drops"):
                    self.msg_drops = value
                    self.msg_drops.value_namespace = name_space
                    self.msg_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "msgs-recvd"):
                    self.msgs_recvd = value
                    self.msgs_recvd.value_namespace = name_space
                    self.msgs_recvd.value_namespace_prefix = name_space_prefix
                if(value_path == "ooo-drops"):
                    self.ooo_drops = value
                    self.ooo_drops.value_namespace = name_space
                    self.ooo_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "recvd-acks-failed"):
                    self.recvd_acks_failed = value
                    self.recvd_acks_failed.value_namespace = name_space
                    self.recvd_acks_failed.value_namespace_prefix = name_space_prefix
                if(value_path == "stale-msgs"):
                    self.stale_msgs = value
                    self.stale_msgs.value_namespace = name_space
                    self.stale_msgs.value_namespace_prefix = name_space_prefix


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("acks_failed",
                                "acks_sent",
                                "msgs_sent",
                                "no_partner",
                                "pending_acks",
                                "qad_ack_count",
                                "qad_frag_count",
                                "qad_last_seq_number",
                                "qad_rx_count",
                                "qad_rx_first_seq_number",
                                "qad_rx_list_count",
                                "qad_rx_list_q_size",
                                "qad_timeouts",
                                "qad_unknown_acks",
                                "resumes",
                                "sends_failed",
                                "sends_fragment",
                                "suspends",
                                "timeouts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.VpdnMirroring.QadSendStatsLastClear, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.VpdnMirroring.QadSendStatsLastClear, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.acks_failed.is_set or
                    self.acks_sent.is_set or
                    self.msgs_sent.is_set or
                    self.no_partner.is_set or
                    self.pending_acks.is_set or
                    self.qad_ack_count.is_set or
                    self.qad_frag_count.is_set or
                    self.qad_last_seq_number.is_set or
                    self.qad_rx_count.is_set or
                    self.qad_rx_first_seq_number.is_set or
                    self.qad_rx_list_count.is_set or
                    self.qad_rx_list_q_size.is_set or
                    self.qad_timeouts.is_set or
                    self.qad_unknown_acks.is_set or
                    self.resumes.is_set or
                    self.sends_failed.is_set or
                    self.sends_fragment.is_set or
                    self.suspends.is_set or
                    self.timeouts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.acks_failed.yfilter != YFilter.not_set or
                    self.acks_sent.yfilter != YFilter.not_set or
                    self.msgs_sent.yfilter != YFilter.not_set or
                    self.no_partner.yfilter != YFilter.not_set or
                    self.pending_acks.yfilter != YFilter.not_set or
                    self.qad_ack_count.yfilter != YFilter.not_set or
                    self.qad_frag_count.yfilter != YFilter.not_set or
                    self.qad_last_seq_number.yfilter != YFilter.not_set or
                    self.qad_rx_count.yfilter != YFilter.not_set or
                    self.qad_rx_first_seq_number.yfilter != YFilter.not_set or
                    self.qad_rx_list_count.yfilter != YFilter.not_set or
                    self.qad_rx_list_q_size.yfilter != YFilter.not_set or
                    self.qad_timeouts.yfilter != YFilter.not_set or
                    self.qad_unknown_acks.yfilter != YFilter.not_set or
                    self.resumes.yfilter != YFilter.not_set or
                    self.sends_failed.yfilter != YFilter.not_set or
                    self.sends_fragment.yfilter != YFilter.not_set or
                    self.suspends.yfilter != YFilter.not_set or
                    self.timeouts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qad-send-stats-last-clear" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.acks_failed.is_set or self.acks_failed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.acks_failed.get_name_leafdata())
                if (self.acks_sent.is_set or self.acks_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.acks_sent.get_name_leafdata())
                if (self.msgs_sent.is_set or self.msgs_sent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msgs_sent.get_name_leafdata())
                if (self.no_partner.is_set or self.no_partner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.no_partner.get_name_leafdata())
                if (self.pending_acks.is_set or self.pending_acks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pending_acks.get_name_leafdata())
                if (self.qad_ack_count.is_set or self.qad_ack_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_ack_count.get_name_leafdata())
                if (self.qad_frag_count.is_set or self.qad_frag_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_frag_count.get_name_leafdata())
                if (self.qad_last_seq_number.is_set or self.qad_last_seq_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_last_seq_number.get_name_leafdata())
                if (self.qad_rx_count.is_set or self.qad_rx_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_count.get_name_leafdata())
                if (self.qad_rx_first_seq_number.is_set or self.qad_rx_first_seq_number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_first_seq_number.get_name_leafdata())
                if (self.qad_rx_list_count.is_set or self.qad_rx_list_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_list_count.get_name_leafdata())
                if (self.qad_rx_list_q_size.is_set or self.qad_rx_list_q_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_rx_list_q_size.get_name_leafdata())
                if (self.qad_timeouts.is_set or self.qad_timeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_timeouts.get_name_leafdata())
                if (self.qad_unknown_acks.is_set or self.qad_unknown_acks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.qad_unknown_acks.get_name_leafdata())
                if (self.resumes.is_set or self.resumes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.resumes.get_name_leafdata())
                if (self.sends_failed.is_set or self.sends_failed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sends_failed.get_name_leafdata())
                if (self.sends_fragment.is_set or self.sends_fragment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sends_fragment.get_name_leafdata())
                if (self.suspends.is_set or self.suspends.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.suspends.get_name_leafdata())
                if (self.timeouts.is_set or self.timeouts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.timeouts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "acks-failed" or name == "acks-sent" or name == "msgs-sent" or name == "no-partner" or name == "pending-acks" or name == "qad-ack-count" or name == "qad-frag-count" or name == "qad-last-seq-number" or name == "qad-rx-count" or name == "qad-rx-first-seq-number" or name == "qad-rx-list-count" or name == "qad-rx-list-q-size" or name == "qad-timeouts" or name == "qad-unknown-acks" or name == "resumes" or name == "sends-failed" or name == "sends-fragment" or name == "suspends" or name == "timeouts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "acks-failed"):
                    self.acks_failed = value
                    self.acks_failed.value_namespace = name_space
                    self.acks_failed.value_namespace_prefix = name_space_prefix
                if(value_path == "acks-sent"):
                    self.acks_sent = value
                    self.acks_sent.value_namespace = name_space
                    self.acks_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "msgs-sent"):
                    self.msgs_sent = value
                    self.msgs_sent.value_namespace = name_space
                    self.msgs_sent.value_namespace_prefix = name_space_prefix
                if(value_path == "no-partner"):
                    self.no_partner = value
                    self.no_partner.value_namespace = name_space
                    self.no_partner.value_namespace_prefix = name_space_prefix
                if(value_path == "pending-acks"):
                    self.pending_acks = value
                    self.pending_acks.value_namespace = name_space
                    self.pending_acks.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-ack-count"):
                    self.qad_ack_count = value
                    self.qad_ack_count.value_namespace = name_space
                    self.qad_ack_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-frag-count"):
                    self.qad_frag_count = value
                    self.qad_frag_count.value_namespace = name_space
                    self.qad_frag_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-last-seq-number"):
                    self.qad_last_seq_number = value
                    self.qad_last_seq_number.value_namespace = name_space
                    self.qad_last_seq_number.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-count"):
                    self.qad_rx_count = value
                    self.qad_rx_count.value_namespace = name_space
                    self.qad_rx_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-first-seq-number"):
                    self.qad_rx_first_seq_number = value
                    self.qad_rx_first_seq_number.value_namespace = name_space
                    self.qad_rx_first_seq_number.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-list-count"):
                    self.qad_rx_list_count = value
                    self.qad_rx_list_count.value_namespace = name_space
                    self.qad_rx_list_count.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-rx-list-q-size"):
                    self.qad_rx_list_q_size = value
                    self.qad_rx_list_q_size.value_namespace = name_space
                    self.qad_rx_list_q_size.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-timeouts"):
                    self.qad_timeouts = value
                    self.qad_timeouts.value_namespace = name_space
                    self.qad_timeouts.value_namespace_prefix = name_space_prefix
                if(value_path == "qad-unknown-acks"):
                    self.qad_unknown_acks = value
                    self.qad_unknown_acks.value_namespace = name_space
                    self.qad_unknown_acks.value_namespace_prefix = name_space_prefix
                if(value_path == "resumes"):
                    self.resumes = value
                    self.resumes.value_namespace = name_space
                    self.resumes.value_namespace_prefix = name_space_prefix
                if(value_path == "sends-failed"):
                    self.sends_failed = value
                    self.sends_failed.value_namespace = name_space
                    self.sends_failed.value_namespace_prefix = name_space_prefix
                if(value_path == "sends-fragment"):
                    self.sends_fragment = value
                    self.sends_fragment.value_namespace = name_space
                    self.sends_fragment.value_namespace_prefix = name_space_prefix
                if(value_path == "suspends"):
                    self.suspends = value
                    self.suspends.value_namespace = name_space
                    self.suspends.value_namespace_prefix = name_space_prefix
                if(value_path == "timeouts"):
                    self.timeouts = value
                    self.timeouts.value_namespace = name_space
                    self.timeouts.value_namespace_prefix = name_space_prefix


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

                self.acks_recvd = YLeaf(YType.uint32, "acks-recvd")

                self.init_drops = YLeaf(YType.uint32, "init-drops")

                self.msg_drops = YLeaf(YType.uint32, "msg-drops")

                self.msgs_recvd = YLeaf(YType.uint32, "msgs-recvd")

                self.ooo_drops = YLeaf(YType.uint32, "ooo-drops")

                self.recvd_acks_failed = YLeaf(YType.uint32, "recvd-acks-failed")

                self.stale_msgs = YLeaf(YType.uint32, "stale-msgs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("acks_recvd",
                                "init_drops",
                                "msg_drops",
                                "msgs_recvd",
                                "ooo_drops",
                                "recvd_acks_failed",
                                "stale_msgs") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.VpdnMirroring.QadRecvStatsLastClear, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.VpdnMirroring.QadRecvStatsLastClear, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.acks_recvd.is_set or
                    self.init_drops.is_set or
                    self.msg_drops.is_set or
                    self.msgs_recvd.is_set or
                    self.ooo_drops.is_set or
                    self.recvd_acks_failed.is_set or
                    self.stale_msgs.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.acks_recvd.yfilter != YFilter.not_set or
                    self.init_drops.yfilter != YFilter.not_set or
                    self.msg_drops.yfilter != YFilter.not_set or
                    self.msgs_recvd.yfilter != YFilter.not_set or
                    self.ooo_drops.yfilter != YFilter.not_set or
                    self.recvd_acks_failed.yfilter != YFilter.not_set or
                    self.stale_msgs.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "qad-recv-stats-last-clear" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/vpdn-mirroring/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.acks_recvd.is_set or self.acks_recvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.acks_recvd.get_name_leafdata())
                if (self.init_drops.is_set or self.init_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.init_drops.get_name_leafdata())
                if (self.msg_drops.is_set or self.msg_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msg_drops.get_name_leafdata())
                if (self.msgs_recvd.is_set or self.msgs_recvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msgs_recvd.get_name_leafdata())
                if (self.ooo_drops.is_set or self.ooo_drops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ooo_drops.get_name_leafdata())
                if (self.recvd_acks_failed.is_set or self.recvd_acks_failed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.recvd_acks_failed.get_name_leafdata())
                if (self.stale_msgs.is_set or self.stale_msgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.stale_msgs.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "acks-recvd" or name == "init-drops" or name == "msg-drops" or name == "msgs-recvd" or name == "ooo-drops" or name == "recvd-acks-failed" or name == "stale-msgs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "acks-recvd"):
                    self.acks_recvd = value
                    self.acks_recvd.value_namespace = name_space
                    self.acks_recvd.value_namespace_prefix = name_space_prefix
                if(value_path == "init-drops"):
                    self.init_drops = value
                    self.init_drops.value_namespace = name_space
                    self.init_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "msg-drops"):
                    self.msg_drops = value
                    self.msg_drops.value_namespace = name_space
                    self.msg_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "msgs-recvd"):
                    self.msgs_recvd = value
                    self.msgs_recvd.value_namespace = name_space
                    self.msgs_recvd.value_namespace_prefix = name_space_prefix
                if(value_path == "ooo-drops"):
                    self.ooo_drops = value
                    self.ooo_drops.value_namespace = name_space
                    self.ooo_drops.value_namespace_prefix = name_space_prefix
                if(value_path == "recvd-acks-failed"):
                    self.recvd_acks_failed = value
                    self.recvd_acks_failed.value_namespace = name_space
                    self.recvd_acks_failed.value_namespace_prefix = name_space_prefix
                if(value_path == "stale-msgs"):
                    self.stale_msgs = value
                    self.stale_msgs.value_namespace = name_space
                    self.stale_msgs.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.alloc_cnt.is_set or
                self.alloc_err_cnt.is_set or
                self.sso_batch_err_cnt.is_set or
                self.sso_err_cnt.is_set or
                self.sync_not_conn_cnt.is_set or
                (self.qad_recv_stats is not None and self.qad_recv_stats.has_data()) or
                (self.qad_recv_stats_last_clear is not None and self.qad_recv_stats_last_clear.has_data()) or
                (self.qad_send_stats is not None and self.qad_send_stats.has_data()) or
                (self.qad_send_stats_last_clear is not None and self.qad_send_stats_last_clear.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.alloc_cnt.yfilter != YFilter.not_set or
                self.alloc_err_cnt.yfilter != YFilter.not_set or
                self.sso_batch_err_cnt.yfilter != YFilter.not_set or
                self.sso_err_cnt.yfilter != YFilter.not_set or
                self.sync_not_conn_cnt.yfilter != YFilter.not_set or
                (self.qad_recv_stats is not None and self.qad_recv_stats.has_operation()) or
                (self.qad_recv_stats_last_clear is not None and self.qad_recv_stats_last_clear.has_operation()) or
                (self.qad_send_stats is not None and self.qad_send_stats.has_operation()) or
                (self.qad_send_stats_last_clear is not None and self.qad_send_stats_last_clear.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vpdn-mirroring" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.alloc_cnt.is_set or self.alloc_cnt.yfilter != YFilter.not_set):
                leaf_name_data.append(self.alloc_cnt.get_name_leafdata())
            if (self.alloc_err_cnt.is_set or self.alloc_err_cnt.yfilter != YFilter.not_set):
                leaf_name_data.append(self.alloc_err_cnt.get_name_leafdata())
            if (self.sso_batch_err_cnt.is_set or self.sso_batch_err_cnt.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sso_batch_err_cnt.get_name_leafdata())
            if (self.sso_err_cnt.is_set or self.sso_err_cnt.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sso_err_cnt.get_name_leafdata())
            if (self.sync_not_conn_cnt.is_set or self.sync_not_conn_cnt.yfilter != YFilter.not_set):
                leaf_name_data.append(self.sync_not_conn_cnt.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "qad-recv-stats"):
                if (self.qad_recv_stats is None):
                    self.qad_recv_stats = Vpdn.VpdnMirroring.QadRecvStats()
                    self.qad_recv_stats.parent = self
                    self._children_name_map["qad_recv_stats"] = "qad-recv-stats"
                return self.qad_recv_stats

            if (child_yang_name == "qad-recv-stats-last-clear"):
                if (self.qad_recv_stats_last_clear is None):
                    self.qad_recv_stats_last_clear = Vpdn.VpdnMirroring.QadRecvStatsLastClear()
                    self.qad_recv_stats_last_clear.parent = self
                    self._children_name_map["qad_recv_stats_last_clear"] = "qad-recv-stats-last-clear"
                return self.qad_recv_stats_last_clear

            if (child_yang_name == "qad-send-stats"):
                if (self.qad_send_stats is None):
                    self.qad_send_stats = Vpdn.VpdnMirroring.QadSendStats()
                    self.qad_send_stats.parent = self
                    self._children_name_map["qad_send_stats"] = "qad-send-stats"
                return self.qad_send_stats

            if (child_yang_name == "qad-send-stats-last-clear"):
                if (self.qad_send_stats_last_clear is None):
                    self.qad_send_stats_last_clear = Vpdn.VpdnMirroring.QadSendStatsLastClear()
                    self.qad_send_stats_last_clear.parent = self
                    self._children_name_map["qad_send_stats_last_clear"] = "qad-send-stats-last-clear"
                return self.qad_send_stats_last_clear

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "qad-recv-stats" or name == "qad-recv-stats-last-clear" or name == "qad-send-stats" or name == "qad-send-stats-last-clear" or name == "alloc-cnt" or name == "alloc-err-cnt" or name == "sso-batch-err-cnt" or name == "sso-err-cnt" or name == "sync-not-conn-cnt"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "alloc-cnt"):
                self.alloc_cnt = value
                self.alloc_cnt.value_namespace = name_space
                self.alloc_cnt.value_namespace_prefix = name_space_prefix
            if(value_path == "alloc-err-cnt"):
                self.alloc_err_cnt = value
                self.alloc_err_cnt.value_namespace = name_space
                self.alloc_err_cnt.value_namespace_prefix = name_space_prefix
            if(value_path == "sso-batch-err-cnt"):
                self.sso_batch_err_cnt = value
                self.sso_batch_err_cnt.value_namespace = name_space
                self.sso_batch_err_cnt.value_namespace_prefix = name_space_prefix
            if(value_path == "sso-err-cnt"):
                self.sso_err_cnt = value
                self.sso_err_cnt.value_namespace = name_space
                self.sso_err_cnt.value_namespace_prefix = name_space_prefix
            if(value_path == "sync-not-conn-cnt"):
                self.sync_not_conn_cnt = value
                self.sync_not_conn_cnt.value_namespace = name_space
                self.sync_not_conn_cnt.value_namespace_prefix = name_space_prefix


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

            self.abort_time = YLeaf(YType.uint64, "abort-time")

            self.finish_time = YLeaf(YType.uint64, "finish-time")

            self.session_synced = YLeaf(YType.uint32, "session-synced")

            self.session_total = YLeaf(YType.uint32, "session-total")

            self.start_time = YLeaf(YType.uint64, "start-time")

            self.state = YLeaf(YType.enumeration, "state")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("abort_time",
                            "finish_time",
                            "session_synced",
                            "session_total",
                            "start_time",
                            "state") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.VpdnRedundancy, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.VpdnRedundancy, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.abort_time.is_set or
                self.finish_time.is_set or
                self.session_synced.is_set or
                self.session_total.is_set or
                self.start_time.is_set or
                self.state.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.abort_time.yfilter != YFilter.not_set or
                self.finish_time.yfilter != YFilter.not_set or
                self.session_synced.yfilter != YFilter.not_set or
                self.session_total.yfilter != YFilter.not_set or
                self.start_time.yfilter != YFilter.not_set or
                self.state.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vpdn-redundancy" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.abort_time.is_set or self.abort_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.abort_time.get_name_leafdata())
            if (self.finish_time.is_set or self.finish_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.finish_time.get_name_leafdata())
            if (self.session_synced.is_set or self.session_synced.yfilter != YFilter.not_set):
                leaf_name_data.append(self.session_synced.get_name_leafdata())
            if (self.session_total.is_set or self.session_total.yfilter != YFilter.not_set):
                leaf_name_data.append(self.session_total.get_name_leafdata())
            if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                leaf_name_data.append(self.start_time.get_name_leafdata())
            if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                leaf_name_data.append(self.state.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "abort-time" or name == "finish-time" or name == "session-synced" or name == "session-total" or name == "start-time" or name == "state"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "abort-time"):
                self.abort_time = value
                self.abort_time.value_namespace = name_space
                self.abort_time.value_namespace_prefix = name_space_prefix
            if(value_path == "finish-time"):
                self.finish_time = value
                self.finish_time.value_namespace = name_space
                self.finish_time.value_namespace_prefix = name_space_prefix
            if(value_path == "session-synced"):
                self.session_synced = value
                self.session_synced.value_namespace = name_space
                self.session_synced.value_namespace_prefix = name_space_prefix
            if(value_path == "session-total"):
                self.session_total = value
                self.session_total.value_namespace = name_space
                self.session_total.value_namespace_prefix = name_space_prefix
            if(value_path == "start-time"):
                self.start_time = value
                self.start_time.value_namespace = name_space
                self.start_time.value_namespace_prefix = name_space_prefix
            if(value_path == "state"):
                self.state = value
                self.state.value_namespace = name_space
                self.state.value_namespace_prefix = name_space_prefix


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

            self.history_failure = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.HistoryFailures, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.HistoryFailures, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("destination_address",
                                "domain_name",
                                "error_repeat_count",
                                "event_time",
                                "failure_type",
                                "home_gateway",
                                "local_client_id",
                                "mid",
                                "nas",
                                "remote_client_id",
                                "remote_name",
                                "source_address",
                                "username",
                                "username_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.HistoryFailures.HistoryFailure, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.HistoryFailures.HistoryFailure, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.destination_address.is_set or
                    self.domain_name.is_set or
                    self.error_repeat_count.is_set or
                    self.event_time.is_set or
                    self.failure_type.is_set or
                    self.home_gateway.is_set or
                    self.local_client_id.is_set or
                    self.mid.is_set or
                    self.nas.is_set or
                    self.remote_client_id.is_set or
                    self.remote_name.is_set or
                    self.source_address.is_set or
                    self.username.is_set or
                    self.username_xr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.destination_address.yfilter != YFilter.not_set or
                    self.domain_name.yfilter != YFilter.not_set or
                    self.error_repeat_count.yfilter != YFilter.not_set or
                    self.event_time.yfilter != YFilter.not_set or
                    self.failure_type.yfilter != YFilter.not_set or
                    self.home_gateway.yfilter != YFilter.not_set or
                    self.local_client_id.yfilter != YFilter.not_set or
                    self.mid.yfilter != YFilter.not_set or
                    self.nas.yfilter != YFilter.not_set or
                    self.remote_client_id.yfilter != YFilter.not_set or
                    self.remote_name.yfilter != YFilter.not_set or
                    self.source_address.yfilter != YFilter.not_set or
                    self.username.yfilter != YFilter.not_set or
                    self.username_xr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "history-failure" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/history-failures/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.destination_address.get_name_leafdata())
                if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.domain_name.get_name_leafdata())
                if (self.error_repeat_count.is_set or self.error_repeat_count.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.error_repeat_count.get_name_leafdata())
                if (self.event_time.is_set or self.event_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.event_time.get_name_leafdata())
                if (self.failure_type.is_set or self.failure_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.failure_type.get_name_leafdata())
                if (self.home_gateway.is_set or self.home_gateway.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.home_gateway.get_name_leafdata())
                if (self.local_client_id.is_set or self.local_client_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_client_id.get_name_leafdata())
                if (self.mid.is_set or self.mid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mid.get_name_leafdata())
                if (self.nas.is_set or self.nas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nas.get_name_leafdata())
                if (self.remote_client_id.is_set or self.remote_client_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_client_id.get_name_leafdata())
                if (self.remote_name.is_set or self.remote_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.remote_name.get_name_leafdata())
                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_address.get_name_leafdata())
                if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.username.get_name_leafdata())
                if (self.username_xr.is_set or self.username_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.username_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "destination-address" or name == "domain-name" or name == "error-repeat-count" or name == "event-time" or name == "failure-type" or name == "home-gateway" or name == "local-client-id" or name == "mid" or name == "nas" or name == "remote-client-id" or name == "remote-name" or name == "source-address" or name == "username" or name == "username-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "destination-address"):
                    self.destination_address = value
                    self.destination_address.value_namespace = name_space
                    self.destination_address.value_namespace_prefix = name_space_prefix
                if(value_path == "domain-name"):
                    self.domain_name = value
                    self.domain_name.value_namespace = name_space
                    self.domain_name.value_namespace_prefix = name_space_prefix
                if(value_path == "error-repeat-count"):
                    self.error_repeat_count = value
                    self.error_repeat_count.value_namespace = name_space
                    self.error_repeat_count.value_namespace_prefix = name_space_prefix
                if(value_path == "event-time"):
                    self.event_time = value
                    self.event_time.value_namespace = name_space
                    self.event_time.value_namespace_prefix = name_space_prefix
                if(value_path == "failure-type"):
                    self.failure_type = value
                    self.failure_type.value_namespace = name_space
                    self.failure_type.value_namespace_prefix = name_space_prefix
                if(value_path == "home-gateway"):
                    self.home_gateway = value
                    self.home_gateway.value_namespace = name_space
                    self.home_gateway.value_namespace_prefix = name_space_prefix
                if(value_path == "local-client-id"):
                    self.local_client_id = value
                    self.local_client_id.value_namespace = name_space
                    self.local_client_id.value_namespace_prefix = name_space_prefix
                if(value_path == "mid"):
                    self.mid = value
                    self.mid.value_namespace = name_space
                    self.mid.value_namespace_prefix = name_space_prefix
                if(value_path == "nas"):
                    self.nas = value
                    self.nas.value_namespace = name_space
                    self.nas.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-client-id"):
                    self.remote_client_id = value
                    self.remote_client_id.value_namespace = name_space
                    self.remote_client_id.value_namespace_prefix = name_space_prefix
                if(value_path == "remote-name"):
                    self.remote_name = value
                    self.remote_name.value_namespace = name_space
                    self.remote_name.value_namespace_prefix = name_space_prefix
                if(value_path == "source-address"):
                    self.source_address = value
                    self.source_address.value_namespace = name_space
                    self.source_address.value_namespace_prefix = name_space_prefix
                if(value_path == "username"):
                    self.username = value
                    self.username.value_namespace = name_space
                    self.username.value_namespace_prefix = name_space_prefix
                if(value_path == "username-xr"):
                    self.username_xr = value
                    self.username_xr.value_namespace = name_space
                    self.username_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.history_failure:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.history_failure:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "history-failures" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "history-failure"):
                for c in self.history_failure:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vpdn.HistoryFailures.HistoryFailure()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.history_failure.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "history-failure"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.history_failures is not None and self.history_failures.has_data()) or
            (self.sessions is not None and self.sessions.has_data()) or
            (self.tunnel_destinations is not None and self.tunnel_destinations.has_data()) or
            (self.vpdn_mirroring is not None and self.vpdn_mirroring.has_data()) or
            (self.vpdn_redundancy is not None and self.vpdn_redundancy.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.history_failures is not None and self.history_failures.has_operation()) or
            (self.sessions is not None and self.sessions.has_operation()) or
            (self.tunnel_destinations is not None and self.tunnel_destinations.has_operation()) or
            (self.vpdn_mirroring is not None and self.vpdn_mirroring.has_operation()) or
            (self.vpdn_redundancy is not None and self.vpdn_redundancy.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "history-failures"):
            if (self.history_failures is None):
                self.history_failures = Vpdn.HistoryFailures()
                self.history_failures.parent = self
                self._children_name_map["history_failures"] = "history-failures"
            return self.history_failures

        if (child_yang_name == "sessions"):
            if (self.sessions is None):
                self.sessions = Vpdn.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
            return self.sessions

        if (child_yang_name == "tunnel-destinations"):
            if (self.tunnel_destinations is None):
                self.tunnel_destinations = Vpdn.TunnelDestinations()
                self.tunnel_destinations.parent = self
                self._children_name_map["tunnel_destinations"] = "tunnel-destinations"
            return self.tunnel_destinations

        if (child_yang_name == "vpdn-mirroring"):
            if (self.vpdn_mirroring is None):
                self.vpdn_mirroring = Vpdn.VpdnMirroring()
                self.vpdn_mirroring.parent = self
                self._children_name_map["vpdn_mirroring"] = "vpdn-mirroring"
            return self.vpdn_mirroring

        if (child_yang_name == "vpdn-redundancy"):
            if (self.vpdn_redundancy is None):
                self.vpdn_redundancy = Vpdn.VpdnRedundancy()
                self.vpdn_redundancy.parent = self
                self._children_name_map["vpdn_redundancy"] = "vpdn-redundancy"
            return self.vpdn_redundancy

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "history-failures" or name == "sessions" or name == "tunnel-destinations" or name == "vpdn-mirroring" or name == "vpdn-redundancy"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vpdn()
        return self._top_entity

