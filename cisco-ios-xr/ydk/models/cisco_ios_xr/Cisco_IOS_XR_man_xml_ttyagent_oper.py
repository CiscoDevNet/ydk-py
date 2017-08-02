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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class XrXmlSessionAlarmRegister(Enum):
    """
    XrXmlSessionAlarmRegister

    AlarmNotify

    .. data:: registered = 1

    	Registered

    .. data:: not_registered = 2

    	NotRegistered

    """

    registered = Enum.YLeaf(1, "registered")

    not_registered = Enum.YLeaf(2, "not-registered")


class XrXmlSessionState(Enum):
    """
    XrXmlSessionState

    SessionState

    .. data:: idle = 1

    	Idle

    .. data:: busy = 2

    	Busy

    """

    idle = Enum.YLeaf(1, "idle")

    busy = Enum.YLeaf(2, "busy")



class Netconf(Entity):
    """
    NETCONF operational information
    
    .. attribute:: agent
    
    	NETCONF agent operational information
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(Netconf, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-oper"

        self.agent = Netconf.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")


    class Agent(Entity):
        """
        NETCONF agent operational information
        
        .. attribute:: tty
        
        	NETCONF agent over TTY
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-oper'
        _revision = '2015-07-30'

        def __init__(self):
            super(Netconf.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "netconf"

            self.tty = Netconf.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"
            self._children_yang_names.add("tty")


        class Tty(Entity):
            """
            NETCONF agent over TTY
            
            .. attribute:: sessions
            
            	Session information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(Netconf.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"

                self.sessions = Netconf.Agent.Tty.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")


            class Sessions(Entity):
                """
                Session information
                
                .. attribute:: session
                
                	Session information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.Netconf.Agent.Tty.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Netconf.Agent.Tty.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "tty"

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
                                super(Netconf.Agent.Tty.Sessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Netconf.Agent.Tty.Sessions, self).__setattr__(name, value)


                class Session(Entity):
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
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
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
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
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
                        super(Netconf.Agent.Tty.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.username = YLeaf(YType.str, "username")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_id",
                                        "admin_config_session_id",
                                        "alarm_notification",
                                        "client_address",
                                        "client_port",
                                        "config_session_id",
                                        "elapsed_time",
                                        "last_state_change",
                                        "start_time",
                                        "state",
                                        "username",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Netconf.Agent.Tty.Sessions.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Netconf.Agent.Tty.Sessions.Session, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.session_id.is_set or
                            self.admin_config_session_id.is_set or
                            self.alarm_notification.is_set or
                            self.client_address.is_set or
                            self.client_port.is_set or
                            self.config_session_id.is_set or
                            self.elapsed_time.is_set or
                            self.last_state_change.is_set or
                            self.start_time.is_set or
                            self.state.is_set or
                            self.username.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.admin_config_session_id.yfilter != YFilter.not_set or
                            self.alarm_notification.yfilter != YFilter.not_set or
                            self.client_address.yfilter != YFilter.not_set or
                            self.client_port.yfilter != YFilter.not_set or
                            self.config_session_id.yfilter != YFilter.not_set or
                            self.elapsed_time.yfilter != YFilter.not_set or
                            self.last_state_change.yfilter != YFilter.not_set or
                            self.start_time.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.username.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/tty/sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.admin_config_session_id.is_set or self.admin_config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.admin_config_session_id.get_name_leafdata())
                        if (self.alarm_notification.is_set or self.alarm_notification.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_notification.get_name_leafdata())
                        if (self.client_address.is_set or self.client_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_address.get_name_leafdata())
                        if (self.client_port.is_set or self.client_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_port.get_name_leafdata())
                        if (self.config_session_id.is_set or self.config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_session_id.get_name_leafdata())
                        if (self.elapsed_time.is_set or self.elapsed_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.elapsed_time.get_name_leafdata())
                        if (self.last_state_change.is_set or self.last_state_change.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_state_change.get_name_leafdata())
                        if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_time.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.username.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-id" or name == "admin-config-session-id" or name == "alarm-notification" or name == "client-address" or name == "client-port" or name == "config-session-id" or name == "elapsed-time" or name == "last-state-change" or name == "start-time" or name == "state" or name == "username" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "admin-config-session-id"):
                            self.admin_config_session_id = value
                            self.admin_config_session_id.value_namespace = name_space
                            self.admin_config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "alarm-notification"):
                            self.alarm_notification = value
                            self.alarm_notification.value_namespace = name_space
                            self.alarm_notification.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-address"):
                            self.client_address = value
                            self.client_address.value_namespace = name_space
                            self.client_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-port"):
                            self.client_port = value
                            self.client_port.value_namespace = name_space
                            self.client_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "config-session-id"):
                            self.config_session_id = value
                            self.config_session_id.value_namespace = name_space
                            self.config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "elapsed-time"):
                            self.elapsed_time = value
                            self.elapsed_time.value_namespace = name_space
                            self.elapsed_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-state-change"):
                            self.last_state_change = value
                            self.last_state_change.value_namespace = name_space
                            self.last_state_change.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-time"):
                            self.start_time = value
                            self.start_time.value_namespace = name_space
                            self.start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "username"):
                            self.username = value
                            self.username.value_namespace = name_space
                            self.username.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

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
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/tty/%s" % self.get_segment_path()
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
                        c = Netconf.Agent.Tty.Sessions.Session()
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

            def has_data(self):
                return (self.sessions is not None and self.sessions.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.sessions is not None and self.sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tty" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sessions"):
                    if (self.sessions is None):
                        self.sessions = Netconf.Agent.Tty.Sessions()
                        self.sessions.parent = self
                        self._children_name_map["sessions"] = "sessions"
                    return self.sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.tty is not None and self.tty.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.tty is not None and self.tty.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "agent" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tty"):
                if (self.tty is None):
                    self.tty = Netconf.Agent.Tty()
                    self.tty.parent = self
                    self._children_name_map["tty"] = "tty"
                return self.tty

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tty"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.agent is not None and self.agent.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.agent is not None and self.agent.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:netconf" + path_buffer

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

        if (child_yang_name == "agent"):
            if (self.agent is None):
                self.agent = Netconf.Agent()
                self.agent.parent = self
                self._children_name_map["agent"] = "agent"
            return self.agent

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "agent"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Netconf()
        return self._top_entity

