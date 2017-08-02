""" Cisco_IOS_XR_tunnel_vpdn_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-vpdn package configuration.

This module contains definitions
for the following management objects\:
  vpdn\: VPDN configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DfBit(Enum):
    """
    DfBit

    Df bit

    .. data:: clear = 0

    	Clear df bit

    .. data:: reflect = 1

    	Reflect df bit from inner ip header

    .. data:: set = 2

    	Set df bit

    """

    clear = Enum.YLeaf(0, "clear")

    reflect = Enum.YLeaf(1, "reflect")

    set = Enum.YLeaf(2, "set")


class Option(Enum):
    """
    Option

    Option

    .. data:: local = 1

    	Log VPDN events locally

    .. data:: user = 2

    	Log VPDN user events

    .. data:: dead_cache = 8

    	Log VPDN dead cache

    .. data:: tunnel_drop = 16

    	Log VPDN tunnel drops

    """

    local = Enum.YLeaf(1, "local")

    user = Enum.YLeaf(2, "user")

    dead_cache = Enum.YLeaf(8, "dead-cache")

    tunnel_drop = Enum.YLeaf(16, "tunnel-drop")



class Vpdn(Entity):
    """
    VPDN configuration
    
    .. attribute:: caller_id
    
    	Options to apply on calling station ID
    	**type**\:   :py:class:`CallerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.CallerId>`
    
    .. attribute:: enable
    
    	Enable VPDN configuration. Deletion of this object also causes deletion of all associated objects under VPDN
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: history
    
    	VPDN history logging
    	**type**\:   :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.History>`
    
    .. attribute:: l2tp
    
    	L2TPv2 protocol commands
    	**type**\:   :py:class:`L2Tp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2Tp>`
    
    .. attribute:: local
    
    	VPDN Local radius process configuration
    	**type**\:   :py:class:`Local <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Local>`
    
    .. attribute:: loggings
    
    	Table of Logging
    	**type**\:   :py:class:`Loggings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Loggings>`
    
    .. attribute:: redundancy
    
    	Enable VPDN redundancy
    	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Redundancy>`
    
    .. attribute:: session_limit
    
    	Maximum simultaneous VPDN sessions
    	**type**\:  int
    
    	**range:** 1..131072
    
    .. attribute:: soft_shut
    
    	New session no longer allowed
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: templates
    
    	Table of Template
    	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates>`
    
    .. attribute:: vpd_ngroups
    
    	Table of VPDNgroup
    	**type**\:   :py:class:`VpdNgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups>`
    
    

    """

    _prefix = 'tunnel-vpdn-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Vpdn, self).__init__()
        self._top_entity = None

        self.yang_name = "vpdn"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-vpdn-cfg"

        self.enable = YLeaf(YType.empty, "enable")

        self.session_limit = YLeaf(YType.uint32, "session-limit")

        self.soft_shut = YLeaf(YType.empty, "soft-shut")

        self.caller_id = Vpdn.CallerId()
        self.caller_id.parent = self
        self._children_name_map["caller_id"] = "caller-id"
        self._children_yang_names.add("caller-id")

        self.history = Vpdn.History()
        self.history.parent = self
        self._children_name_map["history"] = "history"
        self._children_yang_names.add("history")

        self.l2tp = Vpdn.L2Tp()
        self.l2tp.parent = self
        self._children_name_map["l2tp"] = "l2tp"
        self._children_yang_names.add("l2tp")

        self.local = Vpdn.Local()
        self.local.parent = self
        self._children_name_map["local"] = "local"
        self._children_yang_names.add("local")

        self.loggings = Vpdn.Loggings()
        self.loggings.parent = self
        self._children_name_map["loggings"] = "loggings"
        self._children_yang_names.add("loggings")

        self.redundancy = Vpdn.Redundancy()
        self.redundancy.parent = self
        self._children_name_map["redundancy"] = "redundancy"
        self._children_yang_names.add("redundancy")

        self.templates = Vpdn.Templates()
        self.templates.parent = self
        self._children_name_map["templates"] = "templates"
        self._children_yang_names.add("templates")

        self.vpd_ngroups = Vpdn.VpdNgroups()
        self.vpd_ngroups.parent = self
        self._children_name_map["vpd_ngroups"] = "vpd-ngroups"
        self._children_yang_names.add("vpd-ngroups")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable",
                        "session_limit",
                        "soft_shut") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Vpdn, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Vpdn, self).__setattr__(name, value)


    class History(Entity):
        """
        VPDN history logging
        
        .. attribute:: failure
        
        	User failure
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.History, self).__init__()

            self.yang_name = "history"
            self.yang_parent_name = "vpdn"

            self.failure = YLeaf(YType.empty, "failure")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("failure") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.History, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.History, self).__setattr__(name, value)

        def has_data(self):
            return self.failure.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.failure.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "history" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.failure.is_set or self.failure.yfilter != YFilter.not_set):
                leaf_name_data.append(self.failure.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "failure"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "failure"):
                self.failure = value
                self.failure.value_namespace = name_space
                self.failure.value_namespace_prefix = name_space_prefix


    class Redundancy(Entity):
        """
        Enable VPDN redundancy
        
        .. attribute:: enable
        
        	Enable Enable VPDN redundancy. Deletion of this object also causes deletion of all associated objects under Redundancy
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: process_failures
        
        	Process crash configuration
        	**type**\:   :py:class:`ProcessFailures <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Redundancy.ProcessFailures>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.Redundancy, self).__init__()

            self.yang_name = "redundancy"
            self.yang_parent_name = "vpdn"

            self.enable = YLeaf(YType.empty, "enable")

            self.process_failures = Vpdn.Redundancy.ProcessFailures()
            self.process_failures.parent = self
            self._children_name_map["process_failures"] = "process-failures"
            self._children_yang_names.add("process-failures")

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
                        super(Vpdn.Redundancy, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.Redundancy, self).__setattr__(name, value)


        class ProcessFailures(Entity):
            """
            Process crash configuration
            
            .. attribute:: switchover
            
            	Force a switchover if the process crashes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.Redundancy.ProcessFailures, self).__init__()

                self.yang_name = "process-failures"
                self.yang_parent_name = "redundancy"

                self.switchover = YLeaf(YType.empty, "switchover")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("switchover") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.Redundancy.ProcessFailures, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.Redundancy.ProcessFailures, self).__setattr__(name, value)

            def has_data(self):
                return self.switchover.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.switchover.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "process-failures" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/redundancy/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.switchover.is_set or self.switchover.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.switchover.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "switchover"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "switchover"):
                    self.switchover = value
                    self.switchover.value_namespace = name_space
                    self.switchover.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.enable.is_set or
                (self.process_failures is not None and self.process_failures.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                (self.process_failures is not None and self.process_failures.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "redundancy" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
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

            if (child_yang_name == "process-failures"):
                if (self.process_failures is None):
                    self.process_failures = Vpdn.Redundancy.ProcessFailures()
                    self.process_failures.parent = self
                    self._children_name_map["process_failures"] = "process-failures"
                return self.process_failures

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "process-failures" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix


    class Local(Entity):
        """
        VPDN Local radius process configuration
        
        .. attribute:: cache_disabled
        
        	Set constant integer
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: path
        
        	local path of the saved profile
        	**type**\:  str
        
        	**length:** 1..64
        
        .. attribute:: port
        
        	port value
        	**type**\:  int
        
        	**range:** 1..65535
        
        .. attribute:: secret_text
        
        	secret password
        	**type**\:  str
        
        	**length:** 1..32
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.Local, self).__init__()

            self.yang_name = "local"
            self.yang_parent_name = "vpdn"

            self.cache_disabled = YLeaf(YType.empty, "cache-disabled")

            self.path = YLeaf(YType.str, "path")

            self.port = YLeaf(YType.uint16, "port")

            self.secret_text = YLeaf(YType.str, "secret-text")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cache_disabled",
                            "path",
                            "port",
                            "secret_text") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.Local, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.Local, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cache_disabled.is_set or
                self.path.is_set or
                self.port.is_set or
                self.secret_text.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cache_disabled.yfilter != YFilter.not_set or
                self.path.yfilter != YFilter.not_set or
                self.port.yfilter != YFilter.not_set or
                self.secret_text.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "local" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cache_disabled.is_set or self.cache_disabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cache_disabled.get_name_leafdata())
            if (self.path.is_set or self.path.yfilter != YFilter.not_set):
                leaf_name_data.append(self.path.get_name_leafdata())
            if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                leaf_name_data.append(self.port.get_name_leafdata())
            if (self.secret_text.is_set or self.secret_text.yfilter != YFilter.not_set):
                leaf_name_data.append(self.secret_text.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cache-disabled" or name == "path" or name == "port" or name == "secret-text"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cache-disabled"):
                self.cache_disabled = value
                self.cache_disabled.value_namespace = name_space
                self.cache_disabled.value_namespace_prefix = name_space_prefix
            if(value_path == "path"):
                self.path = value
                self.path.value_namespace = name_space
                self.path.value_namespace_prefix = name_space_prefix
            if(value_path == "port"):
                self.port = value
                self.port.value_namespace = name_space
                self.port.value_namespace_prefix = name_space_prefix
            if(value_path == "secret-text"):
                self.secret_text = value
                self.secret_text.value_namespace = name_space
                self.secret_text.value_namespace_prefix = name_space_prefix


    class Templates(Entity):
        """
        Table of Template
        
        .. attribute:: template
        
        	VPDN template configuration
        	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.Templates, self).__init__()

            self.yang_name = "templates"
            self.yang_parent_name = "vpdn"

            self.template = YList(self)

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
                        super(Vpdn.Templates, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.Templates, self).__setattr__(name, value)


        class Template(Entity):
            """
            VPDN template configuration
            
            .. attribute:: template_name  <key>
            
            	VPDN template name
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: caller_id
            
            	Options to apply on calling station id
            	**type**\:   :py:class:`CallerId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.CallerId>`
            
            .. attribute:: cisco_avp100_format_e_enable
            
            	To support NAS\-Port format e in Cisco AVP 100
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: description
            
            	Up to 100 characters describing this VPDN template
            	**type**\:  str
            
            	**length:** 1..100
            
            .. attribute:: dsl_line_forwarding
            
            	Forward DSL Line Info attributes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ip
            
            	Set IP TOS value
            	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Ip>`
            
            .. attribute:: ipv4
            
            	IPv4 settings for tunnel
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Ipv4>`
            
            .. attribute:: l2tp_class
            
            	L2TP class  command
            	**type**\:  str
            
            	**length:** 1..79
            
            .. attribute:: tunnel
            
            	L2TP tunnel commands
            	**type**\:   :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Tunnel>`
            
            .. attribute:: vpn
            
            	VPN ID/VRF name
            	**type**\:   :py:class:`Vpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Vpn>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.Templates.Template, self).__init__()

                self.yang_name = "template"
                self.yang_parent_name = "templates"

                self.template_name = YLeaf(YType.str, "template-name")

                self.cisco_avp100_format_e_enable = YLeaf(YType.empty, "cisco-avp100-format-e-enable")

                self.description = YLeaf(YType.str, "description")

                self.dsl_line_forwarding = YLeaf(YType.empty, "dsl-line-forwarding")

                self.l2tp_class = YLeaf(YType.str, "l2tp-class")

                self.caller_id = Vpdn.Templates.Template.CallerId()
                self.caller_id.parent = self
                self._children_name_map["caller_id"] = "caller-id"
                self._children_yang_names.add("caller-id")

                self.ip = Vpdn.Templates.Template.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"
                self._children_yang_names.add("ip")

                self.ipv4 = Vpdn.Templates.Template.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"
                self._children_yang_names.add("ipv4")

                self.tunnel = Vpdn.Templates.Template.Tunnel()
                self.tunnel.parent = self
                self._children_name_map["tunnel"] = "tunnel"
                self._children_yang_names.add("tunnel")

                self.vpn = Vpdn.Templates.Template.Vpn()
                self.vpn.parent = self
                self._children_name_map["vpn"] = "vpn"
                self._children_yang_names.add("vpn")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("template_name",
                                "cisco_avp100_format_e_enable",
                                "description",
                                "dsl_line_forwarding",
                                "l2tp_class") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.Templates.Template, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.Templates.Template, self).__setattr__(name, value)


            class CallerId(Entity):
                """
                Options to apply on calling station id
                
                .. attribute:: mask
                
                	Mask characters by method
                	**type**\:  str
                
                	**length:** 1..63
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Templates.Template.CallerId, self).__init__()

                    self.yang_name = "caller-id"
                    self.yang_parent_name = "template"

                    self.mask = YLeaf(YType.str, "mask")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mask") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Templates.Template.CallerId, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Templates.Template.CallerId, self).__setattr__(name, value)

                def has_data(self):
                    return self.mask.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mask.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "caller-id" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mask.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mask"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mask"):
                        self.mask = value
                        self.mask.value_namespace = name_space
                        self.mask.value_namespace_prefix = name_space_prefix


            class Vpn(Entity):
                """
                VPN ID/VRF name
                
                .. attribute:: id
                
                	VPN ID
                	**type**\:   :py:class:`Id <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Templates.Template.Vpn.Id>`
                
                .. attribute:: vrf
                
                	VRF name
                	**type**\:  str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Templates.Template.Vpn, self).__init__()

                    self.yang_name = "vpn"
                    self.yang_parent_name = "template"

                    self.vrf = YLeaf(YType.str, "vrf")

                    self.id = Vpdn.Templates.Template.Vpn.Id()
                    self.id.parent = self
                    self._children_name_map["id"] = "id"
                    self._children_yang_names.add("id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vrf") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Templates.Template.Vpn, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Templates.Template.Vpn, self).__setattr__(name, value)


                class Id(Entity):
                    """
                    VPN ID
                    
                    .. attribute:: index
                    
                    	VPN ID, (OUI\:VPN\-Index) format(hex), 4 bytes VPN\_Index Part
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: oui
                    
                    	VPN ID, (OUI\:VPN\-Index) format(hex), 3 bytes OUI Part
                    	**type**\:  str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    

                    """

                    _prefix = 'tunnel-vpdn-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Vpdn.Templates.Template.Vpn.Id, self).__init__()

                        self.yang_name = "id"
                        self.yang_parent_name = "vpn"

                        self.index = YLeaf(YType.str, "index")

                        self.oui = YLeaf(YType.str, "oui")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index",
                                        "oui") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Vpdn.Templates.Template.Vpn.Id, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Vpdn.Templates.Template.Vpn.Id, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.index.is_set or
                            self.oui.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            self.oui.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())
                        if (self.oui.is_set or self.oui.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.oui.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "index" or name == "oui"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix
                        if(value_path == "oui"):
                            self.oui = value
                            self.oui.value_namespace = name_space
                            self.oui.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.vrf.is_set or
                        (self.id is not None and self.id.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vrf.yfilter != YFilter.not_set or
                        (self.id is not None and self.id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vpn" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "id"):
                        if (self.id is None):
                            self.id = Vpdn.Templates.Template.Vpn.Id()
                            self.id.parent = self
                            self._children_name_map["id"] = "id"
                        return self.id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "id" or name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vrf"):
                        self.vrf = value
                        self.vrf.value_namespace = name_space
                        self.vrf.value_namespace_prefix = name_space_prefix


            class Tunnel(Entity):
                """
                L2TP tunnel commands
                
                .. attribute:: busy_timeout
                
                	Busy time out value in seconds
                	**type**\:  int
                
                	**range:** 60..65535
                
                	**units**\: second
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Templates.Template.Tunnel, self).__init__()

                    self.yang_name = "tunnel"
                    self.yang_parent_name = "template"

                    self.busy_timeout = YLeaf(YType.uint32, "busy-timeout")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("busy_timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Templates.Template.Tunnel, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Templates.Template.Tunnel, self).__setattr__(name, value)

                def has_data(self):
                    return self.busy_timeout.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.busy_timeout.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "tunnel" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.busy_timeout.is_set or self.busy_timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.busy_timeout.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "busy-timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "busy-timeout"):
                        self.busy_timeout = value
                        self.busy_timeout.value_namespace = name_space
                        self.busy_timeout.value_namespace_prefix = name_space_prefix


            class Ip(Entity):
                """
                Set IP TOS value
                
                .. attribute:: tos
                
                	Set constant integer
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Templates.Template.Ip, self).__init__()

                    self.yang_name = "ip"
                    self.yang_parent_name = "template"

                    self.tos = YLeaf(YType.int32, "tos")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("tos") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Templates.Template.Ip, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Templates.Template.Ip, self).__setattr__(name, value)

                def has_data(self):
                    return self.tos.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.tos.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.tos.is_set or self.tos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tos.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tos"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "tos"):
                        self.tos = value
                        self.tos.value_namespace = name_space
                        self.tos.value_namespace_prefix = name_space_prefix


            class Ipv4(Entity):
                """
                IPv4 settings for tunnel
                
                .. attribute:: df_bit
                
                	IPv4 don't fragment bit set/clear/reflect
                	**type**\:   :py:class:`DfBit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.DfBit>`
                
                .. attribute:: source
                
                	Enter an IP address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.Templates.Template.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "template"

                    self.df_bit = YLeaf(YType.enumeration, "df-bit")

                    self.source = YLeaf(YType.str, "source")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("df_bit",
                                    "source") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.Templates.Template.Ipv4, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.Templates.Template.Ipv4, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.df_bit.is_set or
                        self.source.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.df_bit.yfilter != YFilter.not_set or
                        self.source.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ipv4" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.df_bit.is_set or self.df_bit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.df_bit.get_name_leafdata())
                    if (self.source.is_set or self.source.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "df-bit" or name == "source"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "df-bit"):
                        self.df_bit = value
                        self.df_bit.value_namespace = name_space
                        self.df_bit.value_namespace_prefix = name_space_prefix
                    if(value_path == "source"):
                        self.source = value
                        self.source.value_namespace = name_space
                        self.source.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.template_name.is_set or
                    self.cisco_avp100_format_e_enable.is_set or
                    self.description.is_set or
                    self.dsl_line_forwarding.is_set or
                    self.l2tp_class.is_set or
                    (self.caller_id is not None and self.caller_id.has_data()) or
                    (self.ip is not None and self.ip.has_data()) or
                    (self.ipv4 is not None and self.ipv4.has_data()) or
                    (self.tunnel is not None and self.tunnel.has_data()) or
                    (self.vpn is not None and self.vpn.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.template_name.yfilter != YFilter.not_set or
                    self.cisco_avp100_format_e_enable.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.dsl_line_forwarding.yfilter != YFilter.not_set or
                    self.l2tp_class.yfilter != YFilter.not_set or
                    (self.caller_id is not None and self.caller_id.has_operation()) or
                    (self.ip is not None and self.ip.has_operation()) or
                    (self.ipv4 is not None and self.ipv4.has_operation()) or
                    (self.tunnel is not None and self.tunnel.has_operation()) or
                    (self.vpn is not None and self.vpn.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "template" + "[template-name='" + self.template_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/templates/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.template_name.is_set or self.template_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.template_name.get_name_leafdata())
                if (self.cisco_avp100_format_e_enable.is_set or self.cisco_avp100_format_e_enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cisco_avp100_format_e_enable.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.dsl_line_forwarding.is_set or self.dsl_line_forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsl_line_forwarding.get_name_leafdata())
                if (self.l2tp_class.is_set or self.l2tp_class.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.l2tp_class.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "caller-id"):
                    if (self.caller_id is None):
                        self.caller_id = Vpdn.Templates.Template.CallerId()
                        self.caller_id.parent = self
                        self._children_name_map["caller_id"] = "caller-id"
                    return self.caller_id

                if (child_yang_name == "ip"):
                    if (self.ip is None):
                        self.ip = Vpdn.Templates.Template.Ip()
                        self.ip.parent = self
                        self._children_name_map["ip"] = "ip"
                    return self.ip

                if (child_yang_name == "ipv4"):
                    if (self.ipv4 is None):
                        self.ipv4 = Vpdn.Templates.Template.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                    return self.ipv4

                if (child_yang_name == "tunnel"):
                    if (self.tunnel is None):
                        self.tunnel = Vpdn.Templates.Template.Tunnel()
                        self.tunnel.parent = self
                        self._children_name_map["tunnel"] = "tunnel"
                    return self.tunnel

                if (child_yang_name == "vpn"):
                    if (self.vpn is None):
                        self.vpn = Vpdn.Templates.Template.Vpn()
                        self.vpn.parent = self
                        self._children_name_map["vpn"] = "vpn"
                    return self.vpn

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "caller-id" or name == "ip" or name == "ipv4" or name == "tunnel" or name == "vpn" or name == "template-name" or name == "cisco-avp100-format-e-enable" or name == "description" or name == "dsl-line-forwarding" or name == "l2tp-class"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "template-name"):
                    self.template_name = value
                    self.template_name.value_namespace = name_space
                    self.template_name.value_namespace_prefix = name_space_prefix
                if(value_path == "cisco-avp100-format-e-enable"):
                    self.cisco_avp100_format_e_enable = value
                    self.cisco_avp100_format_e_enable.value_namespace = name_space
                    self.cisco_avp100_format_e_enable.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "dsl-line-forwarding"):
                    self.dsl_line_forwarding = value
                    self.dsl_line_forwarding.value_namespace = name_space
                    self.dsl_line_forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "l2tp-class"):
                    self.l2tp_class = value
                    self.l2tp_class.value_namespace = name_space
                    self.l2tp_class.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.template:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.template:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "templates" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "template"):
                for c in self.template:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vpdn.Templates.Template()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.template.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "template"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class CallerId(Entity):
        """
        Options to apply on calling station ID
        
        .. attribute:: mask
        
        	Mask characters by method
        	**type**\:  str
        
        	**length:** 1..63
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.CallerId, self).__init__()

            self.yang_name = "caller-id"
            self.yang_parent_name = "vpdn"

            self.mask = YLeaf(YType.str, "mask")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mask") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.CallerId, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.CallerId, self).__setattr__(name, value)

        def has_data(self):
            return self.mask.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mask.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "caller-id" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mask.is_set or self.mask.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mask.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mask"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mask"):
                self.mask = value
                self.mask.value_namespace = name_space
                self.mask.value_namespace_prefix = name_space_prefix


    class VpdNgroups(Entity):
        """
        Table of VPDNgroup
        
        .. attribute:: vpd_ngroup
        
        	vpdn\-group configuration
        	**type**\: list of    :py:class:`VpdNgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.VpdNgroups, self).__init__()

            self.yang_name = "vpd-ngroups"
            self.yang_parent_name = "vpdn"

            self.vpd_ngroup = YList(self)

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
                        super(Vpdn.VpdNgroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.VpdNgroups, self).__setattr__(name, value)


        class VpdNgroup(Entity):
            """
            vpdn\-group configuration
            
            .. attribute:: vpd_ngroupname  <key>
            
            	vpdn\-group name
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: attribute
            
            	match substring
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: cisco_avp100_format_e_enable
            
            	To support NAS\-Port format e in cisco AVP 100
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: desc
            
            	upto 100 characters describing this VPDN group
            	**type**\:  str
            
            	**length:** 1..100
            
            .. attribute:: dsl_line_forwarding
            
            	Forward DSL Line Info attributes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ip
            
            	set ip tos value
            	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup.Ip>`
            
            .. attribute:: l2tp_class
            
            	l2tp class name
            	**type**\:  str
            
            	**length:** 1..79
            
            .. attribute:: sr_ctemplate
            
            	Source vpdn\-template
            	**type**\:  str
            
            	**length:** 1..63
            
            .. attribute:: tunnel_busy_timeout
            
            	Busy list timeout length
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: vpn_id
            
            	Vpn id
            	**type**\:   :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.VpdNgroups.VpdNgroup.VpnId>`
            
            .. attribute:: vrf_name
            
            	Vrf name
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.VpdNgroups.VpdNgroup, self).__init__()

                self.yang_name = "vpd-ngroup"
                self.yang_parent_name = "vpd-ngroups"

                self.vpd_ngroupname = YLeaf(YType.str, "vpd-ngroupname")

                self.attribute = YLeaf(YType.str, "attribute")

                self.cisco_avp100_format_e_enable = YLeaf(YType.empty, "cisco-avp100-format-e-enable")

                self.desc = YLeaf(YType.str, "desc")

                self.dsl_line_forwarding = YLeaf(YType.empty, "dsl-line-forwarding")

                self.l2tp_class = YLeaf(YType.str, "l2tp-class")

                self.sr_ctemplate = YLeaf(YType.str, "sr-ctemplate")

                self.tunnel_busy_timeout = YLeaf(YType.uint32, "tunnel-busy-timeout")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.ip = Vpdn.VpdNgroups.VpdNgroup.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"
                self._children_yang_names.add("ip")

                self.vpn_id = Vpdn.VpdNgroups.VpdNgroup.VpnId()
                self.vpn_id.parent = self
                self._children_name_map["vpn_id"] = "vpn-id"
                self._children_yang_names.add("vpn-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vpd_ngroupname",
                                "attribute",
                                "cisco_avp100_format_e_enable",
                                "desc",
                                "dsl_line_forwarding",
                                "l2tp_class",
                                "sr_ctemplate",
                                "tunnel_busy_timeout",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.VpdNgroups.VpdNgroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.VpdNgroups.VpdNgroup, self).__setattr__(name, value)


            class VpnId(Entity):
                """
                Vpn id
                
                .. attribute:: vpn_id_index
                
                	VPN ID, (OUI\:VPN\-Index) format(hex), 4 bytes VPN\_Index Part
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: vpn_id_oui
                
                	VPN ID, (OUI\:VPN\-Index) format(hex), 3 bytes OUI Part
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.VpdNgroups.VpdNgroup.VpnId, self).__init__()

                    self.yang_name = "vpn-id"
                    self.yang_parent_name = "vpd-ngroup"

                    self.vpn_id_index = YLeaf(YType.str, "vpn-id-index")

                    self.vpn_id_oui = YLeaf(YType.str, "vpn-id-oui")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("vpn_id_index",
                                    "vpn_id_oui") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.VpdNgroups.VpdNgroup.VpnId, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.VpdNgroups.VpdNgroup.VpnId, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.vpn_id_index.is_set or
                        self.vpn_id_oui.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.vpn_id_index.yfilter != YFilter.not_set or
                        self.vpn_id_oui.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vpn-id" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.vpn_id_index.is_set or self.vpn_id_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpn_id_index.get_name_leafdata())
                    if (self.vpn_id_oui.is_set or self.vpn_id_oui.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpn_id_oui.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vpn-id-index" or name == "vpn-id-oui"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "vpn-id-index"):
                        self.vpn_id_index = value
                        self.vpn_id_index.value_namespace = name_space
                        self.vpn_id_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpn-id-oui"):
                        self.vpn_id_oui = value
                        self.vpn_id_oui.value_namespace = name_space
                        self.vpn_id_oui.value_namespace_prefix = name_space_prefix


            class Ip(Entity):
                """
                set ip tos value
                
                .. attribute:: tos
                
                	ip tos value
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.VpdNgroups.VpdNgroup.Ip, self).__init__()

                    self.yang_name = "ip"
                    self.yang_parent_name = "vpd-ngroup"

                    self.tos = YLeaf(YType.uint32, "tos")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("tos") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.VpdNgroups.VpdNgroup.Ip, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.VpdNgroups.VpdNgroup.Ip, self).__setattr__(name, value)

                def has_data(self):
                    return self.tos.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.tos.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.tos.is_set or self.tos.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tos.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tos"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "tos"):
                        self.tos = value
                        self.tos.value_namespace = name_space
                        self.tos.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.vpd_ngroupname.is_set or
                    self.attribute.is_set or
                    self.cisco_avp100_format_e_enable.is_set or
                    self.desc.is_set or
                    self.dsl_line_forwarding.is_set or
                    self.l2tp_class.is_set or
                    self.sr_ctemplate.is_set or
                    self.tunnel_busy_timeout.is_set or
                    self.vrf_name.is_set or
                    (self.ip is not None and self.ip.has_data()) or
                    (self.vpn_id is not None and self.vpn_id.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vpd_ngroupname.yfilter != YFilter.not_set or
                    self.attribute.yfilter != YFilter.not_set or
                    self.cisco_avp100_format_e_enable.yfilter != YFilter.not_set or
                    self.desc.yfilter != YFilter.not_set or
                    self.dsl_line_forwarding.yfilter != YFilter.not_set or
                    self.l2tp_class.yfilter != YFilter.not_set or
                    self.sr_ctemplate.yfilter != YFilter.not_set or
                    self.tunnel_busy_timeout.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.ip is not None and self.ip.has_operation()) or
                    (self.vpn_id is not None and self.vpn_id.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vpd-ngroup" + "[vpd-ngroupname='" + self.vpd_ngroupname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/vpd-ngroups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vpd_ngroupname.is_set or self.vpd_ngroupname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vpd_ngroupname.get_name_leafdata())
                if (self.attribute.is_set or self.attribute.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.attribute.get_name_leafdata())
                if (self.cisco_avp100_format_e_enable.is_set or self.cisco_avp100_format_e_enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cisco_avp100_format_e_enable.get_name_leafdata())
                if (self.desc.is_set or self.desc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.desc.get_name_leafdata())
                if (self.dsl_line_forwarding.is_set or self.dsl_line_forwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dsl_line_forwarding.get_name_leafdata())
                if (self.l2tp_class.is_set or self.l2tp_class.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.l2tp_class.get_name_leafdata())
                if (self.sr_ctemplate.is_set or self.sr_ctemplate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.sr_ctemplate.get_name_leafdata())
                if (self.tunnel_busy_timeout.is_set or self.tunnel_busy_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tunnel_busy_timeout.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ip"):
                    if (self.ip is None):
                        self.ip = Vpdn.VpdNgroups.VpdNgroup.Ip()
                        self.ip.parent = self
                        self._children_name_map["ip"] = "ip"
                    return self.ip

                if (child_yang_name == "vpn-id"):
                    if (self.vpn_id is None):
                        self.vpn_id = Vpdn.VpdNgroups.VpdNgroup.VpnId()
                        self.vpn_id.parent = self
                        self._children_name_map["vpn_id"] = "vpn-id"
                    return self.vpn_id

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ip" or name == "vpn-id" or name == "vpd-ngroupname" or name == "attribute" or name == "cisco-avp100-format-e-enable" or name == "desc" or name == "dsl-line-forwarding" or name == "l2tp-class" or name == "sr-ctemplate" or name == "tunnel-busy-timeout" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vpd-ngroupname"):
                    self.vpd_ngroupname = value
                    self.vpd_ngroupname.value_namespace = name_space
                    self.vpd_ngroupname.value_namespace_prefix = name_space_prefix
                if(value_path == "attribute"):
                    self.attribute = value
                    self.attribute.value_namespace = name_space
                    self.attribute.value_namespace_prefix = name_space_prefix
                if(value_path == "cisco-avp100-format-e-enable"):
                    self.cisco_avp100_format_e_enable = value
                    self.cisco_avp100_format_e_enable.value_namespace = name_space
                    self.cisco_avp100_format_e_enable.value_namespace_prefix = name_space_prefix
                if(value_path == "desc"):
                    self.desc = value
                    self.desc.value_namespace = name_space
                    self.desc.value_namespace_prefix = name_space_prefix
                if(value_path == "dsl-line-forwarding"):
                    self.dsl_line_forwarding = value
                    self.dsl_line_forwarding.value_namespace = name_space
                    self.dsl_line_forwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "l2tp-class"):
                    self.l2tp_class = value
                    self.l2tp_class.value_namespace = name_space
                    self.l2tp_class.value_namespace_prefix = name_space_prefix
                if(value_path == "sr-ctemplate"):
                    self.sr_ctemplate = value
                    self.sr_ctemplate.value_namespace = name_space
                    self.sr_ctemplate.value_namespace_prefix = name_space_prefix
                if(value_path == "tunnel-busy-timeout"):
                    self.tunnel_busy_timeout = value
                    self.tunnel_busy_timeout.value_namespace = name_space
                    self.tunnel_busy_timeout.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vpd_ngroup:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vpd_ngroup:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vpd-ngroups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vpd-ngroup"):
                for c in self.vpd_ngroup:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vpdn.VpdNgroups.VpdNgroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vpd_ngroup.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vpd-ngroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Loggings(Entity):
        """
        Table of Logging
        
        .. attribute:: logging
        
        	Configure logging for VPDN
        	**type**\: list of    :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.Loggings.Logging>`
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.Loggings, self).__init__()

            self.yang_name = "loggings"
            self.yang_parent_name = "vpdn"

            self.logging = YList(self)

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
                        super(Vpdn.Loggings, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.Loggings, self).__setattr__(name, value)


        class Logging(Entity):
            """
            Configure logging for VPDN
            
            .. attribute:: option  <key>
            
            	VPDN logging options
            	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Option>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.Loggings.Logging, self).__init__()

                self.yang_name = "logging"
                self.yang_parent_name = "loggings"

                self.option = YLeaf(YType.enumeration, "option")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("option") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vpdn.Loggings.Logging, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vpdn.Loggings.Logging, self).__setattr__(name, value)

            def has_data(self):
                return self.option.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.option.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "logging" + "[option='" + self.option.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/loggings/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.option.is_set or self.option.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.option.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "option"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "option"):
                    self.option = value
                    self.option.value_namespace = name_space
                    self.option.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.logging:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.logging:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "loggings" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "logging"):
                for c in self.logging:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vpdn.Loggings.Logging()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.logging.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "logging"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class L2Tp(Entity):
        """
        L2TPv2 protocol commands
        
        .. attribute:: reassembly
        
        	L2TP IP packet reassembly enable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: session_id
        
        	Session ID commands
        	**type**\:   :py:class:`SessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2Tp.SessionId>`
        
        .. attribute:: tcp_mss_adjust
        
        	TCP MSS adjust value. The acceptable values might be further limited depending on platform
        	**type**\:  int
        
        	**range:** 1280..1460
        
        

        """

        _prefix = 'tunnel-vpdn-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Vpdn.L2Tp, self).__init__()

            self.yang_name = "l2tp"
            self.yang_parent_name = "vpdn"

            self.reassembly = YLeaf(YType.empty, "reassembly")

            self.tcp_mss_adjust = YLeaf(YType.uint32, "tcp-mss-adjust")

            self.session_id = Vpdn.L2Tp.SessionId()
            self.session_id.parent = self
            self._children_name_map["session_id"] = "session-id"
            self._children_yang_names.add("session-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("reassembly",
                            "tcp_mss_adjust") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Vpdn.L2Tp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vpdn.L2Tp, self).__setattr__(name, value)


        class SessionId(Entity):
            """
            Session ID commands
            
            .. attribute:: space
            
            	Session ID space commands
            	**type**\:   :py:class:`Space <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg.Vpdn.L2Tp.SessionId.Space>`
            
            

            """

            _prefix = 'tunnel-vpdn-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Vpdn.L2Tp.SessionId, self).__init__()

                self.yang_name = "session-id"
                self.yang_parent_name = "l2tp"

                self.space = Vpdn.L2Tp.SessionId.Space()
                self.space.parent = self
                self._children_name_map["space"] = "space"
                self._children_yang_names.add("space")


            class Space(Entity):
                """
                Session ID space commands
                
                .. attribute:: hierarchy
                
                	Session ID space hierarchical command
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'tunnel-vpdn-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Vpdn.L2Tp.SessionId.Space, self).__init__()

                    self.yang_name = "space"
                    self.yang_parent_name = "session-id"

                    self.hierarchy = YLeaf(YType.empty, "hierarchy")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("hierarchy") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Vpdn.L2Tp.SessionId.Space, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Vpdn.L2Tp.SessionId.Space, self).__setattr__(name, value)

                def has_data(self):
                    return self.hierarchy.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.hierarchy.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "space" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/l2tp/session-id/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.hierarchy.is_set or self.hierarchy.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hierarchy.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hierarchy"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "hierarchy"):
                        self.hierarchy = value
                        self.hierarchy.value_namespace = name_space
                        self.hierarchy.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (self.space is not None and self.space.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.space is not None and self.space.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session-id" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/l2tp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "space"):
                    if (self.space is None):
                        self.space = Vpdn.L2Tp.SessionId.Space()
                        self.space.parent = self
                        self._children_name_map["space"] = "space"
                    return self.space

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "space"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.reassembly.is_set or
                self.tcp_mss_adjust.is_set or
                (self.session_id is not None and self.session_id.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.reassembly.yfilter != YFilter.not_set or
                self.tcp_mss_adjust.yfilter != YFilter.not_set or
                (self.session_id is not None and self.session_id.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "l2tp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.reassembly.is_set or self.reassembly.yfilter != YFilter.not_set):
                leaf_name_data.append(self.reassembly.get_name_leafdata())
            if (self.tcp_mss_adjust.is_set or self.tcp_mss_adjust.yfilter != YFilter.not_set):
                leaf_name_data.append(self.tcp_mss_adjust.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "session-id"):
                if (self.session_id is None):
                    self.session_id = Vpdn.L2Tp.SessionId()
                    self.session_id.parent = self
                    self._children_name_map["session_id"] = "session-id"
                return self.session_id

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "session-id" or name == "reassembly" or name == "tcp-mss-adjust"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "reassembly"):
                self.reassembly = value
                self.reassembly.value_namespace = name_space
                self.reassembly.value_namespace_prefix = name_space_prefix
            if(value_path == "tcp-mss-adjust"):
                self.tcp_mss_adjust = value
                self.tcp_mss_adjust.value_namespace = name_space
                self.tcp_mss_adjust.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.enable.is_set or
            self.session_limit.is_set or
            self.soft_shut.is_set or
            (self.caller_id is not None and self.caller_id.has_data()) or
            (self.history is not None and self.history.has_data()) or
            (self.l2tp is not None and self.l2tp.has_data()) or
            (self.local is not None and self.local.has_data()) or
            (self.loggings is not None and self.loggings.has_data()) or
            (self.redundancy is not None and self.redundancy.has_data()) or
            (self.templates is not None and self.templates.has_data()) or
            (self.vpd_ngroups is not None and self.vpd_ngroups.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.session_limit.yfilter != YFilter.not_set or
            self.soft_shut.yfilter != YFilter.not_set or
            (self.caller_id is not None and self.caller_id.has_operation()) or
            (self.history is not None and self.history.has_operation()) or
            (self.l2tp is not None and self.l2tp.has_operation()) or
            (self.local is not None and self.local.has_operation()) or
            (self.loggings is not None and self.loggings.has_operation()) or
            (self.redundancy is not None and self.redundancy.has_operation()) or
            (self.templates is not None and self.templates.has_operation()) or
            (self.vpd_ngroups is not None and self.vpd_ngroups.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-tunnel-vpdn-cfg:vpdn" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.session_limit.is_set or self.session_limit.yfilter != YFilter.not_set):
            leaf_name_data.append(self.session_limit.get_name_leafdata())
        if (self.soft_shut.is_set or self.soft_shut.yfilter != YFilter.not_set):
            leaf_name_data.append(self.soft_shut.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "caller-id"):
            if (self.caller_id is None):
                self.caller_id = Vpdn.CallerId()
                self.caller_id.parent = self
                self._children_name_map["caller_id"] = "caller-id"
            return self.caller_id

        if (child_yang_name == "history"):
            if (self.history is None):
                self.history = Vpdn.History()
                self.history.parent = self
                self._children_name_map["history"] = "history"
            return self.history

        if (child_yang_name == "l2tp"):
            if (self.l2tp is None):
                self.l2tp = Vpdn.L2Tp()
                self.l2tp.parent = self
                self._children_name_map["l2tp"] = "l2tp"
            return self.l2tp

        if (child_yang_name == "local"):
            if (self.local is None):
                self.local = Vpdn.Local()
                self.local.parent = self
                self._children_name_map["local"] = "local"
            return self.local

        if (child_yang_name == "loggings"):
            if (self.loggings is None):
                self.loggings = Vpdn.Loggings()
                self.loggings.parent = self
                self._children_name_map["loggings"] = "loggings"
            return self.loggings

        if (child_yang_name == "redundancy"):
            if (self.redundancy is None):
                self.redundancy = Vpdn.Redundancy()
                self.redundancy.parent = self
                self._children_name_map["redundancy"] = "redundancy"
            return self.redundancy

        if (child_yang_name == "templates"):
            if (self.templates is None):
                self.templates = Vpdn.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
            return self.templates

        if (child_yang_name == "vpd-ngroups"):
            if (self.vpd_ngroups is None):
                self.vpd_ngroups = Vpdn.VpdNgroups()
                self.vpd_ngroups.parent = self
                self._children_name_map["vpd_ngroups"] = "vpd-ngroups"
            return self.vpd_ngroups

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "caller-id" or name == "history" or name == "l2tp" or name == "local" or name == "loggings" or name == "redundancy" or name == "templates" or name == "vpd-ngroups" or name == "enable" or name == "session-limit" or name == "soft-shut"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "session-limit"):
            self.session_limit = value
            self.session_limit.value_namespace = name_space
            self.session_limit.value_namespace_prefix = name_space_prefix
        if(value_path == "soft-shut"):
            self.soft_shut = value
            self.soft_shut.value_namespace = name_space
            self.soft_shut.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Vpdn()
        return self._top_entity

