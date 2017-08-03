""" Cisco_IOS_XE_checkpoint_archive_oper 

This module contains a collection of YANG definitions for
monitoring the checkpoint archives in a Network Element.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CheckpointArchives(Entity):
    """
    Contents of the checkpoint archive information base
    
    .. attribute:: archives
    
    	Archive information
    	**type**\:   :py:class:`Archives <ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper.CheckpointArchives.Archives>`
    
    .. attribute:: current
    
    	The current number of archives
    	**type**\:  int
    
    	**range:** 0..255
    
    .. attribute:: max
    
    	The maxium number of archives
    	**type**\:  int
    
    	**range:** 0..255
    
    .. attribute:: recent
    
    	The most recent archive
    	**type**\:  str
    
    

    """

    _prefix = 'checkpoint-archive-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(CheckpointArchives, self).__init__()
        self._top_entity = None

        self.yang_name = "checkpoint-archives"
        self.yang_parent_name = "Cisco-IOS-XE-checkpoint-archive-oper"

        self.current = YLeaf(YType.uint8, "current")

        self.max = YLeaf(YType.uint8, "max")

        self.recent = YLeaf(YType.str, "recent")

        self.archives = CheckpointArchives.Archives()
        self.archives.parent = self
        self._children_name_map["archives"] = "archives"
        self._children_yang_names.add("archives")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("current",
                        "max",
                        "recent") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(CheckpointArchives, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(CheckpointArchives, self).__setattr__(name, value)


    class Archives(Entity):
        """
        Archive information
        
        .. attribute:: archive
        
        	List of archives
        	**type**\: list of    :py:class:`Archive <ydk.models.cisco_ios_xe.Cisco_IOS_XE_checkpoint_archive_oper.CheckpointArchives.Archives.Archive>`
        
        

        """

        _prefix = 'checkpoint-archive-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(CheckpointArchives.Archives, self).__init__()

            self.yang_name = "archives"
            self.yang_parent_name = "checkpoint-archives"

            self.archive = YList(self)

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
                        super(CheckpointArchives.Archives, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CheckpointArchives.Archives, self).__setattr__(name, value)


        class Archive(Entity):
            """
            List of archives
            
            .. attribute:: number  <key>
            
            	The archive number
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: name
            
            	The name of the archive
            	**type**\:  str
            
            

            """

            _prefix = 'checkpoint-archive-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(CheckpointArchives.Archives.Archive, self).__init__()

                self.yang_name = "archive"
                self.yang_parent_name = "archives"

                self.number = YLeaf(YType.uint16, "number")

                self.name = YLeaf(YType.str, "name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("number",
                                "name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CheckpointArchives.Archives.Archive, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CheckpointArchives.Archives.Archive, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.number.is_set or
                    self.name.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.number.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "archive" + "[number='" + self.number.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archives/archives/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.number.is_set or self.number.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.number.get_name_leafdata())
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "number" or name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "number"):
                    self.number = value
                    self.number.value_namespace = name_space
                    self.number.value_namespace_prefix = name_space_prefix
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.archive:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.archive:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "archives" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archives/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "archive"):
                for c in self.archive:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CheckpointArchives.Archives.Archive()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.archive.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "archive"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.current.is_set or
            self.max.is_set or
            self.recent.is_set or
            (self.archives is not None and self.archives.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.current.yfilter != YFilter.not_set or
            self.max.yfilter != YFilter.not_set or
            self.recent.yfilter != YFilter.not_set or
            (self.archives is not None and self.archives.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-checkpoint-archive-oper:checkpoint-archives" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.current.is_set or self.current.yfilter != YFilter.not_set):
            leaf_name_data.append(self.current.get_name_leafdata())
        if (self.max.is_set or self.max.yfilter != YFilter.not_set):
            leaf_name_data.append(self.max.get_name_leafdata())
        if (self.recent.is_set or self.recent.yfilter != YFilter.not_set):
            leaf_name_data.append(self.recent.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "archives"):
            if (self.archives is None):
                self.archives = CheckpointArchives.Archives()
                self.archives.parent = self
                self._children_name_map["archives"] = "archives"
            return self.archives

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "archives" or name == "current" or name == "max" or name == "recent"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "current"):
            self.current = value
            self.current.value_namespace = name_space
            self.current.value_namespace_prefix = name_space_prefix
        if(value_path == "max"):
            self.max = value
            self.max.value_namespace = name_space
            self.max.value_namespace_prefix = name_space_prefix
        if(value_path == "recent"):
            self.recent = value
            self.recent.value_namespace = name_space
            self.recent.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = CheckpointArchives()
        return self._top_entity

