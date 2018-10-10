""" Cisco_IOS_XR_aaa_locald_admin_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package admin\-plane configuration.

This module contains definitions
for the following management objects\:
  aaa\: Admin plane AAA configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AaaAdminPassword(Enum):
    """
    AaaAdminPassword (Enum Class)

    Aaa admin password

    .. data:: type5 = 5

    	Type 5 password

    .. data:: type8 = 8

    	Type 8 password

    .. data:: type9 = 9

    	Type 9 password

    """

    type5 = Enum.YLeaf(5, "type5")

    type8 = Enum.YLeaf(8, "type8")

    type9 = Enum.YLeaf(9, "type9")



class Aaa(Entity):
    """
    Admin plane AAA configuration
    
    .. attribute:: usernames
    
    	Configure local username
    	**type**\:  :py:class:`Usernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames>`
    
    

    """

    _prefix = 'aaa-locald-admin-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-locald-admin-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("usernames", ("usernames", Aaa.Usernames))])
        self._leafs = OrderedDict()

        self.usernames = Aaa.Usernames()
        self.usernames.parent = self
        self._children_name_map["usernames"] = "usernames"
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-admin-cfg:aaa"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Aaa, [], name, value)


    class Usernames(Entity):
        """
        Configure local username
        
        .. attribute:: username
        
        	Admin Username
        	**type**\: list of  		 :py:class:`Username <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username>`
        
        

        """

        _prefix = 'aaa-locald-admin-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Usernames, self).__init__()

            self.yang_name = "usernames"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("username", ("username", Aaa.Usernames.Username))])
            self._leafs = OrderedDict()

            self.username = YList(self)
            self._segment_path = lambda: "usernames"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-admin-cfg:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Usernames, [], name, value)


        class Username(Entity):
            """
            Admin Username
            
            .. attribute:: name  (key)
            
            	Username
            	**type**\: str
            
            .. attribute:: usergroup_under_usernames
            
            	Specify the usergroup to which this admin user belongs
            	**type**\:  :py:class:`UsergroupUnderUsernames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames>`
            
            .. attribute:: secret
            
            	Specify the secret for the admin user
            	**type**\:  :py:class:`Secret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username.Secret>`
            
            

            """

            _prefix = 'aaa-locald-admin-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Usernames.Username, self).__init__()

                self.yang_name = "username"
                self.yang_parent_name = "usernames"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("usergroup-under-usernames", ("usergroup_under_usernames", Aaa.Usernames.Username.UsergroupUnderUsernames)), ("secret", ("secret", Aaa.Usernames.Username.Secret))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ])
                self.name = None

                self.usergroup_under_usernames = Aaa.Usernames.Username.UsergroupUnderUsernames()
                self.usergroup_under_usernames.parent = self
                self._children_name_map["usergroup_under_usernames"] = "usergroup-under-usernames"

                self.secret = Aaa.Usernames.Username.Secret()
                self.secret.parent = self
                self._children_name_map["secret"] = "secret"
                self._segment_path = lambda: "username" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-admin-cfg:aaa/usernames/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Usernames.Username, ['name'], name, value)


            class UsergroupUnderUsernames(Entity):
                """
                Specify the usergroup to which this admin user
                belongs
                
                .. attribute:: usergroup_under_username
                
                	Name of the usergroup
                	**type**\: list of  		 :py:class:`UsergroupUnderUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername>`
                
                

                """

                _prefix = 'aaa-locald-admin-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usernames.Username.UsergroupUnderUsernames, self).__init__()

                    self.yang_name = "usergroup-under-usernames"
                    self.yang_parent_name = "username"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("usergroup-under-username", ("usergroup_under_username", Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername))])
                    self._leafs = OrderedDict()

                    self.usergroup_under_username = YList(self)
                    self._segment_path = lambda: "usergroup-under-usernames"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usernames.Username.UsergroupUnderUsernames, [], name, value)


                class UsergroupUnderUsername(Entity):
                    """
                    Name of the usergroup
                    
                    .. attribute:: name  (key)
                    
                    	Name of the usergroup
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    

                    """

                    _prefix = 'aaa-locald-admin-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, self).__init__()

                        self.yang_name = "usergroup-under-username"
                        self.yang_parent_name = "usergroup-under-usernames"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "usergroup-under-username" + "[name='" + str(self.name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername, ['name'], name, value)


            class Secret(Entity):
                """
                Specify the secret for the admin user
                
                .. attribute:: type
                
                	Password type
                	**type**\:  :py:class:`AaaAdminPassword <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg.AaaAdminPassword>`
                
                .. attribute:: secret5
                
                	The user's secret password
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: secret8
                
                	Type 8 password
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                .. attribute:: secret9
                
                	Type 9 password
                	**type**\: str
                
                	**pattern:** (!.+)\|([^!].+)
                
                

                """

                _prefix = 'aaa-locald-admin-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usernames.Username.Secret, self).__init__()

                    self.yang_name = "secret"
                    self.yang_parent_name = "username"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'AaaAdminPassword', '')])),
                        ('secret5', (YLeaf(YType.str, 'secret5'), ['str'])),
                        ('secret8', (YLeaf(YType.str, 'secret8'), ['str'])),
                        ('secret9', (YLeaf(YType.str, 'secret9'), ['str'])),
                    ])
                    self.type = None
                    self.secret5 = None
                    self.secret8 = None
                    self.secret9 = None
                    self._segment_path = lambda: "secret"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usernames.Username.Secret, ['type', 'secret5', 'secret8', 'secret9'], name, value)

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity

