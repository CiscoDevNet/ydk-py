""" Cisco_IOS_XR_ha_eem_policy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ha\-eem\-policy package operational data.

This module contains definitions
for the following management objects\:
  eem\: EEM operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Eem(object):
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
        self.avl_policies = Eem.AvlPolicies()
        self.avl_policies.parent = self
        self.dir_user = Eem.DirUser()
        self.dir_user.parent = self
        self.env_variables = Eem.EnvVariables()
        self.env_variables.parent = self
        self.refresh_time = Eem.RefreshTime()
        self.refresh_time.parent = self
        self.reg_policies = Eem.RegPolicies()
        self.reg_policies.parent = self


    class DirUser(object):
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
            self.parent = None
            self.library = Eem.DirUser.Library()
            self.library.parent = self
            self.policy = Eem.DirUser.Policy()
            self.policy.parent = self


        class Library(object):
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
                self.parent = None
                self.library = None
                self.policy = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:dir-user/Cisco-IOS-XR-ha-eem-policy-oper:library'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.library is not None:
                    return True

                if self.policy is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
                return meta._meta_table['Eem.DirUser.Library']['meta_info']


        class Policy(object):
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
                self.parent = None
                self.library = None
                self.policy = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:dir-user/Cisco-IOS-XR-ha-eem-policy-oper:policy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.library is not None:
                    return True

                if self.policy is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
                return meta._meta_table['Eem.DirUser.Policy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:dir-user'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.library is not None and self.library._has_data():
                return True

            if self.policy is not None and self.policy._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
            return meta._meta_table['Eem.DirUser']['meta_info']


    class EnvVariables(object):
        """
        list of environmental variables
        
        .. attribute:: env_variable
        
        	environmental variables name and value 
        	**type**\: list of    :py:class:`EnvVariable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.EnvVariables.EnvVariable>`
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            self.parent = None
            self.env_variable = YList()
            self.env_variable.parent = self
            self.env_variable.name = 'env_variable'


        class EnvVariable(object):
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
                self.parent = None
                self.name = None
                self.name_xr = None
                self.value = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:env-variables/Cisco-IOS-XR-ha-eem-policy-oper:env-variable[Cisco-IOS-XR-ha-eem-policy-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.name_xr is not None:
                    return True

                if self.value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
                return meta._meta_table['Eem.EnvVariables.EnvVariable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:env-variables'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.env_variable is not None:
                for child_ref in self.env_variable:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
            return meta._meta_table['Eem.EnvVariables']['meta_info']


    class RefreshTime(object):
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
            self.parent = None
            self.refreshtime = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:refresh-time'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.refreshtime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
            return meta._meta_table['Eem.RefreshTime']['meta_info']


    class RegPolicies(object):
        """
        list the registered policies
        
        .. attribute:: reg_policy
        
        	policy name and create time 
        	**type**\: list of    :py:class:`RegPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.RegPolicies.RegPolicy>`
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            self.parent = None
            self.reg_policy = YList()
            self.reg_policy.parent = self
            self.reg_policy.name = 'reg_policy'


        class RegPolicy(object):
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
                self.parent = None
                self.name = None
                self.class_ = None
                self.description = None
                self.event_type = None
                self.persist_time = None
                self.policy_name = None
                self.time_created = None
                self.trap = None
                self.type = None
                self.username = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:reg-policies/Cisco-IOS-XR-ha-eem-policy-oper:reg-policy[Cisco-IOS-XR-ha-eem-policy-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.class_ is not None:
                    return True

                if self.description is not None:
                    return True

                if self.event_type is not None:
                    return True

                if self.persist_time is not None:
                    return True

                if self.policy_name is not None:
                    return True

                if self.time_created is not None:
                    return True

                if self.trap is not None:
                    return True

                if self.type is not None:
                    return True

                if self.username is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
                return meta._meta_table['Eem.RegPolicies.RegPolicy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:reg-policies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.reg_policy is not None:
                for child_ref in self.reg_policy:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
            return meta._meta_table['Eem.RegPolicies']['meta_info']


    class AvlPolicies(object):
        """
        list the available policies
        
        .. attribute:: avl_policy
        
        	policy name and create time 
        	**type**\: list of    :py:class:`AvlPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.AvlPolicies.AvlPolicy>`
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            self.parent = None
            self.avl_policy = YList()
            self.avl_policy.parent = self
            self.avl_policy.name = 'avl_policy'


        class AvlPolicy(object):
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
                self.parent = None
                self.name = None
                self.policy_name = None
                self.time_created = None
                self.type = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:avl-policies/Cisco-IOS-XR-ha-eem-policy-oper:avl-policy[Cisco-IOS-XR-ha-eem-policy-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.policy_name is not None:
                    return True

                if self.time_created is not None:
                    return True

                if self.type is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
                return meta._meta_table['Eem.AvlPolicies.AvlPolicy']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ha-eem-policy-oper:eem/Cisco-IOS-XR-ha-eem-policy-oper:avl-policies'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.avl_policy is not None:
                for child_ref in self.avl_policy:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
            return meta._meta_table['Eem.AvlPolicies']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ha-eem-policy-oper:eem'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.avl_policies is not None and self.avl_policies._has_data():
            return True

        if self.dir_user is not None and self.dir_user._has_data():
            return True

        if self.env_variables is not None and self.env_variables._has_data():
            return True

        if self.refresh_time is not None and self.refresh_time._has_data():
            return True

        if self.reg_policies is not None and self.reg_policies._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ha_eem_policy_oper as meta
        return meta._meta_table['Eem']['meta_info']


