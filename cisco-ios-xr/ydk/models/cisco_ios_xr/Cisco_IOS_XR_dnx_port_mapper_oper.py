""" Cisco_IOS_XR_dnx_port_mapper_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR dnx\-port\-mapper package operational data.

This module contains definitions
for the following management objects\:
  oor\: Out of Resource Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Oor(Entity):
    """
    Out of Resource Data
    
    .. attribute:: nodes
    
    	OOR data for available nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes>`
    
    

    """

    _prefix = 'dnx-port-mapper-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Oor, self).__init__()
        self._top_entity = None

        self.yang_name = "oor"
        self.yang_parent_name = "Cisco-IOS-XR-dnx-port-mapper-oper"

        self.nodes = Oor.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        OOR data for available nodes
        
        .. attribute:: node
        
        	DPA operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node>`
        
        

        """

        _prefix = 'dnx-port-mapper-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Oor.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "oor"

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
                        super(Oor.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Oor.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            DPA operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node ID
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: interface_names
            
            	OOR Interface Information
            	**type**\:   :py:class:`InterfaceNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames>`
            
            .. attribute:: summary
            
            	Summary
            	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.Summary>`
            
            

            """

            _prefix = 'dnx-port-mapper-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Oor.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.interface_names = Oor.Nodes.Node.InterfaceNames()
                self.interface_names.parent = self
                self._children_name_map["interface_names"] = "interface-names"
                self._children_yang_names.add("interface-names")

                self.summary = Oor.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Oor.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Oor.Nodes.Node, self).__setattr__(name, value)


            class Summary(Entity):
                """
                Summary
                
                .. attribute:: green
                
                	interfaces in green state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: red
                
                	interfaces in red state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: yel_low
                
                	interfaces in yellow state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Oor.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"

                    self.green = YLeaf(YType.uint32, "green")

                    self.red = YLeaf(YType.uint32, "red")

                    self.yel_low = YLeaf(YType.uint32, "yel-low")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("green",
                                    "red",
                                    "yel_low") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Oor.Nodes.Node.Summary, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Oor.Nodes.Node.Summary, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.green.is_set or
                        self.red.is_set or
                        self.yel_low.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.green.yfilter != YFilter.not_set or
                        self.red.yfilter != YFilter.not_set or
                        self.yel_low.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "summary" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.green.is_set or self.green.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.green.get_name_leafdata())
                    if (self.red.is_set or self.red.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.red.get_name_leafdata())
                    if (self.yel_low.is_set or self.yel_low.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.yel_low.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "green" or name == "red" or name == "yel-low"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "green"):
                        self.green = value
                        self.green.value_namespace = name_space
                        self.green.value_namespace_prefix = name_space_prefix
                    if(value_path == "red"):
                        self.red = value
                        self.red.value_namespace = name_space
                        self.red.value_namespace_prefix = name_space_prefix
                    if(value_path == "yel-low"):
                        self.yel_low = value
                        self.yel_low.value_namespace = name_space
                        self.yel_low.value_namespace_prefix = name_space_prefix


            class InterfaceNames(Entity):
                """
                OOR Interface Information
                
                .. attribute:: interface_name
                
                	OOR Data for particular interface
                	**type**\: list of    :py:class:`InterfaceName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames.InterfaceName>`
                
                

                """

                _prefix = 'dnx-port-mapper-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Oor.Nodes.Node.InterfaceNames, self).__init__()

                    self.yang_name = "interface-names"
                    self.yang_parent_name = "node"

                    self.interface_name = YList(self)

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
                                super(Oor.Nodes.Node.InterfaceNames, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Oor.Nodes.Node.InterfaceNames, self).__setattr__(name, value)


                class InterfaceName(Entity):
                    """
                    OOR Data for particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of the interface
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface
                    
                    	Interface details
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper.Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface>`
                    
                    

                    """

                    _prefix = 'dnx-port-mapper-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Oor.Nodes.Node.InterfaceNames.InterfaceName, self).__init__()

                        self.yang_name = "interface-name"
                        self.yang_parent_name = "interface-names"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.interface = YList(self)

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
                                    super(Oor.Nodes.Node.InterfaceNames.InterfaceName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Oor.Nodes.Node.InterfaceNames.InterfaceName, self).__setattr__(name, value)


                    class Interface(Entity):
                        """
                        Interface details
                        
                        .. attribute:: hardware_resource
                        
                        	Type of harware resoruce
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	Name of the interface
                        	**type**\:  str
                        
                        .. attribute:: interface_status
                        
                        	The current state of the interface
                        	**type**\:  str
                        
                        .. attribute:: npu_id
                        
                        	Npuid of the interface
                        	**type**\:  str
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'dnx-port-mapper-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interface-name"

                            self.hardware_resource = YLeaf(YType.str, "hardware-resource")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_status = YLeaf(YType.str, "interface-status")

                            self.npu_id = YLeaf(YType.str, "npu-id")

                            self.time_stamp = YLeaf(YType.str, "time-stamp")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("hardware_resource",
                                            "interface_name",
                                            "interface_status",
                                            "npu_id",
                                            "time_stamp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.hardware_resource.is_set or
                                self.interface_name.is_set or
                                self.interface_status.is_set or
                                self.npu_id.is_set or
                                self.time_stamp.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.hardware_resource.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.interface_status.yfilter != YFilter.not_set or
                                self.npu_id.yfilter != YFilter.not_set or
                                self.time_stamp.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.hardware_resource.is_set or self.hardware_resource.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hardware_resource.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.interface_status.is_set or self.interface_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_status.get_name_leafdata())
                            if (self.npu_id.is_set or self.npu_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.npu_id.get_name_leafdata())
                            if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_stamp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "hardware-resource" or name == "interface-name" or name == "interface-status" or name == "npu-id" or name == "time-stamp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "hardware-resource"):
                                self.hardware_resource = value
                                self.hardware_resource.value_namespace = name_space
                                self.hardware_resource.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-status"):
                                self.interface_status = value
                                self.interface_status.value_namespace = name_space
                                self.interface_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "npu-id"):
                                self.npu_id = value
                                self.npu_id.value_namespace = name_space
                                self.npu_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-stamp"):
                                self.time_stamp = value
                                self.time_stamp.value_namespace = name_space
                                self.time_stamp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.interface:
                            if (c.has_data()):
                                return True
                        return self.interface_name.is_set

                    def has_operation(self):
                        for c in self.interface:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface-name" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                        if (child_yang_name == "interface"):
                            for c in self.interface:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Oor.Nodes.Node.InterfaceNames.InterfaceName.Interface()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.interface.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface_name:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface_name:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface-names" + path_buffer

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

                    if (child_yang_name == "interface-name"):
                        for c in self.interface_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Oor.Nodes.Node.InterfaceNames.InterfaceName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface_name.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.interface_names is not None and self.interface_names.has_data()) or
                    (self.summary is not None and self.summary.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.interface_names is not None and self.interface_names.has_operation()) or
                    (self.summary is not None and self.summary.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-dnx-port-mapper-oper:oor/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface-names"):
                    if (self.interface_names is None):
                        self.interface_names = Oor.Nodes.Node.InterfaceNames()
                        self.interface_names.parent = self
                        self._children_name_map["interface_names"] = "interface-names"
                    return self.interface_names

                if (child_yang_name == "summary"):
                    if (self.summary is None):
                        self.summary = Oor.Nodes.Node.Summary()
                        self.summary.parent = self
                        self._children_name_map["summary"] = "summary"
                    return self.summary

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-names" or name == "summary" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-dnx-port-mapper-oper:oor/%s" % self.get_segment_path()
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
                c = Oor.Nodes.Node()
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
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-dnx-port-mapper-oper:oor" + path_buffer

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
                self.nodes = Oor.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Oor()
        return self._top_entity

