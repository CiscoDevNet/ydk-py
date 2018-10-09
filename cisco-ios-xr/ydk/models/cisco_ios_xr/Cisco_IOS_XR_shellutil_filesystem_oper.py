""" Cisco_IOS_XR_shellutil_filesystem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil\-filesystem package operational data.

This module contains definitions
for the following management objects\:
  file\-system\: List of filesystems

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class FileSystem(Entity):
    """
    List of filesystems
    
    .. attribute:: node
    
    	Node ID
    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper.FileSystem.Node>`
    
    

    """

    _prefix = 'shellutil-filesystem-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(FileSystem, self).__init__()
        self._top_entity = None

        self.yang_name = "file-system"
        self.yang_parent_name = "Cisco-IOS-XR-shellutil-filesystem-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("node", ("node", FileSystem.Node))])
        self._leafs = OrderedDict()

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-shellutil-filesystem-oper:file-system"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(FileSystem, [], name, value)


    class Node(Entity):
        """
        Node ID
        
        .. attribute:: node_name  (key)
        
        	Node name
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: file_system
        
        	Available file systems
        	**type**\: list of  		 :py:class:`FileSystem_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper.FileSystem.Node.FileSystem_>`
        
        

        """

        _prefix = 'shellutil-filesystem-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FileSystem.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "file-system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['node_name']
            self._child_classes = OrderedDict([("file-system", ("file_system", FileSystem.Node.FileSystem_))])
            self._leafs = OrderedDict([
                ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
            ])
            self.node_name = None

            self.file_system = YList(self)
            self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-filesystem-oper:file-system/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(FileSystem.Node, ['node_name'], name, value)


        class FileSystem_(Entity):
            """
            Available file systems
            
            .. attribute:: size
            
            	Size of the file system in bytes
            	**type**\: str
            
            	**units**\: byte
            
            .. attribute:: free
            
            	Free space in the file system in bytes
            	**type**\: str
            
            	**units**\: byte
            
            .. attribute:: type
            
            	Type of file system
            	**type**\: str
            
            .. attribute:: flags
            
            	Flags of file system
            	**type**\: str
            
            .. attribute:: prefixes
            
            	Prefixes of file system
            	**type**\: str
            
            

            """

            _prefix = 'shellutil-filesystem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FileSystem.Node.FileSystem_, self).__init__()

                self.yang_name = "file-system"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('size', (YLeaf(YType.str, 'size'), ['str'])),
                    ('free', (YLeaf(YType.str, 'free'), ['str'])),
                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                    ('flags', (YLeaf(YType.str, 'flags'), ['str'])),
                    ('prefixes', (YLeaf(YType.str, 'prefixes'), ['str'])),
                ])
                self.size = None
                self.free = None
                self.type = None
                self.flags = None
                self.prefixes = None
                self._segment_path = lambda: "file-system"
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(FileSystem.Node.FileSystem_, ['size', 'free', 'type', 'flags', 'prefixes'], name, value)

    def clone_ptr(self):
        self._top_entity = FileSystem()
        return self._top_entity

