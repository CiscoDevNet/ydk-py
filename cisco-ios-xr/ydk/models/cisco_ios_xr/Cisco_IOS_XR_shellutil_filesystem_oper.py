""" Cisco_IOS_XR_shellutil_filesystem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil\-filesystem package operational data.

This module contains definitions
for the following management objects\:
  file\-system\: List of filesystems

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FileSystem(Entity):
    """
    List of filesystems
    
    .. attribute:: node
    
    	Node ID
    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper.FileSystem.Node>`
    
    

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
        self._child_container_classes = {}
        self._child_list_classes = {"node" : ("node", FileSystem.Node)}

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-shellutil-filesystem-oper:file-system"

    def __setattr__(self, name, value):
        self._perform_setattr(FileSystem, [], name, value)


    class Node(Entity):
        """
        Node ID
        
        .. attribute:: node_name  <key>
        
        	Node name
        	**type**\:  str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: file_system
        
        	Available file systems
        	**type**\: list of    :py:class:`FileSystem <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper.FileSystem.Node.FileSystem>`
        
        

        """

        _prefix = 'shellutil-filesystem-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FileSystem.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "file-system"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"file-system" : ("file_system", FileSystem.Node.FileSystem)}

            self.node_name = YLeaf(YType.str, "node-name")

            self.file_system = YList(self)
            self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-shellutil-filesystem-oper:file-system/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FileSystem.Node, ['node_name'], name, value)


        class FileSystem(Entity):
            """
            Available file systems
            
            .. attribute:: flags
            
            	Flags of file system
            	**type**\:  str
            
            .. attribute:: free
            
            	Free space in the file system in bytes
            	**type**\:  str
            
            	**units**\: byte
            
            .. attribute:: prefixes
            
            	Prefixes of file system
            	**type**\:  str
            
            .. attribute:: size
            
            	Size of the file system in bytes
            	**type**\:  str
            
            	**units**\: byte
            
            .. attribute:: type
            
            	Type of file system
            	**type**\:  str
            
            

            """

            _prefix = 'shellutil-filesystem-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FileSystem.Node.FileSystem, self).__init__()

                self.yang_name = "file-system"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.flags = YLeaf(YType.str, "flags")

                self.free = YLeaf(YType.str, "free")

                self.prefixes = YLeaf(YType.str, "prefixes")

                self.size = YLeaf(YType.str, "size")

                self.type = YLeaf(YType.str, "type")
                self._segment_path = lambda: "file-system"

            def __setattr__(self, name, value):
                self._perform_setattr(FileSystem.Node.FileSystem, ['flags', 'free', 'prefixes', 'size', 'type'], name, value)

    def clone_ptr(self):
        self._top_entity = FileSystem()
        return self._top_entity

