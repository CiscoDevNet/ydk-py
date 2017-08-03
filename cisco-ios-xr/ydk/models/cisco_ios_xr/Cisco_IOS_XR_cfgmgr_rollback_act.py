""" Cisco_IOS_XR_cfgmgr_rollback_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RollBackConfigurationLast(Entity):
    """
    Rollback last <n> commits made
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationLast.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfigurationLast, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration-last"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"

        self.input = RollBackConfigurationLast.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: count
        
        	Number of commits to rollback
        	**type**\:  int
        
        	**range:** 1..100
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfigurationLast.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration-last"

            self.best_effort = YLeaf(YType.boolean, "best-effort")

            self.comment = YLeaf(YType.str, "comment")

            self.count = YLeaf(YType.int32, "count")

            self.force = YLeaf(YType.boolean, "force")

            self.label = YLeaf(YType.str, "label")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("best_effort",
                            "comment",
                            "count",
                            "force",
                            "label") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RollBackConfigurationLast.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RollBackConfigurationLast.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.best_effort.is_set or
                self.comment.is_set or
                self.count.is_set or
                self.force.is_set or
                self.label.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.best_effort.yfilter != YFilter.not_set or
                self.comment.yfilter != YFilter.not_set or
                self.count.yfilter != YFilter.not_set or
                self.force.yfilter != YFilter.not_set or
                self.label.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-last/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.best_effort.is_set or self.best_effort.yfilter != YFilter.not_set):
                leaf_name_data.append(self.best_effort.get_name_leafdata())
            if (self.comment.is_set or self.comment.yfilter != YFilter.not_set):
                leaf_name_data.append(self.comment.get_name_leafdata())
            if (self.count.is_set or self.count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.count.get_name_leafdata())
            if (self.force.is_set or self.force.yfilter != YFilter.not_set):
                leaf_name_data.append(self.force.get_name_leafdata())
            if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.label.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "best-effort" or name == "comment" or name == "count" or name == "force" or name == "label"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "best-effort"):
                self.best_effort = value
                self.best_effort.value_namespace = name_space
                self.best_effort.value_namespace_prefix = name_space_prefix
            if(value_path == "comment"):
                self.comment = value
                self.comment.value_namespace = name_space
                self.comment.value_namespace_prefix = name_space_prefix
            if(value_path == "count"):
                self.count = value
                self.count.value_namespace = name_space
                self.count.value_namespace_prefix = name_space_prefix
            if(value_path == "force"):
                self.force = value
                self.force.value_namespace = name_space
                self.force.value_namespace_prefix = name_space_prefix
            if(value_path == "label"):
                self.label = value
                self.label.value_namespace = name_space
                self.label.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-last" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RollBackConfigurationLast.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RollBackConfigurationLast()
        return self._top_entity

class RollBackConfigurationTo(Entity):
    """
    Rollback up to (and including) a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationTo.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfigurationTo, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration-to"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"

        self.input = RollBackConfigurationTo.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfigurationTo.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration-to"

            self.best_effort = YLeaf(YType.boolean, "best-effort")

            self.comment = YLeaf(YType.str, "comment")

            self.commit_id = YLeaf(YType.str, "commit-id")

            self.force = YLeaf(YType.boolean, "force")

            self.label = YLeaf(YType.str, "label")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("best_effort",
                            "comment",
                            "commit_id",
                            "force",
                            "label") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RollBackConfigurationTo.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RollBackConfigurationTo.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.best_effort.is_set or
                self.comment.is_set or
                self.commit_id.is_set or
                self.force.is_set or
                self.label.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.best_effort.yfilter != YFilter.not_set or
                self.comment.yfilter != YFilter.not_set or
                self.commit_id.yfilter != YFilter.not_set or
                self.force.yfilter != YFilter.not_set or
                self.label.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.best_effort.is_set or self.best_effort.yfilter != YFilter.not_set):
                leaf_name_data.append(self.best_effort.get_name_leafdata())
            if (self.comment.is_set or self.comment.yfilter != YFilter.not_set):
                leaf_name_data.append(self.comment.get_name_leafdata())
            if (self.commit_id.is_set or self.commit_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commit_id.get_name_leafdata())
            if (self.force.is_set or self.force.yfilter != YFilter.not_set):
                leaf_name_data.append(self.force.get_name_leafdata())
            if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.label.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "best-effort" or name == "comment" or name == "commit-id" or name == "force" or name == "label"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "best-effort"):
                self.best_effort = value
                self.best_effort.value_namespace = name_space
                self.best_effort.value_namespace_prefix = name_space_prefix
            if(value_path == "comment"):
                self.comment = value
                self.comment.value_namespace = name_space
                self.comment.value_namespace_prefix = name_space_prefix
            if(value_path == "commit-id"):
                self.commit_id = value
                self.commit_id.value_namespace = name_space
                self.commit_id.value_namespace_prefix = name_space_prefix
            if(value_path == "force"):
                self.force = value
                self.force.value_namespace = name_space
                self.force.value_namespace_prefix = name_space_prefix
            if(value_path == "label"):
                self.label = value
                self.label.value_namespace = name_space
                self.label.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RollBackConfigurationTo.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RollBackConfigurationTo()
        return self._top_entity

class RollBackConfigurationToExclude(Entity):
    """
    Rollback up to (and excluding) a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfigurationToExclude.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfigurationToExclude, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration-to-exclude"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"

        self.input = RollBackConfigurationToExclude.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfigurationToExclude.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration-to-exclude"

            self.best_effort = YLeaf(YType.boolean, "best-effort")

            self.comment = YLeaf(YType.str, "comment")

            self.commit_id = YLeaf(YType.str, "commit-id")

            self.force = YLeaf(YType.boolean, "force")

            self.label = YLeaf(YType.str, "label")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("best_effort",
                            "comment",
                            "commit_id",
                            "force",
                            "label") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RollBackConfigurationToExclude.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RollBackConfigurationToExclude.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.best_effort.is_set or
                self.comment.is_set or
                self.commit_id.is_set or
                self.force.is_set or
                self.label.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.best_effort.yfilter != YFilter.not_set or
                self.comment.yfilter != YFilter.not_set or
                self.commit_id.yfilter != YFilter.not_set or
                self.force.yfilter != YFilter.not_set or
                self.label.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to-exclude/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.best_effort.is_set or self.best_effort.yfilter != YFilter.not_set):
                leaf_name_data.append(self.best_effort.get_name_leafdata())
            if (self.comment.is_set or self.comment.yfilter != YFilter.not_set):
                leaf_name_data.append(self.comment.get_name_leafdata())
            if (self.commit_id.is_set or self.commit_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commit_id.get_name_leafdata())
            if (self.force.is_set or self.force.yfilter != YFilter.not_set):
                leaf_name_data.append(self.force.get_name_leafdata())
            if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.label.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "best-effort" or name == "comment" or name == "commit-id" or name == "force" or name == "label"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "best-effort"):
                self.best_effort = value
                self.best_effort.value_namespace = name_space
                self.best_effort.value_namespace_prefix = name_space_prefix
            if(value_path == "comment"):
                self.comment = value
                self.comment.value_namespace = name_space
                self.comment.value_namespace_prefix = name_space_prefix
            if(value_path == "commit-id"):
                self.commit_id = value
                self.commit_id.value_namespace = name_space
                self.commit_id.value_namespace_prefix = name_space_prefix
            if(value_path == "force"):
                self.force = value
                self.force.value_namespace = name_space
                self.force.value_namespace_prefix = name_space_prefix
            if(value_path == "label"):
                self.label = value
                self.label.value_namespace = name_space
                self.label.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration-to-exclude" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RollBackConfigurationToExclude.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RollBackConfigurationToExclude()
        return self._top_entity

