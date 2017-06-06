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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ActionTypeEnum(Enum):
    """
    ActionTypeEnum

    Action taken by the server when a particular

    rule matches.

    .. data:: permit = 0

    	Requested action is permitted.

    .. data:: deny = 1

    	Requested action is denied.

    """

    permit = 0

    deny = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_acm as meta
        return meta._meta_table['ActionTypeEnum']


class AccessOperationsType(FixedBitsDict):
    """
    AccessOperationsType

    NETCONF Access Operation.
    Keys are:- exec , delete , create , read , update

    """

    def __init__(self):
        self._dictionary = { 
            'exec':False,
            'delete':False,
            'create':False,
            'read':False,
            'update':False,
        }
        self._pos_map = { 
        }


class Nacm(object):
    """
    Parameters for NETCONF Access Control Model.
    
    .. attribute:: denied_data_writes
    
    	Number of times since the server last restarted that a protocol operation request to alter a configuration datastore was denied
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    .. attribute:: denied_notifications
    
    	Number of times since the server last restarted that a notification was dropped for a subscription because access to the event type was denied
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    .. attribute:: denied_operations
    
    	Number of times since the server last restarted that a protocol operation request was denied
    	**type**\:  int
    
    	**range:** 0..4294967295
    
    	**mandatory**\: True
    
    .. attribute:: enable_external_groups
    
    	Controls whether the server uses the groups reported by the NETCONF transport layer when it assigns the user to a set of NACM groups.  If this leaf has the value 'false', any group names reported by the transport layer are ignored by the server
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: enable_nacm
    
    	Enables or disables all NETCONF access control enforcement.  If 'true', then enforcement is enabled.  If 'false', then enforcement is disabled
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: exec_default
    
    	Controls whether exec access is granted if no appropriate rule is found for a particular protocol operation request
    	**type**\:   :py:class:`ActionTypeEnum <ydk.models.ietf.ietf_netconf_acm.ActionTypeEnum>`
    
    	**default value**\: permit
    
    .. attribute:: groups
    
    	NETCONF Access Control Groups
    	**type**\:   :py:class:`Groups <ydk.models.ietf.ietf_netconf_acm.Nacm.Groups>`
    
    .. attribute:: read_default
    
    	Controls whether read access is granted if no appropriate rule is found for a particular read request
    	**type**\:   :py:class:`ActionTypeEnum <ydk.models.ietf.ietf_netconf_acm.ActionTypeEnum>`
    
    	**default value**\: permit
    
    .. attribute:: rule_list
    
    	An ordered collection of access control rules
    	**type**\: list of    :py:class:`RuleList <ydk.models.ietf.ietf_netconf_acm.Nacm.RuleList>`
    
    .. attribute:: write_default
    
    	Controls whether create, update, or delete access is granted if no appropriate rule is found for a particular write request
    	**type**\:   :py:class:`ActionTypeEnum <ydk.models.ietf.ietf_netconf_acm.ActionTypeEnum>`
    
    	**default value**\: deny
    
    

    """

    _prefix = 'nacm'
    _revision = '2012-02-22'

    def __init__(self):
        self.denied_data_writes = None
        self.denied_notifications = None
        self.denied_operations = None
        self.enable_external_groups = None
        self.enable_nacm = None
        self.exec_default = None
        self.groups = Nacm.Groups()
        self.groups.parent = self
        self.read_default = None
        self.rule_list = YList()
        self.rule_list.parent = self
        self.rule_list.name = 'rule_list'
        self.write_default = None


    class Groups(object):
        """
        NETCONF Access Control Groups.
        
        .. attribute:: group
        
        	One NACM Group Entry.  This list will only contain configured entries, not any entries learned from any transport protocols
        	**type**\: list of    :py:class:`Group <ydk.models.ietf.ietf_netconf_acm.Nacm.Groups.Group>`
        
        

        """

        _prefix = 'nacm'
        _revision = '2012-02-22'

        def __init__(self):
            self.parent = None
            self.group = YList()
            self.group.parent = self
            self.group.name = 'group'


        class Group(object):
            """
            One NACM Group Entry.  This list will only contain
            configured entries, not any entries learned from
            any transport protocols.
            
            .. attribute:: name  <key>
            
            	Group name associated with this entry
            	**type**\:  str
            
            	**pattern:** [^\\\*].\*
            
            .. attribute:: user_name
            
            	Each entry identifies the username of a member of the group associated with this entry
            	**type**\:  list of str
            
            	**length:** 1..18446744073709551615
            
            

            """

            _prefix = 'nacm'
            _revision = '2012-02-22'

            def __init__(self):
                self.parent = None
                self.name = None
                self.user_name = YLeafList()
                self.user_name.parent = self
                self.user_name.name = 'user_name'

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/ietf-netconf-acm:nacm/ietf-netconf-acm:groups/ietf-netconf-acm:group[ietf-netconf-acm:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.user_name is not None:
                    for child in self.user_name:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_netconf_acm as meta
                return meta._meta_table['Nacm.Groups.Group']['meta_info']

        @property
        def _common_path(self):

            return '/ietf-netconf-acm:nacm/ietf-netconf-acm:groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.group is not None:
                for child_ref in self.group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_acm as meta
            return meta._meta_table['Nacm.Groups']['meta_info']


    class RuleList(object):
        """
        An ordered collection of access control rules.
        
        .. attribute:: name  <key>
        
        	Arbitrary name assigned to the rule\-list
        	**type**\:  str
        
        	**length:** 1..18446744073709551615
        
        .. attribute:: group
        
        	List of administrative groups that will be assigned the associated access rights defined by the 'rule' list.  The string '\*' indicates that all groups apply to the entry
        	**type**\: one of the below types:
        
        	**type**\:  list of str
        
        	**pattern:** \\\*
        
        
        ----
        	**type**\:  list of str
        
        	**pattern:** [^\\\*].\*
        
        
        ----
        .. attribute:: rule
        
        	One access control rule.  Rules are processed in user\-defined order until a match is found.  A rule matches if 'module\-name', 'rule\-type', and 'access\-operations' match the request.  If a rule matches, the 'action' leaf determines if access is granted or not
        	**type**\: list of    :py:class:`Rule <ydk.models.ietf.ietf_netconf_acm.Nacm.RuleList.Rule>`
        
        

        """

        _prefix = 'nacm'
        _revision = '2012-02-22'

        def __init__(self):
            self.parent = None
            self.name = None
            self.group = YLeafList()
            self.group.parent = self
            self.group.name = 'group'
            self.rule = YList()
            self.rule.parent = self
            self.rule.name = 'rule'


        class Rule(object):
            """
            One access control rule.
            
            Rules are processed in user\-defined order until a match is
            found.  A rule matches if 'module\-name', 'rule\-type', and
            'access\-operations' match the request.  If a rule
            matches, the 'action' leaf determines if access is granted
            or not.
            
            .. attribute:: name  <key>
            
            	Arbitrary name assigned to the rule
            	**type**\:  str
            
            	**length:** 1..18446744073709551615
            
            .. attribute:: access_operations
            
            	Access operations associated with this rule.  This leaf matches if it has the value '\*' or if the bit corresponding to the requested operation is set
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** \\\*
            
            	**default value**\: *
            
            
            ----
            	**type**\:   :py:class:`AccessOperationsType <ydk.models.ietf.ietf_netconf_acm.AccessOperationsType>`
            
            	**default value**\: *
            
            
            ----
            .. attribute:: action
            
            	The access control action associated with the rule.  If a rule is determined to match a particular request, then this object is used to determine whether to permit or deny the request
            	**type**\:   :py:class:`ActionTypeEnum <ydk.models.ietf.ietf_netconf_acm.ActionTypeEnum>`
            
            	**mandatory**\: True
            
            .. attribute:: comment
            
            	A textual description of the access rule
            	**type**\:  str
            
            .. attribute:: module_name
            
            	Name of the module associated with this rule.  This leaf matches if it has the value '\*' or if the object being accessed is defined in the module with the specified module name
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** \\\*
            
            	**default value**\: *
            
            
            ----
            	**type**\:  str
            
            	**default value**\: *
            
            
            ----
            .. attribute:: notification_name
            
            	This leaf matches if it has the value '\*' or if its value equals the requested notification name
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** \\\*
            
            
            ----
            	**type**\:  str
            
            
            ----
            .. attribute:: path
            
            	Data Node Instance Identifier associated with the data node controlled by this rule.  Configuration data or state data instance identifiers start with a top\-level data node.  A complete instance identifier is required for this type of path value.  The special value '/' refers to all possible datastore contents
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: rpc_name
            
            	This leaf matches if it has the value '\*' or if its value equals the requested protocol operation name
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** \\\*
            
            
            ----
            	**type**\:  str
            
            
            ----
            

            """

            _prefix = 'nacm'
            _revision = '2012-02-22'

            def __init__(self):
                self.parent = None
                self.name = None
                self.access_operations = None
                self.action = None
                self.comment = None
                self.module_name = None
                self.notification_name = None
                self.path = None
                self.rpc_name = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return self.parent._common_path +'/ietf-netconf-acm:rule[ietf-netconf-acm:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.access_operations is not None:
                    return True

                if self.action is not None:
                    return True

                if self.comment is not None:
                    return True

                if self.module_name is not None:
                    return True

                if self.notification_name is not None:
                    return True

                if self.path is not None:
                    return True

                if self.rpc_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ietf._meta import _ietf_netconf_acm as meta
                return meta._meta_table['Nacm.RuleList.Rule']['meta_info']

        @property
        def _common_path(self):
            if self.name is None:
                raise YPYModelError('Key property name is None')

            return '/ietf-netconf-acm:nacm/ietf-netconf-acm:rule-list[ietf-netconf-acm:name = ' + str(self.name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.name is not None:
                return True

            if self.group is not None:
                for child in self.group:
                    if child is not None:
                        return True

            if self.rule is not None:
                for child_ref in self.rule:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ietf._meta import _ietf_netconf_acm as meta
            return meta._meta_table['Nacm.RuleList']['meta_info']

    @property
    def _common_path(self):

        return '/ietf-netconf-acm:nacm'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.denied_data_writes is not None:
            return True

        if self.denied_notifications is not None:
            return True

        if self.denied_operations is not None:
            return True

        if self.enable_external_groups is not None:
            return True

        if self.enable_nacm is not None:
            return True

        if self.exec_default is not None:
            return True

        if self.groups is not None and self.groups._has_data():
            return True

        if self.read_default is not None:
            return True

        if self.rule_list is not None:
            for child_ref in self.rule_list:
                if child_ref._has_data():
                    return True

        if self.write_default is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_netconf_acm as meta
        return meta._meta_table['Nacm']['meta_info']


