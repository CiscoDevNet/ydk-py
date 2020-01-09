""" Cisco_IOS_XR_man_xml_ttyagent_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-xml\-ttyagent package operational data.

This module contains definitions
for the following management objects\:
  netconf\: NETCONF operational information
  xr\-xml\: xr xml

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



class XrXmlSessionAlarmRegister(Enum):
    """
    XrXmlSessionAlarmRegister (Enum Class)

    AlarmNotify

    .. data:: registered = 1

    	Registered

    .. data:: not_registered = 2

    	NotRegistered

    """

    registered = Enum.YLeaf(1, "registered")

    not_registered = Enum.YLeaf(2, "not-registered")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['XrXmlSessionAlarmRegister']


class XrXmlSessionState(Enum):
    """
    XrXmlSessionState (Enum Class)

    SessionState

    .. data:: idle = 1

    	Idle

    .. data:: busy = 2

    	Busy

    """

    idle = Enum.YLeaf(1, "idle")

    busy = Enum.YLeaf(2, "busy")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['XrXmlSessionState']



class Netconf(_Entity_):
    """
    NETCONF operational information
    
    .. attribute:: agent
    
    	NETCONF agent operational information
    	**type**\:  :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent>`
    
    	**config**\: False
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Netconf, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("agent", ("agent", Netconf.Agent))])
        self._leafs = OrderedDict()

        self.agent = Netconf.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._segment_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Netconf, [], name, value)


    class Agent(_Entity_):
        """
        NETCONF agent operational information
        
        .. attribute:: tty
        
        	NETCONF agent over TTY
        	**type**\:  :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty>`
        
        	**config**\: False
        
        

        """

        _prefix = 'man-xml-ttyagent-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Netconf.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "netconf"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tty", ("tty", Netconf.Agent.Tty))])
            self._leafs = OrderedDict()

            self.tty = Netconf.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Netconf.Agent, [], name, value)


        class Tty(_Entity_):
            """
            NETCONF agent over TTY
            
            .. attribute:: sessions
            
            	Session information
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Netconf.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sessions", ("sessions", Netconf.Agent.Tty.Sessions))])
                self._leafs = OrderedDict()

                self.sessions = Netconf.Agent.Tty.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._segment_path = lambda: "tty"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Netconf.Agent.Tty, [], name, value)


            class Sessions(_Entity_):
                """
                Session information
                
                .. attribute:: session
                
                	Session information
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Netconf.Agent.Tty.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", Netconf.Agent.Tty.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/tty/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Netconf.Agent.Tty.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    Session information
                    
                    .. attribute:: session_id  (key)
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:  :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    	**config**\: False
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:  :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Netconf.Agent.Tty.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['session_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('username', (YLeaf(YType.str, 'username'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionState', '')])),
                            ('client_address', (YLeaf(YType.str, 'client-address'), ['str'])),
                            ('client_port', (YLeaf(YType.uint32, 'client-port'), ['int'])),
                            ('config_session_id', (YLeaf(YType.str, 'config-session-id'), ['str'])),
                            ('admin_config_session_id', (YLeaf(YType.str, 'admin-config-session-id'), ['str'])),
                            ('alarm_notification', (YLeaf(YType.enumeration, 'alarm-notification'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegister', '')])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                            ('elapsed_time', (YLeaf(YType.uint32, 'elapsed-time'), ['int'])),
                            ('last_state_change', (YLeaf(YType.uint32, 'last-state-change'), ['int'])),
                        ])
                        self.session_id = None
                        self.username = None
                        self.state = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.vrf_name = None
                        self.start_time = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self._segment_path = lambda: "session" + "[session-id='" + str(self.session_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/tty/sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Netconf.Agent.Tty.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['Netconf.Agent.Tty.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['Netconf.Agent.Tty.Sessions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['Netconf.Agent.Tty']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
            return meta._meta_table['Netconf.Agent']['meta_info']

    def clone_ptr(self):
        self._top_entity = Netconf()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['Netconf']['meta_info']


class XrXml(_Entity_):
    """
    xr xml
    
    .. attribute:: agent
    
    	XML agents
    	**type**\:  :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent>`
    
    	**config**\: False
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2017-09-07'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(XrXml, self).__init__()
        self._top_entity = None

        self.yang_name = "xr-xml"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("agent", ("agent", XrXml.Agent))])
        self._leafs = OrderedDict()

        self.agent = XrXml.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._segment_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(XrXml, [], name, value)


    class Agent(_Entity_):
        """
        XML agents
        
        .. attribute:: tty
        
        	TTY sessions information
        	**type**\:  :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty>`
        
        	**config**\: False
        
        .. attribute:: default
        
        	Default sessions information
        	**type**\:  :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default>`
        
        	**config**\: False
        
        .. attribute:: ssl
        
        	SSL sessions information
        	**type**\:  :py:class:`Ssl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl>`
        
        	**config**\: False
        
        

        """

        _prefix = 'man-xml-ttyagent-oper'
        _revision = '2017-09-07'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(XrXml.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "xr-xml"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tty", ("tty", XrXml.Agent.Tty)), ("default", ("default", XrXml.Agent.Default)), ("ssl", ("ssl", XrXml.Agent.Ssl))])
            self._leafs = OrderedDict()

            self.tty = XrXml.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"

            self.default = XrXml.Agent.Default()
            self.default.parent = self
            self._children_name_map["default"] = "default"

            self.ssl = XrXml.Agent.Ssl()
            self.ssl.parent = self
            self._children_name_map["ssl"] = "ssl"
            self._segment_path = lambda: "agent"
            self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(XrXml.Agent, [], name, value)


        class Tty(_Entity_):
            """
            TTY sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(XrXml.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sessions", ("sessions", XrXml.Agent.Tty.Sessions))])
                self._leafs = OrderedDict()

                self.sessions = XrXml.Agent.Tty.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._segment_path = lambda: "tty"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(XrXml.Agent.Tty, [], name, value)


            class Sessions(_Entity_):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(XrXml.Agent.Tty.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "tty"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", XrXml.Agent.Tty.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/tty/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Tty.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  (key)
                    
                    	Session Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:  :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    	**config**\: False
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:  :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(XrXml.Agent.Tty.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['session_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('username', (YLeaf(YType.str, 'username'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionState', '')])),
                            ('client_address', (YLeaf(YType.str, 'client-address'), ['str'])),
                            ('client_port', (YLeaf(YType.uint32, 'client-port'), ['int'])),
                            ('config_session_id', (YLeaf(YType.str, 'config-session-id'), ['str'])),
                            ('admin_config_session_id', (YLeaf(YType.str, 'admin-config-session-id'), ['str'])),
                            ('alarm_notification', (YLeaf(YType.enumeration, 'alarm-notification'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegister', '')])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                            ('elapsed_time', (YLeaf(YType.uint32, 'elapsed-time'), ['int'])),
                            ('last_state_change', (YLeaf(YType.uint32, 'last-state-change'), ['int'])),
                        ])
                        self.session_id = None
                        self.username = None
                        self.state = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.vrf_name = None
                        self.start_time = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self._segment_path = lambda: "session" + "[session-id='" + str(self.session_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/tty/sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Tty.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['XrXml.Agent.Tty.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['XrXml.Agent.Tty.Sessions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['XrXml.Agent.Tty']['meta_info']


        class Default(_Entity_):
            """
            Default sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(XrXml.Agent.Default, self).__init__()

                self.yang_name = "default"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sessions", ("sessions", XrXml.Agent.Default.Sessions))])
                self._leafs = OrderedDict()

                self.sessions = XrXml.Agent.Default.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._segment_path = lambda: "default"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(XrXml.Agent.Default, [], name, value)


            class Sessions(_Entity_):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(XrXml.Agent.Default.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "default"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", XrXml.Agent.Default.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/default/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Default.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  (key)
                    
                    	Session Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:  :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    	**config**\: False
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:  :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(XrXml.Agent.Default.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['session_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('username', (YLeaf(YType.str, 'username'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionState', '')])),
                            ('client_address', (YLeaf(YType.str, 'client-address'), ['str'])),
                            ('client_port', (YLeaf(YType.uint32, 'client-port'), ['int'])),
                            ('config_session_id', (YLeaf(YType.str, 'config-session-id'), ['str'])),
                            ('admin_config_session_id', (YLeaf(YType.str, 'admin-config-session-id'), ['str'])),
                            ('alarm_notification', (YLeaf(YType.enumeration, 'alarm-notification'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegister', '')])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                            ('elapsed_time', (YLeaf(YType.uint32, 'elapsed-time'), ['int'])),
                            ('last_state_change', (YLeaf(YType.uint32, 'last-state-change'), ['int'])),
                        ])
                        self.session_id = None
                        self.username = None
                        self.state = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.vrf_name = None
                        self.start_time = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self._segment_path = lambda: "session" + "[session-id='" + str(self.session_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/default/sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Default.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['XrXml.Agent.Default.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['XrXml.Agent.Default.Sessions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['XrXml.Agent.Default']['meta_info']


        class Ssl(_Entity_):
            """
            SSL sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions>`
            
            	**config**\: False
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2017-09-07'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(XrXml.Agent.Ssl, self).__init__()

                self.yang_name = "ssl"
                self.yang_parent_name = "agent"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("sessions", ("sessions", XrXml.Agent.Ssl.Sessions))])
                self._leafs = OrderedDict()

                self.sessions = XrXml.Agent.Ssl.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._segment_path = lambda: "ssl"
                self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(XrXml.Agent.Ssl, [], name, value)


            class Sessions(_Entity_):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions.Session>`
                
                	**config**\: False
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(XrXml.Agent.Ssl.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "ssl"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("session", ("session", XrXml.Agent.Ssl.Sessions.Session))])
                    self._leafs = OrderedDict()

                    self.session = YList(self)
                    self._segment_path = lambda: "sessions"
                    self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/ssl/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(XrXml.Agent.Ssl.Sessions, [], name, value)


                class Session(_Entity_):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  (key)
                    
                    	Session Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:  :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
                    	**config**\: False
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:  :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
                    	**config**\: False
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\: str
                    
                    	**config**\: False
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**config**\: False
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(XrXml.Agent.Ssl.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['session_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('username', (YLeaf(YType.str, 'username'), ['str'])),
                            ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionState', '')])),
                            ('client_address', (YLeaf(YType.str, 'client-address'), ['str'])),
                            ('client_port', (YLeaf(YType.uint32, 'client-port'), ['int'])),
                            ('config_session_id', (YLeaf(YType.str, 'config-session-id'), ['str'])),
                            ('admin_config_session_id', (YLeaf(YType.str, 'admin-config-session-id'), ['str'])),
                            ('alarm_notification', (YLeaf(YType.enumeration, 'alarm-notification'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegister', '')])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('start_time', (YLeaf(YType.uint32, 'start-time'), ['int'])),
                            ('elapsed_time', (YLeaf(YType.uint32, 'elapsed-time'), ['int'])),
                            ('last_state_change', (YLeaf(YType.uint32, 'last-state-change'), ['int'])),
                        ])
                        self.session_id = None
                        self.username = None
                        self.state = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.vrf_name = None
                        self.start_time = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self._segment_path = lambda: "session" + "[session-id='" + str(self.session_id) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/ssl/sessions/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(XrXml.Agent.Ssl.Sessions.Session, ['session_id', 'username', 'state', 'client_address', 'client_port', 'config_session_id', 'admin_config_session_id', 'alarm_notification', 'vrf_name', 'start_time', 'elapsed_time', 'last_state_change'], name, value)

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['XrXml.Agent.Ssl.Sessions.Session']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['XrXml.Agent.Ssl.Sessions']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['XrXml.Agent.Ssl']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
            return meta._meta_table['XrXml.Agent']['meta_info']

    def clone_ptr(self):
        self._top_entity = XrXml()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['XrXml']['meta_info']


