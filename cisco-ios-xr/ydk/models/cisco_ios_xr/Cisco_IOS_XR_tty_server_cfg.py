""" Cisco_IOS_XR_tty_server_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package configuration.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Tty(Entity):
    """
    TTY Line Configuration
    
    .. attribute:: tty_lines
    
    	TTY templates
    	**type**\:   :py:class:`TtyLines <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines>`
    
    

    """

    _prefix = 'tty-server-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(Tty, self).__init__()
        self._top_entity = None

        self.yang_name = "tty"
        self.yang_parent_name = "Cisco-IOS-XR-tty-server-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"tty-lines" : ("tty_lines", Tty.TtyLines)}
        self._child_list_classes = {}

        self.tty_lines = Tty.TtyLines()
        self.tty_lines.parent = self
        self._children_name_map["tty_lines"] = "tty-lines"
        self._children_yang_names.add("tty-lines")
        self._segment_path = lambda: "Cisco-IOS-XR-tty-server-cfg:tty"


    class TtyLines(Entity):
        """
        TTY templates
        
        .. attribute:: tty_line
        
        	TTY Line,Use string 'console' to configure a console line,Use string 'default' to configure a default line,Use any string to configure a user defined template
        	**type**\: list of    :py:class:`TtyLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine>`
        
        

        """

        _prefix = 'tty-server-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(Tty.TtyLines, self).__init__()

            self.yang_name = "tty-lines"
            self.yang_parent_name = "tty"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"tty-line" : ("tty_line", Tty.TtyLines.TtyLine)}

            self.tty_line = YList(self)
            self._segment_path = lambda: "tty-lines"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-cfg:tty/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.TtyLines, [], name, value)


        class TtyLine(Entity):
            """
            TTY Line,Use string 'console' to configure a
            console line,Use string 'default' to configure
            a default line,Use any string to configure a
            user defined template
            
            .. attribute:: name  <key>
            
            	Name of the template
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: aaa
            
            	Container class for AAA related TTY configuration
            	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa>`
            
            .. attribute:: connection
            
            	Management connection configuration
            	**type**\:   :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection>`
            
            .. attribute:: exec_
            
            	EXEC timeout and timestamp configurtion
            	**type**\:   :py:class:`Exec_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Exec_>`
            
            .. attribute:: exec_mode
            
            	Exec Mode Pager  configurtion
            	**type**\:   :py:class:`ExecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.ExecMode>`
            
            .. attribute:: general
            
            	TTY line general configuration
            	**type**\:   :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.General>`
            
            .. attribute:: telnet
            
            	Telnet protocol\-specific configuration
            	**type**\:   :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Telnet>`
            
            

            """

            _prefix = 'tty-server-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(Tty.TtyLines.TtyLine, self).__init__()

                self.yang_name = "tty-line"
                self.yang_parent_name = "tty-lines"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"aaa" : ("aaa", Tty.TtyLines.TtyLine.Aaa), "connection" : ("connection", Tty.TtyLines.TtyLine.Connection), "exec" : ("exec_", Tty.TtyLines.TtyLine.Exec_), "exec-mode" : ("exec_mode", Tty.TtyLines.TtyLine.ExecMode), "general" : ("general", Tty.TtyLines.TtyLine.General), "telnet" : ("telnet", Tty.TtyLines.TtyLine.Telnet)}
                self._child_list_classes = {}

                self.name = YLeaf(YType.str, "name")

                self.aaa = Tty.TtyLines.TtyLine.Aaa()
                self.aaa.parent = self
                self._children_name_map["aaa"] = "aaa"
                self._children_yang_names.add("aaa")

                self.connection = Tty.TtyLines.TtyLine.Connection()
                self.connection.parent = self
                self._children_name_map["connection"] = "connection"
                self._children_yang_names.add("connection")

                self.exec_ = Tty.TtyLines.TtyLine.Exec_()
                self.exec_.parent = self
                self._children_name_map["exec_"] = "exec"
                self._children_yang_names.add("exec")

                self.exec_mode = Tty.TtyLines.TtyLine.ExecMode()
                self.exec_mode.parent = self
                self._children_name_map["exec_mode"] = "exec-mode"
                self._children_yang_names.add("exec-mode")

                self.general = Tty.TtyLines.TtyLine.General()
                self.general.parent = self
                self._children_name_map["general"] = "general"
                self._children_yang_names.add("general")

                self.telnet = Tty.TtyLines.TtyLine.Telnet()
                self.telnet.parent = self
                self._children_name_map["telnet"] = "telnet"
                self._children_yang_names.add("telnet")
                self._segment_path = lambda: "tty-line" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-cfg:tty/tty-lines/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.TtyLines.TtyLine, ['name'], name, value)


            class Aaa(Entity):
                """
                Container class for AAA related TTY
                configuration
                
                .. attribute:: accounting
                
                	Accounting parameters
                	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Accounting>`
                
                .. attribute:: authentication
                
                	Authentication parameters
                	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Authentication>`
                
                .. attribute:: authorization
                
                	Authorization parameters
                	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Authorization>`
                
                .. attribute:: login_timeout
                
                	Timeouts for any user input during login sequence
                	**type**\:  int
                
                	**range:** 0..300
                
                	**units**\: second
                
                	**default value**\: 30
                
                .. attribute:: password
                
                	Configure the password for the user
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: secret
                
                	Configure a secure one way encrypted password
                	**type**\:  str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: user_groups
                
                	Users characteristics
                	**type**\:   :py:class:`UserGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.UserGroups>`
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Aaa, self).__init__()

                    self.yang_name = "aaa"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"accounting" : ("accounting", Tty.TtyLines.TtyLine.Aaa.Accounting), "authentication" : ("authentication", Tty.TtyLines.TtyLine.Aaa.Authentication), "authorization" : ("authorization", Tty.TtyLines.TtyLine.Aaa.Authorization), "user-groups" : ("user_groups", Tty.TtyLines.TtyLine.Aaa.UserGroups)}
                    self._child_list_classes = {}

                    self.login_timeout = YLeaf(YType.uint32, "login-timeout")

                    self.password = YLeaf(YType.str, "password")

                    self.secret = YLeaf(YType.str, "secret")

                    self.accounting = Tty.TtyLines.TtyLine.Aaa.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                    self._children_yang_names.add("accounting")

                    self.authentication = Tty.TtyLines.TtyLine.Aaa.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"
                    self._children_yang_names.add("authentication")

                    self.authorization = Tty.TtyLines.TtyLine.Aaa.Authorization()
                    self.authorization.parent = self
                    self._children_name_map["authorization"] = "authorization"
                    self._children_yang_names.add("authorization")

                    self.user_groups = Tty.TtyLines.TtyLine.Aaa.UserGroups()
                    self.user_groups.parent = self
                    self._children_name_map["user_groups"] = "user-groups"
                    self._children_yang_names.add("user-groups")
                    self._segment_path = lambda: "aaa"

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Aaa, ['login_timeout', 'password', 'secret'], name, value)


                class Accounting(Entity):
                    """
                    Accounting parameters
                    
                    .. attribute:: commands
                    
                    	For exec (shell) configuration
                    	**type**\:  str
                    
                    .. attribute:: exec_
                    
                    	For starting an exec (shell)
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.Accounting, self).__init__()

                        self.yang_name = "accounting"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.commands = YLeaf(YType.str, "commands")

                        self.exec_ = YLeaf(YType.str, "exec")
                        self._segment_path = lambda: "accounting"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.Accounting, ['commands', 'exec_'], name, value)


                class Authentication(Entity):
                    """
                    Authentication parameters
                    
                    .. attribute:: login
                    
                    	Authentication list name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.login = YLeaf(YType.str, "login")
                        self._segment_path = lambda: "authentication"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.Authentication, ['login'], name, value)


                class Authorization(Entity):
                    """
                    Authorization parameters
                    
                    .. attribute:: commands
                    
                    	For exec (shell) configuration
                    	**type**\:  str
                    
                    .. attribute:: event_manager
                    
                    	Specify 'default' or use an authorization list with this name
                    	**type**\:  str
                    
                    .. attribute:: exec_
                    
                    	For starting an exec (shell)
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.Authorization, self).__init__()

                        self.yang_name = "authorization"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.commands = YLeaf(YType.str, "commands")

                        self.event_manager = YLeaf(YType.str, "event-manager")

                        self.exec_ = YLeaf(YType.str, "exec")
                        self._segment_path = lambda: "authorization"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.Authorization, ['commands', 'event_manager', 'exec_'], name, value)


                class UserGroups(Entity):
                    """
                    Users characteristics
                    
                    .. attribute:: user_group
                    
                    	Group to which the user will belong
                    	**type**\: list of    :py:class:`UserGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup>`
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.UserGroups, self).__init__()

                        self.yang_name = "user-groups"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"user-group" : ("user_group", Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup)}

                        self.user_group = YList(self)
                        self._segment_path = lambda: "user-groups"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.UserGroups, [], name, value)


                    class UserGroup(Entity):
                        """
                        Group to which the user will belong
                        
                        .. attribute:: name  <key>
                        
                        	Name of the group
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: category
                        
                        	Specify as 'root\-system' for root\-system group and 'other' for remaining groups
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'tty-server-cfg'
                        _revision = '2015-07-30'

                        def __init__(self):
                            super(Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup, self).__init__()

                            self.yang_name = "user-group"
                            self.yang_parent_name = "user-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.category = YLeaf(YType.str, "category")
                            self._segment_path = lambda: "user-group" + "[name='" + self.name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup, ['name', 'category'], name, value)


            class Connection(Entity):
                """
                Management connection configuration
                
                .. attribute:: acl_in
                
                	ACL to filter ingoing connections
                	**type**\:  str
                
                .. attribute:: acl_out
                
                	ACL to filter outgoing connections
                	**type**\:  str
                
                .. attribute:: cli_white_space_completion
                
                	Command completion on whitespace
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: disconnect_character
                
                	Disconnect character's decimal equivalent value or Character 
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (\\p{IsBasicLatin}\|\\p{IsLatin\-1Supplement})\*
                
                
                ----
                	**type**\:  int
                
                	**range:** 0..255
                
                
                ----
                .. attribute:: escape_character
                
                	Escape character or ASCII decimal equivalent value orspecial strings NONE,DEFAULT,BREAK
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** ((\\p{IsBasicLatin}\|\\p{IsLatin\-1Supplement})\*)\|(DEFAULT)\|(BREAK)\|(NONE)
                
                	**default value**\: 30
                
                
                ----
                	**type**\:  int
                
                	**range:** 0..255
                
                	**default value**\: 30
                
                
                ----
                .. attribute:: session_limit
                
                	The number of outgoing connections
                	**type**\:  int
                
                	**range:** 0..20
                
                	**default value**\: 6
                
                .. attribute:: session_timeout
                
                	Interval for closing connection when there is no input traffic
                	**type**\:   :py:class:`SessionTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.SessionTimeout>`
                
                	**presence node**\: True
                
                .. attribute:: transport_input
                
                	Protocols to use when connecting to the terminal server
                	**type**\:   :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.TransportInput>`
                
                .. attribute:: transport_output
                
                	Protocols to use for outgoing connections
                	**type**\:   :py:class:`TransportOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.TransportOutput>`
                
                	**presence node**\: True
                
                .. attribute:: transport_preferred
                
                	The preferred protocol to use
                	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                
                

                """

                _prefix = 'tty-management-cfg'
                _revision = '2015-09-25'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Connection, self).__init__()

                    self.yang_name = "connection"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"session-timeout" : ("session_timeout", Tty.TtyLines.TtyLine.Connection.SessionTimeout), "transport-input" : ("transport_input", Tty.TtyLines.TtyLine.Connection.TransportInput), "transport-output" : ("transport_output", Tty.TtyLines.TtyLine.Connection.TransportOutput)}
                    self._child_list_classes = {}

                    self.acl_in = YLeaf(YType.str, "acl-in")

                    self.acl_out = YLeaf(YType.str, "acl-out")

                    self.cli_white_space_completion = YLeaf(YType.empty, "cli-white-space-completion")

                    self.disconnect_character = YLeaf(YType.str, "disconnect-character")

                    self.escape_character = YLeaf(YType.str, "escape-character")

                    self.session_limit = YLeaf(YType.uint32, "session-limit")

                    self.transport_preferred = YLeaf(YType.enumeration, "transport-preferred")

                    self.session_timeout = None
                    self._children_name_map["session_timeout"] = "session-timeout"
                    self._children_yang_names.add("session-timeout")

                    self.transport_input = Tty.TtyLines.TtyLine.Connection.TransportInput()
                    self.transport_input.parent = self
                    self._children_name_map["transport_input"] = "transport-input"
                    self._children_yang_names.add("transport-input")

                    self.transport_output = None
                    self._children_name_map["transport_output"] = "transport-output"
                    self._children_yang_names.add("transport-output")
                    self._segment_path = lambda: "Cisco-IOS-XR-tty-management-cfg:connection"

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Connection, ['acl_in', 'acl_out', 'cli_white_space_completion', 'disconnect_character', 'escape_character', 'session_limit', 'transport_preferred'], name, value)


                class SessionTimeout(Entity):
                    """
                    Interval for closing connection when there is
                    no input traffic
                    
                    .. attribute:: direction
                    
                    	Include output traffic as well as input traffic
                    	**type**\:   :py:class:`TtySessionTimeoutDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtySessionTimeoutDirection>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: timeout
                    
                    	Session timeout interval in minutes
                    	**type**\:  int
                    
                    	**range:** 0..35791
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2015-09-25'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Connection.SessionTimeout, self).__init__()

                        self.yang_name = "session-timeout"
                        self.yang_parent_name = "connection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.direction = YLeaf(YType.enumeration, "direction")

                        self.timeout = YLeaf(YType.uint32, "timeout")
                        self._segment_path = lambda: "session-timeout"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Connection.SessionTimeout, ['direction', 'timeout'], name, value)


                class TransportInput(Entity):
                    """
                    Protocols to use when connecting to the
                    terminal server
                    
                    .. attribute:: none
                    
                    	Not used
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: protocol1
                    
                    	Transport protocol1
                    	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: protocol2
                    
                    	Transport protocol2
                    	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: select
                    
                    	Choose transport protocols
                    	**type**\:   :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                    
                    	**default value**\: all
                    
                    

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2015-09-25'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Connection.TransportInput, self).__init__()

                        self.yang_name = "transport-input"
                        self.yang_parent_name = "connection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.none = YLeaf(YType.int32, "none")

                        self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                        self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                        self.select = YLeaf(YType.enumeration, "select")
                        self._segment_path = lambda: "transport-input"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Connection.TransportInput, ['none', 'protocol1', 'protocol2', 'select'], name, value)


                class TransportOutput(Entity):
                    """
                    Protocols to use for outgoing connections
                    
                    .. attribute:: none
                    
                    	Not used
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: protocol1
                    
                    	Transport protocol1
                    	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: protocol2
                    
                    	Transport protocol2
                    	**type**\:   :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: select
                    
                    	Choose transport protocols
                    	**type**\:   :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2015-09-25'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Connection.TransportOutput, self).__init__()

                        self.yang_name = "transport-output"
                        self.yang_parent_name = "connection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.none = YLeaf(YType.int32, "none")

                        self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                        self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                        self.select = YLeaf(YType.enumeration, "select")
                        self._segment_path = lambda: "transport-output"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Connection.TransportOutput, ['none', 'protocol1', 'protocol2', 'select'], name, value)


            class ExecMode(Entity):
                """
                Exec Mode Pager  configurtion
                
                .. attribute:: pager
                
                	Preferred Paging Utility
                	**type**\:   :py:class:`TtyPager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyPager>`
                
                	**default value**\: more
                
                

                """

                _prefix = 'tty-management-cfg'
                _revision = '2015-09-25'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.ExecMode, self).__init__()

                    self.yang_name = "exec-mode"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.pager = YLeaf(YType.enumeration, "pager")
                    self._segment_path = lambda: "Cisco-IOS-XR-tty-management-cfg:exec-mode"

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.ExecMode, ['pager'], name, value)


            class Exec_(Entity):
                """
                EXEC timeout and timestamp configurtion
                
                .. attribute:: time_stamp
                
                	'True' to Enable & 'False' to Disable time stamp
                	**type**\:  bool
                
                .. attribute:: timeout
                
                	EXEC Timeout
                	**type**\:   :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Exec_.Timeout>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Exec_, self).__init__()

                    self.yang_name = "exec"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"timeout" : ("timeout", Tty.TtyLines.TtyLine.Exec_.Timeout)}
                    self._child_list_classes = {}

                    self.time_stamp = YLeaf(YType.boolean, "time-stamp")

                    self.timeout = None
                    self._children_name_map["timeout"] = "timeout"
                    self._children_yang_names.add("timeout")
                    self._segment_path = lambda: "exec"

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Exec_, ['time_stamp'], name, value)


                class Timeout(Entity):
                    """
                    EXEC Timeout
                    
                    .. attribute:: minutes
                    
                    	Timeout in minutes
                    	**type**\:  int
                    
                    	**range:** 0..35791
                    
                    	**mandatory**\: True
                    
                    	**units**\: minute
                    
                    .. attribute:: seconds
                    
                    	Timeout in seconds
                    	**type**\:  int
                    
                    	**range:** 0..2147483
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Exec_.Timeout, self).__init__()

                        self.yang_name = "timeout"
                        self.yang_parent_name = "exec"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.minutes = YLeaf(YType.uint32, "minutes")

                        self.seconds = YLeaf(YType.uint32, "seconds")
                        self._segment_path = lambda: "timeout"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Exec_.Timeout, ['minutes', 'seconds'], name, value)


            class General(Entity):
                """
                TTY line general configuration
                
                .. attribute:: absolute_timeout
                
                	Absolute timeout for line disconnection
                	**type**\:  int
                
                	**range:** 0..10000
                
                	**units**\: minute
                
                	**default value**\: 0
                
                .. attribute:: length
                
                	Number of lines on a screen
                	**type**\:  int
                
                	**range:** 0..512
                
                	**default value**\: 24
                
                .. attribute:: width
                
                	Number of characters on a screen line
                	**type**\:  int
                
                	**range:** 0..512
                
                	**default value**\: 80
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.General, self).__init__()

                    self.yang_name = "general"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.absolute_timeout = YLeaf(YType.uint32, "absolute-timeout")

                    self.length = YLeaf(YType.uint32, "length")

                    self.width = YLeaf(YType.uint32, "width")
                    self._segment_path = lambda: "general"

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.General, ['absolute_timeout', 'length', 'width'], name, value)


            class Telnet(Entity):
                """
                Telnet protocol\-specific configuration
                
                .. attribute:: transparent
                
                	Send a CR as a CR followed by a NULL instead of a CRfollowed by a LF
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Telnet, self).__init__()

                    self.yang_name = "telnet"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.transparent = YLeaf(YType.empty, "transparent")
                    self._segment_path = lambda: "telnet"

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Telnet, ['transparent'], name, value)

    def clone_ptr(self):
        self._top_entity = Tty()
        return self._top_entity

