""" Cisco_IOS_XR_tty_server_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-server package configuration.

This module contains definitions
for the following management objects\:
  tty\: TTY Line Configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.tty_lines = Tty.TtyLines()
        self.tty_lines.parent = self
        self._children_name_map["tty_lines"] = "tty-lines"
        self._children_yang_names.add("tty-lines")


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

            self.tty_line = YList(self)

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
                        super(Tty.TtyLines, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Tty.TtyLines, self).__setattr__(name, value)


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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Tty.TtyLines.TtyLine, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Tty.TtyLines.TtyLine, self).__setattr__(name, value)


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

                    self.absolute_timeout = YLeaf(YType.uint32, "absolute-timeout")

                    self.length = YLeaf(YType.uint32, "length")

                    self.width = YLeaf(YType.uint32, "width")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("absolute_timeout",
                                    "length",
                                    "width") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Tty.TtyLines.TtyLine.General, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tty.TtyLines.TtyLine.General, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.absolute_timeout.is_set or
                        self.length.is_set or
                        self.width.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.absolute_timeout.yfilter != YFilter.not_set or
                        self.length.yfilter != YFilter.not_set or
                        self.width.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "general" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.absolute_timeout.is_set or self.absolute_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.absolute_timeout.get_name_leafdata())
                    if (self.length.is_set or self.length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.length.get_name_leafdata())
                    if (self.width.is_set or self.width.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.width.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "absolute-timeout" or name == "length" or name == "width"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "absolute-timeout"):
                        self.absolute_timeout = value
                        self.absolute_timeout.value_namespace = name_space
                        self.absolute_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "length"):
                        self.length = value
                        self.length.value_namespace = name_space
                        self.length.value_namespace_prefix = name_space_prefix
                    if(value_path == "width"):
                        self.width = value
                        self.width.value_namespace = name_space
                        self.width.value_namespace_prefix = name_space_prefix


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

                    self.transparent = YLeaf(YType.empty, "transparent")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("transparent") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Tty.TtyLines.TtyLine.Telnet, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tty.TtyLines.TtyLine.Telnet, self).__setattr__(name, value)

                def has_data(self):
                    return self.transparent.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.transparent.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "telnet" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.transparent.is_set or self.transparent.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transparent.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "transparent"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "transparent"):
                        self.transparent = value
                        self.transparent.value_namespace = name_space
                        self.transparent.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("login_timeout",
                                    "password",
                                    "secret") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Tty.TtyLines.TtyLine.Aaa, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tty.TtyLines.TtyLine.Aaa, self).__setattr__(name, value)


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

                        self.user_group = YList(self)

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
                                    super(Tty.TtyLines.TtyLine.Aaa.UserGroups, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Aaa.UserGroups, self).__setattr__(name, value)


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

                            self.name = YLeaf(YType.str, "name")

                            self.category = YLeaf(YType.str, "category")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("name",
                                            "category") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.name.is_set or
                                self.category.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.name.yfilter != YFilter.not_set or
                                self.category.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "user-group" + "[name='" + self.name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.name.get_name_leafdata())
                            if (self.category.is_set or self.category.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.category.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "name" or name == "category"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "name"):
                                self.name = value
                                self.name.value_namespace = name_space
                                self.name.value_namespace_prefix = name_space_prefix
                            if(value_path == "category"):
                                self.category = value
                                self.category.value_namespace = name_space
                                self.category.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.user_group:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.user_group:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "user-groups" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "user-group"):
                            for c in self.user_group:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.user_group.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "user-group"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.commands = YLeaf(YType.str, "commands")

                        self.event_manager = YLeaf(YType.str, "event-manager")

                        self.exec_ = YLeaf(YType.str, "exec")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("commands",
                                        "event_manager",
                                        "exec_") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.TtyLines.TtyLine.Aaa.Authorization, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Aaa.Authorization, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.commands.is_set or
                            self.event_manager.is_set or
                            self.exec_.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.commands.yfilter != YFilter.not_set or
                            self.event_manager.yfilter != YFilter.not_set or
                            self.exec_.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "authorization" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.commands.is_set or self.commands.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.commands.get_name_leafdata())
                        if (self.event_manager.is_set or self.event_manager.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.event_manager.get_name_leafdata())
                        if (self.exec_.is_set or self.exec_.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exec_.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "commands" or name == "event-manager" or name == "exec"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "commands"):
                            self.commands = value
                            self.commands.value_namespace = name_space
                            self.commands.value_namespace_prefix = name_space_prefix
                        if(value_path == "event-manager"):
                            self.event_manager = value
                            self.event_manager.value_namespace = name_space
                            self.event_manager.value_namespace_prefix = name_space_prefix
                        if(value_path == "exec"):
                            self.exec_ = value
                            self.exec_.value_namespace = name_space
                            self.exec_.value_namespace_prefix = name_space_prefix


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

                        self.login = YLeaf(YType.str, "login")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("login") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.TtyLines.TtyLine.Aaa.Authentication, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Aaa.Authentication, self).__setattr__(name, value)

                    def has_data(self):
                        return self.login.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.login.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "authentication" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.login.is_set or self.login.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.login.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "login"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "login"):
                            self.login = value
                            self.login.value_namespace = name_space
                            self.login.value_namespace_prefix = name_space_prefix


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

                        self.commands = YLeaf(YType.str, "commands")

                        self.exec_ = YLeaf(YType.str, "exec")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("commands",
                                        "exec_") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.TtyLines.TtyLine.Aaa.Accounting, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Aaa.Accounting, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.commands.is_set or
                            self.exec_.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.commands.yfilter != YFilter.not_set or
                            self.exec_.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "accounting" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.commands.is_set or self.commands.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.commands.get_name_leafdata())
                        if (self.exec_.is_set or self.exec_.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.exec_.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "commands" or name == "exec"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "commands"):
                            self.commands = value
                            self.commands.value_namespace = name_space
                            self.commands.value_namespace_prefix = name_space_prefix
                        if(value_path == "exec"):
                            self.exec_ = value
                            self.exec_.value_namespace = name_space
                            self.exec_.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.login_timeout.is_set or
                        self.password.is_set or
                        self.secret.is_set or
                        (self.accounting is not None and self.accounting.has_data()) or
                        (self.authentication is not None and self.authentication.has_data()) or
                        (self.authorization is not None and self.authorization.has_data()) or
                        (self.user_groups is not None and self.user_groups.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.login_timeout.yfilter != YFilter.not_set or
                        self.password.yfilter != YFilter.not_set or
                        self.secret.yfilter != YFilter.not_set or
                        (self.accounting is not None and self.accounting.has_operation()) or
                        (self.authentication is not None and self.authentication.has_operation()) or
                        (self.authorization is not None and self.authorization.has_operation()) or
                        (self.user_groups is not None and self.user_groups.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "aaa" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.login_timeout.is_set or self.login_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.login_timeout.get_name_leafdata())
                    if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.password.get_name_leafdata())
                    if (self.secret.is_set or self.secret.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.secret.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "accounting"):
                        if (self.accounting is None):
                            self.accounting = Tty.TtyLines.TtyLine.Aaa.Accounting()
                            self.accounting.parent = self
                            self._children_name_map["accounting"] = "accounting"
                        return self.accounting

                    if (child_yang_name == "authentication"):
                        if (self.authentication is None):
                            self.authentication = Tty.TtyLines.TtyLine.Aaa.Authentication()
                            self.authentication.parent = self
                            self._children_name_map["authentication"] = "authentication"
                        return self.authentication

                    if (child_yang_name == "authorization"):
                        if (self.authorization is None):
                            self.authorization = Tty.TtyLines.TtyLine.Aaa.Authorization()
                            self.authorization.parent = self
                            self._children_name_map["authorization"] = "authorization"
                        return self.authorization

                    if (child_yang_name == "user-groups"):
                        if (self.user_groups is None):
                            self.user_groups = Tty.TtyLines.TtyLine.Aaa.UserGroups()
                            self.user_groups.parent = self
                            self._children_name_map["user_groups"] = "user-groups"
                        return self.user_groups

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "accounting" or name == "authentication" or name == "authorization" or name == "user-groups" or name == "login-timeout" or name == "password" or name == "secret"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "login-timeout"):
                        self.login_timeout = value
                        self.login_timeout.value_namespace = name_space
                        self.login_timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "password"):
                        self.password = value
                        self.password.value_namespace = name_space
                        self.password.value_namespace_prefix = name_space_prefix
                    if(value_path == "secret"):
                        self.secret = value
                        self.secret.value_namespace = name_space
                        self.secret.value_namespace_prefix = name_space_prefix


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

                    self.time_stamp = YLeaf(YType.boolean, "time-stamp")

                    self.timeout = None
                    self._children_name_map["timeout"] = "timeout"
                    self._children_yang_names.add("timeout")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("time_stamp") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Tty.TtyLines.TtyLine.Exec_, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tty.TtyLines.TtyLine.Exec_, self).__setattr__(name, value)


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
                        self.is_presence_container = True

                        self.minutes = YLeaf(YType.uint32, "minutes")

                        self.seconds = YLeaf(YType.uint32, "seconds")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("minutes",
                                        "seconds") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.TtyLines.TtyLine.Exec_.Timeout, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Exec_.Timeout, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.minutes.is_set or
                            self.seconds.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.minutes.yfilter != YFilter.not_set or
                            self.seconds.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "timeout" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.minutes.is_set or self.minutes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.minutes.get_name_leafdata())
                        if (self.seconds.is_set or self.seconds.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.seconds.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "minutes" or name == "seconds"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "minutes"):
                            self.minutes = value
                            self.minutes.value_namespace = name_space
                            self.minutes.value_namespace_prefix = name_space_prefix
                        if(value_path == "seconds"):
                            self.seconds = value
                            self.seconds.value_namespace = name_space
                            self.seconds.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.time_stamp.is_set or
                        (self.timeout is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.time_stamp.yfilter != YFilter.not_set or
                        (self.timeout is not None and self.timeout.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "exec" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.time_stamp.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "timeout"):
                        if (self.timeout is None):
                            self.timeout = Tty.TtyLines.TtyLine.Exec_.Timeout()
                            self.timeout.parent = self
                            self._children_name_map["timeout"] = "timeout"
                        return self.timeout

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "timeout" or name == "time-stamp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "time-stamp"):
                        self.time_stamp = value
                        self.time_stamp.value_namespace = name_space
                        self.time_stamp.value_namespace_prefix = name_space_prefix


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("acl_in",
                                    "acl_out",
                                    "cli_white_space_completion",
                                    "disconnect_character",
                                    "escape_character",
                                    "session_limit",
                                    "transport_preferred") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Tty.TtyLines.TtyLine.Connection, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tty.TtyLines.TtyLine.Connection, self).__setattr__(name, value)


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

                        self.none = YLeaf(YType.int32, "none")

                        self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                        self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                        self.select = YLeaf(YType.enumeration, "select")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("none",
                                        "protocol1",
                                        "protocol2",
                                        "select") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.TtyLines.TtyLine.Connection.TransportInput, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Connection.TransportInput, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.none.is_set or
                            self.protocol1.is_set or
                            self.protocol2.is_set or
                            self.select.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.none.yfilter != YFilter.not_set or
                            self.protocol1.yfilter != YFilter.not_set or
                            self.protocol2.yfilter != YFilter.not_set or
                            self.select.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "transport-input" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.none.is_set or self.none.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.none.get_name_leafdata())
                        if (self.protocol1.is_set or self.protocol1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol1.get_name_leafdata())
                        if (self.protocol2.is_set or self.protocol2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol2.get_name_leafdata())
                        if (self.select.is_set or self.select.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.select.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "none" or name == "protocol1" or name == "protocol2" or name == "select"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "none"):
                            self.none = value
                            self.none.value_namespace = name_space
                            self.none.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol1"):
                            self.protocol1 = value
                            self.protocol1.value_namespace = name_space
                            self.protocol1.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol2"):
                            self.protocol2 = value
                            self.protocol2.value_namespace = name_space
                            self.protocol2.value_namespace_prefix = name_space_prefix
                        if(value_path == "select"):
                            self.select = value
                            self.select.value_namespace = name_space
                            self.select.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.none = YLeaf(YType.int32, "none")

                        self.protocol1 = YLeaf(YType.enumeration, "protocol1")

                        self.protocol2 = YLeaf(YType.enumeration, "protocol2")

                        self.select = YLeaf(YType.enumeration, "select")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("none",
                                        "protocol1",
                                        "protocol2",
                                        "select") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.TtyLines.TtyLine.Connection.TransportOutput, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Connection.TransportOutput, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.none.is_set or
                            self.protocol1.is_set or
                            self.protocol2.is_set or
                            self.select.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.none.yfilter != YFilter.not_set or
                            self.protocol1.yfilter != YFilter.not_set or
                            self.protocol2.yfilter != YFilter.not_set or
                            self.select.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "transport-output" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.none.is_set or self.none.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.none.get_name_leafdata())
                        if (self.protocol1.is_set or self.protocol1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol1.get_name_leafdata())
                        if (self.protocol2.is_set or self.protocol2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protocol2.get_name_leafdata())
                        if (self.select.is_set or self.select.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.select.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "none" or name == "protocol1" or name == "protocol2" or name == "select"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "none"):
                            self.none = value
                            self.none.value_namespace = name_space
                            self.none.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol1"):
                            self.protocol1 = value
                            self.protocol1.value_namespace = name_space
                            self.protocol1.value_namespace_prefix = name_space_prefix
                        if(value_path == "protocol2"):
                            self.protocol2 = value
                            self.protocol2.value_namespace = name_space
                            self.protocol2.value_namespace_prefix = name_space_prefix
                        if(value_path == "select"):
                            self.select = value
                            self.select.value_namespace = name_space
                            self.select.value_namespace_prefix = name_space_prefix


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
                        self.is_presence_container = True

                        self.direction = YLeaf(YType.enumeration, "direction")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("direction",
                                        "timeout") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Tty.TtyLines.TtyLine.Connection.SessionTimeout, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Tty.TtyLines.TtyLine.Connection.SessionTimeout, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.direction.is_set or
                            self.timeout.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.direction.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session-timeout" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.direction.is_set or self.direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.direction.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "direction" or name == "timeout"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "direction"):
                            self.direction = value
                            self.direction.value_namespace = name_space
                            self.direction.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.acl_in.is_set or
                        self.acl_out.is_set or
                        self.cli_white_space_completion.is_set or
                        self.disconnect_character.is_set or
                        self.escape_character.is_set or
                        self.session_limit.is_set or
                        self.transport_preferred.is_set or
                        (self.transport_input is not None and self.transport_input.has_data()) or
                        (self.session_timeout is not None) or
                        (self.transport_output is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.acl_in.yfilter != YFilter.not_set or
                        self.acl_out.yfilter != YFilter.not_set or
                        self.cli_white_space_completion.yfilter != YFilter.not_set or
                        self.disconnect_character.yfilter != YFilter.not_set or
                        self.escape_character.yfilter != YFilter.not_set or
                        self.session_limit.yfilter != YFilter.not_set or
                        self.transport_preferred.yfilter != YFilter.not_set or
                        (self.session_timeout is not None and self.session_timeout.has_operation()) or
                        (self.transport_input is not None and self.transport_input.has_operation()) or
                        (self.transport_output is not None and self.transport_output.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-tty-management-cfg:connection" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.acl_in.is_set or self.acl_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acl_in.get_name_leafdata())
                    if (self.acl_out.is_set or self.acl_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acl_out.get_name_leafdata())
                    if (self.cli_white_space_completion.is_set or self.cli_white_space_completion.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cli_white_space_completion.get_name_leafdata())
                    if (self.disconnect_character.is_set or self.disconnect_character.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disconnect_character.get_name_leafdata())
                    if (self.escape_character.is_set or self.escape_character.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.escape_character.get_name_leafdata())
                    if (self.session_limit.is_set or self.session_limit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_limit.get_name_leafdata())
                    if (self.transport_preferred.is_set or self.transport_preferred.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transport_preferred.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "session-timeout"):
                        if (self.session_timeout is None):
                            self.session_timeout = Tty.TtyLines.TtyLine.Connection.SessionTimeout()
                            self.session_timeout.parent = self
                            self._children_name_map["session_timeout"] = "session-timeout"
                        return self.session_timeout

                    if (child_yang_name == "transport-input"):
                        if (self.transport_input is None):
                            self.transport_input = Tty.TtyLines.TtyLine.Connection.TransportInput()
                            self.transport_input.parent = self
                            self._children_name_map["transport_input"] = "transport-input"
                        return self.transport_input

                    if (child_yang_name == "transport-output"):
                        if (self.transport_output is None):
                            self.transport_output = Tty.TtyLines.TtyLine.Connection.TransportOutput()
                            self.transport_output.parent = self
                            self._children_name_map["transport_output"] = "transport-output"
                        return self.transport_output

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-timeout" or name == "transport-input" or name == "transport-output" or name == "acl-in" or name == "acl-out" or name == "cli-white-space-completion" or name == "disconnect-character" or name == "escape-character" or name == "session-limit" or name == "transport-preferred"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "acl-in"):
                        self.acl_in = value
                        self.acl_in.value_namespace = name_space
                        self.acl_in.value_namespace_prefix = name_space_prefix
                    if(value_path == "acl-out"):
                        self.acl_out = value
                        self.acl_out.value_namespace = name_space
                        self.acl_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "cli-white-space-completion"):
                        self.cli_white_space_completion = value
                        self.cli_white_space_completion.value_namespace = name_space
                        self.cli_white_space_completion.value_namespace_prefix = name_space_prefix
                    if(value_path == "disconnect-character"):
                        self.disconnect_character = value
                        self.disconnect_character.value_namespace = name_space
                        self.disconnect_character.value_namespace_prefix = name_space_prefix
                    if(value_path == "escape-character"):
                        self.escape_character = value
                        self.escape_character.value_namespace = name_space
                        self.escape_character.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-limit"):
                        self.session_limit = value
                        self.session_limit.value_namespace = name_space
                        self.session_limit.value_namespace_prefix = name_space_prefix
                    if(value_path == "transport-preferred"):
                        self.transport_preferred = value
                        self.transport_preferred.value_namespace = name_space
                        self.transport_preferred.value_namespace_prefix = name_space_prefix


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

                    self.pager = YLeaf(YType.enumeration, "pager")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("pager") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Tty.TtyLines.TtyLine.ExecMode, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Tty.TtyLines.TtyLine.ExecMode, self).__setattr__(name, value)

                def has_data(self):
                    return self.pager.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.pager.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "Cisco-IOS-XR-tty-management-cfg:exec-mode" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.pager.is_set or self.pager.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pager.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pager"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "pager"):
                        self.pager = value
                        self.pager.value_namespace = name_space
                        self.pager.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.name.is_set or
                    (self.aaa is not None and self.aaa.has_data()) or
                    (self.connection is not None and self.connection.has_data()) or
                    (self.exec_ is not None and self.exec_.has_data()) or
                    (self.exec_mode is not None and self.exec_mode.has_data()) or
                    (self.general is not None and self.general.has_data()) or
                    (self.telnet is not None and self.telnet.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    (self.aaa is not None and self.aaa.has_operation()) or
                    (self.connection is not None and self.connection.has_operation()) or
                    (self.exec_ is not None and self.exec_.has_operation()) or
                    (self.exec_mode is not None and self.exec_mode.has_operation()) or
                    (self.general is not None and self.general.has_operation()) or
                    (self.telnet is not None and self.telnet.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tty-line" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tty-server-cfg:tty/tty-lines/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "aaa"):
                    if (self.aaa is None):
                        self.aaa = Tty.TtyLines.TtyLine.Aaa()
                        self.aaa.parent = self
                        self._children_name_map["aaa"] = "aaa"
                    return self.aaa

                if (child_yang_name == "connection"):
                    if (self.connection is None):
                        self.connection = Tty.TtyLines.TtyLine.Connection()
                        self.connection.parent = self
                        self._children_name_map["connection"] = "connection"
                    return self.connection

                if (child_yang_name == "exec"):
                    if (self.exec_ is None):
                        self.exec_ = Tty.TtyLines.TtyLine.Exec_()
                        self.exec_.parent = self
                        self._children_name_map["exec_"] = "exec"
                    return self.exec_

                if (child_yang_name == "exec-mode"):
                    if (self.exec_mode is None):
                        self.exec_mode = Tty.TtyLines.TtyLine.ExecMode()
                        self.exec_mode.parent = self
                        self._children_name_map["exec_mode"] = "exec-mode"
                    return self.exec_mode

                if (child_yang_name == "general"):
                    if (self.general is None):
                        self.general = Tty.TtyLines.TtyLine.General()
                        self.general.parent = self
                        self._children_name_map["general"] = "general"
                    return self.general

                if (child_yang_name == "telnet"):
                    if (self.telnet is None):
                        self.telnet = Tty.TtyLines.TtyLine.Telnet()
                        self.telnet.parent = self
                        self._children_name_map["telnet"] = "telnet"
                    return self.telnet

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "aaa" or name == "connection" or name == "exec" or name == "exec-mode" or name == "general" or name == "telnet" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.tty_line:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.tty_line:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "tty-lines" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tty-server-cfg:tty/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "tty-line"):
                for c in self.tty_line:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Tty.TtyLines.TtyLine()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.tty_line.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "tty-line"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.tty_lines is not None and self.tty_lines.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.tty_lines is not None and self.tty_lines.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-tty-server-cfg:tty" + path_buffer

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

        if (child_yang_name == "tty-lines"):
            if (self.tty_lines is None):
                self.tty_lines = Tty.TtyLines()
                self.tty_lines.parent = self
                self._children_name_map["tty_lines"] = "tty-lines"
            return self.tty_lines

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "tty-lines"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Tty()
        return self._top_entity

