""" Cisco_IOS_XR_shellutil_filesystem_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil\-filesystem package operational data.

This module contains definitions
for the following management objects\:
  file\-system\: List of filesystems

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
                    super(FileSystem, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(FileSystem, self).__setattr__(name, value)


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

            self.node_name = YLeaf(YType.str, "node-name")

            self.file_system = YList(self)

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
                        super(FileSystem.Node, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FileSystem.Node, self).__setattr__(name, value)


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

                self.flags = YLeaf(YType.str, "flags")

                self.free = YLeaf(YType.str, "free")

                self.prefixes = YLeaf(YType.str, "prefixes")

                self.size = YLeaf(YType.str, "size")

                self.type = YLeaf(YType.str, "type")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("flags",
                                "free",
                                "prefixes",
                                "size",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(FileSystem.Node.FileSystem, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FileSystem.Node.FileSystem, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.flags.is_set or
                    self.free.is_set or
                    self.prefixes.is_set or
                    self.size.is_set or
                    self.type.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.flags.yfilter != YFilter.not_set or
                    self.free.yfilter != YFilter.not_set or
                    self.prefixes.yfilter != YFilter.not_set or
                    self.size.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "file-system" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.flags.is_set or self.flags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flags.get_name_leafdata())
                if (self.free.is_set or self.free.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.free.get_name_leafdata())
                if (self.prefixes.is_set or self.prefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.prefixes.get_name_leafdata())
                if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.size.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "flags" or name == "free" or name == "prefixes" or name == "size" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "flags"):
                    self.flags = value
                    self.flags.value_namespace = name_space
                    self.flags.value_namespace_prefix = name_space_prefix
                if(value_path == "free"):
                    self.free = value
                    self.free.value_namespace = name_space
                    self.free.value_namespace_prefix = name_space_prefix
                if(value_path == "prefixes"):
                    self.prefixes = value
                    self.prefixes.value_namespace = name_space
                    self.prefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "size"):
                    self.size = value
                    self.size.value_namespace = name_space
                    self.size.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.file_system:
                if (c.has_data()):
                    return True
            return self.node_name.is_set

        def has_operation(self):
            for c in self.file_system:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.node_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-shellutil-filesystem-oper:file-system/%s" % self.get_segment_path()
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

            if (child_yang_name == "file-system"):
                for c in self.file_system:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = FileSystem.Node.FileSystem()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.file_system.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "file-system" or name == "node-name"):
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
        path_buffer = "Cisco-IOS-XR-shellutil-filesystem-oper:file-system" + path_buffer

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

        if (child_yang_name == "node"):
            for c in self.node:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = FileSystem.Node()
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

    def clone_ptr(self):
        self._top_entity = FileSystem()
        return self._top_entity

