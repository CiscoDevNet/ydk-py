""" Cisco_IOS_XR_aaa_locald_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package operational data.

This module contains definitions
for the following management objects\:
  aaa\: AAA operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Aaa(object):
    """
    AAA operational data
    
    .. attribute:: all_tasks
    
    	All tasks supported by system
    	**type**\: :py:class:`AllTasks <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.AllTasks>`
    
    .. attribute:: currentuser_detail
    
    	Current user specific details
    	**type**\: :py:class:`CurrentuserDetail <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentuserDetail>`
    
    .. attribute:: task_map
    
    	Task map of current user
    	**type**\: :py:class:`TaskMap <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.TaskMap>`
    
    .. attribute:: taskgroups
    
    	Individual taskgroups container
    	**type**\: :py:class:`Taskgroups <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups>`
    
    .. attribute:: users
    
    	Container for individual local user information
    	**type**\: :py:class:`Users <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users>`
    
    .. attribute:: usergroups
    
    	Container for individual usergroup Information
    	**type**\: :py:class:`Usergroups <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups>`
    
    .. attribute:: authen_method
    
    	Current users authentication method
    	**type**\: :py:class:`AuthenMethod <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.AuthenMethod>`
    
    .. attribute:: current_usergroup
    
    	Specific Usergroup Information
    	**type**\: :py:class:`CurrentUsergroup <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentUsergroup>`
    
    .. attribute:: radius
    
    	RADIUS operational data
    	**type**\: :py:class:`Radius <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius>`
    
    

    """

    _prefix = 'aaa-locald-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.all_tasks = Aaa.AllTasks()
        self.all_tasks.parent = self
        self.currentuser_detail = Aaa.CurrentuserDetail()
        self.currentuser_detail.parent = self
        self.task_map = Aaa.TaskMap()
        self.task_map.parent = self
        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self.users = Aaa.Users()
        self.users.parent = self
        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self.authen_method = Aaa.AuthenMethod()
        self.authen_method.parent = self
        self.current_usergroup = Aaa.CurrentUsergroup()
        self.current_usergroup.parent = self
        self.radius = Aaa.Radius()
        self.radius.parent = self


    class AllTasks(object):
        """
        All tasks supported by system
        
        .. attribute:: task_id
        
        	Names of available task\-ids
        	**type**\: list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.task_id = YLeafList()
            self.task_id.parent = self
            self.task_id.name = 'task_id'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:all-tasks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.task_id is not None:
                for child in self.task_id:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.AllTasks']['meta_info']


    class CurrentuserDetail(object):
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
            self.parent = None
            self.name = None
            self.authenmethod = None
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:currentuser-detail'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.authenmethod is not None:
                return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.CurrentuserDetail']['meta_info']


    class TaskMap(object):
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
            self.parent = None
            self.name = None
            self.authenmethod = None
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:task-map'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.authenmethod is not None:
                return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.TaskMap']['meta_info']


    class Taskgroups(object):
        """
        Individual taskgroups container
        
        .. attribute:: taskgroup
        
        	Specific Taskgroup Information
        	**type**\: list of :py:class:`Taskgroup <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.taskgroup = YList()
            self.taskgroup.parent = self
            self.taskgroup.name = 'taskgroup'


        class Taskgroup(object):
            """
            Specific Taskgroup Information
            
            .. attribute:: name  <key>
            
            	Taskgroup name
            	**type**\: str
            
            .. attribute:: included_task_ids
            
            	Task\-ids included
            	**type**\: :py:class:`IncludedTaskIds <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds>`
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\: :py:class:`TaskMap <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap>`
            
            .. attribute:: name_xr
            
            	Name of the taskgroup
            	**type**\: str
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.included_task_ids = Aaa.Taskgroups.Taskgroup.IncludedTaskIds()
                self.included_task_ids.parent = self
                self.task_map = Aaa.Taskgroups.Taskgroup.TaskMap()
                self.task_map.parent = self
                self.name_xr = None


            class IncludedTaskIds(object):
                """
                Task\-ids included
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of :py:class:`Tasks <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tasks = YList()
                    self.tasks.parent = self
                    self.tasks.name = 'tasks'


                class Tasks(object):
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
                        self.parent = None
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.task_id is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.write is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.debug is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:included-task-ids'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tasks is not None:
                        for child_ref in self.tasks:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds']['meta_info']


            class TaskMap(object):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of :py:class:`Tasks <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tasks = YList()
                    self.tasks.parent = self
                    self.tasks.name = 'tasks'


                class Tasks(object):
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
                        self.parent = None
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.task_id is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.write is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.debug is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Taskgroups.Taskgroup.TaskMap.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:task-map'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tasks is not None:
                        for child_ref in self.tasks:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Taskgroups.Taskgroup.TaskMap']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:taskgroups/Cisco-IOS-XR-aaa-locald-oper:taskgroup[Cisco-IOS-XR-aaa-locald-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.included_task_ids is not None and self.included_task_ids._has_data():
                    return True

                if self.task_map is not None and self.task_map._has_data():
                    return True

                if self.name_xr is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:taskgroups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.taskgroup is not None:
                for child_ref in self.taskgroup:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Taskgroups']['meta_info']


    class Users(object):
        """
        Container for individual local user information
        
        .. attribute:: user
        
        	Specific local user information
        	**type**\: list of :py:class:`User <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.user = YList()
            self.user.parent = self
            self.user.name = 'user'


        class User(object):
            """
            Specific local user information
            
            .. attribute:: name  <key>
            
            	Username
            	**type**\: str
            
            .. attribute:: task_map
            
            	Computed taskmap
            	**type**\: :py:class:`TaskMap <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap>`
            
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
                self.parent = None
                self.name = None
                self.task_map = Aaa.Users.User.TaskMap()
                self.task_map.parent = self
                self.name_xr = None
                self.admin_user = None
                self.first_user = None
                self.usergroup = YLeafList()
                self.usergroup.parent = self
                self.usergroup.name = 'usergroup'


            class TaskMap(object):
                """
                Computed taskmap
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of :py:class:`Tasks <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tasks = YList()
                    self.tasks.parent = self
                    self.tasks.name = 'tasks'


                class Tasks(object):
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
                        self.parent = None
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.task_id is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.write is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.debug is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Users.User.TaskMap.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:task-map'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tasks is not None:
                        for child_ref in self.tasks:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Users.User.TaskMap']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:users/Cisco-IOS-XR-aaa-locald-oper:user[Cisco-IOS-XR-aaa-locald-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.task_map is not None and self.task_map._has_data():
                    return True

                if self.name_xr is not None:
                    return True

                if self.admin_user is not None:
                    return True

                if self.first_user is not None:
                    return True

                if self.usergroup is not None:
                    for child in self.usergroup:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Users.User']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:users'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.user is not None:
                for child_ref in self.user:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Users']['meta_info']


    class Usergroups(object):
        """
        Container for individual usergroup Information
        
        .. attribute:: usergroup
        
        	Specific Usergroup Information
        	**type**\: list of :py:class:`Usergroup <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup>`
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.usergroup = YList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'


        class Usergroup(object):
            """
            Specific Usergroup Information
            
            .. attribute:: name  <key>
            
            	Usergroup name
            	**type**\: str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\: :py:class:`TaskMap <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap>`
            
            .. attribute:: name_xr
            
            	Name of the usergroup
            	**type**\: str
            
            .. attribute:: taskgroup
            
            	Component taskgroups
            	**type**\: list of :py:class:`Taskgroup <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.task_map = Aaa.Usergroups.Usergroup.TaskMap()
                self.task_map.parent = self
                self.name_xr = None
                self.taskgroup = YList()
                self.taskgroup.parent = self
                self.taskgroup.name = 'taskgroup'


            class TaskMap(object):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of :py:class:`Tasks <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap.Tasks>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tasks = YList()
                    self.tasks.parent = self
                    self.tasks.name = 'tasks'


                class Tasks(object):
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
                        self.parent = None
                        self.task_id = None
                        self.read = None
                        self.write = None
                        self.execute = None
                        self.debug = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.task_id is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.write is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.debug is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.TaskMap.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:task-map'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tasks is not None:
                        for child_ref in self.tasks:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Usergroups.Usergroup.TaskMap']['meta_info']


            class Taskgroup(object):
                """
                Component taskgroups
                
                .. attribute:: included_task_ids
                
                	Task\-ids included
                	**type**\: :py:class:`IncludedTaskIds <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds>`
                
                .. attribute:: task_map
                
                	Computed task map
                	**type**\: :py:class:`TaskMap <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap>`
                
                .. attribute:: name_xr
                
                	Name of the taskgroup
                	**type**\: str
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.included_task_ids = Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds()
                    self.included_task_ids.parent = self
                    self.task_map = Aaa.Usergroups.Usergroup.Taskgroup.TaskMap()
                    self.task_map.parent = self
                    self.name_xr = None


                class IncludedTaskIds(object):
                    """
                    Task\-ids included
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of :py:class:`Tasks <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.tasks = YList()
                        self.tasks.parent = self
                        self.tasks.name = 'tasks'


                    class Tasks(object):
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
                            self.parent = None
                            self.task_id = None
                            self.read = None
                            self.write = None
                            self.execute = None
                            self.debug = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.task_id is not None:
                                return True

                            if self.read is not None:
                                return True

                            if self.write is not None:
                                return True

                            if self.execute is not None:
                                return True

                            if self.debug is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                            return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:included-task-ids'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tasks is not None:
                            for child_ref in self.tasks:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds']['meta_info']


                class TaskMap(object):
                    """
                    Computed task map
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of :py:class:`Tasks <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks>`
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.tasks = YList()
                        self.tasks.parent = self
                        self.tasks.name = 'tasks'


                    class Tasks(object):
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
                            self.parent = None
                            self.task_id = None
                            self.read = None
                            self.write = None
                            self.execute = None
                            self.debug = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.task_id is not None:
                                return True

                            if self.read is not None:
                                return True

                            if self.write is not None:
                                return True

                            if self.execute is not None:
                                return True

                            if self.debug is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                            return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:task-map'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tasks is not None:
                            for child_ref in self.tasks:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:taskgroup'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.included_task_ids is not None and self.included_task_ids._has_data():
                        return True

                    if self.task_map is not None and self.task_map._has_data():
                        return True

                    if self.name_xr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYDataValidationError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:usergroups/Cisco-IOS-XR-aaa-locald-oper:usergroup[Cisco-IOS-XR-aaa-locald-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.task_map is not None and self.task_map._has_data():
                    return True

                if self.name_xr is not None:
                    return True

                if self.taskgroup is not None:
                    for child_ref in self.taskgroup:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Usergroups.Usergroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:usergroups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.usergroup is not None:
                for child_ref in self.usergroup:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Usergroups']['meta_info']


    class AuthenMethod(object):
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
            self.parent = None
            self.name = None
            self.authenmethod = None
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:authen-method'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.authenmethod is not None:
                return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.AuthenMethod']['meta_info']


    class CurrentUsergroup(object):
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
            self.parent = None
            self.name = None
            self.authenmethod = None
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:current-usergroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.name is not None:
                return True

            if self.authenmethod is not None:
                return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.CurrentUsergroup']['meta_info']


    class Radius(object):
        """
        RADIUS operational data
        
        .. attribute:: servers
        
        	List of RADIUS servers configured
        	**type**\: :py:class:`Servers <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers>`
        
        .. attribute:: global_
        
        	RADIUS Client Information
        	**type**\: :py:class:`Global <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Global>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.servers = Aaa.Radius.Servers()
            self.servers.parent = self
            self.global_ = Aaa.Radius.Global()
            self.global_.parent = self


        class Servers(object):
            """
            List of RADIUS servers configured
            
            .. attribute:: server
            
            	RADIUS Server
            	**type**\: list of :py:class:`Server <ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers.Server>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.server = YList()
                self.server.parent = self
                self.server.name = 'server'


            class Server(object):
                """
                RADIUS Server
                
                .. attribute:: ip_address
                
                	IP address of RADIUS server
                	**type**\: one of the below types:
                
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
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
                
                .. attribute:: retransmit
                
                	Per\-server retransmit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_time
                
                	Per\-server deadtime in minutes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_detect_time
                
                	Per\-server dead\-detect time in seconds
                	**type**\: int
                
                	**range:** 0..4294967295
                
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
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
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

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:servers/Cisco-IOS-XR-aaa-protocol-radius-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ip_address is not None:
                        return True

                    if self.auth_port_number is not None:
                        return True

                    if self.acct_port_number is not None:
                        return True

                    if self.ipv4_address is not None:
                        return True

                    if self.priority is not None:
                        return True

                    if self.timeout_xr is not None:
                        return True

                    if self.retransmit is not None:
                        return True

                    if self.dead_time is not None:
                        return True

                    if self.dead_detect_time is not None:
                        return True

                    if self.dead_detect_tries is not None:
                        return True

                    if self.authentication_port is not None:
                        return True

                    if self.accounting_port is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.current_state_duration is not None:
                        return True

                    if self.previous_state_duration is not None:
                        return True

                    if self.packets_in is not None:
                        return True

                    if self.packets_out is not None:
                        return True

                    if self.timeouts is not None:
                        return True

                    if self.aborts is not None:
                        return True

                    if self.replies_expected is not None:
                        return True

                    if self.redirected_requests is not None:
                        return True

                    if self.authentication_rtt is not None:
                        return True

                    if self.access_requests is not None:
                        return True

                    if self.access_request_retransmits is not None:
                        return True

                    if self.access_accepts is not None:
                        return True

                    if self.access_rejects is not None:
                        return True

                    if self.access_challenges is not None:
                        return True

                    if self.bad_access_responses is not None:
                        return True

                    if self.bad_access_authenticators is not None:
                        return True

                    if self.pending_access_requests is not None:
                        return True

                    if self.access_timeouts is not None:
                        return True

                    if self.unknown_access_types is not None:
                        return True

                    if self.dropped_access_responses is not None:
                        return True

                    if self.throttled_access_reqs is not None:
                        return True

                    if self.throttled_timed_out_reqs is not None:
                        return True

                    if self.throttled_dropped_reqs is not None:
                        return True

                    if self.max_throttled_access_reqs is not None:
                        return True

                    if self.currently_throttled_access_reqs is not None:
                        return True

                    if self.authen_response_time is not None:
                        return True

                    if self.authen_transaction_successess is not None:
                        return True

                    if self.authen_transaction_failure is not None:
                        return True

                    if self.authen_unexpected_responses is not None:
                        return True

                    if self.authen_server_error_responses is not None:
                        return True

                    if self.authen_incorrect_responses is not None:
                        return True

                    if self.author_requests is not None:
                        return True

                    if self.author_request_timeouts is not None:
                        return True

                    if self.author_response_time is not None:
                        return True

                    if self.author_transaction_successess is not None:
                        return True

                    if self.author_transaction_failure is not None:
                        return True

                    if self.author_unexpected_responses is not None:
                        return True

                    if self.author_server_error_responses is not None:
                        return True

                    if self.author_incorrect_responses is not None:
                        return True

                    if self.accounting_rtt is not None:
                        return True

                    if self.accounting_requests is not None:
                        return True

                    if self.accounting_retransmits is not None:
                        return True

                    if self.accounting_responses is not None:
                        return True

                    if self.bad_accounting_responses is not None:
                        return True

                    if self.bad_accounting_authenticators is not None:
                        return True

                    if self.pending_accounting_requets is not None:
                        return True

                    if self.accounting_timeouts is not None:
                        return True

                    if self.unknown_accounting_types is not None:
                        return True

                    if self.dropped_accounting_responses is not None:
                        return True

                    if self.is_a_private_server is not None:
                        return True

                    if self.total_test_auth_reqs is not None:
                        return True

                    if self.total_test_auth_timeouts is not None:
                        return True

                    if self.total_test_auth_response is not None:
                        return True

                    if self.total_test_auth_pending is not None:
                        return True

                    if self.total_test_acct_reqs is not None:
                        return True

                    if self.total_test_acct_timeouts is not None:
                        return True

                    if self.total_test_acct_response is not None:
                        return True

                    if self.total_test_acct_pending is not None:
                        return True

                    if self.throttled_acct_transactions is not None:
                        return True

                    if self.throttled_acct_timed_out_stats is not None:
                        return True

                    if self.throttled_acct_failures_stats is not None:
                        return True

                    if self.max_acct_throttled is not None:
                        return True

                    if self.throttleda_acct_transactions is not None:
                        return True

                    if self.acct_unexpected_responses is not None:
                        return True

                    if self.acct_server_error_responses is not None:
                        return True

                    if self.acct_incorrect_responses is not None:
                        return True

                    if self.acct_response_time is not None:
                        return True

                    if self.acct_transaction_successess is not None:
                        return True

                    if self.acct_transaction_failure is not None:
                        return True

                    if self.total_deadtime is not None:
                        return True

                    if self.last_deadtime is not None:
                        return True

                    if self.is_quarantined is not None:
                        return True

                    if self.group_name is not None:
                        return True

                    if self.ip_address_xr is not None:
                        return True

                    if self.family is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Radius.Servers.Server']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:servers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.server is not None:
                    for child_ref in self.server:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Radius.Servers']['meta_info']


        class Global(object):
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
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.unknown_authentication_response = None
                self.authentication_nas_id = None
                self.unknown_accounting_response = None
                self.accounting_nas_id = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:global'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.unknown_authentication_response is not None:
                    return True

                if self.authentication_nas_id is not None:
                    return True

                if self.unknown_accounting_response is not None:
                    return True

                if self.accounting_nas_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Radius.Global']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.servers is not None and self.servers._has_data():
                return True

            if self.global_ is not None and self.global_._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Radius']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-aaa-locald-oper:aaa'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.all_tasks is not None and self.all_tasks._has_data():
            return True

        if self.currentuser_detail is not None and self.currentuser_detail._has_data():
            return True

        if self.task_map is not None and self.task_map._has_data():
            return True

        if self.taskgroups is not None and self.taskgroups._has_data():
            return True

        if self.users is not None and self.users._has_data():
            return True

        if self.usergroups is not None and self.usergroups._has_data():
            return True

        if self.authen_method is not None and self.authen_method._has_data():
            return True

        if self.current_usergroup is not None and self.current_usergroup._has_data():
            return True

        if self.radius is not None and self.radius._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.aaa._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
        return meta._meta_table['Aaa']['meta_info']


