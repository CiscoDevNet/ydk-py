""" Cisco_IOS_XR_aaa_locald_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-locald package operational data.

This module contains definitions
for the following management objects\:
  aaa\: AAA operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Aaa(object):
    """
    AAA operational data
    
    .. attribute:: all_tasks
    
    	All tasks supported by system
    	**type**\:  :py:class:`AllTasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AllTasks>`
    
    .. attribute:: authen_method
    
    	Current users authentication method
    	**type**\:  :py:class:`AuthenMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AuthenMethod>`
    
    .. attribute:: current_usergroup
    
    	Specific Usergroup Information
    	**type**\:  :py:class:`CurrentUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentUsergroup>`
    
    .. attribute:: currentuser_detail
    
    	Current user specific details
    	**type**\:  :py:class:`CurrentuserDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentuserDetail>`
    
    .. attribute:: radius
    
    	RADIUS operational data
    	**type**\:  :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius>`
    
    .. attribute:: tacacs
    
    	TACACS operational data
    	**type**\:  :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs>`
    
    .. attribute:: task_map
    
    	Task map of current user
    	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.TaskMap>`
    
    .. attribute:: taskgroups
    
    	Individual taskgroups container
    	**type**\:  :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Container for individual usergroup Information
    	**type**\:  :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups>`
    
    .. attribute:: users
    
    	Container for individual local user information
    	**type**\:  :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users>`
    
    

    """

    _prefix = 'aaa-locald-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.all_tasks = Aaa.AllTasks()
        self.all_tasks.parent = self
        self.authen_method = Aaa.AuthenMethod()
        self.authen_method.parent = self
        self.current_usergroup = Aaa.CurrentUsergroup()
        self.current_usergroup.parent = self
        self.currentuser_detail = Aaa.CurrentuserDetail()
        self.currentuser_detail.parent = self
        self.radius = Aaa.Radius()
        self.radius.parent = self
        self.tacacs = Aaa.Tacacs()
        self.tacacs.parent = self
        self.task_map = Aaa.TaskMap()
        self.task_map.parent = self
        self.taskgroups = Aaa.Taskgroups()
        self.taskgroups.parent = self
        self.usergroups = Aaa.Usergroups()
        self.usergroups.parent = self
        self.users = Aaa.Users()
        self.users.parent = self


    class AllTasks(object):
        """
        All tasks supported by system
        
        .. attribute:: task_id
        
        	Names of available task\-ids
        	**type**\:  list of str
        
        

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.AllTasks']['meta_info']


    class CurrentuserDetail(object):
        """
        Current user specific details
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.authenmethod = None
            self.name = None
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:currentuser-detail'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.authenmethod is not None:
                return True

            if self.name is not None:
                return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.CurrentuserDetail']['meta_info']


    class TaskMap(object):
        """
        Task map of current user
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.authenmethod = None
            self.name = None
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:task-map'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.authenmethod is not None:
                return True

            if self.name is not None:
                return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.TaskMap']['meta_info']


    class Taskgroups(object):
        """
        Individual taskgroups container
        
        .. attribute:: taskgroup
        
        	Specific Taskgroup Information
        	**type**\: list of  :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup>`
        
        

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
            	**type**\:  str
            
            .. attribute:: included_task_ids
            
            	Task\-ids included
            	**type**\:  :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds>`
            
            .. attribute:: name_xr
            
            	Name of the taskgroup
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.included_task_ids = Aaa.Taskgroups.Taskgroup.IncludedTaskIds()
                self.included_task_ids.parent = self
                self.name_xr = None
                self.task_map = Aaa.Taskgroups.Taskgroup.TaskMap()
                self.task_map.parent = self


            class IncludedTaskIds(object):
                """
                Task\-ids included
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks>`
                
                

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
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.debug = None
                        self.execute = None
                        self.read = None
                        self.task_id = None
                        self.write = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.debug is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.task_id is not None:
                            return True

                        if self.write is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds']['meta_info']


            class TaskMap(object):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap.Tasks>`
                
                

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
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.debug = None
                        self.execute = None
                        self.read = None
                        self.task_id = None
                        self.write = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.debug is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.task_id is not None:
                            return True

                        if self.write is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Taskgroups.Taskgroup.TaskMap.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Taskgroups.Taskgroup.TaskMap']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

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

                if self.name_xr is not None:
                    return True

                if self.task_map is not None and self.task_map._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Taskgroups']['meta_info']


    class Users(object):
        """
        Container for individual local user information
        
        .. attribute:: user
        
        	Specific local user information
        	**type**\: list of  :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User>`
        
        

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
            	**type**\:  str
            
            .. attribute:: admin_user
            
            	Is admin plane user ?
            	**type**\:  bool
            
            .. attribute:: first_user
            
            	Is first user ?
            	**type**\:  bool
            
            .. attribute:: name_xr
            
            	Username
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed taskmap
            	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap>`
            
            .. attribute:: usergroup
            
            	Member usergroups
            	**type**\:  list of str
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.admin_user = None
                self.first_user = None
                self.name_xr = None
                self.task_map = Aaa.Users.User.TaskMap()
                self.task_map.parent = self
                self.usergroup = YLeafList()
                self.usergroup.parent = self
                self.usergroup.name = 'usergroup'


            class TaskMap(object):
                """
                Computed taskmap
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap.Tasks>`
                
                

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
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.debug = None
                        self.execute = None
                        self.read = None
                        self.task_id = None
                        self.write = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.debug is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.task_id is not None:
                            return True

                        if self.write is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Users.User.TaskMap.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Users.User.TaskMap']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:users/Cisco-IOS-XR-aaa-locald-oper:user[Cisco-IOS-XR-aaa-locald-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.admin_user is not None:
                    return True

                if self.first_user is not None:
                    return True

                if self.name_xr is not None:
                    return True

                if self.task_map is not None and self.task_map._has_data():
                    return True

                if self.usergroup is not None:
                    for child in self.usergroup:
                        if child is not None:
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Users']['meta_info']


    class Usergroups(object):
        """
        Container for individual usergroup Information
        
        .. attribute:: usergroup
        
        	Specific Usergroup Information
        	**type**\: list of  :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup>`
        
        

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
            	**type**\:  str
            
            .. attribute:: name_xr
            
            	Name of the usergroup
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap>`
            
            .. attribute:: taskgroup
            
            	Component taskgroups
            	**type**\: list of  :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup>`
            
            

            """

            _prefix = 'aaa-locald-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.name_xr = None
                self.task_map = Aaa.Usergroups.Usergroup.TaskMap()
                self.task_map.parent = self
                self.taskgroup = YList()
                self.taskgroup.parent = self
                self.taskgroup.name = 'taskgroup'


            class TaskMap(object):
                """
                Computed task map
                
                .. attribute:: tasks
                
                	List of permitted tasks
                	**type**\: list of  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap.Tasks>`
                
                

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
                    
                    .. attribute:: debug
                    
                    	Is debug permitted?
                    	**type**\:  bool
                    
                    .. attribute:: execute
                    
                    	Is execute permitted?
                    	**type**\:  bool
                    
                    .. attribute:: read
                    
                    	Is read permitted?
                    	**type**\:  bool
                    
                    .. attribute:: task_id
                    
                    	Name of the task\-id
                    	**type**\:  str
                    
                    .. attribute:: write
                    
                    	Is write permitted?
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'aaa-locald-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.debug = None
                        self.execute = None
                        self.read = None
                        self.task_id = None
                        self.write = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.debug is not None:
                            return True

                        if self.execute is not None:
                            return True

                        if self.read is not None:
                            return True

                        if self.task_id is not None:
                            return True

                        if self.write is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.TaskMap.Tasks']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Usergroups.Usergroup.TaskMap']['meta_info']


            class Taskgroup(object):
                """
                Component taskgroups
                
                .. attribute:: included_task_ids
                
                	Task\-ids included
                	**type**\:  :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds>`
                
                .. attribute:: name_xr
                
                	Name of the taskgroup
                	**type**\:  str
                
                .. attribute:: task_map
                
                	Computed task map
                	**type**\:  :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap>`
                
                

                """

                _prefix = 'aaa-locald-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.included_task_ids = Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds()
                    self.included_task_ids.parent = self
                    self.name_xr = None
                    self.task_map = Aaa.Usergroups.Usergroup.Taskgroup.TaskMap()
                    self.task_map.parent = self


                class IncludedTaskIds(object):
                    """
                    Task\-ids included
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks>`
                    
                    

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
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\:  bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\:  bool
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\:  bool
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\:  str
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.debug = None
                            self.execute = None
                            self.read = None
                            self.task_id = None
                            self.write = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.debug is not None:
                                return True

                            if self.execute is not None:
                                return True

                            if self.read is not None:
                                return True

                            if self.task_id is not None:
                                return True

                            if self.write is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                            return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds']['meta_info']


                class TaskMap(object):
                    """
                    Computed task map
                    
                    .. attribute:: tasks
                    
                    	List of permitted tasks
                    	**type**\: list of  :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks>`
                    
                    

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
                        
                        .. attribute:: debug
                        
                        	Is debug permitted?
                        	**type**\:  bool
                        
                        .. attribute:: execute
                        
                        	Is execute permitted?
                        	**type**\:  bool
                        
                        .. attribute:: read
                        
                        	Is read permitted?
                        	**type**\:  bool
                        
                        .. attribute:: task_id
                        
                        	Name of the task\-id
                        	**type**\:  str
                        
                        .. attribute:: write
                        
                        	Is write permitted?
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'aaa-locald-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.debug = None
                            self.execute = None
                            self.read = None
                            self.task_id = None
                            self.write = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:tasks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.debug is not None:
                                return True

                            if self.execute is not None:
                                return True

                            if self.read is not None:
                                return True

                            if self.task_id is not None:
                                return True

                            if self.write is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                            return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-aaa-locald-oper:taskgroup'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.included_task_ids is not None and self.included_task_ids._has_data():
                        return True

                    if self.name_xr is not None:
                        return True

                    if self.task_map is not None and self.task_map._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:usergroups/Cisco-IOS-XR-aaa-locald-oper:usergroup[Cisco-IOS-XR-aaa-locald-oper:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.name_xr is not None:
                    return True

                if self.task_map is not None and self.task_map._has_data():
                    return True

                if self.taskgroup is not None:
                    for child_ref in self.taskgroup:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Usergroups']['meta_info']


    class AuthenMethod(object):
        """
        Current users authentication method
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.authenmethod = None
            self.name = None
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:authen-method'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.authenmethod is not None:
                return True

            if self.name is not None:
                return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.AuthenMethod']['meta_info']


    class CurrentUsergroup(object):
        """
        Specific Usergroup Information
        
        .. attribute:: authenmethod
        
        	Authentication method
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        .. attribute:: name
        
        	Name of the usergroup
        	**type**\:  str
        
        .. attribute:: taskmap
        
        	Task map details
        	**type**\:  list of str
        
        .. attribute:: usergroup
        
        	Component usergroups
        	**type**\:  list of str
        
        

        """

        _prefix = 'aaa-locald-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.authenmethod = None
            self.name = None
            self.taskmap = YLeafList()
            self.taskmap.parent = self
            self.taskmap.name = 'taskmap'
            self.usergroup = YLeafList()
            self.usergroup.parent = self
            self.usergroup.name = 'usergroup'

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-locald-oper:current-usergroup'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.authenmethod is not None:
                return True

            if self.name is not None:
                return True

            if self.taskmap is not None:
                for child in self.taskmap:
                    if child is not None:
                        return True

            if self.usergroup is not None:
                for child in self.usergroup:
                    if child is not None:
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.CurrentUsergroup']['meta_info']


    class Radius(object):
        """
        RADIUS operational data
        
        .. attribute:: global_
        
        	RADIUS Client Information
        	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Global>`
        
        .. attribute:: servers
        
        	List of RADIUS servers configured
        	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.global_ = Aaa.Radius.Global()
            self.global_.parent = self
            self.servers = Aaa.Radius.Servers()
            self.servers.parent = self


        class Servers(object):
            """
            List of RADIUS servers configured
            
            .. attribute:: server
            
            	RADIUS Server
            	**type**\: list of  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers.Server>`
            
            

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
                
                .. attribute:: aborts
                
                	Total number of requests aborted
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_accepts
                
                	Number of access accepts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_challenges
                
                	Number of access challenges
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_rejects
                
                	Number of access rejects
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_request_retransmits
                
                	Number of retransmitted                          access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_requests
                
                	Number of access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: access_timeouts
                
                	Number of access packets timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_port
                
                	Accounting port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_requests
                
                	Number of accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_responses
                
                	Number of accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_retransmits
                
                	Number of retransmitted                          accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_rtt
                
                	Round\-trip time for accounting                   in milliseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_timeouts
                
                	Number of accounting packets                     timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_incorrect_responses
                
                	Number of incorrect accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_port_number
                
                	Accounting Port number (standard port 1646)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: acct_response_time
                
                	Average response time for authentication requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_server_error_responses
                
                	Number of server error accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: acct_unexpected_responses
                
                	Number of unexpected accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: auth_port_number
                
                	Authentication Port number (standard port 1645)
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: authen_incorrect_responses
                
                	Number of incorrect authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_response_time
                
                	Average response time for authentication requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_server_error_responses
                
                	Number of server error authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_failure
                
                	Number of failed authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_transaction_successess
                
                	Number of succeeded authentication transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authen_unexpected_responses
                
                	Number of unexpected authentication responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_port
                
                	Authentication port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_rtt
                
                	Round\-trip time for authentication               in milliseconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_incorrect_responses
                
                	Number of incorrect authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_request_timeouts
                
                	Number of access packets timed out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_requests
                
                	Number of access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_response_time
                
                	Average response time for authorization requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_server_error_responses
                
                	Number of server error authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_failure
                
                	Number of failed authorization transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_transaction_successess
                
                	Number of succeeded authorization transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: author_unexpected_responses
                
                	Number of unexpected authorization responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_authenticators
                
                	Number of bad access authenticators
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_access_responses
                
                	Number of bad access responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_authenticators
                
                	Number of bad accounting                         authenticators
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bad_accounting_responses
                
                	Number of bad accounting responses
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: current_state_duration
                
                	Elapsed time the server has been in              current state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: currently_throttled_access_reqs
                
                	No of currently throttled access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_detect_time
                
                	Per\-server dead\-detect time in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_detect_tries
                
                	Per\-server dead\-detect tries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_time
                
                	Per\-server deadtime in minutes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_access_responses
                
                	Number of access responses dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dropped_accounting_responses
                
                	Number of accounting responses                   dropped
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: family
                
                	IP address Family
                	**type**\:  str
                
                .. attribute:: group_name
                
                	Server group name for private server
                	**type**\:  str
                
                .. attribute:: ip_address
                
                	IP address of RADIUS server
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: ip_address_xr
                
                	IP address buffer
                	**type**\:  str
                
                .. attribute:: ipv4_address
                
                	IP address of RADIUS server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: is_a_private_server
                
                	Is a private server
                	**type**\:  bool
                
                .. attribute:: is_quarantined
                
                	flag to indicate Server is quarantined           or not (Automated TEST in progress)
                	**type**\:  bool
                
                .. attribute:: last_deadtime
                
                	Time of Server being in DEAD state,              after last UP
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_acct_throttled
                
                	Max throttled acct transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: max_throttled_access_reqs
                
                	Max throttled access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_in
                
                	Total number of incoming packets read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: packets_out
                
                	Total number of outgoing packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_access_requests
                
                	Number of pending access requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: pending_accounting_requets
                
                	Number of pending accounting requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: previous_state_duration
                
                	Elapsed time the server was been in              previous state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: priority
                
                	A number that indicates the priority             of the server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: redirected_requests
                
                	Number of requests redirected
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	Number of replies expected to arrive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: retransmit
                
                	Per\-server retransmit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: state
                
                	State of the server UP/DOWN
                	**type**\:  str
                
                .. attribute:: throttled_access_reqs
                
                	No of throttled access reqs stats
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_failures_stats
                
                	No of acct discarded transaction
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_timed_out_stats
                
                	No of acct transaction that is throttled is timedout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_acct_transactions
                
                	No of throttled acct transactions stats
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_dropped_reqs
                
                	No of discarded access reqs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttled_timed_out_reqs
                
                	No of access reqs that is throttled is timedout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: throttleda_acct_transactions
                
                	No of currently throttled acct transactions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeout_xr
                
                	Per\-server timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: timeouts
                
                	Total number of packets timed\-out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_deadtime
                
                	Total time of Server being in DEAD               state
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_pending
                
                	Total acct test pending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_reqs
                
                	 Total acct test req
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_response
                
                	Total acct test response
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_acct_timeouts
                
                	Total acct test timeouts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_pending
                
                	Total auth test pending
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_reqs
                
                	Total auth test request
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_response
                
                	Total auth test response
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_test_auth_timeouts
                
                	Total auth test timeouts
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_access_types
                
                	Number of packets received with unknown          type from authentication server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: unknown_accounting_types
                
                	Number of packets received with unknown          type from accounting server
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.aborts = None
                    self.access_accepts = None
                    self.access_challenges = None
                    self.access_rejects = None
                    self.access_request_retransmits = None
                    self.access_requests = None
                    self.access_timeouts = None
                    self.accounting_port = None
                    self.accounting_requests = None
                    self.accounting_responses = None
                    self.accounting_retransmits = None
                    self.accounting_rtt = None
                    self.accounting_timeouts = None
                    self.acct_incorrect_responses = None
                    self.acct_port_number = None
                    self.acct_response_time = None
                    self.acct_server_error_responses = None
                    self.acct_transaction_failure = None
                    self.acct_transaction_successess = None
                    self.acct_unexpected_responses = None
                    self.auth_port_number = None
                    self.authen_incorrect_responses = None
                    self.authen_response_time = None
                    self.authen_server_error_responses = None
                    self.authen_transaction_failure = None
                    self.authen_transaction_successess = None
                    self.authen_unexpected_responses = None
                    self.authentication_port = None
                    self.authentication_rtt = None
                    self.author_incorrect_responses = None
                    self.author_request_timeouts = None
                    self.author_requests = None
                    self.author_response_time = None
                    self.author_server_error_responses = None
                    self.author_transaction_failure = None
                    self.author_transaction_successess = None
                    self.author_unexpected_responses = None
                    self.bad_access_authenticators = None
                    self.bad_access_responses = None
                    self.bad_accounting_authenticators = None
                    self.bad_accounting_responses = None
                    self.current_state_duration = None
                    self.currently_throttled_access_reqs = None
                    self.dead_detect_time = None
                    self.dead_detect_tries = None
                    self.dead_time = None
                    self.dropped_access_responses = None
                    self.dropped_accounting_responses = None
                    self.family = None
                    self.group_name = None
                    self.ip_address = None
                    self.ip_address_xr = None
                    self.ipv4_address = None
                    self.is_a_private_server = None
                    self.is_quarantined = None
                    self.last_deadtime = None
                    self.max_acct_throttled = None
                    self.max_throttled_access_reqs = None
                    self.packets_in = None
                    self.packets_out = None
                    self.pending_access_requests = None
                    self.pending_accounting_requets = None
                    self.previous_state_duration = None
                    self.priority = None
                    self.redirected_requests = None
                    self.replies_expected = None
                    self.retransmit = None
                    self.state = None
                    self.throttled_access_reqs = None
                    self.throttled_acct_failures_stats = None
                    self.throttled_acct_timed_out_stats = None
                    self.throttled_acct_transactions = None
                    self.throttled_dropped_reqs = None
                    self.throttled_timed_out_reqs = None
                    self.throttleda_acct_transactions = None
                    self.timeout_xr = None
                    self.timeouts = None
                    self.total_deadtime = None
                    self.total_test_acct_pending = None
                    self.total_test_acct_reqs = None
                    self.total_test_acct_response = None
                    self.total_test_acct_timeouts = None
                    self.total_test_auth_pending = None
                    self.total_test_auth_reqs = None
                    self.total_test_auth_response = None
                    self.total_test_auth_timeouts = None
                    self.unknown_access_types = None
                    self.unknown_accounting_types = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:servers/Cisco-IOS-XR-aaa-protocol-radius-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.aborts is not None:
                        return True

                    if self.access_accepts is not None:
                        return True

                    if self.access_challenges is not None:
                        return True

                    if self.access_rejects is not None:
                        return True

                    if self.access_request_retransmits is not None:
                        return True

                    if self.access_requests is not None:
                        return True

                    if self.access_timeouts is not None:
                        return True

                    if self.accounting_port is not None:
                        return True

                    if self.accounting_requests is not None:
                        return True

                    if self.accounting_responses is not None:
                        return True

                    if self.accounting_retransmits is not None:
                        return True

                    if self.accounting_rtt is not None:
                        return True

                    if self.accounting_timeouts is not None:
                        return True

                    if self.acct_incorrect_responses is not None:
                        return True

                    if self.acct_port_number is not None:
                        return True

                    if self.acct_response_time is not None:
                        return True

                    if self.acct_server_error_responses is not None:
                        return True

                    if self.acct_transaction_failure is not None:
                        return True

                    if self.acct_transaction_successess is not None:
                        return True

                    if self.acct_unexpected_responses is not None:
                        return True

                    if self.auth_port_number is not None:
                        return True

                    if self.authen_incorrect_responses is not None:
                        return True

                    if self.authen_response_time is not None:
                        return True

                    if self.authen_server_error_responses is not None:
                        return True

                    if self.authen_transaction_failure is not None:
                        return True

                    if self.authen_transaction_successess is not None:
                        return True

                    if self.authen_unexpected_responses is not None:
                        return True

                    if self.authentication_port is not None:
                        return True

                    if self.authentication_rtt is not None:
                        return True

                    if self.author_incorrect_responses is not None:
                        return True

                    if self.author_request_timeouts is not None:
                        return True

                    if self.author_requests is not None:
                        return True

                    if self.author_response_time is not None:
                        return True

                    if self.author_server_error_responses is not None:
                        return True

                    if self.author_transaction_failure is not None:
                        return True

                    if self.author_transaction_successess is not None:
                        return True

                    if self.author_unexpected_responses is not None:
                        return True

                    if self.bad_access_authenticators is not None:
                        return True

                    if self.bad_access_responses is not None:
                        return True

                    if self.bad_accounting_authenticators is not None:
                        return True

                    if self.bad_accounting_responses is not None:
                        return True

                    if self.current_state_duration is not None:
                        return True

                    if self.currently_throttled_access_reqs is not None:
                        return True

                    if self.dead_detect_time is not None:
                        return True

                    if self.dead_detect_tries is not None:
                        return True

                    if self.dead_time is not None:
                        return True

                    if self.dropped_access_responses is not None:
                        return True

                    if self.dropped_accounting_responses is not None:
                        return True

                    if self.family is not None:
                        return True

                    if self.group_name is not None:
                        return True

                    if self.ip_address is not None:
                        return True

                    if self.ip_address_xr is not None:
                        return True

                    if self.ipv4_address is not None:
                        return True

                    if self.is_a_private_server is not None:
                        return True

                    if self.is_quarantined is not None:
                        return True

                    if self.last_deadtime is not None:
                        return True

                    if self.max_acct_throttled is not None:
                        return True

                    if self.max_throttled_access_reqs is not None:
                        return True

                    if self.packets_in is not None:
                        return True

                    if self.packets_out is not None:
                        return True

                    if self.pending_access_requests is not None:
                        return True

                    if self.pending_accounting_requets is not None:
                        return True

                    if self.previous_state_duration is not None:
                        return True

                    if self.priority is not None:
                        return True

                    if self.redirected_requests is not None:
                        return True

                    if self.replies_expected is not None:
                        return True

                    if self.retransmit is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.throttled_access_reqs is not None:
                        return True

                    if self.throttled_acct_failures_stats is not None:
                        return True

                    if self.throttled_acct_timed_out_stats is not None:
                        return True

                    if self.throttled_acct_transactions is not None:
                        return True

                    if self.throttled_dropped_reqs is not None:
                        return True

                    if self.throttled_timed_out_reqs is not None:
                        return True

                    if self.throttleda_acct_transactions is not None:
                        return True

                    if self.timeout_xr is not None:
                        return True

                    if self.timeouts is not None:
                        return True

                    if self.total_deadtime is not None:
                        return True

                    if self.total_test_acct_pending is not None:
                        return True

                    if self.total_test_acct_reqs is not None:
                        return True

                    if self.total_test_acct_response is not None:
                        return True

                    if self.total_test_acct_timeouts is not None:
                        return True

                    if self.total_test_auth_pending is not None:
                        return True

                    if self.total_test_auth_reqs is not None:
                        return True

                    if self.total_test_auth_response is not None:
                        return True

                    if self.total_test_auth_timeouts is not None:
                        return True

                    if self.unknown_access_types is not None:
                        return True

                    if self.unknown_accounting_types is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Radius.Servers']['meta_info']


        class Global(object):
            """
            RADIUS Client Information
            
            .. attribute:: accounting_nas_id
            
            	NAS\-Identifier of the RADIUSaccounting client
            	**type**\:  str
            
            .. attribute:: authentication_nas_id
            
            	NAS\-Identifier of the RADIUSauthentication client
            	**type**\:  str
            
            .. attribute:: unknown_accounting_response
            
            	Number of RADIUS Accounting\-Responsepackets received from unknownaddresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_authentication_response
            
            	Number of RADIUS Access\-Responsepackets received from unknownaddresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.accounting_nas_id = None
                self.authentication_nas_id = None
                self.unknown_accounting_response = None
                self.unknown_authentication_response = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:global'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.accounting_nas_id is not None:
                    return True

                if self.authentication_nas_id is not None:
                    return True

                if self.unknown_accounting_response is not None:
                    return True

                if self.unknown_authentication_response is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
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
            if self.global_ is not None and self.global_._has_data():
                return True

            if self.servers is not None and self.servers._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Radius']['meta_info']


    class Tacacs(object):
        """
        TACACS operational data
        
        .. attribute:: requests
        
        	TACACS Active Request List
        	**type**\:  :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests>`
        
        .. attribute:: server_groups
        
        	TACACS sg Information
        	**type**\:  :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups>`
        
        .. attribute:: servers
        
        	TACACS server Information
        	**type**\:  :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers>`
        
        

        """

        _prefix = 'aaa-tacacs-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.requests = Aaa.Tacacs.Requests()
            self.requests.parent = self
            self.server_groups = Aaa.Tacacs.ServerGroups()
            self.server_groups.parent = self
            self.servers = Aaa.Tacacs.Servers()
            self.servers.parent = self


        class Requests(object):
            """
            TACACS Active Request List
            
            .. attribute:: request
            
            	request
            	**type**\: list of  :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.request = YList()
                self.request.parent = self
                self.request.name = 'request'


            class Request(object):
                """
                request
                
                .. attribute:: tacacs_requestbag
                
                	tacacs requestbag
                	**type**\: list of  :py:class:`TacacsRequestbag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request.TacacsRequestbag>`
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tacacs_requestbag = YList()
                    self.tacacs_requestbag.parent = self
                    self.tacacs_requestbag.name = 'tacacs_requestbag'


                class TacacsRequestbag(object):
                    """
                    tacacs requestbag
                    
                    .. attribute:: bytes_in
                    
                    	bytes read from socket
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_out
                    
                    	bytes written
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: in_pak_size
                    
                    	size of the packet to be received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_pak_size
                    
                    	size of the packet to be sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pak_type
                    
                    	the type of packet
                    	**type**\:  str
                    
                    .. attribute:: session_id
                    
                    	same as in pkt hdr
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sock
                    
                    	socket number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: time_remaining
                    
                    	time remaining for this request
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.bytes_in = None
                        self.bytes_out = None
                        self.in_pak_size = None
                        self.out_pak_size = None
                        self.pak_type = None
                        self.session_id = None
                        self.sock = None
                        self.time_remaining = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:requests/Cisco-IOS-XR-aaa-tacacs-oper:request/Cisco-IOS-XR-aaa-tacacs-oper:tacacs-requestbag'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.bytes_in is not None:
                            return True

                        if self.bytes_out is not None:
                            return True

                        if self.in_pak_size is not None:
                            return True

                        if self.out_pak_size is not None:
                            return True

                        if self.pak_type is not None:
                            return True

                        if self.session_id is not None:
                            return True

                        if self.sock is not None:
                            return True

                        if self.time_remaining is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Tacacs.Requests.Request.TacacsRequestbag']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:requests/Cisco-IOS-XR-aaa-tacacs-oper:request'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tacacs_requestbag is not None:
                        for child_ref in self.tacacs_requestbag:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Tacacs.Requests.Request']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:requests'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.request is not None:
                    for child_ref in self.request:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Tacacs.Requests']['meta_info']


        class Servers(object):
            """
            TACACS server Information
            
            .. attribute:: server
            
            	server
            	**type**\: list of  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers.Server>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.server = YList()
                self.server.parent = self
                self.server.name = 'server'


            class Server(object):
                """
                server
                
                .. attribute:: aborts
                
                	abort count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: addr
                
                	internet address of T+ server
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: addr_buf
                
                	IP address buffer
                	**type**\:  str
                
                	**range:** 0..46
                
                .. attribute:: bytes_in
                
                	# of bytes read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: bytes_out
                
                	# of bytes out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: closes
                
                	socket closes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: conn_up
                
                	is the server connected ?
                	**type**\:  bool
                
                .. attribute:: errors
                
                	error count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: family
                
                	IP address Family
                	**type**\:  str
                
                	**range:** 0..5
                
                .. attribute:: is_private
                
                	is this a private server ?
                	**type**\:  bool
                
                .. attribute:: opens
                
                	socket opens
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_in
                
                	# of incoming packets read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: paks_out
                
                	# of outgoing packets sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port
                
                	per server port to use
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: replies_expected
                
                	# of replies expected to arrive
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: single_connect
                
                	is this a single connect server ?
                	**type**\:  bool
                
                .. attribute:: timeout
                
                	per\-server timeout
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: up
                
                	is the server UP or down ?
                	**type**\:  bool
                
                .. attribute:: vrf_name
                
                	VRF in which server is reachable
                	**type**\:  str
                
                	**range:** 0..33
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.aborts = None
                    self.addr = None
                    self.addr_buf = None
                    self.bytes_in = None
                    self.bytes_out = None
                    self.closes = None
                    self.conn_up = None
                    self.errors = None
                    self.family = None
                    self.is_private = None
                    self.opens = None
                    self.paks_in = None
                    self.paks_out = None
                    self.port = None
                    self.replies_expected = None
                    self.single_connect = None
                    self.timeout = None
                    self.up = None
                    self.vrf_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:servers/Cisco-IOS-XR-aaa-tacacs-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.aborts is not None:
                        return True

                    if self.addr is not None:
                        return True

                    if self.addr_buf is not None:
                        return True

                    if self.bytes_in is not None:
                        return True

                    if self.bytes_out is not None:
                        return True

                    if self.closes is not None:
                        return True

                    if self.conn_up is not None:
                        return True

                    if self.errors is not None:
                        return True

                    if self.family is not None:
                        return True

                    if self.is_private is not None:
                        return True

                    if self.opens is not None:
                        return True

                    if self.paks_in is not None:
                        return True

                    if self.paks_out is not None:
                        return True

                    if self.port is not None:
                        return True

                    if self.replies_expected is not None:
                        return True

                    if self.single_connect is not None:
                        return True

                    if self.timeout is not None:
                        return True

                    if self.up is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Tacacs.Servers.Server']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:servers'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Tacacs.Servers']['meta_info']


        class ServerGroups(object):
            """
            TACACS sg Information
            
            .. attribute:: server_group
            
            	server group
            	**type**\: list of  :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup>`
            
            

            """

            _prefix = 'aaa-tacacs-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.server_group = YList()
                self.server_group.parent = self
                self.server_group.name = 'server_group'


            class ServerGroup(object):
                """
                server group
                
                .. attribute:: group_name
                
                	name of the server group
                	**type**\:  str
                
                .. attribute:: server
                
                	list of servers in this group
                	**type**\: list of  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup.Server>`
                
                .. attribute:: sg_map_num
                
                	server group mapped number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	vrf of the group
                	**type**\:  str
                
                	**range:** 0..33
                
                

                """

                _prefix = 'aaa-tacacs-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.group_name = None
                    self.server = YList()
                    self.server.parent = self
                    self.server.name = 'server'
                    self.sg_map_num = None
                    self.vrf_name = None


                class Server(object):
                    """
                    list of servers in this group
                    
                    .. attribute:: aborts
                    
                    	abort count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: addr
                    
                    	internet address of T+ server
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: addr_buf
                    
                    	IP address buffer
                    	**type**\:  str
                    
                    	**range:** 0..46
                    
                    .. attribute:: bytes_in
                    
                    	# of bytes read
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_out
                    
                    	# of bytes out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: closes
                    
                    	socket closes
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: conn_up
                    
                    	is the server connected ?
                    	**type**\:  bool
                    
                    .. attribute:: errors
                    
                    	error count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: family
                    
                    	IP address Family
                    	**type**\:  str
                    
                    	**range:** 0..5
                    
                    .. attribute:: is_private
                    
                    	is this a private server ?
                    	**type**\:  bool
                    
                    .. attribute:: opens
                    
                    	socket opens
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_in
                    
                    	# of incoming packets read
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paks_out
                    
                    	# of outgoing packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: port
                    
                    	per server port to use
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: replies_expected
                    
                    	# of replies expected to arrive
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: single_connect
                    
                    	is this a single connect server ?
                    	**type**\:  bool
                    
                    .. attribute:: timeout
                    
                    	per\-server timeout
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: up
                    
                    	is the server UP or down ?
                    	**type**\:  bool
                    
                    .. attribute:: vrf_name
                    
                    	VRF in which server is reachable
                    	**type**\:  str
                    
                    	**range:** 0..33
                    
                    

                    """

                    _prefix = 'aaa-tacacs-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.aborts = None
                        self.addr = None
                        self.addr_buf = None
                        self.bytes_in = None
                        self.bytes_out = None
                        self.closes = None
                        self.conn_up = None
                        self.errors = None
                        self.family = None
                        self.is_private = None
                        self.opens = None
                        self.paks_in = None
                        self.paks_out = None
                        self.port = None
                        self.replies_expected = None
                        self.single_connect = None
                        self.timeout = None
                        self.up = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:server-groups/Cisco-IOS-XR-aaa-tacacs-oper:server-group/Cisco-IOS-XR-aaa-tacacs-oper:server'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.aborts is not None:
                            return True

                        if self.addr is not None:
                            return True

                        if self.addr_buf is not None:
                            return True

                        if self.bytes_in is not None:
                            return True

                        if self.bytes_out is not None:
                            return True

                        if self.closes is not None:
                            return True

                        if self.conn_up is not None:
                            return True

                        if self.errors is not None:
                            return True

                        if self.family is not None:
                            return True

                        if self.is_private is not None:
                            return True

                        if self.opens is not None:
                            return True

                        if self.paks_in is not None:
                            return True

                        if self.paks_out is not None:
                            return True

                        if self.port is not None:
                            return True

                        if self.replies_expected is not None:
                            return True

                        if self.single_connect is not None:
                            return True

                        if self.timeout is not None:
                            return True

                        if self.up is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                        return meta._meta_table['Aaa.Tacacs.ServerGroups.ServerGroup.Server']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:server-groups/Cisco-IOS-XR-aaa-tacacs-oper:server-group'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.group_name is not None:
                        return True

                    if self.server is not None:
                        for child_ref in self.server:
                            if child_ref._has_data():
                                return True

                    if self.sg_map_num is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Tacacs.ServerGroups.ServerGroup']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs/Cisco-IOS-XR-aaa-tacacs-oper:server-groups'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.server_group is not None:
                    for child_ref in self.server_group:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Tacacs.ServerGroups']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-tacacs-oper:tacacs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.requests is not None and self.requests._has_data():
                return True

            if self.server_groups is not None and self.server_groups._has_data():
                return True

            if self.servers is not None and self.servers._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Tacacs']['meta_info']

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

        if self.authen_method is not None and self.authen_method._has_data():
            return True

        if self.current_usergroup is not None and self.current_usergroup._has_data():
            return True

        if self.currentuser_detail is not None and self.currentuser_detail._has_data():
            return True

        if self.radius is not None and self.radius._has_data():
            return True

        if self.tacacs is not None and self.tacacs._has_data():
            return True

        if self.task_map is not None and self.task_map._has_data():
            return True

        if self.taskgroups is not None and self.taskgroups._has_data():
            return True

        if self.usergroups is not None and self.usergroups._has_data():
            return True

        if self.users is not None and self.users._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
        return meta._meta_table['Aaa']['meta_info']


