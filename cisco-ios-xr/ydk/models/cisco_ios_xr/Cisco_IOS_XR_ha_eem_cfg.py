""" Cisco_IOS_XR_ha_eem_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ha\-eem package configuration.

This module contains definitions
for the following management objects\:
  event\-manager\: Event manager configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"environments" : ("environments", EventManager.Environments), "policies" : ("policies", EventManager.Policies), "scheduler-script" : ("scheduler_script", EventManager.SchedulerScript)}
        self._child_list_classes = {}

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
        self._segment_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager"

    def __setattr__(self, name, value):
        self._perform_setattr(EventManager, ['directory_user_library', 'directory_user_policy', 'refresh_time', 'schedule_suspend'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"environment" : ("environment", EventManager.Environments.Environment)}

            self.environment = YList(self)
            self._segment_path = lambda: "environments"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EventManager.Environments, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.environment_name = YLeaf(YType.str, "environment-name")

                self.environment_value = YLeaf(YType.str, "environment-value")
                self._segment_path = lambda: "environment" + "[environment-name='" + self.environment_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager/environments/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EventManager.Environments.Environment, ['environment_name', 'environment_value'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"policy" : ("policy", EventManager.Policies.Policy)}

            self.policy = YList(self)
            self._segment_path = lambda: "policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(EventManager.Policies, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.policy_name = YLeaf(YType.str, "policy-name")

                self.check_sum_value = YLeaf(YType.str, "check-sum-value")

                self.checksum_type = YLeaf(YType.enumeration, "checksum-type")

                self.persist_time = YLeaf(YType.uint32, "persist-time")

                self.policy_security_level = YLeaf(YType.enumeration, "policy-security-level")

                self.policy_security_mode = YLeaf(YType.enumeration, "policy-security-mode")

                self.policy_type = YLeaf(YType.enumeration, "policy-type")

                self.username = YLeaf(YType.str, "username")
                self._segment_path = lambda: "policy" + "[policy-name='" + self.policy_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager/policies/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EventManager.Policies.Policy, ['policy_name', 'check_sum_value', 'checksum_type', 'persist_time', 'policy_security_level', 'policy_security_mode', 'policy_type', 'username'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"thread-classes" : ("thread_classes", EventManager.SchedulerScript.ThreadClasses)}
            self._child_list_classes = {}

            self.thread_classes = EventManager.SchedulerScript.ThreadClasses()
            self.thread_classes.parent = self
            self._children_name_map["thread_classes"] = "thread-classes"
            self._children_yang_names.add("thread-classes")
            self._segment_path = lambda: "scheduler-script"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager/%s" % self._segment_path()


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"thread-class" : ("thread_class", EventManager.SchedulerScript.ThreadClasses.ThreadClass)}

                self.thread_class = YList(self)
                self._segment_path = lambda: "thread-classes"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager/scheduler-script/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(EventManager.SchedulerScript.ThreadClasses, [], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.thread_class_name = YLeaf(YType.str, "thread-class-name")

                    self.num_threads = YLeaf(YType.uint32, "num-threads")
                    self._segment_path = lambda: "thread-class" + "[thread-class-name='" + self.thread_class_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-cfg:event-manager/scheduler-script/thread-classes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(EventManager.SchedulerScript.ThreadClasses.ThreadClass, ['thread_class_name', 'num_threads'], name, value)

    def clone_ptr(self):
        self._top_entity = EventManager()
        return self._top_entity

