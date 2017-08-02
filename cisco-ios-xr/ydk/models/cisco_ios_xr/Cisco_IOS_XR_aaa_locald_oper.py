""" Cisco_IOS_XR_aaa_locald_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package operational data.

This module contains definitions
for the following management objects\:
  aaa\: AAA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Aaa(Entity):
    """
    AAA operational data
    
    .. attribute:: all_tasks
    
    	All tasks supported by system
    	**type**\:   :py:class:`AllTasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AllTasks>`
    
    .. attribute:: authen_method
    
    	Current users authentication method
    	**type**\:   :py:class:`AuthenMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AuthenMethod>`
    
    .. attribute:: current_usergroup
    
    	Specific Usergroup Information
    	**type**\:   :py:class:`CurrentUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentUsergroup>`
    
    .. attribute:: currentuser_detail
    
    	Current user specific details
    	**type**\:   :py:class:`CurrentuserDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentuserDetail>`
    
    .. attribute:: diameter
    
    	Diameter operational data
    	**type**\:   :py:class:`Diameter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter>`
    
    .. attribute:: radius
    
    	RADIUS operational data
    	**type**\:   :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius>`
    
    .. attribute:: tacacs
    
    	TACACS operational data
    	**type**\:   :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs>`
    
    .. attribute:: task_map
    
    	Task map of current user
    	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.TaskMap>`
    
    .. attribute:: taskgroups
    
    	Individual taskgroups container
    	**type**\:   :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Container for individual usergroup Information
    	**type**\:   :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups>`
    
    .. attribute:: users
    
    	Container for individual local user information
    	**type**\:   :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users>`
    
    

    """

    _prefix = 'aaa-locald-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-locald-oper"

        self.all_tasks = Aaa.AllTasks()
        self.all_tasks.parent = self
        self._children_name_map["all_tasks"] = "all-tasks"
        self._children_yang_names.add("all-tasks")

        self.authen_method = Aaa.AuthenMethod()
        self.authen_method.parent = self
        self._children_name_map["authen_method"] = "authen-method"
        self._children_yang_names.add("authen-method")

        self.current_usergroup = Aaa.CurrentUsergroup()
        self.current_usergroup.parent = self
        self._children_name_map["current_usergroup"] = "current-usergroup"
        self._children_yang_names.add("current-usergroup")

        self.currentuser_detail = Aaa.CurrentuserDetail()
        self.currentuser_detail.parent = self
        self._children_name_map["currentuser_detail"] = "currentuser-detail"
        self._children_yang_names.add("currentuser-detail")

        self.diameter = Aaa.Diameter()
        self.diameter.parent = self
        self._children_name_map["diameter"] = "diameter"
        self._children_yang_names.add("diameter")

        self.radius = Aaa.Radius()
        self.radius.parent = self
        self._children_name_map["radius"] = "radius"
        self._children_yang_names.add("radius")

        self.tacacs = Aaa.Tacacs()
        self.tacacs.parent = self
        self._children_name_map["tacacs"] = "tacacs"
        self._children_yang_names.add("tacacs")

        self.task_map = Aaa.TaskMap()
        self.task_map.parent = self
        self._children_name_map["task_map"] = "task-map"
        self._children_yang_names.add("task-map")

        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self._children_name_map["taskgroups"] = "taskgroups"
        self._children_yang_names.add("taskgroups")

        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self._children_name_map["usergroups"] = "usergroups"
        self._children_yang_names.add("usergroups")

        self.users = Aaa.Users()
        self.users.parent = self
        self._children_name_map["users"] = "users"
        self._children_yang_names.add("users")


    class AllTasks(Entity):
        """
        All tasks supported by system
        
        .. attribute:: task_id
        
        	Names of available task\-ids
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AllTasks, self).__init__()

            self.yang_name = "all-tasks"
            self.yang_parent_name = "aaa"

            self.task_id = YLeafList(YType.str, "task-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("task_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.AllTasks, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.AllTasks, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.task_id.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return False

        def has_operation(self):
            for leaf in self.task_id.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.task_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "all-tasks" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            leaf_name_data.extend(self.task_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "task-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "task-id"):
                self.task_id.append(value)


    class CurrentuserDetail(Entity):
        """
        Current user specific details
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.CurrentuserDetail, self).__init__()

            self.yang_name = "currentuser-detail"
            self.yang_parent_name = "aaa"

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("authenmethod",
                            "name",
                            "taskmap",
                            "usergroup") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.CurrentuserDetail, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.CurrentuserDetail, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.authenmethod.is_set or
                self.name.is_set)

        def has_operation(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.is_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.authenmethod.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.taskmap.yfilter != YFilter.not_set or
                self.usergroup.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "currentuser-detail" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.authenmethod.is_set or self.authenmethod.yfilter != YFilter.not_set):
                leaf_name_data.append(self.authenmethod.get_name_leafdata())
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())

            leaf_name_data.extend(self.taskmap.get_name_leafdata())

            leaf_name_data.extend(self.usergroup.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authenmethod" or name == "name" or name == "taskmap" or name == "usergroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "authenmethod"):
                self.authenmethod = value
                self.authenmethod.value_namespace = name_space
                self.authenmethod.value_namespace_prefix = name_space_prefix
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "taskmap"):
                self.taskmap.append(value)
            if(value_path == "usergroup"):
                self.usergroup.append(value)


    class TaskMap(Entity):
        """
        Task map of current user
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.TaskMap, self).__init__()

            self.yang_name = "task-map"
            self.yang_parent_name = "aaa"

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("authenmethod",
                            "name",
                            "taskmap",
                            "usergroup") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.TaskMap, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.TaskMap, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.authenmethod.is_set or
                self.name.is_set)

        def has_operation(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.is_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.authenmethod.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.taskmap.yfilter != YFilter.not_set or
                self.usergroup.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "task-map" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.authenmethod.is_set or self.authenmethod.yfilter != YFilter.not_set):
                leaf_name_data.append(self.authenmethod.get_name_leafdata())
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())

            leaf_name_data.extend(self.taskmap.get_name_leafdata())

            leaf_name_data.extend(self.usergroup.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authenmethod" or name == "name" or name == "taskmap" or name == "usergroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "authenmethod"):
                self.authenmethod = value
                self.authenmethod.value_namespace = name_space
                self.authenmethod.value_namespace_prefix = name_space_prefix
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "taskmap"):
                self.taskmap.append(value)
            if(value_path == "usergroup"):
                self.usergroup.append(value)


    class Taskgroups(Entity):
        """
        Individual taskgroups container
        
        .. attribute:: taskgroup
        
        	Specific Taskgroup Information
        	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Taskgroups, self).__init__()

            self.yang_name = "taskgroups"
            self.yang_parent_name = "aaa"

            self.taskgroup = YList(self)

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
                        super(Aaa.Taskgroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Taskgroups, self).__setattr__(name, value)


        class Taskgroup(Entity):
            """
            Specific Taskgroup Information
            
            .. attribute:: name  <key>
            
            	Taskgroup name
            	**type**\:  str
            
            .. attribute:: included_task_ids
            
            	Task\-ids included
            	**type**\:   :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds>`
            
            .. attribute:: name_xr
            
            	Name of the taskgroup
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Taskgroups.Taskgroup, self).__init__()

                self.yang_name = "taskgroup"
                self.yang_parent_name = "taskgroups"

                self.name = YLeaf(YType.str, "name")

                self.name_xr = YLeaf(YType.str, "name-xr")

                self.included_task_ids = Aaa.Taskgroups.Taskgroup.IncludedTaskIds()
                self.included_task_ids.parent = self
                self._children_name_map["included_task_ids"] = "included-task-ids"
                self._children_yang_names.add("included-task-ids")

                self.task_map = Aaa.Taskgroups.Taskgroup.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._children_yang_names.add("task-map")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Taskgroups.Taskgroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Taskgroups.Taskgroup, self).__setattr__(name, value)


            class IncludedTaskIds(Entity):
                """
                Task\-ids included
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds, self).__init__()

                    self.yang_name = "included-task-ids"
                    self.yang_parent_name = "taskgroup"

                    self.tasks = YList(self)

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
                                super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds, self).__setattr__(name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "included-task-ids"

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debug",
                                        "execute",
                                        "read",
                                        "task_id",
                                        "write") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debug.is_set or
                            self.execute.is_set or
                            self.read.is_set or
                            self.task_id.is_set or
                            self.write.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debug.yfilter != YFilter.not_set or
                            self.execute.yfilter != YFilter.not_set or
                            self.read.yfilter != YFilter.not_set or
                            self.task_id.yfilter != YFilter.not_set or
                            self.write.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tasks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debug.is_set or self.debug.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debug.get_name_leafdata())
                        if (self.execute.is_set or self.execute.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.execute.get_name_leafdata())
                        if (self.read.is_set or self.read.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.read.get_name_leafdata())
                        if (self.task_id.is_set or self.task_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.task_id.get_name_leafdata())
                        if (self.write.is_set or self.write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.write.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debug" or name == "execute" or name == "read" or name == "task-id" or name == "write"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debug"):
                            self.debug = value
                            self.debug.value_namespace = name_space
                            self.debug.value_namespace_prefix = name_space_prefix
                        if(value_path == "execute"):
                            self.execute = value
                            self.execute.value_namespace = name_space
                            self.execute.value_namespace_prefix = name_space_prefix
                        if(value_path == "read"):
                            self.read = value
                            self.read.value_namespace = name_space
                            self.read.value_namespace_prefix = name_space_prefix
                        if(value_path == "task-id"):
                            self.task_id = value
                            self.task_id.value_namespace = name_space
                            self.task_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "write"):
                            self.write = value
                            self.write.value_namespace = name_space
                            self.write.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.tasks:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.tasks:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "included-task-ids" + path_buffer

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

                    if (child_yang_name == "tasks"):
                        for c in self.tasks:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.tasks.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tasks"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class TaskMap(Entity):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "taskgroup"

                    self.tasks = YList(self)

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
                                super(Aaa.Taskgroups.Taskgroup.TaskMap, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Taskgroups.Taskgroup.TaskMap, self).__setattr__(name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debug",
                                        "execute",
                                        "read",
                                        "task_id",
                                        "write") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Taskgroups.Taskgroup.TaskMap.Tasks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Taskgroups.Taskgroup.TaskMap.Tasks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debug.is_set or
                            self.execute.is_set or
                            self.read.is_set or
                            self.task_id.is_set or
                            self.write.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debug.yfilter != YFilter.not_set or
                            self.execute.yfilter != YFilter.not_set or
                            self.read.yfilter != YFilter.not_set or
                            self.task_id.yfilter != YFilter.not_set or
                            self.write.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tasks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debug.is_set or self.debug.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debug.get_name_leafdata())
                        if (self.execute.is_set or self.execute.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.execute.get_name_leafdata())
                        if (self.read.is_set or self.read.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.read.get_name_leafdata())
                        if (self.task_id.is_set or self.task_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.task_id.get_name_leafdata())
                        if (self.write.is_set or self.write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.write.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debug" or name == "execute" or name == "read" or name == "task-id" or name == "write"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debug"):
                            self.debug = value
                            self.debug.value_namespace = name_space
                            self.debug.value_namespace_prefix = name_space_prefix
                        if(value_path == "execute"):
                            self.execute = value
                            self.execute.value_namespace = name_space
                            self.execute.value_namespace_prefix = name_space_prefix
                        if(value_path == "read"):
                            self.read = value
                            self.read.value_namespace = name_space
                            self.read.value_namespace_prefix = name_space_prefix
                        if(value_path == "task-id"):
                            self.task_id = value
                            self.task_id.value_namespace = name_space
                            self.task_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "write"):
                            self.write = value
                            self.write.value_namespace = name_space
                            self.write.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.tasks:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.tasks:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "task-map" + path_buffer

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

                    if (child_yang_name == "tasks"):
                        for c in self.tasks:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Taskgroups.Taskgroup.TaskMap.Tasks()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.tasks.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tasks"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.name.is_set or
                    self.name_xr.is_set or
                    (self.included_task_ids is not None and self.included_task_ids.has_data()) or
                    (self.task_map is not None and self.task_map.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.name_xr.yfilter != YFilter.not_set or
                    (self.included_task_ids is not None and self.included_task_ids.has_operation()) or
                    (self.task_map is not None and self.task_map.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "taskgroup" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/taskgroups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.name_xr.is_set or self.name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "included-task-ids"):
                    if (self.included_task_ids is None):
                        self.included_task_ids = Aaa.Taskgroups.Taskgroup.IncludedTaskIds()
                        self.included_task_ids.parent = self
                        self._children_name_map["included_task_ids"] = "included-task-ids"
                    return self.included_task_ids

                if (child_yang_name == "task-map"):
                    if (self.task_map is None):
                        self.task_map = Aaa.Taskgroups.Taskgroup.TaskMap()
                        self.task_map.parent = self
                        self._children_name_map["task_map"] = "task-map"
                    return self.task_map

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "included-task-ids" or name == "task-map" or name == "name" or name == "name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "name-xr"):
                    self.name_xr = value
                    self.name_xr.value_namespace = name_space
                    self.name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.taskgroup:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.taskgroup:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "taskgroups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "taskgroup"):
                for c in self.taskgroup:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Taskgroups.Taskgroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.taskgroup.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "taskgroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Users(Entity):
        """
        Container for individual local user information
        
        .. attribute:: user
        
        	Specific local user information
        	**type**\: list of    :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Users, self).__init__()

            self.yang_name = "users"
            self.yang_parent_name = "aaa"

            self.user = YList(self)

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
                        super(Aaa.Users, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Users, self).__setattr__(name, value)


        class User(Entity):
            """
            Specific local user information
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\:  str
            
            .. attribute:: admin_user
            
            	Is admin plane user ?
            	**type**\:  bool
            
            .. attribute:: first_user
            
            	Is first user ?
            	**type**\:  bool
            
            .. attribute:: name_xr
            
            	Username
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed taskmap
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap>`
            
            .. attribute:: usergroup
            
            	Member usergroups
            	**type**\:  list of str
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Users.User, self).__init__()

                self.yang_name = "user"
                self.yang_parent_name = "users"

                self.name = YLeaf(YType.str, "name")

                self.admin_user = YLeaf(YType.boolean, "admin-user")

                self.first_user = YLeaf(YType.boolean, "first-user")

                self.name_xr = YLeaf(YType.str, "name-xr")

                self.usergroup = YLeafList(YType.str, "usergroup")

                self.task_map = Aaa.Users.User.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._children_yang_names.add("task-map")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "admin_user",
                                "first_user",
                                "name_xr",
                                "usergroup") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Users.User, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Users.User, self).__setattr__(name, value)


            class TaskMap(Entity):
                """
                Computed taskmap
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Users.User.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "user"

                    self.tasks = YList(self)

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
                                super(Aaa.Users.User.TaskMap, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Users.User.TaskMap, self).__setattr__(name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Users.User.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debug",
                                        "execute",
                                        "read",
                                        "task_id",
                                        "write") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Users.User.TaskMap.Tasks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Users.User.TaskMap.Tasks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debug.is_set or
                            self.execute.is_set or
                            self.read.is_set or
                            self.task_id.is_set or
                            self.write.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debug.yfilter != YFilter.not_set or
                            self.execute.yfilter != YFilter.not_set or
                            self.read.yfilter != YFilter.not_set or
                            self.task_id.yfilter != YFilter.not_set or
                            self.write.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tasks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debug.is_set or self.debug.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debug.get_name_leafdata())
                        if (self.execute.is_set or self.execute.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.execute.get_name_leafdata())
                        if (self.read.is_set or self.read.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.read.get_name_leafdata())
                        if (self.task_id.is_set or self.task_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.task_id.get_name_leafdata())
                        if (self.write.is_set or self.write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.write.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debug" or name == "execute" or name == "read" or name == "task-id" or name == "write"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debug"):
                            self.debug = value
                            self.debug.value_namespace = name_space
                            self.debug.value_namespace_prefix = name_space_prefix
                        if(value_path == "execute"):
                            self.execute = value
                            self.execute.value_namespace = name_space
                            self.execute.value_namespace_prefix = name_space_prefix
                        if(value_path == "read"):
                            self.read = value
                            self.read.value_namespace = name_space
                            self.read.value_namespace_prefix = name_space_prefix
                        if(value_path == "task-id"):
                            self.task_id = value
                            self.task_id.value_namespace = name_space
                            self.task_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "write"):
                            self.write = value
                            self.write.value_namespace = name_space
                            self.write.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.tasks:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.tasks:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "task-map" + path_buffer

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

                    if (child_yang_name == "tasks"):
                        for c in self.tasks:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Users.User.TaskMap.Tasks()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.tasks.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tasks"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                for leaf in self.usergroup.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.name.is_set or
                    self.admin_user.is_set or
                    self.first_user.is_set or
                    self.name_xr.is_set or
                    (self.task_map is not None and self.task_map.has_data()))

            def has_operation(self):
                for leaf in self.usergroup.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.admin_user.yfilter != YFilter.not_set or
                    self.first_user.yfilter != YFilter.not_set or
                    self.name_xr.yfilter != YFilter.not_set or
                    self.usergroup.yfilter != YFilter.not_set or
                    (self.task_map is not None and self.task_map.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "user" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/users/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.admin_user.is_set or self.admin_user.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.admin_user.get_name_leafdata())
                if (self.first_user.is_set or self.first_user.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.first_user.get_name_leafdata())
                if (self.name_xr.is_set or self.name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name_xr.get_name_leafdata())

                leaf_name_data.extend(self.usergroup.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "task-map"):
                    if (self.task_map is None):
                        self.task_map = Aaa.Users.User.TaskMap()
                        self.task_map.parent = self
                        self._children_name_map["task_map"] = "task-map"
                    return self.task_map

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "task-map" or name == "name" or name == "admin-user" or name == "first-user" or name == "name-xr" or name == "usergroup"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "admin-user"):
                    self.admin_user = value
                    self.admin_user.value_namespace = name_space
                    self.admin_user.value_namespace_prefix = name_space_prefix
                if(value_path == "first-user"):
                    self.first_user = value
                    self.first_user.value_namespace = name_space
                    self.first_user.value_namespace_prefix = name_space_prefix
                if(value_path == "name-xr"):
                    self.name_xr = value
                    self.name_xr.value_namespace = name_space
                    self.name_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "usergroup"):
                    self.usergroup.append(value)

        def has_data(self):
            for c in self.user:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.user:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "users" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "user"):
                for c in self.user:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Users.User()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.user.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "user"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Usergroups(Entity):
        """
        Container for individual usergroup Information
        
        .. attribute:: usergroup
        
        	Specific Usergroup Information
        	**type**\: list of    :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Usergroups, self).__init__()

            self.yang_name = "usergroups"
            self.yang_parent_name = "aaa"

            self.usergroup = YList(self)

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
                        super(Aaa.Usergroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.Usergroups, self).__setattr__(name, value)


        class Usergroup(Entity):
            """
            Specific Usergroup Information
            
            .. attribute:: name  <key>
            
            	Usergroup name
            	**type**\:  str
            
            .. attribute:: name_xr
            
            	Name of the usergroup
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap>`
            
            .. attribute:: taskgroup
            
            	Component taskgroups
            	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Usergroups.Usergroup, self).__init__()

                self.yang_name = "usergroup"
                self.yang_parent_name = "usergroups"

                self.name = YLeaf(YType.str, "name")

                self.name_xr = YLeaf(YType.str, "name-xr")

                self.task_map = Aaa.Usergroups.Usergroup.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._children_yang_names.add("task-map")

                self.taskgroup = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "name_xr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Usergroups.Usergroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Usergroups.Usergroup, self).__setattr__(name, value)


            class TaskMap(Entity):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "usergroup"

                    self.tasks = YList(self)

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
                                super(Aaa.Usergroups.Usergroup.TaskMap, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Usergroups.Usergroup.TaskMap, self).__setattr__(name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"

                        self.debug = YLeaf(YType.boolean, "debug")

                        self.execute = YLeaf(YType.boolean, "execute")

                        self.read = YLeaf(YType.boolean, "read")

                        self.task_id = YLeaf(YType.str, "task-id")

                        self.write = YLeaf(YType.boolean, "write")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("debug",
                                        "execute",
                                        "read",
                                        "task_id",
                                        "write") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Usergroups.Usergroup.TaskMap.Tasks, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Usergroups.Usergroup.TaskMap.Tasks, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.debug.is_set or
                            self.execute.is_set or
                            self.read.is_set or
                            self.task_id.is_set or
                            self.write.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.debug.yfilter != YFilter.not_set or
                            self.execute.yfilter != YFilter.not_set or
                            self.read.yfilter != YFilter.not_set or
                            self.task_id.yfilter != YFilter.not_set or
                            self.write.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tasks" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.debug.is_set or self.debug.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.debug.get_name_leafdata())
                        if (self.execute.is_set or self.execute.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.execute.get_name_leafdata())
                        if (self.read.is_set or self.read.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.read.get_name_leafdata())
                        if (self.task_id.is_set or self.task_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.task_id.get_name_leafdata())
                        if (self.write.is_set or self.write.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.write.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "debug" or name == "execute" or name == "read" or name == "task-id" or name == "write"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "debug"):
                            self.debug = value
                            self.debug.value_namespace = name_space
                            self.debug.value_namespace_prefix = name_space_prefix
                        if(value_path == "execute"):
                            self.execute = value
                            self.execute.value_namespace = name_space
                            self.execute.value_namespace_prefix = name_space_prefix
                        if(value_path == "read"):
                            self.read = value
                            self.read.value_namespace = name_space
                            self.read.value_namespace_prefix = name_space_prefix
                        if(value_path == "task-id"):
                            self.task_id = value
                            self.task_id.value_namespace = name_space
                            self.task_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "write"):
                            self.write = value
                            self.write.value_namespace = name_space
                            self.write.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.tasks:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.tasks:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "task-map" + path_buffer

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

                    if (child_yang_name == "tasks"):
                        for c in self.tasks:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Usergroups.Usergroup.TaskMap.Tasks()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.tasks.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tasks"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Taskgroup(Entity):
                """
                Component taskgroups
                
                .. attribute:: included_task_ids
                
                	Task\-ids included
                	**type**\:   :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds>`
                
                .. attribute:: name_xr
                
                	Name of the taskgroup
                	**type**\:  str
                
                .. attribute:: task_map
                
                	Computed task map
                	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.Taskgroup, self).__init__()

                    self.yang_name = "taskgroup"
                    self.yang_parent_name = "usergroup"

                    self.name_xr = YLeaf(YType.str, "name-xr")

                    self.included_task_ids = Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds()
                    self.included_task_ids.parent = self
                    self._children_name_map["included_task_ids"] = "included-task-ids"
                    self._children_yang_names.add("included-task-ids")

                    self.task_map = Aaa.Usergroups.Usergroup.Taskgroup.TaskMap()
                    self.task_map.parent = self
                    self._children_name_map["task_map"] = "task-map"
                    self._children_yang_names.add("task-map")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name_xr") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Usergroups.Usergroup.Taskgroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Usergroups.Usergroup.Taskgroup, self).__setattr__(name, value)


                class IncludedTaskIds(Entity):
                    """
                    Task\-ids included
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds, self).__init__()

                        self.yang_name = "included-task-ids"
                        self.yang_parent_name = "taskgroup"

                        self.tasks = YList(self)

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
                                    super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds, self).__setattr__(name, value)


                    class Tasks(Entity):
                        """
                        List of permitted tasks
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\:  bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\:  bool
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\:  bool
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\:  str
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks, self).__init__()

                            self.yang_name = "tasks"
                            self.yang_parent_name = "included-task-ids"

                            self.debug = YLeaf(YType.boolean, "debug")

                            self.execute = YLeaf(YType.boolean, "execute")

                            self.read = YLeaf(YType.boolean, "read")

                            self.task_id = YLeaf(YType.str, "task-id")

                            self.write = YLeaf(YType.boolean, "write")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("debug",
                                            "execute",
                                            "read",
                                            "task_id",
                                            "write") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.debug.is_set or
                                self.execute.is_set or
                                self.read.is_set or
                                self.task_id.is_set or
                                self.write.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.debug.yfilter != YFilter.not_set or
                                self.execute.yfilter != YFilter.not_set or
                                self.read.yfilter != YFilter.not_set or
                                self.task_id.yfilter != YFilter.not_set or
                                self.write.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tasks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.debug.is_set or self.debug.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.debug.get_name_leafdata())
                            if (self.execute.is_set or self.execute.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.execute.get_name_leafdata())
                            if (self.read.is_set or self.read.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.read.get_name_leafdata())
                            if (self.task_id.is_set or self.task_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.task_id.get_name_leafdata())
                            if (self.write.is_set or self.write.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.write.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "debug" or name == "execute" or name == "read" or name == "task-id" or name == "write"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "debug"):
                                self.debug = value
                                self.debug.value_namespace = name_space
                                self.debug.value_namespace_prefix = name_space_prefix
                            if(value_path == "execute"):
                                self.execute = value
                                self.execute.value_namespace = name_space
                                self.execute.value_namespace_prefix = name_space_prefix
                            if(value_path == "read"):
                                self.read = value
                                self.read.value_namespace = name_space
                                self.read.value_namespace_prefix = name_space_prefix
                            if(value_path == "task-id"):
                                self.task_id = value
                                self.task_id.value_namespace = name_space
                                self.task_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "write"):
                                self.write = value
                                self.write.value_namespace = name_space
                                self.write.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.tasks:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.tasks:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "included-task-ids" + path_buffer

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

                        if (child_yang_name == "tasks"):
                            for c in self.tasks:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.tasks.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tasks"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class TaskMap(Entity):
                    """
                    Computed task map
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap, self).__init__()

                        self.yang_name = "task-map"
                        self.yang_parent_name = "taskgroup"

                        self.tasks = YList(self)

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
                                    super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap, self).__setattr__(name, value)


                    class Tasks(Entity):
                        """
                        List of permitted tasks
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\:  bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\:  bool
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\:  bool
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\:  str
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks, self).__init__()

                            self.yang_name = "tasks"
                            self.yang_parent_name = "task-map"

                            self.debug = YLeaf(YType.boolean, "debug")

                            self.execute = YLeaf(YType.boolean, "execute")

                            self.read = YLeaf(YType.boolean, "read")

                            self.task_id = YLeaf(YType.str, "task-id")

                            self.write = YLeaf(YType.boolean, "write")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("debug",
                                            "execute",
                                            "read",
                                            "task_id",
                                            "write") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.debug.is_set or
                                self.execute.is_set or
                                self.read.is_set or
                                self.task_id.is_set or
                                self.write.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.debug.yfilter != YFilter.not_set or
                                self.execute.yfilter != YFilter.not_set or
                                self.read.yfilter != YFilter.not_set or
                                self.task_id.yfilter != YFilter.not_set or
                                self.write.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "tasks" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.debug.is_set or self.debug.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.debug.get_name_leafdata())
                            if (self.execute.is_set or self.execute.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.execute.get_name_leafdata())
                            if (self.read.is_set or self.read.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.read.get_name_leafdata())
                            if (self.task_id.is_set or self.task_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.task_id.get_name_leafdata())
                            if (self.write.is_set or self.write.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.write.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "debug" or name == "execute" or name == "read" or name == "task-id" or name == "write"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "debug"):
                                self.debug = value
                                self.debug.value_namespace = name_space
                                self.debug.value_namespace_prefix = name_space_prefix
                            if(value_path == "execute"):
                                self.execute = value
                                self.execute.value_namespace = name_space
                                self.execute.value_namespace_prefix = name_space_prefix
                            if(value_path == "read"):
                                self.read = value
                                self.read.value_namespace = name_space
                                self.read.value_namespace_prefix = name_space_prefix
                            if(value_path == "task-id"):
                                self.task_id = value
                                self.task_id.value_namespace = name_space
                                self.task_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "write"):
                                self.write = value
                                self.write.value_namespace = name_space
                                self.write.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.tasks:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.tasks:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "task-map" + path_buffer

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

                        if (child_yang_name == "tasks"):
                            for c in self.tasks:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.tasks.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "tasks"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.name_xr.is_set or
                        (self.included_task_ids is not None and self.included_task_ids.has_data()) or
                        (self.task_map is not None and self.task_map.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name_xr.yfilter != YFilter.not_set or
                        (self.included_task_ids is not None and self.included_task_ids.has_operation()) or
                        (self.task_map is not None and self.task_map.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "taskgroup" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name_xr.is_set or self.name_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name_xr.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "included-task-ids"):
                        if (self.included_task_ids is None):
                            self.included_task_ids = Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds()
                            self.included_task_ids.parent = self
                            self._children_name_map["included_task_ids"] = "included-task-ids"
                        return self.included_task_ids

                    if (child_yang_name == "task-map"):
                        if (self.task_map is None):
                            self.task_map = Aaa.Usergroups.Usergroup.Taskgroup.TaskMap()
                            self.task_map.parent = self
                            self._children_name_map["task_map"] = "task-map"
                        return self.task_map

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "included-task-ids" or name == "task-map" or name == "name-xr"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name-xr"):
                        self.name_xr = value
                        self.name_xr.value_namespace = name_space
                        self.name_xr.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.taskgroup:
                    if (c.has_data()):
                        return True
                return (
                    self.name.is_set or
                    self.name_xr.is_set or
                    (self.task_map is not None and self.task_map.has_data()))

            def has_operation(self):
                for c in self.taskgroup:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.name_xr.yfilter != YFilter.not_set or
                    (self.task_map is not None and self.task_map.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "usergroup" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/usergroups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.name_xr.is_set or self.name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name_xr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "task-map"):
                    if (self.task_map is None):
                        self.task_map = Aaa.Usergroups.Usergroup.TaskMap()
                        self.task_map.parent = self
                        self._children_name_map["task_map"] = "task-map"
                    return self.task_map

                if (child_yang_name == "taskgroup"):
                    for c in self.taskgroup:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Usergroups.Usergroup.Taskgroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.taskgroup.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "task-map" or name == "taskgroup" or name == "name" or name == "name-xr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "name-xr"):
                    self.name_xr = value
                    self.name_xr.value_namespace = name_space
                    self.name_xr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.usergroup:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.usergroup:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "usergroups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "usergroup"):
                for c in self.usergroup:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Aaa.Usergroups.Usergroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.usergroup.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "usergroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AuthenMethod(Entity):
        """
        Current users authentication method
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AuthenMethod, self).__init__()

            self.yang_name = "authen-method"
            self.yang_parent_name = "aaa"

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("authenmethod",
                            "name",
                            "taskmap",
                            "usergroup") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.AuthenMethod, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.AuthenMethod, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.authenmethod.is_set or
                self.name.is_set)

        def has_operation(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.is_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.authenmethod.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.taskmap.yfilter != YFilter.not_set or
                self.usergroup.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "authen-method" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.authenmethod.is_set or self.authenmethod.yfilter != YFilter.not_set):
                leaf_name_data.append(self.authenmethod.get_name_leafdata())
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())

            leaf_name_data.extend(self.taskmap.get_name_leafdata())

            leaf_name_data.extend(self.usergroup.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authenmethod" or name == "name" or name == "taskmap" or name == "usergroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "authenmethod"):
                self.authenmethod = value
                self.authenmethod.value_namespace = name_space
                self.authenmethod.value_namespace_prefix = name_space_prefix
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "taskmap"):
                self.taskmap.append(value)
            if(value_path == "usergroup"):
                self.usergroup.append(value)


    class CurrentUsergroup(Entity):
        """
        Specific Usergroup Information
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.CurrentUsergroup, self).__init__()

            self.yang_name = "current-usergroup"
            self.yang_parent_name = "aaa"

            self.authenmethod = YLeaf(YType.int32, "authenmethod")

            self.name = YLeaf(YType.str, "name")

            self.taskmap = YLeafList(YType.str, "taskmap")

            self.usergroup = YLeafList(YType.str, "usergroup")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("authenmethod",
                            "name",
                            "taskmap",
                            "usergroup") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Aaa.CurrentUsergroup, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Aaa.CurrentUsergroup, self).__setattr__(name, value)

        def has_data(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.yfilter != YFilter.not_set):
                    return True
            return (
                self.authenmethod.is_set or
                self.name.is_set)

        def has_operation(self):
            for leaf in self.taskmap.getYLeafs():
                if (leaf.is_set):
                    return True
            for leaf in self.usergroup.getYLeafs():
                if (leaf.is_set):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.authenmethod.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.taskmap.yfilter != YFilter.not_set or
                self.usergroup.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "current-usergroup" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.authenmethod.is_set or self.authenmethod.yfilter != YFilter.not_set):
                leaf_name_data.append(self.authenmethod.get_name_leafdata())
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())

            leaf_name_data.extend(self.taskmap.get_name_leafdata())

            leaf_name_data.extend(self.usergroup.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "authenmethod" or name == "name" or name == "taskmap" or name == "usergroup"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "authenmethod"):
                self.authenmethod = value
                self.authenmethod.value_namespace = name_space
                self.authenmethod.value_namespace_prefix = name_space_prefix
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "taskmap"):
                self.taskmap.append(value)
            if(value_path == "usergroup"):
                self.usergroup.append(value)


    class Diameter(Entity):
        """
        Diameter operational data
        
        .. attribute:: gx
        
        	Diameter global gx data
        	**type**\:   :py:class:`Gx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gx>`
        
        .. attribute:: gx_session_ids
        
        	Diameter Gx Session data list
        	**type**\:   :py:class:`GxSessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds>`
        
        .. attribute:: gx_statistics
        
        	Diameter Gx Statistics data
        	**type**\:   :py:class:`GxStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxStatistics>`
        
        .. attribute:: gy
        
        	Diameter global gy data
        	**type**\:   :py:class:`Gy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gy>`
        
        .. attribute:: gy_session_ids
        
        	Diameter Gy Session data list
        	**type**\:   :py:class:`GySessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds>`
        
        .. attribute:: gy_statistics
        
        	Diameter Gy Statistics data
        	**type**\:   :py:class:`GyStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GyStatistics>`
        
        .. attribute:: nas
        
        	Diameter NAS data
        	**type**\:   :py:class:`Nas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas>`
        
        .. attribute:: nas_session
        
        	Diameter Nas Session data
        	**type**\:   :py:class:`NasSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession>`
        
        .. attribute:: nas_summary
        
        	Diameter NAS summary
        	**type**\:   :py:class:`NasSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSummary>`
        
        .. attribute:: peers
        
        	Diameter peer global data
        	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers>`
        
        

        """

        _prefix = 'aaa-diameter-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Diameter, self).__init__()

            self.yang_name = "diameter"
            self.yang_parent_name = "aaa"

            self.gx = Aaa.Diameter.Gx()
            self.gx.parent = self
            self._children_name_map["gx"] = "gx"
            self._children_yang_names.add("gx")

            self.gx_session_ids = Aaa.Diameter.GxSessionIds()
            self.gx_session_ids.parent = self
            self._children_name_map["gx_session_ids"] = "gx-session-ids"
            self._children_yang_names.add("gx-session-ids")

            self.gx_statistics = Aaa.Diameter.GxStatistics()
            self.gx_statistics.parent = self
            self._children_name_map["gx_statistics"] = "gx-statistics"
            self._children_yang_names.add("gx-statistics")

            self.gy = Aaa.Diameter.Gy()
            self.gy.parent = self
            self._children_name_map["gy"] = "gy"
            self._children_yang_names.add("gy")

            self.gy_session_ids = Aaa.Diameter.GySessionIds()
            self.gy_session_ids.parent = self
            self._children_name_map["gy_session_ids"] = "gy-session-ids"
            self._children_yang_names.add("gy-session-ids")

            self.gy_statistics = Aaa.Diameter.GyStatistics()
            self.gy_statistics.parent = self
            self._children_name_map["gy_statistics"] = "gy-statistics"
            self._children_yang_names.add("gy-statistics")

            self.nas = Aaa.Diameter.Nas()
            self.nas.parent = self
            self._children_name_map["nas"] = "nas"
            self._children_yang_names.add("nas")

            self.nas_session = Aaa.Diameter.NasSession()
            self.nas_session.parent = self
            self._children_name_map["nas_session"] = "nas-session"
            self._children_yang_names.add("nas-session")

            self.nas_summary = Aaa.Diameter.NasSummary()
            self.nas_summary.parent = self
            self._children_name_map["nas_summary"] = "nas-summary"
            self._children_yang_names.add("nas-summary")

            self.peers = Aaa.Diameter.Peers()
            self.peers.parent = self
            self._children_name_map["peers"] = "peers"
            self._children_yang_names.add("peers")


        class Gy(Entity):
            """
            Diameter global gy data
            
            .. attribute:: is_enabled
            
            	Gy state
            	**type**\:  bool
            
            .. attribute:: retransmits
            
            	Gy retransmit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_timer
            
            	Gy transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Gy, self).__init__()

                self.yang_name = "gy"
                self.yang_parent_name = "diameter"

                self.is_enabled = YLeaf(YType.boolean, "is-enabled")

                self.retransmits = YLeaf(YType.uint32, "retransmits")

                self.tx_timer = YLeaf(YType.uint32, "tx-timer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("is_enabled",
                                "retransmits",
                                "tx_timer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Gy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Gy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.is_enabled.is_set or
                    self.retransmits.is_set or
                    self.tx_timer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.is_enabled.yfilter != YFilter.not_set or
                    self.retransmits.yfilter != YFilter.not_set or
                    self.tx_timer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gy" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.is_enabled.is_set or self.is_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_enabled.get_name_leafdata())
                if (self.retransmits.is_set or self.retransmits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.retransmits.get_name_leafdata())
                if (self.tx_timer.is_set or self.tx_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tx_timer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "is-enabled" or name == "retransmits" or name == "tx-timer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "is-enabled"):
                    self.is_enabled = value
                    self.is_enabled.value_namespace = name_space
                    self.is_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "retransmits"):
                    self.retransmits = value
                    self.retransmits.value_namespace = name_space
                    self.retransmits.value_namespace_prefix = name_space_prefix
                if(value_path == "tx-timer"):
                    self.tx_timer = value
                    self.tx_timer.value_namespace = name_space
                    self.tx_timer.value_namespace_prefix = name_space_prefix


        class GxStatistics(Entity):
            """
            Diameter Gx Statistics data
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messsages
            
            	ASA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_termination_messages
            
            	Session Termination from server
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GxStatistics, self).__init__()

                self.yang_name = "gx-statistics"
                self.yang_parent_name = "diameter"

                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                self.asa_sent_error_messages = YLeaf(YType.uint32, "asa-sent-error-messages")

                self.asa_sent_messsages = YLeaf(YType.uint32, "asa-sent-messsages")

                self.asr_received_error_messages = YLeaf(YType.uint32, "asr-received-error-messages")

                self.asr_received_messages = YLeaf(YType.uint32, "asr-received-messages")

                self.cca_final_error_messages = YLeaf(YType.uint32, "cca-final-error-messages")

                self.cca_final_messages = YLeaf(YType.uint32, "cca-final-messages")

                self.cca_init_error_messages = YLeaf(YType.uint32, "cca-init-error-messages")

                self.cca_init_messages = YLeaf(YType.uint32, "cca-init-messages")

                self.cca_update_error_messages = YLeaf(YType.uint32, "cca-update-error-messages")

                self.cca_update_messages = YLeaf(YType.uint32, "cca-update-messages")

                self.ccr_final_failed_messages = YLeaf(YType.uint32, "ccr-final-failed-messages")

                self.ccr_final_messages = YLeaf(YType.uint32, "ccr-final-messages")

                self.ccr_final_retry_messages = YLeaf(YType.uint32, "ccr-final-retry-messages")

                self.ccr_final_timed_out_messages = YLeaf(YType.uint32, "ccr-final-timed-out-messages")

                self.ccr_init_failed_messages = YLeaf(YType.uint32, "ccr-init-failed-messages")

                self.ccr_init_messages = YLeaf(YType.uint32, "ccr-init-messages")

                self.ccr_init_retry_messages = YLeaf(YType.uint32, "ccr-init-retry-messages")

                self.ccr_init_timed_out_messages = YLeaf(YType.uint32, "ccr-init-timed-out-messages")

                self.ccr_update_failed_messages = YLeaf(YType.uint32, "ccr-update-failed-messages")

                self.ccr_update_messages = YLeaf(YType.uint32, "ccr-update-messages")

                self.ccr_update_retry_messages = YLeaf(YType.uint32, "ccr-update-retry-messages")

                self.ccr_update_timed_out_messages = YLeaf(YType.uint32, "ccr-update-timed-out-messages")

                self.close_sessions = YLeaf(YType.uint32, "close-sessions")

                self.open_sessions = YLeaf(YType.uint32, "open-sessions")

                self.raa_sent_error_messages = YLeaf(YType.uint32, "raa-sent-error-messages")

                self.raa_sent_messages = YLeaf(YType.uint32, "raa-sent-messages")

                self.rar_received_error_messages = YLeaf(YType.uint32, "rar-received-error-messages")

                self.rar_received_messages = YLeaf(YType.uint32, "rar-received-messages")

                self.restore_sessions = YLeaf(YType.uint32, "restore-sessions")

                self.session_termination_messages = YLeaf(YType.uint32, "session-termination-messages")

                self.unknown_request_messages = YLeaf(YType.uint32, "unknown-request-messages")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("active_sessions",
                                "asa_sent_error_messages",
                                "asa_sent_messsages",
                                "asr_received_error_messages",
                                "asr_received_messages",
                                "cca_final_error_messages",
                                "cca_final_messages",
                                "cca_init_error_messages",
                                "cca_init_messages",
                                "cca_update_error_messages",
                                "cca_update_messages",
                                "ccr_final_failed_messages",
                                "ccr_final_messages",
                                "ccr_final_retry_messages",
                                "ccr_final_timed_out_messages",
                                "ccr_init_failed_messages",
                                "ccr_init_messages",
                                "ccr_init_retry_messages",
                                "ccr_init_timed_out_messages",
                                "ccr_update_failed_messages",
                                "ccr_update_messages",
                                "ccr_update_retry_messages",
                                "ccr_update_timed_out_messages",
                                "close_sessions",
                                "open_sessions",
                                "raa_sent_error_messages",
                                "raa_sent_messages",
                                "rar_received_error_messages",
                                "rar_received_messages",
                                "restore_sessions",
                                "session_termination_messages",
                                "unknown_request_messages") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.GxStatistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.GxStatistics, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.active_sessions.is_set or
                    self.asa_sent_error_messages.is_set or
                    self.asa_sent_messsages.is_set or
                    self.asr_received_error_messages.is_set or
                    self.asr_received_messages.is_set or
                    self.cca_final_error_messages.is_set or
                    self.cca_final_messages.is_set or
                    self.cca_init_error_messages.is_set or
                    self.cca_init_messages.is_set or
                    self.cca_update_error_messages.is_set or
                    self.cca_update_messages.is_set or
                    self.ccr_final_failed_messages.is_set or
                    self.ccr_final_messages.is_set or
                    self.ccr_final_retry_messages.is_set or
                    self.ccr_final_timed_out_messages.is_set or
                    self.ccr_init_failed_messages.is_set or
                    self.ccr_init_messages.is_set or
                    self.ccr_init_retry_messages.is_set or
                    self.ccr_init_timed_out_messages.is_set or
                    self.ccr_update_failed_messages.is_set or
                    self.ccr_update_messages.is_set or
                    self.ccr_update_retry_messages.is_set or
                    self.ccr_update_timed_out_messages.is_set or
                    self.close_sessions.is_set or
                    self.open_sessions.is_set or
                    self.raa_sent_error_messages.is_set or
                    self.raa_sent_messages.is_set or
                    self.rar_received_error_messages.is_set or
                    self.rar_received_messages.is_set or
                    self.restore_sessions.is_set or
                    self.session_termination_messages.is_set or
                    self.unknown_request_messages.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.active_sessions.yfilter != YFilter.not_set or
                    self.asa_sent_error_messages.yfilter != YFilter.not_set or
                    self.asa_sent_messsages.yfilter != YFilter.not_set or
                    self.asr_received_error_messages.yfilter != YFilter.not_set or
                    self.asr_received_messages.yfilter != YFilter.not_set or
                    self.cca_final_error_messages.yfilter != YFilter.not_set or
                    self.cca_final_messages.yfilter != YFilter.not_set or
                    self.cca_init_error_messages.yfilter != YFilter.not_set or
                    self.cca_init_messages.yfilter != YFilter.not_set or
                    self.cca_update_error_messages.yfilter != YFilter.not_set or
                    self.cca_update_messages.yfilter != YFilter.not_set or
                    self.ccr_final_failed_messages.yfilter != YFilter.not_set or
                    self.ccr_final_messages.yfilter != YFilter.not_set or
                    self.ccr_final_retry_messages.yfilter != YFilter.not_set or
                    self.ccr_final_timed_out_messages.yfilter != YFilter.not_set or
                    self.ccr_init_failed_messages.yfilter != YFilter.not_set or
                    self.ccr_init_messages.yfilter != YFilter.not_set or
                    self.ccr_init_retry_messages.yfilter != YFilter.not_set or
                    self.ccr_init_timed_out_messages.yfilter != YFilter.not_set or
                    self.ccr_update_failed_messages.yfilter != YFilter.not_set or
                    self.ccr_update_messages.yfilter != YFilter.not_set or
                    self.ccr_update_retry_messages.yfilter != YFilter.not_set or
                    self.ccr_update_timed_out_messages.yfilter != YFilter.not_set or
                    self.close_sessions.yfilter != YFilter.not_set or
                    self.open_sessions.yfilter != YFilter.not_set or
                    self.raa_sent_error_messages.yfilter != YFilter.not_set or
                    self.raa_sent_messages.yfilter != YFilter.not_set or
                    self.rar_received_error_messages.yfilter != YFilter.not_set or
                    self.rar_received_messages.yfilter != YFilter.not_set or
                    self.restore_sessions.yfilter != YFilter.not_set or
                    self.session_termination_messages.yfilter != YFilter.not_set or
                    self.unknown_request_messages.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gx-statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.active_sessions.is_set or self.active_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.active_sessions.get_name_leafdata())
                if (self.asa_sent_error_messages.is_set or self.asa_sent_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asa_sent_error_messages.get_name_leafdata())
                if (self.asa_sent_messsages.is_set or self.asa_sent_messsages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asa_sent_messsages.get_name_leafdata())
                if (self.asr_received_error_messages.is_set or self.asr_received_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asr_received_error_messages.get_name_leafdata())
                if (self.asr_received_messages.is_set or self.asr_received_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asr_received_messages.get_name_leafdata())
                if (self.cca_final_error_messages.is_set or self.cca_final_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_final_error_messages.get_name_leafdata())
                if (self.cca_final_messages.is_set or self.cca_final_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_final_messages.get_name_leafdata())
                if (self.cca_init_error_messages.is_set or self.cca_init_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_init_error_messages.get_name_leafdata())
                if (self.cca_init_messages.is_set or self.cca_init_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_init_messages.get_name_leafdata())
                if (self.cca_update_error_messages.is_set or self.cca_update_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_update_error_messages.get_name_leafdata())
                if (self.cca_update_messages.is_set or self.cca_update_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_update_messages.get_name_leafdata())
                if (self.ccr_final_failed_messages.is_set or self.ccr_final_failed_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_failed_messages.get_name_leafdata())
                if (self.ccr_final_messages.is_set or self.ccr_final_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_messages.get_name_leafdata())
                if (self.ccr_final_retry_messages.is_set or self.ccr_final_retry_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_retry_messages.get_name_leafdata())
                if (self.ccr_final_timed_out_messages.is_set or self.ccr_final_timed_out_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_timed_out_messages.get_name_leafdata())
                if (self.ccr_init_failed_messages.is_set or self.ccr_init_failed_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_failed_messages.get_name_leafdata())
                if (self.ccr_init_messages.is_set or self.ccr_init_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_messages.get_name_leafdata())
                if (self.ccr_init_retry_messages.is_set or self.ccr_init_retry_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_retry_messages.get_name_leafdata())
                if (self.ccr_init_timed_out_messages.is_set or self.ccr_init_timed_out_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_timed_out_messages.get_name_leafdata())
                if (self.ccr_update_failed_messages.is_set or self.ccr_update_failed_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_failed_messages.get_name_leafdata())
                if (self.ccr_update_messages.is_set or self.ccr_update_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_messages.get_name_leafdata())
                if (self.ccr_update_retry_messages.is_set or self.ccr_update_retry_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_retry_messages.get_name_leafdata())
                if (self.ccr_update_timed_out_messages.is_set or self.ccr_update_timed_out_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_timed_out_messages.get_name_leafdata())
                if (self.close_sessions.is_set or self.close_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.close_sessions.get_name_leafdata())
                if (self.open_sessions.is_set or self.open_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.open_sessions.get_name_leafdata())
                if (self.raa_sent_error_messages.is_set or self.raa_sent_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.raa_sent_error_messages.get_name_leafdata())
                if (self.raa_sent_messages.is_set or self.raa_sent_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.raa_sent_messages.get_name_leafdata())
                if (self.rar_received_error_messages.is_set or self.rar_received_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rar_received_error_messages.get_name_leafdata())
                if (self.rar_received_messages.is_set or self.rar_received_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rar_received_messages.get_name_leafdata())
                if (self.restore_sessions.is_set or self.restore_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.restore_sessions.get_name_leafdata())
                if (self.session_termination_messages.is_set or self.session_termination_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_termination_messages.get_name_leafdata())
                if (self.unknown_request_messages.is_set or self.unknown_request_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unknown_request_messages.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "active-sessions" or name == "asa-sent-error-messages" or name == "asa-sent-messsages" or name == "asr-received-error-messages" or name == "asr-received-messages" or name == "cca-final-error-messages" or name == "cca-final-messages" or name == "cca-init-error-messages" or name == "cca-init-messages" or name == "cca-update-error-messages" or name == "cca-update-messages" or name == "ccr-final-failed-messages" or name == "ccr-final-messages" or name == "ccr-final-retry-messages" or name == "ccr-final-timed-out-messages" or name == "ccr-init-failed-messages" or name == "ccr-init-messages" or name == "ccr-init-retry-messages" or name == "ccr-init-timed-out-messages" or name == "ccr-update-failed-messages" or name == "ccr-update-messages" or name == "ccr-update-retry-messages" or name == "ccr-update-timed-out-messages" or name == "close-sessions" or name == "open-sessions" or name == "raa-sent-error-messages" or name == "raa-sent-messages" or name == "rar-received-error-messages" or name == "rar-received-messages" or name == "restore-sessions" or name == "session-termination-messages" or name == "unknown-request-messages"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "active-sessions"):
                    self.active_sessions = value
                    self.active_sessions.value_namespace = name_space
                    self.active_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "asa-sent-error-messages"):
                    self.asa_sent_error_messages = value
                    self.asa_sent_error_messages.value_namespace = name_space
                    self.asa_sent_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "asa-sent-messsages"):
                    self.asa_sent_messsages = value
                    self.asa_sent_messsages.value_namespace = name_space
                    self.asa_sent_messsages.value_namespace_prefix = name_space_prefix
                if(value_path == "asr-received-error-messages"):
                    self.asr_received_error_messages = value
                    self.asr_received_error_messages.value_namespace = name_space
                    self.asr_received_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "asr-received-messages"):
                    self.asr_received_messages = value
                    self.asr_received_messages.value_namespace = name_space
                    self.asr_received_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-final-error-messages"):
                    self.cca_final_error_messages = value
                    self.cca_final_error_messages.value_namespace = name_space
                    self.cca_final_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-final-messages"):
                    self.cca_final_messages = value
                    self.cca_final_messages.value_namespace = name_space
                    self.cca_final_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-init-error-messages"):
                    self.cca_init_error_messages = value
                    self.cca_init_error_messages.value_namespace = name_space
                    self.cca_init_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-init-messages"):
                    self.cca_init_messages = value
                    self.cca_init_messages.value_namespace = name_space
                    self.cca_init_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-update-error-messages"):
                    self.cca_update_error_messages = value
                    self.cca_update_error_messages.value_namespace = name_space
                    self.cca_update_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-update-messages"):
                    self.cca_update_messages = value
                    self.cca_update_messages.value_namespace = name_space
                    self.cca_update_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-failed-messages"):
                    self.ccr_final_failed_messages = value
                    self.ccr_final_failed_messages.value_namespace = name_space
                    self.ccr_final_failed_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-messages"):
                    self.ccr_final_messages = value
                    self.ccr_final_messages.value_namespace = name_space
                    self.ccr_final_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-retry-messages"):
                    self.ccr_final_retry_messages = value
                    self.ccr_final_retry_messages.value_namespace = name_space
                    self.ccr_final_retry_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-timed-out-messages"):
                    self.ccr_final_timed_out_messages = value
                    self.ccr_final_timed_out_messages.value_namespace = name_space
                    self.ccr_final_timed_out_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-failed-messages"):
                    self.ccr_init_failed_messages = value
                    self.ccr_init_failed_messages.value_namespace = name_space
                    self.ccr_init_failed_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-messages"):
                    self.ccr_init_messages = value
                    self.ccr_init_messages.value_namespace = name_space
                    self.ccr_init_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-retry-messages"):
                    self.ccr_init_retry_messages = value
                    self.ccr_init_retry_messages.value_namespace = name_space
                    self.ccr_init_retry_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-timed-out-messages"):
                    self.ccr_init_timed_out_messages = value
                    self.ccr_init_timed_out_messages.value_namespace = name_space
                    self.ccr_init_timed_out_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-failed-messages"):
                    self.ccr_update_failed_messages = value
                    self.ccr_update_failed_messages.value_namespace = name_space
                    self.ccr_update_failed_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-messages"):
                    self.ccr_update_messages = value
                    self.ccr_update_messages.value_namespace = name_space
                    self.ccr_update_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-retry-messages"):
                    self.ccr_update_retry_messages = value
                    self.ccr_update_retry_messages.value_namespace = name_space
                    self.ccr_update_retry_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-timed-out-messages"):
                    self.ccr_update_timed_out_messages = value
                    self.ccr_update_timed_out_messages.value_namespace = name_space
                    self.ccr_update_timed_out_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "close-sessions"):
                    self.close_sessions = value
                    self.close_sessions.value_namespace = name_space
                    self.close_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "open-sessions"):
                    self.open_sessions = value
                    self.open_sessions.value_namespace = name_space
                    self.open_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "raa-sent-error-messages"):
                    self.raa_sent_error_messages = value
                    self.raa_sent_error_messages.value_namespace = name_space
                    self.raa_sent_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "raa-sent-messages"):
                    self.raa_sent_messages = value
                    self.raa_sent_messages.value_namespace = name_space
                    self.raa_sent_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "rar-received-error-messages"):
                    self.rar_received_error_messages = value
                    self.rar_received_error_messages.value_namespace = name_space
                    self.rar_received_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "rar-received-messages"):
                    self.rar_received_messages = value
                    self.rar_received_messages.value_namespace = name_space
                    self.rar_received_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "restore-sessions"):
                    self.restore_sessions = value
                    self.restore_sessions.value_namespace = name_space
                    self.restore_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "session-termination-messages"):
                    self.session_termination_messages = value
                    self.session_termination_messages.value_namespace = name_space
                    self.session_termination_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "unknown-request-messages"):
                    self.unknown_request_messages = value
                    self.unknown_request_messages.value_namespace = name_space
                    self.unknown_request_messages.value_namespace_prefix = name_space_prefix


        class Gx(Entity):
            """
            Diameter global gx data
            
            .. attribute:: is_enabled
            
            	Gx state
            	**type**\:  bool
            
            .. attribute:: retransmits
            
            	Gx retransmit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_timer
            
            	Gx transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Gx, self).__init__()

                self.yang_name = "gx"
                self.yang_parent_name = "diameter"

                self.is_enabled = YLeaf(YType.boolean, "is-enabled")

                self.retransmits = YLeaf(YType.uint32, "retransmits")

                self.tx_timer = YLeaf(YType.uint32, "tx-timer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("is_enabled",
                                "retransmits",
                                "tx_timer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Gx, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Gx, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.is_enabled.is_set or
                    self.retransmits.is_set or
                    self.tx_timer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.is_enabled.yfilter != YFilter.not_set or
                    self.retransmits.yfilter != YFilter.not_set or
                    self.tx_timer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gx" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.is_enabled.is_set or self.is_enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.is_enabled.get_name_leafdata())
                if (self.retransmits.is_set or self.retransmits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.retransmits.get_name_leafdata())
                if (self.tx_timer.is_set or self.tx_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tx_timer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "is-enabled" or name == "retransmits" or name == "tx-timer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "is-enabled"):
                    self.is_enabled = value
                    self.is_enabled.value_namespace = name_space
                    self.is_enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "retransmits"):
                    self.retransmits = value
                    self.retransmits.value_namespace = name_space
                    self.retransmits.value_namespace_prefix = name_space_prefix
                if(value_path == "tx-timer"):
                    self.tx_timer = value
                    self.tx_timer.value_namespace = name_space
                    self.tx_timer.value_namespace_prefix = name_space_prefix


        class Peers(Entity):
            """
            Diameter peer global data
            
            .. attribute:: conn_retry_timer
            
            	Connection retry timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: origin_host
            
            	Origin Host
            	**type**\:  str
            
            .. attribute:: origin_realm
            
            	Origin Realm
            	**type**\:  str
            
            .. attribute:: peer
            
            	Peer List
            	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers.Peer>`
            
            .. attribute:: source_interface
            
            	Source Interface
            	**type**\:  str
            
            .. attribute:: tls_trustpoint
            
            	TLS Trustpoint
            	**type**\:  str
            
            .. attribute:: trans_max
            
            	Maximum number of transactions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: trans_total
            
            	Total number of transactions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: transaction_timer
            
            	Transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: watchdog_timer
            
            	Watch dog timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Peers, self).__init__()

                self.yang_name = "peers"
                self.yang_parent_name = "diameter"

                self.conn_retry_timer = YLeaf(YType.uint32, "conn-retry-timer")

                self.origin_host = YLeaf(YType.str, "origin-host")

                self.origin_realm = YLeaf(YType.str, "origin-realm")

                self.source_interface = YLeaf(YType.str, "source-interface")

                self.tls_trustpoint = YLeaf(YType.str, "tls-trustpoint")

                self.trans_max = YLeaf(YType.uint32, "trans-max")

                self.trans_total = YLeaf(YType.uint32, "trans-total")

                self.transaction_timer = YLeaf(YType.uint32, "transaction-timer")

                self.watchdog_timer = YLeaf(YType.uint32, "watchdog-timer")

                self.peer = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("conn_retry_timer",
                                "origin_host",
                                "origin_realm",
                                "source_interface",
                                "tls_trustpoint",
                                "trans_max",
                                "trans_total",
                                "transaction_timer",
                                "watchdog_timer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Peers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Peers, self).__setattr__(name, value)


            class Peer(Entity):
                """
                Peer List
                
                .. attribute:: address
                
                	IPv4 or IPv6 address of DIAMETER peer
                	**type**\:  str
                
                .. attribute:: conn_retry_timer
                
                	Connection retry timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: destination_host
                
                	Destination host name
                	**type**\:  str
                
                .. attribute:: destination_realm
                
                	Destination realm
                	**type**\:  str
                
                .. attribute:: firmware_revision
                
                	Firmware revision
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_aa_as
                
                	Incoming AAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_as
                
                	Incoming ACAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_rs
                
                	Incoming ACRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_as_as
                
                	Incoming ASAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_as_rs
                
                	Incoming ASRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_as
                
                	Incoming CCAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_rs
                
                	Incoming CCRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_as
                
                	Incoming CEAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_rs
                
                	Incoming CERs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_as
                
                	Incoming DPAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_rs
                
                	Incoming DPRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_as
                
                	Incoming DWAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_rs
                
                	Incoming DWRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_as
                
                	Incoming RAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_rs
                
                	Incoming RARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_as
                
                	Incoming STAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_rs
                
                	Incoming STRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_disconnect_cause
                
                	Last Disconnect Reason
                	**type**\:   :py:class:`DisconnectCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.DisconnectCause>`
                
                .. attribute:: malformed_requests
                
                	Malformed Requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_aa_rs
                
                	Outgoing AARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_as
                
                	Outgoing ACAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_rs
                
                	Outgoing ACRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_as
                
                	Outgoing ASAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_rs
                
                	Outgoing ASRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_as
                
                	Outgoing CCAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_rs
                
                	Outgoing CCRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_as
                
                	Outgoing CEAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_rs
                
                	Outgoing CERs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_as
                
                	Outgoing DPAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_rs
                
                	Outgoing DPRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_as
                
                	Outgoing DWAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_rs
                
                	Outgoing DWRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_as
                
                	Outgoing RAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_rs
                
                	Outgoing RARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_as
                
                	Outgoing STAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_rs
                
                	Outgoing STRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_index
                
                	Peer Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_name
                
                	Peer Name
                	**type**\:  str
                
                .. attribute:: peer_type
                
                	Peer Type
                	**type**\:   :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.Peer>`
                
                .. attribute:: port
                
                	Port number on which the peeris running
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_connect
                
                	Local Connection port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: protocol_type
                
                	Protocol Type
                	**type**\:   :py:class:`ProtocolTypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.ProtocolTypeValue>`
                
                .. attribute:: received_permanent_fails
                
                	Permanent Failures Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_proto_errors
                
                	Protocol Error Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_transient_fails
                
                	Transient failures Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: security_type
                
                	Security type used to transport
                	**type**\:   :py:class:`SecurityTypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.SecurityTypeValue>`
                
                .. attribute:: sent_permanent_fails
                
                	Permanent Failures Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_proto_errors
                
                	Protocol Error Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_transient_fails
                
                	Transient failures Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: source_interface
                
                	Source Interface
                	**type**\:  str
                
                .. attribute:: state
                
                	Peer Connection Status
                	**type**\:   :py:class:`PeerStateValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.PeerStateValue>`
                
                .. attribute:: state_duration
                
                	State Duration in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transaction_timer
                
                	Transaction timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transport_down
                
                	Transport Down
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	Vrf Name
                	**type**\:  str
                
                .. attribute:: watchdog_timer
                
                	Watch dog timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: who_init_disconnect
                
                	Who Initiated Disconnect
                	**type**\:   :py:class:`WhoInitiatedDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.WhoInitiatedDisconnect>`
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.Peers.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "peers"

                    self.address = YLeaf(YType.str, "address")

                    self.conn_retry_timer = YLeaf(YType.uint32, "conn-retry-timer")

                    self.destination_host = YLeaf(YType.str, "destination-host")

                    self.destination_realm = YLeaf(YType.str, "destination-realm")

                    self.firmware_revision = YLeaf(YType.uint32, "firmware-revision")

                    self.in_aa_as = YLeaf(YType.uint32, "in-aa-as")

                    self.in_ac_as = YLeaf(YType.uint32, "in-ac-as")

                    self.in_ac_rs = YLeaf(YType.uint32, "in-ac-rs")

                    self.in_as_as = YLeaf(YType.uint32, "in-as-as")

                    self.in_as_rs = YLeaf(YType.uint32, "in-as-rs")

                    self.in_cc_as = YLeaf(YType.uint32, "in-cc-as")

                    self.in_cc_rs = YLeaf(YType.uint32, "in-cc-rs")

                    self.in_ce_as = YLeaf(YType.uint32, "in-ce-as")

                    self.in_ce_rs = YLeaf(YType.uint32, "in-ce-rs")

                    self.in_dp_as = YLeaf(YType.uint32, "in-dp-as")

                    self.in_dp_rs = YLeaf(YType.uint32, "in-dp-rs")

                    self.in_dw_as = YLeaf(YType.uint32, "in-dw-as")

                    self.in_dw_rs = YLeaf(YType.uint32, "in-dw-rs")

                    self.in_ra_as = YLeaf(YType.uint32, "in-ra-as")

                    self.in_ra_rs = YLeaf(YType.uint32, "in-ra-rs")

                    self.in_st_as = YLeaf(YType.uint32, "in-st-as")

                    self.in_st_rs = YLeaf(YType.uint32, "in-st-rs")

                    self.last_disconnect_cause = YLeaf(YType.enumeration, "last-disconnect-cause")

                    self.malformed_requests = YLeaf(YType.uint32, "malformed-requests")

                    self.out_aa_rs = YLeaf(YType.uint32, "out-aa-rs")

                    self.out_ac_as = YLeaf(YType.uint32, "out-ac-as")

                    self.out_ac_rs = YLeaf(YType.uint32, "out-ac-rs")

                    self.out_as_as = YLeaf(YType.uint32, "out-as-as")

                    self.out_as_rs = YLeaf(YType.uint32, "out-as-rs")

                    self.out_cc_as = YLeaf(YType.uint32, "out-cc-as")

                    self.out_cc_rs = YLeaf(YType.uint32, "out-cc-rs")

                    self.out_ce_as = YLeaf(YType.uint32, "out-ce-as")

                    self.out_ce_rs = YLeaf(YType.uint32, "out-ce-rs")

                    self.out_dp_as = YLeaf(YType.uint32, "out-dp-as")

                    self.out_dp_rs = YLeaf(YType.uint32, "out-dp-rs")

                    self.out_dw_as = YLeaf(YType.uint32, "out-dw-as")

                    self.out_dw_rs = YLeaf(YType.uint32, "out-dw-rs")

                    self.out_ra_as = YLeaf(YType.uint32, "out-ra-as")

                    self.out_ra_rs = YLeaf(YType.uint32, "out-ra-rs")

                    self.out_st_as = YLeaf(YType.uint32, "out-st-as")

                    self.out_st_rs = YLeaf(YType.uint32, "out-st-rs")

                    self.peer_index = YLeaf(YType.uint32, "peer-index")

                    self.peer_name = YLeaf(YType.str, "peer-name")

                    self.peer_type = YLeaf(YType.enumeration, "peer-type")

                    self.port = YLeaf(YType.uint32, "port")

                    self.port_connect = YLeaf(YType.uint32, "port-connect")

                    self.protocol_type = YLeaf(YType.enumeration, "protocol-type")

                    self.received_permanent_fails = YLeaf(YType.uint32, "received-permanent-fails")

                    self.received_proto_errors = YLeaf(YType.uint32, "received-proto-errors")

                    self.received_transient_fails = YLeaf(YType.uint32, "received-transient-fails")

                    self.security_type = YLeaf(YType.enumeration, "security-type")

                    self.sent_permanent_fails = YLeaf(YType.uint32, "sent-permanent-fails")

                    self.sent_proto_errors = YLeaf(YType.uint32, "sent-proto-errors")

                    self.sent_transient_fails = YLeaf(YType.uint32, "sent-transient-fails")

                    self.source_interface = YLeaf(YType.str, "source-interface")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.state_duration = YLeaf(YType.uint32, "state-duration")

                    self.transaction_timer = YLeaf(YType.uint32, "transaction-timer")

                    self.transport_down = YLeaf(YType.uint32, "transport-down")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.watchdog_timer = YLeaf(YType.uint32, "watchdog-timer")

                    self.who_init_disconnect = YLeaf(YType.enumeration, "who-init-disconnect")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "conn_retry_timer",
                                    "destination_host",
                                    "destination_realm",
                                    "firmware_revision",
                                    "in_aa_as",
                                    "in_ac_as",
                                    "in_ac_rs",
                                    "in_as_as",
                                    "in_as_rs",
                                    "in_cc_as",
                                    "in_cc_rs",
                                    "in_ce_as",
                                    "in_ce_rs",
                                    "in_dp_as",
                                    "in_dp_rs",
                                    "in_dw_as",
                                    "in_dw_rs",
                                    "in_ra_as",
                                    "in_ra_rs",
                                    "in_st_as",
                                    "in_st_rs",
                                    "last_disconnect_cause",
                                    "malformed_requests",
                                    "out_aa_rs",
                                    "out_ac_as",
                                    "out_ac_rs",
                                    "out_as_as",
                                    "out_as_rs",
                                    "out_cc_as",
                                    "out_cc_rs",
                                    "out_ce_as",
                                    "out_ce_rs",
                                    "out_dp_as",
                                    "out_dp_rs",
                                    "out_dw_as",
                                    "out_dw_rs",
                                    "out_ra_as",
                                    "out_ra_rs",
                                    "out_st_as",
                                    "out_st_rs",
                                    "peer_index",
                                    "peer_name",
                                    "peer_type",
                                    "port",
                                    "port_connect",
                                    "protocol_type",
                                    "received_permanent_fails",
                                    "received_proto_errors",
                                    "received_transient_fails",
                                    "security_type",
                                    "sent_permanent_fails",
                                    "sent_proto_errors",
                                    "sent_transient_fails",
                                    "source_interface",
                                    "state",
                                    "state_duration",
                                    "transaction_timer",
                                    "transport_down",
                                    "vrf_name",
                                    "watchdog_timer",
                                    "who_init_disconnect") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.Peers.Peer, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.Peers.Peer, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.conn_retry_timer.is_set or
                        self.destination_host.is_set or
                        self.destination_realm.is_set or
                        self.firmware_revision.is_set or
                        self.in_aa_as.is_set or
                        self.in_ac_as.is_set or
                        self.in_ac_rs.is_set or
                        self.in_as_as.is_set or
                        self.in_as_rs.is_set or
                        self.in_cc_as.is_set or
                        self.in_cc_rs.is_set or
                        self.in_ce_as.is_set or
                        self.in_ce_rs.is_set or
                        self.in_dp_as.is_set or
                        self.in_dp_rs.is_set or
                        self.in_dw_as.is_set or
                        self.in_dw_rs.is_set or
                        self.in_ra_as.is_set or
                        self.in_ra_rs.is_set or
                        self.in_st_as.is_set or
                        self.in_st_rs.is_set or
                        self.last_disconnect_cause.is_set or
                        self.malformed_requests.is_set or
                        self.out_aa_rs.is_set or
                        self.out_ac_as.is_set or
                        self.out_ac_rs.is_set or
                        self.out_as_as.is_set or
                        self.out_as_rs.is_set or
                        self.out_cc_as.is_set or
                        self.out_cc_rs.is_set or
                        self.out_ce_as.is_set or
                        self.out_ce_rs.is_set or
                        self.out_dp_as.is_set or
                        self.out_dp_rs.is_set or
                        self.out_dw_as.is_set or
                        self.out_dw_rs.is_set or
                        self.out_ra_as.is_set or
                        self.out_ra_rs.is_set or
                        self.out_st_as.is_set or
                        self.out_st_rs.is_set or
                        self.peer_index.is_set or
                        self.peer_name.is_set or
                        self.peer_type.is_set or
                        self.port.is_set or
                        self.port_connect.is_set or
                        self.protocol_type.is_set or
                        self.received_permanent_fails.is_set or
                        self.received_proto_errors.is_set or
                        self.received_transient_fails.is_set or
                        self.security_type.is_set or
                        self.sent_permanent_fails.is_set or
                        self.sent_proto_errors.is_set or
                        self.sent_transient_fails.is_set or
                        self.source_interface.is_set or
                        self.state.is_set or
                        self.state_duration.is_set or
                        self.transaction_timer.is_set or
                        self.transport_down.is_set or
                        self.vrf_name.is_set or
                        self.watchdog_timer.is_set or
                        self.who_init_disconnect.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.conn_retry_timer.yfilter != YFilter.not_set or
                        self.destination_host.yfilter != YFilter.not_set or
                        self.destination_realm.yfilter != YFilter.not_set or
                        self.firmware_revision.yfilter != YFilter.not_set or
                        self.in_aa_as.yfilter != YFilter.not_set or
                        self.in_ac_as.yfilter != YFilter.not_set or
                        self.in_ac_rs.yfilter != YFilter.not_set or
                        self.in_as_as.yfilter != YFilter.not_set or
                        self.in_as_rs.yfilter != YFilter.not_set or
                        self.in_cc_as.yfilter != YFilter.not_set or
                        self.in_cc_rs.yfilter != YFilter.not_set or
                        self.in_ce_as.yfilter != YFilter.not_set or
                        self.in_ce_rs.yfilter != YFilter.not_set or
                        self.in_dp_as.yfilter != YFilter.not_set or
                        self.in_dp_rs.yfilter != YFilter.not_set or
                        self.in_dw_as.yfilter != YFilter.not_set or
                        self.in_dw_rs.yfilter != YFilter.not_set or
                        self.in_ra_as.yfilter != YFilter.not_set or
                        self.in_ra_rs.yfilter != YFilter.not_set or
                        self.in_st_as.yfilter != YFilter.not_set or
                        self.in_st_rs.yfilter != YFilter.not_set or
                        self.last_disconnect_cause.yfilter != YFilter.not_set or
                        self.malformed_requests.yfilter != YFilter.not_set or
                        self.out_aa_rs.yfilter != YFilter.not_set or
                        self.out_ac_as.yfilter != YFilter.not_set or
                        self.out_ac_rs.yfilter != YFilter.not_set or
                        self.out_as_as.yfilter != YFilter.not_set or
                        self.out_as_rs.yfilter != YFilter.not_set or
                        self.out_cc_as.yfilter != YFilter.not_set or
                        self.out_cc_rs.yfilter != YFilter.not_set or
                        self.out_ce_as.yfilter != YFilter.not_set or
                        self.out_ce_rs.yfilter != YFilter.not_set or
                        self.out_dp_as.yfilter != YFilter.not_set or
                        self.out_dp_rs.yfilter != YFilter.not_set or
                        self.out_dw_as.yfilter != YFilter.not_set or
                        self.out_dw_rs.yfilter != YFilter.not_set or
                        self.out_ra_as.yfilter != YFilter.not_set or
                        self.out_ra_rs.yfilter != YFilter.not_set or
                        self.out_st_as.yfilter != YFilter.not_set or
                        self.out_st_rs.yfilter != YFilter.not_set or
                        self.peer_index.yfilter != YFilter.not_set or
                        self.peer_name.yfilter != YFilter.not_set or
                        self.peer_type.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.port_connect.yfilter != YFilter.not_set or
                        self.protocol_type.yfilter != YFilter.not_set or
                        self.received_permanent_fails.yfilter != YFilter.not_set or
                        self.received_proto_errors.yfilter != YFilter.not_set or
                        self.received_transient_fails.yfilter != YFilter.not_set or
                        self.security_type.yfilter != YFilter.not_set or
                        self.sent_permanent_fails.yfilter != YFilter.not_set or
                        self.sent_proto_errors.yfilter != YFilter.not_set or
                        self.sent_transient_fails.yfilter != YFilter.not_set or
                        self.source_interface.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.state_duration.yfilter != YFilter.not_set or
                        self.transaction_timer.yfilter != YFilter.not_set or
                        self.transport_down.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set or
                        self.watchdog_timer.yfilter != YFilter.not_set or
                        self.who_init_disconnect.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "peer" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/peers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.conn_retry_timer.is_set or self.conn_retry_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conn_retry_timer.get_name_leafdata())
                    if (self.destination_host.is_set or self.destination_host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_host.get_name_leafdata())
                    if (self.destination_realm.is_set or self.destination_realm.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_realm.get_name_leafdata())
                    if (self.firmware_revision.is_set or self.firmware_revision.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.firmware_revision.get_name_leafdata())
                    if (self.in_aa_as.is_set or self.in_aa_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_aa_as.get_name_leafdata())
                    if (self.in_ac_as.is_set or self.in_ac_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_ac_as.get_name_leafdata())
                    if (self.in_ac_rs.is_set or self.in_ac_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_ac_rs.get_name_leafdata())
                    if (self.in_as_as.is_set or self.in_as_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_as_as.get_name_leafdata())
                    if (self.in_as_rs.is_set or self.in_as_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_as_rs.get_name_leafdata())
                    if (self.in_cc_as.is_set or self.in_cc_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_cc_as.get_name_leafdata())
                    if (self.in_cc_rs.is_set or self.in_cc_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_cc_rs.get_name_leafdata())
                    if (self.in_ce_as.is_set or self.in_ce_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_ce_as.get_name_leafdata())
                    if (self.in_ce_rs.is_set or self.in_ce_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_ce_rs.get_name_leafdata())
                    if (self.in_dp_as.is_set or self.in_dp_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_dp_as.get_name_leafdata())
                    if (self.in_dp_rs.is_set or self.in_dp_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_dp_rs.get_name_leafdata())
                    if (self.in_dw_as.is_set or self.in_dw_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_dw_as.get_name_leafdata())
                    if (self.in_dw_rs.is_set or self.in_dw_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_dw_rs.get_name_leafdata())
                    if (self.in_ra_as.is_set or self.in_ra_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_ra_as.get_name_leafdata())
                    if (self.in_ra_rs.is_set or self.in_ra_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_ra_rs.get_name_leafdata())
                    if (self.in_st_as.is_set or self.in_st_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_st_as.get_name_leafdata())
                    if (self.in_st_rs.is_set or self.in_st_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.in_st_rs.get_name_leafdata())
                    if (self.last_disconnect_cause.is_set or self.last_disconnect_cause.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_disconnect_cause.get_name_leafdata())
                    if (self.malformed_requests.is_set or self.malformed_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.malformed_requests.get_name_leafdata())
                    if (self.out_aa_rs.is_set or self.out_aa_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_aa_rs.get_name_leafdata())
                    if (self.out_ac_as.is_set or self.out_ac_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_ac_as.get_name_leafdata())
                    if (self.out_ac_rs.is_set or self.out_ac_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_ac_rs.get_name_leafdata())
                    if (self.out_as_as.is_set or self.out_as_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_as_as.get_name_leafdata())
                    if (self.out_as_rs.is_set or self.out_as_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_as_rs.get_name_leafdata())
                    if (self.out_cc_as.is_set or self.out_cc_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_cc_as.get_name_leafdata())
                    if (self.out_cc_rs.is_set or self.out_cc_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_cc_rs.get_name_leafdata())
                    if (self.out_ce_as.is_set or self.out_ce_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_ce_as.get_name_leafdata())
                    if (self.out_ce_rs.is_set or self.out_ce_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_ce_rs.get_name_leafdata())
                    if (self.out_dp_as.is_set or self.out_dp_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_dp_as.get_name_leafdata())
                    if (self.out_dp_rs.is_set or self.out_dp_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_dp_rs.get_name_leafdata())
                    if (self.out_dw_as.is_set or self.out_dw_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_dw_as.get_name_leafdata())
                    if (self.out_dw_rs.is_set or self.out_dw_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_dw_rs.get_name_leafdata())
                    if (self.out_ra_as.is_set or self.out_ra_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_ra_as.get_name_leafdata())
                    if (self.out_ra_rs.is_set or self.out_ra_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_ra_rs.get_name_leafdata())
                    if (self.out_st_as.is_set or self.out_st_as.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_st_as.get_name_leafdata())
                    if (self.out_st_rs.is_set or self.out_st_rs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.out_st_rs.get_name_leafdata())
                    if (self.peer_index.is_set or self.peer_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_index.get_name_leafdata())
                    if (self.peer_name.is_set or self.peer_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_name.get_name_leafdata())
                    if (self.peer_type.is_set or self.peer_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.peer_type.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.port_connect.is_set or self.port_connect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port_connect.get_name_leafdata())
                    if (self.protocol_type.is_set or self.protocol_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.protocol_type.get_name_leafdata())
                    if (self.received_permanent_fails.is_set or self.received_permanent_fails.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_permanent_fails.get_name_leafdata())
                    if (self.received_proto_errors.is_set or self.received_proto_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_proto_errors.get_name_leafdata())
                    if (self.received_transient_fails.is_set or self.received_transient_fails.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.received_transient_fails.get_name_leafdata())
                    if (self.security_type.is_set or self.security_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.security_type.get_name_leafdata())
                    if (self.sent_permanent_fails.is_set or self.sent_permanent_fails.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sent_permanent_fails.get_name_leafdata())
                    if (self.sent_proto_errors.is_set or self.sent_proto_errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sent_proto_errors.get_name_leafdata())
                    if (self.sent_transient_fails.is_set or self.sent_transient_fails.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sent_transient_fails.get_name_leafdata())
                    if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.source_interface.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.state_duration.is_set or self.state_duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state_duration.get_name_leafdata())
                    if (self.transaction_timer.is_set or self.transaction_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transaction_timer.get_name_leafdata())
                    if (self.transport_down.is_set or self.transport_down.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.transport_down.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())
                    if (self.watchdog_timer.is_set or self.watchdog_timer.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.watchdog_timer.get_name_leafdata())
                    if (self.who_init_disconnect.is_set or self.who_init_disconnect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.who_init_disconnect.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "conn-retry-timer" or name == "destination-host" or name == "destination-realm" or name == "firmware-revision" or name == "in-aa-as" or name == "in-ac-as" or name == "in-ac-rs" or name == "in-as-as" or name == "in-as-rs" or name == "in-cc-as" or name == "in-cc-rs" or name == "in-ce-as" or name == "in-ce-rs" or name == "in-dp-as" or name == "in-dp-rs" or name == "in-dw-as" or name == "in-dw-rs" or name == "in-ra-as" or name == "in-ra-rs" or name == "in-st-as" or name == "in-st-rs" or name == "last-disconnect-cause" or name == "malformed-requests" or name == "out-aa-rs" or name == "out-ac-as" or name == "out-ac-rs" or name == "out-as-as" or name == "out-as-rs" or name == "out-cc-as" or name == "out-cc-rs" or name == "out-ce-as" or name == "out-ce-rs" or name == "out-dp-as" or name == "out-dp-rs" or name == "out-dw-as" or name == "out-dw-rs" or name == "out-ra-as" or name == "out-ra-rs" or name == "out-st-as" or name == "out-st-rs" or name == "peer-index" or name == "peer-name" or name == "peer-type" or name == "port" or name == "port-connect" or name == "protocol-type" or name == "received-permanent-fails" or name == "received-proto-errors" or name == "received-transient-fails" or name == "security-type" or name == "sent-permanent-fails" or name == "sent-proto-errors" or name == "sent-transient-fails" or name == "source-interface" or name == "state" or name == "state-duration" or name == "transaction-timer" or name == "transport-down" or name == "vrf-name" or name == "watchdog-timer" or name == "who-init-disconnect"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "conn-retry-timer"):
                        self.conn_retry_timer = value
                        self.conn_retry_timer.value_namespace = name_space
                        self.conn_retry_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-host"):
                        self.destination_host = value
                        self.destination_host.value_namespace = name_space
                        self.destination_host.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-realm"):
                        self.destination_realm = value
                        self.destination_realm.value_namespace = name_space
                        self.destination_realm.value_namespace_prefix = name_space_prefix
                    if(value_path == "firmware-revision"):
                        self.firmware_revision = value
                        self.firmware_revision.value_namespace = name_space
                        self.firmware_revision.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-aa-as"):
                        self.in_aa_as = value
                        self.in_aa_as.value_namespace = name_space
                        self.in_aa_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-ac-as"):
                        self.in_ac_as = value
                        self.in_ac_as.value_namespace = name_space
                        self.in_ac_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-ac-rs"):
                        self.in_ac_rs = value
                        self.in_ac_rs.value_namespace = name_space
                        self.in_ac_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-as-as"):
                        self.in_as_as = value
                        self.in_as_as.value_namespace = name_space
                        self.in_as_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-as-rs"):
                        self.in_as_rs = value
                        self.in_as_rs.value_namespace = name_space
                        self.in_as_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-cc-as"):
                        self.in_cc_as = value
                        self.in_cc_as.value_namespace = name_space
                        self.in_cc_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-cc-rs"):
                        self.in_cc_rs = value
                        self.in_cc_rs.value_namespace = name_space
                        self.in_cc_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-ce-as"):
                        self.in_ce_as = value
                        self.in_ce_as.value_namespace = name_space
                        self.in_ce_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-ce-rs"):
                        self.in_ce_rs = value
                        self.in_ce_rs.value_namespace = name_space
                        self.in_ce_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-dp-as"):
                        self.in_dp_as = value
                        self.in_dp_as.value_namespace = name_space
                        self.in_dp_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-dp-rs"):
                        self.in_dp_rs = value
                        self.in_dp_rs.value_namespace = name_space
                        self.in_dp_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-dw-as"):
                        self.in_dw_as = value
                        self.in_dw_as.value_namespace = name_space
                        self.in_dw_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-dw-rs"):
                        self.in_dw_rs = value
                        self.in_dw_rs.value_namespace = name_space
                        self.in_dw_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-ra-as"):
                        self.in_ra_as = value
                        self.in_ra_as.value_namespace = name_space
                        self.in_ra_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-ra-rs"):
                        self.in_ra_rs = value
                        self.in_ra_rs.value_namespace = name_space
                        self.in_ra_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-st-as"):
                        self.in_st_as = value
                        self.in_st_as.value_namespace = name_space
                        self.in_st_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "in-st-rs"):
                        self.in_st_rs = value
                        self.in_st_rs.value_namespace = name_space
                        self.in_st_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-disconnect-cause"):
                        self.last_disconnect_cause = value
                        self.last_disconnect_cause.value_namespace = name_space
                        self.last_disconnect_cause.value_namespace_prefix = name_space_prefix
                    if(value_path == "malformed-requests"):
                        self.malformed_requests = value
                        self.malformed_requests.value_namespace = name_space
                        self.malformed_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-aa-rs"):
                        self.out_aa_rs = value
                        self.out_aa_rs.value_namespace = name_space
                        self.out_aa_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-ac-as"):
                        self.out_ac_as = value
                        self.out_ac_as.value_namespace = name_space
                        self.out_ac_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-ac-rs"):
                        self.out_ac_rs = value
                        self.out_ac_rs.value_namespace = name_space
                        self.out_ac_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-as-as"):
                        self.out_as_as = value
                        self.out_as_as.value_namespace = name_space
                        self.out_as_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-as-rs"):
                        self.out_as_rs = value
                        self.out_as_rs.value_namespace = name_space
                        self.out_as_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-cc-as"):
                        self.out_cc_as = value
                        self.out_cc_as.value_namespace = name_space
                        self.out_cc_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-cc-rs"):
                        self.out_cc_rs = value
                        self.out_cc_rs.value_namespace = name_space
                        self.out_cc_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-ce-as"):
                        self.out_ce_as = value
                        self.out_ce_as.value_namespace = name_space
                        self.out_ce_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-ce-rs"):
                        self.out_ce_rs = value
                        self.out_ce_rs.value_namespace = name_space
                        self.out_ce_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-dp-as"):
                        self.out_dp_as = value
                        self.out_dp_as.value_namespace = name_space
                        self.out_dp_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-dp-rs"):
                        self.out_dp_rs = value
                        self.out_dp_rs.value_namespace = name_space
                        self.out_dp_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-dw-as"):
                        self.out_dw_as = value
                        self.out_dw_as.value_namespace = name_space
                        self.out_dw_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-dw-rs"):
                        self.out_dw_rs = value
                        self.out_dw_rs.value_namespace = name_space
                        self.out_dw_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-ra-as"):
                        self.out_ra_as = value
                        self.out_ra_as.value_namespace = name_space
                        self.out_ra_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-ra-rs"):
                        self.out_ra_rs = value
                        self.out_ra_rs.value_namespace = name_space
                        self.out_ra_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-st-as"):
                        self.out_st_as = value
                        self.out_st_as.value_namespace = name_space
                        self.out_st_as.value_namespace_prefix = name_space_prefix
                    if(value_path == "out-st-rs"):
                        self.out_st_rs = value
                        self.out_st_rs.value_namespace = name_space
                        self.out_st_rs.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-index"):
                        self.peer_index = value
                        self.peer_index.value_namespace = name_space
                        self.peer_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-name"):
                        self.peer_name = value
                        self.peer_name.value_namespace = name_space
                        self.peer_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "peer-type"):
                        self.peer_type = value
                        self.peer_type.value_namespace = name_space
                        self.peer_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "port-connect"):
                        self.port_connect = value
                        self.port_connect.value_namespace = name_space
                        self.port_connect.value_namespace_prefix = name_space_prefix
                    if(value_path == "protocol-type"):
                        self.protocol_type = value
                        self.protocol_type.value_namespace = name_space
                        self.protocol_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-permanent-fails"):
                        self.received_permanent_fails = value
                        self.received_permanent_fails.value_namespace = name_space
                        self.received_permanent_fails.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-proto-errors"):
                        self.received_proto_errors = value
                        self.received_proto_errors.value_namespace = name_space
                        self.received_proto_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "received-transient-fails"):
                        self.received_transient_fails = value
                        self.received_transient_fails.value_namespace = name_space
                        self.received_transient_fails.value_namespace_prefix = name_space_prefix
                    if(value_path == "security-type"):
                        self.security_type = value
                        self.security_type.value_namespace = name_space
                        self.security_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "sent-permanent-fails"):
                        self.sent_permanent_fails = value
                        self.sent_permanent_fails.value_namespace = name_space
                        self.sent_permanent_fails.value_namespace_prefix = name_space_prefix
                    if(value_path == "sent-proto-errors"):
                        self.sent_proto_errors = value
                        self.sent_proto_errors.value_namespace = name_space
                        self.sent_proto_errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "sent-transient-fails"):
                        self.sent_transient_fails = value
                        self.sent_transient_fails.value_namespace = name_space
                        self.sent_transient_fails.value_namespace_prefix = name_space_prefix
                    if(value_path == "source-interface"):
                        self.source_interface = value
                        self.source_interface.value_namespace = name_space
                        self.source_interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "state-duration"):
                        self.state_duration = value
                        self.state_duration.value_namespace = name_space
                        self.state_duration.value_namespace_prefix = name_space_prefix
                    if(value_path == "transaction-timer"):
                        self.transaction_timer = value
                        self.transaction_timer.value_namespace = name_space
                        self.transaction_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "transport-down"):
                        self.transport_down = value
                        self.transport_down.value_namespace = name_space
                        self.transport_down.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "watchdog-timer"):
                        self.watchdog_timer = value
                        self.watchdog_timer.value_namespace = name_space
                        self.watchdog_timer.value_namespace_prefix = name_space_prefix
                    if(value_path == "who-init-disconnect"):
                        self.who_init_disconnect = value
                        self.who_init_disconnect.value_namespace = name_space
                        self.who_init_disconnect.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.peer:
                    if (c.has_data()):
                        return True
                return (
                    self.conn_retry_timer.is_set or
                    self.origin_host.is_set or
                    self.origin_realm.is_set or
                    self.source_interface.is_set or
                    self.tls_trustpoint.is_set or
                    self.trans_max.is_set or
                    self.trans_total.is_set or
                    self.transaction_timer.is_set or
                    self.watchdog_timer.is_set)

            def has_operation(self):
                for c in self.peer:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.conn_retry_timer.yfilter != YFilter.not_set or
                    self.origin_host.yfilter != YFilter.not_set or
                    self.origin_realm.yfilter != YFilter.not_set or
                    self.source_interface.yfilter != YFilter.not_set or
                    self.tls_trustpoint.yfilter != YFilter.not_set or
                    self.trans_max.yfilter != YFilter.not_set or
                    self.trans_total.yfilter != YFilter.not_set or
                    self.transaction_timer.yfilter != YFilter.not_set or
                    self.watchdog_timer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "peers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.conn_retry_timer.is_set or self.conn_retry_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.conn_retry_timer.get_name_leafdata())
                if (self.origin_host.is_set or self.origin_host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.origin_host.get_name_leafdata())
                if (self.origin_realm.is_set or self.origin_realm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.origin_realm.get_name_leafdata())
                if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.source_interface.get_name_leafdata())
                if (self.tls_trustpoint.is_set or self.tls_trustpoint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.tls_trustpoint.get_name_leafdata())
                if (self.trans_max.is_set or self.trans_max.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trans_max.get_name_leafdata())
                if (self.trans_total.is_set or self.trans_total.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trans_total.get_name_leafdata())
                if (self.transaction_timer.is_set or self.transaction_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.transaction_timer.get_name_leafdata())
                if (self.watchdog_timer.is_set or self.watchdog_timer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.watchdog_timer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "peer"):
                    for c in self.peer:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Diameter.Peers.Peer()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.peer.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "peer" or name == "conn-retry-timer" or name == "origin-host" or name == "origin-realm" or name == "source-interface" or name == "tls-trustpoint" or name == "trans-max" or name == "trans-total" or name == "transaction-timer" or name == "watchdog-timer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "conn-retry-timer"):
                    self.conn_retry_timer = value
                    self.conn_retry_timer.value_namespace = name_space
                    self.conn_retry_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "origin-host"):
                    self.origin_host = value
                    self.origin_host.value_namespace = name_space
                    self.origin_host.value_namespace_prefix = name_space_prefix
                if(value_path == "origin-realm"):
                    self.origin_realm = value
                    self.origin_realm.value_namespace = name_space
                    self.origin_realm.value_namespace_prefix = name_space_prefix
                if(value_path == "source-interface"):
                    self.source_interface = value
                    self.source_interface.value_namespace = name_space
                    self.source_interface.value_namespace_prefix = name_space_prefix
                if(value_path == "tls-trustpoint"):
                    self.tls_trustpoint = value
                    self.tls_trustpoint.value_namespace = name_space
                    self.tls_trustpoint.value_namespace_prefix = name_space_prefix
                if(value_path == "trans-max"):
                    self.trans_max = value
                    self.trans_max.value_namespace = name_space
                    self.trans_max.value_namespace_prefix = name_space_prefix
                if(value_path == "trans-total"):
                    self.trans_total = value
                    self.trans_total.value_namespace = name_space
                    self.trans_total.value_namespace_prefix = name_space_prefix
                if(value_path == "transaction-timer"):
                    self.transaction_timer = value
                    self.transaction_timer.value_namespace = name_space
                    self.transaction_timer.value_namespace_prefix = name_space_prefix
                if(value_path == "watchdog-timer"):
                    self.watchdog_timer = value
                    self.watchdog_timer.value_namespace = name_space
                    self.watchdog_timer.value_namespace_prefix = name_space_prefix


        class Nas(Entity):
            """
            Diameter NAS data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\:  str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of    :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.Nas, self).__init__()

                self.yang_name = "nas"
                self.yang_parent_name = "diameter"

                self.aaanas_id = YLeaf(YType.str, "aaanas-id")

                self.list_of_nas = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("aaanas_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.Nas, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.Nas, self).__setattr__(name, value)


            class ListOfNas(Entity):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  str
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\:  str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.Nas.ListOfNas, self).__init__()

                    self.yang_name = "list-of-nas"
                    self.yang_parent_name = "nas"

                    self.aaa_session_id = YLeaf(YType.str, "aaa-session-id")

                    self.accounting_intrim_in_packets = YLeaf(YType.uint32, "accounting-intrim-in-packets")

                    self.accounting_intrim_out_packets = YLeaf(YType.uint32, "accounting-intrim-out-packets")

                    self.accounting_status = YLeaf(YType.uint32, "accounting-status")

                    self.accounting_status_stop = YLeaf(YType.uint32, "accounting-status-stop")

                    self.authentication_status = YLeaf(YType.uint32, "authentication-status")

                    self.authorization_status = YLeaf(YType.uint32, "authorization-status")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.disconnect_status = YLeaf(YType.uint32, "disconnect-status")

                    self.method_list = YLeaf(YType.str, "method-list")

                    self.server_used_list = YLeaf(YType.str, "server-used-list")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("aaa_session_id",
                                    "accounting_intrim_in_packets",
                                    "accounting_intrim_out_packets",
                                    "accounting_status",
                                    "accounting_status_stop",
                                    "authentication_status",
                                    "authorization_status",
                                    "diameter_session_id",
                                    "disconnect_status",
                                    "method_list",
                                    "server_used_list") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.Nas.ListOfNas, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.Nas.ListOfNas, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.aaa_session_id.is_set or
                        self.accounting_intrim_in_packets.is_set or
                        self.accounting_intrim_out_packets.is_set or
                        self.accounting_status.is_set or
                        self.accounting_status_stop.is_set or
                        self.authentication_status.is_set or
                        self.authorization_status.is_set or
                        self.diameter_session_id.is_set or
                        self.disconnect_status.is_set or
                        self.method_list.is_set or
                        self.server_used_list.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.aaa_session_id.yfilter != YFilter.not_set or
                        self.accounting_intrim_in_packets.yfilter != YFilter.not_set or
                        self.accounting_intrim_out_packets.yfilter != YFilter.not_set or
                        self.accounting_status.yfilter != YFilter.not_set or
                        self.accounting_status_stop.yfilter != YFilter.not_set or
                        self.authentication_status.yfilter != YFilter.not_set or
                        self.authorization_status.yfilter != YFilter.not_set or
                        self.diameter_session_id.yfilter != YFilter.not_set or
                        self.disconnect_status.yfilter != YFilter.not_set or
                        self.method_list.yfilter != YFilter.not_set or
                        self.server_used_list.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "list-of-nas" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/nas/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.aaa_session_id.is_set or self.aaa_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aaa_session_id.get_name_leafdata())
                    if (self.accounting_intrim_in_packets.is_set or self.accounting_intrim_in_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_intrim_in_packets.get_name_leafdata())
                    if (self.accounting_intrim_out_packets.is_set or self.accounting_intrim_out_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_intrim_out_packets.get_name_leafdata())
                    if (self.accounting_status.is_set or self.accounting_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_status.get_name_leafdata())
                    if (self.accounting_status_stop.is_set or self.accounting_status_stop.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_status_stop.get_name_leafdata())
                    if (self.authentication_status.is_set or self.authentication_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_status.get_name_leafdata())
                    if (self.authorization_status.is_set or self.authorization_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authorization_status.get_name_leafdata())
                    if (self.diameter_session_id.is_set or self.diameter_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.diameter_session_id.get_name_leafdata())
                    if (self.disconnect_status.is_set or self.disconnect_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disconnect_status.get_name_leafdata())
                    if (self.method_list.is_set or self.method_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.method_list.get_name_leafdata())
                    if (self.server_used_list.is_set or self.server_used_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.server_used_list.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aaa-session-id" or name == "accounting-intrim-in-packets" or name == "accounting-intrim-out-packets" or name == "accounting-status" or name == "accounting-status-stop" or name == "authentication-status" or name == "authorization-status" or name == "diameter-session-id" or name == "disconnect-status" or name == "method-list" or name == "server-used-list"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "aaa-session-id"):
                        self.aaa_session_id = value
                        self.aaa_session_id.value_namespace = name_space
                        self.aaa_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-intrim-in-packets"):
                        self.accounting_intrim_in_packets = value
                        self.accounting_intrim_in_packets.value_namespace = name_space
                        self.accounting_intrim_in_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-intrim-out-packets"):
                        self.accounting_intrim_out_packets = value
                        self.accounting_intrim_out_packets.value_namespace = name_space
                        self.accounting_intrim_out_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-status"):
                        self.accounting_status = value
                        self.accounting_status.value_namespace = name_space
                        self.accounting_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-status-stop"):
                        self.accounting_status_stop = value
                        self.accounting_status_stop.value_namespace = name_space
                        self.accounting_status_stop.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-status"):
                        self.authentication_status = value
                        self.authentication_status.value_namespace = name_space
                        self.authentication_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "authorization-status"):
                        self.authorization_status = value
                        self.authorization_status.value_namespace = name_space
                        self.authorization_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "diameter-session-id"):
                        self.diameter_session_id = value
                        self.diameter_session_id.value_namespace = name_space
                        self.diameter_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "disconnect-status"):
                        self.disconnect_status = value
                        self.disconnect_status.value_namespace = name_space
                        self.disconnect_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "method-list"):
                        self.method_list = value
                        self.method_list.value_namespace = name_space
                        self.method_list.value_namespace_prefix = name_space_prefix
                    if(value_path == "server-used-list"):
                        self.server_used_list = value
                        self.server_used_list.value_namespace = name_space
                        self.server_used_list.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.list_of_nas:
                    if (c.has_data()):
                        return True
                return self.aaanas_id.is_set

            def has_operation(self):
                for c in self.list_of_nas:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.aaanas_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nas" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.aaanas_id.is_set or self.aaanas_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aaanas_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "list-of-nas"):
                    for c in self.list_of_nas:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Diameter.Nas.ListOfNas()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.list_of_nas.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "list-of-nas" or name == "aaanas-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "aaanas-id"):
                    self.aaanas_id = value
                    self.aaanas_id.value_namespace = name_space
                    self.aaanas_id.value_namespace_prefix = name_space_prefix


        class NasSummary(Entity):
            """
            Diameter NAS summary
            
            .. attribute:: accounting_interim_failed_packets
            
            	Accounting interim response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_in_packets
            
            	Accounting Interim request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_out_packets
            
            	Accounting interim requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_response_out_packets
            
            	Accounting interim response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_success_packets
            
            	Accounting interim response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_intrim_response_in_packets
            
            	Accounting interim packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_request_out_packets
            
            	Accounting requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_response_in_packets
            
            	Accounting packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_failed_packets
            
            	Accounting start response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_request_packets
            
            	Accounting start request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_response_packets
            
            	Accounting start response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_success_packets
            
            	Accounting start response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_failed_packets
            
            	Accounting stop response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_in_packets
            
            	Acct stop request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_out_packets
            
            	Accounting stop requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_in_packets
            
            	Accounting stop packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_out_packets
            
            	Acct stop response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_success_response_packets
            
            	Accounting stop response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_in_packets
            
            	Authentication request from client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_out_packets
            
            	Authentication request pkt out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_fail_packets
            
            	Authentication response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_in_packets
            
            	Authentication response pkt in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_out_packets
            
            	Authentication response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_success_packets
            
            	Authentication response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_in_packets
            
            	Authorization response packet in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_out_packets
            
            	Authorization request packet out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_request_in_packets
            
            	Authourization request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_fail_packets
            
            	Authentication response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_out_packets
            
            	Authourization response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_success_packets
            
            	Authentication response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_failed_packets
            
            	COA response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_in_packets
            
            	COA/RAR Request packet in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_packets
            
            	COA request from client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_out_packets
            
            	COA/RAR Response packet out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_packets
            
            	COA response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_success_packets
            
            	COA response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_failed_response_packets
            
            	Disconnect response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_in_packets
            
            	Disconnect request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_out_packets
            
            	Disconnect request pkt out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_in_packets
            
            	Disconnect response packets in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_out_packets
            
            	Disconnect response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_success_response_packets
            
            	Disconnect response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_failed_packets
            
            	POD response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_in_packets
            
            	POD/RAR Request packets in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_out_packets
            
            	PAD/RAR Response packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_request_in_packets
            
            	POD request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_response_out_packets
            
            	POD response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_success_packets
            
            	POD response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.NasSummary, self).__init__()

                self.yang_name = "nas-summary"
                self.yang_parent_name = "diameter"

                self.accounting_interim_failed_packets = YLeaf(YType.uint32, "accounting-interim-failed-packets")

                self.accounting_interim_request_in_packets = YLeaf(YType.uint32, "accounting-interim-request-in-packets")

                self.accounting_interim_request_out_packets = YLeaf(YType.uint32, "accounting-interim-request-out-packets")

                self.accounting_interim_response_out_packets = YLeaf(YType.uint32, "accounting-interim-response-out-packets")

                self.accounting_interim_success_packets = YLeaf(YType.uint32, "accounting-interim-success-packets")

                self.accounting_intrim_response_in_packets = YLeaf(YType.uint32, "accounting-intrim-response-in-packets")

                self.accounting_request_out_packets = YLeaf(YType.uint32, "accounting-request-out-packets")

                self.accounting_response_in_packets = YLeaf(YType.uint32, "accounting-response-in-packets")

                self.accounting_start_failed_packets = YLeaf(YType.uint32, "accounting-start-failed-packets")

                self.accounting_start_request_packets = YLeaf(YType.uint32, "accounting-start-request-packets")

                self.accounting_start_response_packets = YLeaf(YType.uint32, "accounting-start-response-packets")

                self.accounting_start_success_packets = YLeaf(YType.uint32, "accounting-start-success-packets")

                self.accounting_stop_failed_packets = YLeaf(YType.uint32, "accounting-stop-failed-packets")

                self.accounting_stop_request_in_packets = YLeaf(YType.uint32, "accounting-stop-request-in-packets")

                self.accounting_stop_request_out_packets = YLeaf(YType.uint32, "accounting-stop-request-out-packets")

                self.accounting_stop_response_in_packets = YLeaf(YType.uint32, "accounting-stop-response-in-packets")

                self.accounting_stop_response_out_packets = YLeaf(YType.uint32, "accounting-stop-response-out-packets")

                self.accounting_stop_success_response_packets = YLeaf(YType.uint32, "accounting-stop-success-response-packets")

                self.authen_request_in_packets = YLeaf(YType.uint32, "authen-request-in-packets")

                self.authen_request_out_packets = YLeaf(YType.uint32, "authen-request-out-packets")

                self.authen_response_fail_packets = YLeaf(YType.uint32, "authen-response-fail-packets")

                self.authen_response_in_packets = YLeaf(YType.uint32, "authen-response-in-packets")

                self.authen_response_out_packets = YLeaf(YType.uint32, "authen-response-out-packets")

                self.authen_success_packets = YLeaf(YType.uint32, "authen-success-packets")

                self.authorization_in_packets = YLeaf(YType.uint32, "authorization-in-packets")

                self.authorization_out_packets = YLeaf(YType.uint32, "authorization-out-packets")

                self.authorization_request_in_packets = YLeaf(YType.uint32, "authorization-request-in-packets")

                self.authorization_response_fail_packets = YLeaf(YType.uint32, "authorization-response-fail-packets")

                self.authorization_response_out_packets = YLeaf(YType.uint32, "authorization-response-out-packets")

                self.authorization_response_success_packets = YLeaf(YType.uint32, "authorization-response-success-packets")

                self.coa_failed_packets = YLeaf(YType.uint32, "coa-failed-packets")

                self.coa_request_in_packets = YLeaf(YType.uint32, "coa-request-in-packets")

                self.coa_request_packets = YLeaf(YType.uint32, "coa-request-packets")

                self.coa_response_out_packets = YLeaf(YType.uint32, "coa-response-out-packets")

                self.coa_response_packets = YLeaf(YType.uint32, "coa-response-packets")

                self.coa_success_packets = YLeaf(YType.uint32, "coa-success-packets")

                self.disconnect_failed_response_packets = YLeaf(YType.uint32, "disconnect-failed-response-packets")

                self.disconnect_request_in_packets = YLeaf(YType.uint32, "disconnect-request-in-packets")

                self.disconnect_request_out_packets = YLeaf(YType.uint32, "disconnect-request-out-packets")

                self.disconnect_response_in_packets = YLeaf(YType.uint32, "disconnect-response-in-packets")

                self.disconnect_response_out_packets = YLeaf(YType.uint32, "disconnect-response-out-packets")

                self.disconnect_success_response_packets = YLeaf(YType.uint32, "disconnect-success-response-packets")

                self.pod_failed_packets = YLeaf(YType.uint32, "pod-failed-packets")

                self.pod_in_packets = YLeaf(YType.uint32, "pod-in-packets")

                self.pod_out_packets = YLeaf(YType.uint32, "pod-out-packets")

                self.pod_request_in_packets = YLeaf(YType.uint32, "pod-request-in-packets")

                self.pod_response_out_packets = YLeaf(YType.uint32, "pod-response-out-packets")

                self.pod_success_packets = YLeaf(YType.uint32, "pod-success-packets")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("accounting_interim_failed_packets",
                                "accounting_interim_request_in_packets",
                                "accounting_interim_request_out_packets",
                                "accounting_interim_response_out_packets",
                                "accounting_interim_success_packets",
                                "accounting_intrim_response_in_packets",
                                "accounting_request_out_packets",
                                "accounting_response_in_packets",
                                "accounting_start_failed_packets",
                                "accounting_start_request_packets",
                                "accounting_start_response_packets",
                                "accounting_start_success_packets",
                                "accounting_stop_failed_packets",
                                "accounting_stop_request_in_packets",
                                "accounting_stop_request_out_packets",
                                "accounting_stop_response_in_packets",
                                "accounting_stop_response_out_packets",
                                "accounting_stop_success_response_packets",
                                "authen_request_in_packets",
                                "authen_request_out_packets",
                                "authen_response_fail_packets",
                                "authen_response_in_packets",
                                "authen_response_out_packets",
                                "authen_success_packets",
                                "authorization_in_packets",
                                "authorization_out_packets",
                                "authorization_request_in_packets",
                                "authorization_response_fail_packets",
                                "authorization_response_out_packets",
                                "authorization_response_success_packets",
                                "coa_failed_packets",
                                "coa_request_in_packets",
                                "coa_request_packets",
                                "coa_response_out_packets",
                                "coa_response_packets",
                                "coa_success_packets",
                                "disconnect_failed_response_packets",
                                "disconnect_request_in_packets",
                                "disconnect_request_out_packets",
                                "disconnect_response_in_packets",
                                "disconnect_response_out_packets",
                                "disconnect_success_response_packets",
                                "pod_failed_packets",
                                "pod_in_packets",
                                "pod_out_packets",
                                "pod_request_in_packets",
                                "pod_response_out_packets",
                                "pod_success_packets") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.NasSummary, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.NasSummary, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.accounting_interim_failed_packets.is_set or
                    self.accounting_interim_request_in_packets.is_set or
                    self.accounting_interim_request_out_packets.is_set or
                    self.accounting_interim_response_out_packets.is_set or
                    self.accounting_interim_success_packets.is_set or
                    self.accounting_intrim_response_in_packets.is_set or
                    self.accounting_request_out_packets.is_set or
                    self.accounting_response_in_packets.is_set or
                    self.accounting_start_failed_packets.is_set or
                    self.accounting_start_request_packets.is_set or
                    self.accounting_start_response_packets.is_set or
                    self.accounting_start_success_packets.is_set or
                    self.accounting_stop_failed_packets.is_set or
                    self.accounting_stop_request_in_packets.is_set or
                    self.accounting_stop_request_out_packets.is_set or
                    self.accounting_stop_response_in_packets.is_set or
                    self.accounting_stop_response_out_packets.is_set or
                    self.accounting_stop_success_response_packets.is_set or
                    self.authen_request_in_packets.is_set or
                    self.authen_request_out_packets.is_set or
                    self.authen_response_fail_packets.is_set or
                    self.authen_response_in_packets.is_set or
                    self.authen_response_out_packets.is_set or
                    self.authen_success_packets.is_set or
                    self.authorization_in_packets.is_set or
                    self.authorization_out_packets.is_set or
                    self.authorization_request_in_packets.is_set or
                    self.authorization_response_fail_packets.is_set or
                    self.authorization_response_out_packets.is_set or
                    self.authorization_response_success_packets.is_set or
                    self.coa_failed_packets.is_set or
                    self.coa_request_in_packets.is_set or
                    self.coa_request_packets.is_set or
                    self.coa_response_out_packets.is_set or
                    self.coa_response_packets.is_set or
                    self.coa_success_packets.is_set or
                    self.disconnect_failed_response_packets.is_set or
                    self.disconnect_request_in_packets.is_set or
                    self.disconnect_request_out_packets.is_set or
                    self.disconnect_response_in_packets.is_set or
                    self.disconnect_response_out_packets.is_set or
                    self.disconnect_success_response_packets.is_set or
                    self.pod_failed_packets.is_set or
                    self.pod_in_packets.is_set or
                    self.pod_out_packets.is_set or
                    self.pod_request_in_packets.is_set or
                    self.pod_response_out_packets.is_set or
                    self.pod_success_packets.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.accounting_interim_failed_packets.yfilter != YFilter.not_set or
                    self.accounting_interim_request_in_packets.yfilter != YFilter.not_set or
                    self.accounting_interim_request_out_packets.yfilter != YFilter.not_set or
                    self.accounting_interim_response_out_packets.yfilter != YFilter.not_set or
                    self.accounting_interim_success_packets.yfilter != YFilter.not_set or
                    self.accounting_intrim_response_in_packets.yfilter != YFilter.not_set or
                    self.accounting_request_out_packets.yfilter != YFilter.not_set or
                    self.accounting_response_in_packets.yfilter != YFilter.not_set or
                    self.accounting_start_failed_packets.yfilter != YFilter.not_set or
                    self.accounting_start_request_packets.yfilter != YFilter.not_set or
                    self.accounting_start_response_packets.yfilter != YFilter.not_set or
                    self.accounting_start_success_packets.yfilter != YFilter.not_set or
                    self.accounting_stop_failed_packets.yfilter != YFilter.not_set or
                    self.accounting_stop_request_in_packets.yfilter != YFilter.not_set or
                    self.accounting_stop_request_out_packets.yfilter != YFilter.not_set or
                    self.accounting_stop_response_in_packets.yfilter != YFilter.not_set or
                    self.accounting_stop_response_out_packets.yfilter != YFilter.not_set or
                    self.accounting_stop_success_response_packets.yfilter != YFilter.not_set or
                    self.authen_request_in_packets.yfilter != YFilter.not_set or
                    self.authen_request_out_packets.yfilter != YFilter.not_set or
                    self.authen_response_fail_packets.yfilter != YFilter.not_set or
                    self.authen_response_in_packets.yfilter != YFilter.not_set or
                    self.authen_response_out_packets.yfilter != YFilter.not_set or
                    self.authen_success_packets.yfilter != YFilter.not_set or
                    self.authorization_in_packets.yfilter != YFilter.not_set or
                    self.authorization_out_packets.yfilter != YFilter.not_set or
                    self.authorization_request_in_packets.yfilter != YFilter.not_set or
                    self.authorization_response_fail_packets.yfilter != YFilter.not_set or
                    self.authorization_response_out_packets.yfilter != YFilter.not_set or
                    self.authorization_response_success_packets.yfilter != YFilter.not_set or
                    self.coa_failed_packets.yfilter != YFilter.not_set or
                    self.coa_request_in_packets.yfilter != YFilter.not_set or
                    self.coa_request_packets.yfilter != YFilter.not_set or
                    self.coa_response_out_packets.yfilter != YFilter.not_set or
                    self.coa_response_packets.yfilter != YFilter.not_set or
                    self.coa_success_packets.yfilter != YFilter.not_set or
                    self.disconnect_failed_response_packets.yfilter != YFilter.not_set or
                    self.disconnect_request_in_packets.yfilter != YFilter.not_set or
                    self.disconnect_request_out_packets.yfilter != YFilter.not_set or
                    self.disconnect_response_in_packets.yfilter != YFilter.not_set or
                    self.disconnect_response_out_packets.yfilter != YFilter.not_set or
                    self.disconnect_success_response_packets.yfilter != YFilter.not_set or
                    self.pod_failed_packets.yfilter != YFilter.not_set or
                    self.pod_in_packets.yfilter != YFilter.not_set or
                    self.pod_out_packets.yfilter != YFilter.not_set or
                    self.pod_request_in_packets.yfilter != YFilter.not_set or
                    self.pod_response_out_packets.yfilter != YFilter.not_set or
                    self.pod_success_packets.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nas-summary" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.accounting_interim_failed_packets.is_set or self.accounting_interim_failed_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_interim_failed_packets.get_name_leafdata())
                if (self.accounting_interim_request_in_packets.is_set or self.accounting_interim_request_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_interim_request_in_packets.get_name_leafdata())
                if (self.accounting_interim_request_out_packets.is_set or self.accounting_interim_request_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_interim_request_out_packets.get_name_leafdata())
                if (self.accounting_interim_response_out_packets.is_set or self.accounting_interim_response_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_interim_response_out_packets.get_name_leafdata())
                if (self.accounting_interim_success_packets.is_set or self.accounting_interim_success_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_interim_success_packets.get_name_leafdata())
                if (self.accounting_intrim_response_in_packets.is_set or self.accounting_intrim_response_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_intrim_response_in_packets.get_name_leafdata())
                if (self.accounting_request_out_packets.is_set or self.accounting_request_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_request_out_packets.get_name_leafdata())
                if (self.accounting_response_in_packets.is_set or self.accounting_response_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_response_in_packets.get_name_leafdata())
                if (self.accounting_start_failed_packets.is_set or self.accounting_start_failed_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_start_failed_packets.get_name_leafdata())
                if (self.accounting_start_request_packets.is_set or self.accounting_start_request_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_start_request_packets.get_name_leafdata())
                if (self.accounting_start_response_packets.is_set or self.accounting_start_response_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_start_response_packets.get_name_leafdata())
                if (self.accounting_start_success_packets.is_set or self.accounting_start_success_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_start_success_packets.get_name_leafdata())
                if (self.accounting_stop_failed_packets.is_set or self.accounting_stop_failed_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_stop_failed_packets.get_name_leafdata())
                if (self.accounting_stop_request_in_packets.is_set or self.accounting_stop_request_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_stop_request_in_packets.get_name_leafdata())
                if (self.accounting_stop_request_out_packets.is_set or self.accounting_stop_request_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_stop_request_out_packets.get_name_leafdata())
                if (self.accounting_stop_response_in_packets.is_set or self.accounting_stop_response_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_stop_response_in_packets.get_name_leafdata())
                if (self.accounting_stop_response_out_packets.is_set or self.accounting_stop_response_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_stop_response_out_packets.get_name_leafdata())
                if (self.accounting_stop_success_response_packets.is_set or self.accounting_stop_success_response_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_stop_success_response_packets.get_name_leafdata())
                if (self.authen_request_in_packets.is_set or self.authen_request_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authen_request_in_packets.get_name_leafdata())
                if (self.authen_request_out_packets.is_set or self.authen_request_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authen_request_out_packets.get_name_leafdata())
                if (self.authen_response_fail_packets.is_set or self.authen_response_fail_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authen_response_fail_packets.get_name_leafdata())
                if (self.authen_response_in_packets.is_set or self.authen_response_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authen_response_in_packets.get_name_leafdata())
                if (self.authen_response_out_packets.is_set or self.authen_response_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authen_response_out_packets.get_name_leafdata())
                if (self.authen_success_packets.is_set or self.authen_success_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authen_success_packets.get_name_leafdata())
                if (self.authorization_in_packets.is_set or self.authorization_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authorization_in_packets.get_name_leafdata())
                if (self.authorization_out_packets.is_set or self.authorization_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authorization_out_packets.get_name_leafdata())
                if (self.authorization_request_in_packets.is_set or self.authorization_request_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authorization_request_in_packets.get_name_leafdata())
                if (self.authorization_response_fail_packets.is_set or self.authorization_response_fail_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authorization_response_fail_packets.get_name_leafdata())
                if (self.authorization_response_out_packets.is_set or self.authorization_response_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authorization_response_out_packets.get_name_leafdata())
                if (self.authorization_response_success_packets.is_set or self.authorization_response_success_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authorization_response_success_packets.get_name_leafdata())
                if (self.coa_failed_packets.is_set or self.coa_failed_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.coa_failed_packets.get_name_leafdata())
                if (self.coa_request_in_packets.is_set or self.coa_request_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.coa_request_in_packets.get_name_leafdata())
                if (self.coa_request_packets.is_set or self.coa_request_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.coa_request_packets.get_name_leafdata())
                if (self.coa_response_out_packets.is_set or self.coa_response_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.coa_response_out_packets.get_name_leafdata())
                if (self.coa_response_packets.is_set or self.coa_response_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.coa_response_packets.get_name_leafdata())
                if (self.coa_success_packets.is_set or self.coa_success_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.coa_success_packets.get_name_leafdata())
                if (self.disconnect_failed_response_packets.is_set or self.disconnect_failed_response_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disconnect_failed_response_packets.get_name_leafdata())
                if (self.disconnect_request_in_packets.is_set or self.disconnect_request_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disconnect_request_in_packets.get_name_leafdata())
                if (self.disconnect_request_out_packets.is_set or self.disconnect_request_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disconnect_request_out_packets.get_name_leafdata())
                if (self.disconnect_response_in_packets.is_set or self.disconnect_response_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disconnect_response_in_packets.get_name_leafdata())
                if (self.disconnect_response_out_packets.is_set or self.disconnect_response_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disconnect_response_out_packets.get_name_leafdata())
                if (self.disconnect_success_response_packets.is_set or self.disconnect_success_response_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disconnect_success_response_packets.get_name_leafdata())
                if (self.pod_failed_packets.is_set or self.pod_failed_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pod_failed_packets.get_name_leafdata())
                if (self.pod_in_packets.is_set or self.pod_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pod_in_packets.get_name_leafdata())
                if (self.pod_out_packets.is_set or self.pod_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pod_out_packets.get_name_leafdata())
                if (self.pod_request_in_packets.is_set or self.pod_request_in_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pod_request_in_packets.get_name_leafdata())
                if (self.pod_response_out_packets.is_set or self.pod_response_out_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pod_response_out_packets.get_name_leafdata())
                if (self.pod_success_packets.is_set or self.pod_success_packets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pod_success_packets.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accounting-interim-failed-packets" or name == "accounting-interim-request-in-packets" or name == "accounting-interim-request-out-packets" or name == "accounting-interim-response-out-packets" or name == "accounting-interim-success-packets" or name == "accounting-intrim-response-in-packets" or name == "accounting-request-out-packets" or name == "accounting-response-in-packets" or name == "accounting-start-failed-packets" or name == "accounting-start-request-packets" or name == "accounting-start-response-packets" or name == "accounting-start-success-packets" or name == "accounting-stop-failed-packets" or name == "accounting-stop-request-in-packets" or name == "accounting-stop-request-out-packets" or name == "accounting-stop-response-in-packets" or name == "accounting-stop-response-out-packets" or name == "accounting-stop-success-response-packets" or name == "authen-request-in-packets" or name == "authen-request-out-packets" or name == "authen-response-fail-packets" or name == "authen-response-in-packets" or name == "authen-response-out-packets" or name == "authen-success-packets" or name == "authorization-in-packets" or name == "authorization-out-packets" or name == "authorization-request-in-packets" or name == "authorization-response-fail-packets" or name == "authorization-response-out-packets" or name == "authorization-response-success-packets" or name == "coa-failed-packets" or name == "coa-request-in-packets" or name == "coa-request-packets" or name == "coa-response-out-packets" or name == "coa-response-packets" or name == "coa-success-packets" or name == "disconnect-failed-response-packets" or name == "disconnect-request-in-packets" or name == "disconnect-request-out-packets" or name == "disconnect-response-in-packets" or name == "disconnect-response-out-packets" or name == "disconnect-success-response-packets" or name == "pod-failed-packets" or name == "pod-in-packets" or name == "pod-out-packets" or name == "pod-request-in-packets" or name == "pod-response-out-packets" or name == "pod-success-packets"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "accounting-interim-failed-packets"):
                    self.accounting_interim_failed_packets = value
                    self.accounting_interim_failed_packets.value_namespace = name_space
                    self.accounting_interim_failed_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-interim-request-in-packets"):
                    self.accounting_interim_request_in_packets = value
                    self.accounting_interim_request_in_packets.value_namespace = name_space
                    self.accounting_interim_request_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-interim-request-out-packets"):
                    self.accounting_interim_request_out_packets = value
                    self.accounting_interim_request_out_packets.value_namespace = name_space
                    self.accounting_interim_request_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-interim-response-out-packets"):
                    self.accounting_interim_response_out_packets = value
                    self.accounting_interim_response_out_packets.value_namespace = name_space
                    self.accounting_interim_response_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-interim-success-packets"):
                    self.accounting_interim_success_packets = value
                    self.accounting_interim_success_packets.value_namespace = name_space
                    self.accounting_interim_success_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-intrim-response-in-packets"):
                    self.accounting_intrim_response_in_packets = value
                    self.accounting_intrim_response_in_packets.value_namespace = name_space
                    self.accounting_intrim_response_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-request-out-packets"):
                    self.accounting_request_out_packets = value
                    self.accounting_request_out_packets.value_namespace = name_space
                    self.accounting_request_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-response-in-packets"):
                    self.accounting_response_in_packets = value
                    self.accounting_response_in_packets.value_namespace = name_space
                    self.accounting_response_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-start-failed-packets"):
                    self.accounting_start_failed_packets = value
                    self.accounting_start_failed_packets.value_namespace = name_space
                    self.accounting_start_failed_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-start-request-packets"):
                    self.accounting_start_request_packets = value
                    self.accounting_start_request_packets.value_namespace = name_space
                    self.accounting_start_request_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-start-response-packets"):
                    self.accounting_start_response_packets = value
                    self.accounting_start_response_packets.value_namespace = name_space
                    self.accounting_start_response_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-start-success-packets"):
                    self.accounting_start_success_packets = value
                    self.accounting_start_success_packets.value_namespace = name_space
                    self.accounting_start_success_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-stop-failed-packets"):
                    self.accounting_stop_failed_packets = value
                    self.accounting_stop_failed_packets.value_namespace = name_space
                    self.accounting_stop_failed_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-stop-request-in-packets"):
                    self.accounting_stop_request_in_packets = value
                    self.accounting_stop_request_in_packets.value_namespace = name_space
                    self.accounting_stop_request_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-stop-request-out-packets"):
                    self.accounting_stop_request_out_packets = value
                    self.accounting_stop_request_out_packets.value_namespace = name_space
                    self.accounting_stop_request_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-stop-response-in-packets"):
                    self.accounting_stop_response_in_packets = value
                    self.accounting_stop_response_in_packets.value_namespace = name_space
                    self.accounting_stop_response_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-stop-response-out-packets"):
                    self.accounting_stop_response_out_packets = value
                    self.accounting_stop_response_out_packets.value_namespace = name_space
                    self.accounting_stop_response_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "accounting-stop-success-response-packets"):
                    self.accounting_stop_success_response_packets = value
                    self.accounting_stop_success_response_packets.value_namespace = name_space
                    self.accounting_stop_success_response_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authen-request-in-packets"):
                    self.authen_request_in_packets = value
                    self.authen_request_in_packets.value_namespace = name_space
                    self.authen_request_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authen-request-out-packets"):
                    self.authen_request_out_packets = value
                    self.authen_request_out_packets.value_namespace = name_space
                    self.authen_request_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authen-response-fail-packets"):
                    self.authen_response_fail_packets = value
                    self.authen_response_fail_packets.value_namespace = name_space
                    self.authen_response_fail_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authen-response-in-packets"):
                    self.authen_response_in_packets = value
                    self.authen_response_in_packets.value_namespace = name_space
                    self.authen_response_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authen-response-out-packets"):
                    self.authen_response_out_packets = value
                    self.authen_response_out_packets.value_namespace = name_space
                    self.authen_response_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authen-success-packets"):
                    self.authen_success_packets = value
                    self.authen_success_packets.value_namespace = name_space
                    self.authen_success_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authorization-in-packets"):
                    self.authorization_in_packets = value
                    self.authorization_in_packets.value_namespace = name_space
                    self.authorization_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authorization-out-packets"):
                    self.authorization_out_packets = value
                    self.authorization_out_packets.value_namespace = name_space
                    self.authorization_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authorization-request-in-packets"):
                    self.authorization_request_in_packets = value
                    self.authorization_request_in_packets.value_namespace = name_space
                    self.authorization_request_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authorization-response-fail-packets"):
                    self.authorization_response_fail_packets = value
                    self.authorization_response_fail_packets.value_namespace = name_space
                    self.authorization_response_fail_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authorization-response-out-packets"):
                    self.authorization_response_out_packets = value
                    self.authorization_response_out_packets.value_namespace = name_space
                    self.authorization_response_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "authorization-response-success-packets"):
                    self.authorization_response_success_packets = value
                    self.authorization_response_success_packets.value_namespace = name_space
                    self.authorization_response_success_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "coa-failed-packets"):
                    self.coa_failed_packets = value
                    self.coa_failed_packets.value_namespace = name_space
                    self.coa_failed_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "coa-request-in-packets"):
                    self.coa_request_in_packets = value
                    self.coa_request_in_packets.value_namespace = name_space
                    self.coa_request_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "coa-request-packets"):
                    self.coa_request_packets = value
                    self.coa_request_packets.value_namespace = name_space
                    self.coa_request_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "coa-response-out-packets"):
                    self.coa_response_out_packets = value
                    self.coa_response_out_packets.value_namespace = name_space
                    self.coa_response_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "coa-response-packets"):
                    self.coa_response_packets = value
                    self.coa_response_packets.value_namespace = name_space
                    self.coa_response_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "coa-success-packets"):
                    self.coa_success_packets = value
                    self.coa_success_packets.value_namespace = name_space
                    self.coa_success_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "disconnect-failed-response-packets"):
                    self.disconnect_failed_response_packets = value
                    self.disconnect_failed_response_packets.value_namespace = name_space
                    self.disconnect_failed_response_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "disconnect-request-in-packets"):
                    self.disconnect_request_in_packets = value
                    self.disconnect_request_in_packets.value_namespace = name_space
                    self.disconnect_request_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "disconnect-request-out-packets"):
                    self.disconnect_request_out_packets = value
                    self.disconnect_request_out_packets.value_namespace = name_space
                    self.disconnect_request_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "disconnect-response-in-packets"):
                    self.disconnect_response_in_packets = value
                    self.disconnect_response_in_packets.value_namespace = name_space
                    self.disconnect_response_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "disconnect-response-out-packets"):
                    self.disconnect_response_out_packets = value
                    self.disconnect_response_out_packets.value_namespace = name_space
                    self.disconnect_response_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "disconnect-success-response-packets"):
                    self.disconnect_success_response_packets = value
                    self.disconnect_success_response_packets.value_namespace = name_space
                    self.disconnect_success_response_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "pod-failed-packets"):
                    self.pod_failed_packets = value
                    self.pod_failed_packets.value_namespace = name_space
                    self.pod_failed_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "pod-in-packets"):
                    self.pod_in_packets = value
                    self.pod_in_packets.value_namespace = name_space
                    self.pod_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "pod-out-packets"):
                    self.pod_out_packets = value
                    self.pod_out_packets.value_namespace = name_space
                    self.pod_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "pod-request-in-packets"):
                    self.pod_request_in_packets = value
                    self.pod_request_in_packets.value_namespace = name_space
                    self.pod_request_in_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "pod-response-out-packets"):
                    self.pod_response_out_packets = value
                    self.pod_response_out_packets.value_namespace = name_space
                    self.pod_response_out_packets.value_namespace_prefix = name_space_prefix
                if(value_path == "pod-success-packets"):
                    self.pod_success_packets = value
                    self.pod_success_packets.value_namespace = name_space
                    self.pod_success_packets.value_namespace_prefix = name_space_prefix


        class GySessionIds(Entity):
            """
            Diameter Gy Session data list
            
            .. attribute:: gy_session_id
            
            	Diameter Gy Session data
            	**type**\: list of    :py:class:`GySessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds.GySessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GySessionIds, self).__init__()

                self.yang_name = "gy-session-ids"
                self.yang_parent_name = "diameter"

                self.gy_session_id = YList(self)

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
                            super(Aaa.Diameter.GySessionIds, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.GySessionIds, self).__setattr__(name, value)


            class GySessionId(Entity):
                """
                Diameter Gy Session data
                
                .. attribute:: session_id  <key>
                
                	Session Id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: parent_aaa_session_id
                
                	AAA Parent session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\:  str
                
                .. attribute:: retry_count
                
                	Gy Retry count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.GySessionIds.GySessionId, self).__init__()

                    self.yang_name = "gy-session-id"
                    self.yang_parent_name = "gy-session-ids"

                    self.session_id = YLeaf(YType.int32, "session-id")

                    self.aaa_session_id = YLeaf(YType.uint32, "aaa-session-id")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.parent_aaa_session_id = YLeaf(YType.uint32, "parent-aaa-session-id")

                    self.request_number = YLeaf(YType.uint32, "request-number")

                    self.request_type = YLeaf(YType.str, "request-type")

                    self.retry_count = YLeaf(YType.uint32, "retry-count")

                    self.session_state = YLeaf(YType.str, "session-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("session_id",
                                    "aaa_session_id",
                                    "diameter_session_id",
                                    "parent_aaa_session_id",
                                    "request_number",
                                    "request_type",
                                    "retry_count",
                                    "session_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.GySessionIds.GySessionId, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.GySessionIds.GySessionId, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.session_id.is_set or
                        self.aaa_session_id.is_set or
                        self.diameter_session_id.is_set or
                        self.parent_aaa_session_id.is_set or
                        self.request_number.is_set or
                        self.request_type.is_set or
                        self.retry_count.is_set or
                        self.session_state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.session_id.yfilter != YFilter.not_set or
                        self.aaa_session_id.yfilter != YFilter.not_set or
                        self.diameter_session_id.yfilter != YFilter.not_set or
                        self.parent_aaa_session_id.yfilter != YFilter.not_set or
                        self.request_number.yfilter != YFilter.not_set or
                        self.request_type.yfilter != YFilter.not_set or
                        self.retry_count.yfilter != YFilter.not_set or
                        self.session_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "gy-session-id" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/gy-session-ids/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_id.get_name_leafdata())
                    if (self.aaa_session_id.is_set or self.aaa_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aaa_session_id.get_name_leafdata())
                    if (self.diameter_session_id.is_set or self.diameter_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.diameter_session_id.get_name_leafdata())
                    if (self.parent_aaa_session_id.is_set or self.parent_aaa_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.parent_aaa_session_id.get_name_leafdata())
                    if (self.request_number.is_set or self.request_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.request_number.get_name_leafdata())
                    if (self.request_type.is_set or self.request_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.request_type.get_name_leafdata())
                    if (self.retry_count.is_set or self.retry_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retry_count.get_name_leafdata())
                    if (self.session_state.is_set or self.session_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-id" or name == "aaa-session-id" or name == "diameter-session-id" or name == "parent-aaa-session-id" or name == "request-number" or name == "request-type" or name == "retry-count" or name == "session-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "session-id"):
                        self.session_id = value
                        self.session_id.value_namespace = name_space
                        self.session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "aaa-session-id"):
                        self.aaa_session_id = value
                        self.aaa_session_id.value_namespace = name_space
                        self.aaa_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "diameter-session-id"):
                        self.diameter_session_id = value
                        self.diameter_session_id.value_namespace = name_space
                        self.diameter_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "parent-aaa-session-id"):
                        self.parent_aaa_session_id = value
                        self.parent_aaa_session_id.value_namespace = name_space
                        self.parent_aaa_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "request-number"):
                        self.request_number = value
                        self.request_number.value_namespace = name_space
                        self.request_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "request-type"):
                        self.request_type = value
                        self.request_type.value_namespace = name_space
                        self.request_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "retry-count"):
                        self.retry_count = value
                        self.retry_count.value_namespace = name_space
                        self.retry_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-state"):
                        self.session_state = value
                        self.session_state.value_namespace = name_space
                        self.session_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.gy_session_id:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.gy_session_id:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gy-session-ids" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "gy-session-id"):
                    for c in self.gy_session_id:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Diameter.GySessionIds.GySessionId()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.gy_session_id.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "gy-session-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class GyStatistics(Entity):
            """
            Diameter Gy Statistics data
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messages
            
            	ASA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GyStatistics, self).__init__()

                self.yang_name = "gy-statistics"
                self.yang_parent_name = "diameter"

                self.active_sessions = YLeaf(YType.uint32, "active-sessions")

                self.asa_sent_error_messages = YLeaf(YType.uint32, "asa-sent-error-messages")

                self.asa_sent_messages = YLeaf(YType.uint32, "asa-sent-messages")

                self.asr_received_error_messages = YLeaf(YType.uint32, "asr-received-error-messages")

                self.asr_received_messages = YLeaf(YType.uint32, "asr-received-messages")

                self.cca_final_error_messages = YLeaf(YType.uint32, "cca-final-error-messages")

                self.cca_final_messages = YLeaf(YType.uint32, "cca-final-messages")

                self.cca_init_error_messages = YLeaf(YType.uint32, "cca-init-error-messages")

                self.cca_init_messages = YLeaf(YType.uint32, "cca-init-messages")

                self.cca_update_error_messages = YLeaf(YType.uint32, "cca-update-error-messages")

                self.cca_update_messages = YLeaf(YType.uint32, "cca-update-messages")

                self.ccr_final_failed_messages = YLeaf(YType.uint32, "ccr-final-failed-messages")

                self.ccr_final_messages = YLeaf(YType.uint32, "ccr-final-messages")

                self.ccr_final_retry_messages = YLeaf(YType.uint32, "ccr-final-retry-messages")

                self.ccr_final_timed_out_messages = YLeaf(YType.uint32, "ccr-final-timed-out-messages")

                self.ccr_init_failed_messages = YLeaf(YType.uint32, "ccr-init-failed-messages")

                self.ccr_init_messages = YLeaf(YType.uint32, "ccr-init-messages")

                self.ccr_init_retry_messages = YLeaf(YType.uint32, "ccr-init-retry-messages")

                self.ccr_init_timed_out_messages = YLeaf(YType.uint32, "ccr-init-timed-out-messages")

                self.ccr_update_failed_messages = YLeaf(YType.uint32, "ccr-update-failed-messages")

                self.ccr_update_messages = YLeaf(YType.uint32, "ccr-update-messages")

                self.ccr_update_retry_messages = YLeaf(YType.uint32, "ccr-update-retry-messages")

                self.ccr_update_timed_out_messages = YLeaf(YType.uint32, "ccr-update-timed-out-messages")

                self.close_sessions = YLeaf(YType.uint32, "close-sessions")

                self.open_sessions = YLeaf(YType.uint32, "open-sessions")

                self.raa_sent_error_messages = YLeaf(YType.uint32, "raa-sent-error-messages")

                self.raa_sent_messages = YLeaf(YType.uint32, "raa-sent-messages")

                self.rar_received_error_messages = YLeaf(YType.uint32, "rar-received-error-messages")

                self.rar_received_messages = YLeaf(YType.uint32, "rar-received-messages")

                self.restore_sessions = YLeaf(YType.uint32, "restore-sessions")

                self.unknown_request_messages = YLeaf(YType.uint32, "unknown-request-messages")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("active_sessions",
                                "asa_sent_error_messages",
                                "asa_sent_messages",
                                "asr_received_error_messages",
                                "asr_received_messages",
                                "cca_final_error_messages",
                                "cca_final_messages",
                                "cca_init_error_messages",
                                "cca_init_messages",
                                "cca_update_error_messages",
                                "cca_update_messages",
                                "ccr_final_failed_messages",
                                "ccr_final_messages",
                                "ccr_final_retry_messages",
                                "ccr_final_timed_out_messages",
                                "ccr_init_failed_messages",
                                "ccr_init_messages",
                                "ccr_init_retry_messages",
                                "ccr_init_timed_out_messages",
                                "ccr_update_failed_messages",
                                "ccr_update_messages",
                                "ccr_update_retry_messages",
                                "ccr_update_timed_out_messages",
                                "close_sessions",
                                "open_sessions",
                                "raa_sent_error_messages",
                                "raa_sent_messages",
                                "rar_received_error_messages",
                                "rar_received_messages",
                                "restore_sessions",
                                "unknown_request_messages") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.GyStatistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.GyStatistics, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.active_sessions.is_set or
                    self.asa_sent_error_messages.is_set or
                    self.asa_sent_messages.is_set or
                    self.asr_received_error_messages.is_set or
                    self.asr_received_messages.is_set or
                    self.cca_final_error_messages.is_set or
                    self.cca_final_messages.is_set or
                    self.cca_init_error_messages.is_set or
                    self.cca_init_messages.is_set or
                    self.cca_update_error_messages.is_set or
                    self.cca_update_messages.is_set or
                    self.ccr_final_failed_messages.is_set or
                    self.ccr_final_messages.is_set or
                    self.ccr_final_retry_messages.is_set or
                    self.ccr_final_timed_out_messages.is_set or
                    self.ccr_init_failed_messages.is_set or
                    self.ccr_init_messages.is_set or
                    self.ccr_init_retry_messages.is_set or
                    self.ccr_init_timed_out_messages.is_set or
                    self.ccr_update_failed_messages.is_set or
                    self.ccr_update_messages.is_set or
                    self.ccr_update_retry_messages.is_set or
                    self.ccr_update_timed_out_messages.is_set or
                    self.close_sessions.is_set or
                    self.open_sessions.is_set or
                    self.raa_sent_error_messages.is_set or
                    self.raa_sent_messages.is_set or
                    self.rar_received_error_messages.is_set or
                    self.rar_received_messages.is_set or
                    self.restore_sessions.is_set or
                    self.unknown_request_messages.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.active_sessions.yfilter != YFilter.not_set or
                    self.asa_sent_error_messages.yfilter != YFilter.not_set or
                    self.asa_sent_messages.yfilter != YFilter.not_set or
                    self.asr_received_error_messages.yfilter != YFilter.not_set or
                    self.asr_received_messages.yfilter != YFilter.not_set or
                    self.cca_final_error_messages.yfilter != YFilter.not_set or
                    self.cca_final_messages.yfilter != YFilter.not_set or
                    self.cca_init_error_messages.yfilter != YFilter.not_set or
                    self.cca_init_messages.yfilter != YFilter.not_set or
                    self.cca_update_error_messages.yfilter != YFilter.not_set or
                    self.cca_update_messages.yfilter != YFilter.not_set or
                    self.ccr_final_failed_messages.yfilter != YFilter.not_set or
                    self.ccr_final_messages.yfilter != YFilter.not_set or
                    self.ccr_final_retry_messages.yfilter != YFilter.not_set or
                    self.ccr_final_timed_out_messages.yfilter != YFilter.not_set or
                    self.ccr_init_failed_messages.yfilter != YFilter.not_set or
                    self.ccr_init_messages.yfilter != YFilter.not_set or
                    self.ccr_init_retry_messages.yfilter != YFilter.not_set or
                    self.ccr_init_timed_out_messages.yfilter != YFilter.not_set or
                    self.ccr_update_failed_messages.yfilter != YFilter.not_set or
                    self.ccr_update_messages.yfilter != YFilter.not_set or
                    self.ccr_update_retry_messages.yfilter != YFilter.not_set or
                    self.ccr_update_timed_out_messages.yfilter != YFilter.not_set or
                    self.close_sessions.yfilter != YFilter.not_set or
                    self.open_sessions.yfilter != YFilter.not_set or
                    self.raa_sent_error_messages.yfilter != YFilter.not_set or
                    self.raa_sent_messages.yfilter != YFilter.not_set or
                    self.rar_received_error_messages.yfilter != YFilter.not_set or
                    self.rar_received_messages.yfilter != YFilter.not_set or
                    self.restore_sessions.yfilter != YFilter.not_set or
                    self.unknown_request_messages.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gy-statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.active_sessions.is_set or self.active_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.active_sessions.get_name_leafdata())
                if (self.asa_sent_error_messages.is_set or self.asa_sent_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asa_sent_error_messages.get_name_leafdata())
                if (self.asa_sent_messages.is_set or self.asa_sent_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asa_sent_messages.get_name_leafdata())
                if (self.asr_received_error_messages.is_set or self.asr_received_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asr_received_error_messages.get_name_leafdata())
                if (self.asr_received_messages.is_set or self.asr_received_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.asr_received_messages.get_name_leafdata())
                if (self.cca_final_error_messages.is_set or self.cca_final_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_final_error_messages.get_name_leafdata())
                if (self.cca_final_messages.is_set or self.cca_final_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_final_messages.get_name_leafdata())
                if (self.cca_init_error_messages.is_set or self.cca_init_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_init_error_messages.get_name_leafdata())
                if (self.cca_init_messages.is_set or self.cca_init_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_init_messages.get_name_leafdata())
                if (self.cca_update_error_messages.is_set or self.cca_update_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_update_error_messages.get_name_leafdata())
                if (self.cca_update_messages.is_set or self.cca_update_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cca_update_messages.get_name_leafdata())
                if (self.ccr_final_failed_messages.is_set or self.ccr_final_failed_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_failed_messages.get_name_leafdata())
                if (self.ccr_final_messages.is_set or self.ccr_final_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_messages.get_name_leafdata())
                if (self.ccr_final_retry_messages.is_set or self.ccr_final_retry_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_retry_messages.get_name_leafdata())
                if (self.ccr_final_timed_out_messages.is_set or self.ccr_final_timed_out_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_final_timed_out_messages.get_name_leafdata())
                if (self.ccr_init_failed_messages.is_set or self.ccr_init_failed_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_failed_messages.get_name_leafdata())
                if (self.ccr_init_messages.is_set or self.ccr_init_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_messages.get_name_leafdata())
                if (self.ccr_init_retry_messages.is_set or self.ccr_init_retry_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_retry_messages.get_name_leafdata())
                if (self.ccr_init_timed_out_messages.is_set or self.ccr_init_timed_out_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_init_timed_out_messages.get_name_leafdata())
                if (self.ccr_update_failed_messages.is_set or self.ccr_update_failed_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_failed_messages.get_name_leafdata())
                if (self.ccr_update_messages.is_set or self.ccr_update_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_messages.get_name_leafdata())
                if (self.ccr_update_retry_messages.is_set or self.ccr_update_retry_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_retry_messages.get_name_leafdata())
                if (self.ccr_update_timed_out_messages.is_set or self.ccr_update_timed_out_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccr_update_timed_out_messages.get_name_leafdata())
                if (self.close_sessions.is_set or self.close_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.close_sessions.get_name_leafdata())
                if (self.open_sessions.is_set or self.open_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.open_sessions.get_name_leafdata())
                if (self.raa_sent_error_messages.is_set or self.raa_sent_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.raa_sent_error_messages.get_name_leafdata())
                if (self.raa_sent_messages.is_set or self.raa_sent_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.raa_sent_messages.get_name_leafdata())
                if (self.rar_received_error_messages.is_set or self.rar_received_error_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rar_received_error_messages.get_name_leafdata())
                if (self.rar_received_messages.is_set or self.rar_received_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rar_received_messages.get_name_leafdata())
                if (self.restore_sessions.is_set or self.restore_sessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.restore_sessions.get_name_leafdata())
                if (self.unknown_request_messages.is_set or self.unknown_request_messages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unknown_request_messages.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "active-sessions" or name == "asa-sent-error-messages" or name == "asa-sent-messages" or name == "asr-received-error-messages" or name == "asr-received-messages" or name == "cca-final-error-messages" or name == "cca-final-messages" or name == "cca-init-error-messages" or name == "cca-init-messages" or name == "cca-update-error-messages" or name == "cca-update-messages" or name == "ccr-final-failed-messages" or name == "ccr-final-messages" or name == "ccr-final-retry-messages" or name == "ccr-final-timed-out-messages" or name == "ccr-init-failed-messages" or name == "ccr-init-messages" or name == "ccr-init-retry-messages" or name == "ccr-init-timed-out-messages" or name == "ccr-update-failed-messages" or name == "ccr-update-messages" or name == "ccr-update-retry-messages" or name == "ccr-update-timed-out-messages" or name == "close-sessions" or name == "open-sessions" or name == "raa-sent-error-messages" or name == "raa-sent-messages" or name == "rar-received-error-messages" or name == "rar-received-messages" or name == "restore-sessions" or name == "unknown-request-messages"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "active-sessions"):
                    self.active_sessions = value
                    self.active_sessions.value_namespace = name_space
                    self.active_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "asa-sent-error-messages"):
                    self.asa_sent_error_messages = value
                    self.asa_sent_error_messages.value_namespace = name_space
                    self.asa_sent_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "asa-sent-messages"):
                    self.asa_sent_messages = value
                    self.asa_sent_messages.value_namespace = name_space
                    self.asa_sent_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "asr-received-error-messages"):
                    self.asr_received_error_messages = value
                    self.asr_received_error_messages.value_namespace = name_space
                    self.asr_received_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "asr-received-messages"):
                    self.asr_received_messages = value
                    self.asr_received_messages.value_namespace = name_space
                    self.asr_received_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-final-error-messages"):
                    self.cca_final_error_messages = value
                    self.cca_final_error_messages.value_namespace = name_space
                    self.cca_final_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-final-messages"):
                    self.cca_final_messages = value
                    self.cca_final_messages.value_namespace = name_space
                    self.cca_final_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-init-error-messages"):
                    self.cca_init_error_messages = value
                    self.cca_init_error_messages.value_namespace = name_space
                    self.cca_init_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-init-messages"):
                    self.cca_init_messages = value
                    self.cca_init_messages.value_namespace = name_space
                    self.cca_init_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-update-error-messages"):
                    self.cca_update_error_messages = value
                    self.cca_update_error_messages.value_namespace = name_space
                    self.cca_update_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "cca-update-messages"):
                    self.cca_update_messages = value
                    self.cca_update_messages.value_namespace = name_space
                    self.cca_update_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-failed-messages"):
                    self.ccr_final_failed_messages = value
                    self.ccr_final_failed_messages.value_namespace = name_space
                    self.ccr_final_failed_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-messages"):
                    self.ccr_final_messages = value
                    self.ccr_final_messages.value_namespace = name_space
                    self.ccr_final_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-retry-messages"):
                    self.ccr_final_retry_messages = value
                    self.ccr_final_retry_messages.value_namespace = name_space
                    self.ccr_final_retry_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-final-timed-out-messages"):
                    self.ccr_final_timed_out_messages = value
                    self.ccr_final_timed_out_messages.value_namespace = name_space
                    self.ccr_final_timed_out_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-failed-messages"):
                    self.ccr_init_failed_messages = value
                    self.ccr_init_failed_messages.value_namespace = name_space
                    self.ccr_init_failed_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-messages"):
                    self.ccr_init_messages = value
                    self.ccr_init_messages.value_namespace = name_space
                    self.ccr_init_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-retry-messages"):
                    self.ccr_init_retry_messages = value
                    self.ccr_init_retry_messages.value_namespace = name_space
                    self.ccr_init_retry_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-init-timed-out-messages"):
                    self.ccr_init_timed_out_messages = value
                    self.ccr_init_timed_out_messages.value_namespace = name_space
                    self.ccr_init_timed_out_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-failed-messages"):
                    self.ccr_update_failed_messages = value
                    self.ccr_update_failed_messages.value_namespace = name_space
                    self.ccr_update_failed_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-messages"):
                    self.ccr_update_messages = value
                    self.ccr_update_messages.value_namespace = name_space
                    self.ccr_update_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-retry-messages"):
                    self.ccr_update_retry_messages = value
                    self.ccr_update_retry_messages.value_namespace = name_space
                    self.ccr_update_retry_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "ccr-update-timed-out-messages"):
                    self.ccr_update_timed_out_messages = value
                    self.ccr_update_timed_out_messages.value_namespace = name_space
                    self.ccr_update_timed_out_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "close-sessions"):
                    self.close_sessions = value
                    self.close_sessions.value_namespace = name_space
                    self.close_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "open-sessions"):
                    self.open_sessions = value
                    self.open_sessions.value_namespace = name_space
                    self.open_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "raa-sent-error-messages"):
                    self.raa_sent_error_messages = value
                    self.raa_sent_error_messages.value_namespace = name_space
                    self.raa_sent_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "raa-sent-messages"):
                    self.raa_sent_messages = value
                    self.raa_sent_messages.value_namespace = name_space
                    self.raa_sent_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "rar-received-error-messages"):
                    self.rar_received_error_messages = value
                    self.rar_received_error_messages.value_namespace = name_space
                    self.rar_received_error_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "rar-received-messages"):
                    self.rar_received_messages = value
                    self.rar_received_messages.value_namespace = name_space
                    self.rar_received_messages.value_namespace_prefix = name_space_prefix
                if(value_path == "restore-sessions"):
                    self.restore_sessions = value
                    self.restore_sessions.value_namespace = name_space
                    self.restore_sessions.value_namespace_prefix = name_space_prefix
                if(value_path == "unknown-request-messages"):
                    self.unknown_request_messages = value
                    self.unknown_request_messages.value_namespace = name_space
                    self.unknown_request_messages.value_namespace_prefix = name_space_prefix


        class GxSessionIds(Entity):
            """
            Diameter Gx Session data list
            
            .. attribute:: gx_session_id
            
            	Diameter Gx Session data
            	**type**\: list of    :py:class:`GxSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds.GxSessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.GxSessionIds, self).__init__()

                self.yang_name = "gx-session-ids"
                self.yang_parent_name = "diameter"

                self.gx_session_id = YList(self)

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
                            super(Aaa.Diameter.GxSessionIds, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.GxSessionIds, self).__setattr__(name, value)


            class GxSessionId(Entity):
                """
                Diameter Gx Session data
                
                .. attribute:: session_id  <key>
                
                	Session Id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\:  str
                
                .. attribute:: retry_count
                
                	Gx Retry count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.GxSessionIds.GxSessionId, self).__init__()

                    self.yang_name = "gx-session-id"
                    self.yang_parent_name = "gx-session-ids"

                    self.session_id = YLeaf(YType.int32, "session-id")

                    self.aaa_session_id = YLeaf(YType.uint32, "aaa-session-id")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.request_number = YLeaf(YType.uint32, "request-number")

                    self.request_type = YLeaf(YType.str, "request-type")

                    self.retry_count = YLeaf(YType.uint32, "retry-count")

                    self.session_state = YLeaf(YType.str, "session-state")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("session_id",
                                    "aaa_session_id",
                                    "diameter_session_id",
                                    "request_number",
                                    "request_type",
                                    "retry_count",
                                    "session_state") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.GxSessionIds.GxSessionId, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.GxSessionIds.GxSessionId, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.session_id.is_set or
                        self.aaa_session_id.is_set or
                        self.diameter_session_id.is_set or
                        self.request_number.is_set or
                        self.request_type.is_set or
                        self.retry_count.is_set or
                        self.session_state.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.session_id.yfilter != YFilter.not_set or
                        self.aaa_session_id.yfilter != YFilter.not_set or
                        self.diameter_session_id.yfilter != YFilter.not_set or
                        self.request_number.yfilter != YFilter.not_set or
                        self.request_type.yfilter != YFilter.not_set or
                        self.retry_count.yfilter != YFilter.not_set or
                        self.session_state.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "gx-session-id" + "[session-id='" + self.session_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/gx-session-ids/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_id.get_name_leafdata())
                    if (self.aaa_session_id.is_set or self.aaa_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aaa_session_id.get_name_leafdata())
                    if (self.diameter_session_id.is_set or self.diameter_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.diameter_session_id.get_name_leafdata())
                    if (self.request_number.is_set or self.request_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.request_number.get_name_leafdata())
                    if (self.request_type.is_set or self.request_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.request_type.get_name_leafdata())
                    if (self.retry_count.is_set or self.retry_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retry_count.get_name_leafdata())
                    if (self.session_state.is_set or self.session_state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_state.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session-id" or name == "aaa-session-id" or name == "diameter-session-id" or name == "request-number" or name == "request-type" or name == "retry-count" or name == "session-state"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "session-id"):
                        self.session_id = value
                        self.session_id.value_namespace = name_space
                        self.session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "aaa-session-id"):
                        self.aaa_session_id = value
                        self.aaa_session_id.value_namespace = name_space
                        self.aaa_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "diameter-session-id"):
                        self.diameter_session_id = value
                        self.diameter_session_id.value_namespace = name_space
                        self.diameter_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "request-number"):
                        self.request_number = value
                        self.request_number.value_namespace = name_space
                        self.request_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "request-type"):
                        self.request_type = value
                        self.request_type.value_namespace = name_space
                        self.request_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "retry-count"):
                        self.retry_count = value
                        self.retry_count.value_namespace = name_space
                        self.retry_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-state"):
                        self.session_state = value
                        self.session_state.value_namespace = name_space
                        self.session_state.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.gx_session_id:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.gx_session_id:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "gx-session-ids" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "gx-session-id"):
                    for c in self.gx_session_id:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Diameter.GxSessionIds.GxSessionId()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.gx_session_id.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "gx-session-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class NasSession(Entity):
            """
            Diameter Nas Session data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\:  str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of    :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Diameter.NasSession, self).__init__()

                self.yang_name = "nas-session"
                self.yang_parent_name = "diameter"

                self.aaanas_id = YLeaf(YType.str, "aaanas-id")

                self.list_of_nas = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("aaanas_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Diameter.NasSession, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Diameter.NasSession, self).__setattr__(name, value)


            class ListOfNas(Entity):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  str
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\:  str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Diameter.NasSession.ListOfNas, self).__init__()

                    self.yang_name = "list-of-nas"
                    self.yang_parent_name = "nas-session"

                    self.aaa_session_id = YLeaf(YType.str, "aaa-session-id")

                    self.accounting_intrim_in_packets = YLeaf(YType.uint32, "accounting-intrim-in-packets")

                    self.accounting_intrim_out_packets = YLeaf(YType.uint32, "accounting-intrim-out-packets")

                    self.accounting_status = YLeaf(YType.uint32, "accounting-status")

                    self.accounting_status_stop = YLeaf(YType.uint32, "accounting-status-stop")

                    self.authentication_status = YLeaf(YType.uint32, "authentication-status")

                    self.authorization_status = YLeaf(YType.uint32, "authorization-status")

                    self.diameter_session_id = YLeaf(YType.str, "diameter-session-id")

                    self.disconnect_status = YLeaf(YType.uint32, "disconnect-status")

                    self.method_list = YLeaf(YType.str, "method-list")

                    self.server_used_list = YLeaf(YType.str, "server-used-list")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("aaa_session_id",
                                    "accounting_intrim_in_packets",
                                    "accounting_intrim_out_packets",
                                    "accounting_status",
                                    "accounting_status_stop",
                                    "authentication_status",
                                    "authorization_status",
                                    "diameter_session_id",
                                    "disconnect_status",
                                    "method_list",
                                    "server_used_list") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Diameter.NasSession.ListOfNas, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Diameter.NasSession.ListOfNas, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.aaa_session_id.is_set or
                        self.accounting_intrim_in_packets.is_set or
                        self.accounting_intrim_out_packets.is_set or
                        self.accounting_status.is_set or
                        self.accounting_status_stop.is_set or
                        self.authentication_status.is_set or
                        self.authorization_status.is_set or
                        self.diameter_session_id.is_set or
                        self.disconnect_status.is_set or
                        self.method_list.is_set or
                        self.server_used_list.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.aaa_session_id.yfilter != YFilter.not_set or
                        self.accounting_intrim_in_packets.yfilter != YFilter.not_set or
                        self.accounting_intrim_out_packets.yfilter != YFilter.not_set or
                        self.accounting_status.yfilter != YFilter.not_set or
                        self.accounting_status_stop.yfilter != YFilter.not_set or
                        self.authentication_status.yfilter != YFilter.not_set or
                        self.authorization_status.yfilter != YFilter.not_set or
                        self.diameter_session_id.yfilter != YFilter.not_set or
                        self.disconnect_status.yfilter != YFilter.not_set or
                        self.method_list.yfilter != YFilter.not_set or
                        self.server_used_list.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "list-of-nas" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/nas-session/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.aaa_session_id.is_set or self.aaa_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aaa_session_id.get_name_leafdata())
                    if (self.accounting_intrim_in_packets.is_set or self.accounting_intrim_in_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_intrim_in_packets.get_name_leafdata())
                    if (self.accounting_intrim_out_packets.is_set or self.accounting_intrim_out_packets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_intrim_out_packets.get_name_leafdata())
                    if (self.accounting_status.is_set or self.accounting_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_status.get_name_leafdata())
                    if (self.accounting_status_stop.is_set or self.accounting_status_stop.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_status_stop.get_name_leafdata())
                    if (self.authentication_status.is_set or self.authentication_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_status.get_name_leafdata())
                    if (self.authorization_status.is_set or self.authorization_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authorization_status.get_name_leafdata())
                    if (self.diameter_session_id.is_set or self.diameter_session_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.diameter_session_id.get_name_leafdata())
                    if (self.disconnect_status.is_set or self.disconnect_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disconnect_status.get_name_leafdata())
                    if (self.method_list.is_set or self.method_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.method_list.get_name_leafdata())
                    if (self.server_used_list.is_set or self.server_used_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.server_used_list.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aaa-session-id" or name == "accounting-intrim-in-packets" or name == "accounting-intrim-out-packets" or name == "accounting-status" or name == "accounting-status-stop" or name == "authentication-status" or name == "authorization-status" or name == "diameter-session-id" or name == "disconnect-status" or name == "method-list" or name == "server-used-list"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "aaa-session-id"):
                        self.aaa_session_id = value
                        self.aaa_session_id.value_namespace = name_space
                        self.aaa_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-intrim-in-packets"):
                        self.accounting_intrim_in_packets = value
                        self.accounting_intrim_in_packets.value_namespace = name_space
                        self.accounting_intrim_in_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-intrim-out-packets"):
                        self.accounting_intrim_out_packets = value
                        self.accounting_intrim_out_packets.value_namespace = name_space
                        self.accounting_intrim_out_packets.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-status"):
                        self.accounting_status = value
                        self.accounting_status.value_namespace = name_space
                        self.accounting_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-status-stop"):
                        self.accounting_status_stop = value
                        self.accounting_status_stop.value_namespace = name_space
                        self.accounting_status_stop.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-status"):
                        self.authentication_status = value
                        self.authentication_status.value_namespace = name_space
                        self.authentication_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "authorization-status"):
                        self.authorization_status = value
                        self.authorization_status.value_namespace = name_space
                        self.authorization_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "diameter-session-id"):
                        self.diameter_session_id = value
                        self.diameter_session_id.value_namespace = name_space
                        self.diameter_session_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "disconnect-status"):
                        self.disconnect_status = value
                        self.disconnect_status.value_namespace = name_space
                        self.disconnect_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "method-list"):
                        self.method_list = value
                        self.method_list.value_namespace = name_space
                        self.method_list.value_namespace_prefix = name_space_prefix
                    if(value_path == "server-used-list"):
                        self.server_used_list = value
                        self.server_used_list.value_namespace = name_space
                        self.server_used_list.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.list_of_nas:
                    if (c.has_data()):
                        return True
                return self.aaanas_id.is_set

            def has_operation(self):
                for c in self.list_of_nas:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.aaanas_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nas-session" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.aaanas_id.is_set or self.aaanas_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.aaanas_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "list-of-nas"):
                    for c in self.list_of_nas:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Diameter.NasSession.ListOfNas()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.list_of_nas.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "list-of-nas" or name == "aaanas-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "aaanas-id"):
                    self.aaanas_id = value
                    self.aaanas_id.value_namespace = name_space
                    self.aaanas_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.gx is not None and self.gx.has_data()) or
                (self.gx_session_ids is not None and self.gx_session_ids.has_data()) or
                (self.gx_statistics is not None and self.gx_statistics.has_data()) or
                (self.gy is not None and self.gy.has_data()) or
                (self.gy_session_ids is not None and self.gy_session_ids.has_data()) or
                (self.gy_statistics is not None and self.gy_statistics.has_data()) or
                (self.nas is not None and self.nas.has_data()) or
                (self.nas_session is not None and self.nas_session.has_data()) or
                (self.nas_summary is not None and self.nas_summary.has_data()) or
                (self.peers is not None and self.peers.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.gx is not None and self.gx.has_operation()) or
                (self.gx_session_ids is not None and self.gx_session_ids.has_operation()) or
                (self.gx_statistics is not None and self.gx_statistics.has_operation()) or
                (self.gy is not None and self.gy.has_operation()) or
                (self.gy_session_ids is not None and self.gy_session_ids.has_operation()) or
                (self.gy_statistics is not None and self.gy_statistics.has_operation()) or
                (self.nas is not None and self.nas.has_operation()) or
                (self.nas_session is not None and self.nas_session.has_operation()) or
                (self.nas_summary is not None and self.nas_summary.has_operation()) or
                (self.peers is not None and self.peers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-diameter-oper:diameter" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "gx"):
                if (self.gx is None):
                    self.gx = Aaa.Diameter.Gx()
                    self.gx.parent = self
                    self._children_name_map["gx"] = "gx"
                return self.gx

            if (child_yang_name == "gx-session-ids"):
                if (self.gx_session_ids is None):
                    self.gx_session_ids = Aaa.Diameter.GxSessionIds()
                    self.gx_session_ids.parent = self
                    self._children_name_map["gx_session_ids"] = "gx-session-ids"
                return self.gx_session_ids

            if (child_yang_name == "gx-statistics"):
                if (self.gx_statistics is None):
                    self.gx_statistics = Aaa.Diameter.GxStatistics()
                    self.gx_statistics.parent = self
                    self._children_name_map["gx_statistics"] = "gx-statistics"
                return self.gx_statistics

            if (child_yang_name == "gy"):
                if (self.gy is None):
                    self.gy = Aaa.Diameter.Gy()
                    self.gy.parent = self
                    self._children_name_map["gy"] = "gy"
                return self.gy

            if (child_yang_name == "gy-session-ids"):
                if (self.gy_session_ids is None):
                    self.gy_session_ids = Aaa.Diameter.GySessionIds()
                    self.gy_session_ids.parent = self
                    self._children_name_map["gy_session_ids"] = "gy-session-ids"
                return self.gy_session_ids

            if (child_yang_name == "gy-statistics"):
                if (self.gy_statistics is None):
                    self.gy_statistics = Aaa.Diameter.GyStatistics()
                    self.gy_statistics.parent = self
                    self._children_name_map["gy_statistics"] = "gy-statistics"
                return self.gy_statistics

            if (child_yang_name == "nas"):
                if (self.nas is None):
                    self.nas = Aaa.Diameter.Nas()
                    self.nas.parent = self
                    self._children_name_map["nas"] = "nas"
                return self.nas

            if (child_yang_name == "nas-session"):
                if (self.nas_session is None):
                    self.nas_session = Aaa.Diameter.NasSession()
                    self.nas_session.parent = self
                    self._children_name_map["nas_session"] = "nas-session"
                return self.nas_session

            if (child_yang_name == "nas-summary"):
                if (self.nas_summary is None):
                    self.nas_summary = Aaa.Diameter.NasSummary()
                    self.nas_summary.parent = self
                    self._children_name_map["nas_summary"] = "nas-summary"
                return self.nas_summary

            if (child_yang_name == "peers"):
                if (self.peers is None):
                    self.peers = Aaa.Diameter.Peers()
                    self.peers.parent = self
                    self._children_name_map["peers"] = "peers"
                return self.peers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "gx" or name == "gx-session-ids" or name == "gx-statistics" or name == "gy" or name == "gy-session-ids" or name == "gy-statistics" or name == "nas" or name == "nas-session" or name == "nas-summary" or name == "peers"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Radius(Entity):
        """
        RADIUS operational data
        
        .. attribute:: global_
        
        	RADIUS Client Information
        	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Global_>`
        
        .. attribute:: radius_source_interface
        
        	RADIUS source interfaces
        	**type**\:   :py:class:`RadiusSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface>`
        
        .. attribute:: servers
        
        	List of RADIUS servers configured
        	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Radius, self).__init__()

            self.yang_name = "radius"
            self.yang_parent_name = "aaa"

            self.global_ = Aaa.Radius.Global_()
            self.global_.parent = self
            self._children_name_map["global_"] = "global"
            self._children_yang_names.add("global")

            self.radius_source_interface = Aaa.Radius.RadiusSourceInterface()
            self.radius_source_interface.parent = self
            self._children_name_map["radius_source_interface"] = "radius-source-interface"
            self._children_yang_names.add("radius-source-interface")

            self.servers = Aaa.Radius.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"
            self._children_yang_names.add("servers")


        class Servers(Entity):
            """
            List of RADIUS servers configured
            
            .. attribute:: server
            
            	RADIUS Server
            	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers.Server>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "radius"

                self.server = YList(self)

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
                            super(Aaa.Radius.Servers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Servers, self).__setattr__(name, value)


            class Server(Entity):
                """
                RADIUS Server
                
                .. attribute:: aborts
                
                	Total number of requests aborted
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_accepts
                
                	Number of access accepts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_challenges
                
                	Number of access challenges
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_rejects
                
                	Number of access rejects
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_request_retransmits
                
                	Number of retransmitted                          access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_requests
                
                	Number of access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_timeouts
                
                	Number of access packets timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_port
                
                	Accounting port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_requests
                
                	Number of accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_responses
                
                	Number of accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_retransmits
                
                	Number of retransmitted                          accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_rtt
                
                	Round\-trip time for accounting                   in milliseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: accounting_timeouts
                
                	Number of accounting packets                     timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_incorrect_responses
                
                	Number of incorrect accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_port_number
                
                	Accounting Port number (standard port 1646)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: acct_response_time
                
                	Average response time for authentication requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_server_error_responses
                
                	Number of server error accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_unexpected_responses
                
                	Number of unexpected accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_port_number
                
                	Authentication Port number (standard port 1645)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: authen_incorrect_responses
                
                	Number of incorrect authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_response_time
                
                	Average response time for authentication requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_server_error_responses
                
                	Number of server error authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_unexpected_responses
                
                	Number of unexpected authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_port
                
                	Authentication port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_rtt
                
                	Round\-trip time for authentication               in milliseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: author_incorrect_responses
                
                	Number of incorrect authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_request_timeouts
                
                	Number of access packets timed out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_requests
                
                	Number of access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_response_time
                
                	Average response time for authorization requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_server_error_responses
                
                	Number of server error authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_failure
                
                	Number of failed authorization transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_successess
                
                	Number of succeeded authorization transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_unexpected_responses
                
                	Number of unexpected authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_authenticators
                
                	Number of bad access authenticators
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_responses
                
                	Number of bad access responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_authenticators
                
                	Number of bad accounting                         authenticators
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_responses
                
                	Number of bad accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_state_duration
                
                	Elapsed time the server has been in              current state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: currently_throttled_access_reqs
                
                	No of currently throttled access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_detect_time
                
                	Per\-server dead\-detect time in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: dead_detect_tries
                
                	Per\-server dead\-detect tries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_time
                
                	Per\-server deadtime in minutes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: dropped_access_responses
                
                	Number of access responses dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_accounting_responses
                
                	Number of accounting responses                   dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: family
                
                	IP address Family
                	**type**\:  str
                
                .. attribute:: group_name
                
                	Server group name for private server
                	**type**\:  str
                
                .. attribute:: ip_address
                
                	IP address of RADIUS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: ip_address_xr
                
                	IP address buffer
                	**type**\:  str
                
                .. attribute:: ipv4_address
                
                	IP address of RADIUS server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: is_a_private_server
                
                	Is a private server
                	**type**\:  bool
                
                .. attribute:: is_quarantined
                
                	flag to indicate Server is quarantined           or not (Automated TEST in progress)
                	**type**\:  bool
                
                .. attribute:: last_deadtime
                
                	Time of Server being in DEAD state,              after last UP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_acct_throttled
                
                	Max throttled acct transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_throttled_access_reqs
                
                	Max throttled access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_in
                
                	Total number of incoming packets read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_out
                
                	Total number of outgoing packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_access_requests
                
                	Number of pending access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_accounting_requets
                
                	Number of pending accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: previous_state_duration
                
                	Elapsed time the server was been in              previous state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority
                
                	A number that indicates the priority             of the server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: redirected_requests
                
                	Number of requests redirected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	Number of replies expected to arrive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: retransmit
                
                	Per\-server retransmit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	State of the server UP/DOWN
                	**type**\:  str
                
                .. attribute:: throttled_access_reqs
                
                	No of throttled access reqs stats
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_failures_stats
                
                	No of acct discarded transaction
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_timed_out_stats
                
                	No of acct transaction that is throttled is timedout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_transactions
                
                	No of throttled acct transactions stats
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_dropped_reqs
                
                	No of discarded access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_timed_out_reqs
                
                	No of access reqs that is throttled is timedout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttleda_acct_transactions
                
                	No of currently throttled acct transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout_xr
                
                	Per\-server timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: timeouts
                
                	Total number of packets timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_deadtime
                
                	Total time of Server being in DEAD               state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_pending
                
                	Total acct test pending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_reqs
                
                	 Total acct test req
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_response
                
                	Total acct test response
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_timeouts
                
                	Total acct test timeouts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_pending
                
                	Total auth test pending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_reqs
                
                	Total auth test request
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_response
                
                	Total auth test response
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_timeouts
                
                	Total auth test timeouts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_access_types
                
                	Number of packets received with unknown          type from authentication server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_accounting_types
                
                	Number of packets received with unknown          type from accounting server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"

                    self.aborts = YLeaf(YType.uint32, "aborts")

                    self.access_accepts = YLeaf(YType.uint32, "access-accepts")

                    self.access_challenges = YLeaf(YType.uint32, "access-challenges")

                    self.access_rejects = YLeaf(YType.uint32, "access-rejects")

                    self.access_request_retransmits = YLeaf(YType.uint32, "access-request-retransmits")

                    self.access_requests = YLeaf(YType.uint32, "access-requests")

                    self.access_timeouts = YLeaf(YType.uint32, "access-timeouts")

                    self.accounting_port = YLeaf(YType.uint32, "accounting-port")

                    self.accounting_requests = YLeaf(YType.uint32, "accounting-requests")

                    self.accounting_responses = YLeaf(YType.uint32, "accounting-responses")

                    self.accounting_retransmits = YLeaf(YType.uint32, "accounting-retransmits")

                    self.accounting_rtt = YLeaf(YType.uint32, "accounting-rtt")

                    self.accounting_timeouts = YLeaf(YType.uint32, "accounting-timeouts")

                    self.acct_incorrect_responses = YLeaf(YType.uint32, "acct-incorrect-responses")

                    self.acct_port_number = YLeaf(YType.uint32, "acct-port-number")

                    self.acct_response_time = YLeaf(YType.uint32, "acct-response-time")

                    self.acct_server_error_responses = YLeaf(YType.uint32, "acct-server-error-responses")

                    self.acct_transaction_failure = YLeaf(YType.uint32, "acct-transaction-failure")

                    self.acct_transaction_successess = YLeaf(YType.uint32, "acct-transaction-successess")

                    self.acct_unexpected_responses = YLeaf(YType.uint32, "acct-unexpected-responses")

                    self.auth_port_number = YLeaf(YType.uint32, "auth-port-number")

                    self.authen_incorrect_responses = YLeaf(YType.uint32, "authen-incorrect-responses")

                    self.authen_response_time = YLeaf(YType.uint32, "authen-response-time")

                    self.authen_server_error_responses = YLeaf(YType.uint32, "authen-server-error-responses")

                    self.authen_transaction_failure = YLeaf(YType.uint32, "authen-transaction-failure")

                    self.authen_transaction_successess = YLeaf(YType.uint32, "authen-transaction-successess")

                    self.authen_unexpected_responses = YLeaf(YType.uint32, "authen-unexpected-responses")

                    self.authentication_port = YLeaf(YType.uint32, "authentication-port")

                    self.authentication_rtt = YLeaf(YType.uint32, "authentication-rtt")

                    self.author_incorrect_responses = YLeaf(YType.uint32, "author-incorrect-responses")

                    self.author_request_timeouts = YLeaf(YType.uint32, "author-request-timeouts")

                    self.author_requests = YLeaf(YType.uint32, "author-requests")

                    self.author_response_time = YLeaf(YType.uint32, "author-response-time")

                    self.author_server_error_responses = YLeaf(YType.uint32, "author-server-error-responses")

                    self.author_transaction_failure = YLeaf(YType.uint32, "author-transaction-failure")

                    self.author_transaction_successess = YLeaf(YType.uint32, "author-transaction-successess")

                    self.author_unexpected_responses = YLeaf(YType.uint32, "author-unexpected-responses")

                    self.bad_access_authenticators = YLeaf(YType.uint32, "bad-access-authenticators")

                    self.bad_access_responses = YLeaf(YType.uint32, "bad-access-responses")

                    self.bad_accounting_authenticators = YLeaf(YType.uint32, "bad-accounting-authenticators")

                    self.bad_accounting_responses = YLeaf(YType.uint32, "bad-accounting-responses")

                    self.current_state_duration = YLeaf(YType.uint32, "current-state-duration")

                    self.currently_throttled_access_reqs = YLeaf(YType.uint32, "currently-throttled-access-reqs")

                    self.dead_detect_time = YLeaf(YType.uint32, "dead-detect-time")

                    self.dead_detect_tries = YLeaf(YType.uint32, "dead-detect-tries")

                    self.dead_time = YLeaf(YType.uint32, "dead-time")

                    self.dropped_access_responses = YLeaf(YType.uint32, "dropped-access-responses")

                    self.dropped_accounting_responses = YLeaf(YType.uint32, "dropped-accounting-responses")

                    self.family = YLeaf(YType.str, "family")

                    self.group_name = YLeaf(YType.str, "group-name")

                    self.ip_address = YLeaf(YType.str, "ip-address")

                    self.ip_address_xr = YLeaf(YType.str, "ip-address-xr")

                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                    self.is_a_private_server = YLeaf(YType.boolean, "is-a-private-server")

                    self.is_quarantined = YLeaf(YType.boolean, "is-quarantined")

                    self.last_deadtime = YLeaf(YType.uint32, "last-deadtime")

                    self.max_acct_throttled = YLeaf(YType.uint32, "max-acct-throttled")

                    self.max_throttled_access_reqs = YLeaf(YType.uint32, "max-throttled-access-reqs")

                    self.packets_in = YLeaf(YType.uint32, "packets-in")

                    self.packets_out = YLeaf(YType.uint32, "packets-out")

                    self.pending_access_requests = YLeaf(YType.uint32, "pending-access-requests")

                    self.pending_accounting_requets = YLeaf(YType.uint32, "pending-accounting-requets")

                    self.previous_state_duration = YLeaf(YType.uint32, "previous-state-duration")

                    self.priority = YLeaf(YType.uint32, "priority")

                    self.redirected_requests = YLeaf(YType.uint32, "redirected-requests")

                    self.replies_expected = YLeaf(YType.uint32, "replies-expected")

                    self.retransmit = YLeaf(YType.uint32, "retransmit")

                    self.state = YLeaf(YType.str, "state")

                    self.throttled_access_reqs = YLeaf(YType.uint32, "throttled-access-reqs")

                    self.throttled_acct_failures_stats = YLeaf(YType.uint32, "throttled-acct-failures-stats")

                    self.throttled_acct_timed_out_stats = YLeaf(YType.uint32, "throttled-acct-timed-out-stats")

                    self.throttled_acct_transactions = YLeaf(YType.uint32, "throttled-acct-transactions")

                    self.throttled_dropped_reqs = YLeaf(YType.uint32, "throttled-dropped-reqs")

                    self.throttled_timed_out_reqs = YLeaf(YType.uint32, "throttled-timed-out-reqs")

                    self.throttleda_acct_transactions = YLeaf(YType.uint32, "throttleda-acct-transactions")

                    self.timeout_xr = YLeaf(YType.uint32, "timeout-xr")

                    self.timeouts = YLeaf(YType.uint32, "timeouts")

                    self.total_deadtime = YLeaf(YType.uint32, "total-deadtime")

                    self.total_test_acct_pending = YLeaf(YType.uint32, "total-test-acct-pending")

                    self.total_test_acct_reqs = YLeaf(YType.uint32, "total-test-acct-reqs")

                    self.total_test_acct_response = YLeaf(YType.uint32, "total-test-acct-response")

                    self.total_test_acct_timeouts = YLeaf(YType.uint32, "total-test-acct-timeouts")

                    self.total_test_auth_pending = YLeaf(YType.uint32, "total-test-auth-pending")

                    self.total_test_auth_reqs = YLeaf(YType.uint32, "total-test-auth-reqs")

                    self.total_test_auth_response = YLeaf(YType.uint32, "total-test-auth-response")

                    self.total_test_auth_timeouts = YLeaf(YType.uint32, "total-test-auth-timeouts")

                    self.unknown_access_types = YLeaf(YType.uint32, "unknown-access-types")

                    self.unknown_accounting_types = YLeaf(YType.uint32, "unknown-accounting-types")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("aborts",
                                    "access_accepts",
                                    "access_challenges",
                                    "access_rejects",
                                    "access_request_retransmits",
                                    "access_requests",
                                    "access_timeouts",
                                    "accounting_port",
                                    "accounting_requests",
                                    "accounting_responses",
                                    "accounting_retransmits",
                                    "accounting_rtt",
                                    "accounting_timeouts",
                                    "acct_incorrect_responses",
                                    "acct_port_number",
                                    "acct_response_time",
                                    "acct_server_error_responses",
                                    "acct_transaction_failure",
                                    "acct_transaction_successess",
                                    "acct_unexpected_responses",
                                    "auth_port_number",
                                    "authen_incorrect_responses",
                                    "authen_response_time",
                                    "authen_server_error_responses",
                                    "authen_transaction_failure",
                                    "authen_transaction_successess",
                                    "authen_unexpected_responses",
                                    "authentication_port",
                                    "authentication_rtt",
                                    "author_incorrect_responses",
                                    "author_request_timeouts",
                                    "author_requests",
                                    "author_response_time",
                                    "author_server_error_responses",
                                    "author_transaction_failure",
                                    "author_transaction_successess",
                                    "author_unexpected_responses",
                                    "bad_access_authenticators",
                                    "bad_access_responses",
                                    "bad_accounting_authenticators",
                                    "bad_accounting_responses",
                                    "current_state_duration",
                                    "currently_throttled_access_reqs",
                                    "dead_detect_time",
                                    "dead_detect_tries",
                                    "dead_time",
                                    "dropped_access_responses",
                                    "dropped_accounting_responses",
                                    "family",
                                    "group_name",
                                    "ip_address",
                                    "ip_address_xr",
                                    "ipv4_address",
                                    "is_a_private_server",
                                    "is_quarantined",
                                    "last_deadtime",
                                    "max_acct_throttled",
                                    "max_throttled_access_reqs",
                                    "packets_in",
                                    "packets_out",
                                    "pending_access_requests",
                                    "pending_accounting_requets",
                                    "previous_state_duration",
                                    "priority",
                                    "redirected_requests",
                                    "replies_expected",
                                    "retransmit",
                                    "state",
                                    "throttled_access_reqs",
                                    "throttled_acct_failures_stats",
                                    "throttled_acct_timed_out_stats",
                                    "throttled_acct_transactions",
                                    "throttled_dropped_reqs",
                                    "throttled_timed_out_reqs",
                                    "throttleda_acct_transactions",
                                    "timeout_xr",
                                    "timeouts",
                                    "total_deadtime",
                                    "total_test_acct_pending",
                                    "total_test_acct_reqs",
                                    "total_test_acct_response",
                                    "total_test_acct_timeouts",
                                    "total_test_auth_pending",
                                    "total_test_auth_reqs",
                                    "total_test_auth_response",
                                    "total_test_auth_timeouts",
                                    "unknown_access_types",
                                    "unknown_accounting_types") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Radius.Servers.Server, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Radius.Servers.Server, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.aborts.is_set or
                        self.access_accepts.is_set or
                        self.access_challenges.is_set or
                        self.access_rejects.is_set or
                        self.access_request_retransmits.is_set or
                        self.access_requests.is_set or
                        self.access_timeouts.is_set or
                        self.accounting_port.is_set or
                        self.accounting_requests.is_set or
                        self.accounting_responses.is_set or
                        self.accounting_retransmits.is_set or
                        self.accounting_rtt.is_set or
                        self.accounting_timeouts.is_set or
                        self.acct_incorrect_responses.is_set or
                        self.acct_port_number.is_set or
                        self.acct_response_time.is_set or
                        self.acct_server_error_responses.is_set or
                        self.acct_transaction_failure.is_set or
                        self.acct_transaction_successess.is_set or
                        self.acct_unexpected_responses.is_set or
                        self.auth_port_number.is_set or
                        self.authen_incorrect_responses.is_set or
                        self.authen_response_time.is_set or
                        self.authen_server_error_responses.is_set or
                        self.authen_transaction_failure.is_set or
                        self.authen_transaction_successess.is_set or
                        self.authen_unexpected_responses.is_set or
                        self.authentication_port.is_set or
                        self.authentication_rtt.is_set or
                        self.author_incorrect_responses.is_set or
                        self.author_request_timeouts.is_set or
                        self.author_requests.is_set or
                        self.author_response_time.is_set or
                        self.author_server_error_responses.is_set or
                        self.author_transaction_failure.is_set or
                        self.author_transaction_successess.is_set or
                        self.author_unexpected_responses.is_set or
                        self.bad_access_authenticators.is_set or
                        self.bad_access_responses.is_set or
                        self.bad_accounting_authenticators.is_set or
                        self.bad_accounting_responses.is_set or
                        self.current_state_duration.is_set or
                        self.currently_throttled_access_reqs.is_set or
                        self.dead_detect_time.is_set or
                        self.dead_detect_tries.is_set or
                        self.dead_time.is_set or
                        self.dropped_access_responses.is_set or
                        self.dropped_accounting_responses.is_set or
                        self.family.is_set or
                        self.group_name.is_set or
                        self.ip_address.is_set or
                        self.ip_address_xr.is_set or
                        self.ipv4_address.is_set or
                        self.is_a_private_server.is_set or
                        self.is_quarantined.is_set or
                        self.last_deadtime.is_set or
                        self.max_acct_throttled.is_set or
                        self.max_throttled_access_reqs.is_set or
                        self.packets_in.is_set or
                        self.packets_out.is_set or
                        self.pending_access_requests.is_set or
                        self.pending_accounting_requets.is_set or
                        self.previous_state_duration.is_set or
                        self.priority.is_set or
                        self.redirected_requests.is_set or
                        self.replies_expected.is_set or
                        self.retransmit.is_set or
                        self.state.is_set or
                        self.throttled_access_reqs.is_set or
                        self.throttled_acct_failures_stats.is_set or
                        self.throttled_acct_timed_out_stats.is_set or
                        self.throttled_acct_transactions.is_set or
                        self.throttled_dropped_reqs.is_set or
                        self.throttled_timed_out_reqs.is_set or
                        self.throttleda_acct_transactions.is_set or
                        self.timeout_xr.is_set or
                        self.timeouts.is_set or
                        self.total_deadtime.is_set or
                        self.total_test_acct_pending.is_set or
                        self.total_test_acct_reqs.is_set or
                        self.total_test_acct_response.is_set or
                        self.total_test_acct_timeouts.is_set or
                        self.total_test_auth_pending.is_set or
                        self.total_test_auth_reqs.is_set or
                        self.total_test_auth_response.is_set or
                        self.total_test_auth_timeouts.is_set or
                        self.unknown_access_types.is_set or
                        self.unknown_accounting_types.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.aborts.yfilter != YFilter.not_set or
                        self.access_accepts.yfilter != YFilter.not_set or
                        self.access_challenges.yfilter != YFilter.not_set or
                        self.access_rejects.yfilter != YFilter.not_set or
                        self.access_request_retransmits.yfilter != YFilter.not_set or
                        self.access_requests.yfilter != YFilter.not_set or
                        self.access_timeouts.yfilter != YFilter.not_set or
                        self.accounting_port.yfilter != YFilter.not_set or
                        self.accounting_requests.yfilter != YFilter.not_set or
                        self.accounting_responses.yfilter != YFilter.not_set or
                        self.accounting_retransmits.yfilter != YFilter.not_set or
                        self.accounting_rtt.yfilter != YFilter.not_set or
                        self.accounting_timeouts.yfilter != YFilter.not_set or
                        self.acct_incorrect_responses.yfilter != YFilter.not_set or
                        self.acct_port_number.yfilter != YFilter.not_set or
                        self.acct_response_time.yfilter != YFilter.not_set or
                        self.acct_server_error_responses.yfilter != YFilter.not_set or
                        self.acct_transaction_failure.yfilter != YFilter.not_set or
                        self.acct_transaction_successess.yfilter != YFilter.not_set or
                        self.acct_unexpected_responses.yfilter != YFilter.not_set or
                        self.auth_port_number.yfilter != YFilter.not_set or
                        self.authen_incorrect_responses.yfilter != YFilter.not_set or
                        self.authen_response_time.yfilter != YFilter.not_set or
                        self.authen_server_error_responses.yfilter != YFilter.not_set or
                        self.authen_transaction_failure.yfilter != YFilter.not_set or
                        self.authen_transaction_successess.yfilter != YFilter.not_set or
                        self.authen_unexpected_responses.yfilter != YFilter.not_set or
                        self.authentication_port.yfilter != YFilter.not_set or
                        self.authentication_rtt.yfilter != YFilter.not_set or
                        self.author_incorrect_responses.yfilter != YFilter.not_set or
                        self.author_request_timeouts.yfilter != YFilter.not_set or
                        self.author_requests.yfilter != YFilter.not_set or
                        self.author_response_time.yfilter != YFilter.not_set or
                        self.author_server_error_responses.yfilter != YFilter.not_set or
                        self.author_transaction_failure.yfilter != YFilter.not_set or
                        self.author_transaction_successess.yfilter != YFilter.not_set or
                        self.author_unexpected_responses.yfilter != YFilter.not_set or
                        self.bad_access_authenticators.yfilter != YFilter.not_set or
                        self.bad_access_responses.yfilter != YFilter.not_set or
                        self.bad_accounting_authenticators.yfilter != YFilter.not_set or
                        self.bad_accounting_responses.yfilter != YFilter.not_set or
                        self.current_state_duration.yfilter != YFilter.not_set or
                        self.currently_throttled_access_reqs.yfilter != YFilter.not_set or
                        self.dead_detect_time.yfilter != YFilter.not_set or
                        self.dead_detect_tries.yfilter != YFilter.not_set or
                        self.dead_time.yfilter != YFilter.not_set or
                        self.dropped_access_responses.yfilter != YFilter.not_set or
                        self.dropped_accounting_responses.yfilter != YFilter.not_set or
                        self.family.yfilter != YFilter.not_set or
                        self.group_name.yfilter != YFilter.not_set or
                        self.ip_address.yfilter != YFilter.not_set or
                        self.ip_address_xr.yfilter != YFilter.not_set or
                        self.ipv4_address.yfilter != YFilter.not_set or
                        self.is_a_private_server.yfilter != YFilter.not_set or
                        self.is_quarantined.yfilter != YFilter.not_set or
                        self.last_deadtime.yfilter != YFilter.not_set or
                        self.max_acct_throttled.yfilter != YFilter.not_set or
                        self.max_throttled_access_reqs.yfilter != YFilter.not_set or
                        self.packets_in.yfilter != YFilter.not_set or
                        self.packets_out.yfilter != YFilter.not_set or
                        self.pending_access_requests.yfilter != YFilter.not_set or
                        self.pending_accounting_requets.yfilter != YFilter.not_set or
                        self.previous_state_duration.yfilter != YFilter.not_set or
                        self.priority.yfilter != YFilter.not_set or
                        self.redirected_requests.yfilter != YFilter.not_set or
                        self.replies_expected.yfilter != YFilter.not_set or
                        self.retransmit.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.throttled_access_reqs.yfilter != YFilter.not_set or
                        self.throttled_acct_failures_stats.yfilter != YFilter.not_set or
                        self.throttled_acct_timed_out_stats.yfilter != YFilter.not_set or
                        self.throttled_acct_transactions.yfilter != YFilter.not_set or
                        self.throttled_dropped_reqs.yfilter != YFilter.not_set or
                        self.throttled_timed_out_reqs.yfilter != YFilter.not_set or
                        self.throttleda_acct_transactions.yfilter != YFilter.not_set or
                        self.timeout_xr.yfilter != YFilter.not_set or
                        self.timeouts.yfilter != YFilter.not_set or
                        self.total_deadtime.yfilter != YFilter.not_set or
                        self.total_test_acct_pending.yfilter != YFilter.not_set or
                        self.total_test_acct_reqs.yfilter != YFilter.not_set or
                        self.total_test_acct_response.yfilter != YFilter.not_set or
                        self.total_test_acct_timeouts.yfilter != YFilter.not_set or
                        self.total_test_auth_pending.yfilter != YFilter.not_set or
                        self.total_test_auth_reqs.yfilter != YFilter.not_set or
                        self.total_test_auth_response.yfilter != YFilter.not_set or
                        self.total_test_auth_timeouts.yfilter != YFilter.not_set or
                        self.unknown_access_types.yfilter != YFilter.not_set or
                        self.unknown_accounting_types.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/servers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.aborts.is_set or self.aborts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aborts.get_name_leafdata())
                    if (self.access_accepts.is_set or self.access_accepts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_accepts.get_name_leafdata())
                    if (self.access_challenges.is_set or self.access_challenges.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_challenges.get_name_leafdata())
                    if (self.access_rejects.is_set or self.access_rejects.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_rejects.get_name_leafdata())
                    if (self.access_request_retransmits.is_set or self.access_request_retransmits.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_request_retransmits.get_name_leafdata())
                    if (self.access_requests.is_set or self.access_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_requests.get_name_leafdata())
                    if (self.access_timeouts.is_set or self.access_timeouts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.access_timeouts.get_name_leafdata())
                    if (self.accounting_port.is_set or self.accounting_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_port.get_name_leafdata())
                    if (self.accounting_requests.is_set or self.accounting_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_requests.get_name_leafdata())
                    if (self.accounting_responses.is_set or self.accounting_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_responses.get_name_leafdata())
                    if (self.accounting_retransmits.is_set or self.accounting_retransmits.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_retransmits.get_name_leafdata())
                    if (self.accounting_rtt.is_set or self.accounting_rtt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_rtt.get_name_leafdata())
                    if (self.accounting_timeouts.is_set or self.accounting_timeouts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.accounting_timeouts.get_name_leafdata())
                    if (self.acct_incorrect_responses.is_set or self.acct_incorrect_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_incorrect_responses.get_name_leafdata())
                    if (self.acct_port_number.is_set or self.acct_port_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_port_number.get_name_leafdata())
                    if (self.acct_response_time.is_set or self.acct_response_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_response_time.get_name_leafdata())
                    if (self.acct_server_error_responses.is_set or self.acct_server_error_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_server_error_responses.get_name_leafdata())
                    if (self.acct_transaction_failure.is_set or self.acct_transaction_failure.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_transaction_failure.get_name_leafdata())
                    if (self.acct_transaction_successess.is_set or self.acct_transaction_successess.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_transaction_successess.get_name_leafdata())
                    if (self.acct_unexpected_responses.is_set or self.acct_unexpected_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.acct_unexpected_responses.get_name_leafdata())
                    if (self.auth_port_number.is_set or self.auth_port_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.auth_port_number.get_name_leafdata())
                    if (self.authen_incorrect_responses.is_set or self.authen_incorrect_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_incorrect_responses.get_name_leafdata())
                    if (self.authen_response_time.is_set or self.authen_response_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_response_time.get_name_leafdata())
                    if (self.authen_server_error_responses.is_set or self.authen_server_error_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_server_error_responses.get_name_leafdata())
                    if (self.authen_transaction_failure.is_set or self.authen_transaction_failure.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_transaction_failure.get_name_leafdata())
                    if (self.authen_transaction_successess.is_set or self.authen_transaction_successess.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_transaction_successess.get_name_leafdata())
                    if (self.authen_unexpected_responses.is_set or self.authen_unexpected_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_unexpected_responses.get_name_leafdata())
                    if (self.authentication_port.is_set or self.authentication_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_port.get_name_leafdata())
                    if (self.authentication_rtt.is_set or self.authentication_rtt.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authentication_rtt.get_name_leafdata())
                    if (self.author_incorrect_responses.is_set or self.author_incorrect_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_incorrect_responses.get_name_leafdata())
                    if (self.author_request_timeouts.is_set or self.author_request_timeouts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_request_timeouts.get_name_leafdata())
                    if (self.author_requests.is_set or self.author_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_requests.get_name_leafdata())
                    if (self.author_response_time.is_set or self.author_response_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_response_time.get_name_leafdata())
                    if (self.author_server_error_responses.is_set or self.author_server_error_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_server_error_responses.get_name_leafdata())
                    if (self.author_transaction_failure.is_set or self.author_transaction_failure.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_transaction_failure.get_name_leafdata())
                    if (self.author_transaction_successess.is_set or self.author_transaction_successess.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_transaction_successess.get_name_leafdata())
                    if (self.author_unexpected_responses.is_set or self.author_unexpected_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.author_unexpected_responses.get_name_leafdata())
                    if (self.bad_access_authenticators.is_set or self.bad_access_authenticators.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bad_access_authenticators.get_name_leafdata())
                    if (self.bad_access_responses.is_set or self.bad_access_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bad_access_responses.get_name_leafdata())
                    if (self.bad_accounting_authenticators.is_set or self.bad_accounting_authenticators.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bad_accounting_authenticators.get_name_leafdata())
                    if (self.bad_accounting_responses.is_set or self.bad_accounting_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bad_accounting_responses.get_name_leafdata())
                    if (self.current_state_duration.is_set or self.current_state_duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.current_state_duration.get_name_leafdata())
                    if (self.currently_throttled_access_reqs.is_set or self.currently_throttled_access_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.currently_throttled_access_reqs.get_name_leafdata())
                    if (self.dead_detect_time.is_set or self.dead_detect_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dead_detect_time.get_name_leafdata())
                    if (self.dead_detect_tries.is_set or self.dead_detect_tries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dead_detect_tries.get_name_leafdata())
                    if (self.dead_time.is_set or self.dead_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dead_time.get_name_leafdata())
                    if (self.dropped_access_responses.is_set or self.dropped_access_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped_access_responses.get_name_leafdata())
                    if (self.dropped_accounting_responses.is_set or self.dropped_accounting_responses.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dropped_accounting_responses.get_name_leafdata())
                    if (self.family.is_set or self.family.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.family.get_name_leafdata())
                    if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_name.get_name_leafdata())
                    if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address.get_name_leafdata())
                    if (self.ip_address_xr.is_set or self.ip_address_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ip_address_xr.get_name_leafdata())
                    if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                    if (self.is_a_private_server.is_set or self.is_a_private_server.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_a_private_server.get_name_leafdata())
                    if (self.is_quarantined.is_set or self.is_quarantined.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_quarantined.get_name_leafdata())
                    if (self.last_deadtime.is_set or self.last_deadtime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_deadtime.get_name_leafdata())
                    if (self.max_acct_throttled.is_set or self.max_acct_throttled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_acct_throttled.get_name_leafdata())
                    if (self.max_throttled_access_reqs.is_set or self.max_throttled_access_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_throttled_access_reqs.get_name_leafdata())
                    if (self.packets_in.is_set or self.packets_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets_in.get_name_leafdata())
                    if (self.packets_out.is_set or self.packets_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets_out.get_name_leafdata())
                    if (self.pending_access_requests.is_set or self.pending_access_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pending_access_requests.get_name_leafdata())
                    if (self.pending_accounting_requets.is_set or self.pending_accounting_requets.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pending_accounting_requets.get_name_leafdata())
                    if (self.previous_state_duration.is_set or self.previous_state_duration.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.previous_state_duration.get_name_leafdata())
                    if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority.get_name_leafdata())
                    if (self.redirected_requests.is_set or self.redirected_requests.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.redirected_requests.get_name_leafdata())
                    if (self.replies_expected.is_set or self.replies_expected.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.replies_expected.get_name_leafdata())
                    if (self.retransmit.is_set or self.retransmit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.retransmit.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.throttled_access_reqs.is_set or self.throttled_access_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_access_reqs.get_name_leafdata())
                    if (self.throttled_acct_failures_stats.is_set or self.throttled_acct_failures_stats.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_acct_failures_stats.get_name_leafdata())
                    if (self.throttled_acct_timed_out_stats.is_set or self.throttled_acct_timed_out_stats.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_acct_timed_out_stats.get_name_leafdata())
                    if (self.throttled_acct_transactions.is_set or self.throttled_acct_transactions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_acct_transactions.get_name_leafdata())
                    if (self.throttled_dropped_reqs.is_set or self.throttled_dropped_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_dropped_reqs.get_name_leafdata())
                    if (self.throttled_timed_out_reqs.is_set or self.throttled_timed_out_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttled_timed_out_reqs.get_name_leafdata())
                    if (self.throttleda_acct_transactions.is_set or self.throttleda_acct_transactions.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.throttleda_acct_transactions.get_name_leafdata())
                    if (self.timeout_xr.is_set or self.timeout_xr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout_xr.get_name_leafdata())
                    if (self.timeouts.is_set or self.timeouts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeouts.get_name_leafdata())
                    if (self.total_deadtime.is_set or self.total_deadtime.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_deadtime.get_name_leafdata())
                    if (self.total_test_acct_pending.is_set or self.total_test_acct_pending.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_acct_pending.get_name_leafdata())
                    if (self.total_test_acct_reqs.is_set or self.total_test_acct_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_acct_reqs.get_name_leafdata())
                    if (self.total_test_acct_response.is_set or self.total_test_acct_response.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_acct_response.get_name_leafdata())
                    if (self.total_test_acct_timeouts.is_set or self.total_test_acct_timeouts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_acct_timeouts.get_name_leafdata())
                    if (self.total_test_auth_pending.is_set or self.total_test_auth_pending.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_auth_pending.get_name_leafdata())
                    if (self.total_test_auth_reqs.is_set or self.total_test_auth_reqs.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_auth_reqs.get_name_leafdata())
                    if (self.total_test_auth_response.is_set or self.total_test_auth_response.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_auth_response.get_name_leafdata())
                    if (self.total_test_auth_timeouts.is_set or self.total_test_auth_timeouts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_test_auth_timeouts.get_name_leafdata())
                    if (self.unknown_access_types.is_set or self.unknown_access_types.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown_access_types.get_name_leafdata())
                    if (self.unknown_accounting_types.is_set or self.unknown_accounting_types.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.unknown_accounting_types.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aborts" or name == "access-accepts" or name == "access-challenges" or name == "access-rejects" or name == "access-request-retransmits" or name == "access-requests" or name == "access-timeouts" or name == "accounting-port" or name == "accounting-requests" or name == "accounting-responses" or name == "accounting-retransmits" or name == "accounting-rtt" or name == "accounting-timeouts" or name == "acct-incorrect-responses" or name == "acct-port-number" or name == "acct-response-time" or name == "acct-server-error-responses" or name == "acct-transaction-failure" or name == "acct-transaction-successess" or name == "acct-unexpected-responses" or name == "auth-port-number" or name == "authen-incorrect-responses" or name == "authen-response-time" or name == "authen-server-error-responses" or name == "authen-transaction-failure" or name == "authen-transaction-successess" or name == "authen-unexpected-responses" or name == "authentication-port" or name == "authentication-rtt" or name == "author-incorrect-responses" or name == "author-request-timeouts" or name == "author-requests" or name == "author-response-time" or name == "author-server-error-responses" or name == "author-transaction-failure" or name == "author-transaction-successess" or name == "author-unexpected-responses" or name == "bad-access-authenticators" or name == "bad-access-responses" or name == "bad-accounting-authenticators" or name == "bad-accounting-responses" or name == "current-state-duration" or name == "currently-throttled-access-reqs" or name == "dead-detect-time" or name == "dead-detect-tries" or name == "dead-time" or name == "dropped-access-responses" or name == "dropped-accounting-responses" or name == "family" or name == "group-name" or name == "ip-address" or name == "ip-address-xr" or name == "ipv4-address" or name == "is-a-private-server" or name == "is-quarantined" or name == "last-deadtime" or name == "max-acct-throttled" or name == "max-throttled-access-reqs" or name == "packets-in" or name == "packets-out" or name == "pending-access-requests" or name == "pending-accounting-requets" or name == "previous-state-duration" or name == "priority" or name == "redirected-requests" or name == "replies-expected" or name == "retransmit" or name == "state" or name == "throttled-access-reqs" or name == "throttled-acct-failures-stats" or name == "throttled-acct-timed-out-stats" or name == "throttled-acct-transactions" or name == "throttled-dropped-reqs" or name == "throttled-timed-out-reqs" or name == "throttleda-acct-transactions" or name == "timeout-xr" or name == "timeouts" or name == "total-deadtime" or name == "total-test-acct-pending" or name == "total-test-acct-reqs" or name == "total-test-acct-response" or name == "total-test-acct-timeouts" or name == "total-test-auth-pending" or name == "total-test-auth-reqs" or name == "total-test-auth-response" or name == "total-test-auth-timeouts" or name == "unknown-access-types" or name == "unknown-accounting-types"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "aborts"):
                        self.aborts = value
                        self.aborts.value_namespace = name_space
                        self.aborts.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-accepts"):
                        self.access_accepts = value
                        self.access_accepts.value_namespace = name_space
                        self.access_accepts.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-challenges"):
                        self.access_challenges = value
                        self.access_challenges.value_namespace = name_space
                        self.access_challenges.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-rejects"):
                        self.access_rejects = value
                        self.access_rejects.value_namespace = name_space
                        self.access_rejects.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-request-retransmits"):
                        self.access_request_retransmits = value
                        self.access_request_retransmits.value_namespace = name_space
                        self.access_request_retransmits.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-requests"):
                        self.access_requests = value
                        self.access_requests.value_namespace = name_space
                        self.access_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "access-timeouts"):
                        self.access_timeouts = value
                        self.access_timeouts.value_namespace = name_space
                        self.access_timeouts.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-port"):
                        self.accounting_port = value
                        self.accounting_port.value_namespace = name_space
                        self.accounting_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-requests"):
                        self.accounting_requests = value
                        self.accounting_requests.value_namespace = name_space
                        self.accounting_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-responses"):
                        self.accounting_responses = value
                        self.accounting_responses.value_namespace = name_space
                        self.accounting_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-retransmits"):
                        self.accounting_retransmits = value
                        self.accounting_retransmits.value_namespace = name_space
                        self.accounting_retransmits.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-rtt"):
                        self.accounting_rtt = value
                        self.accounting_rtt.value_namespace = name_space
                        self.accounting_rtt.value_namespace_prefix = name_space_prefix
                    if(value_path == "accounting-timeouts"):
                        self.accounting_timeouts = value
                        self.accounting_timeouts.value_namespace = name_space
                        self.accounting_timeouts.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-incorrect-responses"):
                        self.acct_incorrect_responses = value
                        self.acct_incorrect_responses.value_namespace = name_space
                        self.acct_incorrect_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-port-number"):
                        self.acct_port_number = value
                        self.acct_port_number.value_namespace = name_space
                        self.acct_port_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-response-time"):
                        self.acct_response_time = value
                        self.acct_response_time.value_namespace = name_space
                        self.acct_response_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-server-error-responses"):
                        self.acct_server_error_responses = value
                        self.acct_server_error_responses.value_namespace = name_space
                        self.acct_server_error_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-transaction-failure"):
                        self.acct_transaction_failure = value
                        self.acct_transaction_failure.value_namespace = name_space
                        self.acct_transaction_failure.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-transaction-successess"):
                        self.acct_transaction_successess = value
                        self.acct_transaction_successess.value_namespace = name_space
                        self.acct_transaction_successess.value_namespace_prefix = name_space_prefix
                    if(value_path == "acct-unexpected-responses"):
                        self.acct_unexpected_responses = value
                        self.acct_unexpected_responses.value_namespace = name_space
                        self.acct_unexpected_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "auth-port-number"):
                        self.auth_port_number = value
                        self.auth_port_number.value_namespace = name_space
                        self.auth_port_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "authen-incorrect-responses"):
                        self.authen_incorrect_responses = value
                        self.authen_incorrect_responses.value_namespace = name_space
                        self.authen_incorrect_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "authen-response-time"):
                        self.authen_response_time = value
                        self.authen_response_time.value_namespace = name_space
                        self.authen_response_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "authen-server-error-responses"):
                        self.authen_server_error_responses = value
                        self.authen_server_error_responses.value_namespace = name_space
                        self.authen_server_error_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "authen-transaction-failure"):
                        self.authen_transaction_failure = value
                        self.authen_transaction_failure.value_namespace = name_space
                        self.authen_transaction_failure.value_namespace_prefix = name_space_prefix
                    if(value_path == "authen-transaction-successess"):
                        self.authen_transaction_successess = value
                        self.authen_transaction_successess.value_namespace = name_space
                        self.authen_transaction_successess.value_namespace_prefix = name_space_prefix
                    if(value_path == "authen-unexpected-responses"):
                        self.authen_unexpected_responses = value
                        self.authen_unexpected_responses.value_namespace = name_space
                        self.authen_unexpected_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-port"):
                        self.authentication_port = value
                        self.authentication_port.value_namespace = name_space
                        self.authentication_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "authentication-rtt"):
                        self.authentication_rtt = value
                        self.authentication_rtt.value_namespace = name_space
                        self.authentication_rtt.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-incorrect-responses"):
                        self.author_incorrect_responses = value
                        self.author_incorrect_responses.value_namespace = name_space
                        self.author_incorrect_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-request-timeouts"):
                        self.author_request_timeouts = value
                        self.author_request_timeouts.value_namespace = name_space
                        self.author_request_timeouts.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-requests"):
                        self.author_requests = value
                        self.author_requests.value_namespace = name_space
                        self.author_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-response-time"):
                        self.author_response_time = value
                        self.author_response_time.value_namespace = name_space
                        self.author_response_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-server-error-responses"):
                        self.author_server_error_responses = value
                        self.author_server_error_responses.value_namespace = name_space
                        self.author_server_error_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-transaction-failure"):
                        self.author_transaction_failure = value
                        self.author_transaction_failure.value_namespace = name_space
                        self.author_transaction_failure.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-transaction-successess"):
                        self.author_transaction_successess = value
                        self.author_transaction_successess.value_namespace = name_space
                        self.author_transaction_successess.value_namespace_prefix = name_space_prefix
                    if(value_path == "author-unexpected-responses"):
                        self.author_unexpected_responses = value
                        self.author_unexpected_responses.value_namespace = name_space
                        self.author_unexpected_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "bad-access-authenticators"):
                        self.bad_access_authenticators = value
                        self.bad_access_authenticators.value_namespace = name_space
                        self.bad_access_authenticators.value_namespace_prefix = name_space_prefix
                    if(value_path == "bad-access-responses"):
                        self.bad_access_responses = value
                        self.bad_access_responses.value_namespace = name_space
                        self.bad_access_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "bad-accounting-authenticators"):
                        self.bad_accounting_authenticators = value
                        self.bad_accounting_authenticators.value_namespace = name_space
                        self.bad_accounting_authenticators.value_namespace_prefix = name_space_prefix
                    if(value_path == "bad-accounting-responses"):
                        self.bad_accounting_responses = value
                        self.bad_accounting_responses.value_namespace = name_space
                        self.bad_accounting_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "current-state-duration"):
                        self.current_state_duration = value
                        self.current_state_duration.value_namespace = name_space
                        self.current_state_duration.value_namespace_prefix = name_space_prefix
                    if(value_path == "currently-throttled-access-reqs"):
                        self.currently_throttled_access_reqs = value
                        self.currently_throttled_access_reqs.value_namespace = name_space
                        self.currently_throttled_access_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "dead-detect-time"):
                        self.dead_detect_time = value
                        self.dead_detect_time.value_namespace = name_space
                        self.dead_detect_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "dead-detect-tries"):
                        self.dead_detect_tries = value
                        self.dead_detect_tries.value_namespace = name_space
                        self.dead_detect_tries.value_namespace_prefix = name_space_prefix
                    if(value_path == "dead-time"):
                        self.dead_time = value
                        self.dead_time.value_namespace = name_space
                        self.dead_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped-access-responses"):
                        self.dropped_access_responses = value
                        self.dropped_access_responses.value_namespace = name_space
                        self.dropped_access_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "dropped-accounting-responses"):
                        self.dropped_accounting_responses = value
                        self.dropped_accounting_responses.value_namespace = name_space
                        self.dropped_accounting_responses.value_namespace_prefix = name_space_prefix
                    if(value_path == "family"):
                        self.family = value
                        self.family.value_namespace = name_space
                        self.family.value_namespace_prefix = name_space_prefix
                    if(value_path == "group-name"):
                        self.group_name = value
                        self.group_name.value_namespace = name_space
                        self.group_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address"):
                        self.ip_address = value
                        self.ip_address.value_namespace = name_space
                        self.ip_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "ip-address-xr"):
                        self.ip_address_xr = value
                        self.ip_address_xr.value_namespace = name_space
                        self.ip_address_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-address"):
                        self.ipv4_address = value
                        self.ipv4_address.value_namespace = name_space
                        self.ipv4_address.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-a-private-server"):
                        self.is_a_private_server = value
                        self.is_a_private_server.value_namespace = name_space
                        self.is_a_private_server.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-quarantined"):
                        self.is_quarantined = value
                        self.is_quarantined.value_namespace = name_space
                        self.is_quarantined.value_namespace_prefix = name_space_prefix
                    if(value_path == "last-deadtime"):
                        self.last_deadtime = value
                        self.last_deadtime.value_namespace = name_space
                        self.last_deadtime.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-acct-throttled"):
                        self.max_acct_throttled = value
                        self.max_acct_throttled.value_namespace = name_space
                        self.max_acct_throttled.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-throttled-access-reqs"):
                        self.max_throttled_access_reqs = value
                        self.max_throttled_access_reqs.value_namespace = name_space
                        self.max_throttled_access_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets-in"):
                        self.packets_in = value
                        self.packets_in.value_namespace = name_space
                        self.packets_in.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets-out"):
                        self.packets_out = value
                        self.packets_out.value_namespace = name_space
                        self.packets_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "pending-access-requests"):
                        self.pending_access_requests = value
                        self.pending_access_requests.value_namespace = name_space
                        self.pending_access_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "pending-accounting-requets"):
                        self.pending_accounting_requets = value
                        self.pending_accounting_requets.value_namespace = name_space
                        self.pending_accounting_requets.value_namespace_prefix = name_space_prefix
                    if(value_path == "previous-state-duration"):
                        self.previous_state_duration = value
                        self.previous_state_duration.value_namespace = name_space
                        self.previous_state_duration.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority"):
                        self.priority = value
                        self.priority.value_namespace = name_space
                        self.priority.value_namespace_prefix = name_space_prefix
                    if(value_path == "redirected-requests"):
                        self.redirected_requests = value
                        self.redirected_requests.value_namespace = name_space
                        self.redirected_requests.value_namespace_prefix = name_space_prefix
                    if(value_path == "replies-expected"):
                        self.replies_expected = value
                        self.replies_expected.value_namespace = name_space
                        self.replies_expected.value_namespace_prefix = name_space_prefix
                    if(value_path == "retransmit"):
                        self.retransmit = value
                        self.retransmit.value_namespace = name_space
                        self.retransmit.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-access-reqs"):
                        self.throttled_access_reqs = value
                        self.throttled_access_reqs.value_namespace = name_space
                        self.throttled_access_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-acct-failures-stats"):
                        self.throttled_acct_failures_stats = value
                        self.throttled_acct_failures_stats.value_namespace = name_space
                        self.throttled_acct_failures_stats.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-acct-timed-out-stats"):
                        self.throttled_acct_timed_out_stats = value
                        self.throttled_acct_timed_out_stats.value_namespace = name_space
                        self.throttled_acct_timed_out_stats.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-acct-transactions"):
                        self.throttled_acct_transactions = value
                        self.throttled_acct_transactions.value_namespace = name_space
                        self.throttled_acct_transactions.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-dropped-reqs"):
                        self.throttled_dropped_reqs = value
                        self.throttled_dropped_reqs.value_namespace = name_space
                        self.throttled_dropped_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttled-timed-out-reqs"):
                        self.throttled_timed_out_reqs = value
                        self.throttled_timed_out_reqs.value_namespace = name_space
                        self.throttled_timed_out_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "throttleda-acct-transactions"):
                        self.throttleda_acct_transactions = value
                        self.throttleda_acct_transactions.value_namespace = name_space
                        self.throttleda_acct_transactions.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout-xr"):
                        self.timeout_xr = value
                        self.timeout_xr.value_namespace = name_space
                        self.timeout_xr.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeouts"):
                        self.timeouts = value
                        self.timeouts.value_namespace = name_space
                        self.timeouts.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-deadtime"):
                        self.total_deadtime = value
                        self.total_deadtime.value_namespace = name_space
                        self.total_deadtime.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-acct-pending"):
                        self.total_test_acct_pending = value
                        self.total_test_acct_pending.value_namespace = name_space
                        self.total_test_acct_pending.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-acct-reqs"):
                        self.total_test_acct_reqs = value
                        self.total_test_acct_reqs.value_namespace = name_space
                        self.total_test_acct_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-acct-response"):
                        self.total_test_acct_response = value
                        self.total_test_acct_response.value_namespace = name_space
                        self.total_test_acct_response.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-acct-timeouts"):
                        self.total_test_acct_timeouts = value
                        self.total_test_acct_timeouts.value_namespace = name_space
                        self.total_test_acct_timeouts.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-auth-pending"):
                        self.total_test_auth_pending = value
                        self.total_test_auth_pending.value_namespace = name_space
                        self.total_test_auth_pending.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-auth-reqs"):
                        self.total_test_auth_reqs = value
                        self.total_test_auth_reqs.value_namespace = name_space
                        self.total_test_auth_reqs.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-auth-response"):
                        self.total_test_auth_response = value
                        self.total_test_auth_response.value_namespace = name_space
                        self.total_test_auth_response.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-test-auth-timeouts"):
                        self.total_test_auth_timeouts = value
                        self.total_test_auth_timeouts.value_namespace = name_space
                        self.total_test_auth_timeouts.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown-access-types"):
                        self.unknown_access_types = value
                        self.unknown_access_types.value_namespace = name_space
                        self.unknown_access_types.value_namespace_prefix = name_space_prefix
                    if(value_path == "unknown-accounting-types"):
                        self.unknown_accounting_types = value
                        self.unknown_accounting_types.value_namespace = name_space
                        self.unknown_accounting_types.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.server:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.server:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "servers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "server"):
                    for c in self.server:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Radius.Servers.Server()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.server.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "server"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class RadiusSourceInterface(Entity):
            """
            RADIUS source interfaces
            
            .. attribute:: list_of_source_interface
            
            	List of source interfaces
            	**type**\: list of    :py:class:`ListOfSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.RadiusSourceInterface, self).__init__()

                self.yang_name = "radius-source-interface"
                self.yang_parent_name = "radius"

                self.list_of_source_interface = YList(self)

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
                            super(Aaa.Radius.RadiusSourceInterface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.RadiusSourceInterface, self).__setattr__(name, value)


            class ListOfSourceInterface(Entity):
                """
                List of source interfaces
                
                .. attribute:: interface_name
                
                	Name of the source interface
                	**type**\:  str
                
                .. attribute:: ipaddrv4
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: ipaddrv6
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..46
                
                .. attribute:: vrfid
                
                	VRF Id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface, self).__init__()

                    self.yang_name = "list-of-source-interface"
                    self.yang_parent_name = "radius-source-interface"

                    self.interface_name = YLeaf(YType.str, "interface-name")

                    self.ipaddrv4 = YLeaf(YType.str, "ipaddrv4")

                    self.ipaddrv6 = YLeaf(YType.str, "ipaddrv6")

                    self.vrfid = YLeaf(YType.uint32, "vrfid")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "ipaddrv4",
                                    "ipaddrv6",
                                    "vrfid") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.ipaddrv4.is_set or
                        self.ipaddrv6.is_set or
                        self.vrfid.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.ipaddrv4.yfilter != YFilter.not_set or
                        self.ipaddrv6.yfilter != YFilter.not_set or
                        self.vrfid.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "list-of-source-interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/radius-source-interface/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.ipaddrv4.is_set or self.ipaddrv4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipaddrv4.get_name_leafdata())
                    if (self.ipaddrv6.is_set or self.ipaddrv6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipaddrv6.get_name_leafdata())
                    if (self.vrfid.is_set or self.vrfid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrfid.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface-name" or name == "ipaddrv4" or name == "ipaddrv6" or name == "vrfid"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipaddrv4"):
                        self.ipaddrv4 = value
                        self.ipaddrv4.value_namespace = name_space
                        self.ipaddrv4.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipaddrv6"):
                        self.ipaddrv6 = value
                        self.ipaddrv6.value_namespace = name_space
                        self.ipaddrv6.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrfid"):
                        self.vrfid = value
                        self.vrfid.value_namespace = name_space
                        self.vrfid.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.list_of_source_interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.list_of_source_interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "radius-source-interface" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "list-of-source-interface"):
                    for c in self.list_of_source_interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.list_of_source_interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "list-of-source-interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Global_(Entity):
            """
            RADIUS Client Information
            
            .. attribute:: accounting_nas_id
            
            	NAS\-Identifier of the RADIUSaccounting client
            	**type**\:  str
            
            .. attribute:: authentication_nas_id
            
            	NAS\-Identifier of the RADIUSauthentication client
            	**type**\:  str
            
            .. attribute:: unknown_accounting_response
            
            	Number of RADIUS Accounting\-Responsepackets received from unknownaddresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_authentication_response
            
            	Number of RADIUS Access\-Responsepackets received from unknownaddresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Radius.Global_, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "radius"

                self.accounting_nas_id = YLeaf(YType.str, "accounting-nas-id")

                self.authentication_nas_id = YLeaf(YType.str, "authentication-nas-id")

                self.unknown_accounting_response = YLeaf(YType.uint32, "unknown-accounting-response")

                self.unknown_authentication_response = YLeaf(YType.uint32, "unknown-authentication-response")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("accounting_nas_id",
                                "authentication_nas_id",
                                "unknown_accounting_response",
                                "unknown_authentication_response") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Aaa.Radius.Global_, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Radius.Global_, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.accounting_nas_id.is_set or
                    self.authentication_nas_id.is_set or
                    self.unknown_accounting_response.is_set or
                    self.unknown_authentication_response.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.accounting_nas_id.yfilter != YFilter.not_set or
                    self.authentication_nas_id.yfilter != YFilter.not_set or
                    self.unknown_accounting_response.yfilter != YFilter.not_set or
                    self.unknown_authentication_response.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "global" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.accounting_nas_id.is_set or self.accounting_nas_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.accounting_nas_id.get_name_leafdata())
                if (self.authentication_nas_id.is_set or self.authentication_nas_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.authentication_nas_id.get_name_leafdata())
                if (self.unknown_accounting_response.is_set or self.unknown_accounting_response.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unknown_accounting_response.get_name_leafdata())
                if (self.unknown_authentication_response.is_set or self.unknown_authentication_response.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.unknown_authentication_response.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "accounting-nas-id" or name == "authentication-nas-id" or name == "unknown-accounting-response" or name == "unknown-authentication-response"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "accounting-nas-id"):
                    self.accounting_nas_id = value
                    self.accounting_nas_id.value_namespace = name_space
                    self.accounting_nas_id.value_namespace_prefix = name_space_prefix
                if(value_path == "authentication-nas-id"):
                    self.authentication_nas_id = value
                    self.authentication_nas_id.value_namespace = name_space
                    self.authentication_nas_id.value_namespace_prefix = name_space_prefix
                if(value_path == "unknown-accounting-response"):
                    self.unknown_accounting_response = value
                    self.unknown_accounting_response.value_namespace = name_space
                    self.unknown_accounting_response.value_namespace_prefix = name_space_prefix
                if(value_path == "unknown-authentication-response"):
                    self.unknown_authentication_response = value
                    self.unknown_authentication_response.value_namespace = name_space
                    self.unknown_authentication_response.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.global_ is not None and self.global_.has_data()) or
                (self.radius_source_interface is not None and self.radius_source_interface.has_data()) or
                (self.servers is not None and self.servers.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.global_ is not None and self.global_.has_operation()) or
                (self.radius_source_interface is not None and self.radius_source_interface.has_operation()) or
                (self.servers is not None and self.servers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-protocol-radius-oper:radius" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "global"):
                if (self.global_ is None):
                    self.global_ = Aaa.Radius.Global_()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                return self.global_

            if (child_yang_name == "radius-source-interface"):
                if (self.radius_source_interface is None):
                    self.radius_source_interface = Aaa.Radius.RadiusSourceInterface()
                    self.radius_source_interface.parent = self
                    self._children_name_map["radius_source_interface"] = "radius-source-interface"
                return self.radius_source_interface

            if (child_yang_name == "servers"):
                if (self.servers is None):
                    self.servers = Aaa.Radius.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"
                return self.servers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "global" or name == "radius-source-interface" or name == "servers"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Tacacs(Entity):
        """
        TACACS operational data
        
        .. attribute:: requests
        
        	TACACS Active Request List
        	**type**\:   :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests>`
        
        .. attribute:: server_groups
        
        	TACACS sg Information
        	**type**\:   :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups>`
        
        .. attribute:: servers
        
        	TACACS server Information
        	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers>`
        
        

        """

        _prefix = 'aaa-tacacs-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Tacacs, self).__init__()

            self.yang_name = "tacacs"
            self.yang_parent_name = "aaa"

            self.requests = Aaa.Tacacs.Requests()
            self.requests.parent = self
            self._children_name_map["requests"] = "requests"
            self._children_yang_names.add("requests")

            self.server_groups = Aaa.Tacacs.ServerGroups()
            self.server_groups.parent = self
            self._children_name_map["server_groups"] = "server-groups"
            self._children_yang_names.add("server-groups")

            self.servers = Aaa.Tacacs.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"
            self._children_yang_names.add("servers")


        class Requests(Entity):
            """
            TACACS Active Request List
            
            .. attribute:: request
            
            	request
            	**type**\: list of    :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Requests, self).__init__()

                self.yang_name = "requests"
                self.yang_parent_name = "tacacs"

                self.request = YList(self)

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
                            super(Aaa.Tacacs.Requests, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Tacacs.Requests, self).__setattr__(name, value)


            class Request(Entity):
                """
                request
                
                .. attribute:: tacacs_requestbag
                
                	tacacs requestbag
                	**type**\: list of    :py:class:`TacacsRequestbag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request.TacacsRequestbag>`
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Requests.Request, self).__init__()

                    self.yang_name = "request"
                    self.yang_parent_name = "requests"

                    self.tacacs_requestbag = YList(self)

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
                                super(Aaa.Tacacs.Requests.Request, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Tacacs.Requests.Request, self).__setattr__(name, value)


                class TacacsRequestbag(Entity):
                    """
                    tacacs requestbag
                    
                    .. attribute:: bytes_in
                    
                    	bytes read from socket
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_out
                    
                    	bytes written
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: in_pak_size
                    
                    	size of the packet to be received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_pak_size
                    
                    	size of the packet to be sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pak_type
                    
                    	the type of packet
                    	**type**\:  str
                    
                    .. attribute:: session_id
                    
                    	same as in pkt hdr
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sock
                    
                    	socket number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: time_remaining
                    
                    	time remaining for this request
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Tacacs.Requests.Request.TacacsRequestbag, self).__init__()

                        self.yang_name = "tacacs-requestbag"
                        self.yang_parent_name = "request"

                        self.bytes_in = YLeaf(YType.uint32, "bytes-in")

                        self.bytes_out = YLeaf(YType.uint32, "bytes-out")

                        self.in_pak_size = YLeaf(YType.uint32, "in-pak-size")

                        self.out_pak_size = YLeaf(YType.uint32, "out-pak-size")

                        self.pak_type = YLeaf(YType.str, "pak-type")

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.sock = YLeaf(YType.int32, "sock")

                        self.time_remaining = YLeaf(YType.uint32, "time-remaining")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bytes_in",
                                        "bytes_out",
                                        "in_pak_size",
                                        "out_pak_size",
                                        "pak_type",
                                        "session_id",
                                        "sock",
                                        "time_remaining") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Tacacs.Requests.Request.TacacsRequestbag, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Tacacs.Requests.Request.TacacsRequestbag, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bytes_in.is_set or
                            self.bytes_out.is_set or
                            self.in_pak_size.is_set or
                            self.out_pak_size.is_set or
                            self.pak_type.is_set or
                            self.session_id.is_set or
                            self.sock.is_set or
                            self.time_remaining.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bytes_in.yfilter != YFilter.not_set or
                            self.bytes_out.yfilter != YFilter.not_set or
                            self.in_pak_size.yfilter != YFilter.not_set or
                            self.out_pak_size.yfilter != YFilter.not_set or
                            self.pak_type.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            self.sock.yfilter != YFilter.not_set or
                            self.time_remaining.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "tacacs-requestbag" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/requests/request/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bytes_in.is_set or self.bytes_in.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_in.get_name_leafdata())
                        if (self.bytes_out.is_set or self.bytes_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_out.get_name_leafdata())
                        if (self.in_pak_size.is_set or self.in_pak_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_pak_size.get_name_leafdata())
                        if (self.out_pak_size.is_set or self.out_pak_size.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.out_pak_size.get_name_leafdata())
                        if (self.pak_type.is_set or self.pak_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pak_type.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())
                        if (self.sock.is_set or self.sock.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sock.get_name_leafdata())
                        if (self.time_remaining.is_set or self.time_remaining.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time_remaining.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bytes-in" or name == "bytes-out" or name == "in-pak-size" or name == "out-pak-size" or name == "pak-type" or name == "session-id" or name == "sock" or name == "time-remaining"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bytes-in"):
                            self.bytes_in = value
                            self.bytes_in.value_namespace = name_space
                            self.bytes_in.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-out"):
                            self.bytes_out = value
                            self.bytes_out.value_namespace = name_space
                            self.bytes_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "in-pak-size"):
                            self.in_pak_size = value
                            self.in_pak_size.value_namespace = name_space
                            self.in_pak_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "out-pak-size"):
                            self.out_pak_size = value
                            self.out_pak_size.value_namespace = name_space
                            self.out_pak_size.value_namespace_prefix = name_space_prefix
                        if(value_path == "pak-type"):
                            self.pak_type = value
                            self.pak_type.value_namespace = name_space
                            self.pak_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "sock"):
                            self.sock = value
                            self.sock.value_namespace = name_space
                            self.sock.value_namespace_prefix = name_space_prefix
                        if(value_path == "time-remaining"):
                            self.time_remaining = value
                            self.time_remaining.value_namespace = name_space
                            self.time_remaining.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.tacacs_requestbag:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.tacacs_requestbag:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "request" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/requests/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "tacacs-requestbag"):
                        for c in self.tacacs_requestbag:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Tacacs.Requests.Request.TacacsRequestbag()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.tacacs_requestbag.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "tacacs-requestbag"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                for c in self.request:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.request:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "requests" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "request"):
                    for c in self.request:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Tacacs.Requests.Request()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.request.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "request"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Servers(Entity):
            """
            TACACS server Information
            
            .. attribute:: server
            
            	server
            	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers.Server>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "tacacs"

                self.server = YList(self)

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
                            super(Aaa.Tacacs.Servers, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Tacacs.Servers, self).__setattr__(name, value)


            class Server(Entity):
                """
                server
                
                .. attribute:: aborts
                
                	abort count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: addr
                
                	internet address of T+ server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: addr_buf
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..46
                
                .. attribute:: bytes_in
                
                	# of bytes read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: bytes_out
                
                	# of bytes out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: closes
                
                	socket closes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: conn_up
                
                	is the server connected ?
                	**type**\:  bool
                
                .. attribute:: errors
                
                	error count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: family
                
                	IP address Family
                	**type**\:  str
                
                	**length:** 0..5
                
                .. attribute:: is_private
                
                	is this a private server ?
                	**type**\:  bool
                
                .. attribute:: opens
                
                	socket opens
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_in
                
                	# of incoming packets read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_out
                
                	# of outgoing packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port
                
                	per server port to use
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	# of replies expected to arrive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: single_connect
                
                	is this a single connect server ?
                	**type**\:  bool
                
                .. attribute:: timeout
                
                	per\-server timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up
                
                	is the server UP or down ?
                	**type**\:  bool
                
                .. attribute:: vrf_name
                
                	VRF in which server is reachable
                	**type**\:  str
                
                	**length:** 0..33
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"

                    self.aborts = YLeaf(YType.uint32, "aborts")

                    self.addr = YLeaf(YType.str, "addr")

                    self.addr_buf = YLeaf(YType.str, "addr-buf")

                    self.bytes_in = YLeaf(YType.uint32, "bytes-in")

                    self.bytes_out = YLeaf(YType.uint32, "bytes-out")

                    self.closes = YLeaf(YType.uint32, "closes")

                    self.conn_up = YLeaf(YType.boolean, "conn-up")

                    self.errors = YLeaf(YType.uint32, "errors")

                    self.family = YLeaf(YType.str, "family")

                    self.is_private = YLeaf(YType.boolean, "is-private")

                    self.opens = YLeaf(YType.uint32, "opens")

                    self.paks_in = YLeaf(YType.uint32, "paks-in")

                    self.paks_out = YLeaf(YType.uint32, "paks-out")

                    self.port = YLeaf(YType.uint32, "port")

                    self.replies_expected = YLeaf(YType.uint32, "replies-expected")

                    self.single_connect = YLeaf(YType.boolean, "single-connect")

                    self.timeout = YLeaf(YType.uint32, "timeout")

                    self.up = YLeaf(YType.boolean, "up")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("aborts",
                                    "addr",
                                    "addr_buf",
                                    "bytes_in",
                                    "bytes_out",
                                    "closes",
                                    "conn_up",
                                    "errors",
                                    "family",
                                    "is_private",
                                    "opens",
                                    "paks_in",
                                    "paks_out",
                                    "port",
                                    "replies_expected",
                                    "single_connect",
                                    "timeout",
                                    "up",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Tacacs.Servers.Server, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Tacacs.Servers.Server, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.aborts.is_set or
                        self.addr.is_set or
                        self.addr_buf.is_set or
                        self.bytes_in.is_set or
                        self.bytes_out.is_set or
                        self.closes.is_set or
                        self.conn_up.is_set or
                        self.errors.is_set or
                        self.family.is_set or
                        self.is_private.is_set or
                        self.opens.is_set or
                        self.paks_in.is_set or
                        self.paks_out.is_set or
                        self.port.is_set or
                        self.replies_expected.is_set or
                        self.single_connect.is_set or
                        self.timeout.is_set or
                        self.up.is_set or
                        self.vrf_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.aborts.yfilter != YFilter.not_set or
                        self.addr.yfilter != YFilter.not_set or
                        self.addr_buf.yfilter != YFilter.not_set or
                        self.bytes_in.yfilter != YFilter.not_set or
                        self.bytes_out.yfilter != YFilter.not_set or
                        self.closes.yfilter != YFilter.not_set or
                        self.conn_up.yfilter != YFilter.not_set or
                        self.errors.yfilter != YFilter.not_set or
                        self.family.yfilter != YFilter.not_set or
                        self.is_private.yfilter != YFilter.not_set or
                        self.opens.yfilter != YFilter.not_set or
                        self.paks_in.yfilter != YFilter.not_set or
                        self.paks_out.yfilter != YFilter.not_set or
                        self.port.yfilter != YFilter.not_set or
                        self.replies_expected.yfilter != YFilter.not_set or
                        self.single_connect.yfilter != YFilter.not_set or
                        self.timeout.yfilter != YFilter.not_set or
                        self.up.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/servers/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.aborts.is_set or self.aborts.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.aborts.get_name_leafdata())
                    if (self.addr.is_set or self.addr.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.addr.get_name_leafdata())
                    if (self.addr_buf.is_set or self.addr_buf.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.addr_buf.get_name_leafdata())
                    if (self.bytes_in.is_set or self.bytes_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes_in.get_name_leafdata())
                    if (self.bytes_out.is_set or self.bytes_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.bytes_out.get_name_leafdata())
                    if (self.closes.is_set or self.closes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.closes.get_name_leafdata())
                    if (self.conn_up.is_set or self.conn_up.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.conn_up.get_name_leafdata())
                    if (self.errors.is_set or self.errors.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.errors.get_name_leafdata())
                    if (self.family.is_set or self.family.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.family.get_name_leafdata())
                    if (self.is_private.is_set or self.is_private.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.is_private.get_name_leafdata())
                    if (self.opens.is_set or self.opens.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.opens.get_name_leafdata())
                    if (self.paks_in.is_set or self.paks_in.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.paks_in.get_name_leafdata())
                    if (self.paks_out.is_set or self.paks_out.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.paks_out.get_name_leafdata())
                    if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.port.get_name_leafdata())
                    if (self.replies_expected.is_set or self.replies_expected.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.replies_expected.get_name_leafdata())
                    if (self.single_connect.is_set or self.single_connect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.single_connect.get_name_leafdata())
                    if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.timeout.get_name_leafdata())
                    if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.up.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aborts" or name == "addr" or name == "addr-buf" or name == "bytes-in" or name == "bytes-out" or name == "closes" or name == "conn-up" or name == "errors" or name == "family" or name == "is-private" or name == "opens" or name == "paks-in" or name == "paks-out" or name == "port" or name == "replies-expected" or name == "single-connect" or name == "timeout" or name == "up" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "aborts"):
                        self.aborts = value
                        self.aborts.value_namespace = name_space
                        self.aborts.value_namespace_prefix = name_space_prefix
                    if(value_path == "addr"):
                        self.addr = value
                        self.addr.value_namespace = name_space
                        self.addr.value_namespace_prefix = name_space_prefix
                    if(value_path == "addr-buf"):
                        self.addr_buf = value
                        self.addr_buf.value_namespace = name_space
                        self.addr_buf.value_namespace_prefix = name_space_prefix
                    if(value_path == "bytes-in"):
                        self.bytes_in = value
                        self.bytes_in.value_namespace = name_space
                        self.bytes_in.value_namespace_prefix = name_space_prefix
                    if(value_path == "bytes-out"):
                        self.bytes_out = value
                        self.bytes_out.value_namespace = name_space
                        self.bytes_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "closes"):
                        self.closes = value
                        self.closes.value_namespace = name_space
                        self.closes.value_namespace_prefix = name_space_prefix
                    if(value_path == "conn-up"):
                        self.conn_up = value
                        self.conn_up.value_namespace = name_space
                        self.conn_up.value_namespace_prefix = name_space_prefix
                    if(value_path == "errors"):
                        self.errors = value
                        self.errors.value_namespace = name_space
                        self.errors.value_namespace_prefix = name_space_prefix
                    if(value_path == "family"):
                        self.family = value
                        self.family.value_namespace = name_space
                        self.family.value_namespace_prefix = name_space_prefix
                    if(value_path == "is-private"):
                        self.is_private = value
                        self.is_private.value_namespace = name_space
                        self.is_private.value_namespace_prefix = name_space_prefix
                    if(value_path == "opens"):
                        self.opens = value
                        self.opens.value_namespace = name_space
                        self.opens.value_namespace_prefix = name_space_prefix
                    if(value_path == "paks-in"):
                        self.paks_in = value
                        self.paks_in.value_namespace = name_space
                        self.paks_in.value_namespace_prefix = name_space_prefix
                    if(value_path == "paks-out"):
                        self.paks_out = value
                        self.paks_out.value_namespace = name_space
                        self.paks_out.value_namespace_prefix = name_space_prefix
                    if(value_path == "port"):
                        self.port = value
                        self.port.value_namespace = name_space
                        self.port.value_namespace_prefix = name_space_prefix
                    if(value_path == "replies-expected"):
                        self.replies_expected = value
                        self.replies_expected.value_namespace = name_space
                        self.replies_expected.value_namespace_prefix = name_space_prefix
                    if(value_path == "single-connect"):
                        self.single_connect = value
                        self.single_connect.value_namespace = name_space
                        self.single_connect.value_namespace_prefix = name_space_prefix
                    if(value_path == "timeout"):
                        self.timeout = value
                        self.timeout.value_namespace = name_space
                        self.timeout.value_namespace_prefix = name_space_prefix
                    if(value_path == "up"):
                        self.up = value
                        self.up.value_namespace = name_space
                        self.up.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.server:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.server:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "servers" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "server"):
                    for c in self.server:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Tacacs.Servers.Server()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.server.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "server"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class ServerGroups(Entity):
            """
            TACACS sg Information
            
            .. attribute:: server_group
            
            	server group
            	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.ServerGroups, self).__init__()

                self.yang_name = "server-groups"
                self.yang_parent_name = "tacacs"

                self.server_group = YList(self)

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
                            super(Aaa.Tacacs.ServerGroups, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Aaa.Tacacs.ServerGroups, self).__setattr__(name, value)


            class ServerGroup(Entity):
                """
                server group
                
                .. attribute:: group_name
                
                	name of the server group
                	**type**\:  str
                
                .. attribute:: server
                
                	list of servers in this group
                	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup.Server>`
                
                .. attribute:: sg_map_num
                
                	server group mapped number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	vrf of the group
                	**type**\:  str
                
                	**length:** 0..33
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.ServerGroups.ServerGroup, self).__init__()

                    self.yang_name = "server-group"
                    self.yang_parent_name = "server-groups"

                    self.group_name = YLeaf(YType.str, "group-name")

                    self.sg_map_num = YLeaf(YType.uint32, "sg-map-num")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                    self.server = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("group_name",
                                    "sg_map_num",
                                    "vrf_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Aaa.Tacacs.ServerGroups.ServerGroup, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Aaa.Tacacs.ServerGroups.ServerGroup, self).__setattr__(name, value)


                class Server(Entity):
                    """
                    list of servers in this group
                    
                    .. attribute:: aborts
                    
                    	abort count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: addr
                    
                    	internet address of T+ server
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: addr_buf
                    
                    	IP address buffer
                    	**type**\:  str
                    
                    	**length:** 0..46
                    
                    .. attribute:: bytes_in
                    
                    	# of bytes read
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_out
                    
                    	# of bytes out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: closes
                    
                    	socket closes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: conn_up
                    
                    	is the server connected ?
                    	**type**\:  bool
                    
                    .. attribute:: errors
                    
                    	error count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\:  str
                    
                    	**length:** 0..5
                    
                    .. attribute:: is_private
                    
                    	is this a private server ?
                    	**type**\:  bool
                    
                    .. attribute:: opens
                    
                    	socket opens
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_in
                    
                    	# of incoming packets read
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_out
                    
                    	# of outgoing packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port
                    
                    	per server port to use
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_expected
                    
                    	# of replies expected to arrive
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: single_connect
                    
                    	is this a single connect server ?
                    	**type**\:  bool
                    
                    .. attribute:: timeout
                    
                    	per\-server timeout
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up
                    
                    	is the server UP or down ?
                    	**type**\:  bool
                    
                    .. attribute:: vrf_name
                    
                    	VRF in which server is reachable
                    	**type**\:  str
                    
                    	**length:** 0..33
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Tacacs.ServerGroups.ServerGroup.Server, self).__init__()

                        self.yang_name = "server"
                        self.yang_parent_name = "server-group"

                        self.aborts = YLeaf(YType.uint32, "aborts")

                        self.addr = YLeaf(YType.str, "addr")

                        self.addr_buf = YLeaf(YType.str, "addr-buf")

                        self.bytes_in = YLeaf(YType.uint32, "bytes-in")

                        self.bytes_out = YLeaf(YType.uint32, "bytes-out")

                        self.closes = YLeaf(YType.uint32, "closes")

                        self.conn_up = YLeaf(YType.boolean, "conn-up")

                        self.errors = YLeaf(YType.uint32, "errors")

                        self.family = YLeaf(YType.str, "family")

                        self.is_private = YLeaf(YType.boolean, "is-private")

                        self.opens = YLeaf(YType.uint32, "opens")

                        self.paks_in = YLeaf(YType.uint32, "paks-in")

                        self.paks_out = YLeaf(YType.uint32, "paks-out")

                        self.port = YLeaf(YType.uint32, "port")

                        self.replies_expected = YLeaf(YType.uint32, "replies-expected")

                        self.single_connect = YLeaf(YType.boolean, "single-connect")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                        self.up = YLeaf(YType.boolean, "up")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("aborts",
                                        "addr",
                                        "addr_buf",
                                        "bytes_in",
                                        "bytes_out",
                                        "closes",
                                        "conn_up",
                                        "errors",
                                        "family",
                                        "is_private",
                                        "opens",
                                        "paks_in",
                                        "paks_out",
                                        "port",
                                        "replies_expected",
                                        "single_connect",
                                        "timeout",
                                        "up",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Aaa.Tacacs.ServerGroups.ServerGroup.Server, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Aaa.Tacacs.ServerGroups.ServerGroup.Server, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.aborts.is_set or
                            self.addr.is_set or
                            self.addr_buf.is_set or
                            self.bytes_in.is_set or
                            self.bytes_out.is_set or
                            self.closes.is_set or
                            self.conn_up.is_set or
                            self.errors.is_set or
                            self.family.is_set or
                            self.is_private.is_set or
                            self.opens.is_set or
                            self.paks_in.is_set or
                            self.paks_out.is_set or
                            self.port.is_set or
                            self.replies_expected.is_set or
                            self.single_connect.is_set or
                            self.timeout.is_set or
                            self.up.is_set or
                            self.vrf_name.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.aborts.yfilter != YFilter.not_set or
                            self.addr.yfilter != YFilter.not_set or
                            self.addr_buf.yfilter != YFilter.not_set or
                            self.bytes_in.yfilter != YFilter.not_set or
                            self.bytes_out.yfilter != YFilter.not_set or
                            self.closes.yfilter != YFilter.not_set or
                            self.conn_up.yfilter != YFilter.not_set or
                            self.errors.yfilter != YFilter.not_set or
                            self.family.yfilter != YFilter.not_set or
                            self.is_private.yfilter != YFilter.not_set or
                            self.opens.yfilter != YFilter.not_set or
                            self.paks_in.yfilter != YFilter.not_set or
                            self.paks_out.yfilter != YFilter.not_set or
                            self.port.yfilter != YFilter.not_set or
                            self.replies_expected.yfilter != YFilter.not_set or
                            self.single_connect.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set or
                            self.up.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "server" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/server-groups/server-group/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.aborts.is_set or self.aborts.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.aborts.get_name_leafdata())
                        if (self.addr.is_set or self.addr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.addr.get_name_leafdata())
                        if (self.addr_buf.is_set or self.addr_buf.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.addr_buf.get_name_leafdata())
                        if (self.bytes_in.is_set or self.bytes_in.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_in.get_name_leafdata())
                        if (self.bytes_out.is_set or self.bytes_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bytes_out.get_name_leafdata())
                        if (self.closes.is_set or self.closes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.closes.get_name_leafdata())
                        if (self.conn_up.is_set or self.conn_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.conn_up.get_name_leafdata())
                        if (self.errors.is_set or self.errors.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.errors.get_name_leafdata())
                        if (self.family.is_set or self.family.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.family.get_name_leafdata())
                        if (self.is_private.is_set or self.is_private.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.is_private.get_name_leafdata())
                        if (self.opens.is_set or self.opens.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.opens.get_name_leafdata())
                        if (self.paks_in.is_set or self.paks_in.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.paks_in.get_name_leafdata())
                        if (self.paks_out.is_set or self.paks_out.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.paks_out.get_name_leafdata())
                        if (self.port.is_set or self.port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.port.get_name_leafdata())
                        if (self.replies_expected.is_set or self.replies_expected.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.replies_expected.get_name_leafdata())
                        if (self.single_connect.is_set or self.single_connect.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.single_connect.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())
                        if (self.up.is_set or self.up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.up.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "aborts" or name == "addr" or name == "addr-buf" or name == "bytes-in" or name == "bytes-out" or name == "closes" or name == "conn-up" or name == "errors" or name == "family" or name == "is-private" or name == "opens" or name == "paks-in" or name == "paks-out" or name == "port" or name == "replies-expected" or name == "single-connect" or name == "timeout" or name == "up" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "aborts"):
                            self.aborts = value
                            self.aborts.value_namespace = name_space
                            self.aborts.value_namespace_prefix = name_space_prefix
                        if(value_path == "addr"):
                            self.addr = value
                            self.addr.value_namespace = name_space
                            self.addr.value_namespace_prefix = name_space_prefix
                        if(value_path == "addr-buf"):
                            self.addr_buf = value
                            self.addr_buf.value_namespace = name_space
                            self.addr_buf.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-in"):
                            self.bytes_in = value
                            self.bytes_in.value_namespace = name_space
                            self.bytes_in.value_namespace_prefix = name_space_prefix
                        if(value_path == "bytes-out"):
                            self.bytes_out = value
                            self.bytes_out.value_namespace = name_space
                            self.bytes_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "closes"):
                            self.closes = value
                            self.closes.value_namespace = name_space
                            self.closes.value_namespace_prefix = name_space_prefix
                        if(value_path == "conn-up"):
                            self.conn_up = value
                            self.conn_up.value_namespace = name_space
                            self.conn_up.value_namespace_prefix = name_space_prefix
                        if(value_path == "errors"):
                            self.errors = value
                            self.errors.value_namespace = name_space
                            self.errors.value_namespace_prefix = name_space_prefix
                        if(value_path == "family"):
                            self.family = value
                            self.family.value_namespace = name_space
                            self.family.value_namespace_prefix = name_space_prefix
                        if(value_path == "is-private"):
                            self.is_private = value
                            self.is_private.value_namespace = name_space
                            self.is_private.value_namespace_prefix = name_space_prefix
                        if(value_path == "opens"):
                            self.opens = value
                            self.opens.value_namespace = name_space
                            self.opens.value_namespace_prefix = name_space_prefix
                        if(value_path == "paks-in"):
                            self.paks_in = value
                            self.paks_in.value_namespace = name_space
                            self.paks_in.value_namespace_prefix = name_space_prefix
                        if(value_path == "paks-out"):
                            self.paks_out = value
                            self.paks_out.value_namespace = name_space
                            self.paks_out.value_namespace_prefix = name_space_prefix
                        if(value_path == "port"):
                            self.port = value
                            self.port.value_namespace = name_space
                            self.port.value_namespace_prefix = name_space_prefix
                        if(value_path == "replies-expected"):
                            self.replies_expected = value
                            self.replies_expected.value_namespace = name_space
                            self.replies_expected.value_namespace_prefix = name_space_prefix
                        if(value_path == "single-connect"):
                            self.single_connect = value
                            self.single_connect.value_namespace = name_space
                            self.single_connect.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix
                        if(value_path == "up"):
                            self.up = value
                            self.up.value_namespace = name_space
                            self.up.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.server:
                        if (c.has_data()):
                            return True
                    return (
                        self.group_name.is_set or
                        self.sg_map_num.is_set or
                        self.vrf_name.is_set)

                def has_operation(self):
                    for c in self.server:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.group_name.yfilter != YFilter.not_set or
                        self.sg_map_num.yfilter != YFilter.not_set or
                        self.vrf_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server-group" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/server-groups/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.group_name.is_set or self.group_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.group_name.get_name_leafdata())
                    if (self.sg_map_num.is_set or self.sg_map_num.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.sg_map_num.get_name_leafdata())
                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "server"):
                        for c in self.server:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Aaa.Tacacs.ServerGroups.ServerGroup.Server()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.server.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "server" or name == "group-name" or name == "sg-map-num" or name == "vrf-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "group-name"):
                        self.group_name = value
                        self.group_name.value_namespace = name_space
                        self.group_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "sg-map-num"):
                        self.sg_map_num = value
                        self.sg_map_num.value_namespace = name_space
                        self.sg_map_num.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-name"):
                        self.vrf_name = value
                        self.vrf_name.value_namespace = name_space
                        self.vrf_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.server_group:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.server_group:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "server-groups" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "server-group"):
                    for c in self.server_group:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = Aaa.Tacacs.ServerGroups.ServerGroup()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.server_group.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "server-group"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.requests is not None and self.requests.has_data()) or
                (self.server_groups is not None and self.server_groups.has_data()) or
                (self.servers is not None and self.servers.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.requests is not None and self.requests.has_operation()) or
                (self.server_groups is not None and self.server_groups.has_operation()) or
                (self.servers is not None and self.servers.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "Cisco-IOS-XR-aaa-tacacs-oper:tacacs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "requests"):
                if (self.requests is None):
                    self.requests = Aaa.Tacacs.Requests()
                    self.requests.parent = self
                    self._children_name_map["requests"] = "requests"
                return self.requests

            if (child_yang_name == "server-groups"):
                if (self.server_groups is None):
                    self.server_groups = Aaa.Tacacs.ServerGroups()
                    self.server_groups.parent = self
                    self._children_name_map["server_groups"] = "server-groups"
                return self.server_groups

            if (child_yang_name == "servers"):
                if (self.servers is None):
                    self.servers = Aaa.Tacacs.Servers()
                    self.servers.parent = self
                    self._children_name_map["servers"] = "servers"
                return self.servers

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "requests" or name == "server-groups" or name == "servers"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.all_tasks is not None and self.all_tasks.has_data()) or
            (self.authen_method is not None and self.authen_method.has_data()) or
            (self.current_usergroup is not None and self.current_usergroup.has_data()) or
            (self.currentuser_detail is not None and self.currentuser_detail.has_data()) or
            (self.diameter is not None and self.diameter.has_data()) or
            (self.radius is not None and self.radius.has_data()) or
            (self.tacacs is not None and self.tacacs.has_data()) or
            (self.task_map is not None and self.task_map.has_data()) or
            (self.taskgroups is not None and self.taskgroups.has_data()) or
            (self.usergroups is not None and self.usergroups.has_data()) or
            (self.users is not None and self.users.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.all_tasks is not None and self.all_tasks.has_operation()) or
            (self.authen_method is not None and self.authen_method.has_operation()) or
            (self.current_usergroup is not None and self.current_usergroup.has_operation()) or
            (self.currentuser_detail is not None and self.currentuser_detail.has_operation()) or
            (self.diameter is not None and self.diameter.has_operation()) or
            (self.radius is not None and self.radius.has_operation()) or
            (self.tacacs is not None and self.tacacs.has_operation()) or
            (self.task_map is not None and self.task_map.has_operation()) or
            (self.taskgroups is not None and self.taskgroups.has_operation()) or
            (self.usergroups is not None and self.usergroups.has_operation()) or
            (self.users is not None and self.users.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-aaa-locald-oper:aaa" + path_buffer

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

        if (child_yang_name == "all-tasks"):
            if (self.all_tasks is None):
                self.all_tasks = Aaa.AllTasks()
                self.all_tasks.parent = self
                self._children_name_map["all_tasks"] = "all-tasks"
            return self.all_tasks

        if (child_yang_name == "authen-method"):
            if (self.authen_method is None):
                self.authen_method = Aaa.AuthenMethod()
                self.authen_method.parent = self
                self._children_name_map["authen_method"] = "authen-method"
            return self.authen_method

        if (child_yang_name == "current-usergroup"):
            if (self.current_usergroup is None):
                self.current_usergroup = Aaa.CurrentUsergroup()
                self.current_usergroup.parent = self
                self._children_name_map["current_usergroup"] = "current-usergroup"
            return self.current_usergroup

        if (child_yang_name == "currentuser-detail"):
            if (self.currentuser_detail is None):
                self.currentuser_detail = Aaa.CurrentuserDetail()
                self.currentuser_detail.parent = self
                self._children_name_map["currentuser_detail"] = "currentuser-detail"
            return self.currentuser_detail

        if (child_yang_name == "diameter"):
            if (self.diameter is None):
                self.diameter = Aaa.Diameter()
                self.diameter.parent = self
                self._children_name_map["diameter"] = "diameter"
            return self.diameter

        if (child_yang_name == "radius"):
            if (self.radius is None):
                self.radius = Aaa.Radius()
                self.radius.parent = self
                self._children_name_map["radius"] = "radius"
            return self.radius

        if (child_yang_name == "tacacs"):
            if (self.tacacs is None):
                self.tacacs = Aaa.Tacacs()
                self.tacacs.parent = self
                self._children_name_map["tacacs"] = "tacacs"
            return self.tacacs

        if (child_yang_name == "task-map"):
            if (self.task_map is None):
                self.task_map = Aaa.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
            return self.task_map

        if (child_yang_name == "taskgroups"):
            if (self.taskgroups is None):
                self.taskgroups = Aaa.Taskgroups()
                self.taskgroups.parent = self
                self._children_name_map["taskgroups"] = "taskgroups"
            return self.taskgroups

        if (child_yang_name == "usergroups"):
            if (self.usergroups is None):
                self.usergroups = Aaa.Usergroups()
                self.usergroups.parent = self
                self._children_name_map["usergroups"] = "usergroups"
            return self.usergroups

        if (child_yang_name == "users"):
            if (self.users is None):
                self.users = Aaa.Users()
                self.users.parent = self
                self._children_name_map["users"] = "users"
            return self.users

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "all-tasks" or name == "authen-method" or name == "current-usergroup" or name == "currentuser-detail" or name == "diameter" or name == "radius" or name == "tacacs" or name == "task-map" or name == "taskgroups" or name == "usergroups" or name == "users"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity

