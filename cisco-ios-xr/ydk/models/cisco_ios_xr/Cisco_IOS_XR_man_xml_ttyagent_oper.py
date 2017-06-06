""" Cisco_IOS_XR_man_xml_ttyagent_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-xml\-ttyagent package operational data.

This module contains definitions
for the following management objects\:
  netconf\: NETCONF operational information
  xr\-xml\: xr xml

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class XrXmlSessionAlarmRegisterEnum(Enum):
    """
    XrXmlSessionAlarmRegisterEnum

    AlarmNotify

    .. data:: registered = 1

    	Registered

    .. data:: not_registered = 2

    	NotRegistered

    """

    registered = 1

    not_registered = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['XrXmlSessionAlarmRegisterEnum']


class XrXmlSessionStateEnum(Enum):
    """
    XrXmlSessionStateEnum

    SessionState

    .. data:: idle = 1

    	Idle

    .. data:: busy = 2

    	Busy

    """

    idle = 1

    busy = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['XrXmlSessionStateEnum']



class Netconf(object):
    """
    NETCONF operational information
    
    .. attribute:: agent
    
    	NETCONF agent operational information
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2015-07-30'

    def __init__(self):
        self.agent = Netconf.Agent()
        self.agent.parent = self


    class Agent(object):
        """
        NETCONF agent operational information
        
        .. attribute:: tty
        
        	NETCONF agent over TTY
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.tty = Netconf.Agent.Tty()
            self.tty.parent = self


        class Tty(object):
            """
            NETCONF agent over TTY
            
            .. attribute:: sessions
            
            	Session information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.sessions = Netconf.Agent.Tty.Sessions()
                self.sessions.parent = self


            class Sessions(object):
                """
                Session information
                
                .. attribute:: session
                
                	Session information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.session = YList()
                    self.session.parent = self
                    self.session.name = 'session'


                class Session(object):
                    """
                    Session information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegisterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegisterEnum>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionStateEnum>`
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self.start_time = None
                        self.state = None
                        self.username = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.session_id is None:
                            raise YPYModelError('Key property session_id is None')

                        return '/Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:tty/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions/Cisco-IOS-XR-man-xml-ttyagent-oper:session[Cisco-IOS-XR-man-xml-ttyagent-oper:session-id = ' + str(self.session_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_id is not None:
                            return True

                        if self.admin_config_session_id is not None:
                            return True

                        if self.alarm_notification is not None:
                            return True

                        if self.client_address is not None:
                            return True

                        if self.client_port is not None:
                            return True

                        if self.config_session_id is not None:
                            return True

                        if self.elapsed_time is not None:
                            return True

                        if self.last_state_change is not None:
                            return True

                        if self.start_time is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.username is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['Netconf.Agent.Tty.Sessions.Session']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:tty/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['Netconf.Agent.Tty.Sessions']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:tty'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sessions is not None and self.sessions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['Netconf.Agent.Tty']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/Cisco-IOS-XR-man-xml-ttyagent-oper:agent'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.tty is not None and self.tty._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
            return meta._meta_table['Netconf.Agent']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-xml-ttyagent-oper:netconf'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.agent is not None and self.agent._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['Netconf']['meta_info']


class XrXml(object):
    """
    xr xml
    
    .. attribute:: agent
    
    	XML agents
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2015-07-30'

    def __init__(self):
        self.agent = XrXml.Agent()
        self.agent.parent = self


    class Agent(object):
        """
        XML agents
        
        .. attribute:: default
        
        	Default sessions information
        	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default>`
        
        .. attribute:: ssl
        
        	SSL sessions information
        	**type**\:   :py:class:`Ssl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl>`
        
        .. attribute:: tty
        
        	TTY sessions information
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-oper'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.default = XrXml.Agent.Default()
            self.default.parent = self
            self.ssl = XrXml.Agent.Ssl()
            self.ssl.parent = self
            self.tty = XrXml.Agent.Tty()
            self.tty.parent = self


        class Tty(object):
            """
            TTY sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.sessions = XrXml.Agent.Tty.Sessions()
                self.sessions.parent = self


            class Sessions(object):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.session = YList()
                    self.session.parent = self
                    self.session.name = 'session'


                class Session(object):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegisterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegisterEnum>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionStateEnum>`
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self.start_time = None
                        self.state = None
                        self.username = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.session_id is None:
                            raise YPYModelError('Key property session_id is None')

                        return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:tty/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions/Cisco-IOS-XR-man-xml-ttyagent-oper:session[Cisco-IOS-XR-man-xml-ttyagent-oper:session-id = ' + str(self.session_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_id is not None:
                            return True

                        if self.admin_config_session_id is not None:
                            return True

                        if self.alarm_notification is not None:
                            return True

                        if self.client_address is not None:
                            return True

                        if self.client_port is not None:
                            return True

                        if self.config_session_id is not None:
                            return True

                        if self.elapsed_time is not None:
                            return True

                        if self.last_state_change is not None:
                            return True

                        if self.start_time is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.username is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['XrXml.Agent.Tty.Sessions.Session']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:tty/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['XrXml.Agent.Tty.Sessions']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:tty'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sessions is not None and self.sessions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['XrXml.Agent.Tty']['meta_info']


        class Default(object):
            """
            Default sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.sessions = XrXml.Agent.Default.Sessions()
                self.sessions.parent = self


            class Sessions(object):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.session = YList()
                    self.session.parent = self
                    self.session.name = 'session'


                class Session(object):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegisterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegisterEnum>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionStateEnum>`
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self.start_time = None
                        self.state = None
                        self.username = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.session_id is None:
                            raise YPYModelError('Key property session_id is None')

                        return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:default/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions/Cisco-IOS-XR-man-xml-ttyagent-oper:session[Cisco-IOS-XR-man-xml-ttyagent-oper:session-id = ' + str(self.session_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_id is not None:
                            return True

                        if self.admin_config_session_id is not None:
                            return True

                        if self.alarm_notification is not None:
                            return True

                        if self.client_address is not None:
                            return True

                        if self.client_port is not None:
                            return True

                        if self.config_session_id is not None:
                            return True

                        if self.elapsed_time is not None:
                            return True

                        if self.last_state_change is not None:
                            return True

                        if self.start_time is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.username is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['XrXml.Agent.Default.Sessions.Session']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:default/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['XrXml.Agent.Default.Sessions']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:default'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sessions is not None and self.sessions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['XrXml.Agent.Default']['meta_info']


        class Ssl(object):
            """
            SSL sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.sessions = XrXml.Agent.Ssl.Sessions()
                self.sessions.parent = self


            class Sessions(object):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    self.parent = None
                    self.session = YList()
                    self.session.parent = self
                    self.session.name = 'session'


                class Session(object):
                    """
                    xml sessions information
                    
                    .. attribute:: session_id  <key>
                    
                    	Session Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: admin_config_session_id
                    
                    	Admin config session ID
                    	**type**\:  str
                    
                    .. attribute:: alarm_notification
                    
                    	is the session registered for alarm notifications
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegisterEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegisterEnum>`
                    
                    .. attribute:: client_address
                    
                    	ip address of the client
                    	**type**\:  str
                    
                    .. attribute:: client_port
                    
                    	client's port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: config_session_id
                    
                    	Config session ID
                    	**type**\:  str
                    
                    .. attribute:: elapsed_time
                    
                    	 Elapsed time(seconds) since a session is created
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: last_state_change
                    
                    	Time(seconds) since last session state change happened 
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: start_time
                    
                    	session start time in seconds since the Unix Epoch
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: state
                    
                    	state of the session idle/busy
                    	**type**\:   :py:class:`XrXmlSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionStateEnum>`
                    
                    .. attribute:: username
                    
                    	Username
                    	**type**\:  str
                    
                    .. attribute:: vrf_name
                    
                    	VRF name 
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-oper'
                    _revision = '2015-07-30'

                    def __init__(self):
                        self.parent = None
                        self.session_id = None
                        self.admin_config_session_id = None
                        self.alarm_notification = None
                        self.client_address = None
                        self.client_port = None
                        self.config_session_id = None
                        self.elapsed_time = None
                        self.last_state_change = None
                        self.start_time = None
                        self.state = None
                        self.username = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.session_id is None:
                            raise YPYModelError('Key property session_id is None')

                        return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:ssl/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions/Cisco-IOS-XR-man-xml-ttyagent-oper:session[Cisco-IOS-XR-man-xml-ttyagent-oper:session-id = ' + str(self.session_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.session_id is not None:
                            return True

                        if self.admin_config_session_id is not None:
                            return True

                        if self.alarm_notification is not None:
                            return True

                        if self.client_address is not None:
                            return True

                        if self.client_port is not None:
                            return True

                        if self.config_session_id is not None:
                            return True

                        if self.elapsed_time is not None:
                            return True

                        if self.last_state_change is not None:
                            return True

                        if self.start_time is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.username is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                        return meta._meta_table['XrXml.Agent.Ssl.Sessions.Session']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:ssl/Cisco-IOS-XR-man-xml-ttyagent-oper:sessions'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                    return meta._meta_table['XrXml.Agent.Ssl.Sessions']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent/Cisco-IOS-XR-man-xml-ttyagent-oper:ssl'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.sessions is not None and self.sessions._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
                return meta._meta_table['XrXml.Agent.Ssl']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/Cisco-IOS-XR-man-xml-ttyagent-oper:agent'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.default is not None and self.default._has_data():
                return True

            if self.ssl is not None and self.ssl._has_data():
                return True

            if self.tty is not None and self.tty._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
            return meta._meta_table['XrXml.Agent']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.agent is not None and self.agent._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_man_xml_ttyagent_oper as meta
        return meta._meta_table['XrXml']['meta_info']


