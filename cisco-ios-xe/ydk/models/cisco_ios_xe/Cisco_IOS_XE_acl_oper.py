""" Cisco_IOS_XE_acl_oper 

This module contains a collection of YANG definitions for ACL statistical data.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class AccessLists(object):
    """
    This is top level container for Access Control Lists. It can have one
    or more Access Control List.
    
    .. attribute:: access_list
    
    	An access list (acl) is an ordered list of access list entries (ACE). Each access control entries has a list of match criteria, and a list of actions. Since there are several kinds of access control lists implemented with different attributes for each and different for each vendor, this model accommodates customizing access control lists for each kind and for each vendor
    	**type**\: list of    :py:class:`AccessList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList>`
    
    

    """

    _prefix = 'acl-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.access_list = YList()
        self.access_list.parent = self
        self.access_list.name = 'access_list'


    class AccessList(object):
        """
        An access list (acl) is an ordered list of
        access list entries (ACE). Each access control entries has a
        list of match criteria, and a list of actions.
        Since there are several kinds of access control lists
        implemented with different attributes for
        each and different for each vendor, this
        model accommodates customizing access control lists for
        each kind and for each vendor.
        
        .. attribute:: access_control_list_name  <key>
        
        	The name of access\-list. A device MAY restrict the length and value of this name, possibly space and special characters are not allowed
        	**type**\:  str
        
        .. attribute:: access_list_entries
        
        	A list of access\-list\-entry(ACE)
        	**type**\:   :py:class:`AccessListEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries>`
        
        

        """

        _prefix = 'acl-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.access_control_list_name = None
            self.access_list_entries = AccessLists.AccessList.AccessListEntries()
            self.access_list_entries.parent = self


        class AccessListEntries(object):
            """
            A list of access\-list\-entry(ACE)
            
            .. attribute:: access_list_entry
            
            	List of access list entries(ACE)
            	**type**\: list of    :py:class:`AccessListEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries.AccessListEntry>`
            
            

            """

            _prefix = 'acl-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.access_list_entry = YList()
                self.access_list_entry.parent = self
                self.access_list_entry.name = 'access_list_entry'


            class AccessListEntry(object):
                """
                List of access list entries(ACE)
                
                .. attribute:: rule_name  <key>
                
                	Entry number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_list_entries_oper_data
                
                	Per access list entries operational data
                	**type**\:   :py:class:`AccessListEntriesOperData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl_oper.AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData>`
                
                

                """

                _prefix = 'acl-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.rule_name = None
                    self.access_list_entries_oper_data = AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData()
                    self.access_list_entries_oper_data.parent = self


                class AccessListEntriesOperData(object):
                    """
                    Per access list entries operational data
                    
                    .. attribute:: match_counter
                    
                    	Number of matches for an access list entry
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'acl-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.match_counter = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-acl-oper:access-list-entries-oper-data'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.match_counter is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_acl_oper as meta
                        return meta._meta_table['AccessLists.AccessList.AccessListEntries.AccessListEntry.AccessListEntriesOperData']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.rule_name is None:
                        raise YPYModelError('Key property rule_name is None')

                    return self.parent._common_path +'/Cisco-IOS-XE-acl-oper:access-list-entry[Cisco-IOS-XE-acl-oper:rule-name = ' + str(self.rule_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.rule_name is not None:
                        return True

                    if self.access_list_entries_oper_data is not None and self.access_list_entries_oper_data._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_acl_oper as meta
                    return meta._meta_table['AccessLists.AccessList.AccessListEntries.AccessListEntry']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XE-acl-oper:access-list-entries'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.access_list_entry is not None:
                    for child_ref in self.access_list_entry:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_acl_oper as meta
                return meta._meta_table['AccessLists.AccessList.AccessListEntries']['meta_info']

        @property
        def _common_path(self):
            if self.access_control_list_name is None:
                raise YPYModelError('Key property access_control_list_name is None')

            return '/Cisco-IOS-XE-acl-oper:access-lists/Cisco-IOS-XE-acl-oper:access-list[Cisco-IOS-XE-acl-oper:access-control-list-name = ' + str(self.access_control_list_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.access_control_list_name is not None:
                return True

            if self.access_list_entries is not None and self.access_list_entries._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_acl_oper as meta
            return meta._meta_table['AccessLists.AccessList']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-acl-oper:access-lists'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.access_list is not None:
            for child_ref in self.access_list:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_acl_oper as meta
        return meta._meta_table['AccessLists']['meta_info']


