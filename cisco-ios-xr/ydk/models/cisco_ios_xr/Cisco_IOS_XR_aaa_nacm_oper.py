""" Cisco_IOS_XR_aaa_nacm_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-nacm package operational data.

This module contains definitions
for the following management objects\:
  aaa\-nacm\: AAA Nacm Information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class AaaNacm(Entity):
    """
    AAA Nacm Information
    
    .. attribute:: counters
    
    	AAA NACM summary
    	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Counters>`
    
    .. attribute:: users
    
    	AAA NACM User summary
    	**type**\:  :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Users>`
    
    .. attribute:: summary
    
    	AAA NACM summary
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Summary>`
    
    .. attribute:: rules
    
    	AAA NACM Rulelist summary
    	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Rules>`
    
    .. attribute:: groups
    
    	AAA NACM Group summary
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Groups>`
    
    

    """

    _prefix = 'aaa-nacm-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(AaaNacm, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa-nacm"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-nacm-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("counters", ("counters", AaaNacm.Counters)), ("users", ("users", AaaNacm.Users)), ("summary", ("summary", AaaNacm.Summary)), ("rules", ("rules", AaaNacm.Rules)), ("groups", ("groups", AaaNacm.Groups))])
        self._leafs = OrderedDict()

        self.counters = AaaNacm.Counters()
        self.counters.parent = self
        self._children_name_map["counters"] = "counters"

        self.users = AaaNacm.Users()
        self.users.parent = self
        self._children_name_map["users"] = "users"

        self.summary = AaaNacm.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.rules = AaaNacm.Rules()
        self.rules.parent = self
        self._children_name_map["rules"] = "rules"

        self.groups = AaaNacm.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AaaNacm, [], name, value)


    class Counters(Entity):
        """
        AAA NACM summary
        
        .. attribute:: denied_operations
        
        	Denied Operations
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: denied_data_writes
        
        	Denied Data Writes
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: denied_notifications
        
        	Denied Notifications
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        

        """

        _prefix = 'aaa-nacm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AaaNacm.Counters, self).__init__()

            self.yang_name = "counters"
            self.yang_parent_name = "aaa-nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('denied_operations', (YLeaf(YType.int32, 'denied-operations'), ['int'])),
                ('denied_data_writes', (YLeaf(YType.int32, 'denied-data-writes'), ['int'])),
                ('denied_notifications', (YLeaf(YType.int32, 'denied-notifications'), ['int'])),
            ])
            self.denied_operations = None
            self.denied_data_writes = None
            self.denied_notifications = None
            self._segment_path = lambda: "counters"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AaaNacm.Counters, ['denied_operations', 'denied_data_writes', 'denied_notifications'], name, value)


    class Users(Entity):
        """
        AAA NACM User summary
        
        .. attribute:: user
        
        	AAA NACM User detail
        	**type**\: list of  		 :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Users.User>`
        
        

        """

        _prefix = 'aaa-nacm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AaaNacm.Users, self).__init__()

            self.yang_name = "users"
            self.yang_parent_name = "aaa-nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("user", ("user", AaaNacm.Users.User))])
            self._leafs = OrderedDict()

            self.user = YList(self)
            self._segment_path = lambda: "users"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AaaNacm.Users, [], name, value)


        class User(Entity):
            """
            AAA NACM User detail
            
            .. attribute:: user  (key)
            
            	User
            	**type**\: str
            
            	**length:** 1..256
            
            .. attribute:: user_name
            
            	User Name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: group_name
            
            	Group Name List
            	**type**\: list of  		 :py:class:`GroupName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Users.User.GroupName>`
            
            

            """

            _prefix = 'aaa-nacm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AaaNacm.Users.User, self).__init__()

                self.yang_name = "user"
                self.yang_parent_name = "users"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['user']
                self._child_classes = OrderedDict([("group-name", ("group_name", AaaNacm.Users.User.GroupName))])
                self._leafs = OrderedDict([
                    ('user', (YLeaf(YType.str, 'user'), ['str'])),
                    ('user_name', (YLeaf(YType.str, 'user-name'), ['str'])),
                ])
                self.user = None
                self.user_name = None

                self.group_name = YList(self)
                self._segment_path = lambda: "user" + "[user='" + str(self.user) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/users/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AaaNacm.Users.User, ['user', 'user_name'], name, value)


            class GroupName(Entity):
                """
                Group Name List
                
                .. attribute:: name
                
                	Name
                	**type**\: str
                
                	**length:** 0..256
                
                

                """

                _prefix = 'aaa-nacm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AaaNacm.Users.User.GroupName, self).__init__()

                    self.yang_name = "group-name"
                    self.yang_parent_name = "user"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None
                    self._segment_path = lambda: "group-name"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AaaNacm.Users.User.GroupName, ['name'], name, value)


    class Summary(Entity):
        """
        AAA NACM summary
        
        .. attribute:: groups
        
        	Groups
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: users
        
        	Users
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: rulelist
        
        	Rulelist
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: rules
        
        	Rules
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: read_default
        
        	Read Default
        	**type**\: str
        
        	**length:** 0..16
        
        .. attribute:: write_default
        
        	Write Default
        	**type**\: str
        
        	**length:** 0..16
        
        .. attribute:: exec_default
        
        	Exec Default
        	**type**\: str
        
        	**length:** 0..16
        
        .. attribute:: enable_nacm
        
        	Enable Nacm
        	**type**\: str
        
        	**length:** 0..16
        
        .. attribute:: enable_external_groups
        
        	Enable External Groups
        	**type**\: str
        
        	**length:** 0..16
        
        

        """

        _prefix = 'aaa-nacm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AaaNacm.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "aaa-nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('groups', (YLeaf(YType.int32, 'groups'), ['int'])),
                ('users', (YLeaf(YType.int32, 'users'), ['int'])),
                ('rulelist', (YLeaf(YType.int32, 'rulelist'), ['int'])),
                ('rules', (YLeaf(YType.int32, 'rules'), ['int'])),
                ('read_default', (YLeaf(YType.str, 'read-default'), ['str'])),
                ('write_default', (YLeaf(YType.str, 'write-default'), ['str'])),
                ('exec_default', (YLeaf(YType.str, 'exec-default'), ['str'])),
                ('enable_nacm', (YLeaf(YType.str, 'enable-nacm'), ['str'])),
                ('enable_external_groups', (YLeaf(YType.str, 'enable-external-groups'), ['str'])),
            ])
            self.groups = None
            self.users = None
            self.rulelist = None
            self.rules = None
            self.read_default = None
            self.write_default = None
            self.exec_default = None
            self.enable_nacm = None
            self.enable_external_groups = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AaaNacm.Summary, ['groups', 'users', 'rulelist', 'rules', 'read_default', 'write_default', 'exec_default', 'enable_nacm', 'enable_external_groups'], name, value)


    class Rules(Entity):
        """
        AAA NACM Rulelist summary
        
        .. attribute:: rule
        
        	AAA NACM Rulelist detail
        	**type**\: list of  		 :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Rules.Rule>`
        
        

        """

        _prefix = 'aaa-nacm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AaaNacm.Rules, self).__init__()

            self.yang_name = "rules"
            self.yang_parent_name = "aaa-nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rule", ("rule", AaaNacm.Rules.Rule))])
            self._leafs = OrderedDict()

            self.rule = YList(self)
            self._segment_path = lambda: "rules"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AaaNacm.Rules, [], name, value)


        class Rule(Entity):
            """
            AAA NACM Rulelist detail
            
            .. attribute:: rulelist_rules
            
            	AAA NACM Rulelist detail
            	**type**\:  :py:class:`RulelistRules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Rules.Rule.RulelistRules>`
            
            .. attribute:: ordering_index
            
            	Rulelist Ordering Index
            	**type**\: str
            
            	**length:** 1..256
            
            .. attribute:: rulelist_name
            
            	Rulelist Name
            	**type**\: str
            
            	**length:** 1..256
            
            

            """

            _prefix = 'aaa-nacm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AaaNacm.Rules.Rule, self).__init__()

                self.yang_name = "rule"
                self.yang_parent_name = "rules"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rulelist-rules", ("rulelist_rules", AaaNacm.Rules.Rule.RulelistRules))])
                self._leafs = OrderedDict([
                    ('ordering_index', (YLeaf(YType.str, 'ordering-index'), ['str'])),
                    ('rulelist_name', (YLeaf(YType.str, 'rulelist-name'), ['str'])),
                ])
                self.ordering_index = None
                self.rulelist_name = None

                self.rulelist_rules = AaaNacm.Rules.Rule.RulelistRules()
                self.rulelist_rules.parent = self
                self._children_name_map["rulelist_rules"] = "rulelist-rules"
                self._segment_path = lambda: "rule"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/rules/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AaaNacm.Rules.Rule, ['ordering_index', 'rulelist_name'], name, value)


            class RulelistRules(Entity):
                """
                AAA NACM Rulelist detail
                
                .. attribute:: rulelist_rule
                
                	AAA NACM Rulelist detail
                	**type**\: list of  		 :py:class:`RulelistRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Rules.Rule.RulelistRules.RulelistRule>`
                
                

                """

                _prefix = 'aaa-nacm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AaaNacm.Rules.Rule.RulelistRules, self).__init__()

                    self.yang_name = "rulelist-rules"
                    self.yang_parent_name = "rule"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rulelist-rule", ("rulelist_rule", AaaNacm.Rules.Rule.RulelistRules.RulelistRule))])
                    self._leafs = OrderedDict()

                    self.rulelist_rule = YList(self)
                    self._segment_path = lambda: "rulelist-rules"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/rules/rule/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AaaNacm.Rules.Rule.RulelistRules, [], name, value)


                class RulelistRule(Entity):
                    """
                    AAA NACM Rulelist detail
                    
                    .. attribute:: rule  (key)
                    
                    	Rule
                    	**type**\: str
                    
                    	**length:** 1..256
                    
                    .. attribute:: rule_name
                    
                    	Rule Name
                    	**type**\: str
                    
                    	**length:** 0..512
                    
                    .. attribute:: rule_index
                    
                    	Rule Index
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    .. attribute:: rulelist_index
                    
                    	Rulelist Index
                    	**type**\: str
                    
                    	**length:** 0..16
                    
                    .. attribute:: module_name
                    
                    	Module Name
                    	**type**\: str
                    
                    	**length:** 0..512
                    
                    .. attribute:: action
                    
                    	Action
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: rule_type
                    
                    	Rule Type
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: comment
                    
                    	Comment
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: access_operations
                    
                    	Access Operations
                    	**type**\: str
                    
                    	**length:** 0..256
                    
                    .. attribute:: rule_value
                    
                    	Rule Value
                    	**type**\: str
                    
                    	**length:** 0..512
                    
                    .. attribute:: hit_count
                    
                    	Hit Count
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'aaa-nacm-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(AaaNacm.Rules.Rule.RulelistRules.RulelistRule, self).__init__()

                        self.yang_name = "rulelist-rule"
                        self.yang_parent_name = "rulelist-rules"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rule']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rule', (YLeaf(YType.str, 'rule'), ['str'])),
                            ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                            ('rule_index', (YLeaf(YType.str, 'rule-index'), ['str'])),
                            ('rulelist_index', (YLeaf(YType.str, 'rulelist-index'), ['str'])),
                            ('module_name', (YLeaf(YType.str, 'module-name'), ['str'])),
                            ('action', (YLeaf(YType.str, 'action'), ['str'])),
                            ('rule_type', (YLeaf(YType.str, 'rule-type'), ['str'])),
                            ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
                            ('access_operations', (YLeaf(YType.str, 'access-operations'), ['str'])),
                            ('rule_value', (YLeaf(YType.str, 'rule-value'), ['str'])),
                            ('hit_count', (YLeaf(YType.int32, 'hit-count'), ['int'])),
                        ])
                        self.rule = None
                        self.rule_name = None
                        self.rule_index = None
                        self.rulelist_index = None
                        self.module_name = None
                        self.action = None
                        self.rule_type = None
                        self.comment = None
                        self.access_operations = None
                        self.rule_value = None
                        self.hit_count = None
                        self._segment_path = lambda: "rulelist-rule" + "[rule='" + str(self.rule) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/rules/rule/rulelist-rules/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AaaNacm.Rules.Rule.RulelistRules.RulelistRule, ['rule', 'rule_name', 'rule_index', 'rulelist_index', 'module_name', 'action', 'rule_type', 'comment', 'access_operations', 'rule_value', 'hit_count'], name, value)


    class Groups(Entity):
        """
        AAA NACM Group summary
        
        .. attribute:: group
        
        	AAA NACM Group detail
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Groups.Group>`
        
        

        """

        _prefix = 'aaa-nacm-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(AaaNacm.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "aaa-nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("group", ("group", AaaNacm.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AaaNacm.Groups, [], name, value)


        class Group(Entity):
            """
            AAA NACM Group detail
            
            .. attribute:: group  (key)
            
            	Group
            	**type**\: str
            
            	**length:** 1..256
            
            .. attribute:: group_name
            
            	Group Name
            	**type**\: str
            
            	**length:** 0..256
            
            .. attribute:: user_name
            
            	Users Name List
            	**type**\: list of  		 :py:class:`UserName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Groups.Group.UserName>`
            
            .. attribute:: rule_name
            
            	Rules Name List
            	**type**\: list of  		 :py:class:`RuleName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_oper.AaaNacm.Groups.Group.RuleName>`
            
            

            """

            _prefix = 'aaa-nacm-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(AaaNacm.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group']
                self._child_classes = OrderedDict([("user-name", ("user_name", AaaNacm.Groups.Group.UserName)), ("rule-name", ("rule_name", AaaNacm.Groups.Group.RuleName))])
                self._leafs = OrderedDict([
                    ('group', (YLeaf(YType.str, 'group'), ['str'])),
                    ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                ])
                self.group = None
                self.group_name = None

                self.user_name = YList(self)
                self.rule_name = YList(self)
                self._segment_path = lambda: "group" + "[group='" + str(self.group) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-oper:aaa-nacm/groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AaaNacm.Groups.Group, ['group', 'group_name'], name, value)


            class UserName(Entity):
                """
                Users Name List
                
                .. attribute:: name
                
                	Name
                	**type**\: str
                
                	**length:** 0..256
                
                

                """

                _prefix = 'aaa-nacm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AaaNacm.Groups.Group.UserName, self).__init__()

                    self.yang_name = "user-name"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None
                    self._segment_path = lambda: "user-name"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AaaNacm.Groups.Group.UserName, ['name'], name, value)


            class RuleName(Entity):
                """
                Rules Name List
                
                .. attribute:: name
                
                	Name
                	**type**\: str
                
                	**length:** 0..256
                
                

                """

                _prefix = 'aaa-nacm-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(AaaNacm.Groups.Group.RuleName, self).__init__()

                    self.yang_name = "rule-name"
                    self.yang_parent_name = "group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ])
                    self.name = None
                    self._segment_path = lambda: "rule-name"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AaaNacm.Groups.Group.RuleName, ['name'], name, value)

    def clone_ptr(self):
        self._top_entity = AaaNacm()
        return self._top_entity

