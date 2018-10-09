""" Cisco_IOS_XR_procmem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR procmem package operational data.

This module contains definitions
for the following management objects\:
  processes\-memory\: Process statistics

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class ProcessesMemory(Entity):
    """
    Process statistics
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes>`
    
    

    """

    _prefix = 'procmem-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(ProcessesMemory, self).__init__()
        self._top_entity = None

        self.yang_name = "processes-memory"
        self.yang_parent_name = "Cisco-IOS-XR-procmem-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", ProcessesMemory.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = ProcessesMemory.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-procmem-oper:processes-memory"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(ProcessesMemory, [], name, value)


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Node ID
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node>`
        
        

        """

        _prefix = 'procmem-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(ProcessesMemory.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "processes-memory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", ProcessesMemory.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-procmem-oper:processes-memory/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(ProcessesMemory.Nodes, [], name, value)


        class Node(Entity):
            """
            Node ID
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: process_ids
            
            	List of jobs
            	**type**\:  :py:class:`ProcessIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node.ProcessIds>`
            
            

            """

            _prefix = 'procmem-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(ProcessesMemory.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("process-ids", ("process_ids", ProcessesMemory.Nodes.Node.ProcessIds))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.process_ids = ProcessesMemory.Nodes.Node.ProcessIds()
                self.process_ids.parent = self
                self._children_name_map["process_ids"] = "process-ids"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-procmem-oper:processes-memory/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(ProcessesMemory.Nodes.Node, ['node_name'], name, value)


            class ProcessIds(Entity):
                """
                List of jobs
                
                .. attribute:: process_id
                
                	Process Id
                	**type**\: list of  		 :py:class:`ProcessId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper.ProcessesMemory.Nodes.Node.ProcessIds.ProcessId>`
                
                

                """

                _prefix = 'procmem-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(ProcessesMemory.Nodes.Node.ProcessIds, self).__init__()

                    self.yang_name = "process-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process-id", ("process_id", ProcessesMemory.Nodes.Node.ProcessIds.ProcessId))])
                    self._leafs = OrderedDict()

                    self.process_id = YList(self)
                    self._segment_path = lambda: "process-ids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(ProcessesMemory.Nodes.Node.ProcessIds, [], name, value)


                class ProcessId(Entity):
                    """
                    Process Id
                    
                    .. attribute:: process_id  (key)
                    
                    	Process Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	Process name
                    	**type**\: str
                    
                    .. attribute:: jid
                    
                    	Job ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pid
                    
                    	Process ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: text_seg_size
                    
                    	Text Segment Size in KB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_seg_size
                    
                    	Data Segment Size in KB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stack_seg_size
                    
                    	Stack Segment Size in KB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: malloc_size
                    
                    	Malloced Memory Size in KB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dyn_limit
                    
                    	Dynamic memory limit in KB (4294967295 for RLIM\_INFINITY)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: shared_mem
                    
                    	Shared memory size in KB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: physical_mem
                    
                    	Physical memory size in KB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'procmem-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(ProcessesMemory.Nodes.Node.ProcessIds.ProcessId, self).__init__()

                        self.yang_name = "process-id"
                        self.yang_parent_name = "process-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['process_id']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('jid', (YLeaf(YType.uint32, 'jid'), ['int'])),
                            ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                            ('text_seg_size', (YLeaf(YType.uint32, 'text-seg-size'), ['int'])),
                            ('data_seg_size', (YLeaf(YType.uint32, 'data-seg-size'), ['int'])),
                            ('stack_seg_size', (YLeaf(YType.uint32, 'stack-seg-size'), ['int'])),
                            ('malloc_size', (YLeaf(YType.uint32, 'malloc-size'), ['int'])),
                            ('dyn_limit', (YLeaf(YType.uint32, 'dyn-limit'), ['int'])),
                            ('shared_mem', (YLeaf(YType.uint32, 'shared-mem'), ['int'])),
                            ('physical_mem', (YLeaf(YType.uint32, 'physical-mem'), ['int'])),
                        ])
                        self.process_id = None
                        self.name = None
                        self.jid = None
                        self.pid = None
                        self.text_seg_size = None
                        self.data_seg_size = None
                        self.stack_seg_size = None
                        self.malloc_size = None
                        self.dyn_limit = None
                        self.shared_mem = None
                        self.physical_mem = None
                        self._segment_path = lambda: "process-id" + "[process-id='" + str(self.process_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(ProcessesMemory.Nodes.Node.ProcessIds.ProcessId, ['process_id', u'name', u'jid', u'pid', u'text_seg_size', u'data_seg_size', u'stack_seg_size', u'malloc_size', u'dyn_limit', u'shared_mem', u'physical_mem'], name, value)

    def clone_ptr(self):
        self._top_entity = ProcessesMemory()
        return self._top_entity

