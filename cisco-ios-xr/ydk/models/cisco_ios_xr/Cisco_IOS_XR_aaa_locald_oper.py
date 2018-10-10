""" Cisco_IOS_XR_aaa_locald_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package operational data.

This module contains definitions
for the following management objects\:
  aaa\: AAA operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Aaa(Entity):
    """
    AAA operational data
    
    .. attribute:: all_tasks
    
    	All tasks supported by system
    	**type**\:  :py:class:`AllTasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AllTasks>`
    
    .. attribute:: currentuser_detail
    
    	Current user specific details
    	**type**\:  :py:class:`CurrentuserDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentuserDetail>`
    
    .. attribute:: task_map
    
    	Task map of current user
    	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.TaskMap>`
    
    .. attribute:: taskgroups
    
    	Individual taskgroups container
    	**type**\:  :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups>`
    
    .. attribute:: users
    
    	Container for individual local user information
    	**type**\:  :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users>`
    
    .. attribute:: password_policies
    
    	Container for individual password policy Information
    	**type**\:  :py:class:`PasswordPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.PasswordPolicies>`
    
    .. attribute:: usergroups
    
    	Container for individual usergroup Information
    	**type**\:  :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups>`
    
    .. attribute:: authen_method
    
    	Current users authentication method
    	**type**\:  :py:class:`AuthenMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AuthenMethod>`
    
    .. attribute:: current_usergroup
    
    	Specific Usergroup Information
    	**type**\:  :py:class:`CurrentUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentUsergroup>`
    
    .. attribute:: radius
    
    	RADIUS operational data
    	**type**\:  :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius>`
    
    .. attribute:: tacacs
    
    	TACACS operational data
    	**type**\:  :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs>`
    
    .. attribute:: diameter
    
    	Diameter operational data
    	**type**\:  :py:class:`Diameter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter>`
    
    

    """

    _prefix = 'aaa-locald-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Aaa, self).__init__()
        self._top_entity = None

        self.yang_name = "aaa"
        self.yang_parent_name = "Cisco-IOS-XR-aaa-locald-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("all-tasks", ("all_tasks", Aaa.AllTasks)), ("currentuser-detail", ("currentuser_detail", Aaa.CurrentuserDetail)), ("task-map", ("task_map", Aaa.TaskMap)), ("taskgroups", ("taskgroups", Aaa.Taskgroups)), ("users", ("users", Aaa.Users)), ("password-policies", ("password_policies", Aaa.PasswordPolicies)), ("usergroups", ("usergroups", Aaa.Usergroups)), ("authen-method", ("authen_method", Aaa.AuthenMethod)), ("current-usergroup", ("current_usergroup", Aaa.CurrentUsergroup)), ("Cisco-IOS-XR-aaa-protocol-radius-oper:radius", ("radius", Aaa.Radius)), ("Cisco-IOS-XR-aaa-tacacs-oper:tacacs", ("tacacs", Aaa.Tacacs)), ("Cisco-IOS-XR-aaa-diameter-oper:diameter", ("diameter", Aaa.Diameter))])
        self._leafs = OrderedDict()

        self.all_tasks = Aaa.AllTasks()
        self.all_tasks.parent = self
        self._children_name_map["all_tasks"] = "all-tasks"

        self.currentuser_detail = Aaa.CurrentuserDetail()
        self.currentuser_detail.parent = self
        self._children_name_map["currentuser_detail"] = "currentuser-detail"

        self.task_map = Aaa.TaskMap()
        self.task_map.parent = self
        self._children_name_map["task_map"] = "task-map"

        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self._children_name_map["taskgroups"] = "taskgroups"

        self.users = Aaa.Users()
        self.users.parent = self
        self._children_name_map["users"] = "users"

        self.password_policies = Aaa.PasswordPolicies()
        self.password_policies.parent = self
        self._children_name_map["password_policies"] = "password-policies"

        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self._children_name_map["usergroups"] = "usergroups"

        self.authen_method = Aaa.AuthenMethod()
        self.authen_method.parent = self
        self._children_name_map["authen_method"] = "authen-method"

        self.current_usergroup = Aaa.CurrentUsergroup()
        self.current_usergroup.parent = self
        self._children_name_map["current_usergroup"] = "current-usergroup"

        self.radius = Aaa.Radius()
        self.radius.parent = self
        self._children_name_map["radius"] = "Cisco-IOS-XR-aaa-protocol-radius-oper:radius"

        self.tacacs = Aaa.Tacacs()
        self.tacacs.parent = self
        self._children_name_map["tacacs"] = "Cisco-IOS-XR-aaa-tacacs-oper:tacacs"

        self.diameter = Aaa.Diameter()
        self.diameter.parent = self
        self._children_name_map["diameter"] = "Cisco-IOS-XR-aaa-diameter-oper:diameter"
        self._segment_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Aaa, [], name, value)


    class AllTasks(Entity):
        """
        All tasks supported by system
        
        .. attribute:: task_id
        
        	Names of available task\-ids
        	**type**\: list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AllTasks, self).__init__()

            self.yang_name = "all-tasks"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('task_id', (YLeafList(YType.str, 'task-id'), ['str'])),
            ])
            self.task_id = []
            self._segment_path = lambda: "all-tasks"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AllTasks, [u'task_id'], name, value)


    class CurrentuserDetail(Entity):
        """
        Current user specific details
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\: str
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\: list of str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\: list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.CurrentuserDetail, self).__init__()

            self.yang_name = "currentuser-detail"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('authenmethod', (YLeaf(YType.int32, 'authenmethod'), ['int'])),
                ('usergroup', (YLeafList(YType.str, 'usergroup'), ['str'])),
                ('taskmap', (YLeafList(YType.str, 'taskmap'), ['str'])),
            ])
            self.name = None
            self.authenmethod = None
            self.usergroup = []
            self.taskmap = []
            self._segment_path = lambda: "currentuser-detail"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.CurrentuserDetail, [u'name', u'authenmethod', u'usergroup', u'taskmap'], name, value)


    class TaskMap(Entity):
        """
        Task map of current user
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\: str
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\: list of str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\: list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.TaskMap, self).__init__()

            self.yang_name = "task-map"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('authenmethod', (YLeaf(YType.int32, 'authenmethod'), ['int'])),
                ('usergroup', (YLeafList(YType.str, 'usergroup'), ['str'])),
                ('taskmap', (YLeafList(YType.str, 'taskmap'), ['str'])),
            ])
            self.name = None
            self.authenmethod = None
            self.usergroup = []
            self.taskmap = []
            self._segment_path = lambda: "task-map"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.TaskMap, [u'name', u'authenmethod', u'usergroup', u'taskmap'], name, value)


    class Taskgroups(Entity):
        """
        Individual taskgroups container
        
        .. attribute:: taskgroup
        
        	Specific Taskgroup Information
        	**type**\: list of  		 :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Taskgroups, self).__init__()

            self.yang_name = "taskgroups"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("taskgroup", ("taskgroup", Aaa.Taskgroups.Taskgroup))])
            self._leafs = OrderedDict()

            self.taskgroup = YList(self)
            self._segment_path = lambda: "taskgroups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Taskgroups, [], name, value)


        class Taskgroup(Entity):
            """
            Specific Taskgroup Information
            
            .. attribute:: name  (key)
            
            	Taskgroup name
            	**type**\: str
            
            .. attribute:: included_task_ids
            
            	Task\-ids included
            	**type**\:  :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds>`
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap>`
            
            .. attribute:: name_xr
            
            	Name of the taskgroup
            	**type**\: str
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Taskgroups.Taskgroup, self).__init__()

                self.yang_name = "taskgroup"
                self.yang_parent_name = "taskgroups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("included-task-ids", ("included_task_ids", Aaa.Taskgroups.Taskgroup.IncludedTaskIds)), ("task-map", ("task_map", Aaa.Taskgroups.Taskgroup.TaskMap))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('name_xr', (YLeaf(YType.str, 'name-xr'), ['str'])),
                ])
                self.name = None
                self.name_xr = None

                self.included_task_ids = Aaa.Taskgroups.Taskgroup.IncludedTaskIds()
                self.included_task_ids.parent = self
                self._children_name_map["included_task_ids"] = "included-task-ids"

                self.task_map = Aaa.Taskgroups.Taskgroup.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._segment_path = lambda: "taskgroup" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/taskgroups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Taskgroups.Taskgroup, [u'name', u'name_xr'], name, value)


            class IncludedTaskIds(Entity):
                """
                Task\-ids included
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  		 :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds, self).__init__()

                    self.yang_name = "included-task-ids"
                    self.yang_parent_name = "taskgroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tasks", ("tasks", Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks))])
                    self._leafs = OrderedDict()

                    self.tasks = YList(self)
                    self._segment_path = lambda: "included-task-ids"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Taskgroups.Taskgroup.IncludedTaskIds, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\: str
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\: bool
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\: bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\: bool
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "included-task-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('task_id', (YLeaf(YType.str, 'task-id'), ['str'])),
                            ('read', (YLeaf(YType.boolean, 'read'), ['bool'])),
                            ('write', (YLeaf(YType.boolean, 'write'), ['bool'])),
                            ('execute', (YLeaf(YType.boolean, 'execute'), ['bool'])),
                            ('debug', (YLeaf(YType.boolean, 'debug'), ['bool'])),
                        ])
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None
                        self._segment_path = lambda: "tasks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks, [u'task_id', u'read', u'write', u'execute', u'debug'], name, value)


            class TaskMap(Entity):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  		 :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Taskgroups.Taskgroup.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "taskgroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tasks", ("tasks", Aaa.Taskgroups.Taskgroup.TaskMap.Tasks))])
                    self._leafs = OrderedDict()

                    self.tasks = YList(self)
                    self._segment_path = lambda: "task-map"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Taskgroups.Taskgroup.TaskMap, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\: str
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\: bool
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\: bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\: bool
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Taskgroups.Taskgroup.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('task_id', (YLeaf(YType.str, 'task-id'), ['str'])),
                            ('read', (YLeaf(YType.boolean, 'read'), ['bool'])),
                            ('write', (YLeaf(YType.boolean, 'write'), ['bool'])),
                            ('execute', (YLeaf(YType.boolean, 'execute'), ['bool'])),
                            ('debug', (YLeaf(YType.boolean, 'debug'), ['bool'])),
                        ])
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None
                        self._segment_path = lambda: "tasks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Taskgroups.Taskgroup.TaskMap.Tasks, [u'task_id', u'read', u'write', u'execute', u'debug'], name, value)


    class Users(Entity):
        """
        Container for individual local user information
        
        .. attribute:: user
        
        	Specific local user information
        	**type**\: list of  		 :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Users, self).__init__()

            self.yang_name = "users"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("user", ("user", Aaa.Users.User))])
            self._leafs = OrderedDict()

            self.user = YList(self)
            self._segment_path = lambda: "users"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Users, [], name, value)


        class User(Entity):
            """
            Specific local user information
            
            .. attribute:: name  (key)
            
            	Username
            	**type**\: str
            
            .. attribute:: task_map
            
            	Computed taskmap
            	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap>`
            
            .. attribute:: name_xr
            
            	Username
            	**type**\: str
            
            .. attribute:: admin_user
            
            	Is admin plane user ?
            	**type**\: bool
            
            .. attribute:: first_user
            
            	Is first user ?
            	**type**\: bool
            
            .. attribute:: usergroup
            
            	Member usergroups
            	**type**\: list of str
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Users.User, self).__init__()

                self.yang_name = "user"
                self.yang_parent_name = "users"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("task-map", ("task_map", Aaa.Users.User.TaskMap))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('name_xr', (YLeaf(YType.str, 'name-xr'), ['str'])),
                    ('admin_user', (YLeaf(YType.boolean, 'admin-user'), ['bool'])),
                    ('first_user', (YLeaf(YType.boolean, 'first-user'), ['bool'])),
                    ('usergroup', (YLeafList(YType.str, 'usergroup'), ['str'])),
                ])
                self.name = None
                self.name_xr = None
                self.admin_user = None
                self.first_user = None
                self.usergroup = []

                self.task_map = Aaa.Users.User.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"
                self._segment_path = lambda: "user" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/users/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Users.User, [u'name', u'name_xr', u'admin_user', u'first_user', u'usergroup'], name, value)


            class TaskMap(Entity):
                """
                Computed taskmap
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  		 :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Users.User.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "user"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tasks", ("tasks", Aaa.Users.User.TaskMap.Tasks))])
                    self._leafs = OrderedDict()

                    self.tasks = YList(self)
                    self._segment_path = lambda: "task-map"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Users.User.TaskMap, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\: str
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\: bool
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\: bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\: bool
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Users.User.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('task_id', (YLeaf(YType.str, 'task-id'), ['str'])),
                            ('read', (YLeaf(YType.boolean, 'read'), ['bool'])),
                            ('write', (YLeaf(YType.boolean, 'write'), ['bool'])),
                            ('execute', (YLeaf(YType.boolean, 'execute'), ['bool'])),
                            ('debug', (YLeaf(YType.boolean, 'debug'), ['bool'])),
                        ])
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None
                        self._segment_path = lambda: "tasks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Users.User.TaskMap.Tasks, [u'task_id', u'read', u'write', u'execute', u'debug'], name, value)


    class PasswordPolicies(Entity):
        """
        Container for individual password policy
        Information
        
        .. attribute:: password_policy
        
        	Password policy details
        	**type**\: list of  		 :py:class:`PasswordPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.PasswordPolicies.PasswordPolicy>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.PasswordPolicies, self).__init__()

            self.yang_name = "password-policies"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("password-policy", ("password_policy", Aaa.PasswordPolicies.PasswordPolicy))])
            self._leafs = OrderedDict()

            self.password_policy = YList(self)
            self._segment_path = lambda: "password-policies"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.PasswordPolicies, [], name, value)


        class PasswordPolicy(Entity):
            """
            Password policy details
            
            .. attribute:: name  (key)
            
            	Password policy name
            	**type**\: str
            
            .. attribute:: life_time
            
            	Lifetime of the policy
            	**type**\:  :py:class:`LifeTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.PasswordPolicies.PasswordPolicy.LifeTime>`
            
            .. attribute:: lock_out_time
            
            	Lockout time of the policy
            	**type**\:  :py:class:`LockOutTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.PasswordPolicies.PasswordPolicy.LockOutTime>`
            
            .. attribute:: name_xr
            
            	Password Policy Name
            	**type**\: str
            
            .. attribute:: min_len
            
            	Min Length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: max_len
            
            	Max Length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: spl_char
            
            	Special Character length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: upper_case
            
            	UpperCase Character length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: lower_case
            
            	LowerCase Character length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: numeric
            
            	Numeric Character length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: min_char_change
            
            	Number of different characters
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: num_of_users
            
            	Number of users with this policy
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: max_fail_attempts
            
            	Maximum Failure Attempts allowed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: usr_count
            
            	Count of users
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: err_count
            
            	Error Count
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: lock_out_count
            
            	Lock Out Count
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.PasswordPolicies.PasswordPolicy, self).__init__()

                self.yang_name = "password-policy"
                self.yang_parent_name = "password-policies"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("life-time", ("life_time", Aaa.PasswordPolicies.PasswordPolicy.LifeTime)), ("lock-out-time", ("lock_out_time", Aaa.PasswordPolicies.PasswordPolicy.LockOutTime))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('name_xr', (YLeaf(YType.str, 'name-xr'), ['str'])),
                    ('min_len', (YLeaf(YType.uint8, 'min-len'), ['int'])),
                    ('max_len', (YLeaf(YType.uint8, 'max-len'), ['int'])),
                    ('spl_char', (YLeaf(YType.uint8, 'spl-char'), ['int'])),
                    ('upper_case', (YLeaf(YType.uint8, 'upper-case'), ['int'])),
                    ('lower_case', (YLeaf(YType.uint8, 'lower-case'), ['int'])),
                    ('numeric', (YLeaf(YType.uint8, 'numeric'), ['int'])),
                    ('min_char_change', (YLeaf(YType.uint8, 'min-char-change'), ['int'])),
                    ('num_of_users', (YLeaf(YType.uint8, 'num-of-users'), ['int'])),
                    ('max_fail_attempts', (YLeaf(YType.uint32, 'max-fail-attempts'), ['int'])),
                    ('usr_count', (YLeaf(YType.uint8, 'usr-count'), ['int'])),
                    ('err_count', (YLeaf(YType.uint8, 'err-count'), ['int'])),
                    ('lock_out_count', (YLeaf(YType.uint8, 'lock-out-count'), ['int'])),
                ])
                self.name = None
                self.name_xr = None
                self.min_len = None
                self.max_len = None
                self.spl_char = None
                self.upper_case = None
                self.lower_case = None
                self.numeric = None
                self.min_char_change = None
                self.num_of_users = None
                self.max_fail_attempts = None
                self.usr_count = None
                self.err_count = None
                self.lock_out_count = None

                self.life_time = Aaa.PasswordPolicies.PasswordPolicy.LifeTime()
                self.life_time.parent = self
                self._children_name_map["life_time"] = "life-time"

                self.lock_out_time = Aaa.PasswordPolicies.PasswordPolicy.LockOutTime()
                self.lock_out_time.parent = self
                self._children_name_map["lock_out_time"] = "lock-out-time"
                self._segment_path = lambda: "password-policy" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/password-policies/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.PasswordPolicies.PasswordPolicy, [u'name', u'name_xr', u'min_len', u'max_len', u'spl_char', u'upper_case', u'lower_case', u'numeric', u'min_char_change', u'num_of_users', u'max_fail_attempts', u'usr_count', u'err_count', u'lock_out_count'], name, value)


            class LifeTime(Entity):
                """
                Lifetime of the policy
                
                .. attribute:: years
                
                	years
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: months
                
                	months
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: days
                
                	days
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: hours
                
                	hours
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: mins
                
                	mins
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: secs
                
                	secs
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.PasswordPolicies.PasswordPolicy.LifeTime, self).__init__()

                    self.yang_name = "life-time"
                    self.yang_parent_name = "password-policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('years', (YLeaf(YType.uint8, 'years'), ['int'])),
                        ('months', (YLeaf(YType.uint8, 'months'), ['int'])),
                        ('days', (YLeaf(YType.uint8, 'days'), ['int'])),
                        ('hours', (YLeaf(YType.uint8, 'hours'), ['int'])),
                        ('mins', (YLeaf(YType.uint8, 'mins'), ['int'])),
                        ('secs', (YLeaf(YType.uint8, 'secs'), ['int'])),
                    ])
                    self.years = None
                    self.months = None
                    self.days = None
                    self.hours = None
                    self.mins = None
                    self.secs = None
                    self._segment_path = lambda: "life-time"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.PasswordPolicies.PasswordPolicy.LifeTime, [u'years', u'months', u'days', u'hours', u'mins', u'secs'], name, value)


            class LockOutTime(Entity):
                """
                Lockout time of the policy
                
                .. attribute:: years
                
                	years
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: months
                
                	months
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: days
                
                	days
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: hours
                
                	hours
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: mins
                
                	mins
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: secs
                
                	secs
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.PasswordPolicies.PasswordPolicy.LockOutTime, self).__init__()

                    self.yang_name = "lock-out-time"
                    self.yang_parent_name = "password-policy"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('years', (YLeaf(YType.uint8, 'years'), ['int'])),
                        ('months', (YLeaf(YType.uint8, 'months'), ['int'])),
                        ('days', (YLeaf(YType.uint8, 'days'), ['int'])),
                        ('hours', (YLeaf(YType.uint8, 'hours'), ['int'])),
                        ('mins', (YLeaf(YType.uint8, 'mins'), ['int'])),
                        ('secs', (YLeaf(YType.uint8, 'secs'), ['int'])),
                    ])
                    self.years = None
                    self.months = None
                    self.days = None
                    self.hours = None
                    self.mins = None
                    self.secs = None
                    self._segment_path = lambda: "lock-out-time"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.PasswordPolicies.PasswordPolicy.LockOutTime, [u'years', u'months', u'days', u'hours', u'mins', u'secs'], name, value)


    class Usergroups(Entity):
        """
        Container for individual usergroup Information
        
        .. attribute:: usergroup
        
        	Specific Usergroup Information
        	**type**\: list of  		 :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Usergroups, self).__init__()

            self.yang_name = "usergroups"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("usergroup", ("usergroup", Aaa.Usergroups.Usergroup))])
            self._leafs = OrderedDict()

            self.usergroup = YList(self)
            self._segment_path = lambda: "usergroups"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Usergroups, [], name, value)


        class Usergroup(Entity):
            """
            Specific Usergroup Information
            
            .. attribute:: name  (key)
            
            	Usergroup name
            	**type**\: str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap>`
            
            .. attribute:: name_xr
            
            	Name of the usergroup
            	**type**\: str
            
            .. attribute:: taskgroup
            
            	Component taskgroups
            	**type**\: list of  		 :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Usergroups.Usergroup, self).__init__()

                self.yang_name = "usergroup"
                self.yang_parent_name = "usergroups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_classes = OrderedDict([("task-map", ("task_map", Aaa.Usergroups.Usergroup.TaskMap)), ("taskgroup", ("taskgroup", Aaa.Usergroups.Usergroup.Taskgroup))])
                self._leafs = OrderedDict([
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('name_xr', (YLeaf(YType.str, 'name-xr'), ['str'])),
                ])
                self.name = None
                self.name_xr = None

                self.task_map = Aaa.Usergroups.Usergroup.TaskMap()
                self.task_map.parent = self
                self._children_name_map["task_map"] = "task-map"

                self.taskgroup = YList(self)
                self._segment_path = lambda: "usergroup" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/usergroups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Usergroups.Usergroup, [u'name', u'name_xr'], name, value)


            class TaskMap(Entity):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  		 :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.TaskMap, self).__init__()

                    self.yang_name = "task-map"
                    self.yang_parent_name = "usergroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tasks", ("tasks", Aaa.Usergroups.Usergroup.TaskMap.Tasks))])
                    self._leafs = OrderedDict()

                    self.tasks = YList(self)
                    self._segment_path = lambda: "task-map"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usergroups.Usergroup.TaskMap, [], name, value)


                class Tasks(Entity):
                    """
                    List of permitted tasks
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\: str
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\: bool
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\: bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\: bool
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.TaskMap.Tasks, self).__init__()

                        self.yang_name = "tasks"
                        self.yang_parent_name = "task-map"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('task_id', (YLeaf(YType.str, 'task-id'), ['str'])),
                            ('read', (YLeaf(YType.boolean, 'read'), ['bool'])),
                            ('write', (YLeaf(YType.boolean, 'write'), ['bool'])),
                            ('execute', (YLeaf(YType.boolean, 'execute'), ['bool'])),
                            ('debug', (YLeaf(YType.boolean, 'debug'), ['bool'])),
                        ])
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None
                        self._segment_path = lambda: "tasks"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.TaskMap.Tasks, [u'task_id', u'read', u'write', u'execute', u'debug'], name, value)


            class Taskgroup(Entity):
                """
                Component taskgroups
                
                .. attribute:: included_task_ids
                
                	Task\-ids included
                	**type**\:  :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds>`
                
                .. attribute:: task_map
                
                	Computed task map
                	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap>`
                
                .. attribute:: name_xr
                
                	Name of the taskgroup
                	**type**\: str
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Usergroups.Usergroup.Taskgroup, self).__init__()

                    self.yang_name = "taskgroup"
                    self.yang_parent_name = "usergroup"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("included-task-ids", ("included_task_ids", Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds)), ("task-map", ("task_map", Aaa.Usergroups.Usergroup.Taskgroup.TaskMap))])
                    self._leafs = OrderedDict([
                        ('name_xr', (YLeaf(YType.str, 'name-xr'), ['str'])),
                    ])
                    self.name_xr = None

                    self.included_task_ids = Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds()
                    self.included_task_ids.parent = self
                    self._children_name_map["included_task_ids"] = "included-task-ids"

                    self.task_map = Aaa.Usergroups.Usergroup.Taskgroup.TaskMap()
                    self.task_map.parent = self
                    self._children_name_map["task_map"] = "task-map"
                    self._segment_path = lambda: "taskgroup"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup, [u'name_xr'], name, value)


                class IncludedTaskIds(Entity):
                    """
                    Task\-ids included
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of  		 :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds, self).__init__()

                        self.yang_name = "included-task-ids"
                        self.yang_parent_name = "taskgroup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tasks", ("tasks", Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks))])
                        self._leafs = OrderedDict()

                        self.tasks = YList(self)
                        self._segment_path = lambda: "included-task-ids"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds, [], name, value)


                    class Tasks(Entity):
                        """
                        List of permitted tasks
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\: str
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\: bool
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\: bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\: bool
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks, self).__init__()

                            self.yang_name = "tasks"
                            self.yang_parent_name = "included-task-ids"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('task_id', (YLeaf(YType.str, 'task-id'), ['str'])),
                                ('read', (YLeaf(YType.boolean, 'read'), ['bool'])),
                                ('write', (YLeaf(YType.boolean, 'write'), ['bool'])),
                                ('execute', (YLeaf(YType.boolean, 'execute'), ['bool'])),
                                ('debug', (YLeaf(YType.boolean, 'debug'), ['bool'])),
                            ])
                            self.task_id = None
                            self.read = None
                            self.write = None
                            self.execute = None
                            self.debug = None
                            self._segment_path = lambda: "tasks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks, [u'task_id', u'read', u'write', u'execute', u'debug'], name, value)


                class TaskMap(Entity):
                    """
                    Computed task map
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of  		 :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap, self).__init__()

                        self.yang_name = "task-map"
                        self.yang_parent_name = "taskgroup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tasks", ("tasks", Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks))])
                        self._leafs = OrderedDict()

                        self.tasks = YList(self)
                        self._segment_path = lambda: "task-map"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap, [], name, value)


                    class Tasks(Entity):
                        """
                        List of permitted tasks
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\: str
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\: bool
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\: bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\: bool
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks, self).__init__()

                            self.yang_name = "tasks"
                            self.yang_parent_name = "task-map"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('task_id', (YLeaf(YType.str, 'task-id'), ['str'])),
                                ('read', (YLeaf(YType.boolean, 'read'), ['bool'])),
                                ('write', (YLeaf(YType.boolean, 'write'), ['bool'])),
                                ('execute', (YLeaf(YType.boolean, 'execute'), ['bool'])),
                                ('debug', (YLeaf(YType.boolean, 'debug'), ['bool'])),
                            ])
                            self.task_id = None
                            self.read = None
                            self.write = None
                            self.execute = None
                            self.debug = None
                            self._segment_path = lambda: "tasks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks, [u'task_id', u'read', u'write', u'execute', u'debug'], name, value)


    class AuthenMethod(Entity):
        """
        Current users authentication method
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\: str
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\: list of str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\: list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.AuthenMethod, self).__init__()

            self.yang_name = "authen-method"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('authenmethod', (YLeaf(YType.int32, 'authenmethod'), ['int'])),
                ('usergroup', (YLeafList(YType.str, 'usergroup'), ['str'])),
                ('taskmap', (YLeafList(YType.str, 'taskmap'), ['str'])),
            ])
            self.name = None
            self.authenmethod = None
            self.usergroup = []
            self.taskmap = []
            self._segment_path = lambda: "authen-method"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.AuthenMethod, [u'name', u'authenmethod', u'usergroup', u'taskmap'], name, value)


    class CurrentUsergroup(Entity):
        """
        Specific Usergroup Information
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\: str
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\: list of str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\: list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.CurrentUsergroup, self).__init__()

            self.yang_name = "current-usergroup"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                ('authenmethod', (YLeaf(YType.int32, 'authenmethod'), ['int'])),
                ('usergroup', (YLeafList(YType.str, 'usergroup'), ['str'])),
                ('taskmap', (YLeafList(YType.str, 'taskmap'), ['str'])),
            ])
            self.name = None
            self.authenmethod = None
            self.usergroup = []
            self.taskmap = []
            self._segment_path = lambda: "current-usergroup"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.CurrentUsergroup, [u'name', u'authenmethod', u'usergroup', u'taskmap'], name, value)


    class Radius(Entity):
        """
        RADIUS operational data
        
        .. attribute:: servers
        
        	List of RADIUS servers configured
        	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers>`
        
        .. attribute:: radius_source_interface
        
        	RADIUS source interfaces
        	**type**\:  :py:class:`RadiusSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface>`
        
        .. attribute:: global_
        
        	RADIUS Client Information
        	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Global>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2017-11-13'

        def __init__(self):
            super(Aaa.Radius, self).__init__()

            self.yang_name = "radius"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("servers", ("servers", Aaa.Radius.Servers)), ("radius-source-interface", ("radius_source_interface", Aaa.Radius.RadiusSourceInterface)), ("global", ("global_", Aaa.Radius.Global))])
            self._leafs = OrderedDict()

            self.servers = Aaa.Radius.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"

            self.radius_source_interface = Aaa.Radius.RadiusSourceInterface()
            self.radius_source_interface.parent = self
            self._children_name_map["radius_source_interface"] = "radius-source-interface"

            self.global_ = Aaa.Radius.Global()
            self.global_.parent = self
            self._children_name_map["global_"] = "global"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-protocol-radius-oper:radius"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Radius, [], name, value)


        class Servers(Entity):
            """
            List of RADIUS servers configured
            
            .. attribute:: server
            
            	RADIUS Server
            	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers.Server>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Radius.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("server", ("server", Aaa.Radius.Servers.Server))])
                self._leafs = OrderedDict()

                self.server = YList(self)
                self._segment_path = lambda: "servers"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Servers, [], name, value)


            class Server(Entity):
                """
                RADIUS Server
                
                .. attribute:: ip_address
                
                	IP address of RADIUS server
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: auth_port_number
                
                	Authentication Port number (standard port 1645)
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: acct_port_number
                
                	Accounting Port number (standard port 1646)
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: ipv4_address
                
                	IP address of RADIUS server
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: priority
                
                	A number that indicates the priority             of the server
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout_xr
                
                	Per\-server timeout in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: retransmit
                
                	Per\-server retransmit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_time
                
                	Per\-server deadtime in minutes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: dead_detect_time
                
                	Per\-server dead\-detect time in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: dead_detect_tries
                
                	Per\-server dead\-detect tries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_port
                
                	Authentication port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_port
                
                	Accounting port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	State of the server UP/DOWN
                	**type**\: str
                
                .. attribute:: current_state_duration
                
                	Elapsed time the server has been in              current state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: previous_state_duration
                
                	Elapsed time the server was been in              previous state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_in
                
                	Total number of incoming packets read
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_out
                
                	Total number of outgoing packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeouts
                
                	Total number of packets timed\-out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: aborts
                
                	Total number of requests aborted
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	Number of replies expected to arrive
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: redirected_requests
                
                	Number of requests redirected
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_rtt
                
                	Round\-trip time for authentication               in milliseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: access_requests
                
                	Number of access requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_request_retransmits
                
                	Number of retransmitted                          access requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_accepts
                
                	Number of access accepts
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_rejects
                
                	Number of access rejects
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_challenges
                
                	Number of access challenges
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_responses
                
                	Number of bad access responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_authenticators
                
                	Number of bad access authenticators
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_access_requests
                
                	Number of pending access requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_timeouts
                
                	Number of access packets timed\-out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_access_types
                
                	Number of packets received with unknown          type from authentication server
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_access_responses
                
                	Number of access responses dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_access_reqs
                
                	No of throttled access reqs stats
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_timed_out_reqs
                
                	No of access reqs that is throttled is timedout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_dropped_reqs
                
                	No of discarded access reqs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_throttled_access_reqs
                
                	Max throttled access reqs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: currently_throttled_access_reqs
                
                	No of currently throttled access reqs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_response_time
                
                	Average response time for authentication requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_unexpected_responses
                
                	Number of unexpected authentication responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_server_error_responses
                
                	Number of server error authentication responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_incorrect_responses
                
                	Number of incorrect authentication responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_requests
                
                	Number of access requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_request_timeouts
                
                	Number of access packets timed out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_response_time
                
                	Average response time for authorization requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_successess
                
                	Number of succeeded authorization transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_failure
                
                	Number of failed authorization transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_unexpected_responses
                
                	Number of unexpected authorization responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_server_error_responses
                
                	Number of server error authorization responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_incorrect_responses
                
                	Number of incorrect authorization responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_rtt
                
                	Round\-trip time for accounting                   in milliseconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: accounting_requests
                
                	Number of accounting requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_retransmits
                
                	Number of retransmitted                          accounting requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_responses
                
                	Number of accounting responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_responses
                
                	Number of bad accounting responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_authenticators
                
                	Number of bad accounting                         authenticators
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_accounting_requets
                
                	Number of pending accounting requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_timeouts
                
                	Number of accounting packets                     timed\-out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_accounting_types
                
                	Number of packets received with unknown          type from accounting server
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_accounting_responses
                
                	Number of accounting responses                   dropped
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_a_private_server
                
                	Is a private server
                	**type**\: bool
                
                .. attribute:: total_test_auth_reqs
                
                	Total auth test request
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_timeouts
                
                	Total auth test timeouts
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_response
                
                	Total auth test response
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_pending
                
                	Total auth test pending
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_reqs
                
                	 Total acct test req
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_timeouts
                
                	Total acct test timeouts
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_response
                
                	Total acct test response
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_pending
                
                	Total acct test pending
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_transactions
                
                	No of throttled acct transactions stats
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_timed_out_stats
                
                	No of acct transaction that is throttled is timedout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_failures_stats
                
                	No of acct discarded transaction
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_acct_throttled
                
                	Max throttled acct transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttleda_acct_transactions
                
                	No of currently throttled acct transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_unexpected_responses
                
                	Number of unexpected accounting responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_server_error_responses
                
                	Number of server error accounting responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_incorrect_responses
                
                	Number of incorrect accounting responses
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_response_time
                
                	Average response time for authentication requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_deadtime
                
                	Total time of Server being in DEAD               state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_deadtime
                
                	Time of Server being in DEAD state,              after last UP
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: is_quarantined
                
                	flag to indicate Server is quarantined           or not (Automated TEST in progress)
                	**type**\: bool
                
                .. attribute:: group_name
                
                	Server group name for private server
                	**type**\: str
                
                .. attribute:: ip_address_xr
                
                	IP address buffer
                	**type**\: str
                
                .. attribute:: family
                
                	IP address Family
                	**type**\: str
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Aaa.Radius.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str','str'])),
                        ('auth_port_number', (YLeaf(YType.uint32, 'auth-port-number'), ['int'])),
                        ('acct_port_number', (YLeaf(YType.uint32, 'acct-port-number'), ['int'])),
                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                        ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                        ('timeout_xr', (YLeaf(YType.uint32, 'timeout-xr'), ['int'])),
                        ('retransmit', (YLeaf(YType.uint32, 'retransmit'), ['int'])),
                        ('dead_time', (YLeaf(YType.uint32, 'dead-time'), ['int'])),
                        ('dead_detect_time', (YLeaf(YType.uint32, 'dead-detect-time'), ['int'])),
                        ('dead_detect_tries', (YLeaf(YType.uint32, 'dead-detect-tries'), ['int'])),
                        ('authentication_port', (YLeaf(YType.uint32, 'authentication-port'), ['int'])),
                        ('accounting_port', (YLeaf(YType.uint32, 'accounting-port'), ['int'])),
                        ('state', (YLeaf(YType.str, 'state'), ['str'])),
                        ('current_state_duration', (YLeaf(YType.uint32, 'current-state-duration'), ['int'])),
                        ('previous_state_duration', (YLeaf(YType.uint32, 'previous-state-duration'), ['int'])),
                        ('packets_in', (YLeaf(YType.uint32, 'packets-in'), ['int'])),
                        ('packets_out', (YLeaf(YType.uint32, 'packets-out'), ['int'])),
                        ('timeouts', (YLeaf(YType.uint32, 'timeouts'), ['int'])),
                        ('aborts', (YLeaf(YType.uint32, 'aborts'), ['int'])),
                        ('replies_expected', (YLeaf(YType.uint32, 'replies-expected'), ['int'])),
                        ('redirected_requests', (YLeaf(YType.uint32, 'redirected-requests'), ['int'])),
                        ('authentication_rtt', (YLeaf(YType.uint32, 'authentication-rtt'), ['int'])),
                        ('access_requests', (YLeaf(YType.uint32, 'access-requests'), ['int'])),
                        ('access_request_retransmits', (YLeaf(YType.uint32, 'access-request-retransmits'), ['int'])),
                        ('access_accepts', (YLeaf(YType.uint32, 'access-accepts'), ['int'])),
                        ('access_rejects', (YLeaf(YType.uint32, 'access-rejects'), ['int'])),
                        ('access_challenges', (YLeaf(YType.uint32, 'access-challenges'), ['int'])),
                        ('bad_access_responses', (YLeaf(YType.uint32, 'bad-access-responses'), ['int'])),
                        ('bad_access_authenticators', (YLeaf(YType.uint32, 'bad-access-authenticators'), ['int'])),
                        ('pending_access_requests', (YLeaf(YType.uint32, 'pending-access-requests'), ['int'])),
                        ('access_timeouts', (YLeaf(YType.uint32, 'access-timeouts'), ['int'])),
                        ('unknown_access_types', (YLeaf(YType.uint32, 'unknown-access-types'), ['int'])),
                        ('dropped_access_responses', (YLeaf(YType.uint32, 'dropped-access-responses'), ['int'])),
                        ('throttled_access_reqs', (YLeaf(YType.uint32, 'throttled-access-reqs'), ['int'])),
                        ('throttled_timed_out_reqs', (YLeaf(YType.uint32, 'throttled-timed-out-reqs'), ['int'])),
                        ('throttled_dropped_reqs', (YLeaf(YType.uint32, 'throttled-dropped-reqs'), ['int'])),
                        ('max_throttled_access_reqs', (YLeaf(YType.uint32, 'max-throttled-access-reqs'), ['int'])),
                        ('currently_throttled_access_reqs', (YLeaf(YType.uint32, 'currently-throttled-access-reqs'), ['int'])),
                        ('authen_response_time', (YLeaf(YType.uint32, 'authen-response-time'), ['int'])),
                        ('authen_transaction_successess', (YLeaf(YType.uint32, 'authen-transaction-successess'), ['int'])),
                        ('authen_transaction_failure', (YLeaf(YType.uint32, 'authen-transaction-failure'), ['int'])),
                        ('authen_unexpected_responses', (YLeaf(YType.uint32, 'authen-unexpected-responses'), ['int'])),
                        ('authen_server_error_responses', (YLeaf(YType.uint32, 'authen-server-error-responses'), ['int'])),
                        ('authen_incorrect_responses', (YLeaf(YType.uint32, 'authen-incorrect-responses'), ['int'])),
                        ('author_requests', (YLeaf(YType.uint32, 'author-requests'), ['int'])),
                        ('author_request_timeouts', (YLeaf(YType.uint32, 'author-request-timeouts'), ['int'])),
                        ('author_response_time', (YLeaf(YType.uint32, 'author-response-time'), ['int'])),
                        ('author_transaction_successess', (YLeaf(YType.uint32, 'author-transaction-successess'), ['int'])),
                        ('author_transaction_failure', (YLeaf(YType.uint32, 'author-transaction-failure'), ['int'])),
                        ('author_unexpected_responses', (YLeaf(YType.uint32, 'author-unexpected-responses'), ['int'])),
                        ('author_server_error_responses', (YLeaf(YType.uint32, 'author-server-error-responses'), ['int'])),
                        ('author_incorrect_responses', (YLeaf(YType.uint32, 'author-incorrect-responses'), ['int'])),
                        ('accounting_rtt', (YLeaf(YType.uint32, 'accounting-rtt'), ['int'])),
                        ('accounting_requests', (YLeaf(YType.uint32, 'accounting-requests'), ['int'])),
                        ('accounting_retransmits', (YLeaf(YType.uint32, 'accounting-retransmits'), ['int'])),
                        ('accounting_responses', (YLeaf(YType.uint32, 'accounting-responses'), ['int'])),
                        ('bad_accounting_responses', (YLeaf(YType.uint32, 'bad-accounting-responses'), ['int'])),
                        ('bad_accounting_authenticators', (YLeaf(YType.uint32, 'bad-accounting-authenticators'), ['int'])),
                        ('pending_accounting_requets', (YLeaf(YType.uint32, 'pending-accounting-requets'), ['int'])),
                        ('accounting_timeouts', (YLeaf(YType.uint32, 'accounting-timeouts'), ['int'])),
                        ('unknown_accounting_types', (YLeaf(YType.uint32, 'unknown-accounting-types'), ['int'])),
                        ('dropped_accounting_responses', (YLeaf(YType.uint32, 'dropped-accounting-responses'), ['int'])),
                        ('is_a_private_server', (YLeaf(YType.boolean, 'is-a-private-server'), ['bool'])),
                        ('total_test_auth_reqs', (YLeaf(YType.uint32, 'total-test-auth-reqs'), ['int'])),
                        ('total_test_auth_timeouts', (YLeaf(YType.uint32, 'total-test-auth-timeouts'), ['int'])),
                        ('total_test_auth_response', (YLeaf(YType.uint32, 'total-test-auth-response'), ['int'])),
                        ('total_test_auth_pending', (YLeaf(YType.uint32, 'total-test-auth-pending'), ['int'])),
                        ('total_test_acct_reqs', (YLeaf(YType.uint32, 'total-test-acct-reqs'), ['int'])),
                        ('total_test_acct_timeouts', (YLeaf(YType.uint32, 'total-test-acct-timeouts'), ['int'])),
                        ('total_test_acct_response', (YLeaf(YType.uint32, 'total-test-acct-response'), ['int'])),
                        ('total_test_acct_pending', (YLeaf(YType.uint32, 'total-test-acct-pending'), ['int'])),
                        ('throttled_acct_transactions', (YLeaf(YType.uint32, 'throttled-acct-transactions'), ['int'])),
                        ('throttled_acct_timed_out_stats', (YLeaf(YType.uint32, 'throttled-acct-timed-out-stats'), ['int'])),
                        ('throttled_acct_failures_stats', (YLeaf(YType.uint32, 'throttled-acct-failures-stats'), ['int'])),
                        ('max_acct_throttled', (YLeaf(YType.uint32, 'max-acct-throttled'), ['int'])),
                        ('throttleda_acct_transactions', (YLeaf(YType.uint32, 'throttleda-acct-transactions'), ['int'])),
                        ('acct_unexpected_responses', (YLeaf(YType.uint32, 'acct-unexpected-responses'), ['int'])),
                        ('acct_server_error_responses', (YLeaf(YType.uint32, 'acct-server-error-responses'), ['int'])),
                        ('acct_incorrect_responses', (YLeaf(YType.uint32, 'acct-incorrect-responses'), ['int'])),
                        ('acct_response_time', (YLeaf(YType.uint32, 'acct-response-time'), ['int'])),
                        ('acct_transaction_successess', (YLeaf(YType.uint32, 'acct-transaction-successess'), ['int'])),
                        ('acct_transaction_failure', (YLeaf(YType.uint32, 'acct-transaction-failure'), ['int'])),
                        ('total_deadtime', (YLeaf(YType.uint32, 'total-deadtime'), ['int'])),
                        ('last_deadtime', (YLeaf(YType.uint32, 'last-deadtime'), ['int'])),
                        ('is_quarantined', (YLeaf(YType.boolean, 'is-quarantined'), ['bool'])),
                        ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                        ('ip_address_xr', (YLeaf(YType.str, 'ip-address-xr'), ['str'])),
                        ('family', (YLeaf(YType.str, 'family'), ['str'])),
                    ])
                    self.ip_address = None
                    self.auth_port_number = None
                    self.acct_port_number = None
                    self.ipv4_address = None
                    self.priority = None
                    self.timeout_xr = None
                    self.retransmit = None
                    self.dead_time = None
                    self.dead_detect_time = None
                    self.dead_detect_tries = None
                    self.authentication_port = None
                    self.accounting_port = None
                    self.state = None
                    self.current_state_duration = None
                    self.previous_state_duration = None
                    self.packets_in = None
                    self.packets_out = None
                    self.timeouts = None
                    self.aborts = None
                    self.replies_expected = None
                    self.redirected_requests = None
                    self.authentication_rtt = None
                    self.access_requests = None
                    self.access_request_retransmits = None
                    self.access_accepts = None
                    self.access_rejects = None
                    self.access_challenges = None
                    self.bad_access_responses = None
                    self.bad_access_authenticators = None
                    self.pending_access_requests = None
                    self.access_timeouts = None
                    self.unknown_access_types = None
                    self.dropped_access_responses = None
                    self.throttled_access_reqs = None
                    self.throttled_timed_out_reqs = None
                    self.throttled_dropped_reqs = None
                    self.max_throttled_access_reqs = None
                    self.currently_throttled_access_reqs = None
                    self.authen_response_time = None
                    self.authen_transaction_successess = None
                    self.authen_transaction_failure = None
                    self.authen_unexpected_responses = None
                    self.authen_server_error_responses = None
                    self.authen_incorrect_responses = None
                    self.author_requests = None
                    self.author_request_timeouts = None
                    self.author_response_time = None
                    self.author_transaction_successess = None
                    self.author_transaction_failure = None
                    self.author_unexpected_responses = None
                    self.author_server_error_responses = None
                    self.author_incorrect_responses = None
                    self.accounting_rtt = None
                    self.accounting_requests = None
                    self.accounting_retransmits = None
                    self.accounting_responses = None
                    self.bad_accounting_responses = None
                    self.bad_accounting_authenticators = None
                    self.pending_accounting_requets = None
                    self.accounting_timeouts = None
                    self.unknown_accounting_types = None
                    self.dropped_accounting_responses = None
                    self.is_a_private_server = None
                    self.total_test_auth_reqs = None
                    self.total_test_auth_timeouts = None
                    self.total_test_auth_response = None
                    self.total_test_auth_pending = None
                    self.total_test_acct_reqs = None
                    self.total_test_acct_timeouts = None
                    self.total_test_acct_response = None
                    self.total_test_acct_pending = None
                    self.throttled_acct_transactions = None
                    self.throttled_acct_timed_out_stats = None
                    self.throttled_acct_failures_stats = None
                    self.max_acct_throttled = None
                    self.throttleda_acct_transactions = None
                    self.acct_unexpected_responses = None
                    self.acct_server_error_responses = None
                    self.acct_incorrect_responses = None
                    self.acct_response_time = None
                    self.acct_transaction_successess = None
                    self.acct_transaction_failure = None
                    self.total_deadtime = None
                    self.last_deadtime = None
                    self.is_quarantined = None
                    self.group_name = None
                    self.ip_address_xr = None
                    self.family = None
                    self._segment_path = lambda: "server"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/servers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.Servers.Server, ['ip_address', 'auth_port_number', 'acct_port_number', u'ipv4_address', u'priority', u'timeout_xr', u'retransmit', u'dead_time', u'dead_detect_time', u'dead_detect_tries', u'authentication_port', u'accounting_port', u'state', u'current_state_duration', u'previous_state_duration', u'packets_in', u'packets_out', u'timeouts', u'aborts', u'replies_expected', u'redirected_requests', u'authentication_rtt', u'access_requests', u'access_request_retransmits', u'access_accepts', u'access_rejects', u'access_challenges', u'bad_access_responses', u'bad_access_authenticators', u'pending_access_requests', u'access_timeouts', u'unknown_access_types', u'dropped_access_responses', u'throttled_access_reqs', u'throttled_timed_out_reqs', u'throttled_dropped_reqs', u'max_throttled_access_reqs', u'currently_throttled_access_reqs', u'authen_response_time', u'authen_transaction_successess', u'authen_transaction_failure', u'authen_unexpected_responses', u'authen_server_error_responses', u'authen_incorrect_responses', u'author_requests', u'author_request_timeouts', u'author_response_time', u'author_transaction_successess', u'author_transaction_failure', u'author_unexpected_responses', u'author_server_error_responses', u'author_incorrect_responses', u'accounting_rtt', u'accounting_requests', u'accounting_retransmits', u'accounting_responses', u'bad_accounting_responses', u'bad_accounting_authenticators', u'pending_accounting_requets', u'accounting_timeouts', u'unknown_accounting_types', u'dropped_accounting_responses', u'is_a_private_server', u'total_test_auth_reqs', u'total_test_auth_timeouts', u'total_test_auth_response', u'total_test_auth_pending', u'total_test_acct_reqs', u'total_test_acct_timeouts', u'total_test_acct_response', u'total_test_acct_pending', u'throttled_acct_transactions', u'throttled_acct_timed_out_stats', u'throttled_acct_failures_stats', u'max_acct_throttled', u'throttleda_acct_transactions', u'acct_unexpected_responses', u'acct_server_error_responses', u'acct_incorrect_responses', u'acct_response_time', u'acct_transaction_successess', u'acct_transaction_failure', u'total_deadtime', u'last_deadtime', u'is_quarantined', u'group_name', u'ip_address_xr', u'family'], name, value)


        class RadiusSourceInterface(Entity):
            """
            RADIUS source interfaces
            
            .. attribute:: list_of_source_interface
            
            	List of source interfaces
            	**type**\: list of  		 :py:class:`ListOfSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Radius.RadiusSourceInterface, self).__init__()

                self.yang_name = "radius-source-interface"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("list-of-source-interface", ("list_of_source_interface", Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface))])
                self._leafs = OrderedDict()

                self.list_of_source_interface = YList(self)
                self._segment_path = lambda: "radius-source-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.RadiusSourceInterface, [], name, value)


            class ListOfSourceInterface(Entity):
                """
                List of source interfaces
                
                .. attribute:: interface_name
                
                	Name of the source interface
                	**type**\: str
                
                .. attribute:: ipaddrv4
                
                	IP address buffer
                	**type**\: str
                
                .. attribute:: ipaddrv6
                
                	IP address buffer
                	**type**\: str
                
                .. attribute:: vrfid
                
                	VRF Id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2017-11-13'

                def __init__(self):
                    super(Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface, self).__init__()

                    self.yang_name = "list-of-source-interface"
                    self.yang_parent_name = "radius-source-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ('ipaddrv4', (YLeaf(YType.str, 'ipaddrv4'), ['str'])),
                        ('ipaddrv6', (YLeaf(YType.str, 'ipaddrv6'), ['str'])),
                        ('vrfid', (YLeaf(YType.uint32, 'vrfid'), ['int'])),
                    ])
                    self.interface_name = None
                    self.ipaddrv4 = None
                    self.ipaddrv6 = None
                    self.vrfid = None
                    self._segment_path = lambda: "list-of-source-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/radius-source-interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface, [u'interface_name', u'ipaddrv4', u'ipaddrv6', u'vrfid'], name, value)


        class Global(Entity):
            """
            RADIUS Client Information
            
            .. attribute:: unknown_authentication_response
            
            	Number of RADIUS Access\-Responsepackets received from unknownaddresses
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authentication_nas_id
            
            	NAS\-Identifier of the RADIUSauthentication client
            	**type**\: str
            
            .. attribute:: unknown_accounting_response
            
            	Number of RADIUS Accounting\-Responsepackets received from unknownaddresses
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_nas_id
            
            	NAS\-Identifier of the RADIUSaccounting client
            	**type**\: str
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2017-11-13'

            def __init__(self):
                super(Aaa.Radius.Global, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "radius"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('unknown_authentication_response', (YLeaf(YType.uint32, 'unknown-authentication-response'), ['int'])),
                    ('authentication_nas_id', (YLeaf(YType.str, 'authentication-nas-id'), ['str'])),
                    ('unknown_accounting_response', (YLeaf(YType.uint32, 'unknown-accounting-response'), ['int'])),
                    ('accounting_nas_id', (YLeaf(YType.str, 'accounting-nas-id'), ['str'])),
                ])
                self.unknown_authentication_response = None
                self.authentication_nas_id = None
                self.unknown_accounting_response = None
                self.accounting_nas_id = None
                self._segment_path = lambda: "global"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Radius.Global, [u'unknown_authentication_response', u'authentication_nas_id', u'unknown_accounting_response', u'accounting_nas_id'], name, value)


    class Tacacs(Entity):
        """
        TACACS operational data
        
        .. attribute:: requests
        
        	TACACS Active Request List
        	**type**\:  :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests>`
        
        .. attribute:: servers
        
        	TACACS server Information
        	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers>`
        
        .. attribute:: server_groups
        
        	TACACS sg Information
        	**type**\:  :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups>`
        
        

        """

        _prefix = 'aaa-tacacs-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Aaa.Tacacs, self).__init__()

            self.yang_name = "tacacs"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("requests", ("requests", Aaa.Tacacs.Requests)), ("servers", ("servers", Aaa.Tacacs.Servers)), ("server-groups", ("server_groups", Aaa.Tacacs.ServerGroups))])
            self._leafs = OrderedDict()

            self.requests = Aaa.Tacacs.Requests()
            self.requests.parent = self
            self._children_name_map["requests"] = "requests"

            self.servers = Aaa.Tacacs.Servers()
            self.servers.parent = self
            self._children_name_map["servers"] = "servers"

            self.server_groups = Aaa.Tacacs.ServerGroups()
            self.server_groups.parent = self
            self._children_name_map["server_groups"] = "server-groups"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-tacacs-oper:tacacs"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Tacacs, [], name, value)


        class Requests(Entity):
            """
            TACACS Active Request List
            
            .. attribute:: request
            
            	request
            	**type**\: list of  		 :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Requests, self).__init__()

                self.yang_name = "requests"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("request", ("request", Aaa.Tacacs.Requests.Request))])
                self._leafs = OrderedDict()

                self.request = YList(self)
                self._segment_path = lambda: "requests"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Requests, [], name, value)


            class Request(Entity):
                """
                request
                
                .. attribute:: tacacs_requestbag
                
                	tacacs requestbag
                	**type**\: list of  		 :py:class:`TacacsRequestbag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request.TacacsRequestbag>`
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Requests.Request, self).__init__()

                    self.yang_name = "request"
                    self.yang_parent_name = "requests"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("tacacs-requestbag", ("tacacs_requestbag", Aaa.Tacacs.Requests.Request.TacacsRequestbag))])
                    self._leafs = OrderedDict()

                    self.tacacs_requestbag = YList(self)
                    self._segment_path = lambda: "request"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/requests/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.Requests.Request, [], name, value)


                class TacacsRequestbag(Entity):
                    """
                    tacacs requestbag
                    
                    .. attribute:: time_remaining
                    
                    	time remaining for this request
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_out
                    
                    	bytes written
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: out_pak_size
                    
                    	size of the packet to be sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_in
                    
                    	bytes read from socket
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: in_pak_size
                    
                    	size of the packet to be received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pak_type
                    
                    	the type of packet
                    	**type**\: str
                    
                    .. attribute:: session_id
                    
                    	same as in pkt hdr
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sock
                    
                    	socket number
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Tacacs.Requests.Request.TacacsRequestbag, self).__init__()

                        self.yang_name = "tacacs-requestbag"
                        self.yang_parent_name = "request"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time_remaining', (YLeaf(YType.uint32, 'time-remaining'), ['int'])),
                            ('bytes_out', (YLeaf(YType.uint32, 'bytes-out'), ['int'])),
                            ('out_pak_size', (YLeaf(YType.uint32, 'out-pak-size'), ['int'])),
                            ('bytes_in', (YLeaf(YType.uint32, 'bytes-in'), ['int'])),
                            ('in_pak_size', (YLeaf(YType.uint32, 'in-pak-size'), ['int'])),
                            ('pak_type', (YLeaf(YType.str, 'pak-type'), ['str'])),
                            ('session_id', (YLeaf(YType.int32, 'session-id'), ['int'])),
                            ('sock', (YLeaf(YType.int32, 'sock'), ['int'])),
                        ])
                        self.time_remaining = None
                        self.bytes_out = None
                        self.out_pak_size = None
                        self.bytes_in = None
                        self.in_pak_size = None
                        self.pak_type = None
                        self.session_id = None
                        self.sock = None
                        self._segment_path = lambda: "tacacs-requestbag"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/requests/request/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Tacacs.Requests.Request.TacacsRequestbag, ['time_remaining', 'bytes_out', 'out_pak_size', 'bytes_in', 'in_pak_size', 'pak_type', 'session_id', 'sock'], name, value)


        class Servers(Entity):
            """
            TACACS server Information
            
            .. attribute:: server
            
            	server
            	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers.Server>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.Servers, self).__init__()

                self.yang_name = "servers"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("server", ("server", Aaa.Tacacs.Servers.Server))])
                self._leafs = OrderedDict()

                self.server = YList(self)
                self._segment_path = lambda: "servers"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.Servers, [], name, value)


            class Server(Entity):
                """
                server
                
                .. attribute:: addr
                
                	internet address of T+ server
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: timeout
                
                	per\-server timeout
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port
                
                	per server port to use
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bytes_in
                
                	# of bytes read
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: bytes_out
                
                	# of bytes out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: closes
                
                	socket closes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: opens
                
                	socket opens
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: errors
                
                	error count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: aborts
                
                	abort count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_in
                
                	# of incoming packets read
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_out
                
                	# of outgoing packets sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	# of replies expected to arrive
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: up
                
                	is the server UP or down ?
                	**type**\: bool
                
                .. attribute:: conn_up
                
                	is the server connected ?
                	**type**\: bool
                
                .. attribute:: single_connect
                
                	is this a single connect server ?
                	**type**\: bool
                
                .. attribute:: is_private
                
                	is this a private server ?
                	**type**\: bool
                
                .. attribute:: vrf_name
                
                	VRF in which server is reachable
                	**type**\: str
                
                	**length:** 0..33
                
                .. attribute:: addr_buf
                
                	IP address buffer
                	**type**\: str
                
                	**length:** 0..46
                
                .. attribute:: family
                
                	IP address Family
                	**type**\: str
                
                	**length:** 0..5
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.Servers.Server, self).__init__()

                    self.yang_name = "server"
                    self.yang_parent_name = "servers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('addr', (YLeaf(YType.str, 'addr'), ['str'])),
                        ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                        ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ('bytes_in', (YLeaf(YType.uint32, 'bytes-in'), ['int'])),
                        ('bytes_out', (YLeaf(YType.uint32, 'bytes-out'), ['int'])),
                        ('closes', (YLeaf(YType.uint32, 'closes'), ['int'])),
                        ('opens', (YLeaf(YType.uint32, 'opens'), ['int'])),
                        ('errors', (YLeaf(YType.uint32, 'errors'), ['int'])),
                        ('aborts', (YLeaf(YType.uint32, 'aborts'), ['int'])),
                        ('paks_in', (YLeaf(YType.uint32, 'paks-in'), ['int'])),
                        ('paks_out', (YLeaf(YType.uint32, 'paks-out'), ['int'])),
                        ('replies_expected', (YLeaf(YType.uint32, 'replies-expected'), ['int'])),
                        ('up', (YLeaf(YType.boolean, 'up'), ['bool'])),
                        ('conn_up', (YLeaf(YType.boolean, 'conn-up'), ['bool'])),
                        ('single_connect', (YLeaf(YType.boolean, 'single-connect'), ['bool'])),
                        ('is_private', (YLeaf(YType.boolean, 'is-private'), ['bool'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('addr_buf', (YLeaf(YType.str, 'addr-buf'), ['str'])),
                        ('family', (YLeaf(YType.str, 'family'), ['str'])),
                    ])
                    self.addr = None
                    self.timeout = None
                    self.port = None
                    self.bytes_in = None
                    self.bytes_out = None
                    self.closes = None
                    self.opens = None
                    self.errors = None
                    self.aborts = None
                    self.paks_in = None
                    self.paks_out = None
                    self.replies_expected = None
                    self.up = None
                    self.conn_up = None
                    self.single_connect = None
                    self.is_private = None
                    self.vrf_name = None
                    self.addr_buf = None
                    self.family = None
                    self._segment_path = lambda: "server"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/servers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.Servers.Server, ['addr', 'timeout', 'port', 'bytes_in', 'bytes_out', 'closes', 'opens', 'errors', 'aborts', 'paks_in', 'paks_out', 'replies_expected', 'up', 'conn_up', 'single_connect', 'is_private', 'vrf_name', 'addr_buf', 'family'], name, value)


        class ServerGroups(Entity):
            """
            TACACS sg Information
            
            .. attribute:: server_group
            
            	server group
            	**type**\: list of  		 :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Aaa.Tacacs.ServerGroups, self).__init__()

                self.yang_name = "server-groups"
                self.yang_parent_name = "tacacs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("server-group", ("server_group", Aaa.Tacacs.ServerGroups.ServerGroup))])
                self._leafs = OrderedDict()

                self.server_group = YList(self)
                self._segment_path = lambda: "server-groups"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Tacacs.ServerGroups, [], name, value)


            class ServerGroup(Entity):
                """
                server group
                
                .. attribute:: group_name
                
                	name of the server group
                	**type**\: str
                
                .. attribute:: sg_map_num
                
                	server group mapped number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	vrf of the group
                	**type**\: str
                
                	**length:** 0..33
                
                .. attribute:: server
                
                	list of servers in this group
                	**type**\: list of  		 :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup.Server>`
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Aaa.Tacacs.ServerGroups.ServerGroup, self).__init__()

                    self.yang_name = "server-group"
                    self.yang_parent_name = "server-groups"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("server", ("server", Aaa.Tacacs.ServerGroups.ServerGroup.Server))])
                    self._leafs = OrderedDict([
                        ('group_name', (YLeaf(YType.str, 'group-name'), ['str'])),
                        ('sg_map_num', (YLeaf(YType.uint32, 'sg-map-num'), ['int'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ])
                    self.group_name = None
                    self.sg_map_num = None
                    self.vrf_name = None

                    self.server = YList(self)
                    self._segment_path = lambda: "server-group"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/server-groups/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Tacacs.ServerGroups.ServerGroup, ['group_name', 'sg_map_num', 'vrf_name'], name, value)


                class Server(Entity):
                    """
                    list of servers in this group
                    
                    .. attribute:: addr
                    
                    	internet address of T+ server
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: timeout
                    
                    	per\-server timeout
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port
                    
                    	per server port to use
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_in
                    
                    	# of bytes read
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_out
                    
                    	# of bytes out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: closes
                    
                    	socket closes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opens
                    
                    	socket opens
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: errors
                    
                    	error count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: aborts
                    
                    	abort count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_in
                    
                    	# of incoming packets read
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_out
                    
                    	# of outgoing packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_expected
                    
                    	# of replies expected to arrive
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up
                    
                    	is the server UP or down ?
                    	**type**\: bool
                    
                    .. attribute:: conn_up
                    
                    	is the server connected ?
                    	**type**\: bool
                    
                    .. attribute:: single_connect
                    
                    	is this a single connect server ?
                    	**type**\: bool
                    
                    .. attribute:: is_private
                    
                    	is this a private server ?
                    	**type**\: bool
                    
                    .. attribute:: vrf_name
                    
                    	VRF in which server is reachable
                    	**type**\: str
                    
                    	**length:** 0..33
                    
                    .. attribute:: addr_buf
                    
                    	IP address buffer
                    	**type**\: str
                    
                    	**length:** 0..46
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\: str
                    
                    	**length:** 0..5
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Aaa.Tacacs.ServerGroups.ServerGroup.Server, self).__init__()

                        self.yang_name = "server"
                        self.yang_parent_name = "server-group"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('addr', (YLeaf(YType.str, 'addr'), ['str'])),
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                            ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                            ('bytes_in', (YLeaf(YType.uint32, 'bytes-in'), ['int'])),
                            ('bytes_out', (YLeaf(YType.uint32, 'bytes-out'), ['int'])),
                            ('closes', (YLeaf(YType.uint32, 'closes'), ['int'])),
                            ('opens', (YLeaf(YType.uint32, 'opens'), ['int'])),
                            ('errors', (YLeaf(YType.uint32, 'errors'), ['int'])),
                            ('aborts', (YLeaf(YType.uint32, 'aborts'), ['int'])),
                            ('paks_in', (YLeaf(YType.uint32, 'paks-in'), ['int'])),
                            ('paks_out', (YLeaf(YType.uint32, 'paks-out'), ['int'])),
                            ('replies_expected', (YLeaf(YType.uint32, 'replies-expected'), ['int'])),
                            ('up', (YLeaf(YType.boolean, 'up'), ['bool'])),
                            ('conn_up', (YLeaf(YType.boolean, 'conn-up'), ['bool'])),
                            ('single_connect', (YLeaf(YType.boolean, 'single-connect'), ['bool'])),
                            ('is_private', (YLeaf(YType.boolean, 'is-private'), ['bool'])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('addr_buf', (YLeaf(YType.str, 'addr-buf'), ['str'])),
                            ('family', (YLeaf(YType.str, 'family'), ['str'])),
                        ])
                        self.addr = None
                        self.timeout = None
                        self.port = None
                        self.bytes_in = None
                        self.bytes_out = None
                        self.closes = None
                        self.opens = None
                        self.errors = None
                        self.aborts = None
                        self.paks_in = None
                        self.paks_out = None
                        self.replies_expected = None
                        self.up = None
                        self.conn_up = None
                        self.single_connect = None
                        self.is_private = None
                        self.vrf_name = None
                        self.addr_buf = None
                        self.family = None
                        self._segment_path = lambda: "server"
                        self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/server-groups/server-group/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Aaa.Tacacs.ServerGroups.ServerGroup.Server, ['addr', 'timeout', 'port', 'bytes_in', 'bytes_out', 'closes', 'opens', 'errors', 'aborts', 'paks_in', 'paks_out', 'replies_expected', 'up', 'conn_up', 'single_connect', 'is_private', 'vrf_name', 'addr_buf', 'family'], name, value)


    class Diameter(Entity):
        """
        Diameter operational data
        
        .. attribute:: gy
        
        	Diameter global gy data
        	**type**\:  :py:class:`Gy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gy>`
        
        .. attribute:: gx_statistics
        
        	Diameter Gx Statistics data
        	**type**\:  :py:class:`GxStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxStatistics>`
        
        .. attribute:: gx
        
        	Diameter global gx data
        	**type**\:  :py:class:`Gx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gx>`
        
        .. attribute:: peers
        
        	Diameter peer global data
        	**type**\:  :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers>`
        
        .. attribute:: nas
        
        	Diameter NAS data
        	**type**\:  :py:class:`Nas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas>`
        
        .. attribute:: nas_summary
        
        	Diameter NAS summary
        	**type**\:  :py:class:`NasSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSummary>`
        
        .. attribute:: gy_session_ids
        
        	Diameter Gy Session data list
        	**type**\:  :py:class:`GySessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds>`
        
        .. attribute:: gy_statistics
        
        	Diameter Gy Statistics data
        	**type**\:  :py:class:`GyStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GyStatistics>`
        
        .. attribute:: gx_session_ids
        
        	Diameter Gx Session data list
        	**type**\:  :py:class:`GxSessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds>`
        
        .. attribute:: nas_session
        
        	Diameter Nas Session data
        	**type**\:  :py:class:`NasSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession>`
        
        

        """

        _prefix = 'aaa-diameter-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(Aaa.Diameter, self).__init__()

            self.yang_name = "diameter"
            self.yang_parent_name = "aaa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("gy", ("gy", Aaa.Diameter.Gy)), ("gx-statistics", ("gx_statistics", Aaa.Diameter.GxStatistics)), ("gx", ("gx", Aaa.Diameter.Gx)), ("peers", ("peers", Aaa.Diameter.Peers)), ("nas", ("nas", Aaa.Diameter.Nas)), ("nas-summary", ("nas_summary", Aaa.Diameter.NasSummary)), ("gy-session-ids", ("gy_session_ids", Aaa.Diameter.GySessionIds)), ("gy-statistics", ("gy_statistics", Aaa.Diameter.GyStatistics)), ("gx-session-ids", ("gx_session_ids", Aaa.Diameter.GxSessionIds)), ("nas-session", ("nas_session", Aaa.Diameter.NasSession))])
            self._leafs = OrderedDict()

            self.gy = Aaa.Diameter.Gy()
            self.gy.parent = self
            self._children_name_map["gy"] = "gy"

            self.gx_statistics = Aaa.Diameter.GxStatistics()
            self.gx_statistics.parent = self
            self._children_name_map["gx_statistics"] = "gx-statistics"

            self.gx = Aaa.Diameter.Gx()
            self.gx.parent = self
            self._children_name_map["gx"] = "gx"

            self.peers = Aaa.Diameter.Peers()
            self.peers.parent = self
            self._children_name_map["peers"] = "peers"

            self.nas = Aaa.Diameter.Nas()
            self.nas.parent = self
            self._children_name_map["nas"] = "nas"

            self.nas_summary = Aaa.Diameter.NasSummary()
            self.nas_summary.parent = self
            self._children_name_map["nas_summary"] = "nas-summary"

            self.gy_session_ids = Aaa.Diameter.GySessionIds()
            self.gy_session_ids.parent = self
            self._children_name_map["gy_session_ids"] = "gy-session-ids"

            self.gy_statistics = Aaa.Diameter.GyStatistics()
            self.gy_statistics.parent = self
            self._children_name_map["gy_statistics"] = "gy-statistics"

            self.gx_session_ids = Aaa.Diameter.GxSessionIds()
            self.gx_session_ids.parent = self
            self._children_name_map["gx_session_ids"] = "gx-session-ids"

            self.nas_session = Aaa.Diameter.NasSession()
            self.nas_session.parent = self
            self._children_name_map["nas_session"] = "nas-session"
            self._segment_path = lambda: "Cisco-IOS-XR-aaa-diameter-oper:diameter"
            self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Aaa.Diameter, [], name, value)


        class Gy(Entity):
            """
            Diameter global gy data
            
            .. attribute:: is_enabled
            
            	Gy state
            	**type**\: bool
            
            .. attribute:: tx_timer
            
            	Gy transaction timer in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmits
            
            	Gy retransmit count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.Gy, self).__init__()

                self.yang_name = "gy"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                    ('tx_timer', (YLeaf(YType.uint32, 'tx-timer'), ['int'])),
                    ('retransmits', (YLeaf(YType.uint32, 'retransmits'), ['int'])),
                ])
                self.is_enabled = None
                self.tx_timer = None
                self.retransmits = None
                self._segment_path = lambda: "gy"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Gy, ['is_enabled', 'tx_timer', 'retransmits'], name, value)


        class GxStatistics(Entity):
            """
            Diameter Gx Statistics data
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messsages
            
            	ASA Sent Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_termination_messages
            
            	Session Termination from server
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.GxStatistics, self).__init__()

                self.yang_name = "gx-statistics"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccr_init_messages', (YLeaf(YType.uint32, 'ccr-init-messages'), ['int'])),
                    ('ccr_init_failed_messages', (YLeaf(YType.uint32, 'ccr-init-failed-messages'), ['int'])),
                    ('ccr_init_timed_out_messages', (YLeaf(YType.uint32, 'ccr-init-timed-out-messages'), ['int'])),
                    ('ccr_init_retry_messages', (YLeaf(YType.uint32, 'ccr-init-retry-messages'), ['int'])),
                    ('ccr_update_messages', (YLeaf(YType.uint32, 'ccr-update-messages'), ['int'])),
                    ('ccr_update_failed_messages', (YLeaf(YType.uint32, 'ccr-update-failed-messages'), ['int'])),
                    ('ccr_update_timed_out_messages', (YLeaf(YType.uint32, 'ccr-update-timed-out-messages'), ['int'])),
                    ('ccr_update_retry_messages', (YLeaf(YType.uint32, 'ccr-update-retry-messages'), ['int'])),
                    ('ccr_final_messages', (YLeaf(YType.uint32, 'ccr-final-messages'), ['int'])),
                    ('ccr_final_failed_messages', (YLeaf(YType.uint32, 'ccr-final-failed-messages'), ['int'])),
                    ('ccr_final_timed_out_messages', (YLeaf(YType.uint32, 'ccr-final-timed-out-messages'), ['int'])),
                    ('ccr_final_retry_messages', (YLeaf(YType.uint32, 'ccr-final-retry-messages'), ['int'])),
                    ('cca_init_messages', (YLeaf(YType.uint32, 'cca-init-messages'), ['int'])),
                    ('cca_init_error_messages', (YLeaf(YType.uint32, 'cca-init-error-messages'), ['int'])),
                    ('cca_update_messages', (YLeaf(YType.uint32, 'cca-update-messages'), ['int'])),
                    ('cca_update_error_messages', (YLeaf(YType.uint32, 'cca-update-error-messages'), ['int'])),
                    ('cca_final_messages', (YLeaf(YType.uint32, 'cca-final-messages'), ['int'])),
                    ('cca_final_error_messages', (YLeaf(YType.uint32, 'cca-final-error-messages'), ['int'])),
                    ('rar_received_messages', (YLeaf(YType.uint32, 'rar-received-messages'), ['int'])),
                    ('rar_received_error_messages', (YLeaf(YType.uint32, 'rar-received-error-messages'), ['int'])),
                    ('raa_sent_messages', (YLeaf(YType.uint32, 'raa-sent-messages'), ['int'])),
                    ('raa_sent_error_messages', (YLeaf(YType.uint32, 'raa-sent-error-messages'), ['int'])),
                    ('asr_received_messages', (YLeaf(YType.uint32, 'asr-received-messages'), ['int'])),
                    ('asr_received_error_messages', (YLeaf(YType.uint32, 'asr-received-error-messages'), ['int'])),
                    ('asa_sent_messsages', (YLeaf(YType.uint32, 'asa-sent-messsages'), ['int'])),
                    ('asa_sent_error_messages', (YLeaf(YType.uint32, 'asa-sent-error-messages'), ['int'])),
                    ('session_termination_messages', (YLeaf(YType.uint32, 'session-termination-messages'), ['int'])),
                    ('unknown_request_messages', (YLeaf(YType.uint32, 'unknown-request-messages'), ['int'])),
                    ('restore_sessions', (YLeaf(YType.uint32, 'restore-sessions'), ['int'])),
                    ('open_sessions', (YLeaf(YType.uint32, 'open-sessions'), ['int'])),
                    ('close_sessions', (YLeaf(YType.uint32, 'close-sessions'), ['int'])),
                    ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                ])
                self.ccr_init_messages = None
                self.ccr_init_failed_messages = None
                self.ccr_init_timed_out_messages = None
                self.ccr_init_retry_messages = None
                self.ccr_update_messages = None
                self.ccr_update_failed_messages = None
                self.ccr_update_timed_out_messages = None
                self.ccr_update_retry_messages = None
                self.ccr_final_messages = None
                self.ccr_final_failed_messages = None
                self.ccr_final_timed_out_messages = None
                self.ccr_final_retry_messages = None
                self.cca_init_messages = None
                self.cca_init_error_messages = None
                self.cca_update_messages = None
                self.cca_update_error_messages = None
                self.cca_final_messages = None
                self.cca_final_error_messages = None
                self.rar_received_messages = None
                self.rar_received_error_messages = None
                self.raa_sent_messages = None
                self.raa_sent_error_messages = None
                self.asr_received_messages = None
                self.asr_received_error_messages = None
                self.asa_sent_messsages = None
                self.asa_sent_error_messages = None
                self.session_termination_messages = None
                self.unknown_request_messages = None
                self.restore_sessions = None
                self.open_sessions = None
                self.close_sessions = None
                self.active_sessions = None
                self._segment_path = lambda: "gx-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GxStatistics, ['ccr_init_messages', 'ccr_init_failed_messages', 'ccr_init_timed_out_messages', 'ccr_init_retry_messages', 'ccr_update_messages', 'ccr_update_failed_messages', 'ccr_update_timed_out_messages', 'ccr_update_retry_messages', 'ccr_final_messages', 'ccr_final_failed_messages', 'ccr_final_timed_out_messages', 'ccr_final_retry_messages', 'cca_init_messages', 'cca_init_error_messages', 'cca_update_messages', 'cca_update_error_messages', 'cca_final_messages', 'cca_final_error_messages', 'rar_received_messages', 'rar_received_error_messages', 'raa_sent_messages', 'raa_sent_error_messages', 'asr_received_messages', 'asr_received_error_messages', 'asa_sent_messsages', 'asa_sent_error_messages', 'session_termination_messages', 'unknown_request_messages', 'restore_sessions', 'open_sessions', 'close_sessions', 'active_sessions'], name, value)


        class Gx(Entity):
            """
            Diameter global gx data
            
            .. attribute:: is_enabled
            
            	Gx state
            	**type**\: bool
            
            .. attribute:: tx_timer
            
            	Gx transaction timer in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: retransmits
            
            	Gx retransmit count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.Gx, self).__init__()

                self.yang_name = "gx"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('is_enabled', (YLeaf(YType.boolean, 'is-enabled'), ['bool'])),
                    ('tx_timer', (YLeaf(YType.uint32, 'tx-timer'), ['int'])),
                    ('retransmits', (YLeaf(YType.uint32, 'retransmits'), ['int'])),
                ])
                self.is_enabled = None
                self.tx_timer = None
                self.retransmits = None
                self._segment_path = lambda: "gx"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Gx, ['is_enabled', 'tx_timer', 'retransmits'], name, value)


        class Peers(Entity):
            """
            Diameter peer global data
            
            .. attribute:: origin_host
            
            	Origin Host
            	**type**\: str
            
            .. attribute:: origin_realm
            
            	Origin Realm
            	**type**\: str
            
            .. attribute:: source_interface
            
            	Source Interface
            	**type**\: str
            
            .. attribute:: tls_trustpoint
            
            	TLS Trustpoint
            	**type**\: str
            
            .. attribute:: conn_retry_timer
            
            	Connection retry timer in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: watchdog_timer
            
            	Watch dog timer in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: transaction_timer
            
            	Transaction timer in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: trans_total
            
            	Total number of transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: trans_max
            
            	Maximum number of transactions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: peer
            
            	Peer List
            	**type**\: list of  		 :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers.Peer>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.Peers, self).__init__()

                self.yang_name = "peers"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("peer", ("peer", Aaa.Diameter.Peers.Peer))])
                self._leafs = OrderedDict([
                    ('origin_host', (YLeaf(YType.str, 'origin-host'), ['str'])),
                    ('origin_realm', (YLeaf(YType.str, 'origin-realm'), ['str'])),
                    ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                    ('tls_trustpoint', (YLeaf(YType.str, 'tls-trustpoint'), ['str'])),
                    ('conn_retry_timer', (YLeaf(YType.uint32, 'conn-retry-timer'), ['int'])),
                    ('watchdog_timer', (YLeaf(YType.uint32, 'watchdog-timer'), ['int'])),
                    ('transaction_timer', (YLeaf(YType.uint32, 'transaction-timer'), ['int'])),
                    ('trans_total', (YLeaf(YType.uint32, 'trans-total'), ['int'])),
                    ('trans_max', (YLeaf(YType.uint32, 'trans-max'), ['int'])),
                ])
                self.origin_host = None
                self.origin_realm = None
                self.source_interface = None
                self.tls_trustpoint = None
                self.conn_retry_timer = None
                self.watchdog_timer = None
                self.transaction_timer = None
                self.trans_total = None
                self.trans_max = None

                self.peer = YList(self)
                self._segment_path = lambda: "peers"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Peers, ['origin_host', 'origin_realm', 'source_interface', 'tls_trustpoint', 'conn_retry_timer', 'watchdog_timer', 'transaction_timer', 'trans_total', 'trans_max'], name, value)


            class Peer(Entity):
                """
                Peer List
                
                .. attribute:: peer_name
                
                	Peer Name
                	**type**\: str
                
                .. attribute:: peer_index
                
                	Peer Index
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: address
                
                	IPv4 or IPv6 address of DIAMETER peer
                	**type**\: str
                
                .. attribute:: port
                
                	Port number on which the peeris running
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_connect
                
                	Local Connection port
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: protocol_type
                
                	Protocol Type
                	**type**\:  :py:class:`ProtocolTypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.ProtocolTypeValue>`
                
                .. attribute:: security_type
                
                	Security type used to transport
                	**type**\:  :py:class:`SecurityTypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.SecurityTypeValue>`
                
                .. attribute:: conn_retry_timer
                
                	Connection retry timer in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: watchdog_timer
                
                	Watch dog timer in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transaction_timer
                
                	Transaction timer in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: vrf_name
                
                	Vrf Name
                	**type**\: str
                
                .. attribute:: source_interface
                
                	Source Interface
                	**type**\: str
                
                .. attribute:: destination_host
                
                	Destination host name
                	**type**\: str
                
                .. attribute:: destination_realm
                
                	Destination realm
                	**type**\: str
                
                .. attribute:: peer_type
                
                	Peer Type
                	**type**\:  :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.Peer>`
                
                .. attribute:: firmware_revision
                
                	Firmware revision
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: state_duration
                
                	State Duration in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: last_disconnect_cause
                
                	Last Disconnect Reason
                	**type**\:  :py:class:`DisconnectCause <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.DisconnectCause>`
                
                .. attribute:: who_init_disconnect
                
                	Who Initiated Disconnect
                	**type**\:  :py:class:`WhoInitiatedDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.WhoInitiatedDisconnect>`
                
                .. attribute:: in_as_rs
                
                	Incoming ASRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_rs
                
                	Outgoing ASRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_as_as
                
                	Incoming ASAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_as
                
                	Outgoing ASAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_rs
                
                	Incoming ACRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_rs
                
                	Outgoing ACRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_as
                
                	Incoming ACAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_as
                
                	Outgoing ACAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_rs
                
                	Incoming CERs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_rs
                
                	Outgoing CERs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_as
                
                	Incoming CEAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_as
                
                	Outgoing CEAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_rs
                
                	Incoming DWRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_rs
                
                	Outgoing DWRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_as
                
                	Incoming DWAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_as
                
                	Outgoing DWAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_rs
                
                	Incoming DPRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_rs
                
                	Outgoing DPRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_as
                
                	Incoming DPAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_as
                
                	Outgoing DPAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_rs
                
                	Incoming RARs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_rs
                
                	Outgoing RARs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_as
                
                	Incoming RAAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_as
                
                	Outgoing RAAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_rs
                
                	Incoming STRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_rs
                
                	Outgoing STRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_as
                
                	Incoming STAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_as
                
                	Outgoing STAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_rs
                
                	Incoming CCRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_rs
                
                	Outgoing CCRs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_as
                
                	Incoming CCAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_as
                
                	Outgoing CCAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_aa_rs
                
                	Outgoing AARs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_aa_as
                
                	Incoming AAAs
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: malformed_requests
                
                	Malformed Requests
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_proto_errors
                
                	Protocol Error Received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_proto_errors
                
                	Protocol Error Sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_transient_fails
                
                	Transient failures Received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_transient_fails
                
                	Transient failures Sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_permanent_fails
                
                	Permanent Failures Received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_permanent_fails
                
                	Permanent Failures Sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: transport_down
                
                	Transport Down
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	Peer Connection Status
                	**type**\:  :py:class:`PeerStateValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.PeerStateValue>`
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Diameter.Peers.Peer, self).__init__()

                    self.yang_name = "peer"
                    self.yang_parent_name = "peers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('peer_name', (YLeaf(YType.str, 'peer-name'), ['str'])),
                        ('peer_index', (YLeaf(YType.uint32, 'peer-index'), ['int'])),
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('port', (YLeaf(YType.uint32, 'port'), ['int'])),
                        ('port_connect', (YLeaf(YType.uint32, 'port-connect'), ['int'])),
                        ('protocol_type', (YLeaf(YType.enumeration, 'protocol-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'ProtocolTypeValue', '')])),
                        ('security_type', (YLeaf(YType.enumeration, 'security-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'SecurityTypeValue', '')])),
                        ('conn_retry_timer', (YLeaf(YType.uint32, 'conn-retry-timer'), ['int'])),
                        ('watchdog_timer', (YLeaf(YType.uint32, 'watchdog-timer'), ['int'])),
                        ('transaction_timer', (YLeaf(YType.uint32, 'transaction-timer'), ['int'])),
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                        ('destination_host', (YLeaf(YType.str, 'destination-host'), ['str'])),
                        ('destination_realm', (YLeaf(YType.str, 'destination-realm'), ['str'])),
                        ('peer_type', (YLeaf(YType.enumeration, 'peer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'Peer', '')])),
                        ('firmware_revision', (YLeaf(YType.uint32, 'firmware-revision'), ['int'])),
                        ('state_duration', (YLeaf(YType.uint32, 'state-duration'), ['int'])),
                        ('last_disconnect_cause', (YLeaf(YType.enumeration, 'last-disconnect-cause'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'DisconnectCause', '')])),
                        ('who_init_disconnect', (YLeaf(YType.enumeration, 'who-init-disconnect'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'WhoInitiatedDisconnect', '')])),
                        ('in_as_rs', (YLeaf(YType.uint32, 'in-as-rs'), ['int'])),
                        ('out_as_rs', (YLeaf(YType.uint32, 'out-as-rs'), ['int'])),
                        ('in_as_as', (YLeaf(YType.uint32, 'in-as-as'), ['int'])),
                        ('out_as_as', (YLeaf(YType.uint32, 'out-as-as'), ['int'])),
                        ('in_ac_rs', (YLeaf(YType.uint32, 'in-ac-rs'), ['int'])),
                        ('out_ac_rs', (YLeaf(YType.uint32, 'out-ac-rs'), ['int'])),
                        ('in_ac_as', (YLeaf(YType.uint32, 'in-ac-as'), ['int'])),
                        ('out_ac_as', (YLeaf(YType.uint32, 'out-ac-as'), ['int'])),
                        ('in_ce_rs', (YLeaf(YType.uint32, 'in-ce-rs'), ['int'])),
                        ('out_ce_rs', (YLeaf(YType.uint32, 'out-ce-rs'), ['int'])),
                        ('in_ce_as', (YLeaf(YType.uint32, 'in-ce-as'), ['int'])),
                        ('out_ce_as', (YLeaf(YType.uint32, 'out-ce-as'), ['int'])),
                        ('in_dw_rs', (YLeaf(YType.uint32, 'in-dw-rs'), ['int'])),
                        ('out_dw_rs', (YLeaf(YType.uint32, 'out-dw-rs'), ['int'])),
                        ('in_dw_as', (YLeaf(YType.uint32, 'in-dw-as'), ['int'])),
                        ('out_dw_as', (YLeaf(YType.uint32, 'out-dw-as'), ['int'])),
                        ('in_dp_rs', (YLeaf(YType.uint32, 'in-dp-rs'), ['int'])),
                        ('out_dp_rs', (YLeaf(YType.uint32, 'out-dp-rs'), ['int'])),
                        ('in_dp_as', (YLeaf(YType.uint32, 'in-dp-as'), ['int'])),
                        ('out_dp_as', (YLeaf(YType.uint32, 'out-dp-as'), ['int'])),
                        ('in_ra_rs', (YLeaf(YType.uint32, 'in-ra-rs'), ['int'])),
                        ('out_ra_rs', (YLeaf(YType.uint32, 'out-ra-rs'), ['int'])),
                        ('in_ra_as', (YLeaf(YType.uint32, 'in-ra-as'), ['int'])),
                        ('out_ra_as', (YLeaf(YType.uint32, 'out-ra-as'), ['int'])),
                        ('in_st_rs', (YLeaf(YType.uint32, 'in-st-rs'), ['int'])),
                        ('out_st_rs', (YLeaf(YType.uint32, 'out-st-rs'), ['int'])),
                        ('in_st_as', (YLeaf(YType.uint32, 'in-st-as'), ['int'])),
                        ('out_st_as', (YLeaf(YType.uint32, 'out-st-as'), ['int'])),
                        ('in_cc_rs', (YLeaf(YType.uint32, 'in-cc-rs'), ['int'])),
                        ('out_cc_rs', (YLeaf(YType.uint32, 'out-cc-rs'), ['int'])),
                        ('in_cc_as', (YLeaf(YType.uint32, 'in-cc-as'), ['int'])),
                        ('out_cc_as', (YLeaf(YType.uint32, 'out-cc-as'), ['int'])),
                        ('out_aa_rs', (YLeaf(YType.uint32, 'out-aa-rs'), ['int'])),
                        ('in_aa_as', (YLeaf(YType.uint32, 'in-aa-as'), ['int'])),
                        ('malformed_requests', (YLeaf(YType.uint32, 'malformed-requests'), ['int'])),
                        ('received_proto_errors', (YLeaf(YType.uint32, 'received-proto-errors'), ['int'])),
                        ('sent_proto_errors', (YLeaf(YType.uint32, 'sent-proto-errors'), ['int'])),
                        ('received_transient_fails', (YLeaf(YType.uint32, 'received-transient-fails'), ['int'])),
                        ('sent_transient_fails', (YLeaf(YType.uint32, 'sent-transient-fails'), ['int'])),
                        ('received_permanent_fails', (YLeaf(YType.uint32, 'received-permanent-fails'), ['int'])),
                        ('sent_permanent_fails', (YLeaf(YType.uint32, 'sent-permanent-fails'), ['int'])),
                        ('transport_down', (YLeaf(YType.uint32, 'transport-down'), ['int'])),
                        ('state', (YLeaf(YType.enumeration, 'state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'PeerStateValue', '')])),
                    ])
                    self.peer_name = None
                    self.peer_index = None
                    self.address = None
                    self.port = None
                    self.port_connect = None
                    self.protocol_type = None
                    self.security_type = None
                    self.conn_retry_timer = None
                    self.watchdog_timer = None
                    self.transaction_timer = None
                    self.vrf_name = None
                    self.source_interface = None
                    self.destination_host = None
                    self.destination_realm = None
                    self.peer_type = None
                    self.firmware_revision = None
                    self.state_duration = None
                    self.last_disconnect_cause = None
                    self.who_init_disconnect = None
                    self.in_as_rs = None
                    self.out_as_rs = None
                    self.in_as_as = None
                    self.out_as_as = None
                    self.in_ac_rs = None
                    self.out_ac_rs = None
                    self.in_ac_as = None
                    self.out_ac_as = None
                    self.in_ce_rs = None
                    self.out_ce_rs = None
                    self.in_ce_as = None
                    self.out_ce_as = None
                    self.in_dw_rs = None
                    self.out_dw_rs = None
                    self.in_dw_as = None
                    self.out_dw_as = None
                    self.in_dp_rs = None
                    self.out_dp_rs = None
                    self.in_dp_as = None
                    self.out_dp_as = None
                    self.in_ra_rs = None
                    self.out_ra_rs = None
                    self.in_ra_as = None
                    self.out_ra_as = None
                    self.in_st_rs = None
                    self.out_st_rs = None
                    self.in_st_as = None
                    self.out_st_as = None
                    self.in_cc_rs = None
                    self.out_cc_rs = None
                    self.in_cc_as = None
                    self.out_cc_as = None
                    self.out_aa_rs = None
                    self.in_aa_as = None
                    self.malformed_requests = None
                    self.received_proto_errors = None
                    self.sent_proto_errors = None
                    self.received_transient_fails = None
                    self.sent_transient_fails = None
                    self.received_permanent_fails = None
                    self.sent_permanent_fails = None
                    self.transport_down = None
                    self.state = None
                    self._segment_path = lambda: "peer"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/peers/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Peers.Peer, ['peer_name', 'peer_index', 'address', 'port', 'port_connect', 'protocol_type', 'security_type', 'conn_retry_timer', 'watchdog_timer', 'transaction_timer', 'vrf_name', 'source_interface', 'destination_host', 'destination_realm', 'peer_type', 'firmware_revision', 'state_duration', 'last_disconnect_cause', 'who_init_disconnect', 'in_as_rs', 'out_as_rs', 'in_as_as', 'out_as_as', 'in_ac_rs', 'out_ac_rs', 'in_ac_as', 'out_ac_as', 'in_ce_rs', 'out_ce_rs', 'in_ce_as', 'out_ce_as', 'in_dw_rs', 'out_dw_rs', 'in_dw_as', 'out_dw_as', 'in_dp_rs', 'out_dp_rs', 'in_dp_as', 'out_dp_as', 'in_ra_rs', 'out_ra_rs', 'in_ra_as', 'out_ra_as', 'in_st_rs', 'out_st_rs', 'in_st_as', 'out_st_as', 'in_cc_rs', 'out_cc_rs', 'in_cc_as', 'out_cc_as', 'out_aa_rs', 'in_aa_as', 'malformed_requests', 'received_proto_errors', 'sent_proto_errors', 'received_transient_fails', 'sent_transient_fails', 'received_permanent_fails', 'sent_permanent_fails', 'transport_down', 'state'], name, value)


        class Nas(Entity):
            """
            Diameter NAS data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\: str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of  		 :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.Nas, self).__init__()

                self.yang_name = "nas"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("list-of-nas", ("list_of_nas", Aaa.Diameter.Nas.ListOfNas))])
                self._leafs = OrderedDict([
                    ('aaanas_id', (YLeaf(YType.str, 'aaanas-id'), ['str'])),
                ])
                self.aaanas_id = None

                self.list_of_nas = YList(self)
                self._segment_path = lambda: "nas"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.Nas, ['aaanas_id'], name, value)


            class ListOfNas(Entity):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\: str
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\: str
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\: str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\: str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Diameter.Nas.ListOfNas, self).__init__()

                    self.yang_name = "list-of-nas"
                    self.yang_parent_name = "nas"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aaa_session_id', (YLeaf(YType.str, 'aaa-session-id'), ['str'])),
                        ('diameter_session_id', (YLeaf(YType.str, 'diameter-session-id'), ['str'])),
                        ('authentication_status', (YLeaf(YType.uint32, 'authentication-status'), ['int'])),
                        ('authorization_status', (YLeaf(YType.uint32, 'authorization-status'), ['int'])),
                        ('accounting_status', (YLeaf(YType.uint32, 'accounting-status'), ['int'])),
                        ('accounting_status_stop', (YLeaf(YType.uint32, 'accounting-status-stop'), ['int'])),
                        ('disconnect_status', (YLeaf(YType.uint32, 'disconnect-status'), ['int'])),
                        ('accounting_intrim_in_packets', (YLeaf(YType.uint32, 'accounting-intrim-in-packets'), ['int'])),
                        ('accounting_intrim_out_packets', (YLeaf(YType.uint32, 'accounting-intrim-out-packets'), ['int'])),
                        ('method_list', (YLeaf(YType.str, 'method-list'), ['str'])),
                        ('server_used_list', (YLeaf(YType.str, 'server-used-list'), ['str'])),
                    ])
                    self.aaa_session_id = None
                    self.diameter_session_id = None
                    self.authentication_status = None
                    self.authorization_status = None
                    self.accounting_status = None
                    self.accounting_status_stop = None
                    self.disconnect_status = None
                    self.accounting_intrim_in_packets = None
                    self.accounting_intrim_out_packets = None
                    self.method_list = None
                    self.server_used_list = None
                    self._segment_path = lambda: "list-of-nas"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/nas/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.Nas.ListOfNas, ['aaa_session_id', 'diameter_session_id', 'authentication_status', 'authorization_status', 'accounting_status', 'accounting_status_stop', 'disconnect_status', 'accounting_intrim_in_packets', 'accounting_intrim_out_packets', 'method_list', 'server_used_list'], name, value)


        class NasSummary(Entity):
            """
            Diameter NAS summary
            
            .. attribute:: authen_response_in_packets
            
            	Authentication response pkt in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_out_packets
            
            	Authentication request pkt out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_in_packets
            
            	Authentication request from client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_out_packets
            
            	Authentication response frwd to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_success_packets
            
            	Authentication response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_fail_packets
            
            	Authentication response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_in_packets
            
            	Authorization response packet in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_out_packets
            
            	Authorization request packet out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_request_in_packets
            
            	Authourization request from cleint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_out_packets
            
            	Authourization response frwd to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_success_packets
            
            	Authentication response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_fail_packets
            
            	Authentication response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_response_in_packets
            
            	Accounting packet response in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_request_out_packets
            
            	Accounting requests packets out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_request_packets
            
            	Accounting start request from cleint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_response_packets
            
            	Accounting start response forward to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_success_packets
            
            	Accounting start response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_failed_packets
            
            	Accounting start response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_in_packets
            
            	Accounting stop packet response in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_out_packets
            
            	Accounting stop requests packets out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_in_packets
            
            	Acct stop request from cleint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_out_packets
            
            	Acct stop response forward to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_success_response_packets
            
            	Accounting stop response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_failed_packets
            
            	Accounting stop response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_intrim_response_in_packets
            
            	Accounting interim packet response in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_out_packets
            
            	Accounting interim requests packets out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_in_packets
            
            	Accounting Interim request from cleint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_response_out_packets
            
            	Accounting interim response frwd to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_success_packets
            
            	Accounting interim response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_failed_packets
            
            	Accounting interim response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_in_packets
            
            	Disconnect response packets in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_out_packets
            
            	Disconnect request pkt out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_in_packets
            
            	Disconnect request from cleint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_out_packets
            
            	Disconnect response forward to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_success_response_packets
            
            	Disconnect response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_failed_response_packets
            
            	Disconnect response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_in_packets
            
            	COA/RAR Request packet in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_out_packets
            
            	COA/RAR Response packet out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_packets
            
            	COA request from client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_packets
            
            	COA response forward to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_success_packets
            
            	COA response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_failed_packets
            
            	COA response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_in_packets
            
            	POD/RAR Request packets in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_out_packets
            
            	PAD/RAR Response packets out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_request_in_packets
            
            	POD request from cleint
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_response_out_packets
            
            	POD response forward to client
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_success_packets
            
            	POD response with success
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_failed_packets
            
            	POD response with failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.NasSummary, self).__init__()

                self.yang_name = "nas-summary"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('authen_response_in_packets', (YLeaf(YType.uint32, 'authen-response-in-packets'), ['int'])),
                    ('authen_request_out_packets', (YLeaf(YType.uint32, 'authen-request-out-packets'), ['int'])),
                    ('authen_request_in_packets', (YLeaf(YType.uint32, 'authen-request-in-packets'), ['int'])),
                    ('authen_response_out_packets', (YLeaf(YType.uint32, 'authen-response-out-packets'), ['int'])),
                    ('authen_success_packets', (YLeaf(YType.uint32, 'authen-success-packets'), ['int'])),
                    ('authen_response_fail_packets', (YLeaf(YType.uint32, 'authen-response-fail-packets'), ['int'])),
                    ('authorization_in_packets', (YLeaf(YType.uint32, 'authorization-in-packets'), ['int'])),
                    ('authorization_out_packets', (YLeaf(YType.uint32, 'authorization-out-packets'), ['int'])),
                    ('authorization_request_in_packets', (YLeaf(YType.uint32, 'authorization-request-in-packets'), ['int'])),
                    ('authorization_response_out_packets', (YLeaf(YType.uint32, 'authorization-response-out-packets'), ['int'])),
                    ('authorization_response_success_packets', (YLeaf(YType.uint32, 'authorization-response-success-packets'), ['int'])),
                    ('authorization_response_fail_packets', (YLeaf(YType.uint32, 'authorization-response-fail-packets'), ['int'])),
                    ('accounting_response_in_packets', (YLeaf(YType.uint32, 'accounting-response-in-packets'), ['int'])),
                    ('accounting_request_out_packets', (YLeaf(YType.uint32, 'accounting-request-out-packets'), ['int'])),
                    ('accounting_start_request_packets', (YLeaf(YType.uint32, 'accounting-start-request-packets'), ['int'])),
                    ('accounting_start_response_packets', (YLeaf(YType.uint32, 'accounting-start-response-packets'), ['int'])),
                    ('accounting_start_success_packets', (YLeaf(YType.uint32, 'accounting-start-success-packets'), ['int'])),
                    ('accounting_start_failed_packets', (YLeaf(YType.uint32, 'accounting-start-failed-packets'), ['int'])),
                    ('accounting_stop_response_in_packets', (YLeaf(YType.uint32, 'accounting-stop-response-in-packets'), ['int'])),
                    ('accounting_stop_request_out_packets', (YLeaf(YType.uint32, 'accounting-stop-request-out-packets'), ['int'])),
                    ('accounting_stop_request_in_packets', (YLeaf(YType.uint32, 'accounting-stop-request-in-packets'), ['int'])),
                    ('accounting_stop_response_out_packets', (YLeaf(YType.uint32, 'accounting-stop-response-out-packets'), ['int'])),
                    ('accounting_stop_success_response_packets', (YLeaf(YType.uint32, 'accounting-stop-success-response-packets'), ['int'])),
                    ('accounting_stop_failed_packets', (YLeaf(YType.uint32, 'accounting-stop-failed-packets'), ['int'])),
                    ('accounting_intrim_response_in_packets', (YLeaf(YType.uint32, 'accounting-intrim-response-in-packets'), ['int'])),
                    ('accounting_interim_request_out_packets', (YLeaf(YType.uint32, 'accounting-interim-request-out-packets'), ['int'])),
                    ('accounting_interim_request_in_packets', (YLeaf(YType.uint32, 'accounting-interim-request-in-packets'), ['int'])),
                    ('accounting_interim_response_out_packets', (YLeaf(YType.uint32, 'accounting-interim-response-out-packets'), ['int'])),
                    ('accounting_interim_success_packets', (YLeaf(YType.uint32, 'accounting-interim-success-packets'), ['int'])),
                    ('accounting_interim_failed_packets', (YLeaf(YType.uint32, 'accounting-interim-failed-packets'), ['int'])),
                    ('disconnect_response_in_packets', (YLeaf(YType.uint32, 'disconnect-response-in-packets'), ['int'])),
                    ('disconnect_request_out_packets', (YLeaf(YType.uint32, 'disconnect-request-out-packets'), ['int'])),
                    ('disconnect_request_in_packets', (YLeaf(YType.uint32, 'disconnect-request-in-packets'), ['int'])),
                    ('disconnect_response_out_packets', (YLeaf(YType.uint32, 'disconnect-response-out-packets'), ['int'])),
                    ('disconnect_success_response_packets', (YLeaf(YType.uint32, 'disconnect-success-response-packets'), ['int'])),
                    ('disconnect_failed_response_packets', (YLeaf(YType.uint32, 'disconnect-failed-response-packets'), ['int'])),
                    ('coa_request_in_packets', (YLeaf(YType.uint32, 'coa-request-in-packets'), ['int'])),
                    ('coa_response_out_packets', (YLeaf(YType.uint32, 'coa-response-out-packets'), ['int'])),
                    ('coa_request_packets', (YLeaf(YType.uint32, 'coa-request-packets'), ['int'])),
                    ('coa_response_packets', (YLeaf(YType.uint32, 'coa-response-packets'), ['int'])),
                    ('coa_success_packets', (YLeaf(YType.uint32, 'coa-success-packets'), ['int'])),
                    ('coa_failed_packets', (YLeaf(YType.uint32, 'coa-failed-packets'), ['int'])),
                    ('pod_in_packets', (YLeaf(YType.uint32, 'pod-in-packets'), ['int'])),
                    ('pod_out_packets', (YLeaf(YType.uint32, 'pod-out-packets'), ['int'])),
                    ('pod_request_in_packets', (YLeaf(YType.uint32, 'pod-request-in-packets'), ['int'])),
                    ('pod_response_out_packets', (YLeaf(YType.uint32, 'pod-response-out-packets'), ['int'])),
                    ('pod_success_packets', (YLeaf(YType.uint32, 'pod-success-packets'), ['int'])),
                    ('pod_failed_packets', (YLeaf(YType.uint32, 'pod-failed-packets'), ['int'])),
                ])
                self.authen_response_in_packets = None
                self.authen_request_out_packets = None
                self.authen_request_in_packets = None
                self.authen_response_out_packets = None
                self.authen_success_packets = None
                self.authen_response_fail_packets = None
                self.authorization_in_packets = None
                self.authorization_out_packets = None
                self.authorization_request_in_packets = None
                self.authorization_response_out_packets = None
                self.authorization_response_success_packets = None
                self.authorization_response_fail_packets = None
                self.accounting_response_in_packets = None
                self.accounting_request_out_packets = None
                self.accounting_start_request_packets = None
                self.accounting_start_response_packets = None
                self.accounting_start_success_packets = None
                self.accounting_start_failed_packets = None
                self.accounting_stop_response_in_packets = None
                self.accounting_stop_request_out_packets = None
                self.accounting_stop_request_in_packets = None
                self.accounting_stop_response_out_packets = None
                self.accounting_stop_success_response_packets = None
                self.accounting_stop_failed_packets = None
                self.accounting_intrim_response_in_packets = None
                self.accounting_interim_request_out_packets = None
                self.accounting_interim_request_in_packets = None
                self.accounting_interim_response_out_packets = None
                self.accounting_interim_success_packets = None
                self.accounting_interim_failed_packets = None
                self.disconnect_response_in_packets = None
                self.disconnect_request_out_packets = None
                self.disconnect_request_in_packets = None
                self.disconnect_response_out_packets = None
                self.disconnect_success_response_packets = None
                self.disconnect_failed_response_packets = None
                self.coa_request_in_packets = None
                self.coa_response_out_packets = None
                self.coa_request_packets = None
                self.coa_response_packets = None
                self.coa_success_packets = None
                self.coa_failed_packets = None
                self.pod_in_packets = None
                self.pod_out_packets = None
                self.pod_request_in_packets = None
                self.pod_response_out_packets = None
                self.pod_success_packets = None
                self.pod_failed_packets = None
                self._segment_path = lambda: "nas-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.NasSummary, ['authen_response_in_packets', 'authen_request_out_packets', 'authen_request_in_packets', 'authen_response_out_packets', 'authen_success_packets', 'authen_response_fail_packets', 'authorization_in_packets', 'authorization_out_packets', 'authorization_request_in_packets', 'authorization_response_out_packets', 'authorization_response_success_packets', 'authorization_response_fail_packets', 'accounting_response_in_packets', 'accounting_request_out_packets', 'accounting_start_request_packets', 'accounting_start_response_packets', 'accounting_start_success_packets', 'accounting_start_failed_packets', 'accounting_stop_response_in_packets', 'accounting_stop_request_out_packets', 'accounting_stop_request_in_packets', 'accounting_stop_response_out_packets', 'accounting_stop_success_response_packets', 'accounting_stop_failed_packets', 'accounting_intrim_response_in_packets', 'accounting_interim_request_out_packets', 'accounting_interim_request_in_packets', 'accounting_interim_response_out_packets', 'accounting_interim_success_packets', 'accounting_interim_failed_packets', 'disconnect_response_in_packets', 'disconnect_request_out_packets', 'disconnect_request_in_packets', 'disconnect_response_out_packets', 'disconnect_success_response_packets', 'disconnect_failed_response_packets', 'coa_request_in_packets', 'coa_response_out_packets', 'coa_request_packets', 'coa_response_packets', 'coa_success_packets', 'coa_failed_packets', 'pod_in_packets', 'pod_out_packets', 'pod_request_in_packets', 'pod_response_out_packets', 'pod_success_packets', 'pod_failed_packets'], name, value)


        class GySessionIds(Entity):
            """
            Diameter Gy Session data list
            
            .. attribute:: gy_session_id
            
            	Diameter Gy Session data
            	**type**\: list of  		 :py:class:`GySessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds.GySessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.GySessionIds, self).__init__()

                self.yang_name = "gy-session-ids"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("gy-session-id", ("gy_session_id", Aaa.Diameter.GySessionIds.GySessionId))])
                self._leafs = OrderedDict()

                self.gy_session_id = YList(self)
                self._segment_path = lambda: "gy-session-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GySessionIds, [], name, value)


            class GySessionId(Entity):
                """
                Diameter Gy Session data
                
                .. attribute:: session_id  (key)
                
                	Session Id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: parent_aaa_session_id
                
                	AAA Parent session id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\: str
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\: str
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\: str
                
                .. attribute:: retry_count
                
                	Gy Retry count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Diameter.GySessionIds.GySessionId, self).__init__()

                    self.yang_name = "gy-session-id"
                    self.yang_parent_name = "gy-session-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['session_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                        ('aaa_session_id', (YLeaf(YType.uint32, 'aaa-session-id'), ['int'])),
                        ('parent_aaa_session_id', (YLeaf(YType.uint32, 'parent-aaa-session-id'), ['int'])),
                        ('diameter_session_id', (YLeaf(YType.str, 'diameter-session-id'), ['str'])),
                        ('request_number', (YLeaf(YType.uint32, 'request-number'), ['int'])),
                        ('session_state', (YLeaf(YType.str, 'session-state'), ['str'])),
                        ('request_type', (YLeaf(YType.str, 'request-type'), ['str'])),
                        ('retry_count', (YLeaf(YType.uint32, 'retry-count'), ['int'])),
                    ])
                    self.session_id = None
                    self.aaa_session_id = None
                    self.parent_aaa_session_id = None
                    self.diameter_session_id = None
                    self.request_number = None
                    self.session_state = None
                    self.request_type = None
                    self.retry_count = None
                    self._segment_path = lambda: "gy-session-id" + "[session-id='" + str(self.session_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/gy-session-ids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.GySessionIds.GySessionId, ['session_id', 'aaa_session_id', 'parent_aaa_session_id', 'diameter_session_id', 'request_number', 'session_state', 'request_type', 'retry_count'], name, value)


        class GyStatistics(Entity):
            """
            Diameter Gy Statistics data
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messages
            
            	ASA Sent Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.GyStatistics, self).__init__()

                self.yang_name = "gy-statistics"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccr_init_messages', (YLeaf(YType.uint32, 'ccr-init-messages'), ['int'])),
                    ('ccr_init_failed_messages', (YLeaf(YType.uint32, 'ccr-init-failed-messages'), ['int'])),
                    ('ccr_init_timed_out_messages', (YLeaf(YType.uint32, 'ccr-init-timed-out-messages'), ['int'])),
                    ('ccr_init_retry_messages', (YLeaf(YType.uint32, 'ccr-init-retry-messages'), ['int'])),
                    ('ccr_update_messages', (YLeaf(YType.uint32, 'ccr-update-messages'), ['int'])),
                    ('ccr_update_failed_messages', (YLeaf(YType.uint32, 'ccr-update-failed-messages'), ['int'])),
                    ('ccr_update_timed_out_messages', (YLeaf(YType.uint32, 'ccr-update-timed-out-messages'), ['int'])),
                    ('ccr_update_retry_messages', (YLeaf(YType.uint32, 'ccr-update-retry-messages'), ['int'])),
                    ('ccr_final_messages', (YLeaf(YType.uint32, 'ccr-final-messages'), ['int'])),
                    ('ccr_final_failed_messages', (YLeaf(YType.uint32, 'ccr-final-failed-messages'), ['int'])),
                    ('ccr_final_timed_out_messages', (YLeaf(YType.uint32, 'ccr-final-timed-out-messages'), ['int'])),
                    ('ccr_final_retry_messages', (YLeaf(YType.uint32, 'ccr-final-retry-messages'), ['int'])),
                    ('cca_init_messages', (YLeaf(YType.uint32, 'cca-init-messages'), ['int'])),
                    ('cca_init_error_messages', (YLeaf(YType.uint32, 'cca-init-error-messages'), ['int'])),
                    ('cca_update_messages', (YLeaf(YType.uint32, 'cca-update-messages'), ['int'])),
                    ('cca_update_error_messages', (YLeaf(YType.uint32, 'cca-update-error-messages'), ['int'])),
                    ('cca_final_messages', (YLeaf(YType.uint32, 'cca-final-messages'), ['int'])),
                    ('cca_final_error_messages', (YLeaf(YType.uint32, 'cca-final-error-messages'), ['int'])),
                    ('rar_received_messages', (YLeaf(YType.uint32, 'rar-received-messages'), ['int'])),
                    ('rar_received_error_messages', (YLeaf(YType.uint32, 'rar-received-error-messages'), ['int'])),
                    ('raa_sent_messages', (YLeaf(YType.uint32, 'raa-sent-messages'), ['int'])),
                    ('raa_sent_error_messages', (YLeaf(YType.uint32, 'raa-sent-error-messages'), ['int'])),
                    ('asr_received_messages', (YLeaf(YType.uint32, 'asr-received-messages'), ['int'])),
                    ('asr_received_error_messages', (YLeaf(YType.uint32, 'asr-received-error-messages'), ['int'])),
                    ('asa_sent_messages', (YLeaf(YType.uint32, 'asa-sent-messages'), ['int'])),
                    ('asa_sent_error_messages', (YLeaf(YType.uint32, 'asa-sent-error-messages'), ['int'])),
                    ('unknown_request_messages', (YLeaf(YType.uint32, 'unknown-request-messages'), ['int'])),
                    ('restore_sessions', (YLeaf(YType.uint32, 'restore-sessions'), ['int'])),
                    ('open_sessions', (YLeaf(YType.uint32, 'open-sessions'), ['int'])),
                    ('close_sessions', (YLeaf(YType.uint32, 'close-sessions'), ['int'])),
                    ('active_sessions', (YLeaf(YType.uint32, 'active-sessions'), ['int'])),
                ])
                self.ccr_init_messages = None
                self.ccr_init_failed_messages = None
                self.ccr_init_timed_out_messages = None
                self.ccr_init_retry_messages = None
                self.ccr_update_messages = None
                self.ccr_update_failed_messages = None
                self.ccr_update_timed_out_messages = None
                self.ccr_update_retry_messages = None
                self.ccr_final_messages = None
                self.ccr_final_failed_messages = None
                self.ccr_final_timed_out_messages = None
                self.ccr_final_retry_messages = None
                self.cca_init_messages = None
                self.cca_init_error_messages = None
                self.cca_update_messages = None
                self.cca_update_error_messages = None
                self.cca_final_messages = None
                self.cca_final_error_messages = None
                self.rar_received_messages = None
                self.rar_received_error_messages = None
                self.raa_sent_messages = None
                self.raa_sent_error_messages = None
                self.asr_received_messages = None
                self.asr_received_error_messages = None
                self.asa_sent_messages = None
                self.asa_sent_error_messages = None
                self.unknown_request_messages = None
                self.restore_sessions = None
                self.open_sessions = None
                self.close_sessions = None
                self.active_sessions = None
                self._segment_path = lambda: "gy-statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GyStatistics, ['ccr_init_messages', 'ccr_init_failed_messages', 'ccr_init_timed_out_messages', 'ccr_init_retry_messages', 'ccr_update_messages', 'ccr_update_failed_messages', 'ccr_update_timed_out_messages', 'ccr_update_retry_messages', 'ccr_final_messages', 'ccr_final_failed_messages', 'ccr_final_timed_out_messages', 'ccr_final_retry_messages', 'cca_init_messages', 'cca_init_error_messages', 'cca_update_messages', 'cca_update_error_messages', 'cca_final_messages', 'cca_final_error_messages', 'rar_received_messages', 'rar_received_error_messages', 'raa_sent_messages', 'raa_sent_error_messages', 'asr_received_messages', 'asr_received_error_messages', 'asa_sent_messages', 'asa_sent_error_messages', 'unknown_request_messages', 'restore_sessions', 'open_sessions', 'close_sessions', 'active_sessions'], name, value)


        class GxSessionIds(Entity):
            """
            Diameter Gx Session data list
            
            .. attribute:: gx_session_id
            
            	Diameter Gx Session data
            	**type**\: list of  		 :py:class:`GxSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds.GxSessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.GxSessionIds, self).__init__()

                self.yang_name = "gx-session-ids"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("gx-session-id", ("gx_session_id", Aaa.Diameter.GxSessionIds.GxSessionId))])
                self._leafs = OrderedDict()

                self.gx_session_id = YList(self)
                self._segment_path = lambda: "gx-session-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.GxSessionIds, [], name, value)


            class GxSessionId(Entity):
                """
                Diameter Gx Session data
                
                .. attribute:: session_id  (key)
                
                	Session Id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\: str
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\: str
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\: str
                
                .. attribute:: retry_count
                
                	Gx Retry count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: service_count
                
                	 Gx Plus Service Count
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: gx_plus_services
                
                	Gx Plus Services
                	**type**\: str
                
                .. attribute:: reavalidation_time
                
                	Revalidation Time
                	**type**\: str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Diameter.GxSessionIds.GxSessionId, self).__init__()

                    self.yang_name = "gx-session-id"
                    self.yang_parent_name = "gx-session-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['session_id']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                        ('aaa_session_id', (YLeaf(YType.uint32, 'aaa-session-id'), ['int'])),
                        ('diameter_session_id', (YLeaf(YType.str, 'diameter-session-id'), ['str'])),
                        ('request_number', (YLeaf(YType.uint32, 'request-number'), ['int'])),
                        ('session_state', (YLeaf(YType.str, 'session-state'), ['str'])),
                        ('request_type', (YLeaf(YType.str, 'request-type'), ['str'])),
                        ('retry_count', (YLeaf(YType.uint32, 'retry-count'), ['int'])),
                        ('service_count', (YLeaf(YType.uint32, 'service-count'), ['int'])),
                        ('gx_plus_services', (YLeaf(YType.str, 'gx-plus-services'), ['str'])),
                        ('reavalidation_time', (YLeaf(YType.str, 'reavalidation-time'), ['str'])),
                    ])
                    self.session_id = None
                    self.aaa_session_id = None
                    self.diameter_session_id = None
                    self.request_number = None
                    self.session_state = None
                    self.request_type = None
                    self.retry_count = None
                    self.service_count = None
                    self.gx_plus_services = None
                    self.reavalidation_time = None
                    self._segment_path = lambda: "gx-session-id" + "[session-id='" + str(self.session_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/gx-session-ids/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.GxSessionIds.GxSessionId, ['session_id', 'aaa_session_id', 'diameter_session_id', 'request_number', 'session_state', 'request_type', 'retry_count', 'service_count', 'gx_plus_services', 'reavalidation_time'], name, value)


        class NasSession(Entity):
            """
            Diameter Nas Session data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\: str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of  		 :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(Aaa.Diameter.NasSession, self).__init__()

                self.yang_name = "nas-session"
                self.yang_parent_name = "diameter"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("list-of-nas", ("list_of_nas", Aaa.Diameter.NasSession.ListOfNas))])
                self._leafs = OrderedDict([
                    ('aaanas_id', (YLeaf(YType.str, 'aaanas-id'), ['str'])),
                ])
                self.aaanas_id = None

                self.list_of_nas = YList(self)
                self._segment_path = lambda: "nas-session"
                self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Aaa.Diameter.NasSession, ['aaanas_id'], name, value)


            class ListOfNas(Entity):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\: str
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\: str
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\: str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\: str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(Aaa.Diameter.NasSession.ListOfNas, self).__init__()

                    self.yang_name = "list-of-nas"
                    self.yang_parent_name = "nas-session"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('aaa_session_id', (YLeaf(YType.str, 'aaa-session-id'), ['str'])),
                        ('diameter_session_id', (YLeaf(YType.str, 'diameter-session-id'), ['str'])),
                        ('authentication_status', (YLeaf(YType.uint32, 'authentication-status'), ['int'])),
                        ('authorization_status', (YLeaf(YType.uint32, 'authorization-status'), ['int'])),
                        ('accounting_status', (YLeaf(YType.uint32, 'accounting-status'), ['int'])),
                        ('accounting_status_stop', (YLeaf(YType.uint32, 'accounting-status-stop'), ['int'])),
                        ('disconnect_status', (YLeaf(YType.uint32, 'disconnect-status'), ['int'])),
                        ('accounting_intrim_in_packets', (YLeaf(YType.uint32, 'accounting-intrim-in-packets'), ['int'])),
                        ('accounting_intrim_out_packets', (YLeaf(YType.uint32, 'accounting-intrim-out-packets'), ['int'])),
                        ('method_list', (YLeaf(YType.str, 'method-list'), ['str'])),
                        ('server_used_list', (YLeaf(YType.str, 'server-used-list'), ['str'])),
                    ])
                    self.aaa_session_id = None
                    self.diameter_session_id = None
                    self.authentication_status = None
                    self.authorization_status = None
                    self.accounting_status = None
                    self.accounting_status_stop = None
                    self.disconnect_status = None
                    self.accounting_intrim_in_packets = None
                    self.accounting_intrim_out_packets = None
                    self.method_list = None
                    self.server_used_list = None
                    self._segment_path = lambda: "list-of-nas"
                    self._absolute_path = lambda: "Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/nas-session/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Aaa.Diameter.NasSession.ListOfNas, ['aaa_session_id', 'diameter_session_id', 'authentication_status', 'authorization_status', 'accounting_status', 'accounting_status_stop', 'disconnect_status', 'accounting_intrim_in_packets', 'accounting_intrim_out_packets', 'method_list', 'server_used_list'], name, value)

    def clone_ptr(self):
        self._top_entity = Aaa()
        return self._top_entity

