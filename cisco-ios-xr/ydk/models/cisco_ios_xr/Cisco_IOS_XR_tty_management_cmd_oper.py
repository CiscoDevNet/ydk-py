""" Cisco_IOS_XR_tty_management_cmd_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-management\-cmd package operational data.

This module contains definitions
for the following management objects\:
  show\-users\: Show users statistics

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ShowUsers(Entity):
    """
    Show users statistics
    
    .. attribute:: sessions
    
    	Show users statistics
    	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions>`
    
    

    """

    _prefix = 'tty-management-cmd-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ShowUsers, self).__init__()
        self._top_entity = None

        self.yang_name = "show-users"
        self.yang_parent_name = "Cisco-IOS-XR-tty-management-cmd-oper"

        self.sessions = ShowUsers.Sessions()
        self.sessions.parent = self
        self._children_name_map["sessions"] = "sessions"
        self._children_yang_names.add("sessions")


    class Sessions(Entity):
        """
        Show users statistics
        
        .. attribute:: session
        
        	Show users statistics
        	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_cmd_oper.ShowUsers.Sessions.Session>`
        
        

        """

        _prefix = 'tty-management-cmd-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ShowUsers.Sessions, self).__init__()

            self.yang_name = "sessions"
            self.yang_parent_name = "show-users"

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
                        super(ShowUsers.Sessions, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ShowUsers.Sessions, self).__setattr__(name, value)


        class Session(Entity):
            """
            Show users statistics
            
            .. attribute:: session_id  <key>
            
            	Session Id
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: conns
            
            	No. of Connections
            	**type**\:  str
            
            .. attribute:: idle_string
            
            	Idle Time
            	**type**\:  str
            
            .. attribute:: line
            
            	Line Number
            	**type**\:  str
            
            .. attribute:: location
            
            	location
            	**type**\:  str
            
            .. attribute:: service
            
            	Service Name
            	**type**\:  str
            
            .. attribute:: user
            
            	User Name
            	**type**\:  str
            
            

            """

            _prefix = 'tty-management-cmd-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ShowUsers.Sessions.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "sessions"

                self.session_id = YLeaf(YType.int32, "session-id")

                self.conns = YLeaf(YType.str, "conns")

                self.idle_string = YLeaf(YType.str, "idle-string")

                self.line = YLeaf(YType.str, "line")

                self.location = YLeaf(YType.str, "location")

                self.service = YLeaf(YType.str, "service")

                self.user = YLeaf(YType.str, "user")

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
                                "conns",
                                "idle_string",
                                "line",
                                "location",
                                "service",
                                "user") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ShowUsers.Sessions.Session, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ShowUsers.Sessions.Session, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.session_id.is_set or
                    self.conns.is_set or
                    self.idle_string.is_set or
                    self.line.is_set or
                    self.location.is_set or
                    self.service.is_set or
                    self.user.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.session_id.yfilter != YFilter.not_set or
                    self.conns.yfilter != YFilter.not_set or
                    self.idle_string.yfilter != YFilter.not_set or
                    self.line.yfilter != YFilter.not_set or
                    self.location.yfilter != YFilter.not_set or
                    self.service.yfilter != YFilter.not_set or
                    self.user.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tty-management-cmd-oper:show-users/sessions/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_id.get_name_leafdata())
                if (self.conns.is_set or self.conns.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.conns.get_name_leafdata())
                if (self.idle_string.is_set or self.idle_string.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.idle_string.get_name_leafdata())
                if (self.line.is_set or self.line.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.line.get_name_leafdata())
                if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.location.get_name_leafdata())
                if (self.service.is_set or self.service.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.service.get_name_leafdata())
                if (self.user.is_set or self.user.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.user.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "session-id" or name == "conns" or name == "idle-string" or name == "line" or name == "location" or name == "service" or name == "user"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "session-id"):
                    self.session_id = value
                    self.session_id.value_namespace = name_space
                    self.session_id.value_namespace_prefix = name_space_prefix
                if(value_path == "conns"):
                    self.conns = value
                    self.conns.value_namespace = name_space
                    self.conns.value_namespace_prefix = name_space_prefix
                if(value_path == "idle-string"):
                    self.idle_string = value
                    self.idle_string.value_namespace = name_space
                    self.idle_string.value_namespace_prefix = name_space_prefix
                if(value_path == "line"):
                    self.line = value
                    self.line.value_namespace = name_space
                    self.line.value_namespace_prefix = name_space_prefix
                if(value_path == "location"):
                    self.location = value
                    self.location.value_namespace = name_space
                    self.location.value_namespace_prefix = name_space_prefix
                if(value_path == "service"):
                    self.service = value
                    self.service.value_namespace = name_space
                    self.service.value_namespace_prefix = name_space_prefix
                if(value_path == "user"):
                    self.user = value
                    self.user.value_namespace = name_space
                    self.user.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-tty-management-cmd-oper:show-users/%s" % self.get_segment_path()
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
                c = ShowUsers.Sessions.Session()
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
        path_buffer = "Cisco-IOS-XR-tty-management-cmd-oper:show-users" + path_buffer

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

        if (child_yang_name == "sessions"):
            if (self.sessions is None):
                self.sessions = ShowUsers.Sessions()
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

    def clone_ptr(self):
        self._top_entity = ShowUsers()
        return self._top_entity

