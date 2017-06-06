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
    	**type**\:   :py:class:`AllTasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AllTasks>`
    
    .. attribute:: authen_method
    
    	Current users authentication method
    	**type**\:   :py:class:`AuthenMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.AuthenMethod>`
    
    .. attribute:: current_usergroup
    
    	Specific Usergroup Information
    	**type**\:   :py:class:`CurrentUsergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentUsergroup>`
    
    .. attribute:: currentuser_detail
    
    	Current user specific details
    	**type**\:   :py:class:`CurrentuserDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.CurrentuserDetail>`
    
    .. attribute:: diameter
    
    	Diameter operational data
    	**type**\:   :py:class:`Diameter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter>`
    
    .. attribute:: radius
    
    	RADIUS operational data
    	**type**\:   :py:class:`Radius <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius>`
    
    .. attribute:: tacacs
    
    	TACACS operational data
    	**type**\:   :py:class:`Tacacs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs>`
    
    .. attribute:: task_map
    
    	Task map of current user
    	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.TaskMap>`
    
    .. attribute:: taskgroups
    
    	Individual taskgroups container
    	**type**\:   :py:class:`Taskgroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups>`
    
    .. attribute:: usergroups
    
    	Container for individual usergroup Information
    	**type**\:   :py:class:`Usergroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups>`
    
    .. attribute:: users
    
    	Container for individual local user information
    	**type**\:   :py:class:`Users <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users>`
    
    

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
        self.diameter = Aaa.Diameter()
        self.diameter.parent = self
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
        	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup>`
        
        

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
            	**type**\:   :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds>`
            
            .. attribute:: name_xr
            
            	Name of the taskgroup
            	**type**\:  str
            
            .. attribute:: task_map
            
            	Computed task map
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap>`
            
            

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
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks>`
                
                

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
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Taskgroups.Taskgroup.TaskMap.Tasks>`
                
                

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
        	**type**\: list of    :py:class:`User <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User>`
        
        

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
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap>`
            
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
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Users.User.TaskMap.Tasks>`
                
                

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
        	**type**\: list of    :py:class:`Usergroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup>`
        
        

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
            	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap>`
            
            .. attribute:: taskgroup
            
            	Component taskgroups
            	**type**\: list of    :py:class:`Taskgroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup>`
            
            

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
                	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.TaskMap.Tasks>`
                
                

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
                	**type**\:   :py:class:`IncludedTaskIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds>`
                
                .. attribute:: name_xr
                
                	Name of the taskgroup
                	**type**\:  str
                
                .. attribute:: task_map
                
                	Computed task map
                	**type**\:   :py:class:`TaskMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap>`
                
                

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
                    	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks>`
                    
                    

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
                    	**type**\: list of    :py:class:`Tasks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks>`
                    
                    

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


    class Diameter(object):
        """
        Diameter operational data
        
        .. attribute:: gx
        
        	Diameter global gx data
        	**type**\:   :py:class:`Gx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gx>`
        
        .. attribute:: gx_session_ids
        
        	Diameter Gx Session data list
        	**type**\:   :py:class:`GxSessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds>`
        
        .. attribute:: gx_statistics
        
        	Diameter Gx Statistics data
        	**type**\:   :py:class:`GxStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxStatistics>`
        
        .. attribute:: gy
        
        	Diameter global gy data
        	**type**\:   :py:class:`Gy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Gy>`
        
        .. attribute:: gy_session_ids
        
        	Diameter Gy Session data list
        	**type**\:   :py:class:`GySessionIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds>`
        
        .. attribute:: gy_statistics
        
        	Diameter Gy Statistics data
        	**type**\:   :py:class:`GyStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GyStatistics>`
        
        .. attribute:: nas
        
        	Diameter NAS data
        	**type**\:   :py:class:`Nas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas>`
        
        .. attribute:: nas_session
        
        	Diameter Nas Session data
        	**type**\:   :py:class:`NasSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession>`
        
        .. attribute:: nas_summary
        
        	Diameter NAS summary
        	**type**\:   :py:class:`NasSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSummary>`
        
        .. attribute:: peers
        
        	Diameter peer global data
        	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers>`
        
        

        """

        _prefix = 'aaa-diameter-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.gx = Aaa.Diameter.Gx()
            self.gx.parent = self
            self.gx_session_ids = Aaa.Diameter.GxSessionIds()
            self.gx_session_ids.parent = self
            self.gx_statistics = Aaa.Diameter.GxStatistics()
            self.gx_statistics.parent = self
            self.gy = Aaa.Diameter.Gy()
            self.gy.parent = self
            self.gy_session_ids = Aaa.Diameter.GySessionIds()
            self.gy_session_ids.parent = self
            self.gy_statistics = Aaa.Diameter.GyStatistics()
            self.gy_statistics.parent = self
            self.nas = Aaa.Diameter.Nas()
            self.nas.parent = self
            self.nas_session = Aaa.Diameter.NasSession()
            self.nas_session.parent = self
            self.nas_summary = Aaa.Diameter.NasSummary()
            self.nas_summary.parent = self
            self.peers = Aaa.Diameter.Peers()
            self.peers.parent = self


        class Gy(object):
            """
            Diameter global gy data
            
            .. attribute:: is_enabled
            
            	Gy state
            	**type**\:  bool
            
            .. attribute:: retransmits
            
            	Gy retransmit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_timer
            
            	Gy transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.is_enabled = None
                self.retransmits = None
                self.tx_timer = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gy'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.is_enabled is not None:
                    return True

                if self.retransmits is not None:
                    return True

                if self.tx_timer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.Gy']['meta_info']


        class GxStatistics(object):
            """
            Diameter Gx Statistics data
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messsages
            
            	ASA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_termination_messages
            
            	Session Termination from server
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active_sessions = None
                self.asa_sent_error_messages = None
                self.asa_sent_messsages = None
                self.asr_received_error_messages = None
                self.asr_received_messages = None
                self.cca_final_error_messages = None
                self.cca_final_messages = None
                self.cca_init_error_messages = None
                self.cca_init_messages = None
                self.cca_update_error_messages = None
                self.cca_update_messages = None
                self.ccr_final_failed_messages = None
                self.ccr_final_messages = None
                self.ccr_final_retry_messages = None
                self.ccr_final_timed_out_messages = None
                self.ccr_init_failed_messages = None
                self.ccr_init_messages = None
                self.ccr_init_retry_messages = None
                self.ccr_init_timed_out_messages = None
                self.ccr_update_failed_messages = None
                self.ccr_update_messages = None
                self.ccr_update_retry_messages = None
                self.ccr_update_timed_out_messages = None
                self.close_sessions = None
                self.open_sessions = None
                self.raa_sent_error_messages = None
                self.raa_sent_messages = None
                self.rar_received_error_messages = None
                self.rar_received_messages = None
                self.restore_sessions = None
                self.session_termination_messages = None
                self.unknown_request_messages = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gx-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active_sessions is not None:
                    return True

                if self.asa_sent_error_messages is not None:
                    return True

                if self.asa_sent_messsages is not None:
                    return True

                if self.asr_received_error_messages is not None:
                    return True

                if self.asr_received_messages is not None:
                    return True

                if self.cca_final_error_messages is not None:
                    return True

                if self.cca_final_messages is not None:
                    return True

                if self.cca_init_error_messages is not None:
                    return True

                if self.cca_init_messages is not None:
                    return True

                if self.cca_update_error_messages is not None:
                    return True

                if self.cca_update_messages is not None:
                    return True

                if self.ccr_final_failed_messages is not None:
                    return True

                if self.ccr_final_messages is not None:
                    return True

                if self.ccr_final_retry_messages is not None:
                    return True

                if self.ccr_final_timed_out_messages is not None:
                    return True

                if self.ccr_init_failed_messages is not None:
                    return True

                if self.ccr_init_messages is not None:
                    return True

                if self.ccr_init_retry_messages is not None:
                    return True

                if self.ccr_init_timed_out_messages is not None:
                    return True

                if self.ccr_update_failed_messages is not None:
                    return True

                if self.ccr_update_messages is not None:
                    return True

                if self.ccr_update_retry_messages is not None:
                    return True

                if self.ccr_update_timed_out_messages is not None:
                    return True

                if self.close_sessions is not None:
                    return True

                if self.open_sessions is not None:
                    return True

                if self.raa_sent_error_messages is not None:
                    return True

                if self.raa_sent_messages is not None:
                    return True

                if self.rar_received_error_messages is not None:
                    return True

                if self.rar_received_messages is not None:
                    return True

                if self.restore_sessions is not None:
                    return True

                if self.session_termination_messages is not None:
                    return True

                if self.unknown_request_messages is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.GxStatistics']['meta_info']


        class Gx(object):
            """
            Diameter global gx data
            
            .. attribute:: is_enabled
            
            	Gx state
            	**type**\:  bool
            
            .. attribute:: retransmits
            
            	Gx retransmit count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: tx_timer
            
            	Gx transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.is_enabled = None
                self.retransmits = None
                self.tx_timer = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gx'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.is_enabled is not None:
                    return True

                if self.retransmits is not None:
                    return True

                if self.tx_timer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.Gx']['meta_info']


        class Peers(object):
            """
            Diameter peer global data
            
            .. attribute:: conn_retry_timer
            
            	Connection retry timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: origin_host
            
            	Origin Host
            	**type**\:  str
            
            .. attribute:: origin_realm
            
            	Origin Realm
            	**type**\:  str
            
            .. attribute:: peer
            
            	Peer List
            	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Peers.Peer>`
            
            .. attribute:: source_interface
            
            	Source Interface
            	**type**\:  str
            
            .. attribute:: tls_trustpoint
            
            	TLS Trustpoint
            	**type**\:  str
            
            .. attribute:: trans_max
            
            	Maximum number of transactions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: trans_total
            
            	Total number of transactions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: transaction_timer
            
            	Transaction timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: watchdog_timer
            
            	Watch dog timer in seconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.conn_retry_timer = None
                self.origin_host = None
                self.origin_realm = None
                self.peer = YList()
                self.peer.parent = self
                self.peer.name = 'peer'
                self.source_interface = None
                self.tls_trustpoint = None
                self.trans_max = None
                self.trans_total = None
                self.transaction_timer = None
                self.watchdog_timer = None


            class Peer(object):
                """
                Peer List
                
                .. attribute:: address
                
                	IPv4 or IPv6 address of DIAMETER peer
                	**type**\:  str
                
                .. attribute:: conn_retry_timer
                
                	Connection retry timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: destination_host
                
                	Destination host name
                	**type**\:  str
                
                .. attribute:: destination_realm
                
                	Destination realm
                	**type**\:  str
                
                .. attribute:: firmware_revision
                
                	Firmware revision
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_aa_as
                
                	Incoming AAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_as
                
                	Incoming ACAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ac_rs
                
                	Incoming ACRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_as_as
                
                	Incoming ASAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_as_rs
                
                	Incoming ASRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_as
                
                	Incoming CCAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_cc_rs
                
                	Incoming CCRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_as
                
                	Incoming CEAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ce_rs
                
                	Incoming CERs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_as
                
                	Incoming DPAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dp_rs
                
                	Incoming DPRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_as
                
                	Incoming DWAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_dw_rs
                
                	Incoming DWRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_as
                
                	Incoming RAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_ra_rs
                
                	Incoming RARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_as
                
                	Incoming STAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: in_st_rs
                
                	Incoming STRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_disconnect_cause
                
                	Last Disconnect Reason
                	**type**\:   :py:class:`DisconnectCauseEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.DisconnectCauseEnum>`
                
                .. attribute:: malformed_requests
                
                	Malformed Requests
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_aa_rs
                
                	Outgoing AARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_as
                
                	Outgoing ACAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ac_rs
                
                	Outgoing ACRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_as
                
                	Outgoing ASAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_as_rs
                
                	Outgoing ASRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_as
                
                	Outgoing CCAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_cc_rs
                
                	Outgoing CCRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_as
                
                	Outgoing CEAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ce_rs
                
                	Outgoing CERs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_as
                
                	Outgoing DPAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dp_rs
                
                	Outgoing DPRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_as
                
                	Outgoing DWAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_dw_rs
                
                	Outgoing DWRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_as
                
                	Outgoing RAAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_ra_rs
                
                	Outgoing RARs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_as
                
                	Outgoing STAs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: out_st_rs
                
                	Outgoing STRs
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_index
                
                	Peer Index
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: peer_name
                
                	Peer Name
                	**type**\:  str
                
                .. attribute:: peer_type
                
                	Peer Type
                	**type**\:   :py:class:`PeerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.PeerEnum>`
                
                .. attribute:: port
                
                	Port number on which the peeris running
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: port_connect
                
                	Local Connection port
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: protocol_type
                
                	Protocol Type
                	**type**\:   :py:class:`ProtocolTypeValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.ProtocolTypeValueEnum>`
                
                .. attribute:: received_permanent_fails
                
                	Permanent Failures Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_proto_errors
                
                	Protocol Error Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received_transient_fails
                
                	Transient failures Received
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: security_type
                
                	Security type used to transport
                	**type**\:   :py:class:`SecurityTypeValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.SecurityTypeValueEnum>`
                
                .. attribute:: sent_permanent_fails
                
                	Permanent Failures Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_proto_errors
                
                	Protocol Error Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: sent_transient_fails
                
                	Transient failures Sent
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: source_interface
                
                	Source Interface
                	**type**\:  str
                
                .. attribute:: state
                
                	Peer Connection Status
                	**type**\:   :py:class:`PeerStateValueEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.PeerStateValueEnum>`
                
                .. attribute:: state_duration
                
                	State Duration in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transaction_timer
                
                	Transaction timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: transport_down
                
                	Transport Down
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	Vrf Name
                	**type**\:  str
                
                .. attribute:: watchdog_timer
                
                	Watch dog timer in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: who_init_disconnect
                
                	Who Initiated Disconnect
                	**type**\:   :py:class:`WhoInitiatedDisconnectEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper.WhoInitiatedDisconnectEnum>`
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.address = None
                    self.conn_retry_timer = None
                    self.destination_host = None
                    self.destination_realm = None
                    self.firmware_revision = None
                    self.in_aa_as = None
                    self.in_ac_as = None
                    self.in_ac_rs = None
                    self.in_as_as = None
                    self.in_as_rs = None
                    self.in_cc_as = None
                    self.in_cc_rs = None
                    self.in_ce_as = None
                    self.in_ce_rs = None
                    self.in_dp_as = None
                    self.in_dp_rs = None
                    self.in_dw_as = None
                    self.in_dw_rs = None
                    self.in_ra_as = None
                    self.in_ra_rs = None
                    self.in_st_as = None
                    self.in_st_rs = None
                    self.last_disconnect_cause = None
                    self.malformed_requests = None
                    self.out_aa_rs = None
                    self.out_ac_as = None
                    self.out_ac_rs = None
                    self.out_as_as = None
                    self.out_as_rs = None
                    self.out_cc_as = None
                    self.out_cc_rs = None
                    self.out_ce_as = None
                    self.out_ce_rs = None
                    self.out_dp_as = None
                    self.out_dp_rs = None
                    self.out_dw_as = None
                    self.out_dw_rs = None
                    self.out_ra_as = None
                    self.out_ra_rs = None
                    self.out_st_as = None
                    self.out_st_rs = None
                    self.peer_index = None
                    self.peer_name = None
                    self.peer_type = None
                    self.port = None
                    self.port_connect = None
                    self.protocol_type = None
                    self.received_permanent_fails = None
                    self.received_proto_errors = None
                    self.received_transient_fails = None
                    self.security_type = None
                    self.sent_permanent_fails = None
                    self.sent_proto_errors = None
                    self.sent_transient_fails = None
                    self.source_interface = None
                    self.state = None
                    self.state_duration = None
                    self.transaction_timer = None
                    self.transport_down = None
                    self.vrf_name = None
                    self.watchdog_timer = None
                    self.who_init_disconnect = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:peers/Cisco-IOS-XR-aaa-diameter-oper:peer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.address is not None:
                        return True

                    if self.conn_retry_timer is not None:
                        return True

                    if self.destination_host is not None:
                        return True

                    if self.destination_realm is not None:
                        return True

                    if self.firmware_revision is not None:
                        return True

                    if self.in_aa_as is not None:
                        return True

                    if self.in_ac_as is not None:
                        return True

                    if self.in_ac_rs is not None:
                        return True

                    if self.in_as_as is not None:
                        return True

                    if self.in_as_rs is not None:
                        return True

                    if self.in_cc_as is not None:
                        return True

                    if self.in_cc_rs is not None:
                        return True

                    if self.in_ce_as is not None:
                        return True

                    if self.in_ce_rs is not None:
                        return True

                    if self.in_dp_as is not None:
                        return True

                    if self.in_dp_rs is not None:
                        return True

                    if self.in_dw_as is not None:
                        return True

                    if self.in_dw_rs is not None:
                        return True

                    if self.in_ra_as is not None:
                        return True

                    if self.in_ra_rs is not None:
                        return True

                    if self.in_st_as is not None:
                        return True

                    if self.in_st_rs is not None:
                        return True

                    if self.last_disconnect_cause is not None:
                        return True

                    if self.malformed_requests is not None:
                        return True

                    if self.out_aa_rs is not None:
                        return True

                    if self.out_ac_as is not None:
                        return True

                    if self.out_ac_rs is not None:
                        return True

                    if self.out_as_as is not None:
                        return True

                    if self.out_as_rs is not None:
                        return True

                    if self.out_cc_as is not None:
                        return True

                    if self.out_cc_rs is not None:
                        return True

                    if self.out_ce_as is not None:
                        return True

                    if self.out_ce_rs is not None:
                        return True

                    if self.out_dp_as is not None:
                        return True

                    if self.out_dp_rs is not None:
                        return True

                    if self.out_dw_as is not None:
                        return True

                    if self.out_dw_rs is not None:
                        return True

                    if self.out_ra_as is not None:
                        return True

                    if self.out_ra_rs is not None:
                        return True

                    if self.out_st_as is not None:
                        return True

                    if self.out_st_rs is not None:
                        return True

                    if self.peer_index is not None:
                        return True

                    if self.peer_name is not None:
                        return True

                    if self.peer_type is not None:
                        return True

                    if self.port is not None:
                        return True

                    if self.port_connect is not None:
                        return True

                    if self.protocol_type is not None:
                        return True

                    if self.received_permanent_fails is not None:
                        return True

                    if self.received_proto_errors is not None:
                        return True

                    if self.received_transient_fails is not None:
                        return True

                    if self.security_type is not None:
                        return True

                    if self.sent_permanent_fails is not None:
                        return True

                    if self.sent_proto_errors is not None:
                        return True

                    if self.sent_transient_fails is not None:
                        return True

                    if self.source_interface is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.state_duration is not None:
                        return True

                    if self.transaction_timer is not None:
                        return True

                    if self.transport_down is not None:
                        return True

                    if self.vrf_name is not None:
                        return True

                    if self.watchdog_timer is not None:
                        return True

                    if self.who_init_disconnect is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Diameter.Peers.Peer']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:peers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.conn_retry_timer is not None:
                    return True

                if self.origin_host is not None:
                    return True

                if self.origin_realm is not None:
                    return True

                if self.peer is not None:
                    for child_ref in self.peer:
                        if child_ref._has_data():
                            return True

                if self.source_interface is not None:
                    return True

                if self.tls_trustpoint is not None:
                    return True

                if self.trans_max is not None:
                    return True

                if self.trans_total is not None:
                    return True

                if self.transaction_timer is not None:
                    return True

                if self.watchdog_timer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.Peers']['meta_info']


        class Nas(object):
            """
            Diameter NAS data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\:  str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of    :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.Nas.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.aaanas_id = None
                self.list_of_nas = YList()
                self.list_of_nas.parent = self
                self.list_of_nas.name = 'list_of_nas'


            class ListOfNas(object):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  str
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\:  str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.aaa_session_id = None
                    self.accounting_intrim_in_packets = None
                    self.accounting_intrim_out_packets = None
                    self.accounting_status = None
                    self.accounting_status_stop = None
                    self.authentication_status = None
                    self.authorization_status = None
                    self.diameter_session_id = None
                    self.disconnect_status = None
                    self.method_list = None
                    self.server_used_list = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:nas/Cisco-IOS-XR-aaa-diameter-oper:list-of-nas'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.aaa_session_id is not None:
                        return True

                    if self.accounting_intrim_in_packets is not None:
                        return True

                    if self.accounting_intrim_out_packets is not None:
                        return True

                    if self.accounting_status is not None:
                        return True

                    if self.accounting_status_stop is not None:
                        return True

                    if self.authentication_status is not None:
                        return True

                    if self.authorization_status is not None:
                        return True

                    if self.diameter_session_id is not None:
                        return True

                    if self.disconnect_status is not None:
                        return True

                    if self.method_list is not None:
                        return True

                    if self.server_used_list is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Diameter.Nas.ListOfNas']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:nas'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.aaanas_id is not None:
                    return True

                if self.list_of_nas is not None:
                    for child_ref in self.list_of_nas:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.Nas']['meta_info']


        class NasSummary(object):
            """
            Diameter NAS summary
            
            .. attribute:: accounting_interim_failed_packets
            
            	Accounting interim response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_in_packets
            
            	Accounting Interim request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_request_out_packets
            
            	Accounting interim requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_response_out_packets
            
            	Accounting interim response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_interim_success_packets
            
            	Accounting interim response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_intrim_response_in_packets
            
            	Accounting interim packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_request_out_packets
            
            	Accounting requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_response_in_packets
            
            	Accounting packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_failed_packets
            
            	Accounting start response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_request_packets
            
            	Accounting start request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_response_packets
            
            	Accounting start response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_start_success_packets
            
            	Accounting start response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_failed_packets
            
            	Accounting stop response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_in_packets
            
            	Acct stop request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_request_out_packets
            
            	Accounting stop requests packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_in_packets
            
            	Accounting stop packet response in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_response_out_packets
            
            	Acct stop response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: accounting_stop_success_response_packets
            
            	Accounting stop response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_in_packets
            
            	Authentication request from client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_request_out_packets
            
            	Authentication request pkt out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_fail_packets
            
            	Authentication response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_in_packets
            
            	Authentication response pkt in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_response_out_packets
            
            	Authentication response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authen_success_packets
            
            	Authentication response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_in_packets
            
            	Authorization response packet in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_out_packets
            
            	Authorization request packet out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_request_in_packets
            
            	Authourization request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_fail_packets
            
            	Authentication response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_out_packets
            
            	Authourization response frwd to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: authorization_response_success_packets
            
            	Authentication response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_failed_packets
            
            	COA response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_in_packets
            
            	COA/RAR Request packet in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_request_packets
            
            	COA request from client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_out_packets
            
            	COA/RAR Response packet out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_response_packets
            
            	COA response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: coa_success_packets
            
            	COA response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_failed_response_packets
            
            	Disconnect response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_in_packets
            
            	Disconnect request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_request_out_packets
            
            	Disconnect request pkt out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_in_packets
            
            	Disconnect response packets in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_response_out_packets
            
            	Disconnect response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: disconnect_success_response_packets
            
            	Disconnect response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_failed_packets
            
            	POD response with failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_in_packets
            
            	POD/RAR Request packets in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_out_packets
            
            	PAD/RAR Response packets out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_request_in_packets
            
            	POD request from cleint
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_response_out_packets
            
            	POD response forward to client
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pod_success_packets
            
            	POD response with success
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.accounting_interim_failed_packets = None
                self.accounting_interim_request_in_packets = None
                self.accounting_interim_request_out_packets = None
                self.accounting_interim_response_out_packets = None
                self.accounting_interim_success_packets = None
                self.accounting_intrim_response_in_packets = None
                self.accounting_request_out_packets = None
                self.accounting_response_in_packets = None
                self.accounting_start_failed_packets = None
                self.accounting_start_request_packets = None
                self.accounting_start_response_packets = None
                self.accounting_start_success_packets = None
                self.accounting_stop_failed_packets = None
                self.accounting_stop_request_in_packets = None
                self.accounting_stop_request_out_packets = None
                self.accounting_stop_response_in_packets = None
                self.accounting_stop_response_out_packets = None
                self.accounting_stop_success_response_packets = None
                self.authen_request_in_packets = None
                self.authen_request_out_packets = None
                self.authen_response_fail_packets = None
                self.authen_response_in_packets = None
                self.authen_response_out_packets = None
                self.authen_success_packets = None
                self.authorization_in_packets = None
                self.authorization_out_packets = None
                self.authorization_request_in_packets = None
                self.authorization_response_fail_packets = None
                self.authorization_response_out_packets = None
                self.authorization_response_success_packets = None
                self.coa_failed_packets = None
                self.coa_request_in_packets = None
                self.coa_request_packets = None
                self.coa_response_out_packets = None
                self.coa_response_packets = None
                self.coa_success_packets = None
                self.disconnect_failed_response_packets = None
                self.disconnect_request_in_packets = None
                self.disconnect_request_out_packets = None
                self.disconnect_response_in_packets = None
                self.disconnect_response_out_packets = None
                self.disconnect_success_response_packets = None
                self.pod_failed_packets = None
                self.pod_in_packets = None
                self.pod_out_packets = None
                self.pod_request_in_packets = None
                self.pod_response_out_packets = None
                self.pod_success_packets = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:nas-summary'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.accounting_interim_failed_packets is not None:
                    return True

                if self.accounting_interim_request_in_packets is not None:
                    return True

                if self.accounting_interim_request_out_packets is not None:
                    return True

                if self.accounting_interim_response_out_packets is not None:
                    return True

                if self.accounting_interim_success_packets is not None:
                    return True

                if self.accounting_intrim_response_in_packets is not None:
                    return True

                if self.accounting_request_out_packets is not None:
                    return True

                if self.accounting_response_in_packets is not None:
                    return True

                if self.accounting_start_failed_packets is not None:
                    return True

                if self.accounting_start_request_packets is not None:
                    return True

                if self.accounting_start_response_packets is not None:
                    return True

                if self.accounting_start_success_packets is not None:
                    return True

                if self.accounting_stop_failed_packets is not None:
                    return True

                if self.accounting_stop_request_in_packets is not None:
                    return True

                if self.accounting_stop_request_out_packets is not None:
                    return True

                if self.accounting_stop_response_in_packets is not None:
                    return True

                if self.accounting_stop_response_out_packets is not None:
                    return True

                if self.accounting_stop_success_response_packets is not None:
                    return True

                if self.authen_request_in_packets is not None:
                    return True

                if self.authen_request_out_packets is not None:
                    return True

                if self.authen_response_fail_packets is not None:
                    return True

                if self.authen_response_in_packets is not None:
                    return True

                if self.authen_response_out_packets is not None:
                    return True

                if self.authen_success_packets is not None:
                    return True

                if self.authorization_in_packets is not None:
                    return True

                if self.authorization_out_packets is not None:
                    return True

                if self.authorization_request_in_packets is not None:
                    return True

                if self.authorization_response_fail_packets is not None:
                    return True

                if self.authorization_response_out_packets is not None:
                    return True

                if self.authorization_response_success_packets is not None:
                    return True

                if self.coa_failed_packets is not None:
                    return True

                if self.coa_request_in_packets is not None:
                    return True

                if self.coa_request_packets is not None:
                    return True

                if self.coa_response_out_packets is not None:
                    return True

                if self.coa_response_packets is not None:
                    return True

                if self.coa_success_packets is not None:
                    return True

                if self.disconnect_failed_response_packets is not None:
                    return True

                if self.disconnect_request_in_packets is not None:
                    return True

                if self.disconnect_request_out_packets is not None:
                    return True

                if self.disconnect_response_in_packets is not None:
                    return True

                if self.disconnect_response_out_packets is not None:
                    return True

                if self.disconnect_success_response_packets is not None:
                    return True

                if self.pod_failed_packets is not None:
                    return True

                if self.pod_in_packets is not None:
                    return True

                if self.pod_out_packets is not None:
                    return True

                if self.pod_request_in_packets is not None:
                    return True

                if self.pod_response_out_packets is not None:
                    return True

                if self.pod_success_packets is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.NasSummary']['meta_info']


        class GySessionIds(object):
            """
            Diameter Gy Session data list
            
            .. attribute:: gy_session_id
            
            	Diameter Gy Session data
            	**type**\: list of    :py:class:`GySessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GySessionIds.GySessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.gy_session_id = YList()
                self.gy_session_id.parent = self
                self.gy_session_id.name = 'gy_session_id'


            class GySessionId(object):
                """
                Diameter Gy Session data
                
                .. attribute:: session_id  <key>
                
                	Session Id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: parent_aaa_session_id
                
                	AAA Parent session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\:  str
                
                .. attribute:: retry_count
                
                	Gy Retry count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.session_id = None
                    self.aaa_session_id = None
                    self.diameter_session_id = None
                    self.parent_aaa_session_id = None
                    self.request_number = None
                    self.request_type = None
                    self.retry_count = None
                    self.session_state = None

                @property
                def _common_path(self):
                    if self.session_id is None:
                        raise YPYModelError('Key property session_id is None')

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gy-session-ids/Cisco-IOS-XR-aaa-diameter-oper:gy-session-id[Cisco-IOS-XR-aaa-diameter-oper:session-id = ' + str(self.session_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_id is not None:
                        return True

                    if self.aaa_session_id is not None:
                        return True

                    if self.diameter_session_id is not None:
                        return True

                    if self.parent_aaa_session_id is not None:
                        return True

                    if self.request_number is not None:
                        return True

                    if self.request_type is not None:
                        return True

                    if self.retry_count is not None:
                        return True

                    if self.session_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Diameter.GySessionIds.GySessionId']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gy-session-ids'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.gy_session_id is not None:
                    for child_ref in self.gy_session_id:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.GySessionIds']['meta_info']


        class GyStatistics(object):
            """
            Diameter Gy Statistics data
            
            .. attribute:: active_sessions
            
            	Total Active Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_error_messages
            
            	ASA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asa_sent_messages
            
            	ASA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_error_messages
            
            	ASR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: asr_received_messages
            
            	ASR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_error_messages
            
            	CCA Final Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_final_messages
            
            	CCA Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_error_messages
            
            	CCA Initial Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_init_messages
            
            	CCA Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_error_messages
            
            	CCA Update Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cca_update_messages
            
            	CCA Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_failed_messages
            
            	CCR Final Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_messages
            
            	CCR Final Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_retry_messages
            
            	CCR Final Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_final_timed_out_messages
            
            	CCR Final Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_failed_messages
            
            	CCR Initial Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_messages
            
            	CCR Initial Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_retry_messages
            
            	CCR Initial Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_init_timed_out_messages
            
            	CCR Initial Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_failed_messages
            
            	CCR Update Messages Failed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_messages
            
            	CCR Update Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_retry_messages
            
            	CCR Update Messages retry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccr_update_timed_out_messages
            
            	CCR Update Messages Timed Out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: close_sessions
            
            	Total Closed Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_sessions
            
            	Total Opened Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_error_messages
            
            	RAA Sent Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: raa_sent_messages
            
            	RAA Sent Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_error_messages
            
            	RAR Received Messages Error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rar_received_messages
            
            	RAR Received Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: restore_sessions
            
            	Restore Sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: unknown_request_messages
            
            	Unknown Request Messages
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.active_sessions = None
                self.asa_sent_error_messages = None
                self.asa_sent_messages = None
                self.asr_received_error_messages = None
                self.asr_received_messages = None
                self.cca_final_error_messages = None
                self.cca_final_messages = None
                self.cca_init_error_messages = None
                self.cca_init_messages = None
                self.cca_update_error_messages = None
                self.cca_update_messages = None
                self.ccr_final_failed_messages = None
                self.ccr_final_messages = None
                self.ccr_final_retry_messages = None
                self.ccr_final_timed_out_messages = None
                self.ccr_init_failed_messages = None
                self.ccr_init_messages = None
                self.ccr_init_retry_messages = None
                self.ccr_init_timed_out_messages = None
                self.ccr_update_failed_messages = None
                self.ccr_update_messages = None
                self.ccr_update_retry_messages = None
                self.ccr_update_timed_out_messages = None
                self.close_sessions = None
                self.open_sessions = None
                self.raa_sent_error_messages = None
                self.raa_sent_messages = None
                self.rar_received_error_messages = None
                self.rar_received_messages = None
                self.restore_sessions = None
                self.unknown_request_messages = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gy-statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.active_sessions is not None:
                    return True

                if self.asa_sent_error_messages is not None:
                    return True

                if self.asa_sent_messages is not None:
                    return True

                if self.asr_received_error_messages is not None:
                    return True

                if self.asr_received_messages is not None:
                    return True

                if self.cca_final_error_messages is not None:
                    return True

                if self.cca_final_messages is not None:
                    return True

                if self.cca_init_error_messages is not None:
                    return True

                if self.cca_init_messages is not None:
                    return True

                if self.cca_update_error_messages is not None:
                    return True

                if self.cca_update_messages is not None:
                    return True

                if self.ccr_final_failed_messages is not None:
                    return True

                if self.ccr_final_messages is not None:
                    return True

                if self.ccr_final_retry_messages is not None:
                    return True

                if self.ccr_final_timed_out_messages is not None:
                    return True

                if self.ccr_init_failed_messages is not None:
                    return True

                if self.ccr_init_messages is not None:
                    return True

                if self.ccr_init_retry_messages is not None:
                    return True

                if self.ccr_init_timed_out_messages is not None:
                    return True

                if self.ccr_update_failed_messages is not None:
                    return True

                if self.ccr_update_messages is not None:
                    return True

                if self.ccr_update_retry_messages is not None:
                    return True

                if self.ccr_update_timed_out_messages is not None:
                    return True

                if self.close_sessions is not None:
                    return True

                if self.open_sessions is not None:
                    return True

                if self.raa_sent_error_messages is not None:
                    return True

                if self.raa_sent_messages is not None:
                    return True

                if self.rar_received_error_messages is not None:
                    return True

                if self.rar_received_messages is not None:
                    return True

                if self.restore_sessions is not None:
                    return True

                if self.unknown_request_messages is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.GyStatistics']['meta_info']


        class GxSessionIds(object):
            """
            Diameter Gx Session data list
            
            .. attribute:: gx_session_id
            
            	Diameter Gx Session data
            	**type**\: list of    :py:class:`GxSessionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.GxSessionIds.GxSessionId>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.gx_session_id = YList()
                self.gx_session_id.parent = self
                self.gx_session_id.name = 'gx_session_id'


            class GxSessionId(object):
                """
                Diameter Gx Session data
                
                .. attribute:: session_id  <key>
                
                	Session Id
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: request_number
                
                	Request Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: request_type
                
                	Request Type
                	**type**\:  str
                
                .. attribute:: retry_count
                
                	Gx Retry count
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_state
                
                	Session State
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.session_id = None
                    self.aaa_session_id = None
                    self.diameter_session_id = None
                    self.request_number = None
                    self.request_type = None
                    self.retry_count = None
                    self.session_state = None

                @property
                def _common_path(self):
                    if self.session_id is None:
                        raise YPYModelError('Key property session_id is None')

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gx-session-ids/Cisco-IOS-XR-aaa-diameter-oper:gx-session-id[Cisco-IOS-XR-aaa-diameter-oper:session-id = ' + str(self.session_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.session_id is not None:
                        return True

                    if self.aaa_session_id is not None:
                        return True

                    if self.diameter_session_id is not None:
                        return True

                    if self.request_number is not None:
                        return True

                    if self.request_type is not None:
                        return True

                    if self.retry_count is not None:
                        return True

                    if self.session_state is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Diameter.GxSessionIds.GxSessionId']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:gx-session-ids'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.gx_session_id is not None:
                    for child_ref in self.gx_session_id:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.GxSessionIds']['meta_info']


        class NasSession(object):
            """
            Diameter Nas Session data
            
            .. attribute:: aaanas_id
            
            	AAA NAS id
            	**type**\:  str
            
            .. attribute:: list_of_nas
            
            	List of NAS Entries
            	**type**\: list of    :py:class:`ListOfNas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Diameter.NasSession.ListOfNas>`
            
            

            """

            _prefix = 'aaa-diameter-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.aaanas_id = None
                self.list_of_nas = YList()
                self.list_of_nas.parent = self
                self.list_of_nas.name = 'list_of_nas'


            class ListOfNas(object):
                """
                List of NAS Entries
                
                .. attribute:: aaa_session_id
                
                	AAA session id
                	**type**\:  str
                
                .. attribute:: accounting_intrim_in_packets
                
                	Accounting intrim packet response in
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_intrim_out_packets
                
                	Accounting intrim requests packets out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status
                
                	Diameter ACR status start
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: accounting_status_stop
                
                	Diameter ACR status stop
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authentication_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: authorization_status
                
                	Diameter AAR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: diameter_session_id
                
                	Diameter session id
                	**type**\:  str
                
                .. attribute:: disconnect_status
                
                	Diameter STR status
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: method_list
                
                	Method list used for authentication
                	**type**\:  str
                
                .. attribute:: server_used_list
                
                	Server used for authentication
                	**type**\:  str
                
                

                """

                _prefix = 'aaa-diameter-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.aaa_session_id = None
                    self.accounting_intrim_in_packets = None
                    self.accounting_intrim_out_packets = None
                    self.accounting_status = None
                    self.accounting_status_stop = None
                    self.authentication_status = None
                    self.authorization_status = None
                    self.diameter_session_id = None
                    self.disconnect_status = None
                    self.method_list = None
                    self.server_used_list = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:nas-session/Cisco-IOS-XR-aaa-diameter-oper:list-of-nas'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.aaa_session_id is not None:
                        return True

                    if self.accounting_intrim_in_packets is not None:
                        return True

                    if self.accounting_intrim_out_packets is not None:
                        return True

                    if self.accounting_status is not None:
                        return True

                    if self.accounting_status_stop is not None:
                        return True

                    if self.authentication_status is not None:
                        return True

                    if self.authorization_status is not None:
                        return True

                    if self.diameter_session_id is not None:
                        return True

                    if self.disconnect_status is not None:
                        return True

                    if self.method_list is not None:
                        return True

                    if self.server_used_list is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Diameter.NasSession.ListOfNas']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter/Cisco-IOS-XR-aaa-diameter-oper:nas-session'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.aaanas_id is not None:
                    return True

                if self.list_of_nas is not None:
                    for child_ref in self.list_of_nas:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Diameter.NasSession']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-diameter-oper:diameter'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.gx is not None and self.gx._has_data():
                return True

            if self.gx_session_ids is not None and self.gx_session_ids._has_data():
                return True

            if self.gx_statistics is not None and self.gx_statistics._has_data():
                return True

            if self.gy is not None and self.gy._has_data():
                return True

            if self.gy_session_ids is not None and self.gy_session_ids._has_data():
                return True

            if self.gy_statistics is not None and self.gy_statistics._has_data():
                return True

            if self.nas is not None and self.nas._has_data():
                return True

            if self.nas_session is not None and self.nas_session._has_data():
                return True

            if self.nas_summary is not None and self.nas_summary._has_data():
                return True

            if self.peers is not None and self.peers._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
            return meta._meta_table['Aaa.Diameter']['meta_info']


    class Radius(object):
        """
        RADIUS operational data
        
        .. attribute:: global_
        
        	RADIUS Client Information
        	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Global_>`
        
        .. attribute:: radius_source_interface
        
        	RADIUS source interfaces
        	**type**\:   :py:class:`RadiusSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface>`
        
        .. attribute:: servers
        
        	List of RADIUS servers configured
        	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers>`
        
        

        """

        _prefix = 'aaa-protocol-radius-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.global_ = Aaa.Radius.Global_()
            self.global_.parent = self
            self.radius_source_interface = Aaa.Radius.RadiusSourceInterface()
            self.radius_source_interface.parent = self
            self.servers = Aaa.Radius.Servers()
            self.servers.parent = self


        class Servers(object):
            """
            List of RADIUS servers configured
            
            .. attribute:: server
            
            	RADIUS Server
            	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.Servers.Server>`
            
            

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
                
                	**units**\: millisecond
                
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
                
                	**units**\: millisecond
                
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
                
                	**units**\: second
                
                .. attribute:: dead_detect_tries
                
                	Per\-server dead\-detect tries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: dead_time
                
                	Per\-server deadtime in minutes
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
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
                
                	**units**\: second
                
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
                if self.server is not None:
                    for child_ref in self.server:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Radius.Servers']['meta_info']


        class RadiusSourceInterface(object):
            """
            RADIUS source interfaces
            
            .. attribute:: list_of_source_interface
            
            	List of source interfaces
            	**type**\: list of    :py:class:`ListOfSourceInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface>`
            
            

            """

            _prefix = 'aaa-protocol-radius-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.list_of_source_interface = YList()
                self.list_of_source_interface.parent = self
                self.list_of_source_interface.name = 'list_of_source_interface'


            class ListOfSourceInterface(object):
                """
                List of source interfaces
                
                .. attribute:: interface_name
                
                	Name of the source interface
                	**type**\:  str
                
                .. attribute:: ipaddrv4
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..16
                
                .. attribute:: ipaddrv6
                
                	IP address buffer
                	**type**\:  str
                
                	**length:** 0..46
                
                .. attribute:: vrfid
                
                	VRF Id
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'aaa-protocol-radius-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface_name = None
                    self.ipaddrv4 = None
                    self.ipaddrv6 = None
                    self.vrfid = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:radius-source-interface/Cisco-IOS-XR-aaa-protocol-radius-oper:list-of-source-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.ipaddrv4 is not None:
                        return True

                    if self.ipaddrv6 is not None:
                        return True

                    if self.vrfid is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                    return meta._meta_table['Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius/Cisco-IOS-XR-aaa-protocol-radius-oper:radius-source-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.list_of_source_interface is not None:
                    for child_ref in self.list_of_source_interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_locald_oper as meta
                return meta._meta_table['Aaa.Radius.RadiusSourceInterface']['meta_info']


        class Global_(object):
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
                return meta._meta_table['Aaa.Radius.Global_']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-aaa-locald-oper:aaa/Cisco-IOS-XR-aaa-protocol-radius-oper:radius'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.global_ is not None and self.global_._has_data():
                return True

            if self.radius_source_interface is not None and self.radius_source_interface._has_data():
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
        	**type**\:   :py:class:`Requests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests>`
        
        .. attribute:: server_groups
        
        	TACACS sg Information
        	**type**\:   :py:class:`ServerGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups>`
        
        .. attribute:: servers
        
        	TACACS server Information
        	**type**\:   :py:class:`Servers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers>`
        
        

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
            	**type**\: list of    :py:class:`Request <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request>`
            
            

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
                	**type**\: list of    :py:class:`TacacsRequestbag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Requests.Request.TacacsRequestbag>`
                
                

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
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_out
                    
                    	bytes written
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
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
            	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.Servers.Server>`
            
            

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
                
                	**length:** 0..46
                
                .. attribute:: bytes_in
                
                	# of bytes read
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
                .. attribute:: bytes_out
                
                	# of bytes out
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: byte
                
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
                
                	**length:** 0..5
                
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
                
                	**length:** 0..33
                
                

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
            	**type**\: list of    :py:class:`ServerGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup>`
            
            

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
                	**type**\: list of    :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper.Aaa.Tacacs.ServerGroups.ServerGroup.Server>`
                
                .. attribute:: sg_map_num
                
                	server group mapped number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: vrf_name
                
                	vrf of the group
                	**type**\:  str
                
                	**length:** 0..33
                
                

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
                    
                    	**length:** 0..46
                    
                    .. attribute:: bytes_in
                    
                    	# of bytes read
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: bytes_out
                    
                    	# of bytes out
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
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
                    
                    	**length:** 0..5
                    
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
                    
                    	**length:** 0..33
                    
                    

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
        if self.all_tasks is not None and self.all_tasks._has_data():
            return True

        if self.authen_method is not None and self.authen_method._has_data():
            return True

        if self.current_usergroup is not None and self.current_usergroup._has_data():
            return True

        if self.currentuser_detail is not None and self.currentuser_detail._has_data():
            return True

        if self.diameter is not None and self.diameter._has_data():
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


