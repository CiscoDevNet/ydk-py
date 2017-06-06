""" Cisco_IOS_XR_ha_eem_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ha\-eem package configuration.

This module contains definitions
for the following management objects\:
  event\-manager\: Event manager configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EventManagerChecksumEnum(Enum):
    """
    EventManagerChecksumEnum

    Event manager checksum

    .. data:: sha_1 = 1

    	Use SHA-1 checksum

    .. data:: md5 = 2

    	Use MD5 checksum

    """

    sha_1 = 1

    md5 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
        return meta._meta_table['EventManagerChecksumEnum']


class EventManagerPolicyEnum(Enum):
    """
    EventManagerPolicyEnum

    Event manager policy

    .. data:: system = 0

    	Event manager system policy

    .. data:: user = 1

    	Event manager user policy

    """

    system = 0

    user = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
        return meta._meta_table['EventManagerPolicyEnum']


class EventManagerPolicyModeEnum(Enum):
    """
    EventManagerPolicyModeEnum

    Event manager policy mode

    .. data:: cisco = 1

    	Cisco Signature

    .. data:: trust = 2

    	Trust Signature

    """

    cisco = 1

    trust = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
        return meta._meta_table['EventManagerPolicyModeEnum']


class EventManagerPolicySecEnum(Enum):
    """
    EventManagerPolicySecEnum

    Event manager policy sec

    .. data:: rsa_2048 = 2

    	Cisco Signature

    .. data:: trust = 3

    	Trust Signature

    """

    rsa_2048 = 2

    trust = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
        return meta._meta_table['EventManagerPolicySecEnum']



class EventManager(object):
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
        self.directory_user_library = None
        self.directory_user_policy = None
        self.environments = EventManager.Environments()
        self.environments.parent = self
        self.policies = EventManager.Policies()
        self.policies.parent = self
        self.refresh_time = None
        self.schedule_suspend = None
        self.scheduler_script = EventManager.SchedulerScript()
        self.scheduler_script.parent = self


    class Policies(object):
        """
        Register an event manager policy
        
        .. attribute:: policy
        
        	Name of the policy file
        	**type**\: list of    :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.Policies.Policy>`
        
        

        """

        _prefix = 'ha-eem-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.policy = YList()
            self.policy.parent = self
            self.policy.name = 'policy'


        class Policy(object):
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
            	**type**\:   :py:class:`EventManagerChecksumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerChecksumEnum>`
            
            .. attribute:: persist_time
            
            	Time of validity (in seconds) for cached AAA taskmap of username (default is 3600)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            	**units**\: second
            
            .. attribute:: policy_security_level
            
            	Event Manager policy security Level
            	**type**\:   :py:class:`EventManagerPolicySecEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerPolicySecEnum>`
            
            .. attribute:: policy_security_mode
            
            	Specify Embedded Event Manager policy security mode
            	**type**\:   :py:class:`EventManagerPolicyModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerPolicyModeEnum>`
            
            .. attribute:: policy_type
            
            	Event manager type of this policy
            	**type**\:   :py:class:`EventManagerPolicyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManagerPolicyEnum>`
            
            .. attribute:: username
            
            	A configured username
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'ha-eem-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.policy_name = None
                self.check_sum_value = None
                self.checksum_type = None
                self.persist_time = None
                self.policy_security_level = None
                self.policy_security_mode = None
                self.policy_type = None
                self.username = None

            @property
            def _common_path(self):
                if self.policy_name is None:
                    raise YPYModelError('Key property policy_name is None')

                return '/Cisco-IOS-XR-ha-eem-cfg:event-manager/Cisco-IOS-XR-ha-eem-cfg:policies/Cisco-IOS-XR-ha-eem-cfg:policy[Cisco-IOS-XR-ha-eem-cfg:policy-name = ' + str(self.policy_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.policy_name is not None:
                    return True

                if self.check_sum_value is not None:
                    return True

                if self.checksum_type is not None:
                    return True

                if self.persist_time is not None:
                    return True

                if self.policy_security_level is not None:
                    return True

                if self.policy_security_mode is not None:
                    return True

                if self.policy_type is not None:
                    return True

                if self.username is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
                return meta._meta_table['EventManager.Policies.Policy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-cfg:event-manager/Cisco-IOS-XR-ha-eem-cfg:policies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.policy is not None:
                for child_ref in self.policy:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
            return meta._meta_table['EventManager.Policies']['meta_info']


    class SchedulerScript(object):
        """
        scheduler classs type
        
        .. attribute:: thread_classes
        
        	scheduler thread classs 
        	**type**\:   :py:class:`ThreadClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.SchedulerScript.ThreadClasses>`
        
        

        """

        _prefix = 'ha-eem-cfg'
        _revision = '2015-07-30'

        def __init__(self):
            self.parent = None
            self.thread_classes = EventManager.SchedulerScript.ThreadClasses()
            self.thread_classes.parent = self


        class ThreadClasses(object):
            """
            scheduler thread classs 
            
            .. attribute:: thread_class
            
            	scheduler classs type argument
            	**type**\: list of    :py:class:`ThreadClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg.EventManager.SchedulerScript.ThreadClasses.ThreadClass>`
            
            

            """

            _prefix = 'ha-eem-cfg'
            _revision = '2015-07-30'

            def __init__(self):
                self.parent = None
                self.thread_class = YList()
                self.thread_class.parent = self
                self.thread_class.name = 'thread_class'


            class ThreadClass(object):
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
                    self.parent = None
                    self.thread_class_name = None
                    self.num_threads = None

                @property
                def _common_path(self):
                    if self.thread_class_name is None:
                        raise YPYModelError('Key property thread_class_name is None')

                    return '/Cisco-IOS-XR-ha-eem-cfg:event-manager/Cisco-IOS-XR-ha-eem-cfg:scheduler-script/Cisco-IOS-XR-ha-eem-cfg:thread-classes/Cisco-IOS-XR-ha-eem-cfg:thread-class[Cisco-IOS-XR-ha-eem-cfg:thread-class-name = ' + str(self.thread_class_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.thread_class_name is not None:
                        return True

                    if self.num_threads is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
                    return meta._meta_table['EventManager.SchedulerScript.ThreadClasses.ThreadClass']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ha-eem-cfg:event-manager/Cisco-IOS-XR-ha-eem-cfg:scheduler-script/Cisco-IOS-XR-ha-eem-cfg:thread-classes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.thread_class is not None:
                    for child_ref in self.thread_class:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
                return meta._meta_table['EventManager.SchedulerScript.ThreadClasses']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-cfg:event-manager/Cisco-IOS-XR-ha-eem-cfg:scheduler-script'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.thread_classes is not None and self.thread_classes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
            return meta._meta_table['EventManager.SchedulerScript']['meta_info']


    class Environments(object):
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
            self.parent = None
            self.environment = YList()
            self.environment.parent = self
            self.environment.name = 'environment'


        class Environment(object):
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
                self.parent = None
                self.environment_name = None
                self.environment_value = None

            @property
            def _common_path(self):
                if self.environment_name is None:
                    raise YPYModelError('Key property environment_name is None')

                return '/Cisco-IOS-XR-ha-eem-cfg:event-manager/Cisco-IOS-XR-ha-eem-cfg:environments/Cisco-IOS-XR-ha-eem-cfg:environment[Cisco-IOS-XR-ha-eem-cfg:environment-name = ' + str(self.environment_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.environment_name is not None:
                    return True

                if self.environment_value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
                return meta._meta_table['EventManager.Environments.Environment']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-cfg:event-manager/Cisco-IOS-XR-ha-eem-cfg:environments'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.environment is not None:
                for child_ref in self.environment:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
            return meta._meta_table['EventManager.Environments']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ha-eem-cfg:event-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.directory_user_library is not None:
            return True

        if self.directory_user_policy is not None:
            return True

        if self.environments is not None and self.environments._has_data():
            return True

        if self.policies is not None and self.policies._has_data():
            return True

        if self.refresh_time is not None:
            return True

        if self.schedule_suspend is not None:
            return True

        if self.scheduler_script is not None and self.scheduler_script._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_cfg as meta
        return meta._meta_table['EventManager']['meta_info']