class XrXml(Entity):
    """
    xr xml
    
    .. attribute:: agent
    
    	XML agents
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-oper'
    _revision = '2015-07-30'

    def __init__(self):
        super(XrXml, self).__init__()
        self._top_entity = None

        self.yang_name = "xr-xml"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-oper"

        self.agent = XrXml.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")


    class Agent(Entity):
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
            super(XrXml.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "xr-xml"

            self.default = XrXml.Agent.Default()
            self.default.parent = self
            self._children_name_map["default"] = "default"
            self._children_yang_names.add("default")

            self.ssl = XrXml.Agent.Ssl()
            self.ssl.parent = self
            self._children_name_map["ssl"] = "ssl"
            self._children_yang_names.add("ssl")

            self.tty = XrXml.Agent.Tty()
            self.tty.parent = self
            self._children_name_map["tty"] = "tty"
            self._children_yang_names.add("tty")


        class Tty(Entity):
            """
            TTY sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"

                self.sessions = XrXml.Agent.Tty.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")


            class Sessions(Entity):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Tty.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Tty.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "tty"

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
                                super(XrXml.Agent.Tty.Sessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Tty.Sessions, self).__setattr__(name, value)


                class Session(Entity):
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
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
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
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
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
                        super(XrXml.Agent.Tty.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.username = YLeaf(YType.str, "username")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_id",
                                        "admin_config_session_id",
                                        "alarm_notification",
                                        "client_address",
                                        "client_port",
                                        "config_session_id",
                                        "elapsed_time",
                                        "last_state_change",
                                        "start_time",
                                        "state",
                                        "username",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(XrXml.Agent.Tty.Sessions.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(XrXml.Agent.Tty.Sessions.Session, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.session_id.is_set or
                            self.admin_config_session_id.is_set or
                            self.alarm_notification.is_set or
                            self.client_address.is_set or
                            self.client_port.is_set or
                            self.config_session_id.is_set or
                            self.elapsed_time.is_set or
                            self.last_state_change.is_set or
                            self.start_time.is_set or
                            self.state.is_set or
                            self.username.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.admin_config_session_id.yfilter != YFilter.not_set or
                            self.alarm_notification.yfilter != YFilter.not_set or
                            self.client_address.yfilter != YFilter.not_set or
                            self.client_port.yfilter != YFilter.not_set or
                            self.config_session_id.yfilter != YFilter.not_set or
                            self.elapsed_time.yfilter != YFilter.not_set or
                            self.last_state_change.yfilter != YFilter.not_set or
                            self.start_time.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.username.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/tty/sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.admin_config_session_id.is_set or self.admin_config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.admin_config_session_id.get_name_leafdata())
                        if (self.alarm_notification.is_set or self.alarm_notification.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_notification.get_name_leafdata())
                        if (self.client_address.is_set or self.client_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_address.get_name_leafdata())
                        if (self.client_port.is_set or self.client_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_port.get_name_leafdata())
                        if (self.config_session_id.is_set or self.config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_session_id.get_name_leafdata())
                        if (self.elapsed_time.is_set or self.elapsed_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.elapsed_time.get_name_leafdata())
                        if (self.last_state_change.is_set or self.last_state_change.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_state_change.get_name_leafdata())
                        if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_time.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.username.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-id" or name == "admin-config-session-id" or name == "alarm-notification" or name == "client-address" or name == "client-port" or name == "config-session-id" or name == "elapsed-time" or name == "last-state-change" or name == "start-time" or name == "state" or name == "username" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "admin-config-session-id"):
                            self.admin_config_session_id = value
                            self.admin_config_session_id.value_namespace = name_space
                            self.admin_config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "alarm-notification"):
                            self.alarm_notification = value
                            self.alarm_notification.value_namespace = name_space
                            self.alarm_notification.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-address"):
                            self.client_address = value
                            self.client_address.value_namespace = name_space
                            self.client_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-port"):
                            self.client_port = value
                            self.client_port.value_namespace = name_space
                            self.client_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "config-session-id"):
                            self.config_session_id = value
                            self.config_session_id.value_namespace = name_space
                            self.config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "elapsed-time"):
                            self.elapsed_time = value
                            self.elapsed_time.value_namespace = name_space
                            self.elapsed_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-state-change"):
                            self.last_state_change = value
                            self.last_state_change.value_namespace = name_space
                            self.last_state_change.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-time"):
                            self.start_time = value
                            self.start_time.value_namespace = name_space
                            self.start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "username"):
                            self.username = value
                            self.username.value_namespace = name_space
                            self.username.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

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
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/tty/%s" % self.get_segment_path()
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
                        c = XrXml.Agent.Tty.Sessions.Session()
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

            def has_data(self):
                return (self.sessions is not None and self.sessions.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.sessions is not None and self.sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tty" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sessions"):
                    if (self.sessions is None):
                        self.sessions = XrXml.Agent.Tty.Sessions()
                        self.sessions.parent = self
                        self._children_name_map["sessions"] = "sessions"
                    return self.sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Default(Entity):
            """
            Default sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Default, self).__init__()

                self.yang_name = "default"
                self.yang_parent_name = "agent"

                self.sessions = XrXml.Agent.Default.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")


            class Sessions(Entity):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Default.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Default.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "default"

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
                                super(XrXml.Agent.Default.Sessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Default.Sessions, self).__setattr__(name, value)


                class Session(Entity):
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
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
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
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
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
                        super(XrXml.Agent.Default.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.username = YLeaf(YType.str, "username")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_id",
                                        "admin_config_session_id",
                                        "alarm_notification",
                                        "client_address",
                                        "client_port",
                                        "config_session_id",
                                        "elapsed_time",
                                        "last_state_change",
                                        "start_time",
                                        "state",
                                        "username",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(XrXml.Agent.Default.Sessions.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(XrXml.Agent.Default.Sessions.Session, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.session_id.is_set or
                            self.admin_config_session_id.is_set or
                            self.alarm_notification.is_set or
                            self.client_address.is_set or
                            self.client_port.is_set or
                            self.config_session_id.is_set or
                            self.elapsed_time.is_set or
                            self.last_state_change.is_set or
                            self.start_time.is_set or
                            self.state.is_set or
                            self.username.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.admin_config_session_id.yfilter != YFilter.not_set or
                            self.alarm_notification.yfilter != YFilter.not_set or
                            self.client_address.yfilter != YFilter.not_set or
                            self.client_port.yfilter != YFilter.not_set or
                            self.config_session_id.yfilter != YFilter.not_set or
                            self.elapsed_time.yfilter != YFilter.not_set or
                            self.last_state_change.yfilter != YFilter.not_set or
                            self.start_time.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.username.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/default/sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.admin_config_session_id.is_set or self.admin_config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.admin_config_session_id.get_name_leafdata())
                        if (self.alarm_notification.is_set or self.alarm_notification.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_notification.get_name_leafdata())
                        if (self.client_address.is_set or self.client_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_address.get_name_leafdata())
                        if (self.client_port.is_set or self.client_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_port.get_name_leafdata())
                        if (self.config_session_id.is_set or self.config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_session_id.get_name_leafdata())
                        if (self.elapsed_time.is_set or self.elapsed_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.elapsed_time.get_name_leafdata())
                        if (self.last_state_change.is_set or self.last_state_change.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_state_change.get_name_leafdata())
                        if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_time.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.username.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-id" or name == "admin-config-session-id" or name == "alarm-notification" or name == "client-address" or name == "client-port" or name == "config-session-id" or name == "elapsed-time" or name == "last-state-change" or name == "start-time" or name == "state" or name == "username" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "admin-config-session-id"):
                            self.admin_config_session_id = value
                            self.admin_config_session_id.value_namespace = name_space
                            self.admin_config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "alarm-notification"):
                            self.alarm_notification = value
                            self.alarm_notification.value_namespace = name_space
                            self.alarm_notification.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-address"):
                            self.client_address = value
                            self.client_address.value_namespace = name_space
                            self.client_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-port"):
                            self.client_port = value
                            self.client_port.value_namespace = name_space
                            self.client_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "config-session-id"):
                            self.config_session_id = value
                            self.config_session_id.value_namespace = name_space
                            self.config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "elapsed-time"):
                            self.elapsed_time = value
                            self.elapsed_time.value_namespace = name_space
                            self.elapsed_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-state-change"):
                            self.last_state_change = value
                            self.last_state_change.value_namespace = name_space
                            self.last_state_change.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-time"):
                            self.start_time = value
                            self.start_time.value_namespace = name_space
                            self.start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "username"):
                            self.username = value
                            self.username.value_namespace = name_space
                            self.username.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

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
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/default/%s" % self.get_segment_path()
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
                        c = XrXml.Agent.Default.Sessions.Session()
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

            def has_data(self):
                return (self.sessions is not None and self.sessions.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.sessions is not None and self.sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "default" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sessions"):
                    if (self.sessions is None):
                        self.sessions = XrXml.Agent.Default.Sessions()
                        self.sessions.parent = self
                        self._children_name_map["sessions"] = "sessions"
                    return self.sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Ssl(Entity):
            """
            SSL sessions information
            
            .. attribute:: sessions
            
            	sessions information
            	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions>`
            
            

            """

            _prefix = 'man-xml-ttyagent-oper'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Ssl, self).__init__()

                self.yang_name = "ssl"
                self.yang_parent_name = "agent"

                self.sessions = XrXml.Agent.Ssl.Sessions()
                self.sessions.parent = self
                self._children_name_map["sessions"] = "sessions"
                self._children_yang_names.add("sessions")


            class Sessions(Entity):
                """
                sessions information
                
                .. attribute:: session
                
                	xml sessions information
                	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXml.Agent.Ssl.Sessions.Session>`
                
                

                """

                _prefix = 'man-xml-ttyagent-oper'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Sessions, self).__init__()

                    self.yang_name = "sessions"
                    self.yang_parent_name = "ssl"

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
                                super(XrXml.Agent.Ssl.Sessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Ssl.Sessions, self).__setattr__(name, value)


                class Session(Entity):
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
                    	**type**\:   :py:class:`XrXmlSessionAlarmRegister <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionAlarmRegister>`
                    
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
                    	**type**\:   :py:class:`XrXmlSessionState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper.XrXmlSessionState>`
                    
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
                        super(XrXml.Agent.Ssl.Sessions.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "sessions"

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.admin_config_session_id = YLeaf(YType.str, "admin-config-session-id")

                        self.alarm_notification = YLeaf(YType.enumeration, "alarm-notification")

                        self.client_address = YLeaf(YType.str, "client-address")

                        self.client_port = YLeaf(YType.uint32, "client-port")

                        self.config_session_id = YLeaf(YType.str, "config-session-id")

                        self.elapsed_time = YLeaf(YType.uint32, "elapsed-time")

                        self.last_state_change = YLeaf(YType.uint32, "last-state-change")

                        self.start_time = YLeaf(YType.uint32, "start-time")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.username = YLeaf(YType.str, "username")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session_id",
                                        "admin_config_session_id",
                                        "alarm_notification",
                                        "client_address",
                                        "client_port",
                                        "config_session_id",
                                        "elapsed_time",
                                        "last_state_change",
                                        "start_time",
                                        "state",
                                        "username",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(XrXml.Agent.Ssl.Sessions.Session, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(XrXml.Agent.Ssl.Sessions.Session, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.session_id.is_set or
                            self.admin_config_session_id.is_set or
                            self.alarm_notification.is_set or
                            self.client_address.is_set or
                            self.client_port.is_set or
                            self.config_session_id.is_set or
                            self.elapsed_time.is_set or
                            self.last_state_change.is_set or
                            self.start_time.is_set or
                            self.state.is_set or
                            self.username.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.admin_config_session_id.yfilter != YFilter.not_set or
                            self.alarm_notification.yfilter != YFilter.not_set or
                            self.client_address.yfilter != YFilter.not_set or
                            self.client_port.yfilter != YFilter.not_set or
                            self.config_session_id.yfilter != YFilter.not_set or
                            self.elapsed_time.yfilter != YFilter.not_set or
                            self.last_state_change.yfilter != YFilter.not_set or
                            self.start_time.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.username.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/ssl/sessions/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.admin_config_session_id.is_set or self.admin_config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.admin_config_session_id.get_name_leafdata())
                        if (self.alarm_notification.is_set or self.alarm_notification.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.alarm_notification.get_name_leafdata())
                        if (self.client_address.is_set or self.client_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_address.get_name_leafdata())
                        if (self.client_port.is_set or self.client_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.client_port.get_name_leafdata())
                        if (self.config_session_id.is_set or self.config_session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.config_session_id.get_name_leafdata())
                        if (self.elapsed_time.is_set or self.elapsed_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.elapsed_time.get_name_leafdata())
                        if (self.last_state_change.is_set or self.last_state_change.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.last_state_change.get_name_leafdata())
                        if (self.start_time.is_set or self.start_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.start_time.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.username.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "session-id" or name == "admin-config-session-id" or name == "alarm-notification" or name == "client-address" or name == "client-port" or name == "config-session-id" or name == "elapsed-time" or name == "last-state-change" or name == "start-time" or name == "state" or name == "username" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "admin-config-session-id"):
                            self.admin_config_session_id = value
                            self.admin_config_session_id.value_namespace = name_space
                            self.admin_config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "alarm-notification"):
                            self.alarm_notification = value
                            self.alarm_notification.value_namespace = name_space
                            self.alarm_notification.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-address"):
                            self.client_address = value
                            self.client_address.value_namespace = name_space
                            self.client_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "client-port"):
                            self.client_port = value
                            self.client_port.value_namespace = name_space
                            self.client_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "config-session-id"):
                            self.config_session_id = value
                            self.config_session_id.value_namespace = name_space
                            self.config_session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "elapsed-time"):
                            self.elapsed_time = value
                            self.elapsed_time.value_namespace = name_space
                            self.elapsed_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "last-state-change"):
                            self.last_state_change = value
                            self.last_state_change.value_namespace = name_space
                            self.last_state_change.value_namespace_prefix = name_space_prefix
                        if(value_path == "start-time"):
                            self.start_time = value
                            self.start_time.value_namespace = name_space
                            self.start_time.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "username"):
                            self.username = value
                            self.username.value_namespace = name_space
                            self.username.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

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
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/ssl/%s" % self.get_segment_path()
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
                        c = XrXml.Agent.Ssl.Sessions.Session()
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

            def has_data(self):
                return (self.sessions is not None and self.sessions.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.sessions is not None and self.sessions.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ssl" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sessions"):
                    if (self.sessions is None):
                        self.sessions = XrXml.Agent.Ssl.Sessions()
                        self.sessions.parent = self
                        self._children_name_map["sessions"] = "sessions"
                    return self.sessions

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.default is not None and self.default.has_data()) or
                (self.ssl is not None and self.ssl.has_data()) or
                (self.tty is not None and self.tty.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.default is not None and self.default.has_operation()) or
                (self.ssl is not None and self.ssl.has_operation()) or
                (self.tty is not None and self.tty.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "agent" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "default"):
                if (self.default is None):
                    self.default = XrXml.Agent.Default()
                    self.default.parent = self
                    self._children_name_map["default"] = "default"
                return self.default

            if (child_yang_name == "ssl"):
                if (self.ssl is None):
                    self.ssl = XrXml.Agent.Ssl()
                    self.ssl.parent = self
                    self._children_name_map["ssl"] = "ssl"
                return self.ssl

            if (child_yang_name == "tty"):
                if (self.tty is None):
                    self.tty = XrXml.Agent.Tty()
                    self.tty.parent = self
                    self._children_name_map["tty"] = "tty"
                return self.tty

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "default" or name == "ssl" or name == "tty"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.agent is not None and self.agent.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.agent is not None and self.agent.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-oper:xr-xml" + path_buffer

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

        if (child_yang_name == "agent"):
            if (self.agent is None):
                self.agent = XrXml.Agent()
                self.agent.parent = self
                self._children_name_map["agent"] = "agent"
            return self.agent

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "agent"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = XrXml()
        return self._top_entity

