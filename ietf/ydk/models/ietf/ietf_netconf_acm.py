""" ietf_netconf_acm 

NETCONF Access Control Model.

Copyright (c) 2012 IETF Trust and the persons identified as
authors of the code.  All rights reserved.

Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD
License set forth in Section 4.c of the IETF Trust's
Legal Provisions Relating to IETF Documents
(http\://trustee.ietf.org/license\-info).

This version of this YANG module is part of RFC 6536; see
the RFC itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ActionType(Enum):
    """
    ActionType (Enum Class)

    Action taken by the server when a particular

    rule matches.

    .. data:: permit = 0

    	Requested action is permitted.

    .. data:: deny = 1

    	Requested action is denied.

    """

    permit = Enum.YLeaf(0, "permit")

    deny = Enum.YLeaf(1, "deny")



class Nacm(Entity):
    """
    Parameters for NETCONF Access Control Model.
    
    .. attribute:: enable_nacm
    
    	Enables or disables all NETCONF access control enforcement.  If 'true', then enforcement is enabled.  If 'false', then enforcement is disabled
    	**type**\: bool
    
    	**default value**\: true
    
    .. attribute:: read_default
    
    	Controls whether read access is granted if no appropriate rule is found for a particular read request
    	**type**\:  :py:class:`ActionType <ydk.models.ietf.ietf_netconf_acm.ActionType>`
    
    	**default value**\: permit
    
    .. attribute:: write_default
    
    	Controls whether create, update, or delete access is granted if no appropriate rule is found for a particular write request
    	**type**\:  :py:class:`ActionType <ydk.models.ietf.ietf_netconf_acm.ActionType>`
    
    	**default value**\: deny
    
    .. attribute:: exec_default
    
    	Controls whether exec access is granted if no appropriate rule is found for a particular protocol operation request
    	**type**\:  :py:class:`ActionType <ydk.models.ietf.ietf_netconf_acm.ActionType>`
    
    	**default value**\: permit
    
    .. attribute:: enable_external_groups
    
    	Controls whether the server uses the groups reported by the NETCONF transport layer when it assigns the user to a set of NACM groups.  If this leaf has the value 'false', any group names reported by the transport layer are ignored by the server
    	**type**\: bool
    
    	**default value**\: true
    
    .. attribute:: denied_operations
    
    	Number of times since the server last restarted that a protocol operation request was denied
    	**type**\: int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    .. attribute:: denied_data_writes
    
    	Number of times since the server last restarted that a protocol operation request to alter a configuration datastore was denied
    	**type**\: int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    .. attribute:: denied_notifications
    
    	Number of times since the server last restarted that a notification was dropped for a subscription because access to the event type was denied
    	**type**\: int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    .. attribute:: groups
    
    	NETCONF Access Control Groups
    	**type**\:  :py:class:`Groups <ydk.models.ietf.ietf_netconf_acm.Nacm.Groups>`
    
    .. attribute:: rule_list
    
    	An ordered collection of access control rules
    	**type**\: list of  		 :py:class:`RuleList <ydk.models.ietf.ietf_netconf_acm.Nacm.RuleList>`
    
    

    """

    _prefix = 'nacm'
    _revision = '2012-02-22'

    def __init__(self):
        super(Nacm, self).__init__()
        self._top_entity = None

        self.yang_name = "nacm"
        self.yang_parent_name = "ietf-netconf-acm"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("groups", ("groups", Nacm.Groups))])
        self._child_list_classes = OrderedDict([("rule-list", ("rule_list", Nacm.RuleList))])
        self._leafs = OrderedDict([
            ('enable_nacm', YLeaf(YType.boolean, 'enable-nacm')),
            ('read_default', YLeaf(YType.enumeration, 'read-default')),
            ('write_default', YLeaf(YType.enumeration, 'write-default')),
            ('exec_default', YLeaf(YType.enumeration, 'exec-default')),
            ('enable_external_groups', YLeaf(YType.boolean, 'enable-external-groups')),
            ('denied_operations', YLeaf(YType.uint32, 'denied-operations')),
            ('denied_data_writes', YLeaf(YType.uint32, 'denied-data-writes')),
            ('denied_notifications', YLeaf(YType.uint32, 'denied-notifications')),
        ])
        self.enable_nacm = None
        self.read_default = None
        self.write_default = None
        self.exec_default = None
        self.enable_external_groups = None
        self.denied_operations = None
        self.denied_data_writes = None
        self.denied_notifications = None

        self.groups = Nacm.Groups()
        self.groups.parent = self
        self._children_name_map["groups"] = "groups"
        self._children_yang_names.add("groups")

        self.rule_list = YList(self)
        self._segment_path = lambda: "ietf-netconf-acm:nacm"

    def __setattr__(self, name, value):
        self._perform_setattr(Nacm, ['enable_nacm', 'read_default', 'write_default', 'exec_default', 'enable_external_groups', 'denied_operations', 'denied_data_writes', 'denied_notifications'], name, value)


    class Groups(Entity):
        """
        NETCONF Access Control Groups.
        
        .. attribute:: group
        
        	One NACM Group Entry.  This list will only contain configured entries, not any entries learned from any transport protocols
        	**type**\: list of  		 :py:class:`Group <ydk.models.ietf.ietf_netconf_acm.Nacm.Groups.Group>`
        
        

        """

        _prefix = 'nacm'
        _revision = '2012-02-22'

        def __init__(self):
            super(Nacm.Groups, self).__init__()

            self.yang_name = "groups"
            self.yang_parent_name = "nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("group", ("group", Nacm.Groups.Group))])
            self._leafs = OrderedDict()

            self.group = YList(self)
            self._segment_path = lambda: "groups"
            self._absolute_path = lambda: "ietf-netconf-acm:nacm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Nacm.Groups, [], name, value)


        class Group(Entity):
            """
            One NACM Group Entry.  This list will only contain
            configured entries, not any entries learned from
            any transport protocols.
            
            .. attribute:: name  (key)
            
            	Group name associated with this entry
            	**type**\: str
            
            	**pattern:** [^\\\*].\*
            
            .. attribute:: user_name
            
            	Each entry identifies the username of a member of the group associated with this entry
            	**type**\: list of str
            
            	**length:** 1..18446744073709551615
            
            

            """

            _prefix = 'nacm'
            _revision = '2012-02-22'

            def __init__(self):
                super(Nacm.Groups.Group, self).__init__()

                self.yang_name = "group"
                self.yang_parent_name = "groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('user_name', YLeafList(YType.str, 'user-name')),
                ])
                self.name = None
                self.user_name = []
                self._segment_path = lambda: "group" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "ietf-netconf-acm:nacm/groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Nacm.Groups.Group, ['name', 'user_name'], name, value)


    class RuleList(Entity):
        """
        An ordered collection of access control rules.
        
        .. attribute:: name  (key)
        
        	Arbitrary name assigned to the rule\-list
        	**type**\: str
        
        	**length:** 1..18446744073709551615
        
        .. attribute:: group
        
        	List of administrative groups that will be assigned the associated access rights defined by the 'rule' list.  The string '\*' indicates that all groups apply to the entry
        	**type**\: union of the below types:
        
        		**type**\: list of str
        
        			**pattern:** \\\*
        
        		**type**\: list of str
        
        			**pattern:** [^\\\*].\*
        
        .. attribute:: rule
        
        	One access control rule.  Rules are processed in user\-defined order until a match is found.  A rule matches if 'module\-name', 'rule\-type', and 'access\-operations' match the request.  If a rule matches, the 'action' leaf determines if access is granted or not
        	**type**\: list of  		 :py:class:`Rule <ydk.models.ietf.ietf_netconf_acm.Nacm.RuleList.Rule>`
        
        

        """

        _prefix = 'nacm'
        _revision = '2012-02-22'

        def __init__(self):
            super(Nacm.RuleList, self).__init__()

            self.yang_name = "rule-list"
            self.yang_parent_name = "nacm"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("rule", ("rule", Nacm.RuleList.Rule))])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('group', YLeafList(YType.str, 'group')),
            ])
            self.name = None
            self.group = []

            self.rule = YList(self)
            self._segment_path = lambda: "rule-list" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "ietf-netconf-acm:nacm/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Nacm.RuleList, ['name', 'group'], name, value)


        class Rule(Entity):
            """
            One access control rule.
            
            Rules are processed in user\-defined order until a match is
            found.  A rule matches if 'module\-name', 'rule\-type', and
            'access\-operations' match the request.  If a rule
            matches, the 'action' leaf determines if access is granted
            or not.
            
            .. attribute:: name  (key)
            
            	Arbitrary name assigned to the rule
            	**type**\: str
            
            	**length:** 1..18446744073709551615
            
            .. attribute:: module_name
            
            	Name of the module associated with this rule.  This leaf matches if it has the value '\*' or if the object being accessed is defined in the module with the specified module name
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** \\\*
            
            		**type**\: str
            
            	**default value**\: *
            
            .. attribute:: rpc_name
            
            	This leaf matches if it has the value '\*' or if its value equals the requested protocol operation name
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** \\\*
            
            		**type**\: str
            
            .. attribute:: notification_name
            
            	This leaf matches if it has the value '\*' or if its value equals the requested notification name
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** \\\*
            
            		**type**\: str
            
            .. attribute:: path
            
            	Data Node Instance Identifier associated with the data node controlled by this rule.  Configuration data or state data instance identifiers start with a top\-level data node.  A complete instance identifier is required for this type of path value.  The special value '/' refers to all possible datastore contents
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: access_operations
            
            	Access operations associated with this rule.  This leaf matches if it has the value '\*' or if the bit corresponding to the requested operation is set
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** \\\*
            
            		**type**\:  :py:class:`AccessOperationsType <ydk.models.ietf.ietf_netconf_acm.AccessOperationsType>`
            
            	**default value**\: *
            
            .. attribute:: action
            
            	The access control action associated with the rule.  If a rule is determined to match a particular request, then this object is used to determine whether to permit or deny the request
            	**type**\:  :py:class:`ActionType <ydk.models.ietf.ietf_netconf_acm.ActionType>`
            
            	**mandatory**\: True
            
            .. attribute:: comment
            
            	A textual description of the access rule
            	**type**\: str
            
            

            """

            _prefix = 'nacm'
            _revision = '2012-02-22'

            def __init__(self):
                super(Nacm.RuleList.Rule, self).__init__()

                self.yang_name = "rule"
                self.yang_parent_name = "rule-list"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('module_name', YLeaf(YType.str, 'module-name')),
                    ('rpc_name', YLeaf(YType.str, 'rpc-name')),
                    ('notification_name', YLeaf(YType.str, 'notification-name')),
                    ('path', YLeaf(YType.str, 'path')),
                    ('access_operations', YLeaf(YType.str, 'access-operations')),
                    ('action', YLeaf(YType.enumeration, 'action')),
                    ('comment', YLeaf(YType.str, 'comment')),
                ])
                self.name = None
                self.module_name = None
                self.rpc_name = None
                self.notification_name = None
                self.path = None
                self.access_operations = None
                self.action = None
                self.comment = None
                self._segment_path = lambda: "rule" + "[name='" + str(self.name) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(Nacm.RuleList.Rule, ['name', 'module_name', 'rpc_name', 'notification_name', 'path', 'access_operations', 'action', 'comment'], name, value)

    def clone_ptr(self):
        self._top_entity = Nacm()
        return self._top_entity

