


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Eem.DirUser.Library' : {
        'meta_info' : _MetaInfoClass('Eem.DirUser.Library',
            False, 
            [
            _MetaInfoClassMember('library', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                library
                ''',
                'library',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy
                ''',
                'policy',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'library',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.DirUser.Policy' : {
        'meta_info' : _MetaInfoClass('Eem.DirUser.Policy',
            False, 
            [
            _MetaInfoClassMember('library', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                library
                ''',
                'library',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy
                ''',
                'policy',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.DirUser' : {
        'meta_info' : _MetaInfoClass('Eem.DirUser',
            False, 
            [
            _MetaInfoClassMember('library', REFERENCE_CLASS, 'Library' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.DirUser.Library', 
                [], [], 
                '''                directory user library
                ''',
                'library',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.DirUser.Policy', 
                [], [], 
                '''                directory user policy
                ''',
                'policy',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'dir-user',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.EnvVariables.EnvVariable' : {
        'meta_info' : _MetaInfoClass('Eem.EnvVariables.EnvVariable',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Environmental variable name
                ''',
                'name',
                'Cisco-IOS-XR-ha-eem-policy-oper', True),
            _MetaInfoClassMember('name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                variable name
                ''',
                'name_xr',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                value
                ''',
                'value',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'env-variable',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.EnvVariables' : {
        'meta_info' : _MetaInfoClass('Eem.EnvVariables',
            False, 
            [
            _MetaInfoClassMember('env-variable', REFERENCE_LIST, 'EnvVariable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.EnvVariables.EnvVariable', 
                [], [], 
                '''                environmental variables name and value 
                ''',
                'env_variable',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'env-variables',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.RefreshTime' : {
        'meta_info' : _MetaInfoClass('Eem.RefreshTime',
            False, 
            [
            _MetaInfoClassMember('refreshtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Event manager refresh-time 
                ''',
                'refreshtime',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'refresh-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.RegPolicies.RegPolicy' : {
        'meta_info' : _MetaInfoClass('Eem.RegPolicies.RegPolicy',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                policy name
                ''',
                'name',
                'Cisco-IOS-XR-ha-eem-policy-oper', True),
            _MetaInfoClassMember('class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class
                ''',
                'class_',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                description
                ''',
                'description',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('event-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                event type
                ''',
                'event_type',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('persist-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PersistTime 
                ''',
                'persist_time',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('time-created', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                time created
                ''',
                'time_created',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('trap', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                trap
                ''',
                'trap',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy type
                ''',
                'type',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                username
                ''',
                'username',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'reg-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.RegPolicies' : {
        'meta_info' : _MetaInfoClass('Eem.RegPolicies',
            False, 
            [
            _MetaInfoClassMember('reg-policy', REFERENCE_LIST, 'RegPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.RegPolicies.RegPolicy', 
                [], [], 
                '''                policy name and create time 
                ''',
                'reg_policy',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'reg-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.AvlPolicies.AvlPolicy' : {
        'meta_info' : _MetaInfoClass('Eem.AvlPolicies.AvlPolicy',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                System policy name
                ''',
                'name',
                'Cisco-IOS-XR-ha-eem-policy-oper', True),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('time-created', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                time created
                ''',
                'time_created',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy type
                ''',
                'type',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'avl-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem.AvlPolicies' : {
        'meta_info' : _MetaInfoClass('Eem.AvlPolicies',
            False, 
            [
            _MetaInfoClassMember('avl-policy', REFERENCE_LIST, 'AvlPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.AvlPolicies.AvlPolicy', 
                [], [], 
                '''                policy name and create time 
                ''',
                'avl_policy',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'avl-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
    'Eem' : {
        'meta_info' : _MetaInfoClass('Eem',
            False, 
            [
            _MetaInfoClassMember('avl-policies', REFERENCE_CLASS, 'AvlPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.AvlPolicies', 
                [], [], 
                '''                list the available policies
                ''',
                'avl_policies',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('dir-user', REFERENCE_CLASS, 'DirUser' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.DirUser', 
                [], [], 
                '''                directory user
                ''',
                'dir_user',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('env-variables', REFERENCE_CLASS, 'EnvVariables' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.EnvVariables', 
                [], [], 
                '''                list of environmental variables
                ''',
                'env_variables',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('refresh-time', REFERENCE_CLASS, 'RefreshTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.RefreshTime', 
                [], [], 
                '''                Refresh time
                ''',
                'refresh_time',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            _MetaInfoClassMember('reg-policies', REFERENCE_CLASS, 'RegPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper', 'Eem.RegPolicies', 
                [], [], 
                '''                list the registered policies
                ''',
                'reg_policies',
                'Cisco-IOS-XR-ha-eem-policy-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-policy-oper',
            'eem',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-policy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_policy_oper'
        ),
    },
}
_meta_table['Eem.DirUser.Library']['meta_info'].parent =_meta_table['Eem.DirUser']['meta_info']
_meta_table['Eem.DirUser.Policy']['meta_info'].parent =_meta_table['Eem.DirUser']['meta_info']
_meta_table['Eem.EnvVariables.EnvVariable']['meta_info'].parent =_meta_table['Eem.EnvVariables']['meta_info']
_meta_table['Eem.RegPolicies.RegPolicy']['meta_info'].parent =_meta_table['Eem.RegPolicies']['meta_info']
_meta_table['Eem.AvlPolicies.AvlPolicy']['meta_info'].parent =_meta_table['Eem.AvlPolicies']['meta_info']
_meta_table['Eem.DirUser']['meta_info'].parent =_meta_table['Eem']['meta_info']
_meta_table['Eem.EnvVariables']['meta_info'].parent =_meta_table['Eem']['meta_info']
_meta_table['Eem.RefreshTime']['meta_info'].parent =_meta_table['Eem']['meta_info']
_meta_table['Eem.RegPolicies']['meta_info'].parent =_meta_table['Eem']['meta_info']
_meta_table['Eem.AvlPolicies']['meta_info'].parent =_meta_table['Eem']['meta_info']
