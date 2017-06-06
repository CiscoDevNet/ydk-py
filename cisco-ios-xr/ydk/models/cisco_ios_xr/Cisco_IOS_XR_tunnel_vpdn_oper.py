""" Cisco_IOS_XR_tunnel_vpdn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package operational data.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LsgStatusEnum(Enum):
    """
    LsgStatusEnum

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

    none = 0

    active = 1

    down = 2

    testable = 3

    testing = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['LsgStatusEnum']


class SessionStateEnum(Enum):
    """
    SessionStateEnum

    Session states

    .. data:: idle = 0

    	Idle state

    .. data:: connected = 1

    	Connected state

    .. data:: established = 2

    	Established state

    """

    idle = 0

    connected = 1

    established = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['SessionStateEnum']


class TosModeEnum(Enum):
    """
    TosModeEnum

    TOS modes

    .. data:: default = 0

    	default

    .. data:: set = 1

    	set

    .. data:: reflect = 2

    	reflect

    """

    default = 0

    set = 1

    reflect = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['TosModeEnum']


class VpdnFailcodeEnum(Enum):
    """
    VpdnFailcodeEnum

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

    unknown = 0

    peer_action = 1

    authentication = 2

    authentication_error = 3

    authentication_failed = 4

    authorization = 5

    authorization_failed = 6

    home_gatewayfailure = 7

    connection_termination = 8

    no_resources_available = 9

    timer_expiry = 10

    session_mid_exceeded = 11

    soft_shut = 12

    session_limit_exceeded = 13

    administrative = 14

    link_failure = 15

    security = 16

    tunnel_in_resync = 17

    call_prarmeters = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['VpdnFailcodeEnum']


class VpdnNasPortEnum(Enum):
    """
    VpdnNasPortEnum

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

    none = 0

    primary = 1

    bri = 2

    serial = 3

    asynchronous = 4

    vty = 5

    atm = 6

    ethernet = 7

    ppp_atm = 8

    pppoe_over_atm = 9

    pppoe_over_ethernet = 10

    pppoe_over_vlan = 11

    pppoe_over_q_in_q = 12

    v120 = 13

    v110 = 14

    piafs = 15

    x75 = 16

    ip_sec = 17

    other = 18

    virtual_pppoe_over_ethernet = 19

    virtual_pppoe_over_vlan = 20

    virtual_pppoe_over_q_in_q = 21

    ipo_e_over_ethernet = 22

    ipo_e_over_vlan = 23

    ipo_e_over_q_in_q = 24

    virtual_i_po_e_over_ethernet = 25

    virtual_i_po_e_over_vlan = 26

    virtual_i_po_e_over_q_in_q = 27

    unknown = 28


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['VpdnNasPortEnum']


class VpdnStateEnum(Enum):
    """
    VpdnStateEnum

    Vpdn states

    .. data:: initial_state = 0

    	Initial state

    .. data:: init_sync_in_progress = 1

    	Initial Sync in progress

    .. data:: steady_state = 2

    	Initial Sync Done

    """

    initial_state = 0

    init_sync_in_progress = 1

    steady_state = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['VpdnStateEnum']



