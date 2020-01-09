""" Cisco_IOS_XR_tunnel_vpdn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package operational data.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['LsgStatus']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['SessionState']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['TosMode']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['VpdnFailcode']


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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['VpdnState']



class Vpdn(_Entity_):
    """
    VPDN operational data
    
    .. attribute:: nodes
    
    	List of nodes for which subscriber data is collected
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes>`
    
    	**config**\: False
    
    

    """

    _prefix = 'tunnel-vpdn-oper'
    _revision = '2015-11-09'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Vpdn, self).__init__()
        self._top_entity = None

        self.yang_name = "vpdn"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-vpdn-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Vpdn.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Vpdn.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Vpdn, [], name, value)


    class Nodes(_Entity_):
        """
        List of nodes for which subscriber data is
        collected
        
        .. attribute:: node
        
        	Subscriber data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node>`
        
        	**config**\: False
        
        

        """

        _prefix = 'tunnel-vpdn-oper'
        _revision = '2015-11-09'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Vpdn.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "vpdn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Vpdn.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Vpdn.Nodes, [], name, value)


        class Node(_Entity_):
            """
            Subscriber data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            	**config**\: False
            
            .. attribute:: sessions
            
            	VPDN session list
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.Sessions>`
            
            	**config**\: False
            
            .. attribute:: tunnel_destinations
            
            	VPDN tunnel Destinations
            	**type**\:  :py:class:`TunnelDestinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.TunnelDestinations>`
            
            	**config**\: False
            
            .. attribute:: vpdn_mirroring
            
            	VPDN Mirroring Statistics
            	**type**\:  :py:class:`VpdnMirroring <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.VpdnMirroring>`
            
            	**config**\: False
            
            .. attribute:: vpdn_redundancy
            
            	Show VPDN Redundancy information
            	**type**\:  :py:class:`VpdnRedundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.VpdnRedundancy>`
            
            	**config**\: False
            
            .. attribute:: history_failures
            
            	VPDN history failure list
            	**type**\:  :py:class:`HistoryFailures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.HistoryFailures>`
            
            	**config**\: False
            
            

            """

            _prefix = 'tunnel-vpdn-oper'
            _revision = '2015-11-09'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Vpdn.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("sessions", ("sessions", Vpdn.Nodes.Node.Sessions)), ("tunnel-destinations", ("tunnel_destinations", Vpdn.Nodes.Node.TunnelDestinations)), ("vpdn-mirroring", ("vpdn_mirroring", Vpdn.Nodes.Node.VpdnMirroring)), ("vpdn-redundancy", ("vpdn_redundancy", Vpdn.Nodes.Node.VpdnRedundancy)), ("history-failures", ("history_failures", Vpdn.Nodes.Node.HistoryFailures))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.sessions = Vpdn.Nodes.Node.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"

                self.tunnel_destinations = Vpdn.Nodes.Node.TunnelDestinations()
                self.tunnel_destinations.parent = self
                self._children_name_map["tunnel_destinations"] = "tunnel-destinations"

                self.vpdn_mirroring = Vpdn.Nodes.Node.VpdnMirroring()
                self.vpdn_mirroring.parent = self
                self._children_name_map["vpdn_mirroring"] = "vpdn-mirroring"

                self.vpdn_redundancy = Vpdn.Nodes.Node.VpdnRedundancy()
                self.vpdn_redundancy.parent = self
                self._children_name_map["vpdn_redundancy"] = "vpdn-redundancy"

                self.history_failures = Vpdn.Nodes.Node.HistoryFailures()
                self.history_failures.parent = self
                self._children_name_map["history_failures"] = "history-failures"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-vpdn-oper:vpdn/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Vpdn.Nodes.Node, ['node_name'], name, value)


            class Sessions(_Entity_):
                """
                VPDN session list
                
                .. attribute:: session
                
                	 VPDN session information
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Vpdn.Nodes.Node.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", Vpdn.Nodes.Node.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Nodes.Node.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                     VPDN session information
                    
                    .. attribute:: session_label  (key)
                    
                    	Session label
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    	**config**\: False
                    
                    .. attribute:: session
                    
                    	Session data
                    	**type**\:  :py:class:`Session_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.Sessions.Session.Session_>`
                    
                    	**config**\: False
                    
                    .. attribute:: l2tp
                    
                    	L2TP data
                    	**type**\:  :py:class:`L2tp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.Sessions.Session.L2tp>`
                    
                    	**config**\: False
                    
                    .. attribute:: subscriber
                    
                    	Subscriber data
                    	**type**\:  :py:class:`Subscriber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.Sessions.Session.Subscriber>`
                    
                    	**config**\: False
                    
                    .. attribute:: configuration
                    
                    	Configuration data
                    	**type**\:  :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.Sessions.Session.Configuration>`
                    
                    	**config**\: False
                    
                    .. attribute:: setup_time
                    
                    	Time to setup session in sec\:msec
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: parent_interface_name
                    
                    	Parent interface name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vpdn.Nodes.Node.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['session_label']
                        self._child_classes = OrderedDict([("session", ("session", Vpdn.Nodes.Node.Sessions.Session.Session_)), ("l2tp", ("l2tp", Vpdn.Nodes.Node.Sessions.Session.L2tp)), ("subscriber", ("subscriber", Vpdn.Nodes.Node.Sessions.Session.Subscriber)), ("configuration", ("configuration", Vpdn.Nodes.Node.Sessions.Session.Configuration))])
                        self._leafs = OrderedDict([
                            ('session_label', (YLeaf(YType.str, 'session-label'), ['str'])),
                            ('setup_time', (YLeaf(YType.uint32, 'setup-time'), ['int'])),
                            ('parent_interface_name', (YLeaf(YType.str, 'parent-interface-name'), ['str'])),
                        ])
                        self.session_label = None
                        self.setup_time = None
                        self.parent_interface_name = None

                        self.session = Vpdn.Nodes.Node.Sessions.Session.Session_()
                        self.session.parent = self
                        self._children_name_map["session"] = "session"

                        self.l2tp = Vpdn.Nodes.Node.Sessions.Session.L2tp()
                        self.l2tp.parent = self
                        self._children_name_map["l2tp"] = "l2tp"

                        self.subscriber = Vpdn.Nodes.Node.Sessions.Session.Subscriber()
                        self.subscriber.parent = self
                        self._children_name_map["subscriber"] = "subscriber"

                        self.configuration = Vpdn.Nodes.Node.Sessions.Session.Configuration()
                        self.configuration.parent = self
                        self._children_name_map["configuration"] = "configuration"
                        self._segment_path = lambda: "session" + "[session-label='" + str(self.session_label) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Nodes.Node.Sessions.Session, ['session_label', 'setup_time', 'parent_interface_name'], name, value)


                    class Session_(_Entity_):
                        """
                        Session data
                        
                        .. attribute:: last_change
                        
                        	Elapsed time since last change in hh\:mm\:ss format
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: interface_name
                        
                        	Session interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        	**config**\: False
                        
                        .. attribute:: username
                        
                        	Authentication username
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: state
                        
                        	Session state
                        	**type**\:  :py:class:`SessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.SessionState>`
                        
                        	**config**\: False
                        
                        .. attribute:: l2tp_session_id
                        
                        	L2TP session ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: l2tp_tunnel_id
                        
                        	L2TP tunnel ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: srg_slave
                        
                        	Session SRG Slave
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-vpdn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Vpdn.Nodes.Node.Sessions.Session.Session_, self).__init__()

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
                            self._perform_setattr(Vpdn.Nodes.Node.Sessions.Session.Session_, ['last_change', 'interface_name', 'username', 'domain_name', 'state', 'l2tp_session_id', 'l2tp_tunnel_id', 'srg_slave'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                            return meta._meta_table['Vpdn.Nodes.Node.Sessions.Session.Session_']['meta_info']


                    class L2tp(_Entity_):
                        """
                        L2TP data
                        
                        .. attribute:: local_endpoint
                        
                        	Local endpoint IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: remote_endpoint
                        
                        	Remote endpoint IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**config**\: False
                        
                        .. attribute:: call_serial_number
                        
                        	Call serial number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: is_l2tp_class_attribute_mask_set
                        
                        	True if L2TP class attribute mask is set
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: local_tunnel_id
                        
                        	Local tunnel ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: remote_tunnel_id
                        
                        	Remote tunnel ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: local_session_id
                        
                        	Local session ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: remote_session_id
                        
                        	Remote session ID
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: remote_port
                        
                        	Remote port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        .. attribute:: tunnel_client_authentication_id
                        
                        	Tunnel client authentication ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: tunnel_server_authentication_id
                        
                        	Tunnel server authentication ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: tunnel_assignment_id
                        
                        	Tunnel assignment ID
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: is_tunnel_authentication_enabled
                        
                        	True if tunnel authentication is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-vpdn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Vpdn.Nodes.Node.Sessions.Session.L2tp, self).__init__()

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
                            self._perform_setattr(Vpdn.Nodes.Node.Sessions.Session.L2tp, ['local_endpoint', 'remote_endpoint', 'call_serial_number', 'is_l2tp_class_attribute_mask_set', 'local_tunnel_id', 'remote_tunnel_id', 'local_session_id', 'remote_session_id', 'remote_port', 'tunnel_client_authentication_id', 'tunnel_server_authentication_id', 'tunnel_assignment_id', 'is_tunnel_authentication_enabled'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                            return meta._meta_table['Vpdn.Nodes.Node.Sessions.Session.L2tp']['meta_info']


                    class Subscriber(_Entity_):
                        """
                        Subscriber data
                        
                        .. attribute:: nas_port_id_val
                        
                        	NAS port ID Val
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: nas_port_type
                        
                        	NAS port type
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: physical_channel_id
                        
                        	Physical channel ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: receive_connect_speed
                        
                        	Receive connect speed in nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        .. attribute:: transmit_connect_speed
                        
                        	Transmit connect speed in nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'tunnel-vpdn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Vpdn.Nodes.Node.Sessions.Session.Subscriber, self).__init__()

                            self.yang_name = "subscriber"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('nas_port_id_val', (YLeaf(YType.str, 'nas-port-id-val'), ['str'])),
                                ('nas_port_type', (YLeaf(YType.str, 'nas-port-type'), ['str'])),
                                ('physical_channel_id', (YLeaf(YType.uint32, 'physical-channel-id'), ['int'])),
                                ('receive_connect_speed', (YLeaf(YType.uint64, 'receive-connect-speed'), ['int'])),
                                ('transmit_connect_speed', (YLeaf(YType.uint64, 'transmit-connect-speed'), ['int'])),
                            ])
                            self.nas_port_id_val = None
                            self.nas_port_type = None
                            self.physical_channel_id = None
                            self.receive_connect_speed = None
                            self.transmit_connect_speed = None
                            self._segment_path = lambda: "subscriber"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vpdn.Nodes.Node.Sessions.Session.Subscriber, ['nas_port_id_val', 'nas_port_type', 'physical_channel_id', 'receive_connect_speed', 'transmit_connect_speed'], name, value)

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                            return meta._meta_table['Vpdn.Nodes.Node.Sessions.Session.Subscriber']['meta_info']


                    class Configuration(_Entity_):
                        """
                        Configuration data
                        
                        .. attribute:: vpn_id
                        
                        	VPN ID
                        	**type**\:  :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.Sessions.Session.Configuration.VpnId>`
                        
                        	**config**\: False
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: l2tp_busy_timeout
                        
                        	L2TP busy timeout in seconds
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**config**\: False
                        
                        	**units**\: second
                        
                        .. attribute:: tos_mode
                        
                        	TOS mode
                        	**type**\:  :py:class:`TosMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.TosMode>`
                        
                        	**config**\: False
                        
                        .. attribute:: tos
                        
                        	TOS setting value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        	**config**\: False
                        
                        .. attribute:: dsl_line_forwarding
                        
                        	True if DSL line info forwarding is enabled
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'tunnel-vpdn-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Vpdn.Nodes.Node.Sessions.Session.Configuration, self).__init__()

                            self.yang_name = "configuration"
                            self.yang_parent_name = "session"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("vpn-id", ("vpn_id", Vpdn.Nodes.Node.Sessions.Session.Configuration.VpnId))])
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

                            self.vpn_id = Vpdn.Nodes.Node.Sessions.Session.Configuration.VpnId()
                            self.vpn_id.parent = self
                            self._children_name_map["vpn_id"] = "vpn-id"
                            self._segment_path = lambda: "configuration"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Vpdn.Nodes.Node.Sessions.Session.Configuration, ['template_name', 'vrf_name', 'l2tp_busy_timeout', 'tos_mode', 'tos', 'dsl_line_forwarding'], name, value)


                        class VpnId(_Entity_):
                            """
                            VPN ID
                            
                            .. attribute:: oui
                            
                            	OUI
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: index
                            
                            	Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'tunnel-vpdn-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Vpdn.Nodes.Node.Sessions.Session.Configuration.VpnId, self).__init__()

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
                                self._perform_setattr(Vpdn.Nodes.Node.Sessions.Session.Configuration.VpnId, ['oui', 'index'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                                return meta._meta_table['Vpdn.Nodes.Node.Sessions.Session.Configuration.VpnId']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                            return meta._meta_table['Vpdn.Nodes.Node.Sessions.Session.Configuration']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Nodes.Node.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Nodes.Node.Sessions']['meta_info']


            class TunnelDestinations(_Entity_):
                """
                VPDN tunnel Destinations
                
                .. attribute:: tunnel_destination
                
                	VPDN tunnel destination information
                	**type**\: list of  		 :py:class:`TunnelDestination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.TunnelDestinations.TunnelDestination>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Vpdn.Nodes.Node.TunnelDestinations, self).__init__()

                    self.yang_name = "tunnel-destinations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tunnel-destination", ("tunnel_destination", Vpdn.Nodes.Node.TunnelDestinations.TunnelDestination))])
                    self._leafs = OrderedDict()

                    self.tunnel_destination = YList(self)
                    self._segment_path = lambda: "tunnel-destinations"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Nodes.Node.TunnelDestinations, [], name, value)


                class TunnelDestination(_Entity_):
                    """
                    VPDN tunnel destination information
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: address
                    
                    	IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name_xr
                    
                    	VRF name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: load
                    
                    	Current load on LNS
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: status
                    
                    	Status of LNS
                    	**type**\:  :py:class:`LsgStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.LsgStatus>`
                    
                    	**config**\: False
                    
                    .. attribute:: connects
                    
                    	Total count of tunnels connected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: disconnects
                    
                    	Total count of tunnels disconnected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: retry
                    
                    	Retries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: status_change_time
                    
                    	Seconds since last status change
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vpdn.Nodes.Node.TunnelDestinations.TunnelDestination, self).__init__()

                        self.yang_name = "tunnel-destination"
                        self.yang_parent_name = "tunnel-destinations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Nodes.Node.TunnelDestinations.TunnelDestination, ['vrf_name', 'address', 'vrf_name_xr', 'load', 'status', 'connects', 'disconnects', 'retry', 'status_change_time'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Nodes.Node.TunnelDestinations.TunnelDestination']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Nodes.Node.TunnelDestinations']['meta_info']


            class VpdnMirroring(_Entity_):
                """
                VPDN Mirroring Statistics
                
                .. attribute:: qad_send_stats
                
                	qad send stats
                	**type**\:  :py:class:`QadSendStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.VpdnMirroring.QadSendStats>`
                
                	**config**\: False
                
                .. attribute:: qad_recv_stats
                
                	qad recv stats
                	**type**\:  :py:class:`QadRecvStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.VpdnMirroring.QadRecvStats>`
                
                	**config**\: False
                
                .. attribute:: qad_send_stats_last_clear
                
                	qad send stats last clear
                	**type**\:  :py:class:`QadSendStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.VpdnMirroring.QadSendStatsLastClear>`
                
                	**config**\: False
                
                .. attribute:: qad_recv_stats_last_clear
                
                	qad recv stats last clear
                	**type**\:  :py:class:`QadRecvStatsLastClear <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.VpdnMirroring.QadRecvStatsLastClear>`
                
                	**config**\: False
                
                .. attribute:: sync_not_conn_cnt
                
                	sync not conn cnt
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sso_err_cnt
                
                	sso err cnt
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: sso_batch_err_cnt
                
                	sso batch err cnt
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: alloc_err_cnt
                
                	alloc err cnt
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: alloc_cnt
                
                	alloc cnt
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Vpdn.Nodes.Node.VpdnMirroring, self).__init__()

                    self.yang_name = "vpdn-mirroring"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("qad-send-stats", ("qad_send_stats", Vpdn.Nodes.Node.VpdnMirroring.QadSendStats)), ("qad-recv-stats", ("qad_recv_stats", Vpdn.Nodes.Node.VpdnMirroring.QadRecvStats)), ("qad-send-stats-last-clear", ("qad_send_stats_last_clear", Vpdn.Nodes.Node.VpdnMirroring.QadSendStatsLastClear)), ("qad-recv-stats-last-clear", ("qad_recv_stats_last_clear", Vpdn.Nodes.Node.VpdnMirroring.QadRecvStatsLastClear))])
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

                    self.qad_send_stats = Vpdn.Nodes.Node.VpdnMirroring.QadSendStats()
                    self.qad_send_stats.parent = self
                    self._children_name_map["qad_send_stats"] = "qad-send-stats"

                    self.qad_recv_stats = Vpdn.Nodes.Node.VpdnMirroring.QadRecvStats()
                    self.qad_recv_stats.parent = self
                    self._children_name_map["qad_recv_stats"] = "qad-recv-stats"

                    self.qad_send_stats_last_clear = Vpdn.Nodes.Node.VpdnMirroring.QadSendStatsLastClear()
                    self.qad_send_stats_last_clear.parent = self
                    self._children_name_map["qad_send_stats_last_clear"] = "qad-send-stats-last-clear"

                    self.qad_recv_stats_last_clear = Vpdn.Nodes.Node.VpdnMirroring.QadRecvStatsLastClear()
                    self.qad_recv_stats_last_clear.parent = self
                    self._children_name_map["qad_recv_stats_last_clear"] = "qad-recv-stats-last-clear"
                    self._segment_path = lambda: "vpdn-mirroring"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Nodes.Node.VpdnMirroring, ['sync_not_conn_cnt', 'sso_err_cnt', 'sso_batch_err_cnt', 'alloc_err_cnt', 'alloc_cnt'], name, value)


                class QadSendStats(_Entity_):
                    """
                    qad send stats
                    
                    .. attribute:: msgs_sent
                    
                    	msgs sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: acks_sent
                    
                    	acks sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_partner
                    
                    	no partner
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sends_failed
                    
                    	sends failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: acks_failed
                    
                    	acks failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pending_acks
                    
                    	pending acks
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: timeouts
                    
                    	timeouts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: suspends
                    
                    	suspends
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resumes
                    
                    	resumes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sends_fragment
                    
                    	sends fragment
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_last_seq_number
                    
                    	qad last seq number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_frag_count
                    
                    	qad frag count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_ack_count
                    
                    	qad ack count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_unknown_acks
                    
                    	qad unknown acks
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_timeouts
                    
                    	qad timeouts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_count
                    
                    	qad rx count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_list_count
                    
                    	qad rx list count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_list_q_size
                    
                    	qad rx list q size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_first_seq_number
                    
                    	qad rx first seq number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vpdn.Nodes.Node.VpdnMirroring.QadSendStats, self).__init__()

                        self.yang_name = "qad-send-stats"
                        self.yang_parent_name = "vpdn-mirroring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Nodes.Node.VpdnMirroring.QadSendStats, ['msgs_sent', 'acks_sent', 'no_partner', 'sends_failed', 'acks_failed', 'pending_acks', 'timeouts', 'suspends', 'resumes', 'sends_fragment', 'qad_last_seq_number', 'qad_frag_count', 'qad_ack_count', 'qad_unknown_acks', 'qad_timeouts', 'qad_rx_count', 'qad_rx_list_count', 'qad_rx_list_q_size', 'qad_rx_first_seq_number'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Nodes.Node.VpdnMirroring.QadSendStats']['meta_info']


                class QadRecvStats(_Entity_):
                    """
                    qad recv stats
                    
                    .. attribute:: msgs_recvd
                    
                    	msgs recvd
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: acks_recvd
                    
                    	acks recvd
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: recvd_acks_failed
                    
                    	recvd acks failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: init_drops
                    
                    	init drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: msg_drops
                    
                    	msg drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ooo_drops
                    
                    	ooo drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_msgs
                    
                    	stale msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vpdn.Nodes.Node.VpdnMirroring.QadRecvStats, self).__init__()

                        self.yang_name = "qad-recv-stats"
                        self.yang_parent_name = "vpdn-mirroring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Nodes.Node.VpdnMirroring.QadRecvStats, ['msgs_recvd', 'acks_recvd', 'recvd_acks_failed', 'init_drops', 'msg_drops', 'ooo_drops', 'stale_msgs'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Nodes.Node.VpdnMirroring.QadRecvStats']['meta_info']


                class QadSendStatsLastClear(_Entity_):
                    """
                    qad send stats last clear
                    
                    .. attribute:: msgs_sent
                    
                    	msgs sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: acks_sent
                    
                    	acks sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: no_partner
                    
                    	no partner
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sends_failed
                    
                    	sends failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: acks_failed
                    
                    	acks failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: pending_acks
                    
                    	pending acks
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: timeouts
                    
                    	timeouts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: suspends
                    
                    	suspends
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: resumes
                    
                    	resumes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: sends_fragment
                    
                    	sends fragment
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_last_seq_number
                    
                    	qad last seq number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_frag_count
                    
                    	qad frag count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_ack_count
                    
                    	qad ack count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_unknown_acks
                    
                    	qad unknown acks
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_timeouts
                    
                    	qad timeouts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_count
                    
                    	qad rx count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_list_count
                    
                    	qad rx list count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_list_q_size
                    
                    	qad rx list q size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: qad_rx_first_seq_number
                    
                    	qad rx first seq number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vpdn.Nodes.Node.VpdnMirroring.QadSendStatsLastClear, self).__init__()

                        self.yang_name = "qad-send-stats-last-clear"
                        self.yang_parent_name = "vpdn-mirroring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Nodes.Node.VpdnMirroring.QadSendStatsLastClear, ['msgs_sent', 'acks_sent', 'no_partner', 'sends_failed', 'acks_failed', 'pending_acks', 'timeouts', 'suspends', 'resumes', 'sends_fragment', 'qad_last_seq_number', 'qad_frag_count', 'qad_ack_count', 'qad_unknown_acks', 'qad_timeouts', 'qad_rx_count', 'qad_rx_list_count', 'qad_rx_list_q_size', 'qad_rx_first_seq_number'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Nodes.Node.VpdnMirroring.QadSendStatsLastClear']['meta_info']


                class QadRecvStatsLastClear(_Entity_):
                    """
                    qad recv stats last clear
                    
                    .. attribute:: msgs_recvd
                    
                    	msgs recvd
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: acks_recvd
                    
                    	acks recvd
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: recvd_acks_failed
                    
                    	recvd acks failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: init_drops
                    
                    	init drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: msg_drops
                    
                    	msg drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: ooo_drops
                    
                    	ooo drops
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: stale_msgs
                    
                    	stale msgs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vpdn.Nodes.Node.VpdnMirroring.QadRecvStatsLastClear, self).__init__()

                        self.yang_name = "qad-recv-stats-last-clear"
                        self.yang_parent_name = "vpdn-mirroring"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Nodes.Node.VpdnMirroring.QadRecvStatsLastClear, ['msgs_recvd', 'acks_recvd', 'recvd_acks_failed', 'init_drops', 'msg_drops', 'ooo_drops', 'stale_msgs'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Nodes.Node.VpdnMirroring.QadRecvStatsLastClear']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Nodes.Node.VpdnMirroring']['meta_info']


            class VpdnRedundancy(_Entity_):
                """
                Show VPDN Redundancy information
                
                .. attribute:: session_total
                
                	session total
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: session_synced
                
                	session synced
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**config**\: False
                
                .. attribute:: state
                
                	state
                	**type**\:  :py:class:`VpdnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnState>`
                
                	**config**\: False
                
                .. attribute:: start_time
                
                	start time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: finish_time
                
                	finish time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                .. attribute:: abort_time
                
                	abort time
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Vpdn.Nodes.Node.VpdnRedundancy, self).__init__()

                    self.yang_name = "vpdn-redundancy"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
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
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Nodes.Node.VpdnRedundancy, ['session_total', 'session_synced', 'state', 'start_time', 'finish_time', 'abort_time'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Nodes.Node.VpdnRedundancy']['meta_info']


            class HistoryFailures(_Entity_):
                """
                VPDN history failure list
                
                .. attribute:: history_failure
                
                	VPDN history failure information
                	**type**\: list of  		 :py:class:`HistoryFailure <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.Vpdn.Nodes.Node.HistoryFailures.HistoryFailure>`
                
                	**config**\: False
                
                

                """

                _prefix = 'tunnel-vpdn-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Vpdn.Nodes.Node.HistoryFailures, self).__init__()

                    self.yang_name = "history-failures"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("history-failure", ("history_failure", Vpdn.Nodes.Node.HistoryFailures.HistoryFailure))])
                    self._leafs = OrderedDict()

                    self.history_failure = YList(self)
                    self._segment_path = lambda: "history-failures"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Vpdn.Nodes.Node.HistoryFailures, [], name, value)


                class HistoryFailure(_Entity_):
                    """
                    VPDN history failure information
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: remote_name
                    
                    	Remote name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    	**config**\: False
                    
                    .. attribute:: username_xr
                    
                    	Authentication username
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: domain_name
                    
                    	Domain name
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: mid
                    
                    	VPDN user session ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: nas
                    
                    	Network access server
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: destination_address
                    
                    	NAS IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: remote_client_id
                    
                    	Remote client ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: home_gateway
                    
                    	Home gateway
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: source_address
                    
                    	Source IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**config**\: False
                    
                    .. attribute:: local_client_id
                    
                    	Local client ID
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: event_time
                    
                    	Event logged time in Ex\: Wed Aug  3 10\:28\:30 2011
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: error_repeat_count
                    
                    	Error repeat count
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**config**\: False
                    
                    .. attribute:: failure_type
                    
                    	Failure type
                    	**type**\:  :py:class:`VpdnFailcode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_oper.VpdnFailcode>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Vpdn.Nodes.Node.HistoryFailures.HistoryFailure, self).__init__()

                        self.yang_name = "history-failure"
                        self.yang_parent_name = "history-failures"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
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
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Vpdn.Nodes.Node.HistoryFailures.HistoryFailure, ['username', 'remote_name', 'username_xr', 'domain_name', 'mid', 'nas', 'destination_address', 'remote_client_id', 'home_gateway', 'source_address', 'local_client_id', 'event_time', 'error_repeat_count', 'failure_type'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                        return meta._meta_table['Vpdn.Nodes.Node.HistoryFailures.HistoryFailure']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                    return meta._meta_table['Vpdn.Nodes.Node.HistoryFailures']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
                return meta._meta_table['Vpdn.Nodes.Node']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
            return meta._meta_table['Vpdn.Nodes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Vpdn()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_tunnel_vpdn_oper as meta
        return meta._meta_table['Vpdn']['meta_info']


