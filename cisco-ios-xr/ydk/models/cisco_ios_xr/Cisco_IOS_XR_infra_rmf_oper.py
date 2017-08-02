""" Cisco_IOS_XR_infra_rmf_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rmf package operational data.

This module contains definitions
for the following management objects\:
  redundancy\: Redundancy show information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Redundancy(Entity):
    """
    Redundancy show information
    
    .. attribute:: nodes
    
    	Location show information
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes>`
    
    .. attribute:: summary
    
    	Redundancy Summary of Nodes
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary>`
    
    

    """

    _prefix = 'infra-rmf-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Redundancy, self).__init__()
        self._top_entity = None

        self.yang_name = "redundancy"
        self.yang_parent_name = "Cisco-IOS-XR-infra-rmf-oper"

        self.nodes = Redundancy.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.summary = Redundancy.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")


    class Nodes(Entity):
        """
        Location show information
        
        .. attribute:: node
        
        	Redundancy Node Information
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node>`
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Redundancy.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "redundancy"

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
                        super(Redundancy.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Redundancy.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Redundancy Node Information
            
            .. attribute:: node_id  <key>
            
            	Node Location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: active_reboot_reason
            
            	Active node reload
            	**type**\:  str
            
            .. attribute:: err_log
            
            	Error Log
            	**type**\:  str
            
            .. attribute:: log
            
            	Reload and boot logs
            	**type**\:  str
            
            .. attribute:: redundancy
            
            	Row information
            	**type**\:   :py:class:`Redundancy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy>`
            
            .. attribute:: standby_reboot_reason
            
            	Standby node reload
            	**type**\:  str
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Redundancy.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_id = YLeaf(YType.str, "node-id")

                self.active_reboot_reason = YLeaf(YType.str, "active-reboot-reason")

                self.err_log = YLeaf(YType.str, "err-log")

                self.log = YLeaf(YType.str, "log")

                self.standby_reboot_reason = YLeaf(YType.str, "standby-reboot-reason")

                self.redundancy = Redundancy.Nodes.Node.Redundancy()
                self.redundancy.parent = self
                self._children_name_map["redundancy"] = "redundancy"
                self._children_yang_names.add("redundancy")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_id",
                                "active_reboot_reason",
                                "err_log",
                                "log",
                                "standby_reboot_reason") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Redundancy.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Redundancy.Nodes.Node, self).__setattr__(name, value)


            class Redundancy(Entity):
                """
                Row information
                
                .. attribute:: active
                
                	Active node name R/S/I
                	**type**\:  str
                
                .. attribute:: groupinfo
                
                	groupinfo
                	**type**\: list of    :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Nodes.Node.Redundancy.Groupinfo>`
                
                .. attribute:: ha_state
                
                	High Availability state Ready/Not Ready
                	**type**\:  str
                
                .. attribute:: nsr_state
                
                	NSR state Configured/Not Configured
                	**type**\:  str
                
                .. attribute:: standby
                
                	Standby node name R/S/I
                	**type**\:  str
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Redundancy.Nodes.Node.Redundancy, self).__init__()

                    self.yang_name = "redundancy"
                    self.yang_parent_name = "node"

                    self.active = YLeaf(YType.str, "active")

                    self.ha_state = YLeaf(YType.str, "ha-state")

                    self.nsr_state = YLeaf(YType.str, "nsr-state")

                    self.standby = YLeaf(YType.str, "standby")

                    self.groupinfo = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "ha_state",
                                    "nsr_state",
                                    "standby") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Redundancy.Nodes.Node.Redundancy, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Redundancy.Nodes.Node.Redundancy, self).__setattr__(name, value)


                class Groupinfo(Entity):
                    """
                    groupinfo
                    
                    .. attribute:: active
                    
                    	Active
                    	**type**\:  str
                    
                    .. attribute:: ha_state
                    
                    	HAState
                    	**type**\:  str
                    
                    .. attribute:: nsr_state
                    
                    	NSRState
                    	**type**\:  str
                    
                    .. attribute:: standby
                    
                    	Standby
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'infra-rmf-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Redundancy.Nodes.Node.Redundancy.Groupinfo, self).__init__()

                        self.yang_name = "groupinfo"
                        self.yang_parent_name = "redundancy"

                        self.active = YLeaf(YType.str, "active")

                        self.ha_state = YLeaf(YType.str, "ha-state")

                        self.nsr_state = YLeaf(YType.str, "nsr-state")

                        self.standby = YLeaf(YType.str, "standby")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("active",
                                        "ha_state",
                                        "nsr_state",
                                        "standby") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Redundancy.Nodes.Node.Redundancy.Groupinfo, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Redundancy.Nodes.Node.Redundancy.Groupinfo, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.active.is_set or
                            self.ha_state.is_set or
                            self.nsr_state.is_set or
                            self.standby.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.active.yfilter != YFilter.not_set or
                            self.ha_state.yfilter != YFilter.not_set or
                            self.nsr_state.yfilter != YFilter.not_set or
                            self.standby.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "groupinfo" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.active.get_name_leafdata())
                        if (self.ha_state.is_set or self.ha_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ha_state.get_name_leafdata())
                        if (self.nsr_state.is_set or self.nsr_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nsr_state.get_name_leafdata())
                        if (self.standby.is_set or self.standby.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.standby.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "active" or name == "ha-state" or name == "nsr-state" or name == "standby"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "active"):
                            self.active = value
                            self.active.value_namespace = name_space
                            self.active.value_namespace_prefix = name_space_prefix
                        if(value_path == "ha-state"):
                            self.ha_state = value
                            self.ha_state.value_namespace = name_space
                            self.ha_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "nsr-state"):
                            self.nsr_state = value
                            self.nsr_state.value_namespace = name_space
                            self.nsr_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "standby"):
                            self.standby = value
                            self.standby.value_namespace = name_space
                            self.standby.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.groupinfo:
                        if (c.has_data()):
                            return True
                    return (
                        self.active.is_set or
                        self.ha_state.is_set or
                        self.nsr_state.is_set or
                        self.standby.is_set)

                def has_operation(self):
                    for c in self.groupinfo:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.ha_state.yfilter != YFilter.not_set or
                        self.nsr_state.yfilter != YFilter.not_set or
                        self.standby.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "redundancy" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.ha_state.is_set or self.ha_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ha_state.get_name_leafdata())
                    if (self.nsr_state.is_set or self.nsr_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nsr_state.get_name_leafdata())
                    if (self.standby.is_set or self.standby.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "groupinfo"):
                        for c in self.groupinfo:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Redundancy.Nodes.Node.Redundancy.Groupinfo()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.groupinfo.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "groupinfo" or name == "active" or name == "ha-state" or name == "nsr-state" or name == "standby"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "ha-state"):
                        self.ha_state = value
                        self.ha_state.value_namespace = name_space
                        self.ha_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "nsr-state"):
                        self.nsr_state = value
                        self.nsr_state.value_namespace = name_space
                        self.nsr_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby"):
                        self.standby = value
                        self.standby.value_namespace = name_space
                        self.standby.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.node_id.is_set or
                    self.active_reboot_reason.is_set or
                    self.err_log.is_set or
                    self.log.is_set or
                    self.standby_reboot_reason.is_set or
                    (self.redundancy is not None and self.redundancy.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_id.yfilter != YFilter.not_set or
                    self.active_reboot_reason.yfilter != YFilter.not_set or
                    self.err_log.yfilter != YFilter.not_set or
                    self.log.yfilter != YFilter.not_set or
                    self.standby_reboot_reason.yfilter != YFilter.not_set or
                    (self.redundancy is not None and self.redundancy.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rmf-oper:redundancy/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_id.get_name_leafdata())
                if (self.active_reboot_reason.is_set or self.active_reboot_reason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.active_reboot_reason.get_name_leafdata())
                if (self.err_log.is_set or self.err_log.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.err_log.get_name_leafdata())
                if (self.log.is_set or self.log.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.log.get_name_leafdata())
                if (self.standby_reboot_reason.is_set or self.standby_reboot_reason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.standby_reboot_reason.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "redundancy"):
                    if (self.redundancy is None):
                        self.redundancy = Redundancy.Nodes.Node.Redundancy()
                        self.redundancy.parent = self
                        self._children_name_map["redundancy"] = "redundancy"
                    return self.redundancy

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "redundancy" or name == "node-id" or name == "active-reboot-reason" or name == "err-log" or name == "log" or name == "standby-reboot-reason"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-id"):
                    self.node_id = value
                    self.node_id.value_namespace = name_space
                    self.node_id.value_namespace_prefix = name_space_prefix
                if(value_path == "active-reboot-reason"):
                    self.active_reboot_reason = value
                    self.active_reboot_reason.value_namespace = name_space
                    self.active_reboot_reason.value_namespace_prefix = name_space_prefix
                if(value_path == "err-log"):
                    self.err_log = value
                    self.err_log.value_namespace = name_space
                    self.err_log.value_namespace_prefix = name_space_prefix
                if(value_path == "log"):
                    self.log = value
                    self.log.value_namespace = name_space
                    self.log.value_namespace_prefix = name_space_prefix
                if(value_path == "standby-reboot-reason"):
                    self.standby_reboot_reason = value
                    self.standby_reboot_reason.value_namespace = name_space
                    self.standby_reboot_reason.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-infra-rmf-oper:redundancy/%s" % self.get_segment_path()
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
                c = Redundancy.Nodes.Node()
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


    class Summary(Entity):
        """
        Redundancy Summary of Nodes
        
        .. attribute:: err_log
        
        	Error Log
        	**type**\:  str
        
        .. attribute:: red_pair
        
        	Redundancy Pair
        	**type**\: list of    :py:class:`RedPair <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair>`
        
        

        """

        _prefix = 'infra-rmf-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Redundancy.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "redundancy"

            self.err_log = YLeaf(YType.str, "err-log")

            self.red_pair = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("err_log") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Redundancy.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Redundancy.Summary, self).__setattr__(name, value)


        class RedPair(Entity):
            """
            Redundancy Pair
            
            .. attribute:: active
            
            	Active node name R/S/I
            	**type**\:  str
            
            .. attribute:: groupinfo
            
            	groupinfo
            	**type**\: list of    :py:class:`Groupinfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rmf_oper.Redundancy.Summary.RedPair.Groupinfo>`
            
            .. attribute:: ha_state
            
            	High Availability state Ready/Not Ready
            	**type**\:  str
            
            .. attribute:: nsr_state
            
            	NSR state Configured/Not Configured
            	**type**\:  str
            
            .. attribute:: standby
            
            	Standby node name R/S/I
            	**type**\:  str
            
            

            """

            _prefix = 'infra-rmf-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Redundancy.Summary.RedPair, self).__init__()

                self.yang_name = "red-pair"
                self.yang_parent_name = "summary"

                self.active = YLeaf(YType.str, "active")

                self.ha_state = YLeaf(YType.str, "ha-state")

                self.nsr_state = YLeaf(YType.str, "nsr-state")

                self.standby = YLeaf(YType.str, "standby")

                self.groupinfo = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("active",
                                "ha_state",
                                "nsr_state",
                                "standby") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Redundancy.Summary.RedPair, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Redundancy.Summary.RedPair, self).__setattr__(name, value)


            class Groupinfo(Entity):
                """
                groupinfo
                
                .. attribute:: active
                
                	Active
                	**type**\:  str
                
                .. attribute:: ha_state
                
                	HAState
                	**type**\:  str
                
                .. attribute:: nsr_state
                
                	NSRState
                	**type**\:  str
                
                .. attribute:: standby
                
                	Standby
                	**type**\:  str
                
                

                """

                _prefix = 'infra-rmf-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Redundancy.Summary.RedPair.Groupinfo, self).__init__()

                    self.yang_name = "groupinfo"
                    self.yang_parent_name = "red-pair"

                    self.active = YLeaf(YType.str, "active")

                    self.ha_state = YLeaf(YType.str, "ha-state")

                    self.nsr_state = YLeaf(YType.str, "nsr-state")

                    self.standby = YLeaf(YType.str, "standby")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("active",
                                    "ha_state",
                                    "nsr_state",
                                    "standby") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Redundancy.Summary.RedPair.Groupinfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Redundancy.Summary.RedPair.Groupinfo, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.active.is_set or
                        self.ha_state.is_set or
                        self.nsr_state.is_set or
                        self.standby.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.active.yfilter != YFilter.not_set or
                        self.ha_state.yfilter != YFilter.not_set or
                        self.nsr_state.yfilter != YFilter.not_set or
                        self.standby.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "groupinfo" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-infra-rmf-oper:redundancy/summary/red-pair/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.active.get_name_leafdata())
                    if (self.ha_state.is_set or self.ha_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ha_state.get_name_leafdata())
                    if (self.nsr_state.is_set or self.nsr_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.nsr_state.get_name_leafdata())
                    if (self.standby.is_set or self.standby.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.standby.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "active" or name == "ha-state" or name == "nsr-state" or name == "standby"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "active"):
                        self.active = value
                        self.active.value_namespace = name_space
                        self.active.value_namespace_prefix = name_space_prefix
                    if(value_path == "ha-state"):
                        self.ha_state = value
                        self.ha_state.value_namespace = name_space
                        self.ha_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "nsr-state"):
                        self.nsr_state = value
                        self.nsr_state.value_namespace = name_space
                        self.nsr_state.value_namespace_prefix = name_space_prefix
                    if(value_path == "standby"):
                        self.standby = value
                        self.standby.value_namespace = name_space
                        self.standby.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.groupinfo:
                    if (c.has_data()):
                        return True
                return (
                    self.active.is_set or
                    self.ha_state.is_set or
                    self.nsr_state.is_set or
                    self.standby.is_set)

            def has_operation(self):
                for c in self.groupinfo:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.active.yfilter != YFilter.not_set or
                    self.ha_state.yfilter != YFilter.not_set or
                    self.nsr_state.yfilter != YFilter.not_set or
                    self.standby.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "red-pair" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-rmf-oper:redundancy/summary/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.active.is_set or self.active.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.active.get_name_leafdata())
                if (self.ha_state.is_set or self.ha_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ha_state.get_name_leafdata())
                if (self.nsr_state.is_set or self.nsr_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nsr_state.get_name_leafdata())
                if (self.standby.is_set or self.standby.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.standby.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "groupinfo"):
                    for c in self.groupinfo:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Redundancy.Summary.RedPair.Groupinfo()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.groupinfo.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "groupinfo" or name == "active" or name == "ha-state" or name == "nsr-state" or name == "standby"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "active"):
                    self.active = value
                    self.active.value_namespace = name_space
                    self.active.value_namespace_prefix = name_space_prefix
                if(value_path == "ha-state"):
                    self.ha_state = value
                    self.ha_state.value_namespace = name_space
                    self.ha_state.value_namespace_prefix = name_space_prefix
                if(value_path == "nsr-state"):
                    self.nsr_state = value
                    self.nsr_state.value_namespace = name_space
                    self.nsr_state.value_namespace_prefix = name_space_prefix
                if(value_path == "standby"):
                    self.standby = value
                    self.standby.value_namespace = name_space
                    self.standby.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.red_pair:
                if (c.has_data()):
                    return True
            return self.err_log.is_set

        def has_operation(self):
            for c in self.red_pair:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.err_log.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-rmf-oper:redundancy/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.err_log.is_set or self.err_log.yfilter != YFilter.not_set):
                leaf_name_data.append(self.err_log.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "red-pair"):
                for c in self.red_pair:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Redundancy.Summary.RedPair()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.red_pair.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "red-pair" or name == "err-log"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "err-log"):
                self.err_log = value
                self.err_log.value_namespace = name_space
                self.err_log.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.nodes is not None and self.nodes.has_data()) or
            (self.summary is not None and self.summary.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()) or
            (self.summary is not None and self.summary.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-rmf-oper:redundancy" + path_buffer

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

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Redundancy.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = Redundancy.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
            return self.summary

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes" or name == "summary"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Redundancy()
        return self._top_entity

