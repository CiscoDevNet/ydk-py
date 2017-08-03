""" Cisco_IOS_XR_infra_rcmd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rcmd package configuration.

This module contains definitions
for the following management objects\:
  router\-convergence\: Configure Router Convergence Monitoring

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ProtocolName(Enum):
    """
    ProtocolName

    Protocol name

    .. data:: ospf = 0

    	Configure parameters related to OSPF

    .. data:: isis = 1

    	Configure parameters related to ISIS

    """

    ospf = Enum.YLeaf(0, "ospf")

    isis = Enum.YLeaf(1, "isis")


class RcmdPriority(Enum):
    """
    RcmdPriority

    Rcmd priority

    .. data:: critical = 0

    	Critical routes

    .. data:: high = 1

    	High priority routes

    .. data:: medium = 2

    	Medium priority routes

    .. data:: low = 3

    	Low priority routes

    """

    critical = Enum.YLeaf(0, "critical")

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")



class RouterConvergence(Entity):
    """
    Configure Router Convergence Monitoring
    
    .. attribute:: collect_diagnostics
    
    	Table of CollectDiagnostics
    	**type**\:   :py:class:`CollectDiagnostics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.CollectDiagnostics>`
    
    .. attribute:: disable
    
    	Disable the monitoring of route convergence on the entire router
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable Configure Router Convergence Monitoring. Deletion of this object also causes deletion of all associated objects under RouterConvergence
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: event_buffer_size
    
    	Event buffer size for storing event traces (as number of events)
    	**type**\:  int
    
    	**range:** 100..500
    
    .. attribute:: max_events_stored
    
    	Maximum number of events stored in the server
    	**type**\:  int
    
    	**range:** 10..500
    
    .. attribute:: monitoring_interval
    
    	Interval in which to collect logs (in mins)
    	**type**\:  int
    
    	**range:** 5..120
    
    	**units**\: minute
    
    .. attribute:: mpls_ldp
    
    	RCMD related configuration for MPLS\-LDP
    	**type**\:   :py:class:`MplsLdp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.MplsLdp>`
    
    	**presence node**\: True
    
    .. attribute:: nodes
    
    	Table of Node
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Nodes>`
    
    .. attribute:: prefix_monitor_limit
    
    	Limits Individual Prefix Monitoring
    	**type**\:  int
    
    	**range:** 0..100
    
    .. attribute:: protocols
    
    	Table of Protocol
    	**type**\:   :py:class:`Protocols <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols>`
    
    .. attribute:: storage_location
    
    	Absolute directory path for saving the archive files. Example /disk0\:/rcmd/ or <tftp\-location>/rcmd/
    	**type**\:   :py:class:`StorageLocation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.StorageLocation>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'infra-rcmd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(RouterConvergence, self).__init__()
        self._top_entity = None

        self.yang_name = "router-convergence"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rcmd-cfg"

        self.disable = YLeaf(YType.empty, "disable")

        self.enable = YLeaf(YType.empty, "enable")

        self.event_buffer_size = YLeaf(YType.uint32, "event-buffer-size")

        self.max_events_stored = YLeaf(YType.uint32, "max-events-stored")

        self.monitoring_interval = YLeaf(YType.uint32, "monitoring-interval")

        self.prefix_monitor_limit = YLeaf(YType.uint32, "prefix-monitor-limit")

        self.collect_diagnostics = RouterConvergence.CollectDiagnostics()
        self.collect_diagnostics.parent = self
        self._children_name_map["collect_diagnostics"] = "collect-diagnostics"
        self._children_yang_names.add("collect-diagnostics")

        self.mpls_ldp = None
        self._children_name_map["mpls_ldp"] = "mpls-ldp"
        self._children_yang_names.add("mpls-ldp")

        self.nodes = RouterConvergence.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.protocols = RouterConvergence.Protocols()
        self.protocols.parent = self
        self._children_name_map["protocols"] = "protocols"
        self._children_yang_names.add("protocols")

        self.storage_location = None
        self._children_name_map["storage_location"] = "storage-location"
        self._children_yang_names.add("storage-location")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("disable",
                        "enable",
                        "event_buffer_size",
                        "max_events_stored",
                        "monitoring_interval",
                        "prefix_monitor_limit") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(RouterConvergence, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(RouterConvergence, self).__setattr__(name, value)


    class Protocols(Entity):
        """
        Table of Protocol
        
        .. attribute:: protocol
        
        	Protocol for which to configure RCMD parameters
        	**type**\: list of    :py:class:`Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(RouterConvergence.Protocols, self).__init__()

            self.yang_name = "protocols"
            self.yang_parent_name = "router-convergence"

            self.protocol = YList(self)

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
                        super(RouterConvergence.Protocols, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RouterConvergence.Protocols, self).__setattr__(name, value)


        class Protocol(Entity):
            """
            Protocol for which to configure RCMD parameters
            
            .. attribute:: protocol_name  <key>
            
            	Specify the protocol
            	**type**\:   :py:class:`ProtocolName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.ProtocolName>`
            
            .. attribute:: enable
            
            	Enable Protocol for which to configure RCMD parameters. Deletion of this object also causes deletion of all associated objects under Protocol
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: priorities
            
            	Table of Priority
            	**type**\:   :py:class:`Priorities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol.Priorities>`
            
            

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(RouterConvergence.Protocols.Protocol, self).__init__()

                self.yang_name = "protocol"
                self.yang_parent_name = "protocols"

                self.protocol_name = YLeaf(YType.enumeration, "protocol-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.priorities = RouterConvergence.Protocols.Protocol.Priorities()
                self.priorities.parent = self
                self._children_name_map["priorities"] = "priorities"
                self._children_yang_names.add("priorities")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("protocol_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RouterConvergence.Protocols.Protocol, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RouterConvergence.Protocols.Protocol, self).__setattr__(name, value)


            class Priorities(Entity):
                """
                Table of Priority
                
                .. attribute:: priority
                
                	Priority
                	**type**\: list of    :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Protocols.Protocol.Priorities.Priority>`
                
                

                """

                _prefix = 'infra-rcmd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(RouterConvergence.Protocols.Protocol.Priorities, self).__init__()

                    self.yang_name = "priorities"
                    self.yang_parent_name = "protocol"

                    self.priority = YList(self)

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
                                super(RouterConvergence.Protocols.Protocol.Priorities, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(RouterConvergence.Protocols.Protocol.Priorities, self).__setattr__(name, value)


                class Priority(Entity):
                    """
                    Priority
                    
                    .. attribute:: rcmd_priority  <key>
                    
                    	Specify the priority
                    	**type**\:   :py:class:`RcmdPriority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RcmdPriority>`
                    
                    .. attribute:: disable
                    
                    	Disables the monitoring of route convergence for specified priority
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Enable Priority. Deletion of this object also causes deletion of all associated objects under Priority
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: frr_threshold
                    
                    	Threshold value for Fast ReRoute Coverage (in percentage)
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    	**units**\: percentage
                    
                    .. attribute:: leaf_networks
                    
                    	Specify the maximum number of leaf networks monitored
                    	**type**\:  int
                    
                    	**range:** 10..100
                    
                    .. attribute:: threshold
                    
                    	Threshold value for convergence (in msec)
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'infra-rcmd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(RouterConvergence.Protocols.Protocol.Priorities.Priority, self).__init__()

                        self.yang_name = "priority"
                        self.yang_parent_name = "priorities"

                        self.rcmd_priority = YLeaf(YType.enumeration, "rcmd-priority")

                        self.disable = YLeaf(YType.empty, "disable")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.frr_threshold = YLeaf(YType.uint32, "frr-threshold")

                        self.leaf_networks = YLeaf(YType.uint32, "leaf-networks")

                        self.threshold = YLeaf(YType.int32, "threshold")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("rcmd_priority",
                                        "disable",
                                        "enable",
                                        "frr_threshold",
                                        "leaf_networks",
                                        "threshold") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(RouterConvergence.Protocols.Protocol.Priorities.Priority, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(RouterConvergence.Protocols.Protocol.Priorities.Priority, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.rcmd_priority.is_set or
                            self.disable.is_set or
                            self.enable.is_set or
                            self.frr_threshold.is_set or
                            self.leaf_networks.is_set or
                            self.threshold.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.rcmd_priority.yfilter != YFilter.not_set or
                            self.disable.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            self.frr_threshold.yfilter != YFilter.not_set or
                            self.leaf_networks.yfilter != YFilter.not_set or
                            self.threshold.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "priority" + "[rcmd-priority='" + self.rcmd_priority.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.rcmd_priority.is_set or self.rcmd_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rcmd_priority.get_name_leafdata())
                        if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disable.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())
                        if (self.frr_threshold.is_set or self.frr_threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.frr_threshold.get_name_leafdata())
                        if (self.leaf_networks.is_set or self.leaf_networks.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.leaf_networks.get_name_leafdata())
                        if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rcmd-priority" or name == "disable" or name == "enable" or name == "frr-threshold" or name == "leaf-networks" or name == "threshold"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "rcmd-priority"):
                            self.rcmd_priority = value
                            self.rcmd_priority.value_namespace = name_space
                            self.rcmd_priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "disable"):
                            self.disable = value
                            self.disable.value_namespace = name_space
                            self.disable.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix
                        if(value_path == "frr-threshold"):
                            self.frr_threshold = value
                            self.frr_threshold.value_namespace = name_space
                            self.frr_threshold.value_namespace_prefix = name_space_prefix
                        if(value_path == "leaf-networks"):
                            self.leaf_networks = value
                            self.leaf_networks.value_namespace = name_space
                            self.leaf_networks.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold"):
                            self.threshold = value
                            self.threshold.value_namespace = name_space
                            self.threshold.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.priority:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.priority:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "priorities" + path_buffer

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

                    if (child_yang_name == "priority"):
                        for c in self.priority:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = RouterConvergence.Protocols.Protocol.Priorities.Priority()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.priority.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "priority"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.protocol_name.is_set or
                    self.enable.is_set or
                    (self.priorities is not None and self.priorities.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.protocol_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.priorities is not None and self.priorities.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "protocol" + "[protocol-name='" + self.protocol_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/protocols/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.protocol_name.is_set or self.protocol_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.protocol_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "priorities"):
                    if (self.priorities is None):
                        self.priorities = RouterConvergence.Protocols.Protocol.Priorities()
                        self.priorities.parent = self
                        self._children_name_map["priorities"] = "priorities"
                    return self.priorities

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "priorities" or name == "protocol-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "protocol-name"):
                    self.protocol_name = value
                    self.protocol_name.value_namespace = name_space
                    self.protocol_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.protocol:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.protocol:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "protocols" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "protocol"):
                for c in self.protocol:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RouterConvergence.Protocols.Protocol()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.protocol.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "protocol"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class StorageLocation(Entity):
        """
        Absolute directory path for saving the archive
        files. Example /disk0\:/rcmd/ or
        <tftp\-location>/rcmd/
        
        .. attribute:: diagnostics
        
        	Absolute directory path for storing diagnostic reports. Example /disk0\:/rcmd/ or <tftp\-location>/rcmd/
        	**type**\:  str
        
        .. attribute:: diagnostics_size
        
        	Maximum size of diagnostics dir (5% \- 80%) for local storage
        	**type**\:  int
        
        	**range:** 5..80
        
        .. attribute:: reports
        
        	Absolute directory path for storing reports. Example /disk0\:/rcmd/ or <tftp\-location>/rcmd/
        	**type**\:  str
        
        .. attribute:: reports_size
        
        	Maximum size of reports dir (5% \- 80%) for local storage
        	**type**\:  int
        
        	**range:** 5..80
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(RouterConvergence.StorageLocation, self).__init__()

            self.yang_name = "storage-location"
            self.yang_parent_name = "router-convergence"
            self.is_presence_container = True

            self.diagnostics = YLeaf(YType.str, "diagnostics")

            self.diagnostics_size = YLeaf(YType.uint32, "diagnostics-size")

            self.reports = YLeaf(YType.str, "reports")

            self.reports_size = YLeaf(YType.uint32, "reports-size")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("diagnostics",
                            "diagnostics_size",
                            "reports",
                            "reports_size") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RouterConvergence.StorageLocation, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RouterConvergence.StorageLocation, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.diagnostics.is_set or
                self.diagnostics_size.is_set or
                self.reports.is_set or
                self.reports_size.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.diagnostics.yfilter != YFilter.not_set or
                self.diagnostics_size.yfilter != YFilter.not_set or
                self.reports.yfilter != YFilter.not_set or
                self.reports_size.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "storage-location" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.diagnostics.is_set or self.diagnostics.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diagnostics.get_name_leafdata())
            if (self.diagnostics_size.is_set or self.diagnostics_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.diagnostics_size.get_name_leafdata())
            if (self.reports.is_set or self.reports.yfilter != YFilter.not_set):
                leaf_name_data.append(self.reports.get_name_leafdata())
            if (self.reports_size.is_set or self.reports_size.yfilter != YFilter.not_set):
                leaf_name_data.append(self.reports_size.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "diagnostics" or name == "diagnostics-size" or name == "reports" or name == "reports-size"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "diagnostics"):
                self.diagnostics = value
                self.diagnostics.value_namespace = name_space
                self.diagnostics.value_namespace_prefix = name_space_prefix
            if(value_path == "diagnostics-size"):
                self.diagnostics_size = value
                self.diagnostics_size.value_namespace = name_space
                self.diagnostics_size.value_namespace_prefix = name_space_prefix
            if(value_path == "reports"):
                self.reports = value
                self.reports.value_namespace = name_space
                self.reports.value_namespace_prefix = name_space_prefix
            if(value_path == "reports-size"):
                self.reports_size = value
                self.reports_size.value_namespace = name_space
                self.reports_size.value_namespace_prefix = name_space_prefix


    class MplsLdp(Entity):
        """
        RCMD related configuration for MPLS\-LDP
        
        .. attribute:: remote_lfa
        
        	Monitoring configuration for Remote LFA
        	**type**\:   :py:class:`RemoteLfa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.MplsLdp.RemoteLfa>`
        
        	**presence node**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(RouterConvergence.MplsLdp, self).__init__()

            self.yang_name = "mpls-ldp"
            self.yang_parent_name = "router-convergence"
            self.is_presence_container = True

            self.remote_lfa = None
            self._children_name_map["remote_lfa"] = "remote-lfa"
            self._children_yang_names.add("remote-lfa")


        class RemoteLfa(Entity):
            """
            Monitoring configuration for Remote LFA
            
            .. attribute:: threshold
            
            	Threshold value for label coverage (in percentage)
            	**type**\:  int
            
            	**range:** 1..100
            
            	**units**\: percentage
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(RouterConvergence.MplsLdp.RemoteLfa, self).__init__()

                self.yang_name = "remote-lfa"
                self.yang_parent_name = "mpls-ldp"
                self.is_presence_container = True

                self.threshold = YLeaf(YType.uint32, "threshold")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("threshold") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RouterConvergence.MplsLdp.RemoteLfa, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RouterConvergence.MplsLdp.RemoteLfa, self).__setattr__(name, value)

            def has_data(self):
                return self.threshold.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.threshold.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "remote-lfa" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/mpls-ldp/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.threshold.is_set or self.threshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.threshold.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "threshold"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "threshold"):
                    self.threshold = value
                    self.threshold.value_namespace = name_space
                    self.threshold.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.remote_lfa is not None)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.remote_lfa is not None and self.remote_lfa.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mpls-ldp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "remote-lfa"):
                if (self.remote_lfa is None):
                    self.remote_lfa = RouterConvergence.MplsLdp.RemoteLfa()
                    self.remote_lfa.parent = self
                    self._children_name_map["remote_lfa"] = "remote-lfa"
                return self.remote_lfa

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "remote-lfa"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class CollectDiagnostics(Entity):
        """
        Table of CollectDiagnostics
        
        .. attribute:: collect_diagnostic
        
        	Collect diagnostics on specified node
        	**type**\: list of    :py:class:`CollectDiagnostic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.CollectDiagnostics.CollectDiagnostic>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(RouterConvergence.CollectDiagnostics, self).__init__()

            self.yang_name = "collect-diagnostics"
            self.yang_parent_name = "router-convergence"

            self.collect_diagnostic = YList(self)

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
                        super(RouterConvergence.CollectDiagnostics, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RouterConvergence.CollectDiagnostics, self).__setattr__(name, value)


        class CollectDiagnostic(Entity):
            """
            Collect diagnostics on specified node
            
            .. attribute:: node_name  <key>
            
            	Specified location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: enable
            
            	Enables collection of diagnostics on the specified location
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(RouterConvergence.CollectDiagnostics.CollectDiagnostic, self).__init__()

                self.yang_name = "collect-diagnostic"
                self.yang_parent_name = "collect-diagnostics"

                self.node_name = YLeaf(YType.str, "node-name")

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
                    if name in ("node_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RouterConvergence.CollectDiagnostics.CollectDiagnostic, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RouterConvergence.CollectDiagnostics.CollectDiagnostic, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.node_name.is_set or
                    self.enable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "collect-diagnostic" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/collect-diagnostics/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())
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
                if(name == "node-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.collect_diagnostic:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.collect_diagnostic:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "collect-diagnostics" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "collect-diagnostic"):
                for c in self.collect_diagnostic:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RouterConvergence.CollectDiagnostics.CollectDiagnostic()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.collect_diagnostic.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "collect-diagnostic"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nodes(Entity):
        """
        Table of Node
        
        .. attribute:: node
        
        	Configure parameters for the specified node (Partially qualified location allowed)
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg.RouterConvergence.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rcmd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(RouterConvergence.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "router-convergence"

            self.node = YList(self)

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
                        super(RouterConvergence.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RouterConvergence.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Configure parameters for the specified node
            (Partially qualified location allowed)
            
            .. attribute:: node_name  <key>
            
            	Wildcard expression(eg. \*/\*/\*, R/\*/\*, R/S/\*, R/S/I)
            	**type**\:  str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
            
            .. attribute:: disable
            
            	Disables the monitoring of route convergence on specified location
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	Enable Configure parameters for the specified node (Partially qualified location allowed). Deletion of this object also causes deletion of all associated objects under Node
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rcmd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(RouterConvergence.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.disable = YLeaf(YType.empty, "disable")

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
                    if name in ("node_name",
                                "disable",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RouterConvergence.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RouterConvergence.Nodes.Node, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.node_name.is_set or
                    self.disable.is_set or
                    self.enable.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    self.disable.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())
                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable.get_name_leafdata())
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
                if(name == "node-name" or name == "disable" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix
                if(value_path == "disable"):
                    self.disable = value
                    self.disable.value_namespace = name_space
                    self.disable.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RouterConvergence.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.disable.is_set or
            self.enable.is_set or
            self.event_buffer_size.is_set or
            self.max_events_stored.is_set or
            self.monitoring_interval.is_set or
            self.prefix_monitor_limit.is_set or
            (self.collect_diagnostics is not None and self.collect_diagnostics.has_data()) or
            (self.nodes is not None and self.nodes.has_data()) or
            (self.protocols is not None and self.protocols.has_data()) or
            (self.mpls_ldp is not None) or
            (self.storage_location is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.disable.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.event_buffer_size.yfilter != YFilter.not_set or
            self.max_events_stored.yfilter != YFilter.not_set or
            self.monitoring_interval.yfilter != YFilter.not_set or
            self.prefix_monitor_limit.yfilter != YFilter.not_set or
            (self.collect_diagnostics is not None and self.collect_diagnostics.has_operation()) or
            (self.mpls_ldp is not None and self.mpls_ldp.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()) or
            (self.protocols is not None and self.protocols.has_operation()) or
            (self.storage_location is not None and self.storage_location.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rcmd-cfg:router-convergence" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.disable.get_name_leafdata())
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.event_buffer_size.is_set or self.event_buffer_size.yfilter != YFilter.not_set):
            leaf_name_data.append(self.event_buffer_size.get_name_leafdata())
        if (self.max_events_stored.is_set or self.max_events_stored.yfilter != YFilter.not_set):
            leaf_name_data.append(self.max_events_stored.get_name_leafdata())
        if (self.monitoring_interval.is_set or self.monitoring_interval.yfilter != YFilter.not_set):
            leaf_name_data.append(self.monitoring_interval.get_name_leafdata())
        if (self.prefix_monitor_limit.is_set or self.prefix_monitor_limit.yfilter != YFilter.not_set):
            leaf_name_data.append(self.prefix_monitor_limit.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "collect-diagnostics"):
            if (self.collect_diagnostics is None):
                self.collect_diagnostics = RouterConvergence.CollectDiagnostics()
                self.collect_diagnostics.parent = self
                self._children_name_map["collect_diagnostics"] = "collect-diagnostics"
            return self.collect_diagnostics

        if (child_yang_name == "mpls-ldp"):
            if (self.mpls_ldp is None):
                self.mpls_ldp = RouterConvergence.MplsLdp()
                self.mpls_ldp.parent = self
                self._children_name_map["mpls_ldp"] = "mpls-ldp"
            return self.mpls_ldp

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = RouterConvergence.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        if (child_yang_name == "protocols"):
            if (self.protocols is None):
                self.protocols = RouterConvergence.Protocols()
                self.protocols.parent = self
                self._children_name_map["protocols"] = "protocols"
            return self.protocols

        if (child_yang_name == "storage-location"):
            if (self.storage_location is None):
                self.storage_location = RouterConvergence.StorageLocation()
                self.storage_location.parent = self
                self._children_name_map["storage_location"] = "storage-location"
            return self.storage_location

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "collect-diagnostics" or name == "mpls-ldp" or name == "nodes" or name == "protocols" or name == "storage-location" or name == "disable" or name == "enable" or name == "event-buffer-size" or name == "max-events-stored" or name == "monitoring-interval" or name == "prefix-monitor-limit"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "disable"):
            self.disable = value
            self.disable.value_namespace = name_space
            self.disable.value_namespace_prefix = name_space_prefix
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "event-buffer-size"):
            self.event_buffer_size = value
            self.event_buffer_size.value_namespace = name_space
            self.event_buffer_size.value_namespace_prefix = name_space_prefix
        if(value_path == "max-events-stored"):
            self.max_events_stored = value
            self.max_events_stored.value_namespace = name_space
            self.max_events_stored.value_namespace_prefix = name_space_prefix
        if(value_path == "monitoring-interval"):
            self.monitoring_interval = value
            self.monitoring_interval.value_namespace = name_space
            self.monitoring_interval.value_namespace_prefix = name_space_prefix
        if(value_path == "prefix-monitor-limit"):
            self.prefix_monitor_limit = value
            self.prefix_monitor_limit.value_namespace = name_space
            self.prefix_monitor_limit.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = RouterConvergence()
        return self._top_entity

