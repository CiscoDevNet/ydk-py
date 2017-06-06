


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EventManagerPolicyModeEnum' : _MetaInfoEnum('EventManagerPolicyModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        {
            'cisco':'cisco',
            'trust':'trust',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManagerChecksumEnum' : _MetaInfoEnum('EventManagerChecksumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        {
            'sha-1':'sha_1',
            'md5':'md5',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManagerPolicySecEnum' : _MetaInfoEnum('EventManagerPolicySecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        {
            'rsa-2048':'rsa_2048',
            'trust':'trust',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManagerPolicyEnum' : _MetaInfoEnum('EventManagerPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg',
        {
            'system':'system',
            'user':'user',
        }, 'Cisco-IOS-XR-ha-eem-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg']),
    'EventManager.Policies.Policy' : {
        'meta_info' : _MetaInfoClass('EventManager.Policies.Policy',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the policy file
                ''',
                'policy_name',
                'Cisco-IOS-XR-ha-eem-cfg', True),
            _MetaInfoClassMember('check-sum-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CheckSum Value
                ''',
                'check_sum_value',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('checksum-type', REFERENCE_ENUM_CLASS, 'EventManagerChecksumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerChecksumEnum', 
                [], [], 
                '''                Specify Embedded Event Manager policy checksum
                ''',
                'checksum_type',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('persist-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time of validity (in seconds) for cached AAA
                taskmap of username (default is 3600)
                ''',
                'persist_time',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('policy-security-level', REFERENCE_ENUM_CLASS, 'EventManagerPolicySecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicySecEnum', 
                [], [], 
                '''                Event Manager policy security Level
                ''',
                'policy_security_level',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('policy-security-mode', REFERENCE_ENUM_CLASS, 'EventManagerPolicyModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicyModeEnum', 
                [], [], 
                '''                Specify Embedded Event Manager policy security
                mode
                ''',
                'policy_security_mode',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('policy-type', REFERENCE_ENUM_CLASS, 'EventManagerPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManagerPolicyEnum', 
                [], [], 
                '''                Event manager type of this policy
                ''',
                'policy_type',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A configured username
                ''',
                'username',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
    'EventManager.Policies' : {
        'meta_info' : _MetaInfoClass('EventManager.Policies',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_LIST, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Policies.Policy', 
                [], [], 
                '''                Name of the policy file
                ''',
                'policy',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'policies',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
    'EventManager.SchedulerScript.ThreadClasses.ThreadClass' : {
        'meta_info' : _MetaInfoClass('EventManager.SchedulerScript.ThreadClasses.ThreadClass',
            False, 
            [
            _MetaInfoClassMember('thread-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the global variable
                ''',
                'thread_class_name',
                'Cisco-IOS-XR-ha-eem-cfg', True),
            _MetaInfoClassMember('num-threads', ATTRIBUTE, 'int' , None, None, 
                [('1', '5')], [], 
                '''                number of scheduler threads
                ''',
                'num_threads',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'thread-class',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
    'EventManager.SchedulerScript.ThreadClasses' : {
        'meta_info' : _MetaInfoClass('EventManager.SchedulerScript.ThreadClasses',
            False, 
            [
            _MetaInfoClassMember('thread-class', REFERENCE_LIST, 'ThreadClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.SchedulerScript.ThreadClasses.ThreadClass', 
                [], [], 
                '''                scheduler classs type argument
                ''',
                'thread_class',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'thread-classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
    'EventManager.SchedulerScript' : {
        'meta_info' : _MetaInfoClass('EventManager.SchedulerScript',
            False, 
            [
            _MetaInfoClassMember('thread-classes', REFERENCE_CLASS, 'ThreadClasses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.SchedulerScript.ThreadClasses', 
                [], [], 
                '''                scheduler thread classs 
                ''',
                'thread_classes',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'scheduler-script',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
    'EventManager.Environments.Environment' : {
        'meta_info' : _MetaInfoClass('EventManager.Environments.Environment',
            False, 
            [
            _MetaInfoClassMember('environment-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the global variable
                ''',
                'environment_name',
                'Cisco-IOS-XR-ha-eem-cfg', True),
            _MetaInfoClassMember('environment-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Value of the global variable
                ''',
                'environment_value',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'environment',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
    'EventManager.Environments' : {
        'meta_info' : _MetaInfoClass('EventManager.Environments',
            False, 
            [
            _MetaInfoClassMember('environment', REFERENCE_LIST, 'Environment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Environments.Environment', 
                [], [], 
                '''                Name of the global variable
                ''',
                'environment',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'environments',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
    'EventManager' : {
        'meta_info' : _MetaInfoClass('EventManager',
            False, 
            [
            _MetaInfoClassMember('directory-user-library', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path of the user policy library directory
                ''',
                'directory_user_library',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('directory-user-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set event manager user policy directory
                ''',
                'directory_user_policy',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('environments', REFERENCE_CLASS, 'Environments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Environments', 
                [], [], 
                '''                Set an event manager global variable for event
                manager policies
                ''',
                'environments',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('policies', REFERENCE_CLASS, 'Policies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.Policies', 
                [], [], 
                '''                Register an event manager policy
                ''',
                'policies',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('refresh-time', ATTRIBUTE, 'int' , None, None, 
                [('10', '4294967295')], [], 
                '''                Set refresh time (in seconds) for policy
                username's AAA taskmap
                ''',
                'refresh_time',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('schedule-suspend', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable suspend policy scheduling
                ''',
                'schedule_suspend',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            _MetaInfoClassMember('scheduler-script', REFERENCE_CLASS, 'SchedulerScript' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg', 'EventManager.SchedulerScript', 
                [], [], 
                '''                scheduler classs type
                ''',
                'scheduler_script',
                'Cisco-IOS-XR-ha-eem-cfg', False),
            ],
            'Cisco-IOS-XR-ha-eem-cfg',
            'event-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ha_eem_cfg'
        ),
    },
}
_meta_table['EventManager.Policies.Policy']['meta_info'].parent =_meta_table['EventManager.Policies']['meta_info']
_meta_table['EventManager.SchedulerScript.ThreadClasses.ThreadClass']['meta_info'].parent =_meta_table['EventManager.SchedulerScript.ThreadClasses']['meta_info']
_meta_table['EventManager.SchedulerScript.ThreadClasses']['meta_info'].parent =_meta_table['EventManager.SchedulerScript']['meta_info']
_meta_table['EventManager.Environments.Environment']['meta_info'].parent =_meta_table['EventManager.Environments']['meta_info']
_meta_table['EventManager.Policies']['meta_info'].parent =_meta_table['EventManager']['meta_info']
_meta_table['EventManager.SchedulerScript']['meta_info'].parent =_meta_table['EventManager']['meta_info']
_meta_table['EventManager.Environments']['meta_info'].parent =_meta_table['EventManager']['meta_info']
