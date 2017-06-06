


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Aaa.AllTasks' : {
        'meta_info' : _MetaInfoClass('Aaa.AllTasks',
            False, 
            [
            _MetaInfoClassMember('task-id', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Names of available task-ids
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'all-tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.CurrentuserDetail' : {
        'meta_info' : _MetaInfoClass('Aaa.CurrentuserDetail',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Authentication method
                ''',
                'authenmethod',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskmap', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Task map details
                ''',
                'taskmap',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('usergroup', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Component usergroups
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'currentuser-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.TaskMap',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Authentication method
                ''',
                'authenmethod',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskmap', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Task map details
                ''',
                'taskmap',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('usergroup', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Component usergroups
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks',
            False, 
            [
            _MetaInfoClassMember('debug', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is debug permitted?
                ''',
                'debug',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('execute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is execute permitted?
                ''',
                'execute',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is read permitted?
                ''',
                'read',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the task-id
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('write', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is write permitted?
                ''',
                'write',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.IncludedTaskIds' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.IncludedTaskIds',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'included-task-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.TaskMap.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.TaskMap.Tasks',
            False, 
            [
            _MetaInfoClassMember('debug', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is debug permitted?
                ''',
                'debug',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('execute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is execute permitted?
                ''',
                'execute',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is read permitted?
                ''',
                'read',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the task-id
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('write', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is write permitted?
                ''',
                'write',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups.Taskgroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Taskgroup name
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-oper', True),
            _MetaInfoClassMember('included-task-ids', REFERENCE_CLASS, 'IncludedTaskIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.IncludedTaskIds', 
                [], [], 
                '''                Task-ids included
                ''',
                'included_task_ids',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the taskgroup
                ''',
                'name_xr',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.TaskMap', 
                [], [], 
                '''                Computed task map
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup', REFERENCE_LIST, 'Taskgroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup', 
                [], [], 
                '''                Specific Taskgroup Information
                ''',
                'taskgroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'taskgroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Users.User.TaskMap.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Users.User.TaskMap.Tasks',
            False, 
            [
            _MetaInfoClassMember('debug', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is debug permitted?
                ''',
                'debug',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('execute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is execute permitted?
                ''',
                'execute',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is read permitted?
                ''',
                'read',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the task-id
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('write', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is write permitted?
                ''',
                'write',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Users.User.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Users.User.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users.User.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Users.User' : {
        'meta_info' : _MetaInfoClass('Aaa.Users.User',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-oper', True),
            _MetaInfoClassMember('admin-user', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is admin plane user ?
                ''',
                'admin_user',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('first-user', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is first user ?
                ''',
                'first_user',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'name_xr',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users.User.TaskMap', 
                [], [], 
                '''                Computed taskmap
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('usergroup', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Member usergroups
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'user',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Users' : {
        'meta_info' : _MetaInfoClass('Aaa.Users',
            False, 
            [
            _MetaInfoClassMember('user', REFERENCE_LIST, 'User' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users.User', 
                [], [], 
                '''                Specific local user information
                ''',
                'user',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'users',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.TaskMap.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.TaskMap.Tasks',
            False, 
            [
            _MetaInfoClassMember('debug', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is debug permitted?
                ''',
                'debug',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('execute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is execute permitted?
                ''',
                'execute',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is read permitted?
                ''',
                'read',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the task-id
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('write', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is write permitted?
                ''',
                'write',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks',
            False, 
            [
            _MetaInfoClassMember('debug', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is debug permitted?
                ''',
                'debug',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('execute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is execute permitted?
                ''',
                'execute',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is read permitted?
                ''',
                'read',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the task-id
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('write', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is write permitted?
                ''',
                'write',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'included-task-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks',
            False, 
            [
            _MetaInfoClassMember('debug', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is debug permitted?
                ''',
                'debug',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('execute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is execute permitted?
                ''',
                'execute',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is read permitted?
                ''',
                'read',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the task-id
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('write', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is write permitted?
                ''',
                'write',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup',
            False, 
            [
            _MetaInfoClassMember('included-task-ids', REFERENCE_CLASS, 'IncludedTaskIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds', 
                [], [], 
                '''                Task-ids included
                ''',
                'included_task_ids',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the taskgroup
                ''',
                'name_xr',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.TaskMap', 
                [], [], 
                '''                Computed task map
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Usergroup name
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-oper', True),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the usergroup
                ''',
                'name_xr',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.TaskMap', 
                [], [], 
                '''                Computed task map
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskgroup', REFERENCE_LIST, 'Taskgroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup', 
                [], [], 
                '''                Component taskgroups
                ''',
                'taskgroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups',
            False, 
            [
            _MetaInfoClassMember('usergroup', REFERENCE_LIST, 'Usergroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup', 
                [], [], 
                '''                Specific Usergroup Information
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.AuthenMethod' : {
        'meta_info' : _MetaInfoClass('Aaa.AuthenMethod',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Authentication method
                ''',
                'authenmethod',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskmap', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Task map details
                ''',
                'taskmap',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('usergroup', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Component usergroups
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'authen-method',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.CurrentUsergroup' : {
        'meta_info' : _MetaInfoClass('Aaa.CurrentUsergroup',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Authentication method
                ''',
                'authenmethod',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskmap', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Task map details
                ''',
                'taskmap',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('usergroup', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Component usergroups
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'current-usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.Gy' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Gy',
            False, 
            [
            _MetaInfoClassMember('is-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Gy state
                ''',
                'is_enabled',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('retransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Gy retransmit count
                ''',
                'retransmits',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('tx-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Gy transaction timer in seconds
                ''',
                'tx_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gy',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.GxStatistics' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.GxStatistics',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Active Sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asa-sent-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASA Sent Messages Error
                ''',
                'asa_sent_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asa-sent-messsages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASA Sent Messages
                ''',
                'asa_sent_messsages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asr-received-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASR Received Messages Error
                ''',
                'asr_received_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asr-received-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASR Received Messages
                ''',
                'asr_received_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-final-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Final Messages Error
                ''',
                'cca_final_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-final-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Final Messages
                ''',
                'cca_final_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-init-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Initial Messages Error
                ''',
                'cca_init_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-init-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Initial Messages
                ''',
                'cca_init_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-update-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Update Messages Error
                ''',
                'cca_update_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Update Messages
                ''',
                'cca_update_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-failed-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages Failed
                ''',
                'ccr_final_failed_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages
                ''',
                'ccr_final_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-retry-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages retry
                ''',
                'ccr_final_retry_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-timed-out-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages Timed Out
                ''',
                'ccr_final_timed_out_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-failed-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages Failed
                ''',
                'ccr_init_failed_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages
                ''',
                'ccr_init_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-retry-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages retry
                ''',
                'ccr_init_retry_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-timed-out-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages Timed Out
                ''',
                'ccr_init_timed_out_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-failed-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages Failed
                ''',
                'ccr_update_failed_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages
                ''',
                'ccr_update_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-retry-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages retry
                ''',
                'ccr_update_retry_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-timed-out-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages Timed Out
                ''',
                'ccr_update_timed_out_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('close-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Closed Sessions
                ''',
                'close_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('open-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Opened Sessions
                ''',
                'open_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('raa-sent-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAA Sent Messages Error
                ''',
                'raa_sent_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('raa-sent-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAA Sent Messages
                ''',
                'raa_sent_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('rar-received-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAR Received Messages Error
                ''',
                'rar_received_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('rar-received-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAR Received Messages
                ''',
                'rar_received_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('restore-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Restore Sessions
                ''',
                'restore_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('session-termination-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Termination from server
                ''',
                'session_termination_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('unknown-request-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown Request Messages
                ''',
                'unknown_request_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gx-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.Gx' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Gx',
            False, 
            [
            _MetaInfoClassMember('is-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Gx state
                ''',
                'is_enabled',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('retransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Gx retransmit count
                ''',
                'retransmits',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('tx-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Gx transaction timer in seconds
                ''',
                'tx_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gx',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 or IPv6 address of DIAMETER peer
                ''',
                'address',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('conn-retry-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection retry timer in seconds
                ''',
                'conn_retry_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('destination-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination host name
                ''',
                'destination_host',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('destination-realm', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination realm
                ''',
                'destination_realm',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Firmware revision
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-aa-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming AAAs
                ''',
                'in_aa_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-ac-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming ACAs
                ''',
                'in_ac_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-ac-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming ACRs
                ''',
                'in_ac_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-as-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming ASAs
                ''',
                'in_as_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-as-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming ASRs
                ''',
                'in_as_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-cc-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming CCAs
                ''',
                'in_cc_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-cc-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming CCRs
                ''',
                'in_cc_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-ce-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming CEAs
                ''',
                'in_ce_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-ce-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming CERs
                ''',
                'in_ce_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-dp-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming DPAs
                ''',
                'in_dp_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-dp-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming DPRs
                ''',
                'in_dp_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-dw-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming DWAs
                ''',
                'in_dw_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-dw-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming DWRs
                ''',
                'in_dw_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-ra-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming RAAs
                ''',
                'in_ra_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-ra-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming RARs
                ''',
                'in_ra_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-st-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming STAs
                ''',
                'in_st_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('in-st-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming STRs
                ''',
                'in_st_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('last-disconnect-cause', REFERENCE_ENUM_CLASS, 'DisconnectCauseEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'DisconnectCauseEnum', 
                [], [], 
                '''                Last Disconnect Reason
                ''',
                'last_disconnect_cause',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('malformed-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Malformed Requests
                ''',
                'malformed_requests',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-aa-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing AARs
                ''',
                'out_aa_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-ac-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing ACAs
                ''',
                'out_ac_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-ac-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing ACRs
                ''',
                'out_ac_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-as-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing ASAs
                ''',
                'out_as_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-as-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing ASRs
                ''',
                'out_as_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-cc-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing CCAs
                ''',
                'out_cc_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-cc-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing CCRs
                ''',
                'out_cc_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-ce-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing CEAs
                ''',
                'out_ce_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-ce-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing CERs
                ''',
                'out_ce_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-dp-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing DPAs
                ''',
                'out_dp_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-dp-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing DPRs
                ''',
                'out_dp_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-dw-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing DWAs
                ''',
                'out_dw_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-dw-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing DWRs
                ''',
                'out_dw_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-ra-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing RAAs
                ''',
                'out_ra_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-ra-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing RARs
                ''',
                'out_ra_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-st-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing STAs
                ''',
                'out_st_as',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('out-st-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing STRs
                ''',
                'out_st_rs',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('peer-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peer Index
                ''',
                'peer_index',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('peer-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer Name
                ''',
                'peer_name',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('peer-type', REFERENCE_ENUM_CLASS, 'PeerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'PeerEnum', 
                [], [], 
                '''                Peer Type
                ''',
                'peer_type',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port number on which the peeris running
                ''',
                'port',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('port-connect', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Connection port
                ''',
                'port_connect',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('protocol-type', REFERENCE_ENUM_CLASS, 'ProtocolTypeValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'ProtocolTypeValueEnum', 
                [], [], 
                '''                Protocol Type
                ''',
                'protocol_type',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('received-permanent-fails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Permanent Failures Received
                ''',
                'received_permanent_fails',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('received-proto-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol Error Received
                ''',
                'received_proto_errors',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('received-transient-fails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transient failures Received
                ''',
                'received_transient_fails',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('security-type', REFERENCE_ENUM_CLASS, 'SecurityTypeValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'SecurityTypeValueEnum', 
                [], [], 
                '''                Security type used to transport
                ''',
                'security_type',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('sent-permanent-fails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Permanent Failures Sent
                ''',
                'sent_permanent_fails',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('sent-proto-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol Error Sent
                ''',
                'sent_proto_errors',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('sent-transient-fails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transient failures Sent
                ''',
                'sent_transient_fails',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PeerStateValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'PeerStateValueEnum', 
                [], [], 
                '''                Peer Connection Status
                ''',
                'state',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('state-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State Duration in seconds
                ''',
                'state_duration',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('transaction-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transaction timer in seconds
                ''',
                'transaction_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('transport-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transport Down
                ''',
                'transport_down',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vrf Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('watchdog-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Watch dog timer in seconds
                ''',
                'watchdog_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('who-init-disconnect', REFERENCE_ENUM_CLASS, 'WhoInitiatedDisconnectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_diameter_oper', 'WhoInitiatedDisconnectEnum', 
                [], [], 
                '''                Who Initiated Disconnect
                ''',
                'who_init_disconnect',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.Peers' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Peers',
            False, 
            [
            _MetaInfoClassMember('conn-retry-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Connection retry timer in seconds
                ''',
                'conn_retry_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('origin-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Origin Host
                ''',
                'origin_host',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('origin-realm', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Origin Realm
                ''',
                'origin_realm',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.Peers.Peer', 
                [], [], 
                '''                Peer List
                ''',
                'peer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Interface
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('tls-trustpoint', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TLS Trustpoint
                ''',
                'tls_trustpoint',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('trans-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of transactions
                ''',
                'trans_max',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('trans-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of transactions
                ''',
                'trans_total',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('transaction-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transaction timer in seconds
                ''',
                'transaction_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('watchdog-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Watch dog timer in seconds
                ''',
                'watchdog_timer',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.Nas.ListOfNas' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Nas.ListOfNas',
            False, 
            [
            _MetaInfoClassMember('aaa-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA session id
                ''',
                'aaa_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-intrim-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting intrim packet response in
                ''',
                'accounting_intrim_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-intrim-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting intrim requests packets out
                ''',
                'accounting_intrim_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter ACR status start
                ''',
                'accounting_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-status-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter ACR status stop
                ''',
                'accounting_status_stop',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authentication-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter AAR status
                ''',
                'authentication_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter AAR status
                ''',
                'authorization_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('diameter-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diameter session id
                ''',
                'diameter_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter STR status
                ''',
                'disconnect_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('method-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Method list used for authentication
                ''',
                'method_list',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('server-used-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Server used for authentication
                ''',
                'server_used_list',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'list-of-nas',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.Nas' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Nas',
            False, 
            [
            _MetaInfoClassMember('aaanas-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA NAS id
                ''',
                'aaanas_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('list-of-nas', REFERENCE_LIST, 'ListOfNas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.Nas.ListOfNas', 
                [], [], 
                '''                List of NAS Entries
                ''',
                'list_of_nas',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'nas',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.NasSummary' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.NasSummary',
            False, 
            [
            _MetaInfoClassMember('accounting-interim-failed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting interim response with failure
                ''',
                'accounting_interim_failed_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-interim-request-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting Interim request from cleint
                ''',
                'accounting_interim_request_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-interim-request-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting interim requests packets out
                ''',
                'accounting_interim_request_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-interim-response-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting interim response frwd to client
                ''',
                'accounting_interim_response_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-interim-success-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting interim response with success
                ''',
                'accounting_interim_success_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-intrim-response-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting interim packet response in
                ''',
                'accounting_intrim_response_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-request-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting requests packets out
                ''',
                'accounting_request_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-response-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting packet response in
                ''',
                'accounting_response_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-start-failed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting start response with failure
                ''',
                'accounting_start_failed_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-start-request-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting start request from cleint
                ''',
                'accounting_start_request_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-start-response-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting start response forward to client
                ''',
                'accounting_start_response_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-start-success-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting start response with success
                ''',
                'accounting_start_success_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-stop-failed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting stop response with failure
                ''',
                'accounting_stop_failed_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-stop-request-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Acct stop request from cleint
                ''',
                'accounting_stop_request_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-stop-request-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting stop requests packets out
                ''',
                'accounting_stop_request_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-stop-response-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting stop packet response in
                ''',
                'accounting_stop_response_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-stop-response-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Acct stop response forward to client
                ''',
                'accounting_stop_response_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-stop-success-response-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting stop response with success
                ''',
                'accounting_stop_success_response_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authen-request-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication request from client
                ''',
                'authen_request_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authen-request-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication request pkt out
                ''',
                'authen_request_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authen-response-fail-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication response with failure
                ''',
                'authen_response_fail_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authen-response-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication response pkt in
                ''',
                'authen_response_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authen-response-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication response frwd to client
                ''',
                'authen_response_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authen-success-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication response with success
                ''',
                'authen_success_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authorization response packet in
                ''',
                'authorization_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authorization request packet out
                ''',
                'authorization_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-request-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authourization request from cleint
                ''',
                'authorization_request_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-response-fail-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication response with failure
                ''',
                'authorization_response_fail_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-response-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authourization response frwd to client
                ''',
                'authorization_response_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-response-success-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication response with success
                ''',
                'authorization_response_success_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('coa-failed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COA response with failure
                ''',
                'coa_failed_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('coa-request-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COA/RAR Request packet in
                ''',
                'coa_request_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('coa-request-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COA request from client
                ''',
                'coa_request_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('coa-response-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COA/RAR Response packet out
                ''',
                'coa_response_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('coa-response-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COA response forward to client
                ''',
                'coa_response_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('coa-success-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COA response with success
                ''',
                'coa_success_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-failed-response-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnect response with failure
                ''',
                'disconnect_failed_response_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-request-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnect request from cleint
                ''',
                'disconnect_request_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-request-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnect request pkt out
                ''',
                'disconnect_request_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-response-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnect response packets in
                ''',
                'disconnect_response_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-response-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnect response forward to client
                ''',
                'disconnect_response_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-success-response-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnect response with success
                ''',
                'disconnect_success_response_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('pod-failed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                POD response with failure
                ''',
                'pod_failed_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('pod-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                POD/RAR Request packets in
                ''',
                'pod_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('pod-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PAD/RAR Response packets out
                ''',
                'pod_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('pod-request-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                POD request from cleint
                ''',
                'pod_request_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('pod-response-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                POD response forward to client
                ''',
                'pod_response_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('pod-success-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                POD response with success
                ''',
                'pod_success_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'nas-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.GySessionIds.GySessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.GySessionIds.GySessionId',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session Id
                ''',
                'session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', True),
            _MetaInfoClassMember('aaa-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AAA session id
                ''',
                'aaa_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('diameter-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diameter session id
                ''',
                'diameter_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('parent-aaa-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AAA Parent session id
                ''',
                'parent_aaa_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('request-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Number
                ''',
                'request_number',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('request-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Request Type
                ''',
                'request_type',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Gy Retry count
                ''',
                'retry_count',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('session-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gy-session-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.GySessionIds' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.GySessionIds',
            False, 
            [
            _MetaInfoClassMember('gy-session-id', REFERENCE_LIST, 'GySessionId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.GySessionIds.GySessionId', 
                [], [], 
                '''                Diameter Gy Session data
                ''',
                'gy_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gy-session-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.GyStatistics' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.GyStatistics',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Active Sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asa-sent-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASA Sent Messages Error
                ''',
                'asa_sent_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asa-sent-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASA Sent Messages
                ''',
                'asa_sent_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asr-received-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASR Received Messages Error
                ''',
                'asr_received_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('asr-received-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASR Received Messages
                ''',
                'asr_received_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-final-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Final Messages Error
                ''',
                'cca_final_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-final-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Final Messages
                ''',
                'cca_final_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-init-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Initial Messages Error
                ''',
                'cca_init_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-init-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Initial Messages
                ''',
                'cca_init_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-update-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Update Messages Error
                ''',
                'cca_update_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('cca-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCA Update Messages
                ''',
                'cca_update_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-failed-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages Failed
                ''',
                'ccr_final_failed_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages
                ''',
                'ccr_final_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-retry-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages retry
                ''',
                'ccr_final_retry_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-final-timed-out-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Final Messages Timed Out
                ''',
                'ccr_final_timed_out_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-failed-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages Failed
                ''',
                'ccr_init_failed_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages
                ''',
                'ccr_init_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-retry-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages retry
                ''',
                'ccr_init_retry_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-init-timed-out-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Initial Messages Timed Out
                ''',
                'ccr_init_timed_out_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-failed-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages Failed
                ''',
                'ccr_update_failed_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages
                ''',
                'ccr_update_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-retry-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages retry
                ''',
                'ccr_update_retry_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('ccr-update-timed-out-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCR Update Messages Timed Out
                ''',
                'ccr_update_timed_out_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('close-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Closed Sessions
                ''',
                'close_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('open-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Opened Sessions
                ''',
                'open_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('raa-sent-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAA Sent Messages Error
                ''',
                'raa_sent_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('raa-sent-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAA Sent Messages
                ''',
                'raa_sent_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('rar-received-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAR Received Messages Error
                ''',
                'rar_received_error_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('rar-received-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RAR Received Messages
                ''',
                'rar_received_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('restore-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Restore Sessions
                ''',
                'restore_sessions',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('unknown-request-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown Request Messages
                ''',
                'unknown_request_messages',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gy-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.GxSessionIds.GxSessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.GxSessionIds.GxSessionId',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session Id
                ''',
                'session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', True),
            _MetaInfoClassMember('aaa-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AAA session id
                ''',
                'aaa_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('diameter-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diameter session id
                ''',
                'diameter_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('request-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Number
                ''',
                'request_number',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('request-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Request Type
                ''',
                'request_type',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Gx Retry count
                ''',
                'retry_count',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('session-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gx-session-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.GxSessionIds' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.GxSessionIds',
            False, 
            [
            _MetaInfoClassMember('gx-session-id', REFERENCE_LIST, 'GxSessionId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.GxSessionIds.GxSessionId', 
                [], [], 
                '''                Diameter Gx Session data
                ''',
                'gx_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'gx-session-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.NasSession.ListOfNas' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.NasSession.ListOfNas',
            False, 
            [
            _MetaInfoClassMember('aaa-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA session id
                ''',
                'aaa_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-intrim-in-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting intrim packet response in
                ''',
                'accounting_intrim_in_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-intrim-out-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting intrim requests packets out
                ''',
                'accounting_intrim_out_packets',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter ACR status start
                ''',
                'accounting_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('accounting-status-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter ACR status stop
                ''',
                'accounting_status_stop',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authentication-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter AAR status
                ''',
                'authentication_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('authorization-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter AAR status
                ''',
                'authorization_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('diameter-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diameter session id
                ''',
                'diameter_session_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('disconnect-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diameter STR status
                ''',
                'disconnect_status',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('method-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Method list used for authentication
                ''',
                'method_list',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('server-used-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Server used for authentication
                ''',
                'server_used_list',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'list-of-nas',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter.NasSession' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.NasSession',
            False, 
            [
            _MetaInfoClassMember('aaanas-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA NAS id
                ''',
                'aaanas_id',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('list-of-nas', REFERENCE_LIST, 'ListOfNas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.NasSession.ListOfNas', 
                [], [], 
                '''                List of NAS Entries
                ''',
                'list_of_nas',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'nas-session',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Diameter' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter',
            False, 
            [
            _MetaInfoClassMember('gx', REFERENCE_CLASS, 'Gx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.Gx', 
                [], [], 
                '''                Diameter global gx data
                ''',
                'gx',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('gx-session-ids', REFERENCE_CLASS, 'GxSessionIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.GxSessionIds', 
                [], [], 
                '''                Diameter Gx Session data list
                ''',
                'gx_session_ids',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('gx-statistics', REFERENCE_CLASS, 'GxStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.GxStatistics', 
                [], [], 
                '''                Diameter Gx Statistics data
                ''',
                'gx_statistics',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('gy', REFERENCE_CLASS, 'Gy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.Gy', 
                [], [], 
                '''                Diameter global gy data
                ''',
                'gy',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('gy-session-ids', REFERENCE_CLASS, 'GySessionIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.GySessionIds', 
                [], [], 
                '''                Diameter Gy Session data list
                ''',
                'gy_session_ids',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('gy-statistics', REFERENCE_CLASS, 'GyStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.GyStatistics', 
                [], [], 
                '''                Diameter Gy Statistics data
                ''',
                'gy_statistics',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('nas', REFERENCE_CLASS, 'Nas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.Nas', 
                [], [], 
                '''                Diameter NAS data
                ''',
                'nas',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('nas-session', REFERENCE_CLASS, 'NasSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.NasSession', 
                [], [], 
                '''                Diameter Nas Session data
                ''',
                'nas_session',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('nas-summary', REFERENCE_CLASS, 'NasSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.NasSummary', 
                [], [], 
                '''                Diameter NAS summary
                ''',
                'nas_summary',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter.Peers', 
                [], [], 
                '''                Diameter peer global data
                ''',
                'peers',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-oper',
            'diameter',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('aborts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of requests aborted
                ''',
                'aborts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-accepts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access accepts
                ''',
                'access_accepts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-challenges', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access challenges
                ''',
                'access_challenges',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-rejects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access rejects
                ''',
                'access_rejects',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-request-retransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retransmitted                         
                access requests
                ''',
                'access_request_retransmits',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access requests
                ''',
                'access_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access packets timed-out
                ''',
                'access_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting port
                ''',
                'accounting_port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting requests
                ''',
                'accounting_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting responses
                ''',
                'accounting_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-retransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retransmitted                         
                accounting requests
                ''',
                'accounting_retransmits',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round-trip time for accounting                  
                in milliseconds
                ''',
                'accounting_rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting packets                    
                timed-out
                ''',
                'accounting_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of incorrect accounting responses
                ''',
                'acct_incorrect_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-response-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average response time for authentication
                requests
                ''',
                'acct_response_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-server-error-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of server error accounting responses
                ''',
                'acct_server_error_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-transaction-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed authentication transactions
                ''',
                'acct_transaction_failure',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-transaction-successess', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of succeeded authentication transactions
                ''',
                'acct_transaction_successess',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-unexpected-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unexpected accounting responses
                ''',
                'acct_unexpected_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of incorrect authentication responses
                ''',
                'authen_incorrect_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-response-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average response time for authentication
                requests
                ''',
                'authen_response_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-server-error-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of server error authentication responses
                ''',
                'authen_server_error_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-transaction-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed authentication transactions
                ''',
                'authen_transaction_failure',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-transaction-successess', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of succeeded authentication transactions
                ''',
                'authen_transaction_successess',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-unexpected-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unexpected authentication responses
                ''',
                'authen_unexpected_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication port
                ''',
                'authentication_port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication-rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round-trip time for authentication              
                in milliseconds
                ''',
                'authentication_rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of incorrect authorization responses
                ''',
                'author_incorrect_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-request-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access packets timed out
                ''',
                'author_request_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access requests
                ''',
                'author_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-response-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average response time for authorization requests
                ''',
                'author_response_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-server-error-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of server error authorization responses
                ''',
                'author_server_error_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-transaction-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed authorization transactions
                ''',
                'author_transaction_failure',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-transaction-successess', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of succeeded authorization transactions
                ''',
                'author_transaction_successess',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-unexpected-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unexpected authorization responses
                ''',
                'author_unexpected_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-access-authenticators', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad access authenticators
                ''',
                'bad_access_authenticators',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-access-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad access responses
                ''',
                'bad_access_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-accounting-authenticators', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad accounting                        
                authenticators
                ''',
                'bad_accounting_authenticators',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-accounting-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad accounting responses
                ''',
                'bad_accounting_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('current-state-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Elapsed time the server has been in             
                current state
                ''',
                'current_state_duration',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('currently-throttled-access-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of currently throttled access reqs
                ''',
                'currently_throttled_access_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dead-detect-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per-server dead-detect time in seconds
                ''',
                'dead_detect_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dead-detect-tries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per-server dead-detect tries
                ''',
                'dead_detect_tries',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dead-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per-server deadtime in minutes
                ''',
                'dead_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dropped-access-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access responses dropped
                ''',
                'dropped_access_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dropped-accounting-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting responses                  
                dropped
                ''',
                'dropped_accounting_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address Family
                ''',
                'family',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Server group name for private server
                ''',
                'group_name',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of RADIUS server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
                ]),
            _MetaInfoClassMember('ip-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address buffer
                ''',
                'ip_address_xr',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of RADIUS server
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('is-a-private-server', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is a private server
                ''',
                'is_a_private_server',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('is-quarantined', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                flag to indicate Server is quarantined          
                or not (Automated TEST in progress)
                ''',
                'is_quarantined',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('last-deadtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of Server being in DEAD state,             
                after last UP
                ''',
                'last_deadtime',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('max-acct-throttled', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max throttled acct transactions
                ''',
                'max_acct_throttled',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('max-throttled-access-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max throttled access reqs
                ''',
                'max_throttled_access_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('packets-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of incoming packets read
                ''',
                'packets_in',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('packets-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of outgoing packets sent
                ''',
                'packets_out',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-access-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending access requests
                ''',
                'pending_access_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-accounting-requets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending accounting requests
                ''',
                'pending_accounting_requets',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('previous-state-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Elapsed time the server was been in             
                previous state
                ''',
                'previous_state_duration',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A number that indicates the priority            
                of the server
                ''',
                'priority',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('redirected-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of requests redirected
                ''',
                'redirected_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('replies-expected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of replies expected to arrive
                ''',
                'replies_expected',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('retransmit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per-server retransmit
                ''',
                'retransmit',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                State of the server UP/DOWN
                ''',
                'state',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-access-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of throttled access reqs stats
                ''',
                'throttled_access_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-acct-failures-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of acct discarded transaction
                ''',
                'throttled_acct_failures_stats',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-acct-timed-out-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of acct transaction that is throttled is
                timedout
                ''',
                'throttled_acct_timed_out_stats',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-acct-transactions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of throttled acct transactions stats
                ''',
                'throttled_acct_transactions',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-dropped-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of discarded access reqs
                ''',
                'throttled_dropped_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-timed-out-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of access reqs that is throttled is timedout
                ''',
                'throttled_timed_out_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttleda-acct-transactions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No of currently throttled acct transactions
                ''',
                'throttleda_acct_transactions',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('timeout-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per-server timeout in seconds
                ''',
                'timeout_xr',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of packets timed-out
                ''',
                'timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-deadtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total time of Server being in DEAD              
                state
                ''',
                'total_deadtime',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total acct test pending
                ''',
                'total_test_acct_pending',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Total acct test req
                ''',
                'total_test_acct_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-response', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total acct test response
                ''',
                'total_test_acct_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total acct test timeouts
                ''',
                'total_test_acct_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total auth test pending
                ''',
                'total_test_auth_pending',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total auth test request
                ''',
                'total_test_auth_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-response', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total auth test response
                ''',
                'total_test_auth_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total auth test timeouts
                ''',
                'total_test_auth_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-access-types', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with unknown         
                type from authentication server
                ''',
                'unknown_access_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-accounting-types', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with unknown         
                type from accounting server
                ''',
                'unknown_accounting_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.Servers.Server', 
                [], [], 
                '''                RADIUS Server
                ''',
                'server',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the source interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('ipaddrv4', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                IP address buffer
                ''',
                'ipaddrv4',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('ipaddrv6', ATTRIBUTE, 'str' , None, None, 
                [(0, 46)], [], 
                '''                IP address buffer
                ''',
                'ipaddrv6',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('vrfid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF Id
                ''',
                'vrfid',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'list-of-source-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.RadiusSourceInterface' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusSourceInterface',
            False, 
            [
            _MetaInfoClassMember('list-of-source-interface', REFERENCE_LIST, 'ListOfSourceInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface', 
                [], [], 
                '''                List of source interfaces
                ''',
                'list_of_source_interface',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'radius-source-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.Global_' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Global_',
            False, 
            [
            _MetaInfoClassMember('accounting-nas-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NAS-Identifier of the RADIUSaccounting client
                ''',
                'accounting_nas_id',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication-nas-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NAS-Identifier of the RADIUSauthentication
                client
                ''',
                'authentication_nas_id',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-accounting-response', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of RADIUS Accounting-Responsepackets
                received from unknownaddresses
                ''',
                'unknown_accounting_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-authentication-response', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of RADIUS Access-Responsepackets received
                from unknownaddresses
                ''',
                'unknown_authentication_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.Global_', 
                [], [], 
                '''                RADIUS Client Information
                ''',
                'global_',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('radius-source-interface', REFERENCE_CLASS, 'RadiusSourceInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.RadiusSourceInterface', 
                [], [], 
                '''                RADIUS source interfaces
                ''',
                'radius_source_interface',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.Servers', 
                [], [], 
                '''                List of RADIUS servers configured
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'radius',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.Requests.Request.TacacsRequestbag' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Requests.Request.TacacsRequestbag',
            False, 
            [
            _MetaInfoClassMember('bytes-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                bytes read from socket
                ''',
                'bytes_in',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('bytes-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                bytes written
                ''',
                'bytes_out',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('in-pak-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                size of the packet to be received
                ''',
                'in_pak_size',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('out-pak-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                size of the packet to be sent
                ''',
                'out_pak_size',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('pak-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                the type of packet
                ''',
                'pak_type',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                same as in pkt hdr
                ''',
                'session_id',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('sock', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                socket number
                ''',
                'sock',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                time remaining for this request
                ''',
                'time_remaining',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'tacacs-requestbag',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.Requests.Request' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Requests.Request',
            False, 
            [
            _MetaInfoClassMember('tacacs-requestbag', REFERENCE_LIST, 'TacacsRequestbag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.Requests.Request.TacacsRequestbag', 
                [], [], 
                '''                tacacs requestbag
                ''',
                'tacacs_requestbag',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.Requests' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Requests',
            False, 
            [
            _MetaInfoClassMember('request', REFERENCE_LIST, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.Requests.Request', 
                [], [], 
                '''                request
                ''',
                'request',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'requests',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('aborts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                abort count
                ''',
                'aborts',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                internet address of T+ server
                ''',
                'addr',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('addr-buf', ATTRIBUTE, 'str' , None, None, 
                [(0, 46)], [], 
                '''                IP address buffer
                ''',
                'addr_buf',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('bytes-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of bytes read
                ''',
                'bytes_in',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('bytes-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of bytes out
                ''',
                'bytes_out',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('closes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                socket closes
                ''',
                'closes',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('conn-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is the server connected ?
                ''',
                'conn_up',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                error count
                ''',
                'errors',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                IP address Family
                ''',
                'family',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('is-private', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is this a private server ?
                ''',
                'is_private',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('opens', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                socket opens
                ''',
                'opens',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('paks-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of incoming packets read
                ''',
                'paks_in',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('paks-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of outgoing packets sent
                ''',
                'paks_out',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                per server port to use
                ''',
                'port',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('replies-expected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of replies expected to arrive
                ''',
                'replies_expected',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('single-connect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is this a single connect server ?
                ''',
                'single_connect',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                per-server timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is the server UP or down ?
                ''',
                'up',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF in which server is reachable
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.Servers.Server', 
                [], [], 
                '''                server
                ''',
                'server',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.ServerGroups.ServerGroup.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.ServerGroups.ServerGroup.Server',
            False, 
            [
            _MetaInfoClassMember('aborts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                abort count
                ''',
                'aborts',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                internet address of T+ server
                ''',
                'addr',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('addr-buf', ATTRIBUTE, 'str' , None, None, 
                [(0, 46)], [], 
                '''                IP address buffer
                ''',
                'addr_buf',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('bytes-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of bytes read
                ''',
                'bytes_in',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('bytes-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of bytes out
                ''',
                'bytes_out',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('closes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                socket closes
                ''',
                'closes',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('conn-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is the server connected ?
                ''',
                'conn_up',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                error count
                ''',
                'errors',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                IP address Family
                ''',
                'family',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('is-private', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is this a private server ?
                ''',
                'is_private',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('opens', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                socket opens
                ''',
                'opens',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('paks-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of incoming packets read
                ''',
                'paks_in',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('paks-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of outgoing packets sent
                ''',
                'paks_out',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                per server port to use
                ''',
                'port',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('replies-expected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                # of replies expected to arrive
                ''',
                'replies_expected',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('single-connect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is this a single connect server ?
                ''',
                'single_connect',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                per-server timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is the server UP or down ?
                ''',
                'up',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF in which server is reachable
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.ServerGroups.ServerGroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.ServerGroups.ServerGroup',
            False, 
            [
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name of the server group
                ''',
                'group_name',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.ServerGroups.ServerGroup.Server', 
                [], [], 
                '''                list of servers in this group
                ''',
                'server',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('sg-map-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                server group mapped number
                ''',
                'sg_map_num',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                vrf of the group
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'server-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs.ServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.ServerGroups',
            False, 
            [
            _MetaInfoClassMember('server-group', REFERENCE_LIST, 'ServerGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.ServerGroups.ServerGroup', 
                [], [], 
                '''                server group
                ''',
                'server_group',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Tacacs' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs',
            False, 
            [
            _MetaInfoClassMember('requests', REFERENCE_CLASS, 'Requests' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.Requests', 
                [], [], 
                '''                TACACS Active Request List
                ''',
                'requests',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('server-groups', REFERENCE_CLASS, 'ServerGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.ServerGroups', 
                [], [], 
                '''                TACACS sg Information
                ''',
                'server_groups',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs.Servers', 
                [], [], 
                '''                TACACS server Information
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-oper',
            'tacacs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa' : {
        'meta_info' : _MetaInfoClass('Aaa',
            False, 
            [
            _MetaInfoClassMember('all-tasks', REFERENCE_CLASS, 'AllTasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.AllTasks', 
                [], [], 
                '''                All tasks supported by system
                ''',
                'all_tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('authen-method', REFERENCE_CLASS, 'AuthenMethod' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.AuthenMethod', 
                [], [], 
                '''                Current users authentication method
                ''',
                'authen_method',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('current-usergroup', REFERENCE_CLASS, 'CurrentUsergroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.CurrentUsergroup', 
                [], [], 
                '''                Specific Usergroup Information
                ''',
                'current_usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('currentuser-detail', REFERENCE_CLASS, 'CurrentuserDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.CurrentuserDetail', 
                [], [], 
                '''                Current user specific details
                ''',
                'currentuser_detail',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('diameter', REFERENCE_CLASS, 'Diameter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Diameter', 
                [], [], 
                '''                Diameter operational data
                ''',
                'diameter',
                'Cisco-IOS-XR-aaa-diameter-oper', False),
            _MetaInfoClassMember('radius', REFERENCE_CLASS, 'Radius' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius', 
                [], [], 
                '''                RADIUS operational data
                ''',
                'radius',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('tacacs', REFERENCE_CLASS, 'Tacacs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Tacacs', 
                [], [], 
                '''                TACACS operational data
                ''',
                'tacacs',
                'Cisco-IOS-XR-aaa-tacacs-oper', False),
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.TaskMap', 
                [], [], 
                '''                Task map of current user
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskgroups', REFERENCE_CLASS, 'Taskgroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups', 
                [], [], 
                '''                Individual taskgroups container
                ''',
                'taskgroups',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('usergroups', REFERENCE_CLASS, 'Usergroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups', 
                [], [], 
                '''                Container for individual usergroup Information
                ''',
                'usergroups',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('users', REFERENCE_CLASS, 'Users' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users', 
                [], [], 
                '''                Container for individual local user information
                ''',
                'users',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
}
_meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup.TaskMap']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.TaskMap']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info'].parent =_meta_table['Aaa.Taskgroups']['meta_info']
_meta_table['Aaa.Users.User.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Users.User.TaskMap']['meta_info']
_meta_table['Aaa.Users.User.TaskMap']['meta_info'].parent =_meta_table['Aaa.Users.User']['meta_info']
_meta_table['Aaa.Users.User']['meta_info'].parent =_meta_table['Aaa.Users']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.TaskMap']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.TaskMap']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup']['meta_info'].parent =_meta_table['Aaa.Usergroups']['meta_info']
_meta_table['Aaa.Diameter.Peers.Peer']['meta_info'].parent =_meta_table['Aaa.Diameter.Peers']['meta_info']
_meta_table['Aaa.Diameter.Nas.ListOfNas']['meta_info'].parent =_meta_table['Aaa.Diameter.Nas']['meta_info']
_meta_table['Aaa.Diameter.GySessionIds.GySessionId']['meta_info'].parent =_meta_table['Aaa.Diameter.GySessionIds']['meta_info']
_meta_table['Aaa.Diameter.GxSessionIds.GxSessionId']['meta_info'].parent =_meta_table['Aaa.Diameter.GxSessionIds']['meta_info']
_meta_table['Aaa.Diameter.NasSession.ListOfNas']['meta_info'].parent =_meta_table['Aaa.Diameter.NasSession']['meta_info']
_meta_table['Aaa.Diameter.Gy']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.GxStatistics']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Gx']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Peers']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Nas']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.NasSummary']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.GySessionIds']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.GyStatistics']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.GxSessionIds']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.NasSession']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Radius.Servers.Server']['meta_info'].parent =_meta_table['Aaa.Radius.Servers']['meta_info']
_meta_table['Aaa.Radius.RadiusSourceInterface.ListOfSourceInterface']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusSourceInterface']['meta_info']
_meta_table['Aaa.Radius.Servers']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.RadiusSourceInterface']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Global_']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Tacacs.Requests.Request.TacacsRequestbag']['meta_info'].parent =_meta_table['Aaa.Tacacs.Requests.Request']['meta_info']
_meta_table['Aaa.Tacacs.Requests.Request']['meta_info'].parent =_meta_table['Aaa.Tacacs.Requests']['meta_info']
_meta_table['Aaa.Tacacs.Servers.Server']['meta_info'].parent =_meta_table['Aaa.Tacacs.Servers']['meta_info']
_meta_table['Aaa.Tacacs.ServerGroups.ServerGroup.Server']['meta_info'].parent =_meta_table['Aaa.Tacacs.ServerGroups.ServerGroup']['meta_info']
_meta_table['Aaa.Tacacs.ServerGroups.ServerGroup']['meta_info'].parent =_meta_table['Aaa.Tacacs.ServerGroups']['meta_info']
_meta_table['Aaa.Tacacs.Requests']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.Servers']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.ServerGroups']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.AllTasks']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.CurrentuserDetail']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.TaskMap']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Taskgroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Users']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Usergroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.AuthenMethod']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.CurrentUsergroup']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Diameter']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Radius']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Tacacs']['meta_info'].parent =_meta_table['Aaa']['meta_info']
