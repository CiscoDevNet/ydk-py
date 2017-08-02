""" Cisco_IOS_XR_man_xml_ttyagent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR man\-xml\-ttyagent package configuration.

This module contains definitions
for the following management objects\:
  xr\-xml\: XML
  netconf\: netconf

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class XrXml(Entity):
    """
    XML
    
    .. attribute:: agent
    
    	XML agent
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(XrXml, self).__init__()
        self._top_entity = None

        self.yang_name = "xr-xml"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-cfg"

        self.agent = XrXml.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")


    class Agent(Entity):
        """
        XML agent
        
        .. attribute:: default
        
        	XML default dedicated agent
        	**type**\:   :py:class:`Default <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default>`
        
        .. attribute:: ssl
        
        	XML SSL agent
        	**type**\:   :py:class:`Ssl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl>`
        
        .. attribute:: tty
        
        	XML TTY agent
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-cfg'
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


        class Default(Entity):
            """
            XML default dedicated agent
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: ipv4_disable
            
            	TRUE to disable IPV4
            	**type**\:  bool
            
            .. attribute:: ipv6_enable
            
            	IPv6 Transport State
            	**type**\:  bool
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\:  int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Session>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\:  int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Throttle>`
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Vrfs>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Default, self).__init__()

                self.yang_name = "default"
                self.yang_parent_name = "agent"

                self.enable = YLeaf(YType.empty, "enable")

                self.ipv4_disable = YLeaf(YType.boolean, "ipv4-disable")

                self.ipv6_enable = YLeaf(YType.boolean, "ipv6-enable")

                self.iteration_size = YLeaf(YType.uint32, "iteration-size")

                self.streaming_size = YLeaf(YType.uint32, "streaming-size")

                self.session = XrXml.Agent.Default.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")

                self.throttle = XrXml.Agent.Default.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"
                self._children_yang_names.add("throttle")

                self.vrfs = XrXml.Agent.Default.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._children_yang_names.add("vrfs")

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
                                "ipv4_disable",
                                "ipv6_enable",
                                "iteration_size",
                                "streaming_size") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(XrXml.Agent.Default, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(XrXml.Agent.Default, self).__setattr__(name, value)


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Default.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "default"

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
                        if name in ("timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(XrXml.Agent.Default.Session, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Default.Session, self).__setattr__(name, value)

                def has_data(self):
                    return self.timeout.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "session" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
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
                    if(name == "timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix


            class Throttle(Entity):
                """
                XML agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Default.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "default"

                    self.memory = YLeaf(YType.uint32, "memory")

                    self.process_rate = YLeaf(YType.uint32, "process-rate")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory",
                                    "process_rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(XrXml.Agent.Default.Throttle, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Default.Throttle, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory.is_set or
                        self.process_rate.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory.yfilter != YFilter.not_set or
                        self.process_rate.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "throttle" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory.is_set or self.memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory.get_name_leafdata())
                    if (self.process_rate.is_set or self.process_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.process_rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory" or name == "process-rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory"):
                        self.memory = value
                        self.memory.value_namespace = name_space
                        self.memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "process-rate"):
                        self.process_rate = value
                        self.process_rate.value_namespace = name_space
                        self.process_rate.value_namespace_prefix = name_space_prefix


            class Vrfs(Entity):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	A specific VRF
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Default.Vrfs.Vrf>`
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Default.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "default"

                    self.vrf = YList(self)

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
                                super(XrXml.Agent.Default.Vrfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Default.Vrfs, self).__setattr__(name, value)


                class Vrf(Entity):
                    """
                    A specific VRF
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: access_list
                    
                    	Access list for XML agent
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv4_access_list
                    
                    	IPv4 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	IPv6 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: shutdown
                    
                    	Shutdown default VRF. This is applicable only for VRF default
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(XrXml.Agent.Default.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.access_list = YLeaf(YType.str, "access-list")

                        self.ipv4_access_list = YLeaf(YType.str, "ipv4-access-list")

                        self.ipv6_access_list = YLeaf(YType.str, "ipv6-access-list")

                        self.shutdown = YLeaf(YType.empty, "shutdown")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name",
                                        "access_list",
                                        "ipv4_access_list",
                                        "ipv6_access_list",
                                        "shutdown") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(XrXml.Agent.Default.Vrfs.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(XrXml.Agent.Default.Vrfs.Vrf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            self.access_list.is_set or
                            self.ipv4_access_list.is_set or
                            self.ipv6_access_list.is_set or
                            self.shutdown.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.access_list.yfilter != YFilter.not_set or
                            self.ipv4_access_list.yfilter != YFilter.not_set or
                            self.ipv6_access_list.yfilter != YFilter.not_set or
                            self.shutdown.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/vrfs/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.access_list.is_set or self.access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list.get_name_leafdata())
                        if (self.ipv4_access_list.is_set or self.ipv4_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_access_list.get_name_leafdata())
                        if (self.ipv6_access_list.is_set or self.ipv6_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_access_list.get_name_leafdata())
                        if (self.shutdown.is_set or self.shutdown.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shutdown.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf-name" or name == "access-list" or name == "ipv4-access-list" or name == "ipv6-access-list" or name == "shutdown"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-list"):
                            self.access_list = value
                            self.access_list.value_namespace = name_space
                            self.access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-access-list"):
                            self.ipv4_access_list = value
                            self.ipv4_access_list.value_namespace = name_space
                            self.ipv4_access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-access-list"):
                            self.ipv6_access_list = value
                            self.ipv6_access_list.value_namespace = name_space
                            self.ipv6_access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "shutdown"):
                            self.shutdown = value
                            self.shutdown.value_namespace = name_space
                            self.shutdown.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrfs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/default/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = XrXml.Agent.Default.Vrfs.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.enable.is_set or
                    self.ipv4_disable.is_set or
                    self.ipv6_enable.is_set or
                    self.iteration_size.is_set or
                    self.streaming_size.is_set or
                    (self.session is not None and self.session.has_data()) or
                    (self.throttle is not None and self.throttle.has_data()) or
                    (self.vrfs is not None and self.vrfs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.ipv4_disable.yfilter != YFilter.not_set or
                    self.ipv6_enable.yfilter != YFilter.not_set or
                    self.iteration_size.yfilter != YFilter.not_set or
                    self.streaming_size.yfilter != YFilter.not_set or
                    (self.session is not None and self.session.has_operation()) or
                    (self.throttle is not None and self.throttle.has_operation()) or
                    (self.vrfs is not None and self.vrfs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "default" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.ipv4_disable.is_set or self.ipv4_disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv4_disable.get_name_leafdata())
                if (self.ipv6_enable.is_set or self.ipv6_enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6_enable.get_name_leafdata())
                if (self.iteration_size.is_set or self.iteration_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iteration_size.get_name_leafdata())
                if (self.streaming_size.is_set or self.streaming_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.streaming_size.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "session"):
                    if (self.session is None):
                        self.session = XrXml.Agent.Default.Session()
                        self.session.parent = self
                        self._children_name_map["session"] = "session"
                    return self.session

                if (child_yang_name == "throttle"):
                    if (self.throttle is None):
                        self.throttle = XrXml.Agent.Default.Throttle()
                        self.throttle.parent = self
                        self._children_name_map["throttle"] = "throttle"
                    return self.throttle

                if (child_yang_name == "vrfs"):
                    if (self.vrfs is None):
                        self.vrfs = XrXml.Agent.Default.Vrfs()
                        self.vrfs.parent = self
                        self._children_name_map["vrfs"] = "vrfs"
                    return self.vrfs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "session" or name == "throttle" or name == "vrfs" or name == "enable" or name == "ipv4-disable" or name == "ipv6-enable" or name == "iteration-size" or name == "streaming-size"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv4-disable"):
                    self.ipv4_disable = value
                    self.ipv4_disable.value_namespace = name_space
                    self.ipv4_disable.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6-enable"):
                    self.ipv6_enable = value
                    self.ipv6_enable.value_namespace = name_space
                    self.ipv6_enable.value_namespace_prefix = name_space_prefix
                if(value_path == "iteration-size"):
                    self.iteration_size = value
                    self.iteration_size.value_namespace = name_space
                    self.iteration_size.value_namespace_prefix = name_space_prefix
                if(value_path == "streaming-size"):
                    self.streaming_size = value
                    self.streaming_size.value_namespace = name_space
                    self.streaming_size.value_namespace_prefix = name_space_prefix


        class Tty(Entity):
            """
            XML TTY agent
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\:  int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty.Session>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\:  int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Tty.Throttle>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"

                self.enable = YLeaf(YType.empty, "enable")

                self.iteration_size = YLeaf(YType.uint32, "iteration-size")

                self.streaming_size = YLeaf(YType.uint32, "streaming-size")

                self.session = XrXml.Agent.Tty.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")

                self.throttle = XrXml.Agent.Tty.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"
                self._children_yang_names.add("throttle")

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
                                "iteration_size",
                                "streaming_size") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(XrXml.Agent.Tty, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(XrXml.Agent.Tty, self).__setattr__(name, value)


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Tty.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "tty"

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
                        if name in ("timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(XrXml.Agent.Tty.Session, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Tty.Session, self).__setattr__(name, value)

                def has_data(self):
                    return self.timeout.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "session" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/tty/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
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
                    if(name == "timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix


            class Throttle(Entity):
                """
                XML agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Tty.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "tty"

                    self.memory = YLeaf(YType.uint32, "memory")

                    self.process_rate = YLeaf(YType.uint32, "process-rate")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory",
                                    "process_rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(XrXml.Agent.Tty.Throttle, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Tty.Throttle, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory.is_set or
                        self.process_rate.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory.yfilter != YFilter.not_set or
                        self.process_rate.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "throttle" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/tty/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory.is_set or self.memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory.get_name_leafdata())
                    if (self.process_rate.is_set or self.process_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.process_rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory" or name == "process-rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory"):
                        self.memory = value
                        self.memory.value_namespace = name_space
                        self.memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "process-rate"):
                        self.process_rate = value
                        self.process_rate.value_namespace = name_space
                        self.process_rate.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enable.is_set or
                    self.iteration_size.is_set or
                    self.streaming_size.is_set or
                    (self.session is not None and self.session.has_data()) or
                    (self.throttle is not None and self.throttle.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.iteration_size.yfilter != YFilter.not_set or
                    self.streaming_size.yfilter != YFilter.not_set or
                    (self.session is not None and self.session.has_operation()) or
                    (self.throttle is not None and self.throttle.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tty" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.iteration_size.is_set or self.iteration_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iteration_size.get_name_leafdata())
                if (self.streaming_size.is_set or self.streaming_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.streaming_size.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "session"):
                    if (self.session is None):
                        self.session = XrXml.Agent.Tty.Session()
                        self.session.parent = self
                        self._children_name_map["session"] = "session"
                    return self.session

                if (child_yang_name == "throttle"):
                    if (self.throttle is None):
                        self.throttle = XrXml.Agent.Tty.Throttle()
                        self.throttle.parent = self
                        self._children_name_map["throttle"] = "throttle"
                    return self.throttle

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "session" or name == "throttle" or name == "enable" or name == "iteration-size" or name == "streaming-size"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "iteration-size"):
                    self.iteration_size = value
                    self.iteration_size.value_namespace = name_space
                    self.iteration_size.value_namespace_prefix = name_space_prefix
                if(value_path == "streaming-size"):
                    self.streaming_size = value
                    self.streaming_size.value_namespace = name_space
                    self.streaming_size.value_namespace_prefix = name_space_prefix


        class Ssl(Entity):
            """
            XML SSL agent
            
            .. attribute:: enable
            
            	Enable specified XML agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: iteration_size
            
            	Iterator size, in KBytes, of the XML response. Specify 0 to turn off the XML response iterator
            	**type**\:  int
            
            	**range:** 0..100000
            
            	**units**\: kilobyte
            
            	**default value**\: 48
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Session>`
            
            .. attribute:: streaming_size
            
            	Streaming size, in KBytes, of the XML response
            	**type**\:  int
            
            	**range:** 1..100000
            
            	**units**\: kilobyte
            
            .. attribute:: throttle
            
            	XML agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Throttle>`
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Vrfs>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(XrXml.Agent.Ssl, self).__init__()

                self.yang_name = "ssl"
                self.yang_parent_name = "agent"

                self.enable = YLeaf(YType.empty, "enable")

                self.iteration_size = YLeaf(YType.uint32, "iteration-size")

                self.streaming_size = YLeaf(YType.uint32, "streaming-size")

                self.session = XrXml.Agent.Ssl.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")

                self.throttle = XrXml.Agent.Ssl.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"
                self._children_yang_names.add("throttle")

                self.vrfs = XrXml.Agent.Ssl.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
                self._children_yang_names.add("vrfs")

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
                                "iteration_size",
                                "streaming_size") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(XrXml.Agent.Ssl, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(XrXml.Agent.Ssl, self).__setattr__(name, value)


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "ssl"

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
                        if name in ("timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(XrXml.Agent.Ssl.Session, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Ssl.Session, self).__setattr__(name, value)

                def has_data(self):
                    return self.timeout.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "session" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
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
                    if(name == "timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix


            class Throttle(Entity):
                """
                XML agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "ssl"

                    self.memory = YLeaf(YType.uint32, "memory")

                    self.process_rate = YLeaf(YType.uint32, "process-rate")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory",
                                    "process_rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(XrXml.Agent.Ssl.Throttle, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Ssl.Throttle, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory.is_set or
                        self.process_rate.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory.yfilter != YFilter.not_set or
                        self.process_rate.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "throttle" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory.is_set or self.memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory.get_name_leafdata())
                    if (self.process_rate.is_set or self.process_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.process_rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory" or name == "process-rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory"):
                        self.memory = value
                        self.memory.value_namespace = name_space
                        self.memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "process-rate"):
                        self.process_rate = value
                        self.process_rate.value_namespace = name_space
                        self.process_rate.value_namespace_prefix = name_space_prefix


            class Vrfs(Entity):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	A specific VRF
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.XrXml.Agent.Ssl.Vrfs.Vrf>`
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(XrXml.Agent.Ssl.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "ssl"

                    self.vrf = YList(self)

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
                                super(XrXml.Agent.Ssl.Vrfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(XrXml.Agent.Ssl.Vrfs, self).__setattr__(name, value)


                class Vrf(Entity):
                    """
                    A specific VRF
                    
                    .. attribute:: vrf_name  <key>
                    
                    	VRF name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: access_list
                    
                    	Access list for XML agent
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv4_access_list
                    
                    	IPv4 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: ipv6_access_list
                    
                    	IPv6 Transport Access list for VRF
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: shutdown
                    
                    	Shutdown default VRF. This is applicable only for VRF default
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'man-xml-ttyagent-cfg'
                    _revision = '2015-07-30'

                    def __init__(self):
                        super(XrXml.Agent.Ssl.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.access_list = YLeaf(YType.str, "access-list")

                        self.ipv4_access_list = YLeaf(YType.str, "ipv4-access-list")

                        self.ipv6_access_list = YLeaf(YType.str, "ipv6-access-list")

                        self.shutdown = YLeaf(YType.empty, "shutdown")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name",
                                        "access_list",
                                        "ipv4_access_list",
                                        "ipv6_access_list",
                                        "shutdown") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(XrXml.Agent.Ssl.Vrfs.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(XrXml.Agent.Ssl.Vrfs.Vrf, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            self.access_list.is_set or
                            self.ipv4_access_list.is_set or
                            self.ipv6_access_list.is_set or
                            self.shutdown.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.access_list.yfilter != YFilter.not_set or
                            self.ipv4_access_list.yfilter != YFilter.not_set or
                            self.ipv6_access_list.yfilter != YFilter.not_set or
                            self.shutdown.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/vrfs/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.access_list.is_set or self.access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.access_list.get_name_leafdata())
                        if (self.ipv4_access_list.is_set or self.ipv4_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_access_list.get_name_leafdata())
                        if (self.ipv6_access_list.is_set or self.ipv6_access_list.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_access_list.get_name_leafdata())
                        if (self.shutdown.is_set or self.shutdown.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shutdown.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "vrf-name" or name == "access-list" or name == "ipv4-access-list" or name == "ipv6-access-list" or name == "shutdown"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "access-list"):
                            self.access_list = value
                            self.access_list.value_namespace = name_space
                            self.access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-access-list"):
                            self.ipv4_access_list = value
                            self.ipv4_access_list.value_namespace = name_space
                            self.ipv4_access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-access-list"):
                            self.ipv6_access_list = value
                            self.ipv6_access_list.value_namespace = name_space
                            self.ipv6_access_list.value_namespace_prefix = name_space_prefix
                        if(value_path == "shutdown"):
                            self.shutdown = value
                            self.shutdown.value_namespace = name_space
                            self.shutdown.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrfs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/ssl/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = XrXml.Agent.Ssl.Vrfs.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.enable.is_set or
                    self.iteration_size.is_set or
                    self.streaming_size.is_set or
                    (self.session is not None and self.session.has_data()) or
                    (self.throttle is not None and self.throttle.has_data()) or
                    (self.vrfs is not None and self.vrfs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.iteration_size.yfilter != YFilter.not_set or
                    self.streaming_size.yfilter != YFilter.not_set or
                    (self.session is not None and self.session.has_operation()) or
                    (self.throttle is not None and self.throttle.has_operation()) or
                    (self.vrfs is not None and self.vrfs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ssl" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/agent/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.iteration_size.is_set or self.iteration_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.iteration_size.get_name_leafdata())
                if (self.streaming_size.is_set or self.streaming_size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.streaming_size.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "session"):
                    if (self.session is None):
                        self.session = XrXml.Agent.Ssl.Session()
                        self.session.parent = self
                        self._children_name_map["session"] = "session"
                    return self.session

                if (child_yang_name == "throttle"):
                    if (self.throttle is None):
                        self.throttle = XrXml.Agent.Ssl.Throttle()
                        self.throttle.parent = self
                        self._children_name_map["throttle"] = "throttle"
                    return self.throttle

                if (child_yang_name == "vrfs"):
                    if (self.vrfs is None):
                        self.vrfs = XrXml.Agent.Ssl.Vrfs()
                        self.vrfs.parent = self
                        self._children_name_map["vrfs"] = "vrfs"
                    return self.vrfs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "session" or name == "throttle" or name == "vrfs" or name == "enable" or name == "iteration-size" or name == "streaming-size"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "iteration-size"):
                    self.iteration_size = value
                    self.iteration_size.value_namespace = name_space
                    self.iteration_size.value_namespace_prefix = name_space_prefix
                if(value_path == "streaming-size"):
                    self.streaming_size = value
                    self.streaming_size.value_namespace = name_space
                    self.streaming_size.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml/%s" % self.get_segment_path()
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
        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:xr-xml" + path_buffer

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

class Netconf(Entity):
    """
    netconf
    
    .. attribute:: agent
    
    	XML agent
    	**type**\:   :py:class:`Agent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent>`
    
    

    """

    _prefix = 'man-xml-ttyagent-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(Netconf, self).__init__()
        self._top_entity = None

        self.yang_name = "netconf"
        self.yang_parent_name = "Cisco-IOS-XR-man-xml-ttyagent-cfg"

        self.agent = Netconf.Agent()
        self.agent.parent = self
        self._children_name_map["agent"] = "agent"
        self._children_yang_names.add("agent")


    class Agent(Entity):
        """
        XML agent
        
        .. attribute:: tty
        
        	NETCONF agent over TTY
        	**type**\:   :py:class:`Tty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty>`
        
        

        """

        _prefix = 'man-xml-ttyagent-cfg'
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
            
            .. attribute:: enable
            
            	Enable specified NETCONF agent
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: session
            
            	Session attributes
            	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty.Session>`
            
            .. attribute:: throttle
            
            	NETCONF agent throttling
            	**type**\:   :py:class:`Throttle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_cfg.Netconf.Agent.Tty.Throttle>`
            
            

            """

            _prefix = 'man-xml-ttyagent-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(Netconf.Agent.Tty, self).__init__()

                self.yang_name = "tty"
                self.yang_parent_name = "agent"

                self.enable = YLeaf(YType.empty, "enable")

                self.session = Netconf.Agent.Tty.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")

                self.throttle = Netconf.Agent.Tty.Throttle()
                self.throttle.parent = self
                self._children_name_map["throttle"] = "throttle"
                self._children_yang_names.add("throttle")

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
                            super(Netconf.Agent.Tty, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Netconf.Agent.Tty, self).__setattr__(name, value)


            class Throttle(Entity):
                """
                NETCONF agent throttling
                
                .. attribute:: memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 100..600
                
                	**units**\: megabyte
                
                	**default value**\: 300
                
                .. attribute:: offload_memory
                
                	Size of memory usage, in MBytes, per session
                	**type**\:  int
                
                	**range:** 0..12000
                
                	**units**\: megabyte
                
                	**default value**\: 0
                
                .. attribute:: process_rate
                
                	Process rate in number of XML tags per second
                	**type**\:  int
                
                	**range:** 1000..30000
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Netconf.Agent.Tty.Throttle, self).__init__()

                    self.yang_name = "throttle"
                    self.yang_parent_name = "tty"

                    self.memory = YLeaf(YType.uint32, "memory")

                    self.offload_memory = YLeaf(YType.uint32, "offload-memory")

                    self.process_rate = YLeaf(YType.uint32, "process-rate")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory",
                                    "offload_memory",
                                    "process_rate") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Netconf.Agent.Tty.Throttle, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Netconf.Agent.Tty.Throttle, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory.is_set or
                        self.offload_memory.is_set or
                        self.process_rate.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory.yfilter != YFilter.not_set or
                        self.offload_memory.yfilter != YFilter.not_set or
                        self.process_rate.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "throttle" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/agent/tty/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory.is_set or self.memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory.get_name_leafdata())
                    if (self.offload_memory.is_set or self.offload_memory.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.offload_memory.get_name_leafdata())
                    if (self.process_rate.is_set or self.process_rate.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.process_rate.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory" or name == "offload-memory" or name == "process-rate"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory"):
                        self.memory = value
                        self.memory.value_namespace = name_space
                        self.memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "offload-memory"):
                        self.offload_memory = value
                        self.offload_memory.value_namespace = name_space
                        self.offload_memory.value_namespace_prefix = name_space_prefix
                    if(value_path == "process-rate"):
                        self.process_rate = value
                        self.process_rate.value_namespace = name_space
                        self.process_rate.value_namespace_prefix = name_space_prefix


            class Session(Entity):
                """
                Session attributes
                
                .. attribute:: timeout
                
                	Timeout in minutes
                	**type**\:  int
                
                	**range:** 1..1440
                
                	**units**\: minute
                
                

                """

                _prefix = 'man-xml-ttyagent-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(Netconf.Agent.Tty.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "tty"

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
                        if name in ("timeout") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Netconf.Agent.Tty.Session, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Netconf.Agent.Tty.Session, self).__setattr__(name, value)

                def has_data(self):
                    return self.timeout.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "session" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/agent/tty/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
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
                    if(name == "timeout"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.enable.is_set or
                    (self.session is not None and self.session.has_data()) or
                    (self.throttle is not None and self.throttle.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.session is not None and self.session.has_operation()) or
                    (self.throttle is not None and self.throttle.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "tty" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/agent/%s" % self.get_segment_path()
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

                if (child_yang_name == "session"):
                    if (self.session is None):
                        self.session = Netconf.Agent.Tty.Session()
                        self.session.parent = self
                        self._children_name_map["session"] = "session"
                    return self.session

                if (child_yang_name == "throttle"):
                    if (self.throttle is None):
                        self.throttle = Netconf.Agent.Tty.Throttle()
                        self.throttle.parent = self
                        self._children_name_map["throttle"] = "throttle"
                    return self.throttle

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "session" or name == "throttle" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf/%s" % self.get_segment_path()
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
        path_buffer = "Cisco-IOS-XR-man-xml-ttyagent-cfg:netconf" + path_buffer

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

