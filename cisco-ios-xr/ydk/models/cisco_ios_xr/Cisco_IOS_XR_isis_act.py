""" Cisco_IOS_XR_isis_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ISIS action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ClearIsisProcess(Entity):
    """
    Clear all IS\-IS data structures
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisProcess.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisProcess, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-process"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"

        self.input = ClearIsisProcess.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisProcess.Input.Instance>`
        
        .. attribute:: process
        
        	Clear all IS\-IS data structures
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisProcess.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-process"

            self.process = YLeaf(YType.empty, "process")

            self.instance = ClearIsisProcess.Input.Instance()
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
                        super(ClearIsisProcess.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearIsisProcess.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisProcess.Input.Instance, self).__init__()

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
                            super(ClearIsisProcess.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ClearIsisProcess.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-process/input/%s" % self.get_segment_path()
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
                path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-process/%s" % self.get_segment_path()
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
                    self.instance = ClearIsisProcess.Input.Instance()
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
        path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-process" + path_buffer

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
                self.input = ClearIsisProcess.Input()
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
        self._top_entity = ClearIsisProcess()
        return self._top_entity

class ClearIsisRoute(Entity):
    """
    Clear IS\-IS routes
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRoute.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisRoute, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-route"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"

        self.input = ClearIsisRoute.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisRoute.Input.Instance>`
        
        .. attribute:: route
        
        	Clear IS\-IS routes
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisRoute.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-route"

            self.route = YLeaf(YType.empty, "route")

            self.instance = ClearIsisRoute.Input.Instance()
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
                        super(ClearIsisRoute.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearIsisRoute.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisRoute.Input.Instance, self).__init__()

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
                            super(ClearIsisRoute.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ClearIsisRoute.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-route/input/%s" % self.get_segment_path()
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
                path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-route/%s" % self.get_segment_path()
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
                    self.instance = ClearIsisRoute.Input.Instance()
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
        path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-route" + path_buffer

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
                self.input = ClearIsisRoute.Input()
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
        self._top_entity = ClearIsisRoute()
        return self._top_entity

class ClearIsisStat(Entity):
    """
    Clear IS\-IS protocol statistics
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStat.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisStat, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-stat"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"

        self.input = ClearIsisStat.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStat.Input.Instance>`
        
        .. attribute:: statistics
        
        	Clear IS\-IS protocol statistics
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisStat.Input.Statistics>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisStat.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-stat"

            self.instance = ClearIsisStat.Input.Instance()
            self.instance.parent = self
            self._children_name_map["instance"] = "instance"
            self._children_yang_names.add("instance")

            self.statistics = ClearIsisStat.Input.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")


        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisStat.Input.Instance, self).__init__()

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
                            super(ClearIsisStat.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ClearIsisStat.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-stat/input/%s" % self.get_segment_path()
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


        class Statistics(Entity):
            """
            Clear IS\-IS protocol statistics
            
            .. attribute:: interface_name
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisStat.Input.Statistics, self).__init__()

                self.yang_name = "statistics"
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
                            super(ClearIsisStat.Input.Statistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ClearIsisStat.Input.Statistics, self).__setattr__(name, value)

            def has_data(self):
                return self.interface_name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-stat/input/%s" % self.get_segment_path()
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
                (self.statistics is not None and self.statistics.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()) or
                (self.statistics is not None and self.statistics.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-stat/%s" % self.get_segment_path()
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
                    self.instance = ClearIsisStat.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            if (child_yang_name == "statistics"):
                if (self.statistics is None):
                    self.statistics = ClearIsisStat.Input.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                return self.statistics

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "statistics"):
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
        path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-stat" + path_buffer

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
                self.input = ClearIsisStat.Input()
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
        self._top_entity = ClearIsisStat()
        return self._top_entity