class RollBackConfiguration(Entity):
    """
    Rollback a specific commit
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act.RollBackConfiguration.Input>`
    
    

    """

    _prefix = 'rollback-act'
    _revision = '2016-04-17'

    def __init__(self):
        super(RollBackConfiguration, self).__init__()
        self._top_entity = None

        self.yang_name = "roll-back-configuration"
        self.yang_parent_name = "Cisco-IOS-XR-cfgmgr-rollback-act"

        self.input = RollBackConfiguration.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")


    class Input(Entity):
        """
        
        
        .. attribute:: best_effort
        
        	Rollback via best\-effort operation
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: comment
        
        	Assign a comment to this rollback
        	**type**\:  str
        
        .. attribute:: commit_id
        
        	Commit ID
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: force
        
        	Override commit blocks
        	**type**\:  bool
        
        	**default value**\: false
        
        .. attribute:: label
        
        	Assign a label to this rollback
        	**type**\:  str
        
        

        """

        _prefix = 'rollback-act'
        _revision = '2016-04-17'

        def __init__(self):
            super(RollBackConfiguration.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "roll-back-configuration"

            self.best_effort = YLeaf(YType.boolean, "best-effort")

            self.comment = YLeaf(YType.str, "comment")

            self.commit_id = YLeaf(YType.str, "commit-id")

            self.force = YLeaf(YType.boolean, "force")

            self.label = YLeaf(YType.str, "label")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("best_effort",
                            "comment",
                            "commit_id",
                            "force",
                            "label") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RollBackConfiguration.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RollBackConfiguration.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.best_effort.is_set or
                self.comment.is_set or
                self.commit_id.is_set or
                self.force.is_set or
                self.label.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.best_effort.yfilter != YFilter.not_set or
                self.comment.yfilter != YFilter.not_set or
                self.commit_id.yfilter != YFilter.not_set or
                self.force.yfilter != YFilter.not_set or
                self.label.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.best_effort.is_set or self.best_effort.yfilter != YFilter.not_set):
                leaf_name_data.append(self.best_effort.get_name_leafdata())
            if (self.comment.is_set or self.comment.yfilter != YFilter.not_set):
                leaf_name_data.append(self.comment.get_name_leafdata())
            if (self.commit_id.is_set or self.commit_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.commit_id.get_name_leafdata())
            if (self.force.is_set or self.force.yfilter != YFilter.not_set):
                leaf_name_data.append(self.force.get_name_leafdata())
            if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                leaf_name_data.append(self.label.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "best-effort" or name == "comment" or name == "commit-id" or name == "force" or name == "label"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "best-effort"):
                self.best_effort = value
                self.best_effort.value_namespace = name_space
                self.best_effort.value_namespace_prefix = name_space_prefix
            if(value_path == "comment"):
                self.comment = value
                self.comment.value_namespace = name_space
                self.comment.value_namespace_prefix = name_space_prefix
            if(value_path == "commit-id"):
                self.commit_id = value
                self.commit_id.value_namespace = name_space
                self.commit_id.value_namespace_prefix = name_space_prefix
            if(value_path == "force"):
                self.force = value
                self.force.value_namespace = name_space
                self.force.value_namespace_prefix = name_space_prefix
            if(value_path == "label"):
                self.label = value
                self.label.value_namespace = name_space
                self.label.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.input is not None and self.input.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-cfgmgr-rollback-act:roll-back-configuration" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = RollBackConfiguration.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RollBackConfiguration()
        return self._top_entity

