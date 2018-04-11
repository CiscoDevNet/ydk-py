""" Cisco_IOS_XE_acl_oper 

This module contains a collection of YANG definitions
for ACL statistical data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AccessLists(Entity):
    """
    This is top level container for Access Control Lists. It can have one
    or more Access Control List.
    
    .. attribute:: access_list
    
    	An access list (acl) is an ordered list of access list entries (ACE). Each access control entries has a list of match criteria, and a list of actions. Since there are several kinds of access control lists implemented with different attributes for each and different for each vendor, this model accommodates customizing access control lists for each kind and for each vendor
    	**type**\: list of  		 :py:class:`AccessList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList>`
    
    

    """

    _prefix = 'acl-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(AccessLists, self).__init__()
        self._top_entity = None

        self.yang_name = "access-lists"
        self.yang_parent_name = "Cisco-IOS-XE-acl-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("access-list", ("access_list", AccessLists.AccessList))])
        self._leafs = OrderedDict()

        self.access_list = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-acl-oper:access-lists"

    def __setattr__(self, name, value):
        self._perform_setattr(AccessLists, [], name, value)


    class AccessList(Entity):
        """
        An access list (acl) is an ordered list of
        access list entries (ACE). Each access control entries has a
        list of match criteria, and a list of actions.
        Since there are several kinds of access control lists
        implemented with different attributes for
        each and different for each vendor, this
        model accommodates customizing access control lists for
        each kind and for each vendor.
        
        .. attribute:: access_control_list_name  (key)
        
        	The name of access\-list. A device MAY restrict the length and value of this name, possibly space and special characters are not allowed
        	**type**\: str
        
        .. attribute:: access_list_entries
        
        	access\-list\-entry(ACE) information
        	**type**\:  :py:class:`AccessListEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries>`
        
        

        """

        _prefix = 'acl-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(AccessLists.AccessList, self).__init__()

            self.yang_name = "access-list"
            self.yang_parent_name = "access-lists"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['access_control_list_name']
            self._child_container_classes = OrderedDict([("access-list-entries", ("access_list_entries", AccessLists.AccessList.AccessListEntries))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('access_control_list_name', YLeaf(YType.str, 'access-control-list-name')),
            ])
            self.access_control_list_name = None

            self.access_list_entries = AccessLists.AccessList.AccessListEntries()
            self.access_list_entries.parent = self
            self._children_name_map["access_list_entries"] = "access-list-entries"
            self._children_yang_names.add("access-list-entries")
            self._segment_path = lambda: "access-list" + "[access-control-list-name='" + str(self.access_control_list_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-acl-oper:access-lists/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(AccessLists.AccessList, ['access_control_list_name'], name, value)


        class AccessListEntries(Entity):
            """
            access\-list\-entry(ACE) information
            
            .. attribute:: access_list_entry
            
            	A list of ACEs
            	**type**\: list of  		 :py:class:`AccessListEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries.AccessListEntry>`
            
            

            """

            _prefix = 'acl-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                super(AccessLists.AccessList.AccessListEntries, self).__init__()

                self.yang_name = "access-list-entries"
                self.yang_parent_name = "access-list"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("access-list-entry", ("access_list_entry", AccessLists.AccessList.AccessListEntries.AccessListEntry))])
                self._leafs = OrderedDict()

                self.access_list_entry = YList(self)
                self._segment_path = lambda: "access-list-entries"

            def __setattr__(self, name, value):
                self._perform_setattr(AccessLists.AccessList.AccessListEntries, [], name, value)


            class AccessListEntry(Entity):
                """
                A list of ACEs
                
                .. attribute:: rule_name  (key)
                
                	Entry number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_list_entries_oper_data
                
                	Per access list entries operational data
                	**type**\:  :py:class:`AccessListEntriesOperData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData>`
                
                

                """

                _prefix = 'acl-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    super(AccessLists.AccessList.AccessListEntries.AccessListEntry, self).__init__()

                    self.yang_name = "access-list-entry"
                    self.yang_parent_name = "access-list-entries"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['rule_name']
                    self._child_container_classes = OrderedDict([("access-list-entries-oper-data", ("access_list_entries_oper_data", AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rule_name', YLeaf(YType.uint32, 'rule-name')),
                    ])
                    self.rule_name = None

                    self.access_list_entries_oper_data = AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData()
                    self.access_list_entries_oper_data.parent = self
                    self._children_name_map["access_list_entries_oper_data"] = "access-list-entries-oper-data"
                    self._children_yang_names.add("access-list-entries-oper-data")
                    self._segment_path = lambda: "access-list-entry" + "[rule-name='" + str(self.rule_name) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(AccessLists.AccessList.AccessListEntries.AccessListEntry, ['rule_name'], name, value)


                class AccessListEntriesOperData(Entity):
                    """
                    Per access list entries operational data
                    
                    .. attribute:: match_counter
                    
                    	Number of matches for an access list entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'acl-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        super(AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData, self).__init__()

                        self.yang_name = "access-list-entries-oper-data"
                        self.yang_parent_name = "access-list-entry"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('match_counter', YLeaf(YType.uint64, 'match-counter')),
                        ])
                        self.match_counter = None
                        self._segment_path = lambda: "access-list-entries-oper-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData, ['match_counter'], name, value)

    def clone_ptr(self):
        self._top_entity = AccessLists()
        return self._top_entity