class ClearIsisDist(Entity):
    """
    Reset BGP\-LS topology distribution
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisDist.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsisDist, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis-dist"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"

        self.input = ClearIsisDist.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: distribution
        
        	Reset BGP\-LS topology distribution
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: instance
        
        	Reset BGP\-LS topology from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsisDist.Input.Instance>`
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsisDist.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis-dist"

            self.distribution = YLeaf(YType.empty, "distribution")

            self.instance = ClearIsisDist.Input.Instance()
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
                if name in ("distribution") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ClearIsisDist.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearIsisDist.Input, self).__setattr__(name, value)


        class Instance(Entity):
            """
            Reset BGP\-LS topology from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsisDist.Input.Instance, self).__init__()

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
                            super(ClearIsisDist.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ClearIsisDist.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-dist/input/%s" % self.get_segment_path()
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
                self.distribution.is_set or
                (self.instance is not None and self.instance.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.distribution.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-dist/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.distribution.is_set or self.distribution.yfilter != YFilter.not_set):
                leaf_name_data.append(self.distribution.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ClearIsisDist.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "distribution"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "distribution"):
                self.distribution = value
                self.distribution.value_namespace = name_space
                self.distribution.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-isis-act:clear-isis-dist" + path_buffer

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
                self.input = ClearIsisDist.Input()
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
        self._top_entity = ClearIsisDist()
        return self._top_entity

class ClearIsis(Entity):
    """
    Clear IS\-IS data structures
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsis.Input>`
    
    

    """

    _prefix = 'isis-act'
    _revision = '2016-06-30'

    def __init__(self):
        super(ClearIsis, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-isis"
        self.yang_parent_name = "Cisco-IOS-XR-isis-act"

        self.input = ClearIsis.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: instance
        
        	Clear data from single IS\-IS instance
        	**type**\:   :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsis.Input.Instance>`
        
        .. attribute:: route
        
        	Clear IS\-IS routes
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: rt_type
        
        	Clear data for these route types
        	**type**\:   :py:class:`RtType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_isis_act.ClearIsis.Input.RtType>`
        
        .. attribute:: topology
        
        	Topology table information
        	**type**\:  str
        
        

        """

        _prefix = 'isis-act'
        _revision = '2016-06-30'

        def __init__(self):
            super(ClearIsis.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-isis"

            self.route = YLeaf(YType.empty, "route")

            self.rt_type = YLeaf(YType.enumeration, "rt-type")

            self.topology = YLeaf(YType.str, "topology")

            self.instance = ClearIsis.Input.Instance()
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
                if name in ("route",
                            "rt_type",
                            "topology") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ClearIsis.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearIsis.Input, self).__setattr__(name, value)

        class RtType(Enum):
            """
            RtType

            Clear data for these route types

            .. data:: AFI_ALL_MULTICAST = 0

            .. data:: AFI_ALL_SAFI_ALL = 1

            .. data:: AFI_ALL_UNICAST = 2

            .. data:: IPv4_MULTICAST = 3

            .. data:: IPv4_SAFI_ALL = 4

            .. data:: IPv4_UNICAST = 5

            .. data:: IPv6_MULTICAST = 6

            .. data:: IPv6_SAFI_ALL = 7

            .. data:: IPv6_UNICAST = 8

            """

            AFI_ALL_MULTICAST = Enum.YLeaf(0, "AFI-ALL-MULTICAST")

            AFI_ALL_SAFI_ALL = Enum.YLeaf(1, "AFI-ALL-SAFI-ALL")

            AFI_ALL_UNICAST = Enum.YLeaf(2, "AFI-ALL-UNICAST")

            IPv4_MULTICAST = Enum.YLeaf(3, "IPv4-MULTICAST")

            IPv4_SAFI_ALL = Enum.YLeaf(4, "IPv4-SAFI-ALL")

            IPv4_UNICAST = Enum.YLeaf(5, "IPv4-UNICAST")

            IPv6_MULTICAST = Enum.YLeaf(6, "IPv6-MULTICAST")

            IPv6_SAFI_ALL = Enum.YLeaf(7, "IPv6-SAFI-ALL")

            IPv6_UNICAST = Enum.YLeaf(8, "IPv6-UNICAST")



        class Instance(Entity):
            """
            Clear data from single IS\-IS instance
            
            .. attribute:: instance_identifier
            
            	IS\-IS process instance identifier
            	**type**\:  str
            
            

            """

            _prefix = 'isis-act'
            _revision = '2016-06-30'

            def __init__(self):
                super(ClearIsis.Input.Instance, self).__init__()

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
                            super(ClearIsis.Input.Instance, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ClearIsis.Input.Instance, self).__setattr__(name, value)

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
                    path_buffer = "Cisco-IOS-XR-isis-act:clear-isis/input/%s" % self.get_segment_path()
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
                self.rt_type.is_set or
                self.topology.is_set or
                (self.instance is not None and self.instance.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.route.yfilter != YFilter.not_set or
                self.rt_type.yfilter != YFilter.not_set or
                self.topology.yfilter != YFilter.not_set or
                (self.instance is not None and self.instance.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-isis-act:clear-isis/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.route.is_set or self.route.yfilter != YFilter.not_set):
                leaf_name_data.append(self.route.get_name_leafdata())
            if (self.rt_type.is_set or self.rt_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rt_type.get_name_leafdata())
            if (self.topology.is_set or self.topology.yfilter != YFilter.not_set):
                leaf_name_data.append(self.topology.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "instance"):
                if (self.instance is None):
                    self.instance = ClearIsis.Input.Instance()
                    self.instance.parent = self
                    self._children_name_map["instance"] = "instance"
                return self.instance

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "instance" or name == "route" or name == "rt-type" or name == "topology"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "route"):
                self.route = value
                self.route.value_namespace = name_space
                self.route.value_namespace_prefix = name_space_prefix
            if(value_path == "rt-type"):
                self.rt_type = value
                self.rt_type.value_namespace = name_space
                self.rt_type.value_namespace_prefix = name_space_prefix
            if(value_path == "topology"):
                self.topology = value
                self.topology.value_namespace = name_space
                self.topology.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-isis-act:clear-isis" + path_buffer

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
                self.input = ClearIsis.Input()
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
        self._top_entity = ClearIsis()
        return self._top_entity

