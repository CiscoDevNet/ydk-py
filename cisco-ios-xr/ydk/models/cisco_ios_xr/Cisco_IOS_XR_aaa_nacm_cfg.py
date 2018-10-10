""" Cisco_IOS_XR_aaa_nacm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-nacm package configuration.

This module contains definitions
for the following management objects\:
  nacm\: Parameters for NETCONF Access Control Model

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NacmAction(Enum):
    """
    NacmAction (Enum Class)

    Nacm action

    .. data:: permit = 0

    	Permit

    .. data:: deny = 1

    	Deny

    """

    permit = Enum.YLeaf(0, "permit")

    deny = Enum.YLeaf(1, "deny")


class NacmRule(Enum):
    """
    NacmRule (Enum Class)

    Nacm rule

    .. data:: protocol_operation = 0

    	Protocoloperation

    .. data:: data_node = 1

    	Datanode

    .. data:: notification = 2

    	Notification

    """

    protocol_operation = Enum.YLeaf(0, "protocol-operation")

    data_node = Enum.YLeaf(1, "data-node")

    notification = Enum.YLeaf(2, "notification")



class Nacm(Entity):
    """
    Parameters for NETCONF Access Control Model
    
    .. attribute:: groups
    
    	NETCONF Access Control Groups
    	**type**\:  :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.Groups>`
    
    .. attribute:: rulelist_classes
    
    	Contains all rule lists of NACM
    	**type**\:  :py:class:`RulelistClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.RulelistClasses>`
    
    .. attribute:: enable_nacm
    
    	Enables or Disables all NETCONF access control enforcement
    	**type**\: bool
    
    .. attribute:: write_default
    
    	Controls write access if no appropriate rule is found
    	**type**\:  :py:class:`NacmAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.NacmAction>`
    
    .. attribute:: exec_default
    
    	Controls exec access if no appropriate rule is found
    	**type**\:  :py:class:`NacmAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.NacmAction>`
    
    .. attribute:: enable_external_groups
    
    	Controls whether the server uses the groups reported by NETCONF transport layer
    	**type**\: bool
    
    .. attribute:: read_default
    
    	Controls read access if no appropriate rule is found
    	**type**\:  :py:class:`NacmAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.NacmAction>`
    
    

    """

    _prefix = 'aaa-nacm-cfg'
    _revision = '2017-09-30'

    def __init__(self):
        super(Nacm, self).__init__()
        self._top_entity = None

        self.yang_name = "nacm"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-nacm-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("groups", ("groups", Nacm.Groups)), ("rulelist-classes", ("rulelist_classes", Nacm.RulelistClasses))])
        self._leafs = OrderedDict([
            ('enable_nacm', (YLeaf(YType.boolean, 'enable-nacm'), ['bool'])),
            ('write_default', (YLeaf(YType.enumeration, 'write-default'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction', '')])),
            ('exec_default', (YLeaf(YType.enumeration, 'exec-default'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction', '')])),
            ('enable_external_groups', (YLeaf(YType.boolean, 'enable-external-groups'), ['bool'])),
            ('read_default', (YLeaf(YType.enumeration, 'read-default'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction', '')])),
        ])
        self.enable_nacm = None
        self.write_default = None
        self.exec_default = None
        self.enable_external_groups = None
        self.read_default = None

        self.groups = Nacm.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"

        self.rulelist_classes = Nacm.RulelistClasses()
        self.rulelist_classes.parent = self
        self._children_name_map["rulelist_classes"] = "rulelist-classes"
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-nacm-cfg:nacm"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Nacm, ['enable_nacm', 'write_default', 'exec_default', 'enable_external_groups', 'read_default'], name, value)


    class Groups(Entity):
        """
        NETCONF Access Control Groups
        
        .. attribute:: group
        
        	One NACM Group Entry
        	**type**\: list of  		 :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.Groups.Group>`
        
        

        """

        _prefix = 'aaa-nacm-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Nacm.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("group", ("group", Nacm.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-cfg:nacm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Nacm.Groups, [], name, value)


        class Group(Entity):
            """
            One NACM Group Entry
            
            .. attribute:: group_name  (key)
            
            	User group name
            	**type**\: str
            
            	**length:** 1..63
            
            .. attribute:: user_name
            
            	User name
            	**type**\: list of str
            
            	**length:** 1..63
            
            

            """

            _prefix = 'aaa-nacm-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(Nacm.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['group_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                    ('user_name', (YLeafList(YType.str, 'user-name'), ['str'])),
                ])
                self.group_name = None
                self.user_name = []
                self._segment_path = lambda: "group" + "[group-name='" + str(self.group_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-cfg:nacm/groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Nacm.Groups.Group, ['group_name', 'user_name'], name, value)


    class RulelistClasses(Entity):
        """
        Contains all rule lists of NACM
        
        .. attribute:: rulelist_class
        
        	Each rule list of NACM
        	**type**\: list of  		 :py:class:`RulelistClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.RulelistClasses.RulelistClass>`
        
        

        """

        _prefix = 'aaa-nacm-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Nacm.RulelistClasses, self).__init__()

            self.yang_name = "rulelist-classes"
            self.yang_parent_name = "nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rulelist-class", ("rulelist_class", Nacm.RulelistClasses.RulelistClass))])
            self._leafs = OrderedDict()

            self.rulelist_class = YList(self)
            self._segment_path = lambda: "rulelist-classes"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-cfg:nacm/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Nacm.RulelistClasses, [], name, value)


        class RulelistClass(Entity):
            """
            Each rule list of NACM
            
            .. attribute:: ordering_index  (key)
            
            	This is used to sort the rulelists in the order of precedence
            	**type**\: str
            
            	**length:** 1..15
            
            .. attribute:: rulelist_name  (key)
            
            	Rulelist key name
            	**type**\: str
            
            	**length:** 1..63
            
            .. attribute:: group_names
            
            	List of groups that will be assigned with the rule
            	**type**\:  :py:class:`GroupNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.RulelistClasses.RulelistClass.GroupNames>`
            
            .. attribute:: rules
            
            	Set of rules in a rulelist
            	**type**\:  :py:class:`Rules <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.RulelistClasses.RulelistClass.Rules>`
            
            

            """

            _prefix = 'aaa-nacm-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(Nacm.RulelistClasses.RulelistClass, self).__init__()

                self.yang_name = "rulelist-class"
                self.yang_parent_name = "rulelist-classes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ordering_index','rulelist_name']
                self._child_classes = OrderedDict([("group-names", ("group_names", Nacm.RulelistClasses.RulelistClass.GroupNames)), ("rules", ("rules", Nacm.RulelistClasses.RulelistClass.Rules))])
                self._leafs = OrderedDict([
                    ('ordering_index', (YLeaf(YType.str, 'ordering-index'), ['str'])),
                    ('rulelist_name', (YLeaf(YType.str, 'rulelist-name'), ['str'])),
                ])
                self.ordering_index = None
                self.rulelist_name = None

                self.group_names = Nacm.RulelistClasses.RulelistClass.GroupNames()
                self.group_names.parent = self
                self._children_name_map["group_names"] = "group-names"

                self.rules = Nacm.RulelistClasses.RulelistClass.Rules()
                self.rules.parent = self
                self._children_name_map["rules"] = "rules"
                self._segment_path = lambda: "rulelist-class" + "[ordering-index='" + str(self.ordering_index) + "']" + "[rulelist-name='" + str(self.rulelist_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-nacm-cfg:nacm/rulelist-classes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Nacm.RulelistClasses.RulelistClass, ['ordering_index', 'rulelist_name'], name, value)


            class GroupNames(Entity):
                """
                List of groups that will be assigned with the
                rule
                
                .. attribute:: group_name
                
                	Group name
                	**type**\: list of str
                
                	**length:** 1..63
                
                

                """

                _prefix = 'aaa-nacm-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Nacm.RulelistClasses.RulelistClass.GroupNames, self).__init__()

                    self.yang_name = "group-names"
                    self.yang_parent_name = "rulelist-class"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('group_name', (YLeafList(YType.str, 'group-name'), ['str'])),
                    ])
                    self.group_name = []
                    self._segment_path = lambda: "group-names"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Nacm.RulelistClasses.RulelistClass.GroupNames, ['group_name'], name, value)


            class Rules(Entity):
                """
                Set of rules in a rulelist
                
                .. attribute:: rule
                
                	Each rule in a rulelist
                	**type**\: list of  		 :py:class:`Rule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.RulelistClasses.RulelistClass.Rules.Rule>`
                
                

                """

                _prefix = 'aaa-nacm-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Nacm.RulelistClasses.RulelistClass.Rules, self).__init__()

                    self.yang_name = "rules"
                    self.yang_parent_name = "rulelist-class"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rule", ("rule", Nacm.RulelistClasses.RulelistClass.Rules.Rule))])
                    self._leafs = OrderedDict()

                    self.rule = YList(self)
                    self._segment_path = lambda: "rules"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Nacm.RulelistClasses.RulelistClass.Rules, [], name, value)


                class Rule(Entity):
                    """
                    Each rule in a rulelist
                    
                    .. attribute:: ordering_index  (key)
                    
                    	This is used to sort the rules in the order of precedence
                    	**type**\: str
                    
                    	**length:** 1..15
                    
                    .. attribute:: rule_name  (key)
                    
                    	Rule name
                    	**type**\: str
                    
                    	**length:** 1..63
                    
                    .. attribute:: rule_type
                    
                    	Rule Type associated with this rule
                    	**type**\:  :py:class:`RuleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType>`
                    
                    .. attribute:: access_operations
                    
                    	Access operations associated with this rule
                    	**type**\:  :py:class:`AccessOperations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations>`
                    
                    .. attribute:: module_name
                    
                    	Name of the module associated with this rule
                    	**type**\: str
                    
                    	**length:** 1..63
                    
                    .. attribute:: action
                    
                    	The access control action associated with the rule
                    	**type**\:  :py:class:`NacmAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.NacmAction>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: comment
                    
                    	Textual description of the access rule
                    	**type**\: str
                    
                    	**length:** 1..255
                    
                    

                    """

                    _prefix = 'aaa-nacm-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Nacm.RulelistClasses.RulelistClass.Rules.Rule, self).__init__()

                        self.yang_name = "rule"
                        self.yang_parent_name = "rules"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ordering_index','rule_name']
                        self._child_classes = OrderedDict([("rule-type", ("rule_type", Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType)), ("access-operations", ("access_operations", Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations))])
                        self._leafs = OrderedDict([
                            ('ordering_index', (YLeaf(YType.str, 'ordering-index'), ['str'])),
                            ('rule_name', (YLeaf(YType.str, 'rule-name'), ['str'])),
                            ('module_name', (YLeaf(YType.str, 'module-name'), ['str'])),
                            ('action', (YLeaf(YType.enumeration, 'action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmAction', '')])),
                            ('comment', (YLeaf(YType.str, 'comment'), ['str'])),
                        ])
                        self.ordering_index = None
                        self.rule_name = None
                        self.module_name = None
                        self.action = None
                        self.comment = None

                        self.rule_type = Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType()
                        self.rule_type.parent = self
                        self._children_name_map["rule_type"] = "rule-type"

                        self.access_operations = Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations()
                        self.access_operations.parent = self
                        self._children_name_map["access_operations"] = "access-operations"
                        self._segment_path = lambda: "rule" + "[ordering-index='" + str(self.ordering_index) + "']" + "[rule-name='" + str(self.rule_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Nacm.RulelistClasses.RulelistClass.Rules.Rule, ['ordering_index', 'rule_name', 'module_name', 'action', 'comment'], name, value)


                    class RuleType(Entity):
                        """
                        Rule Type associated with this rule
                        
                        .. attribute:: type
                        
                        	Rule Type
                        	**type**\:  :py:class:`NacmRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg.NacmRule>`
                        
                        .. attribute:: value
                        
                        	Rule Value
                        	**type**\: str
                        
                        	**length:** 1..511
                        
                        

                        """

                        _prefix = 'aaa-nacm-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType, self).__init__()

                            self.yang_name = "rule-type"
                            self.yang_parent_name = "rule"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_nacm_cfg', 'NacmRule', '')])),
                                ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ])
                            self.type = None
                            self.value = None
                            self._segment_path = lambda: "rule-type"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Nacm.RulelistClasses.RulelistClass.Rules.Rule.RuleType, ['type', 'value'], name, value)


                    class AccessOperations(Entity):
                        """
                        Access operations associated with this rule
                        
                        .. attribute:: create
                        
                        	Enable Create
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: read
                        
                        	Enable Read
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: update
                        
                        	Enable Update
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delete
                        
                        	Enable Delete
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: exec_
                        
                        	Enable Exec
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: all
                        
                        	Enable All permissions
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'aaa-nacm-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations, self).__init__()

                            self.yang_name = "access-operations"
                            self.yang_parent_name = "rule"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('create', (YLeaf(YType.uint32, 'create'), ['int'])),
                                ('read', (YLeaf(YType.uint32, 'read'), ['int'])),
                                ('update', (YLeaf(YType.uint32, 'update'), ['int'])),
                                ('delete', (YLeaf(YType.uint32, 'delete'), ['int'])),
                                ('exec_', (YLeaf(YType.uint32, 'exec'), ['int'])),
                                ('all', (YLeaf(YType.uint32, 'all'), ['int'])),
                            ])
                            self.create = None
                            self.read = None
                            self.update = None
                            self.delete = None
                            self.exec_ = None
                            self.all = None
                            self._segment_path = lambda: "access-operations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Nacm.RulelistClasses.RulelistClass.Rules.Rule.AccessOperations, ['create', 'read', 'update', 'delete', 'exec_', 'all'], name, value)

    def clone_ptr(self):
        self._top_entity = Nacm()
        return self._top_entity

