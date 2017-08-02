""" Cisco_IOS_XR_ha_eem_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ha\-eem package configuration.

This module contains definitions
for the following management objects\:
  event\-manager\: Event manager configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EventManagerChecksum(Enum):
    """
    EventManagerChecksum

    Event manager checksum

    .. data:: sha_1 = 1

    	Use SHA-1 checksum

    .. data:: md5 = 2

    	Use MD5 checksum

    """

    sha_1 = Enum.YLeaf(1, "sha-1")

    md5 = Enum.YLeaf(2, "md5")


class EventManagerPolicy(Enum):
    """
    EventManagerPolicy

    Event manager policy

    .. data:: system = 0

    	Event manager system policy

    .. data:: user = 1

    	Event manager user policy

    """

    system = Enum.YLeaf(0, "system")

    user = Enum.YLeaf(1, "user")


class EventManagerPolicyMode(Enum):
    """
    EventManagerPolicyMode

    Event manager policy mode

    .. data:: cisco = 1

    	Cisco Signature

    .. data:: trust = 2

    	Trust Signature

    """

    cisco = Enum.YLeaf(1, "cisco")

    trust = Enum.YLeaf(2, "trust")


class EventManagerPolicySec(Enum):
    """
    EventManagerPolicySec

    Event manager policy sec

    .. data:: rsa_2048 = 2

    	Cisco Signature

    .. data:: trust = 3

    	Trust Signature

    """

    rsa_2048 = Enum.YLeaf(2, "rsa-2048")

    trust = Enum.YLeaf(3, "trust")



class EventManager(Entity):
    """
    Event manager configuration
    
    .. attribute:: directory_user_library
    
    	Path of the user policy library directory
    	**type**\:  str
    
    .. attribute:: directory_user_policy
    
    	Set event manager user policy directory
    	**type**\:  str
    
    .. attribute:: environments
    
    	Set an event manager global variable for event manager policies
    	**type**\:   :py:class:`Environments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.Environments>`
    
    .. attribute:: policies
    
    	Register an event manager policy
    	**type**\:   :py:class:`Policies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.Policies>`
    
    .. attribute:: refresh_time
    
    	Set refresh time (in seconds) for policy username's AAA taskmap
    	**type**\:  int
    
    	**range:** 10..4294967295
    
    	**units**\: second
    
    	**default value**\: 1800
    
    .. attribute:: schedule_suspend
    
    	Enable suspend policy scheduling
    	**type**\:  bool
    
    .. attribute:: scheduler_script
    
    	scheduler classs type
    	**type**\:   :py:class:`SchedulerScript <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.SchedulerScript>`
    
    

    """

    _prefix = 'ha-eem-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(EventManager, self).__init__()
        self._top_entity = None

        self.yang_name = "event-manager"
        self.yang_parent_name = "Cisco-IOS-XR-ha-eem-cfg"

        self.directory_user_library = YLeaf(YType.str, "directory-user-library")

        self.directory_user_policy = YLeaf(YType.str, "directory-user-policy")

        self.refresh_time = YLeaf(YType.uint32, "refresh-time")

        self.schedule_suspend = YLeaf(YType.boolean, "schedule-suspend")

        self.environments = EventManager.Environments()
        self.environments.parent = self
        self._children_name_map["environments"] = "environments"
        self._children_yang_names.add("environments")

        self.policies = EventManager.Policies()
        self.policies.parent = self
        self._children_name_map["policies"] = "policies"
        self._children_yang_names.add("policies")

        self.scheduler_script = EventManager.SchedulerScript()
        self.scheduler_script.parent = self
        self._children_name_map["scheduler_script"] = "scheduler-script"
        self._children_yang_names.add("scheduler-script")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("directory_user_library",
                        "directory_user_policy",
                        "refresh_time",
                        "schedule_suspend") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(EventManager, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(EventManager, self).__setattr__(name, value)


    class Policies(Entity):
        """
        Register an event manager policy
        
        .. attribute:: policy
        
        	Name of the policy file
        	**type**\: list of    :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.Policies.Policy>`
        
        

        """

        _prefix = 'ha-eem-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(EventManager.Policies, self).__init__()

            self.yang_name = "policies"
            self.yang_parent_name = "event-manager"

            self.policy = YList(self)

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
                        super(EventManager.Policies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EventManager.Policies, self).__setattr__(name, value)


        class Policy(Entity):
            """
            Name of the policy file
            
            .. attribute:: policy_name  <key>
            
            	Name of the policy file
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: check_sum_value
            
            	CheckSum Value
            	**type**\:  str
            
            .. attribute:: checksum_type
            
            	Specify Embedded Event Manager policy checksum
            	**type**\:   :py:class:`EventManagerChecksum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerChecksum>`
            
            .. attribute:: persist_time
            
            	Time of validity (in seconds) for cached AAA taskmap of username (default is 3600)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            	**units**\: second
            
            .. attribute:: policy_security_level
            
            	Event Manager policy security Level
            	**type**\:   :py:class:`EventManagerPolicySec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerPolicySec>`
            
            .. attribute:: policy_security_mode
            
            	Specify Embedded Event Manager policy security mode
            	**type**\:   :py:class:`EventManagerPolicyMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerPolicyMode>`
            
            .. attribute:: policy_type
            
            	Event manager type of this policy
            	**type**\:   :py:class:`EventManagerPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerPolicy>`
            
            .. attribute:: username
            
            	A configured username
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ha-eem-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(EventManager.Policies.Policy, self).__init__()

                self.yang_name = "policy"
                self.yang_parent_name = "policies"

                self.policy_name = YLeaf(YType.str, "policy-name")

                self.check_sum_value = YLeaf(YType.str, "check-sum-value")

                self.checksum_type = YLeaf(YType.enumeration, "checksum-type")

                self.persist_time = YLeaf(YType.uint32, "persist-time")

                self.policy_security_level = YLeaf(YType.enumeration, "policy-security-level")

                self.policy_security_mode = YLeaf(YType.enumeration, "policy-security-mode")

                self.policy_type = YLeaf(YType.enumeration, "policy-type")

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
                    if name in ("policy_name",
                                "check_sum_value",
                                "checksum_type",
                                "persist_time",
                                "policy_security_level",
                                "policy_security_mode",
                                "policy_type",
                                "username") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EventManager.Policies.Policy, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EventManager.Policies.Policy, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.policy_name.is_set or
                    self.check_sum_value.is_set or
                    self.checksum_type.is_set or
                    self.persist_time.is_set or
                    self.policy_security_level.is_set or
                    self.policy_security_mode.is_set or
                    self.policy_type.is_set or
                    self.username.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.policy_name.yfilter != YFilter.not_set or
                    self.check_sum_value.yfilter != YFilter.not_set or
                    self.checksum_type.yfilter != YFilter.not_set or
                    self.persist_time.yfilter != YFilter.not_set or
                    self.policy_security_level.yfilter != YFilter.not_set or
                    self.policy_security_mode.yfilter != YFilter.not_set or
                    self.policy_type.yfilter != YFilter.not_set or
                    self.username.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy" + "[policy-name='" + self.policy_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager/policies/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_name.get_name_leafdata())
                if (self.check_sum_value.is_set or self.check_sum_value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.check_sum_value.get_name_leafdata())
                if (self.checksum_type.is_set or self.checksum_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.checksum_type.get_name_leafdata())
                if (self.persist_time.is_set or self.persist_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.persist_time.get_name_leafdata())
                if (self.policy_security_level.is_set or self.policy_security_level.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_security_level.get_name_leafdata())
                if (self.policy_security_mode.is_set or self.policy_security_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_security_mode.get_name_leafdata())
                if (self.policy_type.is_set or self.policy_type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.policy_type.get_name_leafdata())
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
                if(name == "policy-name" or name == "check-sum-value" or name == "checksum-type" or name == "persist-time" or name == "policy-security-level" or name == "policy-security-mode" or name == "policy-type" or name == "username"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "policy-name"):
                    self.policy_name = value
                    self.policy_name.value_namespace = name_space
                    self.policy_name.value_namespace_prefix = name_space_prefix
                if(value_path == "check-sum-value"):
                    self.check_sum_value = value
                    self.check_sum_value.value_namespace = name_space
                    self.check_sum_value.value_namespace_prefix = name_space_prefix
                if(value_path == "checksum-type"):
                    self.checksum_type = value
                    self.checksum_type.value_namespace = name_space
                    self.checksum_type.value_namespace_prefix = name_space_prefix
                if(value_path == "persist-time"):
                    self.persist_time = value
                    self.persist_time.value_namespace = name_space
                    self.persist_time.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-security-level"):
                    self.policy_security_level = value
                    self.policy_security_level.value_namespace = name_space
                    self.policy_security_level.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-security-mode"):
                    self.policy_security_mode = value
                    self.policy_security_mode.value_namespace = name_space
                    self.policy_security_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "policy-type"):
                    self.policy_type = value
                    self.policy_type.value_namespace = name_space
                    self.policy_type.value_namespace_prefix = name_space_prefix
                if(value_path == "username"):
                    self.username = value
                    self.username.value_namespace = name_space
                    self.username.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.policy:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.policy:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "policies" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "policy"):
                for c in self.policy:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EventManager.Policies.Policy()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.policy.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "policy"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class SchedulerScript(Entity):
        """
        scheduler classs type
        
        .. attribute:: thread_classes
        
        	scheduler thread classs 
        	**type**\:   :py:class:`ThreadClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.SchedulerScript.ThreadClasses>`
        
        

        """

        _prefix = 'ha-eem-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(EventManager.SchedulerScript, self).__init__()

            self.yang_name = "scheduler-script"
            self.yang_parent_name = "event-manager"

            self.thread_classes = EventManager.SchedulerScript.ThreadClasses()
            self.thread_classes.parent = self
            self._children_name_map["thread_classes"] = "thread-classes"
            self._children_yang_names.add("thread-classes")


        class ThreadClasses(Entity):
            """
            scheduler thread classs 
            
            .. attribute:: thread_class
            
            	scheduler classs type argument
            	**type**\: list of    :py:class:`ThreadClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.SchedulerScript.ThreadClasses.ThreadClass>`
            
            

            """

            _prefix = 'ha-eem-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(EventManager.SchedulerScript.ThreadClasses, self).__init__()

                self.yang_name = "thread-classes"
                self.yang_parent_name = "scheduler-script"

                self.thread_class = YList(self)

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
                            super(EventManager.SchedulerScript.ThreadClasses, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EventManager.SchedulerScript.ThreadClasses, self).__setattr__(name, value)


            class ThreadClass(Entity):
                """
                scheduler classs type argument
                
                .. attribute:: thread_class_name  <key>
                
                	Name of the global variable
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: num_threads
                
                	number of scheduler threads
                	**type**\:  int
                
                	**range:** 1..5
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'ha-eem-cfg'
                _revision = '2015-07-30'

                def __init__(self):
                    super(EventManager.SchedulerScript.ThreadClasses.ThreadClass, self).__init__()

                    self.yang_name = "thread-class"
                    self.yang_parent_name = "thread-classes"

                    self.thread_class_name = YLeaf(YType.str, "thread-class-name")

                    self.num_threads = YLeaf(YType.uint32, "num-threads")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("thread_class_name",
                                    "num_threads") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(EventManager.SchedulerScript.ThreadClasses.ThreadClass, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(EventManager.SchedulerScript.ThreadClasses.ThreadClass, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.thread_class_name.is_set or
                        self.num_threads.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.thread_class_name.yfilter != YFilter.not_set or
                        self.num_threads.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "thread-class" + "[thread-class-name='" + self.thread_class_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager/scheduler-script/thread-classes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.thread_class_name.is_set or self.thread_class_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.thread_class_name.get_name_leafdata())
                    if (self.num_threads.is_set or self.num_threads.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.num_threads.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "thread-class-name" or name == "num-threads"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "thread-class-name"):
                        self.thread_class_name = value
                        self.thread_class_name.value_namespace = name_space
                        self.thread_class_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "num-threads"):
                        self.num_threads = value
                        self.num_threads.value_namespace = name_space
                        self.num_threads.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.thread_class:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.thread_class:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "thread-classes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager/scheduler-script/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "thread-class"):
                    for c in self.thread_class:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = EventManager.SchedulerScript.ThreadClasses.ThreadClass()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.thread_class.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "thread-class"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (self.thread_classes is not None and self.thread_classes.has_data())

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.thread_classes is not None and self.thread_classes.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "scheduler-script" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "thread-classes"):
                if (self.thread_classes is None):
                    self.thread_classes = EventManager.SchedulerScript.ThreadClasses()
                    self.thread_classes.parent = self
                    self._children_name_map["thread_classes"] = "thread-classes"
                return self.thread_classes

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "thread-classes"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Environments(Entity):
        """
        Set an event manager global variable for event
        manager policies
        
        .. attribute:: environment
        
        	Name of the global variable
        	**type**\: list of    :py:class:`Environment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.Environments.Environment>`
        
        

        """

        _prefix = 'ha-eem-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            super(EventManager.Environments, self).__init__()

            self.yang_name = "environments"
            self.yang_parent_name = "event-manager"

            self.environment = YList(self)

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
                        super(EventManager.Environments, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EventManager.Environments, self).__setattr__(name, value)


        class Environment(Entity):
            """
            Name of the global variable
            
            .. attribute:: environment_name  <key>
            
            	Name of the global variable
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: environment_value
            
            	Value of the global variable
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ha-eem-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                super(EventManager.Environments.Environment, self).__init__()

                self.yang_name = "environment"
                self.yang_parent_name = "environments"

                self.environment_name = YLeaf(YType.str, "environment-name")

                self.environment_value = YLeaf(YType.str, "environment-value")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("environment_name",
                                "environment_value") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EventManager.Environments.Environment, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EventManager.Environments.Environment, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.environment_name.is_set or
                    self.environment_value.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.environment_name.yfilter != YFilter.not_set or
                    self.environment_value.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "environment" + "[environment-name='" + self.environment_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager/environments/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.environment_name.is_set or self.environment_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.environment_name.get_name_leafdata())
                if (self.environment_value.is_set or self.environment_value.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.environment_value.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "environment-name" or name == "environment-value"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "environment-name"):
                    self.environment_name = value
                    self.environment_name.value_namespace = name_space
                    self.environment_name.value_namespace_prefix = name_space_prefix
                if(value_path == "environment-value"):
                    self.environment_value = value
                    self.environment_value.value_namespace = name_space
                    self.environment_value.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.environment:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.environment:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "environments" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "environment"):
                for c in self.environment:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EventManager.Environments.Environment()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.environment.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "environment"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.directory_user_library.is_set or
            self.directory_user_policy.is_set or
            self.refresh_time.is_set or
            self.schedule_suspend.is_set or
            (self.environments is not None and self.environments.has_data()) or
            (self.policies is not None and self.policies.has_data()) or
            (self.scheduler_script is not None and self.scheduler_script.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.directory_user_library.yfilter != YFilter.not_set or
            self.directory_user_policy.yfilter != YFilter.not_set or
            self.refresh_time.yfilter != YFilter.not_set or
            self.schedule_suspend.yfilter != YFilter.not_set or
            (self.environments is not None and self.environments.has_operation()) or
            (self.policies is not None and self.policies.has_operation()) or
            (self.scheduler_script is not None and self.scheduler_script.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ha-eem-cfg:event-manager" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.directory_user_library.is_set or self.directory_user_library.yfilter != YFilter.not_set):
            leaf_name_data.append(self.directory_user_library.get_name_leafdata())
        if (self.directory_user_policy.is_set or self.directory_user_policy.yfilter != YFilter.not_set):
            leaf_name_data.append(self.directory_user_policy.get_name_leafdata())
        if (self.refresh_time.is_set or self.refresh_time.yfilter != YFilter.not_set):
            leaf_name_data.append(self.refresh_time.get_name_leafdata())
        if (self.schedule_suspend.is_set or self.schedule_suspend.yfilter != YFilter.not_set):
            leaf_name_data.append(self.schedule_suspend.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "environments"):
            if (self.environments is None):
                self.environments = EventManager.Environments()
                self.environments.parent = self
                self._children_name_map["environments"] = "environments"
            return self.environments

        if (child_yang_name == "policies"):
            if (self.policies is None):
                self.policies = EventManager.Policies()
                self.policies.parent = self
                self._children_name_map["policies"] = "policies"
            return self.policies

        if (child_yang_name == "scheduler-script"):
            if (self.scheduler_script is None):
                self.scheduler_script = EventManager.SchedulerScript()
                self.scheduler_script.parent = self
                self._children_name_map["scheduler_script"] = "scheduler-script"
            return self.scheduler_script

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "environments" or name == "policies" or name == "scheduler-script" or name == "directory-user-library" or name == "directory-user-policy" or name == "refresh-time" or name == "schedule-suspend"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "directory-user-library"):
            self.directory_user_library = value
            self.directory_user_library.value_namespace = name_space
            self.directory_user_library.value_namespace_prefix = name_space_prefix
        if(value_path == "directory-user-policy"):
            self.directory_user_policy = value
            self.directory_user_policy.value_namespace = name_space
            self.directory_user_policy.value_namespace_prefix = name_space_prefix
        if(value_path == "refresh-time"):
            self.refresh_time = value
            self.refresh_time.value_namespace = name_space
            self.refresh_time.value_namespace_prefix = name_space_prefix
        if(value_path == "schedule-suspend"):
            self.schedule_suspend = value
            self.schedule_suspend.value_namespace = name_space
            self.schedule_suspend.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = EventManager()
        return self._top_entity

