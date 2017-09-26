""" Cisco_IOS_XR_procmem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR procmem package operational data.

This module contains definitions
for the following management objects\:
  processes\-memory\: Process statistics

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
    _revision = '2017-05-01'

    def __init__(self):
        super(ProcessesMemory, self).__init__()
        self._top_entity = None

        self.yang_name = "processes-memory"
        self.yang_parent_name = "Cisco-IOS-XR-procmem-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", ProcessesMemory.Nodes)}
        self._child_list_classes = {}

        self.nodes = ProcessesMemory.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-procmem-oper:processes-memory"


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node>`
        
        

        """

        _prefix = 'procmem-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(ProcessesMemory.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "processes-memory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", ProcessesMemory.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-procmem-oper:processes-memory/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ProcessesMemory.Nodes, [], name, value)


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
            _revision = '2017-05-01'

            def __init__(self):
                super(ProcessesMemory.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"process-ids" : ("process_ids", ProcessesMemory.Nodes.Node.ProcessIds)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.process_ids = ProcessesMemory.Nodes.Node.ProcessIds()
                self.process_ids.parent = self
                self._children_name_map["process_ids"] = "process-ids"
                self._children_yang_names.add("process-ids")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-procmem-oper:processes-memory/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ProcessesMemory.Nodes.Node, ['node_name'], name, value)


            class ProcessIds(Entity):
                """
                List of jobs
                
                .. attribute:: process_id
                
                	Process Id
                	**type**\: list of    :py:class:`ProcessId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node.ProcessIds.ProcessId>`
                
                

                """

                _prefix = 'procmem-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(ProcessesMemory.Nodes.Node.ProcessIds, self).__init__()

                    self.yang_name = "process-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"process-id" : ("process_id", ProcessesMemory.Nodes.Node.ProcessIds.ProcessId)}

                    self.process_id = YList(self)
                    self._segment_path = lambda: "process-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(ProcessesMemory.Nodes.Node.ProcessIds, [], name, value)


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
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(ProcessesMemory.Nodes.Node.ProcessIds.ProcessId, self).__init__()

                        self.yang_name = "process-id"
                        self.yang_parent_name = "process-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "process-id" + "[process-id='" + self.process_id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(ProcessesMemory.Nodes.Node.ProcessIds.ProcessId, ['process_id', 'data_seg_size', 'dyn_limit', 'jid', 'malloc_size', 'name', 'physical_mem', 'pid', 'shared_mem', 'stack_seg_size', 'text_seg_size'], name, value)

    def clone_ptr(self):
        self._top_entity = ProcessesMemory()
        return self._top_entity

