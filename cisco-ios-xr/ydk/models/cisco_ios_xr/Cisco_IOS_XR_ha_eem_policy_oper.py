""" Cisco_IOS_XR_ha_eem_policy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ha\-eem\-policy package operational data.

This module contains definitions
for the following management objects\:
  eem\: EEM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Eem(Entity):
    """
    EEM operational data
    
    .. attribute:: avl_policies
    
    	list the available policies
    	**type**\:   :py:class:`AvlPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.AvlPolicies>`
    
    .. attribute:: dir_user
    
    	directory user
    	**type**\:   :py:class:`DirUser <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.DirUser>`
    
    .. attribute:: env_variables
    
    	list of environmental variables
    	**type**\:   :py:class:`EnvVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.EnvVariables>`
    
    .. attribute:: refresh_time
    
    	Refresh time
    	**type**\:   :py:class:`RefreshTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.RefreshTime>`
    
    .. attribute:: reg_policies
    
    	list the registered policies
    	**type**\:   :py:class:`RegPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.RegPolicies>`
    
    

    """

    _prefix = 'ha-eem-policy-oper'
    _revision = '2016-02-05'

    def __init__(self):
        super(Eem, self).__init__()
        self._top_entity = None

        self.yang_name = "eem"
        self.yang_parent_name = "Cisco-IOS-XR-ha-eem-policy-oper"

        self.avl_policies = Eem.AvlPolicies()
        self.avl_policies.parent = self
        self._children_name_map["avl_policies"] = "avl-policies"
        self._children_yang_names.add("avl-policies")

        self.dir_user = Eem.DirUser()
        self.dir_user.parent = self
        self._children_name_map["dir_user"] = "dir-user"
        self._children_yang_names.add("dir-user")

        self.env_variables = Eem.EnvVariables()
        self.env_variables.parent = self
        self._children_name_map["env_variables"] = "env-variables"
        self._children_yang_names.add("env-variables")

        self.refresh_time = Eem.RefreshTime()
        self.refresh_time.parent = self
        self._children_name_map["refresh_time"] = "refresh-time"
        self._children_yang_names.add("refresh-time")

        self.reg_policies = Eem.RegPolicies()
        self.reg_policies.parent = self
        self._children_name_map["reg_policies"] = "reg-policies"
        self._children_yang_names.add("reg-policies")


    class DirUser(Entity):
        """
        directory user
        
        .. attribute:: library
        
        	directory user library
        	**type**\:   :py:class:`Library <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.DirUser.Library>`
        
        .. attribute:: policy
        
        	directory user policy
        	**type**\:   :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.DirUser.Policy>`
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.DirUser, self).__init__()

            self.yang_name = "dir-user"
            self.yang_parent_name = "eem"

            self.library = Eem.DirUser.Library()
            self.library.parent = self
            self._children_name_map["library"] = "library"
            self._children_yang_names.add("library")

            self.policy = Eem.DirUser.Policy()
            self.policy.parent = self
            self._children_name_map["policy"] = "policy"
            self._children_yang_names.add("policy")


        class Library(Entity):
            """
            directory user library
            
            .. attribute:: library
            
            	library
            	**type**\:  str
            
            .. attribute:: policy
            
            	policy
            	**type**\:  str
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.DirUser.Library, self).__init__()

                self.yang_name = "library"
                self.yang_parent_name = "dir-user"

                self.library = YLeaf(YType.str, "library")

                self.policy = YLeaf(YType.str, "policy")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("library",
                                "policy") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Eem.DirUser.Library, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Eem.DirUser.Library, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.library.is_set or
                    self.policy.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.library.yfilter != YFilter.not_set or
                    self.policy.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "library" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/dir-user/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.library.is_set or self.library.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.library.get_name_leafdata())
                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "library" or name == "policy"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "library"):
                    self.library = value
                    self.library.value_namespace = name_space
                    self.library.value_namespace_prefix = name_space_prefix
                if(value_path == "policy"):
                    self.policy = value
                    self.policy.value_namespace = name_space
                    self.policy.value_namespace_prefix = name_space_prefix


        class Policy(Entity):
            """
            directory user policy
            
            .. attribute:: library
            
            	library
            	**type**\:  str
            
            .. attribute:: policy
            
            	policy
            	**type**\:  str
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.DirUser.Policy, self).__init__()

                self.yang_name = "policy"
                self.yang_parent_name = "dir-user"

                self.library = YLeaf(YType.str, "library")

                self.policy = YLeaf(YType.str, "policy")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("library",
                                "policy") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Eem.DirUser.Policy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Eem.DirUser.Policy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.library.is_set or
                    self.policy.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.library.yfilter != YFilter.not_set or
                    self.policy.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/dir-user/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.library.is_set or self.library.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.library.get_name_leafdata())
                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "library" or name == "policy"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "library"):
                    self.library = value
                    self.library.value_namespace = name_space
                    self.library.value_namespace_prefix = name_space_prefix
                if(value_path == "policy"):
                    self.policy = value
                    self.policy.value_namespace = name_space
                    self.policy.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                (self.library is not None and self.library.has_data()) or
                (self.policy is not None and self.policy.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.library is not None and self.library.has_operation()) or
                (self.policy is not None and self.policy.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "dir-user" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "library"):
                if (self.library is None):
                    self.library = Eem.DirUser.Library()
                    self.library.parent = self
                    self._children_name_map["library"] = "library"
                return self.library

            if (child_yang_name == "policy"):
                if (self.policy is None):
                    self.policy = Eem.DirUser.Policy()
                    self.policy.parent = self
                    self._children_name_map["policy"] = "policy"
                return self.policy

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "library" or name == "policy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class EnvVariables(Entity):
        """
        list of environmental variables
        
        .. attribute:: env_variable
        
        	environmental variables name and value 
        	**type**\: list of    :py:class:`EnvVariable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.EnvVariables.EnvVariable>`
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.EnvVariables, self).__init__()

            self.yang_name = "env-variables"
            self.yang_parent_name = "eem"

            self.env_variable = YList(self)

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
                        super(Eem.EnvVariables, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Eem.EnvVariables, self).__setattr__(name, value)


        class EnvVariable(Entity):
            """
            environmental variables name and value 
            
            .. attribute:: name  <key>
            
            	Environmental variable name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: name_xr
            
            	variable name
            	**type**\:  str
            
            .. attribute:: value
            
            	value
            	**type**\:  str
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.EnvVariables.EnvVariable, self).__init__()

                self.yang_name = "env-variable"
                self.yang_parent_name = "env-variables"

                self.name = YLeaf(YType.str, "name")

                self.name_xr = YLeaf(YType.str, "name-xr")

                self.value = YLeaf(YType.str, "value")

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
                                "name_xr",
                                "value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Eem.EnvVariables.EnvVariable, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Eem.EnvVariables.EnvVariable, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.name_xr.is_set or
                    self.value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.name_xr.yfilter != YFilter.not_set or
                    self.value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "env-variable" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/env-variables/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.name_xr.is_set or self.name_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name_xr.get_name_leafdata())
                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "name-xr" or name == "value"):
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
                if(value_path == "value"):
                    self.value = value
                    self.value.value_namespace = name_space
                    self.value.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.env_variable:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.env_variable:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "env-variables" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "env-variable"):
                for c in self.env_variable:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Eem.EnvVariables.EnvVariable()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.env_variable.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "env-variable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class RefreshTime(Entity):
        """
        Refresh time
        
        .. attribute:: refreshtime
        
        	Event manager refresh\-time 
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.RefreshTime, self).__init__()

            self.yang_name = "refresh-time"
            self.yang_parent_name = "eem"

            self.refreshtime = YLeaf(YType.uint32, "refreshtime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("refreshtime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Eem.RefreshTime, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Eem.RefreshTime, self).__setattr__(name, value)

        def has_data(self):
            return self.refreshtime.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.refreshtime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "refresh-time" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.refreshtime.is_set or self.refreshtime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.refreshtime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "refreshtime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "refreshtime"):
                self.refreshtime = value
                self.refreshtime.value_namespace = name_space
                self.refreshtime.value_namespace_prefix = name_space_prefix


    class RegPolicies(Entity):
        """
        list the registered policies
        
        .. attribute:: reg_policy
        
        	policy name and create time 
        	**type**\: list of    :py:class:`RegPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.RegPolicies.RegPolicy>`
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.RegPolicies, self).__init__()

            self.yang_name = "reg-policies"
            self.yang_parent_name = "eem"

            self.reg_policy = YList(self)

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
                        super(Eem.RegPolicies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Eem.RegPolicies, self).__setattr__(name, value)


        class RegPolicy(Entity):
            """
            policy name and create time 
            
            .. attribute:: name  <key>
            
            	policy name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: class_
            
            	class
            	**type**\:  str
            
            .. attribute:: description
            
            	description
            	**type**\:  str
            
            .. attribute:: event_type
            
            	event type
            	**type**\:  str
            
            .. attribute:: persist_time
            
            	PersistTime 
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: policy_name
            
            	policy name
            	**type**\:  str
            
            .. attribute:: time_created
            
            	time created
            	**type**\:  str
            
            .. attribute:: trap
            
            	trap
            	**type**\:  str
            
            .. attribute:: type
            
            	policy type
            	**type**\:  str
            
            .. attribute:: username
            
            	username
            	**type**\:  str
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.RegPolicies.RegPolicy, self).__init__()

                self.yang_name = "reg-policy"
                self.yang_parent_name = "reg-policies"

                self.name = YLeaf(YType.str, "name")

                self.class_ = YLeaf(YType.str, "class")

                self.description = YLeaf(YType.str, "description")

                self.event_type = YLeaf(YType.str, "event-type")

                self.persist_time = YLeaf(YType.uint32, "persist-time")

                self.policy_name = YLeaf(YType.str, "policy-name")

                self.time_created = YLeaf(YType.str, "time-created")

                self.trap = YLeaf(YType.str, "trap")

                self.type = YLeaf(YType.str, "type")

                self.username = YLeaf(YType.str, "username")

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
                                "class_",
                                "description",
                                "event_type",
                                "persist_time",
                                "policy_name",
                                "time_created",
                                "trap",
                                "type",
                                "username") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Eem.RegPolicies.RegPolicy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Eem.RegPolicies.RegPolicy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.class_.is_set or
                    self.description.is_set or
                    self.event_type.is_set or
                    self.persist_time.is_set or
                    self.policy_name.is_set or
                    self.time_created.is_set or
                    self.trap.is_set or
                    self.type.is_set or
                    self.username.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.class_.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.event_type.yfilter != YFilter.not_set or
                    self.persist_time.yfilter != YFilter.not_set or
                    self.policy_name.yfilter != YFilter.not_set or
                    self.time_created.yfilter != YFilter.not_set or
                    self.trap.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.username.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "reg-policy" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/reg-policies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.class_.is_set or self.class_.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.class_.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.event_type.is_set or self.event_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.event_type.get_name_leafdata())
                if (self.persist_time.is_set or self.persist_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.persist_time.get_name_leafdata())
                if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_name.get_name_leafdata())
                if (self.time_created.is_set or self.time_created.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_created.get_name_leafdata())
                if (self.trap.is_set or self.trap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.trap.get_name_leafdata())
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.username.is_set or self.username.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.username.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "class" or name == "description" or name == "event-type" or name == "persist-time" or name == "policy-name" or name == "time-created" or name == "trap" or name == "type" or name == "username"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "class"):
                    self.class_ = value
                    self.class_.value_namespace = name_space
                    self.class_.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "event-type"):
                    self.event_type = value
                    self.event_type.value_namespace = name_space
                    self.event_type.value_namespace_prefix = name_space_prefix
                if(value_path == "persist-time"):
                    self.persist_time = value
                    self.persist_time.value_namespace = name_space
                    self.persist_time.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-name"):
                    self.policy_name = value
                    self.policy_name.value_namespace = name_space
                    self.policy_name.value_namespace_prefix = name_space_prefix
                if(value_path == "time-created"):
                    self.time_created = value
                    self.time_created.value_namespace = name_space
                    self.time_created.value_namespace_prefix = name_space_prefix
                if(value_path == "trap"):
                    self.trap = value
                    self.trap.value_namespace = name_space
                    self.trap.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "username"):
                    self.username = value
                    self.username.value_namespace = name_space
                    self.username.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.reg_policy:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.reg_policy:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "reg-policies" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "reg-policy"):
                for c in self.reg_policy:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Eem.RegPolicies.RegPolicy()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.reg_policy.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "reg-policy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class AvlPolicies(Entity):
        """
        list the available policies
        
        .. attribute:: avl_policy
        
        	policy name and create time 
        	**type**\: list of    :py:class:`AvlPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.AvlPolicies.AvlPolicy>`
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.AvlPolicies, self).__init__()

            self.yang_name = "avl-policies"
            self.yang_parent_name = "eem"

            self.avl_policy = YList(self)

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
                        super(Eem.AvlPolicies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Eem.AvlPolicies, self).__setattr__(name, value)


        class AvlPolicy(Entity):
            """
            policy name and create time 
            
            .. attribute:: name  <key>
            
            	System policy name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: policy_name
            
            	policy name
            	**type**\:  str
            
            .. attribute:: time_created
            
            	time created
            	**type**\:  str
            
            .. attribute:: type
            
            	policy type
            	**type**\:  str
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.AvlPolicies.AvlPolicy, self).__init__()

                self.yang_name = "avl-policy"
                self.yang_parent_name = "avl-policies"

                self.name = YLeaf(YType.str, "name")

                self.policy_name = YLeaf(YType.str, "policy-name")

                self.time_created = YLeaf(YType.str, "time-created")

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
                    if name in ("name",
                                "policy_name",
                                "time_created",
                                "type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Eem.AvlPolicies.AvlPolicy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Eem.AvlPolicies.AvlPolicy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.policy_name.is_set or
                    self.time_created.is_set or
                    self.type.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.policy_name.yfilter != YFilter.not_set or
                    self.time_created.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "avl-policy" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/avl-policies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_name.get_name_leafdata())
                if (self.time_created.is_set or self.time_created.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.time_created.get_name_leafdata())
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
                if(name == "name" or name == "policy-name" or name == "time-created" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-name"):
                    self.policy_name = value
                    self.policy_name.value_namespace = name_space
                    self.policy_name.value_namespace_prefix = name_space_prefix
                if(value_path == "time-created"):
                    self.time_created = value
                    self.time_created.value_namespace = name_space
                    self.time_created.value_namespace_prefix = name_space_prefix
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.avl_policy:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.avl_policy:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "avl-policies" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "avl-policy"):
                for c in self.avl_policy:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Eem.AvlPolicies.AvlPolicy()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.avl_policy.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "avl-policy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.avl_policies is not None and self.avl_policies.has_data()) or
            (self.dir_user is not None and self.dir_user.has_data()) or
            (self.env_variables is not None and self.env_variables.has_data()) or
            (self.refresh_time is not None and self.refresh_time.has_data()) or
            (self.reg_policies is not None and self.reg_policies.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.avl_policies is not None and self.avl_policies.has_operation()) or
            (self.dir_user is not None and self.dir_user.has_operation()) or
            (self.env_variables is not None and self.env_variables.has_operation()) or
            (self.refresh_time is not None and self.refresh_time.has_operation()) or
            (self.reg_policies is not None and self.reg_policies.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ha-eem-policy-oper:eem" + path_buffer

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

        if (child_yang_name == "avl-policies"):
            if (self.avl_policies is None):
                self.avl_policies = Eem.AvlPolicies()
                self.avl_policies.parent = self
                self._children_name_map["avl_policies"] = "avl-policies"
            return self.avl_policies

        if (child_yang_name == "dir-user"):
            if (self.dir_user is None):
                self.dir_user = Eem.DirUser()
                self.dir_user.parent = self
                self._children_name_map["dir_user"] = "dir-user"
            return self.dir_user

        if (child_yang_name == "env-variables"):
            if (self.env_variables is None):
                self.env_variables = Eem.EnvVariables()
                self.env_variables.parent = self
                self._children_name_map["env_variables"] = "env-variables"
            return self.env_variables

        if (child_yang_name == "refresh-time"):
            if (self.refresh_time is None):
                self.refresh_time = Eem.RefreshTime()
                self.refresh_time.parent = self
                self._children_name_map["refresh_time"] = "refresh-time"
            return self.refresh_time

        if (child_yang_name == "reg-policies"):
            if (self.reg_policies is None):
                self.reg_policies = Eem.RegPolicies()
                self.reg_policies.parent = self
                self._children_name_map["reg_policies"] = "reg-policies"
            return self.reg_policies

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "avl-policies" or name == "dir-user" or name == "env-variables" or name == "refresh-time" or name == "reg-policies"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Eem()
        return self._top_entity

