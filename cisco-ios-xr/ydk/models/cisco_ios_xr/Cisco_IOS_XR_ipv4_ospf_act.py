""" Cisco_IOS_XR_ipv4_ospf_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR OSPF action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ActOspfRoutes(Entity):
    """
    Clear OSPF Routes Table
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRoutes.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfRoutes, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospf-routes"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"

        self.input = ActOspfRoutes.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRoutes.Input.Instance>`
        
        .. attribute:: route
        
        	Clear OSPF route table
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfRoutes.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospf-routes"

            self.route = YLeaf(YType.empty, "route")

            self.instance = ActOspfRoutes.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("route") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ActOspfRoutes.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfRoutes.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfRoutes.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("instance_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfRoutes.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfRoutes.Input.Instance, self).__setattr__(name, value)

            def has_data(self):
                return self.instance_identifier.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.instance_identifier.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "instance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-routes/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.instance_identifier.is_set or self.instance_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.instance_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "instance-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "instance-identifier"):
                    self.instance_identifier = value
                    self.instance_identifier.value_namespace = name_space
                    self.instance_identifier.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.route.is_set or
                (self.instance is not None and self.instance.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.route.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-routes/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.route.is_set or self.route.yfilter != YFilter.not_set):
                leaf_name_data.append(self.route.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ActOspfRoutes.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "route"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "route"):
                self.route = value
                self.route.value_namespace = name_space
                self.route.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-routes" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ActOspfRoutes.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActOspfRoutes()
        return self._top_entity

class ActOspfRedistribution(Entity):
    """
    Clear OSPF Route Redistribution
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRedistribution.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfRedistribution, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospf-redistribution"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"

        self.input = ActOspfRedistribution.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfRedistribution.Input.Instance>`
        
        .. attribute:: redistribution
        
        	Clear OSPF Route Redistribution
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfRedistribution.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospf-redistribution"

            self.redistribution = YLeaf(YType.empty, "redistribution")

            self.instance = ActOspfRedistribution.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("redistribution") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ActOspfRedistribution.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfRedistribution.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfRedistribution.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("instance_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfRedistribution.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfRedistribution.Input.Instance, self).__setattr__(name, value)

            def has_data(self):
                return self.instance_identifier.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.instance_identifier.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "instance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-redistribution/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.instance_identifier.is_set or self.instance_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.instance_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "instance-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "instance-identifier"):
                    self.instance_identifier = value
                    self.instance_identifier.value_namespace = name_space
                    self.instance_identifier.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.redistribution.is_set or
                (self.instance is not None and self.instance.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.redistribution.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-redistribution/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.redistribution.is_set or self.redistribution.yfilter != YFilter.not_set):
                leaf_name_data.append(self.redistribution.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ActOspfRedistribution.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "redistribution"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "redistribution"):
                self.redistribution = value
                self.redistribution.value_namespace = name_space
                self.redistribution.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-redistribution" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ActOspfRedistribution.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActOspfRedistribution()
        return self._top_entity

