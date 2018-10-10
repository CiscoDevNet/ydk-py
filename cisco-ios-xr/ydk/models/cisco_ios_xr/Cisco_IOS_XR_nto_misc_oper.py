""" Cisco_IOS_XR_nto_misc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR nto\-misc package operational data.

This module contains definitions
for the following management objects\:
  memory\-summary\: Memory summary information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class MemorySummary(Entity):
    """
    Memory summary information
    
    .. attribute:: nodes
    
    	List of nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes>`
    
    

    """

    _prefix = 'nto-misc-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MemorySummary, self).__init__()
        self._top_entity = None

        self.yang_name = "memory-summary"
        self.yang_parent_name = "Cisco-IOS-XR-nto-misc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", MemorySummary.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = MemorySummary.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-nto-misc-oper:memory-summary"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MemorySummary, [], name, value)


    class Nodes(Entity):
        """
        List of nodes
        
        .. attribute:: node
        
        	Name of nodes
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node>`
        
        

        """

        _prefix = 'nto-misc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MemorySummary.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "memory-summary"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", MemorySummary.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-nto-misc-oper:memory-summary/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MemorySummary.Nodes, [], name, value)


        class Node(Entity):
            """
            Name of nodes
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: summary
            
            	Memory summary information for a specific node
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node.Summary>`
            
            .. attribute:: detail
            
            	Detail Memory summary information for a specific node
            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node.Detail>`
            
            

            """

            _prefix = 'nto-misc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MemorySummary.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("summary", ("summary", MemorySummary.Nodes.Node.Summary)), ("detail", ("detail", MemorySummary.Nodes.Node.Detail))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.summary = MemorySummary.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.detail = MemorySummary.Nodes.Node.Detail()
                self.detail.parent = self
                self._children_name_map["detail"] = "detail"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-nto-misc-oper:memory-summary/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MemorySummary.Nodes.Node, ['node_name'], name, value)


            class Summary(Entity):
                """
                Memory summary information for a specific node
                
                .. attribute:: page_size
                
                	Page size in bytes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: ram_memory
                
                	Physical memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_physical_memory
                
                	Physical memory available in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: system_ram_memory
                
                	Application memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_application_memory
                
                	Application memory available in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: image_memory
                
                	Image memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: boot_ram_size
                
                	Boot RAM size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: reserved_memory
                
                	Reserved memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: io_memory
                
                	IO memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: flash_system
                
                	Flash System size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                

                """

                _prefix = 'nto-misc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MemorySummary.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('page_size', (YLeaf(YType.uint32, 'page-size'), ['int'])),
                        ('ram_memory', (YLeaf(YType.uint64, 'ram-memory'), ['int'])),
                        ('free_physical_memory', (YLeaf(YType.uint64, 'free-physical-memory'), ['int'])),
                        ('system_ram_memory', (YLeaf(YType.uint64, 'system-ram-memory'), ['int'])),
                        ('free_application_memory', (YLeaf(YType.uint64, 'free-application-memory'), ['int'])),
                        ('image_memory', (YLeaf(YType.uint64, 'image-memory'), ['int'])),
                        ('boot_ram_size', (YLeaf(YType.uint64, 'boot-ram-size'), ['int'])),
                        ('reserved_memory', (YLeaf(YType.uint64, 'reserved-memory'), ['int'])),
                        ('io_memory', (YLeaf(YType.uint64, 'io-memory'), ['int'])),
                        ('flash_system', (YLeaf(YType.uint64, 'flash-system'), ['int'])),
                    ])
                    self.page_size = None
                    self.ram_memory = None
                    self.free_physical_memory = None
                    self.system_ram_memory = None
                    self.free_application_memory = None
                    self.image_memory = None
                    self.boot_ram_size = None
                    self.reserved_memory = None
                    self.io_memory = None
                    self.flash_system = None
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MemorySummary.Nodes.Node.Summary, [u'page_size', u'ram_memory', u'free_physical_memory', u'system_ram_memory', u'free_application_memory', u'image_memory', u'boot_ram_size', u'reserved_memory', u'io_memory', u'flash_system'], name, value)


            class Detail(Entity):
                """
                Detail Memory summary information for a
                specific node
                
                .. attribute:: page_size
                
                	Page size in bytes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: ram_memory
                
                	Physical memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_physical_memory
                
                	Physical memory available in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: private_physical_memory
                
                	Private Physical memory in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: system_ram_memory
                
                	Application memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: free_application_memory
                
                	Application memory available in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: image_memory
                
                	Image memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: boot_ram_size
                
                	Boot RAM size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: reserved_memory
                
                	Reserved memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: io_memory
                
                	IO memory size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: flash_system
                
                	Flash System size in bytes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                	**units**\: byte
                
                .. attribute:: total_shared_window
                
                	Total Shared window
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: allocated_memory
                
                	Allocated Memory Size
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: program_text
                
                	Program Text Size
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: program_data
                
                	Program Data Size
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: program_stack
                
                	Program Stack Size
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_used
                
                	Total Used
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: shared_window
                
                	Available Shared windows
                	**type**\: list of  		 :py:class:`SharedWindow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_oper.MemorySummary.Nodes.Node.Detail.SharedWindow>`
                
                

                """

                _prefix = 'nto-misc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MemorySummary.Nodes.Node.Detail, self).__init__()

                    self.yang_name = "detail"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("shared-window", ("shared_window", MemorySummary.Nodes.Node.Detail.SharedWindow))])
                    self._leafs = OrderedDict([
                        ('page_size', (YLeaf(YType.uint32, 'page-size'), ['int'])),
                        ('ram_memory', (YLeaf(YType.uint64, 'ram-memory'), ['int'])),
                        ('free_physical_memory', (YLeaf(YType.uint64, 'free-physical-memory'), ['int'])),
                        ('private_physical_memory', (YLeaf(YType.uint64, 'private-physical-memory'), ['int'])),
                        ('system_ram_memory', (YLeaf(YType.uint64, 'system-ram-memory'), ['int'])),
                        ('free_application_memory', (YLeaf(YType.uint64, 'free-application-memory'), ['int'])),
                        ('image_memory', (YLeaf(YType.uint64, 'image-memory'), ['int'])),
                        ('boot_ram_size', (YLeaf(YType.uint64, 'boot-ram-size'), ['int'])),
                        ('reserved_memory', (YLeaf(YType.uint64, 'reserved-memory'), ['int'])),
                        ('io_memory', (YLeaf(YType.uint64, 'io-memory'), ['int'])),
                        ('flash_system', (YLeaf(YType.uint64, 'flash-system'), ['int'])),
                        ('total_shared_window', (YLeaf(YType.uint64, 'total-shared-window'), ['int'])),
                        ('allocated_memory', (YLeaf(YType.uint64, 'allocated-memory'), ['int'])),
                        ('program_text', (YLeaf(YType.uint64, 'program-text'), ['int'])),
                        ('program_data', (YLeaf(YType.uint64, 'program-data'), ['int'])),
                        ('program_stack', (YLeaf(YType.uint64, 'program-stack'), ['int'])),
                        ('total_used', (YLeaf(YType.uint64, 'total-used'), ['int'])),
                    ])
                    self.page_size = None
                    self.ram_memory = None
                    self.free_physical_memory = None
                    self.private_physical_memory = None
                    self.system_ram_memory = None
                    self.free_application_memory = None
                    self.image_memory = None
                    self.boot_ram_size = None
                    self.reserved_memory = None
                    self.io_memory = None
                    self.flash_system = None
                    self.total_shared_window = None
                    self.allocated_memory = None
                    self.program_text = None
                    self.program_data = None
                    self.program_stack = None
                    self.total_used = None

                    self.shared_window = YList(self)
                    self._segment_path = lambda: "detail"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MemorySummary.Nodes.Node.Detail, [u'page_size', u'ram_memory', u'free_physical_memory', u'private_physical_memory', u'system_ram_memory', u'free_application_memory', u'image_memory', u'boot_ram_size', u'reserved_memory', u'io_memory', u'flash_system', u'total_shared_window', u'allocated_memory', u'program_text', u'program_data', u'program_stack', u'total_used'], name, value)


                class SharedWindow(Entity):
                    """
                    Available Shared windows
                    
                    .. attribute:: shared_window
                    
                    	Name of shared window
                    	**type**\: str
                    
                    .. attribute:: window_size
                    
                    	Size of shared window
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'nto-misc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MemorySummary.Nodes.Node.Detail.SharedWindow, self).__init__()

                        self.yang_name = "shared-window"
                        self.yang_parent_name = "detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('shared_window', (YLeaf(YType.str, 'shared-window'), ['str'])),
                            ('window_size', (YLeaf(YType.uint64, 'window-size'), ['int'])),
                        ])
                        self.shared_window = None
                        self.window_size = None
                        self._segment_path = lambda: "shared-window"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MemorySummary.Nodes.Node.Detail.SharedWindow, [u'shared_window', u'window_size'], name, value)

    def clone_ptr(self):
        self._top_entity = MemorySummary()
        return self._top_entity

