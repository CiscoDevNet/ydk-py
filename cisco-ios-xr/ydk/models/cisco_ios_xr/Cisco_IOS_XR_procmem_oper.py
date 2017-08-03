""" Cisco_IOS_XR_procmem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR procmem package operational data.

This module contains definitions
for the following management objects\:
  processes\-memory\: Process statistics

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ProcessesMemory(Entity):
    """
    Process statistics
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes>`
    
    

    """

    _prefix = 'procmem-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ProcessesMemory, self).__init__()
        self._top_entity = None

        self.yang_name = "processes-memory"
        self.yang_parent_name = "Cisco-IOS-XR-procmem-oper"

        self.nodes = ProcessesMemory.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node>`
        
        

        """

        _prefix = 'procmem-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ProcessesMemory.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "processes-memory"

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
                        super(ProcessesMemory.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ProcessesMemory.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node ID
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process_ids
            
            	List of jobs
            	**type**\:   :py:class:`ProcessIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node.ProcessIds>`
            
            

            """

            _prefix = 'procmem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ProcessesMemory.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.process_ids = ProcessesMemory.Nodes.Node.ProcessIds()
                self.process_ids.parent = self
                self._children_name_map["process_ids"] = "process-ids"
                self._children_yang_names.add("process-ids")

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
                            super(ProcessesMemory.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ProcessesMemory.Nodes.Node, self).__setattr__(name, value)


            class ProcessIds(Entity):
                """
                List of jobs
                
                .. attribute:: process_id
                
                	Process Id
                	**type**\: list of    :py:class:`ProcessId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node.ProcessIds.ProcessId>`
                
                

                """

                _prefix = 'procmem-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ProcessesMemory.Nodes.Node.ProcessIds, self).__init__()

                    self.yang_name = "process-ids"
                    self.yang_parent_name = "node"

                    self.process_id = YList(self)

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
                                super(ProcessesMemory.Nodes.Node.ProcessIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ProcessesMemory.Nodes.Node.ProcessIds, self).__setattr__(name, value)


                class ProcessId(Entity):
                    """
                    Process Id
                    
                    .. attribute:: process_id  <key>
                    
                    	Process Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: data_seg_size
                    
                    	Data Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dyn_limit
                    
                    	Dynamic memory limit
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: malloc_size
                    
                    	Malloced Memory Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\:  str
                    
                    .. attribute:: physical_mem
                    
                    	Physical memory size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pid
                    
                    	Process ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shared_mem
                    
                    	Shared memory size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stack_seg_size
                    
                    	Stack Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: text_seg_size
                    
                    	Text Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'procmem-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ProcessesMemory.Nodes.Node.ProcessIds.ProcessId, self).__init__()

                        self.yang_name = "process-id"
                        self.yang_parent_name = "process-ids"

                        self.process_id = YLeaf(YType.int32, "process-id")

                        self.data_seg_size = YLeaf(YType.uint32, "data-seg-size")

                        self.dyn_limit = YLeaf(YType.uint32, "dyn-limit")

                        self.jid = YLeaf(YType.uint32, "jid")

                        self.malloc_size = YLeaf(YType.uint32, "malloc-size")

                        self.name = YLeaf(YType.str, "name")

                        self.physical_mem = YLeaf(YType.uint32, "physical-mem")

                        self.pid = YLeaf(YType.uint32, "pid")

                        self.shared_mem = YLeaf(YType.uint32, "shared-mem")

                        self.stack_seg_size = YLeaf(YType.uint32, "stack-seg-size")

                        self.text_seg_size = YLeaf(YType.uint32, "text-seg-size")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("process_id",
                                        "data_seg_size",
                                        "dyn_limit",
                                        "jid",
                                        "malloc_size",
                                        "name",
                                        "physical_mem",
                                        "pid",
                                        "shared_mem",
                                        "stack_seg_size",
                                        "text_seg_size") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ProcessesMemory.Nodes.Node.ProcessIds.ProcessId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ProcessesMemory.Nodes.Node.ProcessIds.ProcessId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.process_id.is_set or
                            self.data_seg_size.is_set or
                            self.dyn_limit.is_set or
                            self.jid.is_set or
                            self.malloc_size.is_set or
                            self.name.is_set or
                            self.physical_mem.is_set or
                            self.pid.is_set or
                            self.shared_mem.is_set or
                            self.stack_seg_size.is_set or
                            self.text_seg_size.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.process_id.yfilter != YFilter.not_set or
                            self.data_seg_size.yfilter != YFilter.not_set or
                            self.dyn_limit.yfilter != YFilter.not_set or
                            self.jid.yfilter != YFilter.not_set or
                            self.malloc_size.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.physical_mem.yfilter != YFilter.not_set or
                            self.pid.yfilter != YFilter.not_set or
                            self.shared_mem.yfilter != YFilter.not_set or
                            self.stack_seg_size.yfilter != YFilter.not_set or
                            self.text_seg_size.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "process-id" + "[process-id='" + self.process_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.process_id.get_name_leafdata())
                        if (self.data_seg_size.is_set or self.data_seg_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.data_seg_size.get_name_leafdata())
                        if (self.dyn_limit.is_set or self.dyn_limit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dyn_limit.get_name_leafdata())
                        if (self.jid.is_set or self.jid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.jid.get_name_leafdata())
                        if (self.malloc_size.is_set or self.malloc_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.malloc_size.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.physical_mem.is_set or self.physical_mem.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.physical_mem.get_name_leafdata())
                        if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pid.get_name_leafdata())
                        if (self.shared_mem.is_set or self.shared_mem.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.shared_mem.get_name_leafdata())
                        if (self.stack_seg_size.is_set or self.stack_seg_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.stack_seg_size.get_name_leafdata())
                        if (self.text_seg_size.is_set or self.text_seg_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.text_seg_size.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "process-id" or name == "data-seg-size" or name == "dyn-limit" or name == "jid" or name == "malloc-size" or name == "name" or name == "physical-mem" or name == "pid" or name == "shared-mem" or name == "stack-seg-size" or name == "text-seg-size"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "process-id"):
                            self.process_id = value
                            self.process_id.value_namespace = name_space
                            self.process_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "data-seg-size"):
                            self.data_seg_size = value
                            self.data_seg_size.value_namespace = name_space
                            self.data_seg_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "dyn-limit"):
                            self.dyn_limit = value
                            self.dyn_limit.value_namespace = name_space
                            self.dyn_limit.value_namespace_prefix = name_space_prefix
                        if(value_path == "jid"):
                            self.jid = value
                            self.jid.value_namespace = name_space
                            self.jid.value_namespace_prefix = name_space_prefix
                        if(value_path == "malloc-size"):
                            self.malloc_size = value
                            self.malloc_size.value_namespace = name_space
                            self.malloc_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "physical-mem"):
                            self.physical_mem = value
                            self.physical_mem.value_namespace = name_space
                            self.physical_mem.value_namespace_prefix = name_space_prefix
                        if(value_path == "pid"):
                            self.pid = value
                            self.pid.value_namespace = name_space
                            self.pid.value_namespace_prefix = name_space_prefix
                        if(value_path == "shared-mem"):
                            self.shared_mem = value
                            self.shared_mem.value_namespace = name_space
                            self.shared_mem.value_namespace_prefix = name_space_prefix
                        if(value_path == "stack-seg-size"):
                            self.stack_seg_size = value
                            self.stack_seg_size.value_namespace = name_space
                            self.stack_seg_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "text-seg-size"):
                            self.text_seg_size = value
                            self.text_seg_size.value_namespace = name_space
                            self.text_seg_size.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.process_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.process_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "process-ids" + path_buffer

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

                    if (child_yang_name == "process-id"):
                        for c in self.process_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ProcessesMemory.Nodes.Node.ProcessIds.ProcessId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.process_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "process-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.process_ids is not None and self.process_ids.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.process_ids is not None and self.process_ids.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-procmem-oper:processes-memory/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "process-ids"):
                    if (self.process_ids is None):
                        self.process_ids = ProcessesMemory.Nodes.Node.ProcessIds()
                        self.process_ids.parent = self
                        self._children_name_map["process_ids"] = "process-ids"
                    return self.process_ids

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "process-ids" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-procmem-oper:processes-memory/%s" % self.get_segment_path()
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
                c = ProcessesMemory.Nodes.Node()
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
        path_buffer = "Cisco-IOS-XR-procmem-oper:processes-memory" + path_buffer

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
                self.nodes = ProcessesMemory.Nodes()
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
        self._top_entity = ProcessesMemory()
        return self._top_entity

