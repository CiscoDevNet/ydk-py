""" Cisco_IOS_XR_man_netconf_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-netconf package configuration.

This module contains definitions
for the following management objects\:
  netconf\-yang\: NETCONF YANG configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NetconfYang(Entity):
    """
    NETCONF YANG configuration commands
    
    .. attribute:: agent
    
    	NETCONF YANG agent configuration commands
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent>`
    
    

    """

    _prefix = 'man-netconf-cfg'
    _revision = '2016-03-15'

    def __init__(self):
        super(NetconfYang, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf-yang"
        self.yang_parent_name = "Cisco-IOS-XR-man-netconf-cfg"

        self.agent = NetconfYang.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")


    class Agent(Entity):
        """
        NETCONF YANG agent configuration commands
        
        .. attribute:: rate_limit
        
        	Number of bytes to process per sec
        	**type**\:  int
        
        	**range:** 4096..4294967295
        
        	**units**\: byte
        
        .. attribute:: session
        
        	Session settings
        	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Session>`
        
        .. attribute:: ssh
        
        	NETCONF YANG agent over SSH connection
        	**type**\:   :py:class:`Ssh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_netconf_cfg.NetconfYang.Agent.Ssh>`
        
        

        """

        _prefix = 'man-netconf-cfg'
        _revision = '2016-03-15'

        def __init__(self):
            super(NetconfYang.Agent, self).__init__()

            self.yang_name = "agent"
            self.yang_parent_name = "netconf-yang"

            self.rate_limit = YLeaf(YType.uint32, "rate-limit")

            self.session = NetconfYang.Agent.Session()
            self.session.parent = self
            self._children_name_map["session"] = "session"
            self._children_yang_names.add("session")

            self.ssh = NetconfYang.Agent.Ssh()
            self.ssh.parent = self
            self._children_name_map["ssh"] = "ssh"
            self._children_yang_names.add("ssh")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("rate_limit") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NetconfYang.Agent, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NetconfYang.Agent, self).__setattr__(name, value)


        class Ssh(Entity):
            """
            NETCONF YANG agent over SSH connection
            
            .. attribute:: enable
            
            	Enable NETCONF YANG agent over SSH connection
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'man-netconf-cfg'
            _revision = '2016-03-15'

            def __init__(self):
                super(NetconfYang.Agent.Ssh, self).__init__()

                self.yang_name = "ssh"
                self.yang_parent_name = "agent"

                self.enable = YLeaf(YType.empty, "enable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.Agent.Ssh, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.Agent.Ssh, self).__setattr__(name, value)

            def has_data(self):
                return self.enable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ssh" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix


        class Session(Entity):
            """
            Session settings
            
            .. attribute:: absolute_timeout
            
            	Absolute timeout in minutes
            	**type**\:  int
            
            	**range:** 1..1440
            
            	**units**\: minute
            
            .. attribute:: idle_timeout
            
            	Non\-active session lifetime
            	**type**\:  int
            
            	**range:** 1..1440
            
            	**units**\: minute
            
            .. attribute:: limit
            
            	Count of allowable concurrent netconf\-yang sessions
            	**type**\:  int
            
            	**range:** 1..50
            
            	**default value**\: 50
            
            

            """

            _prefix = 'man-netconf-cfg'
            _revision = '2016-03-15'

            def __init__(self):
                super(NetconfYang.Agent.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "agent"

                self.absolute_timeout = YLeaf(YType.uint32, "absolute-timeout")

                self.idle_timeout = YLeaf(YType.uint32, "idle-timeout")

                self.limit = YLeaf(YType.uint32, "limit")

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
                                "idle_timeout",
                                "limit") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NetconfYang.Agent.Session, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NetconfYang.Agent.Session, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.absolute_timeout.is_set or
                    self.idle_timeout.is_set or
                    self.limit.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.absolute_timeout.yfilter != YFilter.not_set or
                    self.idle_timeout.yfilter != YFilter.not_set or
                    self.limit.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.absolute_timeout.is_set or self.absolute_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.absolute_timeout.get_name_leafdata())
                if (self.idle_timeout.is_set or self.idle_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.idle_timeout.get_name_leafdata())
                if (self.limit.is_set or self.limit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.limit.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "absolute-timeout" or name == "idle-timeout" or name == "limit"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "absolute-timeout"):
                    self.absolute_timeout = value
                    self.absolute_timeout.value_namespace = name_space
                    self.absolute_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "idle-timeout"):
                    self.idle_timeout = value
                    self.idle_timeout.value_namespace = name_space
                    self.idle_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "limit"):
                    self.limit = value
                    self.limit.value_namespace = name_space
                    self.limit.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.rate_limit.is_set or
                (self.session is not None and self.session.has_data()) or
                (self.ssh is not None and self.ssh.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.rate_limit.yfilter != YFilter.not_set or
                (self.session is not None and self.session.has_operation()) or
                (self.ssh is not None and self.ssh.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "agent" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-man-netconf-cfg:netconf-yang/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.rate_limit.is_set or self.rate_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rate_limit.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "session"):
                if (self.session is None):
                    self.session = NetconfYang.Agent.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                return self.session

            if (child_yang_name == "ssh"):
                if (self.ssh is None):
                    self.ssh = NetconfYang.Agent.Ssh()
                    self.ssh.parent = self
                    self._children_name_map["ssh"] = "ssh"
                return self.ssh

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "session" or name == "ssh" or name == "rate-limit"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "rate-limit"):
                self.rate_limit = value
                self.rate_limit.value_namespace = name_space
                self.rate_limit.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.agent is not None and self.agent.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.agent is not None and self.agent.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-man-netconf-cfg:netconf-yang" + path_buffer

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
                self.agent = NetconfYang.Agent()
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
        self._top_entity = NetconfYang()
        return self._top_entity

