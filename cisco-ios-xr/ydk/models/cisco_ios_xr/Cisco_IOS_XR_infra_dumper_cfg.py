""" Cisco_IOS_XR_infra_dumper_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-dumper package configuration.

This module contains definitions
for the following management objects\:
  exception\: Core dump configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Exception(Entity):
    """
    Core dump configuration commands
    
    .. attribute:: choice1
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice1>`
    
    	**presence node**\: True
    
    .. attribute:: choice2
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice2>`
    
    	**presence node**\: True
    
    .. attribute:: choice3
    
    	Preference of the dump location
    	**type**\:   :py:class:`Choice3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg.Exception.Choice3>`
    
    	**presence node**\: True
    
    .. attribute:: kernel_debugger
    
    	Enable kernel debugger
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: packet_memory
    
    	Specify 'true' to dump packet memory for all process, 'false' to disable dump of packet memory
    	**type**\:  bool
    
    .. attribute:: sparse
    
    	Specify 'true' to enable sparse core dump, 'false' to disable sparse core dump
    	**type**\:  bool
    
    .. attribute:: sparse_size
    
    	Switch to sparse core dump at this size
    	**type**\:  int
    
    	**range:** 1..4095
    
    

    """

    _prefix = 'infra-dumper-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Exception, self).__init__()
        self._top_entity = None

        self.yang_name = "exception"
        self.yang_parent_name = "Cisco-IOS-XR-infra-dumper-cfg"

        self.kernel_debugger = YLeaf(YType.empty, "kernel-debugger")

        self.packet_memory = YLeaf(YType.boolean, "packet-memory")

        self.sparse = YLeaf(YType.boolean, "sparse")

        self.sparse_size = YLeaf(YType.uint32, "sparse-size")

        self.choice1 = None
        self._children_name_map["choice1"] = "choice1"
        self._children_yang_names.add("choice1")

        self.choice2 = None
        self._children_name_map["choice2"] = "choice2"
        self._children_yang_names.add("choice2")

        self.choice3 = None
        self._children_name_map["choice3"] = "choice3"
        self._children_yang_names.add("choice3")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("kernel_debugger",
                        "packet_memory",
                        "sparse",
                        "sparse_size") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Exception, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Exception, self).__setattr__(name, value)


    class Choice1(Entity):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Exception.Choice1, self).__init__()

            self.yang_name = "choice1"
            self.yang_parent_name = "exception"
            self.is_presence_container = True

            self.compress = YLeaf(YType.boolean, "compress")

            self.file_path = YLeaf(YType.str, "file-path")

            self.filename = YLeaf(YType.str, "filename")

            self.higher_limit = YLeaf(YType.uint32, "higher-limit")

            self.lower_limit = YLeaf(YType.uint32, "lower-limit")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("compress",
                            "file_path",
                            "filename",
                            "higher_limit",
                            "lower_limit") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Exception.Choice1, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Exception.Choice1, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.compress.is_set or
                self.file_path.is_set or
                self.filename.is_set or
                self.higher_limit.is_set or
                self.lower_limit.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.compress.yfilter != YFilter.not_set or
                self.file_path.yfilter != YFilter.not_set or
                self.filename.yfilter != YFilter.not_set or
                self.higher_limit.yfilter != YFilter.not_set or
                self.lower_limit.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "choice1" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-dumper-cfg:exception/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.compress.is_set or self.compress.yfilter != YFilter.not_set):
                leaf_name_data.append(self.compress.get_name_leafdata())
            if (self.file_path.is_set or self.file_path.yfilter != YFilter.not_set):
                leaf_name_data.append(self.file_path.get_name_leafdata())
            if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filename.get_name_leafdata())
            if (self.higher_limit.is_set or self.higher_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.higher_limit.get_name_leafdata())
            if (self.lower_limit.is_set or self.lower_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lower_limit.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "compress" or name == "file-path" or name == "filename" or name == "higher-limit" or name == "lower-limit"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "compress"):
                self.compress = value
                self.compress.value_namespace = name_space
                self.compress.value_namespace_prefix = name_space_prefix
            if(value_path == "file-path"):
                self.file_path = value
                self.file_path.value_namespace = name_space
                self.file_path.value_namespace_prefix = name_space_prefix
            if(value_path == "filename"):
                self.filename = value
                self.filename.value_namespace = name_space
                self.filename.value_namespace_prefix = name_space_prefix
            if(value_path == "higher-limit"):
                self.higher_limit = value
                self.higher_limit.value_namespace = name_space
                self.higher_limit.value_namespace_prefix = name_space_prefix
            if(value_path == "lower-limit"):
                self.lower_limit = value
                self.lower_limit.value_namespace = name_space
                self.lower_limit.value_namespace_prefix = name_space_prefix


    class Choice3(Entity):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Exception.Choice3, self).__init__()

            self.yang_name = "choice3"
            self.yang_parent_name = "exception"
            self.is_presence_container = True

            self.compress = YLeaf(YType.boolean, "compress")

            self.file_path = YLeaf(YType.str, "file-path")

            self.filename = YLeaf(YType.str, "filename")

            self.higher_limit = YLeaf(YType.uint32, "higher-limit")

            self.lower_limit = YLeaf(YType.uint32, "lower-limit")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("compress",
                            "file_path",
                            "filename",
                            "higher_limit",
                            "lower_limit") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Exception.Choice3, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Exception.Choice3, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.compress.is_set or
                self.file_path.is_set or
                self.filename.is_set or
                self.higher_limit.is_set or
                self.lower_limit.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.compress.yfilter != YFilter.not_set or
                self.file_path.yfilter != YFilter.not_set or
                self.filename.yfilter != YFilter.not_set or
                self.higher_limit.yfilter != YFilter.not_set or
                self.lower_limit.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "choice3" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-dumper-cfg:exception/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.compress.is_set or self.compress.yfilter != YFilter.not_set):
                leaf_name_data.append(self.compress.get_name_leafdata())
            if (self.file_path.is_set or self.file_path.yfilter != YFilter.not_set):
                leaf_name_data.append(self.file_path.get_name_leafdata())
            if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filename.get_name_leafdata())
            if (self.higher_limit.is_set or self.higher_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.higher_limit.get_name_leafdata())
            if (self.lower_limit.is_set or self.lower_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lower_limit.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "compress" or name == "file-path" or name == "filename" or name == "higher-limit" or name == "lower-limit"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "compress"):
                self.compress = value
                self.compress.value_namespace = name_space
                self.compress.value_namespace_prefix = name_space_prefix
            if(value_path == "file-path"):
                self.file_path = value
                self.file_path.value_namespace = name_space
                self.file_path.value_namespace_prefix = name_space_prefix
            if(value_path == "filename"):
                self.filename = value
                self.filename.value_namespace = name_space
                self.filename.value_namespace_prefix = name_space_prefix
            if(value_path == "higher-limit"):
                self.higher_limit = value
                self.higher_limit.value_namespace = name_space
                self.higher_limit.value_namespace_prefix = name_space_prefix
            if(value_path == "lower-limit"):
                self.lower_limit = value
                self.lower_limit.value_namespace = name_space
                self.lower_limit.value_namespace_prefix = name_space_prefix


    class Choice2(Entity):
        """
        Preference of the dump location
        
        .. attribute:: compress
        
        	Specify 'true' to compress core files dumped on this path, 'false' to not compress
        	**type**\:  bool
        
        .. attribute:: file_path
        
        	Protocol and directory
        	**type**\:  str
        
        .. attribute:: filename
        
        	Dump filename
        	**type**\:  str
        
        .. attribute:: higher_limit
        
        	Higher limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 5..64
        
        .. attribute:: lower_limit
        
        	Lower limit.  This is required if Filename is specified
        	**type**\:  int
        
        	**range:** 0..4
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-dumper-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Exception.Choice2, self).__init__()

            self.yang_name = "choice2"
            self.yang_parent_name = "exception"
            self.is_presence_container = True

            self.compress = YLeaf(YType.boolean, "compress")

            self.file_path = YLeaf(YType.str, "file-path")

            self.filename = YLeaf(YType.str, "filename")

            self.higher_limit = YLeaf(YType.uint32, "higher-limit")

            self.lower_limit = YLeaf(YType.uint32, "lower-limit")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("compress",
                            "file_path",
                            "filename",
                            "higher_limit",
                            "lower_limit") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Exception.Choice2, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Exception.Choice2, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.compress.is_set or
                self.file_path.is_set or
                self.filename.is_set or
                self.higher_limit.is_set or
                self.lower_limit.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.compress.yfilter != YFilter.not_set or
                self.file_path.yfilter != YFilter.not_set or
                self.filename.yfilter != YFilter.not_set or
                self.higher_limit.yfilter != YFilter.not_set or
                self.lower_limit.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "choice2" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-dumper-cfg:exception/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.compress.is_set or self.compress.yfilter != YFilter.not_set):
                leaf_name_data.append(self.compress.get_name_leafdata())
            if (self.file_path.is_set or self.file_path.yfilter != YFilter.not_set):
                leaf_name_data.append(self.file_path.get_name_leafdata())
            if (self.filename.is_set or self.filename.yfilter != YFilter.not_set):
                leaf_name_data.append(self.filename.get_name_leafdata())
            if (self.higher_limit.is_set or self.higher_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.higher_limit.get_name_leafdata())
            if (self.lower_limit.is_set or self.lower_limit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lower_limit.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "compress" or name == "file-path" or name == "filename" or name == "higher-limit" or name == "lower-limit"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "compress"):
                self.compress = value
                self.compress.value_namespace = name_space
                self.compress.value_namespace_prefix = name_space_prefix
            if(value_path == "file-path"):
                self.file_path = value
                self.file_path.value_namespace = name_space
                self.file_path.value_namespace_prefix = name_space_prefix
            if(value_path == "filename"):
                self.filename = value
                self.filename.value_namespace = name_space
                self.filename.value_namespace_prefix = name_space_prefix
            if(value_path == "higher-limit"):
                self.higher_limit = value
                self.higher_limit.value_namespace = name_space
                self.higher_limit.value_namespace_prefix = name_space_prefix
            if(value_path == "lower-limit"):
                self.lower_limit = value
                self.lower_limit.value_namespace = name_space
                self.lower_limit.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.kernel_debugger.is_set or
            self.packet_memory.is_set or
            self.sparse.is_set or
            self.sparse_size.is_set or
            (self.choice1 is not None) or
            (self.choice2 is not None) or
            (self.choice3 is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.kernel_debugger.yfilter != YFilter.not_set or
            self.packet_memory.yfilter != YFilter.not_set or
            self.sparse.yfilter != YFilter.not_set or
            self.sparse_size.yfilter != YFilter.not_set or
            (self.choice1 is not None and self.choice1.has_operation()) or
            (self.choice2 is not None and self.choice2.has_operation()) or
            (self.choice3 is not None and self.choice3.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-dumper-cfg:exception" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.kernel_debugger.is_set or self.kernel_debugger.yfilter != YFilter.not_set):
            leaf_name_data.append(self.kernel_debugger.get_name_leafdata())
        if (self.packet_memory.is_set or self.packet_memory.yfilter != YFilter.not_set):
            leaf_name_data.append(self.packet_memory.get_name_leafdata())
        if (self.sparse.is_set or self.sparse.yfilter != YFilter.not_set):
            leaf_name_data.append(self.sparse.get_name_leafdata())
        if (self.sparse_size.is_set or self.sparse_size.yfilter != YFilter.not_set):
            leaf_name_data.append(self.sparse_size.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "choice1"):
            if (self.choice1 is None):
                self.choice1 = Exception.Choice1()
                self.choice1.parent = self
                self._children_name_map["choice1"] = "choice1"
            return self.choice1

        if (child_yang_name == "choice2"):
            if (self.choice2 is None):
                self.choice2 = Exception.Choice2()
                self.choice2.parent = self
                self._children_name_map["choice2"] = "choice2"
            return self.choice2

        if (child_yang_name == "choice3"):
            if (self.choice3 is None):
                self.choice3 = Exception.Choice3()
                self.choice3.parent = self
                self._children_name_map["choice3"] = "choice3"
            return self.choice3

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "choice1" or name == "choice2" or name == "choice3" or name == "kernel-debugger" or name == "packet-memory" or name == "sparse" or name == "sparse-size"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "kernel-debugger"):
            self.kernel_debugger = value
            self.kernel_debugger.value_namespace = name_space
            self.kernel_debugger.value_namespace_prefix = name_space_prefix
        if(value_path == "packet-memory"):
            self.packet_memory = value
            self.packet_memory.value_namespace = name_space
            self.packet_memory.value_namespace_prefix = name_space_prefix
        if(value_path == "sparse"):
            self.sparse = value
            self.sparse.value_namespace = name_space
            self.sparse.value_namespace_prefix = name_space_prefix
        if(value_path == "sparse-size"):
            self.sparse_size = value
            self.sparse_size.value_namespace = name_space
            self.sparse_size.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Exception()
        return self._top_entity

