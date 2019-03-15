""" Cisco_IOS_XR_ha_eem_policy_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ha\-eem\-policy package operational data.

This module contains definitions
for the following management objects\:
  eem\: EEM operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Eem(Entity):
    """
    EEM operational data
    
    .. attribute:: dir_user
    
    	directory user
    	**type**\:  :py:class:`DirUser <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.DirUser>`
    
    	**config**\: False
    
    .. attribute:: env_variables
    
    	list of environmental variables
    	**type**\:  :py:class:`EnvVariables <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.EnvVariables>`
    
    	**config**\: False
    
    .. attribute:: refresh_time
    
    	Refresh time
    	**type**\:  :py:class:`RefreshTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.RefreshTime>`
    
    	**config**\: False
    
    .. attribute:: reg_policies
    
    	list the registered policies
    	**type**\:  :py:class:`RegPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.RegPolicies>`
    
    	**config**\: False
    
    .. attribute:: avl_policies
    
    	list the available policies
    	**type**\:  :py:class:`AvlPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.AvlPolicies>`
    
    	**config**\: False
    
    

    """

    _prefix = 'ha-eem-policy-oper'
    _revision = '2016-02-05'

    def __init__(self):
        super(Eem, self).__init__()
        self._top_entity = None

        self.yang_name = "eem"
        self.yang_parent_name = "Cisco-IOS-XR-ha-eem-policy-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("dir-user", ("dir_user", Eem.DirUser)), ("env-variables", ("env_variables", Eem.EnvVariables)), ("refresh-time", ("refresh_time", Eem.RefreshTime)), ("reg-policies", ("reg_policies", Eem.RegPolicies)), ("avl-policies", ("avl_policies", Eem.AvlPolicies))])
        self._leafs = OrderedDict()

        self.dir_user = Eem.DirUser()
        self.dir_user.parent = self
        self._children_name_map["dir_user"] = "dir-user"

        self.env_variables = Eem.EnvVariables()
        self.env_variables.parent = self
        self._children_name_map["env_variables"] = "env-variables"

        self.refresh_time = Eem.RefreshTime()
        self.refresh_time.parent = self
        self._children_name_map["refresh_time"] = "refresh-time"

        self.reg_policies = Eem.RegPolicies()
        self.reg_policies.parent = self
        self._children_name_map["reg_policies"] = "reg-policies"

        self.avl_policies = Eem.AvlPolicies()
        self.avl_policies.parent = self
        self._children_name_map["avl_policies"] = "avl-policies"
        self._segment_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Eem, [], name, value)


    class DirUser(Entity):
        """
        directory user
        
        .. attribute:: library
        
        	directory user library
        	**type**\:  :py:class:`Library <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.DirUser.Library>`
        
        	**config**\: False
        
        .. attribute:: policy
        
        	directory user policy
        	**type**\:  :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.DirUser.Policy>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.DirUser, self).__init__()

            self.yang_name = "dir-user"
            self.yang_parent_name = "eem"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("library", ("library", Eem.DirUser.Library)), ("policy", ("policy", Eem.DirUser.Policy))])
            self._leafs = OrderedDict()

            self.library = Eem.DirUser.Library()
            self.library.parent = self
            self._children_name_map["library"] = "library"

            self.policy = Eem.DirUser.Policy()
            self.policy.parent = self
            self._children_name_map["policy"] = "policy"
            self._segment_path = lambda: "dir-user"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eem.DirUser, [], name, value)


        class Library(Entity):
            """
            directory user library
            
            .. attribute:: policy
            
            	policy
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: library
            
            	library
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.DirUser.Library, self).__init__()

                self.yang_name = "library"
                self.yang_parent_name = "dir-user"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('policy', (YLeaf(YType.str, 'policy'), ['str'])),
                    ('library', (YLeaf(YType.str, 'library'), ['str'])),
                ])
                self.policy = None
                self.library = None
                self._segment_path = lambda: "library"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/dir-user/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eem.DirUser.Library, ['policy', 'library'], name, value)



        class Policy(Entity):
            """
            directory user policy
            
            .. attribute:: policy
            
            	policy
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: library
            
            	library
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.DirUser.Policy, self).__init__()

                self.yang_name = "policy"
                self.yang_parent_name = "dir-user"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('policy', (YLeaf(YType.str, 'policy'), ['str'])),
                    ('library', (YLeaf(YType.str, 'library'), ['str'])),
                ])
                self.policy = None
                self.library = None
                self._segment_path = lambda: "policy"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/dir-user/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eem.DirUser.Policy, ['policy', 'library'], name, value)




    class EnvVariables(Entity):
        """
        list of environmental variables
        
        .. attribute:: env_variable
        
        	environmental variables name and value 
        	**type**\: list of  		 :py:class:`EnvVariable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.EnvVariables.EnvVariable>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.EnvVariables, self).__init__()

            self.yang_name = "env-variables"
            self.yang_parent_name = "eem"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("env-variable", ("env_variable", Eem.EnvVariables.EnvVariable))])
            self._leafs = OrderedDict()

            self.env_variable = YList(self)
            self._segment_path = lambda: "env-variables"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eem.EnvVariables, [], name, value)


        class EnvVariable(Entity):
            """
            environmental variables name and value 
            
            .. attribute:: name  (key)
            
            	Environmental variable name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: name_xr
            
            	variable name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: value
            
            	value
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.EnvVariables.EnvVariable, self).__init__()

                self.yang_name = "env-variable"
                self.yang_parent_name = "env-variables"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('name_xr', (YLeaf(YType.str, 'name-xr'), ['str'])),
                    ('value', (YLeaf(YType.str, 'value'), ['str'])),
                ])
                self.name = None
                self.name_xr = None
                self.value = None
                self._segment_path = lambda: "env-variable" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/env-variables/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eem.EnvVariables.EnvVariable, ['name', 'name_xr', 'value'], name, value)




    class RefreshTime(Entity):
        """
        Refresh time
        
        .. attribute:: refreshtime
        
        	Event manager refresh\-time 
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.RefreshTime, self).__init__()

            self.yang_name = "refresh-time"
            self.yang_parent_name = "eem"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('refreshtime', (YLeaf(YType.uint32, 'refreshtime'), ['int'])),
            ])
            self.refreshtime = None
            self._segment_path = lambda: "refresh-time"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eem.RefreshTime, ['refreshtime'], name, value)



    class RegPolicies(Entity):
        """
        list the registered policies
        
        .. attribute:: reg_policy
        
        	policy name and create time 
        	**type**\: list of  		 :py:class:`RegPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.RegPolicies.RegPolicy>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.RegPolicies, self).__init__()

            self.yang_name = "reg-policies"
            self.yang_parent_name = "eem"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("reg-policy", ("reg_policy", Eem.RegPolicies.RegPolicy))])
            self._leafs = OrderedDict()

            self.reg_policy = YList(self)
            self._segment_path = lambda: "reg-policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eem.RegPolicies, [], name, value)


        class RegPolicy(Entity):
            """
            policy name and create time 
            
            .. attribute:: name  (key)
            
            	policy name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: type
            
            	policy type
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: time_created
            
            	time created
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: policy_name
            
            	policy name
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: class_
            
            	class
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: event_type
            
            	event type
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: trap
            
            	trap
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: persist_time
            
            	PersistTime 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: username
            
            	username
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: description
            
            	description
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.RegPolicies.RegPolicy, self).__init__()

                self.yang_name = "reg-policy"
                self.yang_parent_name = "reg-policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                    ('time_created', (YLeaf(YType.str, 'time-created'), ['str'])),
                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                    ('class_', (YLeaf(YType.str, 'class'), ['str'])),
                    ('event_type', (YLeaf(YType.str, 'event-type'), ['str'])),
                    ('trap', (YLeaf(YType.str, 'trap'), ['str'])),
                    ('persist_time', (YLeaf(YType.uint32, 'persist-time'), ['int'])),
                    ('username', (YLeaf(YType.str, 'username'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ])
                self.name = None
                self.type = None
                self.time_created = None
                self.policy_name = None
                self.class_ = None
                self.event_type = None
                self.trap = None
                self.persist_time = None
                self.username = None
                self.description = None
                self._segment_path = lambda: "reg-policy" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/reg-policies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eem.RegPolicies.RegPolicy, ['name', 'type', 'time_created', 'policy_name', 'class_', 'event_type', 'trap', 'persist_time', 'username', 'description'], name, value)




    class AvlPolicies(Entity):
        """
        list the available policies
        
        .. attribute:: avl_policy
        
        	policy name and create time 
        	**type**\: list of  		 :py:class:`AvlPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper.Eem.AvlPolicies.AvlPolicy>`
        
        	**config**\: False
        
        

        """

        _prefix = 'ha-eem-policy-oper'
        _revision = '2016-02-05'

        def __init__(self):
            super(Eem.AvlPolicies, self).__init__()

            self.yang_name = "avl-policies"
            self.yang_parent_name = "eem"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("avl-policy", ("avl_policy", Eem.AvlPolicies.AvlPolicy))])
            self._leafs = OrderedDict()

            self.avl_policy = YList(self)
            self._segment_path = lambda: "avl-policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eem.AvlPolicies, [], name, value)


        class AvlPolicy(Entity):
            """
            policy name and create time 
            
            .. attribute:: name  (key)
            
            	System policy name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            	**config**\: False
            
            .. attribute:: type
            
            	policy type
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: time_created
            
            	time created
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: policy_name
            
            	policy name
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'ha-eem-policy-oper'
            _revision = '2016-02-05'

            def __init__(self):
                super(Eem.AvlPolicies.AvlPolicy, self).__init__()

                self.yang_name = "avl-policy"
                self.yang_parent_name = "avl-policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('type', (YLeaf(YType.str, 'type'), ['str'])),
                    ('time_created', (YLeaf(YType.str, 'time-created'), ['str'])),
                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                ])
                self.name = None
                self.type = None
                self.time_created = None
                self.policy_name = None
                self._segment_path = lambda: "avl-policy" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ha-eem-policy-oper:eem/avl-policies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eem.AvlPolicies.AvlPolicy, ['name', 'type', 'time_created', 'policy_name'], name, value)



    def clone_ptr(self):
        self._top_entity = Eem()
        return self._top_entity