class Vpdn(object):
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
        self.history_failures = Vpdn.HistoryFailures()
        self.history_failures.parent = self
        self.sessions = Vpdn.Sessions()
        self.sessions.parent = self
        self.tunnel_destinations = Vpdn.TunnelDestinations()
        self.tunnel_destinations.parent = self
        self.vpdn_mirroring = Vpdn.VpdnMirroring()
        self.vpdn_mirroring.parent = self
        self.vpdn_redundancy = Vpdn.VpdnRedundancy()
        self.vpdn_redundancy.parent = self


    class Sessions(object):
        """
        VPDN session list
        
        .. attribute:: session
        
        	 VPDN session information
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.session = YList()
            self.session.parent = self
            self.session.name = 'session'


        class Session(object):
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
            	**type**\:   :py:class:`Session_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Sessions.Session.Session_>`
            
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
                self.parent = None
                self.session_label = None
                self.configuration = Vpdn.Sessions.Session.Configuration()
                self.configuration.parent = self
                self.l2tp = Vpdn.Sessions.Session.L2Tp()
                self.l2tp.parent = self
                self.parent_interface_name = None
                self.session = Vpdn.Sessions.Session.Session_()
                self.session.parent = self
                self.setup_time = None
                self.subscriber = Vpdn.Sessions.Session.Subscriber()
                self.subscriber.parent = self


            class Session_(object):
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
                	**type**\:   :py:class:`SessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.SessionStateEnum>`
                
                .. attribute:: username
                
                	Authentication username
                	**type**\:  str
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.domain_name = None
                    self.interface_name = None
                    self.l2tp_session_id = None
                    self.l2tp_tunnel_id = None
                    self.last_change = None
                    self.srg_slave = None
                    self.state = None
                    self.username = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-oper:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.domain_name is not None:
                        return True

                    if self.interface_name is not None:
                        return True

                    if self.l2tp_session_id is not None:
                        return True

                    if self.l2tp_tunnel_id is not None:
                        return True

                    if self.last_change is not None:
                        return True

                    if self.srg_slave is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.username is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Sessions.Session.Session_']['meta_info']


            class L2Tp(object):
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
                    self.parent = None
                    self.call_serial_number = None
                    self.is_l2tp_class_attribute_mask_set = None
                    self.is_tunnel_authentication_enabled = None
                    self.local_endpoint = None
                    self.local_session_id = None
                    self.local_tunnel_id = None
                    self.remote_endpoint = None
                    self.remote_port = None
                    self.remote_session_id = None
                    self.remote_tunnel_id = None
                    self.tunnel_assignment_id = None
                    self.tunnel_client_authentication_id = None
                    self.tunnel_server_authentication_id = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-oper:l2tp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.call_serial_number is not None:
                        return True

                    if self.is_l2tp_class_attribute_mask_set is not None:
                        return True

                    if self.is_tunnel_authentication_enabled is not None:
                        return True

                    if self.local_endpoint is not None:
                        return True

                    if self.local_session_id is not None:
                        return True

                    if self.local_tunnel_id is not None:
                        return True

                    if self.remote_endpoint is not None:
                        return True

                    if self.remote_port is not None:
                        return True

                    if self.remote_session_id is not None:
                        return True

                    if self.remote_tunnel_id is not None:
                        return True

                    if self.tunnel_assignment_id is not None:
                        return True

                    if self.tunnel_client_authentication_id is not None:
                        return True

                    if self.tunnel_server_authentication_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Sessions.Session.L2Tp']['meta_info']


            class Subscriber(object):
                """
                Subscriber data
                
                .. attribute:: nas_port
                
                	NAS port ID
                	**type**\:  list of int
                
                	**range:** 0..255
                
                .. attribute:: nas_port_type
                
                	NAS port type
                	**type**\:   :py:class:`VpdnNasPortEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnNasPortEnum>`
                
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
                    self.parent = None
                    self.nas_port = YLeafList()
                    self.nas_port.parent = self
                    self.nas_port.name = 'nas_port'
                    self.nas_port_type = None
                    self.physical_channel_id = None
                    self.receive_connect_speed = None
                    self.transmit_connect_speed = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-oper:subscriber'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.nas_port is not None:
                        for child in self.nas_port:
                            if child is not None:
                                return True

                    if self.nas_port_type is not None:
                        return True

                    if self.physical_channel_id is not None:
                        return True

                    if self.receive_connect_speed is not None:
                        return True

                    if self.transmit_connect_speed is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Sessions.Session.Subscriber']['meta_info']


            class Configuration(object):
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
                	**type**\:   :py:class:`TosModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.TosModeEnum>`
                
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
                    self.parent = None
                    self.dsl_line_forwarding = None
                    self.l2tp_busy_timeout = None
                    self.template_name = None
                    self.tos = None
                    self.tos_mode = None
                    self.vpn_id = Vpdn.Sessions.Session.Configuration.VpnId()
                    self.vpn_id.parent = self
                    self.vrf_name = None


                class VpnId(object):
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
                        self.parent = None
                        self.index = None
                        self.oui = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-oper:vpn-id'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.index is not None:
                            return True

                        if self.oui is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Sessions.Session.Configuration.VpnId']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-tunnel-vpdn-oper:configuration'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.dsl_line_forwarding is not None:
                        return True

                    if self.l2tp_busy_timeout is not None:
                        return True

                    if self.template_name is not None:
                        return True

                    if self.tos is not None:
                        return True

                    if self.tos_mode is not None:
                        return True

                    if self.vpn_id is not None and self.vpn_id._has_data():
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Sessions.Session.Configuration']['meta_info']

            @property
            def _common_path(self):
                if self.session_label is None:
                    raise YPYModelError('Key property session_label is None')

                return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:sessions/Cisco-IOS-XR-tunnel-vpdn-oper:session[Cisco-IOS-XR-tunnel-vpdn-oper:session-label = ' + str(self.session_label) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.session_label is not None:
                    return True

                if self.configuration is not None and self.configuration._has_data():
                    return True

                if self.l2tp is not None and self.l2tp._has_data():
                    return True

                if self.parent_interface_name is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                if self.setup_time is not None:
                    return True

                if self.subscriber is not None and self.subscriber._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.Sessions.Session']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:sessions'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.session is not None:
                for child_ref in self.session:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
            return meta._meta_table['Vpdn.Sessions']['meta_info']


    class TunnelDestinations(object):
        """
        VPDN tunnel Destinations
        
        .. attribute:: tunnel_destination
        
        	VPDN tunnel destination information
        	**type**\: list of    :py:class:`TunnelDestination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.TunnelDestinations.TunnelDestination>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.tunnel_destination = YList()
            self.tunnel_destination.parent = self
            self.tunnel_destination.name = 'tunnel_destination'


        class TunnelDestination(object):
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
            	**type**\:   :py:class:`LsgStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.LsgStatusEnum>`
            
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
                self.parent = None
                self.address = None
                self.connects = None
                self.disconnects = None
                self.load = None
                self.retry = None
                self.status = None
                self.status_change_time = None
                self.vrf_name = None
                self.vrf_name_xr = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:tunnel-destinations/Cisco-IOS-XR-tunnel-vpdn-oper:tunnel-destination'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.address is not None:
                    return True

                if self.connects is not None:
                    return True

                if self.disconnects is not None:
                    return True

                if self.load is not None:
                    return True

                if self.retry is not None:
                    return True

                if self.status is not None:
                    return True

                if self.status_change_time is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.vrf_name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.TunnelDestinations.TunnelDestination']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:tunnel-destinations'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tunnel_destination is not None:
                for child_ref in self.tunnel_destination:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
            return meta._meta_table['Vpdn.TunnelDestinations']['meta_info']


    class VpdnMirroring(object):
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
            self.parent = None
            self.alloc_cnt = None
            self.alloc_err_cnt = None
            self.qad_recv_stats = Vpdn.VpdnMirroring.QadRecvStats()
            self.qad_recv_stats.parent = self
            self.qad_recv_stats_last_clear = Vpdn.VpdnMirroring.QadRecvStatsLastClear()
            self.qad_recv_stats_last_clear.parent = self
            self.qad_send_stats = Vpdn.VpdnMirroring.QadSendStats()
            self.qad_send_stats.parent = self
            self.qad_send_stats_last_clear = Vpdn.VpdnMirroring.QadSendStatsLastClear()
            self.qad_send_stats_last_clear.parent = self
            self.sso_batch_err_cnt = None
            self.sso_err_cnt = None
            self.sync_not_conn_cnt = None


        class QadSendStats(object):
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
                self.parent = None
                self.acks_failed = None
                self.acks_sent = None
                self.msgs_sent = None
                self.no_partner = None
                self.pending_acks = None
                self.qad_ack_count = None
                self.qad_frag_count = None
                self.qad_last_seq_number = None
                self.qad_rx_count = None
                self.qad_rx_first_seq_number = None
                self.qad_rx_list_count = None
                self.qad_rx_list_q_size = None
                self.qad_timeouts = None
                self.qad_unknown_acks = None
                self.resumes = None
                self.sends_failed = None
                self.sends_fragment = None
                self.suspends = None
                self.timeouts = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn-mirroring/Cisco-IOS-XR-tunnel-vpdn-oper:qad-send-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.acks_failed is not None:
                    return True

                if self.acks_sent is not None:
                    return True

                if self.msgs_sent is not None:
                    return True

                if self.no_partner is not None:
                    return True

                if self.pending_acks is not None:
                    return True

                if self.qad_ack_count is not None:
                    return True

                if self.qad_frag_count is not None:
                    return True

                if self.qad_last_seq_number is not None:
                    return True

                if self.qad_rx_count is not None:
                    return True

                if self.qad_rx_first_seq_number is not None:
                    return True

                if self.qad_rx_list_count is not None:
                    return True

                if self.qad_rx_list_q_size is not None:
                    return True

                if self.qad_timeouts is not None:
                    return True

                if self.qad_unknown_acks is not None:
                    return True

                if self.resumes is not None:
                    return True

                if self.sends_failed is not None:
                    return True

                if self.sends_fragment is not None:
                    return True

                if self.suspends is not None:
                    return True

                if self.timeouts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.VpdnMirroring.QadSendStats']['meta_info']


        class QadRecvStats(object):
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
                self.parent = None
                self.acks_recvd = None
                self.init_drops = None
                self.msg_drops = None
                self.msgs_recvd = None
                self.ooo_drops = None
                self.recvd_acks_failed = None
                self.stale_msgs = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn-mirroring/Cisco-IOS-XR-tunnel-vpdn-oper:qad-recv-stats'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.acks_recvd is not None:
                    return True

                if self.init_drops is not None:
                    return True

                if self.msg_drops is not None:
                    return True

                if self.msgs_recvd is not None:
                    return True

                if self.ooo_drops is not None:
                    return True

                if self.recvd_acks_failed is not None:
                    return True

                if self.stale_msgs is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.VpdnMirroring.QadRecvStats']['meta_info']


        class QadSendStatsLastClear(object):
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
                self.parent = None
                self.acks_failed = None
                self.acks_sent = None
                self.msgs_sent = None
                self.no_partner = None
                self.pending_acks = None
                self.qad_ack_count = None
                self.qad_frag_count = None
                self.qad_last_seq_number = None
                self.qad_rx_count = None
                self.qad_rx_first_seq_number = None
                self.qad_rx_list_count = None
                self.qad_rx_list_q_size = None
                self.qad_timeouts = None
                self.qad_unknown_acks = None
                self.resumes = None
                self.sends_failed = None
                self.sends_fragment = None
                self.suspends = None
                self.timeouts = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn-mirroring/Cisco-IOS-XR-tunnel-vpdn-oper:qad-send-stats-last-clear'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.acks_failed is not None:
                    return True

                if self.acks_sent is not None:
                    return True

                if self.msgs_sent is not None:
                    return True

                if self.no_partner is not None:
                    return True

                if self.pending_acks is not None:
                    return True

                if self.qad_ack_count is not None:
                    return True

                if self.qad_frag_count is not None:
                    return True

                if self.qad_last_seq_number is not None:
                    return True

                if self.qad_rx_count is not None:
                    return True

                if self.qad_rx_first_seq_number is not None:
                    return True

                if self.qad_rx_list_count is not None:
                    return True

                if self.qad_rx_list_q_size is not None:
                    return True

                if self.qad_timeouts is not None:
                    return True

                if self.qad_unknown_acks is not None:
                    return True

                if self.resumes is not None:
                    return True

                if self.sends_failed is not None:
                    return True

                if self.sends_fragment is not None:
                    return True

                if self.suspends is not None:
                    return True

                if self.timeouts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.VpdnMirroring.QadSendStatsLastClear']['meta_info']


        class QadRecvStatsLastClear(object):
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
                self.parent = None
                self.acks_recvd = None
                self.init_drops = None
                self.msg_drops = None
                self.msgs_recvd = None
                self.ooo_drops = None
                self.recvd_acks_failed = None
                self.stale_msgs = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn-mirroring/Cisco-IOS-XR-tunnel-vpdn-oper:qad-recv-stats-last-clear'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.acks_recvd is not None:
                    return True

                if self.init_drops is not None:
                    return True

                if self.msg_drops is not None:
                    return True

                if self.msgs_recvd is not None:
                    return True

                if self.ooo_drops is not None:
                    return True

                if self.recvd_acks_failed is not None:
                    return True

                if self.stale_msgs is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.VpdnMirroring.QadRecvStatsLastClear']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn-mirroring'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.alloc_cnt is not None:
                return True

            if self.alloc_err_cnt is not None:
                return True

            if self.qad_recv_stats is not None and self.qad_recv_stats._has_data():
                return True

            if self.qad_recv_stats_last_clear is not None and self.qad_recv_stats_last_clear._has_data():
                return True

            if self.qad_send_stats is not None and self.qad_send_stats._has_data():
                return True

            if self.qad_send_stats_last_clear is not None and self.qad_send_stats_last_clear._has_data():
                return True

            if self.sso_batch_err_cnt is not None:
                return True

            if self.sso_err_cnt is not None:
                return True

            if self.sync_not_conn_cnt is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
            return meta._meta_table['Vpdn.VpdnMirroring']['meta_info']


    class VpdnRedundancy(object):
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
        	**type**\:   :py:class:`VpdnStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnStateEnum>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.abort_time = None
            self.finish_time = None
            self.session_synced = None
            self.session_total = None
            self.start_time = None
            self.state = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn-redundancy'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.abort_time is not None:
                return True

            if self.finish_time is not None:
                return True

            if self.session_synced is not None:
                return True

            if self.session_total is not None:
                return True

            if self.start_time is not None:
                return True

            if self.state is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
            return meta._meta_table['Vpdn.VpdnRedundancy']['meta_info']


    class HistoryFailures(object):
        """
        VPDN history failure list
        
        .. attribute:: history_failure
        
        	VPDN history failure information
        	**type**\: list of    :py:class:`HistoryFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.HistoryFailures.HistoryFailure>`
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.history_failure = YList()
            self.history_failure.parent = self
            self.history_failure.name = 'history_failure'


        class HistoryFailure(object):
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
            	**type**\:   :py:class:`VpdnFailcodeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnFailcodeEnum>`
            
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
                self.parent = None
                self.destination_address = None
                self.domain_name = None
                self.error_repeat_count = None
                self.event_time = None
                self.failure_type = None
                self.home_gateway = None
                self.local_client_id = None
                self.mid = None
                self.nas = None
                self.remote_client_id = None
                self.remote_name = None
                self.source_address = None
                self.username = None
                self.username_xr = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:history-failures/Cisco-IOS-XR-tunnel-vpdn-oper:history-failure'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.destination_address is not None:
                    return True

                if self.domain_name is not None:
                    return True

                if self.error_repeat_count is not None:
                    return True

                if self.event_time is not None:
                    return True

                if self.failure_type is not None:
                    return True

                if self.home_gateway is not None:
                    return True

                if self.local_client_id is not None:
                    return True

                if self.mid is not None:
                    return True

                if self.nas is not None:
                    return True

                if self.remote_client_id is not None:
                    return True

                if self.remote_name is not None:
                    return True

                if self.source_address is not None:
                    return True

                if self.username is not None:
                    return True

                if self.username_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.HistoryFailures.HistoryFailure']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/Cisco-IOS-XR-tunnel-vpdn-oper:history-failures'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.history_failure is not None:
                for child_ref in self.history_failure:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
            return meta._meta_table['Vpdn.HistoryFailures']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-tunnel-vpdn-oper:vpdn'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.history_failures is not None and self.history_failures._has_data():
            return True

        if self.sessions is not None and self.sessions._has_data():
            return True

        if self.tunnel_destinations is not None and self.tunnel_destinations._has_data():
            return True

        if self.vpdn_mirroring is not None and self.vpdn_mirroring._has_data():
            return True

        if self.vpdn_redundancy is not None and self.vpdn_redundancy._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['Vpdn']['meta_info']


