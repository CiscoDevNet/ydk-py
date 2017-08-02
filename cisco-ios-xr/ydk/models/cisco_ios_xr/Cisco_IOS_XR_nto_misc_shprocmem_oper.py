""" Cisco_IOS_XR_nto_misc_shprocmem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR nto\-misc\-shprocmem package operational data.

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
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes>`
    
    

    """

    _prefix = 'nto-misc-shprocmem-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ProcessesMemory, self).__init__()
        self._top_entity = None

        self.yang_name = "processes-memory"
        self.yang_parent_name = "Cisco-IOS-XR-nto-misc-shprocmem-oper"

        self.nodes = ProcessesMemory.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes.Node>`
        
        

        """

        _prefix = 'nto-misc-shprocmem-oper'
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
            
            .. attribute:: job_ids
            
            	List of jobs
            	**type**\:   :py:class:`JobIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes.Node.JobIds>`
            
            

            """

            _prefix = 'nto-misc-shprocmem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ProcessesMemory.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.job_ids = ProcessesMemory.Nodes.Node.JobIds()
                self.job_ids.parent = self
                self._children_name_map["job_ids"] = "job-ids"
                self._children_yang_names.add("job-ids")

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


            class JobIds(Entity):
                """
                List of jobs
                
                .. attribute:: job_id
                
                	Job Id
                	**type**\: list of    :py:class:`JobId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shprocmem_oper.ProcessesMemory.Nodes.Node.JobIds.JobId>`
                
                

                """

                _prefix = 'nto-misc-shprocmem-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ProcessesMemory.Nodes.Node.JobIds, self).__init__()

                    self.yang_name = "job-ids"
                    self.yang_parent_name = "node"

                    self.job_id = YList(self)

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
                                super(ProcessesMemory.Nodes.Node.JobIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ProcessesMemory.Nodes.Node.JobIds, self).__setattr__(name, value)


                class JobId(Entity):
                    """
                    Job Id
                    
                    .. attribute:: job_id  <key>
                    
                    	Job Id
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: data_seg_size
                    
                    	Data Segment Size
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
                    
                    .. attribute:: stack_seg_size
                    
                    	Stack Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: text_seg_size
                    
                    	Text Segment Size
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'nto-misc-shprocmem-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(ProcessesMemory.Nodes.Node.JobIds.JobId, self).__init__()

                        self.yang_name = "job-id"
                        self.yang_parent_name = "job-ids"

                        self.job_id = YLeaf(YType.int32, "job-id")

                        self.data_seg_size = YLeaf(YType.uint32, "data-seg-size")

                        self.jid = YLeaf(YType.uint32, "jid")

                        self.malloc_size = YLeaf(YType.uint32, "malloc-size")

                        self.name = YLeaf(YType.str, "name")

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
                            if name in ("job_id",
                                        "data_seg_size",
                                        "jid",
                                        "malloc_size",
                                        "name",
                                        "stack_seg_size",
                                        "text_seg_size") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(ProcessesMemory.Nodes.Node.JobIds.JobId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(ProcessesMemory.Nodes.Node.JobIds.JobId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.job_id.is_set or
                            self.data_seg_size.is_set or
                            self.jid.is_set or
                            self.malloc_size.is_set or
                            self.name.is_set or
                            self.stack_seg_size.is_set or
                            self.text_seg_size.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.job_id.yfilter != YFilter.not_set or
                            self.data_seg_size.yfilter != YFilter.not_set or
                            self.jid.yfilter != YFilter.not_set or
                            self.malloc_size.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.stack_seg_size.yfilter != YFilter.not_set or
                            self.text_seg_size.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "job-id" + "[job-id='" + self.job_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.job_id.is_set or self.job_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.job_id.get_name_leafdata())
                        if (self.data_seg_size.is_set or self.data_seg_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.data_seg_size.get_name_leafdata())
                        if (self.jid.is_set or self.jid.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.jid.get_name_leafdata())
                        if (self.malloc_size.is_set or self.malloc_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.malloc_size.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
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
                        if(name == "job-id" or name == "data-seg-size" or name == "jid" or name == "malloc-size" or name == "name" or name == "stack-seg-size" or name == "text-seg-size"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "job-id"):
                            self.job_id = value
                            self.job_id.value_namespace = name_space
                            self.job_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "data-seg-size"):
                            self.data_seg_size = value
                            self.data_seg_size.value_namespace = name_space
                            self.data_seg_size.value_namespace_prefix = name_space_prefix
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
                        if(value_path == "stack-seg-size"):
                            self.stack_seg_size = value
                            self.stack_seg_size.value_namespace = name_space
                            self.stack_seg_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "text-seg-size"):
                            self.text_seg_size = value
                            self.text_seg_size.value_namespace = name_space
                            self.text_seg_size.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.job_id:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.job_id:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "job-ids" + path_buffer

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

                    if (child_yang_name == "job-id"):
                        for c in self.job_id:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = ProcessesMemory.Nodes.Node.JobIds.JobId()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.job_id.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "job-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.job_ids is not None and self.job_ids.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.job_ids is not None and self.job_ids.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-nto-misc-shprocmem-oper:processes-memory/nodes/%s" % self.get_segment_path()
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

                if (child_yang_name == "job-ids"):
                    if (self.job_ids is None):
                        self.job_ids = ProcessesMemory.Nodes.Node.JobIds()
                        self.job_ids.parent = self
                        self._children_name_map["job_ids"] = "job-ids"
                    return self.job_ids

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "job-ids" or name == "node-name"):
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
                path_buffer = "Cisco-IOS-XR-nto-misc-shprocmem-oper:processes-memory/%s" % self.get_segment_path()
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
        path_buffer = "Cisco-IOS-XR-nto-misc-shprocmem-oper:processes-memory" + path_buffer

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