class ActOspfStatistics(Entity):
    """
    Clear OSPF Counters And Statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatistics.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfStatistics, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospf-statistics"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"

        self.input = ActOspfStatistics.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: all
        
        	All OSPF counters and statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatistics.Input.Instance>`
        
        .. attribute:: interface_name
        
        	OSPF interface statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: message_queue
        
        	Message\-queue statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: neighbor
        
        	Neighbor statistics per neighbor id
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: spf
        
        	SPF statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfStatistics.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospf-statistics"

            self.all = YLeaf(YType.empty, "all")

            self.interface_name = YLeaf(YType.empty, "interface-name")

            self.message_queue = YLeaf(YType.empty, "message-queue")

            self.neighbor = YLeaf(YType.empty, "neighbor")

            self.spf = YLeaf(YType.empty, "spf")

            self.instance = ActOspfStatistics.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("all",
                            "interface_name",
                            "message_queue",
                            "neighbor",
                            "spf") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ActOspfStatistics.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfStatistics.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfStatistics.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("instance_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfStatistics.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfStatistics.Input.Instance, self).__setattr__(name, value)

            def has_data(self):
                return self.instance_identifier.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.instance_identifier.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "instance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.instance_identifier.is_set or self.instance_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.instance_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "instance-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "instance-identifier"):
                    self.instance_identifier = value
                    self.instance_identifier.value_namespace = name_space
                    self.instance_identifier.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.all.is_set or
                self.interface_name.is_set or
                self.message_queue.is_set or
                self.neighbor.is_set or
                self.spf.is_set or
                (self.instance is not None and self.instance.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.all.yfilter != YFilter.not_set or
                self.interface_name.yfilter != YFilter.not_set or
                self.message_queue.yfilter != YFilter.not_set or
                self.neighbor.yfilter != YFilter.not_set or
                self.spf.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.all.is_set or self.all.yfilter != YFilter.not_set):
                leaf_name_data.append(self.all.get_name_leafdata())
            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface_name.get_name_leafdata())
            if (self.message_queue.is_set or self.message_queue.yfilter != YFilter.not_set):
                leaf_name_data.append(self.message_queue.get_name_leafdata())
            if (self.neighbor.is_set or self.neighbor.yfilter != YFilter.not_set):
                leaf_name_data.append(self.neighbor.get_name_leafdata())
            if (self.spf.is_set or self.spf.yfilter != YFilter.not_set):
                leaf_name_data.append(self.spf.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ActOspfStatistics.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "all" or name == "interface-name" or name == "message-queue" or name == "neighbor" or name == "spf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "all"):
                self.all = value
                self.all.value_namespace = name_space
                self.all.value_namespace_prefix = name_space_prefix
            if(value_path == "interface-name"):
                self.interface_name = value
                self.interface_name.value_namespace = name_space
                self.interface_name.value_namespace_prefix = name_space_prefix
            if(value_path == "message-queue"):
                self.message_queue = value
                self.message_queue.value_namespace = name_space
                self.message_queue.value_namespace_prefix = name_space_prefix
            if(value_path == "neighbor"):
                self.neighbor = value
                self.neighbor.value_namespace = name_space
                self.neighbor.value_namespace_prefix = name_space_prefix
            if(value_path == "spf"):
                self.spf = value
                self.spf.value_namespace = name_space
                self.spf.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ActOspfStatistics.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActOspfStatistics()
        return self._top_entity

class ActOspfStatisticsNeighbor(Entity):
    """
    Neighbor statistics per neighbor id
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsNeighbor.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfStatisticsNeighbor, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospf-statistics-neighbor"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"

        self.input = ActOspfStatisticsNeighbor.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsNeighbor.Input.Instance>`
        
        .. attribute:: neighbor
        
        	
        	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsNeighbor.Input.Neighbor>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfStatisticsNeighbor.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospf-statistics-neighbor"

            self.instance = ActOspfStatisticsNeighbor.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

            self.neighbor = ActOspfStatisticsNeighbor.Input.Neighbor()
            self.neighbor.parent = self
            self._children_name_map["neighbor"] = "neighbor"
            self._children_yang_names.add("neighbor")


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfStatisticsNeighbor.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("instance_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfStatisticsNeighbor.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfStatisticsNeighbor.Input.Instance, self).__setattr__(name, value)

            def has_data(self):
                return self.instance_identifier.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.instance_identifier.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "instance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.instance_identifier.is_set or self.instance_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.instance_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "instance-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "instance-identifier"):
                    self.instance_identifier = value
                    self.instance_identifier.value_namespace = name_space
                    self.instance_identifier.value_namespace_prefix = name_space_prefix


        class Neighbor(Entity):
            """
            
            
            .. attribute:: interface_name
            
            	Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: neighbor_id
            
            	Neighbor ID
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfStatisticsNeighbor.Input.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "input"

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.neighbor_id = YLeaf(YType.str, "neighbor-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name",
                                "neighbor_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfStatisticsNeighbor.Input.Neighbor, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfStatisticsNeighbor.Input.Neighbor, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    self.neighbor_id.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.neighbor_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "neighbor" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.neighbor_id.is_set or self.neighbor_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.neighbor_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name" or name == "neighbor-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "neighbor-id"):
                    self.neighbor_id = value
                    self.neighbor_id.value_namespace = name_space
                    self.neighbor_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.instance is not None and self.instance.has_data()) or
                (self.neighbor is not None and self.neighbor.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()) or
                (self.neighbor is not None and self.neighbor.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ActOspfStatisticsNeighbor.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            if (child_yang_name == "neighbor"):
                if (self.neighbor is None):
                    self.neighbor = ActOspfStatisticsNeighbor.Input.Neighbor()
                    self.neighbor.parent = self
                    self._children_name_map["neighbor"] = "neighbor"
                return self.neighbor

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "neighbor"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-neighbor" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ActOspfStatisticsNeighbor.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActOspfStatisticsNeighbor()
        return self._top_entity

class ActOspfStatisticsInterface(Entity):
    """
    Neighbor statistics per interface
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsInterface.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfStatisticsInterface, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospf-statistics-interface"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"

        self.input = ActOspfStatisticsInterface.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsInterface.Input.Instance>`
        
        .. attribute:: interface
        
        	
        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfStatisticsInterface.Input.Interface>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfStatisticsInterface.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospf-statistics-interface"

            self.instance = ActOspfStatisticsInterface.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

            self.interface = ActOspfStatisticsInterface.Input.Interface()
            self.interface.parent = self
            self._children_name_map["interface"] = "interface"
            self._children_yang_names.add("interface")


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfStatisticsInterface.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("instance_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfStatisticsInterface.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfStatisticsInterface.Input.Instance, self).__setattr__(name, value)

            def has_data(self):
                return self.instance_identifier.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.instance_identifier.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "instance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.instance_identifier.is_set or self.instance_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.instance_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "instance-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "instance-identifier"):
                    self.instance_identifier = value
                    self.instance_identifier.value_namespace = name_space
                    self.instance_identifier.value_namespace_prefix = name_space_prefix


        class Interface(Entity):
            """
            
            
            .. attribute:: interface_name
            
            	OSPF interface statistics
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfStatisticsInterface.Input.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "input"

                self.interface_name = YLeaf(YType.str, "interface-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfStatisticsInterface.Input.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfStatisticsInterface.Input.Interface, self).__setattr__(name, value)

            def has_data(self):
                return self.interface_name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.instance is not None and self.instance.has_data()) or
                (self.interface is not None and self.interface.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()) or
                (self.interface is not None and self.interface.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ActOspfStatisticsInterface.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            if (child_yang_name == "interface"):
                if (self.interface is None):
                    self.interface = ActOspfStatisticsInterface.Input.Interface()
                    self.interface.parent = self
                    self._children_name_map["interface"] = "interface"
                return self.interface

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-statistics-interface" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ActOspfStatisticsInterface.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActOspfStatisticsInterface()
        return self._top_entity

class ActOspfProcess(Entity):
    """
    Reset OSPF Process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfProcess.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfProcess, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospf-process"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"

        self.input = ActOspfProcess.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPF instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfProcess.Input.Instance>`
        
        .. attribute:: process
        
        	Reset OSPF process
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfProcess.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospf-process"

            self.process = YLeaf(YType.empty, "process")

            self.instance = ActOspfProcess.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("process") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ActOspfProcess.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfProcess.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPF instance
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfProcess.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("instance_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfProcess.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfProcess.Input.Instance, self).__setattr__(name, value)

            def has_data(self):
                return self.instance_identifier.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.instance_identifier.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "instance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-process/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.instance_identifier.is_set or self.instance_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.instance_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "instance-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "instance-identifier"):
                    self.instance_identifier = value
                    self.instance_identifier.value_namespace = name_space
                    self.instance_identifier.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.process.is_set or
                (self.instance is not None and self.instance.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.process.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-process/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.process.is_set or self.process.yfilter != YFilter.not_set):
                leaf_name_data.append(self.process.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ActOspfProcess.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "process"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "process"):
                self.process = value
                self.process.value_namespace = name_space
                self.process.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-process" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ActOspfProcess.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActOspfProcess()
        return self._top_entity

class ActOspfInstanceVrf(Entity):
    """
    Clear one or more non\-default OSPF VRFs in process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input>`
    
    

    """

    _prefix = 'ospf-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfInstanceVrf, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospf-instance-vrf"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-ospf-act"

        self.input = ActOspfInstanceVrf.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	OSPF instance name
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance>`
        
        

        """

        _prefix = 'ospf-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfInstanceVrf.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospf-instance-vrf"

            self.instance = ActOspfInstanceVrf.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")


        class Instance(Entity):
            """
            OSPF instance name
            
            .. attribute:: all
            
            	Clear all non\-default OSPF VRFs
            	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.All>`
            
            .. attribute:: all_inclusive
            
            	Clear all non\-default and default OSPF VRFs
            	**type**\:   :py:class:`AllInclusive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.AllInclusive>`
            
            .. attribute:: instance_identifier
            
            	OSPF process instance identifier
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: vrf
            
            	Clear one or more non\-default OSPF VRFs in process
            	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.Vrf>`
            
            

            """

            _prefix = 'ospf-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfInstanceVrf.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

                self.all = ActOspfInstanceVrf.Input.Instance.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._children_yang_names.add("all")

                self.all_inclusive = ActOspfInstanceVrf.Input.Instance.AllInclusive()
                self.all_inclusive.parent = self
                self._children_name_map["all_inclusive"] = "all-inclusive"
                self._children_yang_names.add("all-inclusive")

                self.vrf = ActOspfInstanceVrf.Input.Instance.Vrf()
                self.vrf.parent = self
                self._children_name_map["vrf"] = "vrf"
                self._children_yang_names.add("vrf")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("instance_identifier") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ActOspfInstanceVrf.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfInstanceVrf.Input.Instance, self).__setattr__(name, value)


            class Vrf(Entity):
                """
                Clear one or more non\-default OSPF VRFs in process
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.Vrf.Stats>`
                
                .. attribute:: vrf_name
                
                	OSPF VRF name
                	**type**\:  str
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ActOspfInstanceVrf.Input.Instance.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "instance"

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.stats = ActOspfInstanceVrf.Input.Instance.Vrf.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("process",
                                    "redistribution",
                                    "route",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ActOspfInstanceVrf.Input.Instance.Vrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActOspfInstanceVrf.Input.Instance.Vrf, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "vrf"

                        self.message_queue = YLeaf(YType.empty, "message-queue")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.interface = ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"
                        self._children_yang_names.add("interface")

                        self.neighbor = ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._children_yang_names.add("neighbor")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("message_queue",
                                        "spf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "stats"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return self.interface_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/vrf/stats/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._children_yang_names.add("interface")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("neighbor_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"

                                self.interface_name = YLeaf(YType.str, "interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__setattr__(name, value)

                            def has_data(self):
                                return self.interface_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/vrf/stats/neighbor/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.neighbor_id.is_set or
                                (self.interface is not None and self.interface.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.neighbor_id.yfilter != YFilter.not_set or
                                (self.interface is not None and self.interface.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "neighbor" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/vrf/stats/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.neighbor_id.is_set or self.neighbor_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "interface"):
                                if (self.interface is None):
                                    self.interface = ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface()
                                    self.interface.parent = self
                                    self._children_name_map["interface"] = "interface"
                                return self.interface

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface" or name == "neighbor-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "neighbor-id"):
                                self.neighbor_id = value
                                self.neighbor_id.value_namespace = name_space
                                self.neighbor_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.message_queue.is_set or
                            self.spf.is_set or
                            (self.interface is not None and self.interface.has_data()) or
                            (self.neighbor is not None and self.neighbor.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.message_queue.yfilter != YFilter.not_set or
                            self.spf.yfilter != YFilter.not_set or
                            (self.interface is not None and self.interface.has_operation()) or
                            (self.neighbor is not None and self.neighbor.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/vrf/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.message_queue.is_set or self.message_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_queue.get_name_leafdata())
                        if (self.spf.is_set or self.spf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.spf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interface"):
                            if (self.interface is None):
                                self.interface = ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Interface()
                                self.interface.parent = self
                                self._children_name_map["interface"] = "interface"
                            return self.interface

                        if (child_yang_name == "neighbor"):
                            if (self.neighbor is None):
                                self.neighbor = ActOspfInstanceVrf.Input.Instance.Vrf.Stats.Neighbor()
                                self.neighbor.parent = self
                                self._children_name_map["neighbor"] = "neighbor"
                            return self.neighbor

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "neighbor" or name == "message-queue" or name == "spf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "message-queue"):
                            self.message_queue = value
                            self.message_queue.value_namespace = name_space
                            self.message_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "spf"):
                            self.spf = value
                            self.spf.value_namespace = name_space
                            self.spf.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.process.is_set or
                        self.redistribution.is_set or
                        self.route.is_set or
                        self.vrf_name.is_set or
                        (self.stats is not None and self.stats.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.process.yfilter != YFilter.not_set or
                        self.redistribution.yfilter != YFilter.not_set or
                        self.route.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        (self.stats is not None and self.stats.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrf" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.process.is_set or self.process.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.process.get_name_leafdata())
                    if (self.redistribution.is_set or self.redistribution.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redistribution.get_name_leafdata())
                    if (self.route.is_set or self.route.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "stats"):
                        if (self.stats is None):
                            self.stats = ActOspfInstanceVrf.Input.Instance.Vrf.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                        return self.stats

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "stats" or name == "process" or name == "redistribution" or name == "route" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "process"):
                        self.process = value
                        self.process.value_namespace = name_space
                        self.process.value_namespace_prefix = name_space_prefix
                    if(value_path == "redistribution"):
                        self.redistribution = value
                        self.redistribution.value_namespace = name_space
                        self.redistribution.value_namespace_prefix = name_space_prefix
                    if(value_path == "route"):
                        self.route = value
                        self.route.value_namespace = name_space
                        self.route.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix


            class All(Entity):
                """
                Clear all non\-default OSPF VRFs
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.All.Stats>`
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ActOspfInstanceVrf.Input.Instance.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "instance"

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.stats = ActOspfInstanceVrf.Input.Instance.All.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("process",
                                    "redistribution",
                                    "route") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ActOspfInstanceVrf.Input.Instance.All, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActOspfInstanceVrf.Input.Instance.All, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.All.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ActOspfInstanceVrf.Input.Instance.All.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all"

                        self.message_queue = YLeaf(YType.empty, "message-queue")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.interface = ActOspfInstanceVrf.Input.Instance.All.Stats.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"
                        self._children_yang_names.add("interface")

                        self.neighbor = ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._children_yang_names.add("neighbor")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("message_queue",
                                        "spf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActOspfInstanceVrf.Input.Instance.All.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActOspfInstanceVrf.Input.Instance.All.Stats, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfInstanceVrf.Input.Instance.All.Stats.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "stats"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ActOspfInstanceVrf.Input.Instance.All.Stats.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfInstanceVrf.Input.Instance.All.Stats.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return self.interface_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all/stats/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._children_yang_names.add("interface")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("neighbor_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"

                                self.interface_name = YLeaf(YType.str, "interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__setattr__(name, value)

                            def has_data(self):
                                return self.interface_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all/stats/neighbor/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.neighbor_id.is_set or
                                (self.interface is not None and self.interface.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.neighbor_id.yfilter != YFilter.not_set or
                                (self.interface is not None and self.interface.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "neighbor" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all/stats/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.neighbor_id.is_set or self.neighbor_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "interface"):
                                if (self.interface is None):
                                    self.interface = ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor.Interface()
                                    self.interface.parent = self
                                    self._children_name_map["interface"] = "interface"
                                return self.interface

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface" or name == "neighbor-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "neighbor-id"):
                                self.neighbor_id = value
                                self.neighbor_id.value_namespace = name_space
                                self.neighbor_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.message_queue.is_set or
                            self.spf.is_set or
                            (self.interface is not None and self.interface.has_data()) or
                            (self.neighbor is not None and self.neighbor.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.message_queue.yfilter != YFilter.not_set or
                            self.spf.yfilter != YFilter.not_set or
                            (self.interface is not None and self.interface.has_operation()) or
                            (self.neighbor is not None and self.neighbor.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.message_queue.is_set or self.message_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_queue.get_name_leafdata())
                        if (self.spf.is_set or self.spf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.spf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interface"):
                            if (self.interface is None):
                                self.interface = ActOspfInstanceVrf.Input.Instance.All.Stats.Interface()
                                self.interface.parent = self
                                self._children_name_map["interface"] = "interface"
                            return self.interface

                        if (child_yang_name == "neighbor"):
                            if (self.neighbor is None):
                                self.neighbor = ActOspfInstanceVrf.Input.Instance.All.Stats.Neighbor()
                                self.neighbor.parent = self
                                self._children_name_map["neighbor"] = "neighbor"
                            return self.neighbor

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "neighbor" or name == "message-queue" or name == "spf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "message-queue"):
                            self.message_queue = value
                            self.message_queue.value_namespace = name_space
                            self.message_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "spf"):
                            self.spf = value
                            self.spf.value_namespace = name_space
                            self.spf.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.process.is_set or
                        self.redistribution.is_set or
                        self.route.is_set or
                        (self.stats is not None and self.stats.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.process.yfilter != YFilter.not_set or
                        self.redistribution.yfilter != YFilter.not_set or
                        self.route.yfilter != YFilter.not_set or
                        (self.stats is not None and self.stats.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "all" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.process.is_set or self.process.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.process.get_name_leafdata())
                    if (self.redistribution.is_set or self.redistribution.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redistribution.get_name_leafdata())
                    if (self.route.is_set or self.route.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "stats"):
                        if (self.stats is None):
                            self.stats = ActOspfInstanceVrf.Input.Instance.All.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                        return self.stats

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "stats" or name == "process" or name == "redistribution" or name == "route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "process"):
                        self.process = value
                        self.process.value_namespace = name_space
                        self.process.value_namespace_prefix = name_space_prefix
                    if(value_path == "redistribution"):
                        self.redistribution = value
                        self.redistribution.value_namespace = name_space
                        self.redistribution.value_namespace_prefix = name_space_prefix
                    if(value_path == "route"):
                        self.route = value
                        self.route.value_namespace = name_space
                        self.route.value_namespace_prefix = name_space_prefix


            class AllInclusive(Entity):
                """
                Clear all non\-default and default OSPF VRFs
                
                .. attribute:: process
                
                	Reset OSPF process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPF route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPF route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPF counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats>`
                
                

                """

                _prefix = 'ospf-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ActOspfInstanceVrf.Input.Instance.AllInclusive, self).__init__()

                    self.yang_name = "all-inclusive"
                    self.yang_parent_name = "instance"

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.stats = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats()
                    self.stats.parent = self
                    self._children_name_map["stats"] = "stats"
                    self._children_yang_names.add("stats")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("process",
                                    "redistribution",
                                    "route") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ActOspfInstanceVrf.Input.Instance.AllInclusive, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActOspfInstanceVrf.Input.Instance.AllInclusive, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    OSPF counters and statistics
                    
                    .. attribute:: interface
                    
                    	OSPF interface statistics
                    	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface>`
                    
                    .. attribute:: message_queue
                    
                    	Message\-queue statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospf-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all-inclusive"

                        self.message_queue = YLeaf(YType.empty, "message-queue")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.interface = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface()
                        self.interface.parent = self
                        self._children_name_map["interface"] = "interface"
                        self._children_yang_names.add("interface")

                        self.neighbor = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                        self._children_yang_names.add("neighbor")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("message_queue",
                                        "spf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        OSPF interface statistics
                        
                        .. attribute:: interface_name
                        
                        	
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "stats"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return self.interface_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all-inclusive/stats/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ospf_act.ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospf-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
                            self.interface.parent = self
                            self._children_name_map["interface"] = "interface"
                            self._children_yang_names.add("interface")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("neighbor_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPF interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospf-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__init__()

                                self.yang_name = "interface"
                                self.yang_parent_name = "neighbor"

                                self.interface_name = YLeaf(YType.str, "interface-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("interface_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__setattr__(name, value)

                            def has_data(self):
                                return self.interface_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "interface" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all-inclusive/stats/neighbor/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "interface-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.neighbor_id.is_set or
                                (self.interface is not None and self.interface.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.neighbor_id.yfilter != YFilter.not_set or
                                (self.interface is not None and self.interface.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "neighbor" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all-inclusive/stats/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.neighbor_id.is_set or self.neighbor_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "interface"):
                                if (self.interface is None):
                                    self.interface = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
                                    self.interface.parent = self
                                    self._children_name_map["interface"] = "interface"
                                return self.interface

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface" or name == "neighbor-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "neighbor-id"):
                                self.neighbor_id = value
                                self.neighbor_id.value_namespace = name_space
                                self.neighbor_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.message_queue.is_set or
                            self.spf.is_set or
                            (self.interface is not None and self.interface.has_data()) or
                            (self.neighbor is not None and self.neighbor.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.message_queue.yfilter != YFilter.not_set or
                            self.spf.yfilter != YFilter.not_set or
                            (self.interface is not None and self.interface.has_operation()) or
                            (self.neighbor is not None and self.neighbor.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/all-inclusive/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.message_queue.is_set or self.message_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.message_queue.get_name_leafdata())
                        if (self.spf.is_set or self.spf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.spf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interface"):
                            if (self.interface is None):
                                self.interface = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Interface()
                                self.interface.parent = self
                                self._children_name_map["interface"] = "interface"
                            return self.interface

                        if (child_yang_name == "neighbor"):
                            if (self.neighbor is None):
                                self.neighbor = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor()
                                self.neighbor.parent = self
                                self._children_name_map["neighbor"] = "neighbor"
                            return self.neighbor

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "neighbor" or name == "message-queue" or name == "spf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "message-queue"):
                            self.message_queue = value
                            self.message_queue.value_namespace = name_space
                            self.message_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "spf"):
                            self.spf = value
                            self.spf.value_namespace = name_space
                            self.spf.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.process.is_set or
                        self.redistribution.is_set or
                        self.route.is_set or
                        (self.stats is not None and self.stats.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.process.yfilter != YFilter.not_set or
                        self.redistribution.yfilter != YFilter.not_set or
                        self.route.yfilter != YFilter.not_set or
                        (self.stats is not None and self.stats.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "all-inclusive" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/instance/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.process.is_set or self.process.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.process.get_name_leafdata())
                    if (self.redistribution.is_set or self.redistribution.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redistribution.get_name_leafdata())
                    if (self.route.is_set or self.route.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.route.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "stats"):
                        if (self.stats is None):
                            self.stats = ActOspfInstanceVrf.Input.Instance.AllInclusive.Stats()
                            self.stats.parent = self
                            self._children_name_map["stats"] = "stats"
                        return self.stats

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "stats" or name == "process" or name == "redistribution" or name == "route"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "process"):
                        self.process = value
                        self.process.value_namespace = name_space
                        self.process.value_namespace_prefix = name_space_prefix
                    if(value_path == "redistribution"):
                        self.redistribution = value
                        self.redistribution.value_namespace = name_space
                        self.redistribution.value_namespace_prefix = name_space_prefix
                    if(value_path == "route"):
                        self.route = value
                        self.route.value_namespace = name_space
                        self.route.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.instance_identifier.is_set or
                    (self.all is not None and self.all.has_data()) or
                    (self.all_inclusive is not None and self.all_inclusive.has_data()) or
                    (self.vrf is not None and self.vrf.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.instance_identifier.yfilter != YFilter.not_set or
                    (self.all is not None and self.all.has_operation()) or
                    (self.all_inclusive is not None and self.all_inclusive.has_operation()) or
                    (self.vrf is not None and self.vrf.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "instance" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.instance_identifier.is_set or self.instance_identifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.instance_identifier.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "all"):
                    if (self.all is None):
                        self.all = ActOspfInstanceVrf.Input.Instance.All()
                        self.all.parent = self
                        self._children_name_map["all"] = "all"
                    return self.all

                if (child_yang_name == "all-inclusive"):
                    if (self.all_inclusive is None):
                        self.all_inclusive = ActOspfInstanceVrf.Input.Instance.AllInclusive()
                        self.all_inclusive.parent = self
                        self._children_name_map["all_inclusive"] = "all-inclusive"
                    return self.all_inclusive

                if (child_yang_name == "vrf"):
                    if (self.vrf is None):
                        self.vrf = ActOspfInstanceVrf.Input.Instance.Vrf()
                        self.vrf.parent = self
                        self._children_name_map["vrf"] = "vrf"
                    return self.vrf

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "all" or name == "all-inclusive" or name == "vrf" or name == "instance-identifier"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "instance-identifier"):
                    self.instance_identifier = value
                    self.instance_identifier.value_namespace = name_space
                    self.instance_identifier.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.instance is not None and self.instance.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ActOspfInstanceVrf.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-ospf-act:act-ospf-instance-vrf" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ActOspfInstanceVrf.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ActOspfInstanceVrf()
        return self._top_entity

