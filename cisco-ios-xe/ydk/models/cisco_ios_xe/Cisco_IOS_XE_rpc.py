""" Cisco_IOS_XE_rpc 

NED RPC YANG module for IOS
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Switch(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(Switch, self).__init__()
        self._top_entity = None

        self.yang_name = "switch"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"

        self.input = Switch.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Switch.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: priority
        
        	<1\-15>  Switch Priority
        	**type**\:  int
        
        	**range:** 1..15
        
        .. attribute:: renumber
        
        	<1\-9>  New number of the Switch
        	**type**\:  int
        
        	**range:** 1..9
        
        .. attribute:: statck
        
        	
        	**type**\:   :py:class:`Statck <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Switch.Input.Statck>`
        
        .. attribute:: switch_number
        
        	
        	**type**\:  int
        
        	**range:** 1..9
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Switch.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "switch"

            self.priority = YLeaf(YType.uint8, "priority")

            self.renumber = YLeaf(YType.uint8, "renumber")

            self.switch_number = YLeaf(YType.uint8, "switch-number")

            self.statck = Switch.Input.Statck()
            self.statck.parent = self
            self._children_name_map["statck"] = "statck"
            self._children_yang_names.add("statck")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("priority",
                            "renumber",
                            "switch_number") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Switch.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Switch.Input, self).__setattr__(name, value)


        class Statck(Entity):
            """
            
            
            .. attribute:: port
            
            	<1\-2>  Stack port number to enable/disable
            	**type**\:  int
            
            	**range:** 1..2
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-02-07'

            def __init__(self):
                super(Switch.Input.Statck, self).__init__()

                self.yang_name = "statck"
                self.yang_parent_name = "input"

                self.port = YLeaf(YType.uint8, "port")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("port") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Switch.Input.Statck, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Switch.Input.Statck, self).__setattr__(name, value)

            def has_data(self):
                return self.port.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.port.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statck" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-rpc:switch/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.port.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "port"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "port"):
                    self.port = value
                    self.port.value_namespace = name_space
                    self.port.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.priority.is_set or
                self.renumber.is_set or
                self.switch_number.is_set or
                (self.statck is not None and self.statck.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.priority.yfilter != YFilter.not_set or
                self.renumber.yfilter != YFilter.not_set or
                self.switch_number.yfilter != YFilter.not_set or
                (self.statck is not None and self.statck.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-rpc:switch/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                leaf_name_data.append(self.priority.get_name_leafdata())
            if (self.renumber.is_set or self.renumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.renumber.get_name_leafdata())
            if (self.switch_number.is_set or self.switch_number.yfilter != YFilter.not_set):
                leaf_name_data.append(self.switch_number.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "statck"):
                if (self.statck is None):
                    self.statck = Switch.Input.Statck()
                    self.statck.parent = self
                    self._children_name_map["statck"] = "statck"
                return self.statck

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "statck" or name == "priority" or name == "renumber" or name == "switch-number"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "priority"):
                self.priority = value
                self.priority.value_namespace = name_space
                self.priority.value_namespace_prefix = name_space_prefix
            if(value_path == "renumber"):
                self.renumber = value
                self.renumber.value_namespace = name_space
                self.renumber.value_namespace_prefix = name_space_prefix
            if(value_path == "switch-number"):
                self.switch_number = value
                self.switch_number.value_namespace = name_space
                self.switch_number.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Switch.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "switch"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Switch.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Switch.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-rpc:switch/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-rpc:switch" + path_buffer

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
                self.input = Switch.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Switch.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Switch()
        return self._top_entity

class Default(Entity):
    """
    Set a command to its defaults
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Default.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(Default, self).__init__()
        self._top_entity = None

        self.yang_name = "default"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"

        self.input = Default.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = Default.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: interface
        
        	Select an interface to configure
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Default.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "default"

            self.interface = YLeaf(YType.str, "interface")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("interface") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Default.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Default.Input, self).__setattr__(name, value)

        def has_data(self):
            return self.interface.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.interface.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-rpc:default/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "interface"):
                self.interface = value
                self.interface.value_namespace = name_space
                self.interface.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Default.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "default"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Default.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Default.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-rpc:default/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-rpc:default" + path_buffer

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
                self.input = Default.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Default.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Default()
        return self._top_entity

class Reload(Entity):
    """
    Halt and perform a cold restart
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.Reload.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(Reload, self).__init__()
        self._top_entity = None

        self.yang_name = "reload"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"

        self.output = Reload.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(Reload.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "reload"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Reload.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Reload.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-rpc:reload/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.output is not None and self.output.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-rpc:reload" + path_buffer

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

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = Reload.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Reload()
        return self._top_entity

class License(Entity):
    """
    
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Output>`
    
    

    """

    _prefix = 'ios-xe-rpc'
    _revision = '2017-02-07'

    def __init__(self):
        super(License, self).__init__()
        self._top_entity = None

        self.yang_name = "license"
        self.yang_parent_name = "Cisco-IOS-XE-rpc"

        self.input = License.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = License.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: smart
        
        	
        	**type**\:   :py:class:`Smart <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart>`
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(License.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "license"

            self.smart = License.Input.Smart()
            self.smart.parent = self
            self._children_name_map["smart"] = "smart"
            self._children_yang_names.add("smart")


        class Smart(Entity):
            """
            
            
            .. attribute:: deregister
            
            	
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: register
            
            	
            	**type**\:   :py:class:`Register <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Register>`
            
            .. attribute:: renew
            
            	
            	**type**\:   :py:class:`Renew <ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc.License.Input.Smart.Renew>`
            
            

            """

            _prefix = 'ios-xe-rpc'
            _revision = '2017-02-07'

            def __init__(self):
                super(License.Input.Smart, self).__init__()

                self.yang_name = "smart"
                self.yang_parent_name = "input"

                self.deregister = YLeaf(YType.empty, "deregister")

                self.register = License.Input.Smart.Register()
                self.register.parent = self
                self._children_name_map["register"] = "register"
                self._children_yang_names.add("register")

                self.renew = License.Input.Smart.Renew()
                self.renew.parent = self
                self._children_name_map["renew"] = "renew"
                self._children_yang_names.add("renew")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("deregister") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(License.Input.Smart, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(License.Input.Smart, self).__setattr__(name, value)


            class Register(Entity):
                """
                
                
                .. attribute:: idtoken
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-02-07'

                def __init__(self):
                    super(License.Input.Smart.Register, self).__init__()

                    self.yang_name = "register"
                    self.yang_parent_name = "smart"

                    self.idtoken = YLeaf(YType.empty, "idtoken")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("idtoken") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(License.Input.Smart.Register, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(License.Input.Smart.Register, self).__setattr__(name, value)

                def has_data(self):
                    return self.idtoken.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.idtoken.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "register" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XE-rpc:license/input/smart/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.idtoken.is_set or self.idtoken.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.idtoken.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "idtoken"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "idtoken"):
                        self.idtoken = value
                        self.idtoken.value_namespace = name_space
                        self.idtoken.value_namespace_prefix = name_space_prefix


            class Renew(Entity):
                """
                
                
                .. attribute:: auth
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: id
                
                	
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ios-xe-rpc'
                _revision = '2017-02-07'

                def __init__(self):
                    super(License.Input.Smart.Renew, self).__init__()

                    self.yang_name = "renew"
                    self.yang_parent_name = "smart"

                    self.auth = YLeaf(YType.empty, "auth")

                    self.id = YLeaf(YType.empty, "id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("auth",
                                    "id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(License.Input.Smart.Renew, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(License.Input.Smart.Renew, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.auth.is_set or
                        self.id.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.auth.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "renew" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XE-rpc:license/input/smart/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.auth.is_set or self.auth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth.get_name_leafdata())
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "auth" or name == "id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "auth"):
                        self.auth = value
                        self.auth.value_namespace = name_space
                        self.auth.value_namespace_prefix = name_space_prefix
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.deregister.is_set or
                    (self.register is not None and self.register.has_data()) or
                    (self.renew is not None and self.renew.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.deregister.yfilter != YFilter.not_set or
                    (self.register is not None and self.register.has_operation()) or
                    (self.renew is not None and self.renew.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "smart" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-rpc:license/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.deregister.is_set or self.deregister.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.deregister.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "register"):
                    if (self.register is None):
                        self.register = License.Input.Smart.Register()
                        self.register.parent = self
                        self._children_name_map["register"] = "register"
                    return self.register

                if (child_yang_name == "renew"):
                    if (self.renew is None):
                        self.renew = License.Input.Smart.Renew()
                        self.renew.parent = self
                        self._children_name_map["renew"] = "renew"
                    return self.renew

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "register" or name == "renew" or name == "deregister"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "deregister"):
                    self.deregister = value
                    self.deregister.value_namespace = name_space
                    self.deregister.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (self.smart is not None and self.smart.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.smart is not None and self.smart.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-rpc:license/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "smart"):
                if (self.smart is None):
                    self.smart = License.Input.Smart()
                    self.smart.parent = self
                    self._children_name_map["smart"] = "smart"
                return self.smart

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "smart"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Output(Entity):
        """
        
        
        .. attribute:: result
        
        	Output returned by the network element
        	**type**\:  str
        
        

        """

        _prefix = 'ios-xe-rpc'
        _revision = '2017-02-07'

        def __init__(self):
            super(License.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "license"

            self.result = YLeaf(YType.str, "result")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("result") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(License.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(License.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.result.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.result.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-rpc:license/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.result.is_set or self.result.yfilter != YFilter.not_set):
                leaf_name_data.append(self.result.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "result"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "result"):
                self.result = value
                self.result.value_namespace = name_space
                self.result.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-rpc:license" + path_buffer

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
                self.input = License.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = License.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = License()
        return self._top_entity

