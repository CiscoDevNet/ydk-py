""" Cisco_IOS_XR_ipv6_ospfv3_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR IPv6 OSPFv3 action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ActOspfv3Routes(Entity):
    """
    Clear OSPFv3 Routes Table
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Routes.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfv3Routes, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospfv3-routes"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"

        self.input = ActOspfv3Routes.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Routes.Input.Instance>`
        
        .. attribute:: route
        
        	Clear OSPFv3 route table
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfv3Routes.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospfv3-routes"

            self.route = YLeaf(YType.empty, "route")

            self.instance = ActOspfv3Routes.Input.Instance()
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
                        super(ActOspfv3Routes.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfv3Routes.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfv3Routes.Input.Instance, self).__init__()

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
                            super(ActOspfv3Routes.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfv3Routes.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-routes/input/%s" % self.get_segment_path()
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
                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-routes/%s" % self.get_segment_path()
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
                    self.instance = ActOspfv3Routes.Input.Instance()
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
        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-routes" + path_buffer

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
                self.input = ActOspfv3Routes.Input()
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
        self._top_entity = ActOspfv3Routes()
        return self._top_entity

class ActOspfv3Redistribution(Entity):
    """
    Clear OSPFv3 Route Redistribution
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Redistribution.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfv3Redistribution, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospfv3-redistribution"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"

        self.input = ActOspfv3Redistribution.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Redistribution.Input.Instance>`
        
        .. attribute:: redistribution
        
        	Clear OSPFv3 Route Redistribution
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfv3Redistribution.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospfv3-redistribution"

            self.redistribution = YLeaf(YType.empty, "redistribution")

            self.instance = ActOspfv3Redistribution.Input.Instance()
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
                        super(ActOspfv3Redistribution.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfv3Redistribution.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfv3Redistribution.Input.Instance, self).__init__()

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
                            super(ActOspfv3Redistribution.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfv3Redistribution.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-redistribution/input/%s" % self.get_segment_path()
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
                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-redistribution/%s" % self.get_segment_path()
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
                    self.instance = ActOspfv3Redistribution.Input.Instance()
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
        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-redistribution" + path_buffer

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
                self.input = ActOspfv3Redistribution.Input()
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
        self._top_entity = ActOspfv3Redistribution()
        return self._top_entity

class ActOspfv3Process(Entity):
    """
    Reset OSPFv3 Process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Process.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfv3Process, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospfv3-process"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"

        self.input = ActOspfv3Process.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Process.Input.Instance>`
        
        .. attribute:: process
        
        	Reset OSPFv3 process
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfv3Process.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospfv3-process"

            self.process = YLeaf(YType.empty, "process")

            self.instance = ActOspfv3Process.Input.Instance()
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
                        super(ActOspfv3Process.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfv3Process.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfv3Process.Input.Instance, self).__init__()

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
                            super(ActOspfv3Process.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfv3Process.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-process/input/%s" % self.get_segment_path()
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
                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-process/%s" % self.get_segment_path()
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
                    self.instance = ActOspfv3Process.Input.Instance()
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
        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-process" + path_buffer

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
                self.input = ActOspfv3Process.Input()
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
        self._top_entity = ActOspfv3Process()
        return self._top_entity

class ActOspfv3StatisticsNeighbor(Entity):
    """
    Neighbor statistics per neighbor id
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsNeighbor.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfv3StatisticsNeighbor, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospfv3-statistics-neighbor"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"

        self.input = ActOspfv3StatisticsNeighbor.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsNeighbor.Input.Instance>`
        
        .. attribute:: neighbor
        
        	
        	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3StatisticsNeighbor.Input.Neighbor>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfv3StatisticsNeighbor.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospfv3-statistics-neighbor"

            self.instance = ActOspfv3StatisticsNeighbor.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

            self.neighbor = ActOspfv3StatisticsNeighbor.Input.Neighbor()
            self.neighbor.parent = self
            self._children_name_map["neighbor"] = "neighbor"
            self._children_yang_names.add("neighbor")


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfv3StatisticsNeighbor.Input.Instance, self).__init__()

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
                            super(ActOspfv3StatisticsNeighbor.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfv3StatisticsNeighbor.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor/input/%s" % self.get_segment_path()
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

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfv3StatisticsNeighbor.Input.Neighbor, self).__init__()

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
                            super(ActOspfv3StatisticsNeighbor.Input.Neighbor, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfv3StatisticsNeighbor.Input.Neighbor, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor/input/%s" % self.get_segment_path()
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
                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor/%s" % self.get_segment_path()
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
                    self.instance = ActOspfv3StatisticsNeighbor.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            if (child_yang_name == "neighbor"):
                if (self.neighbor is None):
                    self.neighbor = ActOspfv3StatisticsNeighbor.Input.Neighbor()
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
        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics-neighbor" + path_buffer

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
                self.input = ActOspfv3StatisticsNeighbor.Input()
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
        self._top_entity = ActOspfv3StatisticsNeighbor()
        return self._top_entity

class ActOspfv3Statistics(Entity):
    """
    Clear OSPFv3 Counters And Statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Statistics.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfv3Statistics, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospfv3-statistics"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"

        self.input = ActOspfv3Statistics.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from OSPFv3 instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3Statistics.Input.Instance>`
        
        .. attribute:: neighbor
        
        	Neighbor statistics per neighbor id
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: prefix_priority
        
        	All OSPFv3 counters and statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: spf
        
        	SPF statistics
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfv3Statistics.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospfv3-statistics"

            self.neighbor = YLeaf(YType.empty, "neighbor")

            self.prefix_priority = YLeaf(YType.empty, "prefix-priority")

            self.spf = YLeaf(YType.empty, "spf")

            self.instance = ActOspfv3Statistics.Input.Instance()
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
                if name in ("neighbor",
                            "prefix_priority",
                            "spf") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ActOspfv3Statistics.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ActOspfv3Statistics.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from OSPFv3 instance
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfv3Statistics.Input.Instance, self).__init__()

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
                            super(ActOspfv3Statistics.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfv3Statistics.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics/input/%s" % self.get_segment_path()
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
                self.neighbor.is_set or
                self.prefix_priority.is_set or
                self.spf.is_set or
                (self.instance is not None and self.instance.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.neighbor.yfilter != YFilter.not_set or
                self.prefix_priority.yfilter != YFilter.not_set or
                self.spf.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.neighbor.is_set or self.neighbor.yfilter != YFilter.not_set):
                leaf_name_data.append(self.neighbor.get_name_leafdata())
            if (self.prefix_priority.is_set or self.prefix_priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.prefix_priority.get_name_leafdata())
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
                    self.instance = ActOspfv3Statistics.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "neighbor" or name == "prefix-priority" or name == "spf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "neighbor"):
                self.neighbor = value
                self.neighbor.value_namespace = name_space
                self.neighbor.value_namespace_prefix = name_space_prefix
            if(value_path == "prefix-priority"):
                self.prefix_priority = value
                self.prefix_priority.value_namespace = name_space
                self.prefix_priority.value_namespace_prefix = name_space_prefix
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
        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-statistics" + path_buffer

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
                self.input = ActOspfv3Statistics.Input()
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
        self._top_entity = ActOspfv3Statistics()
        return self._top_entity

class ActOspfv3InstanceVrf(Entity):
    """
    Clear one or more non\-default OSPFv3 VRFs in process
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input>`
    
    

    """

    _prefix = 'ospfv3-act'
    _revision = '2016-09-14'

    def __init__(self):
        super(ActOspfv3InstanceVrf, self).__init__()
        self._top_entity = None

        self.yang_name = "act-ospfv3-instance-vrf"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-ospfv3-act"

        self.input = ActOspfv3InstanceVrf.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	OSPFv3 instance name
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance>`
        
        

        """

        _prefix = 'ospfv3-act'
        _revision = '2016-09-14'

        def __init__(self):
            super(ActOspfv3InstanceVrf.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "act-ospfv3-instance-vrf"

            self.instance = ActOspfv3InstanceVrf.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")


        class Instance(Entity):
            """
            OSPFv3 instance name
            
            .. attribute:: all
            
            	Clear all non\-default OSPFv3 VRFs
            	**type**\:   :py:class:`All <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.All>`
            
            .. attribute:: all_inclusive
            
            	Clear all non\-default and default OSPFv3 VRFs
            	**type**\:   :py:class:`AllInclusive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.AllInclusive>`
            
            .. attribute:: instance_identifier
            
            	OSPFv3 process instance identifier
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: vrf
            
            	Clear one or more non\-default OSPFv3 VRFs in process
            	**type**\:   :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.Vrf>`
            
            

            """

            _prefix = 'ospfv3-act'
            _revision = '2016-09-14'

            def __init__(self):
                super(ActOspfv3InstanceVrf.Input.Instance, self).__init__()

                self.yang_name = "instance"
                self.yang_parent_name = "input"

                self.instance_identifier = YLeaf(YType.str, "instance-identifier")

                self.all = ActOspfv3InstanceVrf.Input.Instance.All()
                self.all.parent = self
                self._children_name_map["all"] = "all"
                self._children_yang_names.add("all")

                self.all_inclusive = ActOspfv3InstanceVrf.Input.Instance.AllInclusive()
                self.all_inclusive.parent = self
                self._children_name_map["all_inclusive"] = "all-inclusive"
                self._children_yang_names.add("all-inclusive")

                self.vrf = ActOspfv3InstanceVrf.Input.Instance.Vrf()
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
                            super(ActOspfv3InstanceVrf.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ActOspfv3InstanceVrf.Input.Instance, self).__setattr__(name, value)


            class Vrf(Entity):
                """
                Clear one or more non\-default OSPFv3 VRFs in process
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats>`
                
                .. attribute:: vrf_name
                
                	OSPFv3 VRF name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ActOspfv3InstanceVrf.Input.Instance.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "instance"

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.stats = ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats()
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
                                super(ActOspfv3InstanceVrf.Input.Instance.Vrf, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActOspfv3InstanceVrf.Input.Instance.Vrf, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "vrf"

                        self.prefix_priority = YLeaf(YType.empty, "prefix-priority")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.neighbor = ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor()
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
                            if name in ("prefix_priority",
                                        "spf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats, self).__setattr__(name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface()
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
                                        super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__init__()

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
                                            super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface, self).__setattr__(name, value)

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
                                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/vrf/stats/neighbor/%s" % self.get_segment_path()
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
                                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/vrf/stats/%s" % self.get_segment_path()
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
                                    self.interface = ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor.Interface()
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
                            self.prefix_priority.is_set or
                            self.spf.is_set or
                            (self.neighbor is not None and self.neighbor.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix_priority.yfilter != YFilter.not_set or
                            self.spf.yfilter != YFilter.not_set or
                            (self.neighbor is not None and self.neighbor.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/vrf/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix_priority.is_set or self.prefix_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_priority.get_name_leafdata())
                        if (self.spf.is_set or self.spf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.spf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "neighbor"):
                            if (self.neighbor is None):
                                self.neighbor = ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats.Neighbor()
                                self.neighbor.parent = self
                                self._children_name_map["neighbor"] = "neighbor"
                            return self.neighbor

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "neighbor" or name == "prefix-priority" or name == "spf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix-priority"):
                            self.prefix_priority = value
                            self.prefix_priority.value_namespace = name_space
                            self.prefix_priority.value_namespace_prefix = name_space_prefix
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
                        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/%s" % self.get_segment_path()
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
                            self.stats = ActOspfv3InstanceVrf.Input.Instance.Vrf.Stats()
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
                Clear all non\-default OSPFv3 VRFs
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.All.Stats>`
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ActOspfv3InstanceVrf.Input.Instance.All, self).__init__()

                    self.yang_name = "all"
                    self.yang_parent_name = "instance"

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.stats = ActOspfv3InstanceVrf.Input.Instance.All.Stats()
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
                                super(ActOspfv3InstanceVrf.Input.Instance.All, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActOspfv3InstanceVrf.Input.Instance.All, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ActOspfv3InstanceVrf.Input.Instance.All.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all"

                        self.prefix_priority = YLeaf(YType.empty, "prefix-priority")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.neighbor = ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor()
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
                            if name in ("prefix_priority",
                                        "spf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActOspfv3InstanceVrf.Input.Instance.All.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActOspfv3InstanceVrf.Input.Instance.All.Stats, self).__setattr__(name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface()
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
                                        super(ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__init__()

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
                                            super(ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface, self).__setattr__(name, value)

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
                                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/all/stats/neighbor/%s" % self.get_segment_path()
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
                                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/all/stats/%s" % self.get_segment_path()
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
                                    self.interface = ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor.Interface()
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
                            self.prefix_priority.is_set or
                            self.spf.is_set or
                            (self.neighbor is not None and self.neighbor.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix_priority.yfilter != YFilter.not_set or
                            self.spf.yfilter != YFilter.not_set or
                            (self.neighbor is not None and self.neighbor.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/all/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix_priority.is_set or self.prefix_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_priority.get_name_leafdata())
                        if (self.spf.is_set or self.spf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.spf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "neighbor"):
                            if (self.neighbor is None):
                                self.neighbor = ActOspfv3InstanceVrf.Input.Instance.All.Stats.Neighbor()
                                self.neighbor.parent = self
                                self._children_name_map["neighbor"] = "neighbor"
                            return self.neighbor

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "neighbor" or name == "prefix-priority" or name == "spf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix-priority"):
                            self.prefix_priority = value
                            self.prefix_priority.value_namespace = name_space
                            self.prefix_priority.value_namespace_prefix = name_space_prefix
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
                        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/%s" % self.get_segment_path()
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
                            self.stats = ActOspfv3InstanceVrf.Input.Instance.All.Stats()
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
                Clear all non\-default and default OSPFv3 VRFs
                
                .. attribute:: process
                
                	Reset OSPFv3 process
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: redistribution
                
                	Clear OSPFv3 route redistrbution
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: route
                
                	Clear OSPFv3 route table
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: stats
                
                	OSPFv3 counters and statistics
                	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats>`
                
                

                """

                _prefix = 'ospfv3-act'
                _revision = '2016-09-14'

                def __init__(self):
                    super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive, self).__init__()

                    self.yang_name = "all-inclusive"
                    self.yang_parent_name = "instance"

                    self.process = YLeaf(YType.empty, "process")

                    self.redistribution = YLeaf(YType.empty, "redistribution")

                    self.route = YLeaf(YType.empty, "route")

                    self.stats = ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats()
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
                                super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive, self).__setattr__(name, value)


                class Stats(Entity):
                    """
                    OSPFv3 counters and statistics
                    
                    .. attribute:: neighbor
                    
                    	Neighbor statistics per interface or neighbor id
                    	**type**\:   :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor>`
                    
                    .. attribute:: prefix_priority
                    
                    	SPF Prefix Priority statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: spf
                    
                    	SPF statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ospfv3-act'
                    _revision = '2016-09-14'

                    def __init__(self):
                        super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats, self).__init__()

                        self.yang_name = "stats"
                        self.yang_parent_name = "all-inclusive"

                        self.prefix_priority = YLeaf(YType.empty, "prefix-priority")

                        self.spf = YLeaf(YType.empty, "spf")

                        self.neighbor = ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor()
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
                            if name in ("prefix_priority",
                                        "spf") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats, self).__setattr__(name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor statistics per interface or neighbor id
                        
                        .. attribute:: interface
                        
                        	
                        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_act.ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface>`
                        
                        .. attribute:: neighbor_id
                        
                        	Neighbor ID
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ospfv3-act'
                        _revision = '2016-09-14'

                        def __init__(self):
                            super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "stats"

                            self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                            self.interface = ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
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
                                        super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor, self).__setattr__(name, value)


                        class Interface(Entity):
                            """
                            
                            
                            .. attribute:: interface_name
                            
                            	OSPFv3 interface statistics
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            

                            """

                            _prefix = 'ospfv3-act'
                            _revision = '2016-09-14'

                            def __init__(self):
                                super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__init__()

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
                                            super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface, self).__setattr__(name, value)

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
                                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/all-inclusive/stats/neighbor/%s" % self.get_segment_path()
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
                                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/all-inclusive/stats/%s" % self.get_segment_path()
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
                                    self.interface = ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor.Interface()
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
                            self.prefix_priority.is_set or
                            self.spf.is_set or
                            (self.neighbor is not None and self.neighbor.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.prefix_priority.yfilter != YFilter.not_set or
                            self.spf.yfilter != YFilter.not_set or
                            (self.neighbor is not None and self.neighbor.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "stats" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/all-inclusive/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.prefix_priority.is_set or self.prefix_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_priority.get_name_leafdata())
                        if (self.spf.is_set or self.spf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.spf.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "neighbor"):
                            if (self.neighbor is None):
                                self.neighbor = ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats.Neighbor()
                                self.neighbor.parent = self
                                self._children_name_map["neighbor"] = "neighbor"
                            return self.neighbor

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "neighbor" or name == "prefix-priority" or name == "spf"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "prefix-priority"):
                            self.prefix_priority = value
                            self.prefix_priority.value_namespace = name_space
                            self.prefix_priority.value_namespace_prefix = name_space_prefix
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
                        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/instance/%s" % self.get_segment_path()
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
                            self.stats = ActOspfv3InstanceVrf.Input.Instance.AllInclusive.Stats()
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
                    path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/input/%s" % self.get_segment_path()
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
                        self.all = ActOspfv3InstanceVrf.Input.Instance.All()
                        self.all.parent = self
                        self._children_name_map["all"] = "all"
                    return self.all

                if (child_yang_name == "all-inclusive"):
                    if (self.all_inclusive is None):
                        self.all_inclusive = ActOspfv3InstanceVrf.Input.Instance.AllInclusive()
                        self.all_inclusive.parent = self
                        self._children_name_map["all_inclusive"] = "all-inclusive"
                    return self.all_inclusive

                if (child_yang_name == "vrf"):
                    if (self.vrf is None):
                        self.vrf = ActOspfv3InstanceVrf.Input.Instance.Vrf()
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
                path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf/%s" % self.get_segment_path()
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
                    self.instance = ActOspfv3InstanceVrf.Input.Instance()
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
        path_buffer = "Cisco-IOS-XR-ipv6-ospfv3-act:act-ospfv3-instance-vrf" + path_buffer

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
                self.input = ActOspfv3InstanceVrf.Input()
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
        self._top_entity = ActOspfv3InstanceVrf()
        return self._top_entity

