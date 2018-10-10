""" Cisco_IOS_XR_tty_server_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package configuration.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Tty(Entity):
    """
    TTY Line Configuration
    
    .. attribute:: tty_lines
    
    	TTY templates
    	**type**\:  :py:class:`TtyLines <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("tty-lines", ("tty_lines", Tty.TtyLines))])
        self._leafs = OrderedDict()

        self.tty_lines = Tty.TtyLines()
        self.tty_lines.parent = self
        self._children_name_map["tty_lines"] = "tty-lines"
        self._segment_path = lambda: "Cisco-IOS-XR-tty-server-cfg:tty"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Tty, [], name, value)


    class TtyLines(Entity):
        """
        TTY templates
        
        .. attribute:: tty_line
        
        	TTY Line,Use string 'console' to configure a console line,Use string 'default' to configure a default line,Use any string to configure a user defined template
        	**type**\: list of  		 :py:class:`TtyLine <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine>`
        
        

        """

        _prefix = 'tty-server-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(Tty.TtyLines, self).__init__()

            self.yang_name = "tty-lines"
            self.yang_parent_name = "tty"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tty-line", ("tty_line", Tty.TtyLines.TtyLine))])
            self._leafs = OrderedDict()

            self.tty_line = YList(self)
            self._segment_path = lambda: "tty-lines"
            self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-cfg:tty/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Tty.TtyLines, [], name, value)


        class TtyLine(Entity):
            """
            TTY Line,Use string 'console' to configure a
            console line,Use string 'default' to configure
            a default line,Use any string to configure a
            user defined template
            
            .. attribute:: name  (key)
            
            	Name of the template
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: general
            
            	TTY line general configuration
            	**type**\:  :py:class:`General <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.General>`
            
            .. attribute:: telnet
            
            	Telnet protocol\-specific configuration
            	**type**\:  :py:class:`Telnet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Telnet>`
            
            .. attribute:: aaa
            
            	Container class for AAA related TTY configuration
            	**type**\:  :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa>`
            
            .. attribute:: exec_
            
            	EXEC timeout and timestamp configurtion
            	**type**\:  :py:class:`Exec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Exec>`
            
            .. attribute:: connection
            
            	Management connection configuration
            	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection>`
            
            .. attribute:: exec_mode
            
            	Exec Mode Pager  configurtion
            	**type**\:  :py:class:`ExecMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.ExecMode>`
            
            

            """

            _prefix = 'tty-server-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(Tty.TtyLines.TtyLine, self).__init__()

                self.yang_name = "tty-line"
                self.yang_parent_name = "tty-lines"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("general", ("general", Tty.TtyLines.TtyLine.General)), ("telnet", ("telnet", Tty.TtyLines.TtyLine.Telnet)), ("aaa", ("aaa", Tty.TtyLines.TtyLine.Aaa)), ("exec", ("exec_", Tty.TtyLines.TtyLine.Exec)), ("Cisco-IOS-XR-tty-management-cfg:connection", ("connection", Tty.TtyLines.TtyLine.Connection)), ("Cisco-IOS-XR-tty-management-cfg:exec-mode", ("exec_mode", Tty.TtyLines.TtyLine.ExecMode))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.general = Tty.TtyLines.TtyLine.General()
                self.general.parent = self
                self._children_name_map["general"] = "general"

                self.telnet = Tty.TtyLines.TtyLine.Telnet()
                self.telnet.parent = self
                self._children_name_map["telnet"] = "telnet"

                self.aaa = Tty.TtyLines.TtyLine.Aaa()
                self.aaa.parent = self
                self._children_name_map["aaa"] = "aaa"

                self.exec_ = Tty.TtyLines.TtyLine.Exec()
                self.exec_.parent = self
                self._children_name_map["exec_"] = "exec"

                self.connection = Tty.TtyLines.TtyLine.Connection()
                self.connection.parent = self
                self._children_name_map["connection"] = "Cisco-IOS-XR-tty-management-cfg:connection"

                self.exec_mode = Tty.TtyLines.TtyLine.ExecMode()
                self.exec_mode.parent = self
                self._children_name_map["exec_mode"] = "Cisco-IOS-XR-tty-management-cfg:exec-mode"
                self._segment_path = lambda: "tty-line" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tty-server-cfg:tty/tty-lines/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Tty.TtyLines.TtyLine, ['name'], name, value)


            class General(Entity):
                """
                TTY line general configuration
                
                .. attribute:: length
                
                	Number of lines on a screen
                	**type**\: int
                
                	**range:** 0..512
                
                	**default value**\: 24
                
                .. attribute:: absolute_timeout
                
                	Absolute timeout for line disconnection
                	**type**\: int
                
                	**range:** 0..10000
                
                	**units**\: minute
                
                	**default value**\: 0
                
                .. attribute:: width
                
                	Number of characters on a screen line
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('length', (YLeaf(YType.uint32, 'length'), ['int'])),
                        ('absolute_timeout', (YLeaf(YType.uint32, 'absolute-timeout'), ['int'])),
                        ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                    ])
                    self.length = None
                    self.absolute_timeout = None
                    self.width = None
                    self._segment_path = lambda: "general"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.General, ['length', 'absolute_timeout', 'width'], name, value)


            class Telnet(Entity):
                """
                Telnet protocol\-specific configuration
                
                .. attribute:: transparent
                
                	Send a CR as a CR followed by a NULL instead of a CRfollowed by a LF
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Telnet, self).__init__()

                    self.yang_name = "telnet"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('transparent', (YLeaf(YType.empty, 'transparent'), ['Empty'])),
                    ])
                    self.transparent = None
                    self._segment_path = lambda: "telnet"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Telnet, ['transparent'], name, value)


            class Aaa(Entity):
                """
                Container class for AAA related TTY
                configuration
                
                .. attribute:: user_groups
                
                	Users characteristics
                	**type**\:  :py:class:`UserGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.UserGroups>`
                
                .. attribute:: authorization
                
                	Authorization parameters
                	**type**\:  :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Authorization>`
                
                .. attribute:: authentication
                
                	Authentication parameters
                	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Authentication>`
                
                .. attribute:: accounting
                
                	Accounting parameters
                	**type**\:  :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.Accounting>`
                
                .. attribute:: login_timeout
                
                	Timeouts for any user input during login sequence
                	**type**\: int
                
                	**range:** 0..300
                
                	**units**\: second
                
                	**default value**\: 30
                
                .. attribute:: secret
                
                	Configure a secure one way encrypted password
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: password
                
                	Configure the password for the user
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Aaa, self).__init__()

                    self.yang_name = "aaa"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("user-groups", ("user_groups", Tty.TtyLines.TtyLine.Aaa.UserGroups)), ("authorization", ("authorization", Tty.TtyLines.TtyLine.Aaa.Authorization)), ("authentication", ("authentication", Tty.TtyLines.TtyLine.Aaa.Authentication)), ("accounting", ("accounting", Tty.TtyLines.TtyLine.Aaa.Accounting))])
                    self._leafs = OrderedDict([
                        ('login_timeout', (YLeaf(YType.uint32, 'login-timeout'), ['int'])),
                        ('secret', (YLeaf(YType.str, 'secret'), ['str'])),
                        ('password', (YLeaf(YType.str, 'password'), ['str'])),
                    ])
                    self.login_timeout = None
                    self.secret = None
                    self.password = None

                    self.user_groups = Tty.TtyLines.TtyLine.Aaa.UserGroups()
                    self.user_groups.parent = self
                    self._children_name_map["user_groups"] = "user-groups"

                    self.authorization = Tty.TtyLines.TtyLine.Aaa.Authorization()
                    self.authorization.parent = self
                    self._children_name_map["authorization"] = "authorization"

                    self.authentication = Tty.TtyLines.TtyLine.Aaa.Authentication()
                    self.authentication.parent = self
                    self._children_name_map["authentication"] = "authentication"

                    self.accounting = Tty.TtyLines.TtyLine.Aaa.Accounting()
                    self.accounting.parent = self
                    self._children_name_map["accounting"] = "accounting"
                    self._segment_path = lambda: "aaa"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Aaa, ['login_timeout', 'secret', 'password'], name, value)


                class UserGroups(Entity):
                    """
                    Users characteristics
                    
                    .. attribute:: user_group
                    
                    	Group to which the user will belong
                    	**type**\: list of  		 :py:class:`UserGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup>`
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.UserGroups, self).__init__()

                        self.yang_name = "user-groups"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("user-group", ("user_group", Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup))])
                        self._leafs = OrderedDict()

                        self.user_group = YList(self)
                        self._segment_path = lambda: "user-groups"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.UserGroups, [], name, value)


                    class UserGroup(Entity):
                        """
                        Group to which the user will belong
                        
                        .. attribute:: name  (key)
                        
                        	Name of the group
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: category
                        
                        	Specify as 'root\-system' for root\-system group and 'other' for remaining groups
                        	**type**\: str
                        
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
                            self.ylist_key_names = ['name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('category', (YLeaf(YType.str, 'category'), ['str'])),
                            ])
                            self.name = None
                            self.category = None
                            self._segment_path = lambda: "user-group" + "[name='" + str(self.name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup, ['name', 'category'], name, value)


                class Authorization(Entity):
                    """
                    Authorization parameters
                    
                    .. attribute:: exec_
                    
                    	For starting an exec (shell)
                    	**type**\: str
                    
                    .. attribute:: event_manager
                    
                    	Specify 'default' or use an authorization list with this name
                    	**type**\: str
                    
                    .. attribute:: commands
                    
                    	For exec (shell) configuration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.Authorization, self).__init__()

                        self.yang_name = "authorization"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('exec_', (YLeaf(YType.str, 'exec'), ['str'])),
                            ('event_manager', (YLeaf(YType.str, 'event-manager'), ['str'])),
                            ('commands', (YLeaf(YType.str, 'commands'), ['str'])),
                        ])
                        self.exec_ = None
                        self.event_manager = None
                        self.commands = None
                        self._segment_path = lambda: "authorization"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.Authorization, ['exec_', 'event_manager', 'commands'], name, value)


                class Authentication(Entity):
                    """
                    Authentication parameters
                    
                    .. attribute:: login
                    
                    	Authentication list name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.Authentication, self).__init__()

                        self.yang_name = "authentication"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('login', (YLeaf(YType.str, 'login'), ['str'])),
                        ])
                        self.login = None
                        self._segment_path = lambda: "authentication"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.Authentication, ['login'], name, value)


                class Accounting(Entity):
                    """
                    Accounting parameters
                    
                    .. attribute:: exec_
                    
                    	For starting an exec (shell)
                    	**type**\: str
                    
                    .. attribute:: commands
                    
                    	For exec (shell) configuration
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Aaa.Accounting, self).__init__()

                        self.yang_name = "accounting"
                        self.yang_parent_name = "aaa"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('exec_', (YLeaf(YType.str, 'exec'), ['str'])),
                            ('commands', (YLeaf(YType.str, 'commands'), ['str'])),
                        ])
                        self.exec_ = None
                        self.commands = None
                        self._segment_path = lambda: "accounting"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Aaa.Accounting, ['exec_', 'commands'], name, value)


            class Exec(Entity):
                """
                EXEC timeout and timestamp configurtion
                
                .. attribute:: timeout
                
                	EXEC Timeout
                	**type**\:  :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Exec.Timeout>`
                
                	**presence node**\: True
                
                .. attribute:: time_stamp
                
                	'True' to Enable & 'False' to Disable time stamp
                	**type**\: bool
                
                

                """

                _prefix = 'tty-server-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Exec, self).__init__()

                    self.yang_name = "exec"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("timeout", ("timeout", Tty.TtyLines.TtyLine.Exec.Timeout))])
                    self._leafs = OrderedDict([
                        ('time_stamp', (YLeaf(YType.boolean, 'time-stamp'), ['bool'])),
                    ])
                    self.time_stamp = None

                    self.timeout = None
                    self._children_name_map["timeout"] = "timeout"
                    self._segment_path = lambda: "exec"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Exec, ['time_stamp'], name, value)


                class Timeout(Entity):
                    """
                    EXEC Timeout
                    
                    .. attribute:: minutes
                    
                    	Timeout in minutes
                    	**type**\: int
                    
                    	**range:** 0..35791
                    
                    	**mandatory**\: True
                    
                    	**units**\: minute
                    
                    .. attribute:: seconds
                    
                    	Timeout in seconds
                    	**type**\: int
                    
                    	**range:** 0..2147483
                    
                    	**mandatory**\: True
                    
                    	**units**\: second
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-server-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Exec.Timeout, self).__init__()

                        self.yang_name = "timeout"
                        self.yang_parent_name = "exec"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('minutes', (YLeaf(YType.uint32, 'minutes'), ['int'])),
                            ('seconds', (YLeaf(YType.uint32, 'seconds'), ['int'])),
                        ])
                        self.minutes = None
                        self.seconds = None
                        self._segment_path = lambda: "timeout"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Exec.Timeout, ['minutes', 'seconds'], name, value)


            class Connection(Entity):
                """
                Management connection configuration
                
                .. attribute:: transport_input
                
                	Protocols to use when connecting to the terminal server
                	**type**\:  :py:class:`TransportInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.TransportInput>`
                
                .. attribute:: transport_output
                
                	Protocols to use for outgoing connections
                	**type**\:  :py:class:`TransportOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.TransportOutput>`
                
                	**presence node**\: True
                
                .. attribute:: session_timeout
                
                	Interval for closing connection when there is no input traffic
                	**type**\:  :py:class:`SessionTimeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg.Tty.TtyLines.TtyLine.Connection.SessionTimeout>`
                
                	**presence node**\: True
                
                .. attribute:: disconnect_character
                
                	Disconnect character's decimal equivalent value or Character 
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (\\p{IsBasicLatin}\|\\p{IsLatin\-1Supplement})\*
                
                		**type**\: int
                
                			**range:** 0..255
                
                .. attribute:: acl_in
                
                	ACL to filter ingoing connections
                	**type**\: str
                
                .. attribute:: acl_out
                
                	ACL to filter outgoing connections
                	**type**\: str
                
                .. attribute:: cli_white_space_completion
                
                	Command completion on whitespace
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: session_limit
                
                	The number of outgoing connections
                	**type**\: int
                
                	**range:** 0..20
                
                	**default value**\: 6
                
                .. attribute:: escape_character
                
                	Escape character or ASCII decimal equivalent value orspecial strings NONE,DEFAULT,BREAK
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (\\p{IsBasicLatin}\|\\p{IsLatin\-1Supplement})\|(DEFAULT)\|(BREAK)\|(NONE)
                
                		**type**\: int
                
                			**range:** 0..255
                
                	**default value**\: 30
                
                .. attribute:: transport_preferred
                
                	The preferred protocol to use
                	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                
                

                """

                _prefix = 'tty-management-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.Connection, self).__init__()

                    self.yang_name = "connection"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("transport-input", ("transport_input", Tty.TtyLines.TtyLine.Connection.TransportInput)), ("transport-output", ("transport_output", Tty.TtyLines.TtyLine.Connection.TransportOutput)), ("session-timeout", ("session_timeout", Tty.TtyLines.TtyLine.Connection.SessionTimeout))])
                    self._leafs = OrderedDict([
                        ('disconnect_character', (YLeaf(YType.str, 'disconnect-character'), ['str','int'])),
                        ('acl_in', (YLeaf(YType.str, 'acl-in'), ['str'])),
                        ('acl_out', (YLeaf(YType.str, 'acl-out'), ['str'])),
                        ('cli_white_space_completion', (YLeaf(YType.empty, 'cli-white-space-completion'), ['Empty'])),
                        ('session_limit', (YLeaf(YType.uint32, 'session-limit'), ['int'])),
                        ('escape_character', (YLeaf(YType.str, 'escape-character'), ['str','int'])),
                        ('transport_preferred', (YLeaf(YType.enumeration, 'transport-preferred'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                    ])
                    self.disconnect_character = None
                    self.acl_in = None
                    self.acl_out = None
                    self.cli_white_space_completion = None
                    self.session_limit = None
                    self.escape_character = None
                    self.transport_preferred = None

                    self.transport_input = Tty.TtyLines.TtyLine.Connection.TransportInput()
                    self.transport_input.parent = self
                    self._children_name_map["transport_input"] = "transport-input"

                    self.transport_output = None
                    self._children_name_map["transport_output"] = "transport-output"

                    self.session_timeout = None
                    self._children_name_map["session_timeout"] = "session-timeout"
                    self._segment_path = lambda: "Cisco-IOS-XR-tty-management-cfg:connection"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.Connection, ['disconnect_character', 'acl_in', 'acl_out', 'cli_white_space_completion', 'session_limit', 'escape_character', 'transport_preferred'], name, value)


                class TransportInput(Entity):
                    """
                    Protocols to use when connecting to the
                    terminal server
                    
                    .. attribute:: select
                    
                    	Choose transport protocols
                    	**type**\:  :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                    
                    	**default value**\: all
                    
                    .. attribute:: protocol1
                    
                    	Transport protocol1
                    	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: protocol2
                    
                    	Transport protocol2
                    	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: none
                    
                    	Not used
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Connection.TransportInput, self).__init__()

                        self.yang_name = "transport-input"
                        self.yang_parent_name = "connection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('select', (YLeaf(YType.enumeration, 'select'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect', '')])),
                            ('protocol1', (YLeaf(YType.enumeration, 'protocol1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                            ('protocol2', (YLeaf(YType.enumeration, 'protocol2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                            ('none', (YLeaf(YType.uint32, 'none'), ['int'])),
                        ])
                        self.select = None
                        self.protocol1 = None
                        self.protocol2 = None
                        self.none = None
                        self._segment_path = lambda: "transport-input"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Connection.TransportInput, ['select', 'protocol1', 'protocol2', 'none'], name, value)


                class TransportOutput(Entity):
                    """
                    Protocols to use for outgoing connections
                    
                    .. attribute:: select
                    
                    	Choose transport protocols
                    	**type**\:  :py:class:`TtyTransportProtocolSelect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocolSelect>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: protocol1
                    
                    	Transport protocol1
                    	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: protocol2
                    
                    	Transport protocol2
                    	**type**\:  :py:class:`TtyTransportProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyTransportProtocol>`
                    
                    .. attribute:: none
                    
                    	Not used
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Connection.TransportOutput, self).__init__()

                        self.yang_name = "transport-output"
                        self.yang_parent_name = "connection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('select', (YLeaf(YType.enumeration, 'select'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelect', '')])),
                            ('protocol1', (YLeaf(YType.enumeration, 'protocol1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                            ('protocol2', (YLeaf(YType.enumeration, 'protocol2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocol', '')])),
                            ('none', (YLeaf(YType.uint32, 'none'), ['int'])),
                        ])
                        self.select = None
                        self.protocol1 = None
                        self.protocol2 = None
                        self.none = None
                        self._segment_path = lambda: "transport-output"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Connection.TransportOutput, ['select', 'protocol1', 'protocol2', 'none'], name, value)


                class SessionTimeout(Entity):
                    """
                    Interval for closing connection when there is
                    no input traffic
                    
                    .. attribute:: timeout
                    
                    	Session timeout interval in minutes
                    	**type**\: int
                    
                    	**range:** 0..35791
                    
                    	**mandatory**\: True
                    
                    .. attribute:: direction
                    
                    	Include output traffic as well as input traffic
                    	**type**\:  :py:class:`TtySessionTimeoutDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtySessionTimeoutDirection>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'tty-management-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(Tty.TtyLines.TtyLine.Connection.SessionTimeout, self).__init__()

                        self.yang_name = "session-timeout"
                        self.yang_parent_name = "connection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtySessionTimeoutDirection', '')])),
                        ])
                        self.timeout = None
                        self.direction = None
                        self._segment_path = lambda: "session-timeout"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tty.TtyLines.TtyLine.Connection.SessionTimeout, ['timeout', 'direction'], name, value)


            class ExecMode(Entity):
                """
                Exec Mode Pager  configurtion
                
                .. attribute:: pager
                
                	Preferred Paging Utility
                	**type**\:  :py:class:`TtyPager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes.TtyPager>`
                
                	**default value**\: more
                
                

                """

                _prefix = 'tty-management-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Tty.TtyLines.TtyLine.ExecMode, self).__init__()

                    self.yang_name = "exec-mode"
                    self.yang_parent_name = "tty-line"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('pager', (YLeaf(YType.enumeration, 'pager'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyPager', '')])),
                    ])
                    self.pager = None
                    self._segment_path = lambda: "Cisco-IOS-XR-tty-management-cfg:exec-mode"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Tty.TtyLines.TtyLine.ExecMode, ['pager'], name, value)

    def clone_ptr(self):
        self._top_entity = Tty()
        return self._top_entity

