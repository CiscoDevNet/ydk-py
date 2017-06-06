


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Aaa.Accountings.Accounting' : {
        'meta_info' : _MetaInfoClass('Aaa.Accountings.Accounting',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                exec:Account exec sessions, commands: Account
                CLI commands
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named accounting list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('broadcast', REFERENCE_ENUM_CLASS, 'AaaAccountingBroadcastEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingBroadcastEnum', 
                [], [], 
                '''                Broadcast
                ''',
                'broadcast',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-lib-cfg', False, max_elements=4),
            _MetaInfoClassMember('rp-failover', REFERENCE_ENUM_CLASS, 'AaaAccountingRpFailoverEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingRpFailoverEnum', 
                [], [], 
                '''                rpfailover
                ''',
                'rp_failover',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-lib-cfg', False, max_elements=4),
            _MetaInfoClassMember('type-xr', REFERENCE_ENUM_CLASS, 'AaaAccountingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingEnum', 
                [], [], 
                '''                Stop only/Start Stop
                ''',
                'type_xr',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Accountings' : {
        'meta_info' : _MetaInfoClass('Aaa.Accountings',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_LIST, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Accountings.Accounting', 
                [], [], 
                '''                Configurations related to accounting
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'accountings',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authorizations.Authorization' : {
        'meta_info' : _MetaInfoClass('Aaa.Authorizations.Authorization',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                network: Authorize IKE requests, commands:
                Authorize CLI commands
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                List name for AAA authorization
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Methods
                ''',
                'method',
                'Cisco-IOS-XR-aaa-lib-cfg', False, max_elements=4, min_elements=1),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-lib-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authorizations' : {
        'meta_info' : _MetaInfoClass('Aaa.Authorizations',
            False, 
            [
            _MetaInfoClassMember('authorization', REFERENCE_LIST, 'Authorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authorizations.Authorization', 
                [], [], 
                '''                Configurations related to authorization
                ''',
                'authorization',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'authorizations',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AccountingUpdate' : {
        'meta_info' : _MetaInfoClass('Aaa.AccountingUpdate',
            False, 
            [
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '35791394')], [], 
                '''                Periodic update interval in minutes
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AaaAccountingUpdateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingUpdateEnum', 
                [], [], 
                '''                newinfo/periodic
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'accounting-update',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Banner' : {
        'meta_info' : _MetaInfoClass('Aaa.Banner',
            False, 
            [
            _MetaInfoClassMember('login', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA login banner
                ''',
                'login',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'banner',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authentications.Authentication' : {
        'meta_info' : _MetaInfoClass('Aaa.Authentications.Authentication',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                login: Authenticate login sessions, ppp:
                Authenticate ppp sessions
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                List name for AAA authentication
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Methods
                ''',
                'method',
                'Cisco-IOS-XR-aaa-lib-cfg', False, max_elements=4, min_elements=1),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-lib-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authentications' : {
        'meta_info' : _MetaInfoClass('Aaa.Authentications',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_LIST, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authentications.Authentication', 
                [], [], 
                '''                Configurations related to authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'authentications',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'(subscriber)|(service)|(policy-if)|(prepaid)|(dot1x)'], 
                '''                Set authorization lists
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named authorization list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4, min_elements=1),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'policy-if-author',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.PolicyIfAuthors' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.PolicyIfAuthors',
            False, 
            [
            _MetaInfoClassMember('policy-if-author', REFERENCE_LIST, 'PolicyIfAuthor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor', 
                [], [], 
                '''                Configurations related to authorization
                ''',
                'policy_if_author',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'policy-if-authors',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.Accountings.Accounting' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.Accountings.Accounting',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'(subscriber)|(service)|(policy-if)|(prepaid)|(dot1x)'], 
                '''                Set accounting lists
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named accounting list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('broadcast', REFERENCE_ENUM_CLASS, 'AaaAccountingBroadcastEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingBroadcastEnum', 
                [], [], 
                '''                Broadcast
                ''',
                'broadcast',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.Accountings' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.Accountings',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_LIST, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.Accountings.Accounting', 
                [], [], 
                '''                Configurations related to accounting
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'accountings',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.ServiceAccounting' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.ServiceAccounting',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AaaServiceAccountingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_aaacore_cfg', 'AaaServiceAccountingEnum', 
                [], [], 
                '''                Send extended/brief service accounting records
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'service-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'(subscriber)|(service)|(policy-if)|(prepaid)|(dot1x)'], 
                '''                Set authorization lists
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named authorization list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4, min_elements=1),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'prepaid-author',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.PrepaidAuthors' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.PrepaidAuthors',
            False, 
            [
            _MetaInfoClassMember('prepaid-author', REFERENCE_LIST, 'PrepaidAuthor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor', 
                [], [], 
                '''                Configurations related to authorization
                ''',
                'prepaid_author',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'prepaid-authors',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.Authorizations.Authorization' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.Authorizations.Authorization',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'(subscriber)|(service)|(policy-if)|(prepaid)|(dot1x)'], 
                '''                Set authorization lists
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named authorization list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4, min_elements=1),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.Authorizations' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.Authorizations',
            False, 
            [
            _MetaInfoClassMember('authorization', REFERENCE_LIST, 'Authorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.Authorizations.Authorization', 
                [], [], 
                '''                Configurations related to authorization
                ''',
                'authorization',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'authorizations',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.Authentications.Authentication' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.Authentications.Authentication',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'(subscriber)|(service)|(policy-if)|(prepaid)|(dot1x)'], 
                '''                Set authentication lists
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named authentication list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4, min_elements=1),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber.Authentications' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber.Authentications',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_LIST, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.Authentications.Authentication', 
                [], [], 
                '''                Configurations related to authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'authentications',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaSubscriber' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaSubscriber',
            False, 
            [
            _MetaInfoClassMember('accountings', REFERENCE_CLASS, 'Accountings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.Accountings', 
                [], [], 
                '''                AAA accounting
                ''',
                'accountings',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('authentications', REFERENCE_CLASS, 'Authentications' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.Authentications', 
                [], [], 
                '''                AAA authentication
                ''',
                'authentications',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('authorizations', REFERENCE_CLASS, 'Authorizations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.Authorizations', 
                [], [], 
                '''                AAA authorization
                ''',
                'authorizations',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('policy-if-authors', REFERENCE_CLASS, 'PolicyIfAuthors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.PolicyIfAuthors', 
                [], [], 
                '''                AAA authorization policy
                ''',
                'policy_if_authors',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('prepaid-authors', REFERENCE_CLASS, 'PrepaidAuthors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.PrepaidAuthors', 
                [], [], 
                '''                AAA authorization prepaid
                ''',
                'prepaid_authors',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('service-accounting', REFERENCE_CLASS, 'ServiceAccounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber.ServiceAccounting', 
                [], [], 
                '''                Set accounting parameters for Service
                ''',
                'service_accounting',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'aaa-subscriber',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaMobile.Mobiles.Mobile' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaMobile.Mobiles.Mobile',
            False, 
            [
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named accounting list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('broadcast', REFERENCE_ENUM_CLASS, 'AaaAccountingBroadcastEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaAccountingBroadcastEnum', 
                [], [], 
                '''                Broadcast
                ''',
                'broadcast',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'mobile',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaMobile.Mobiles' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaMobile.Mobiles',
            False, 
            [
            _MetaInfoClassMember('mobile', REFERENCE_LIST, 'Mobile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaMobile.Mobiles.Mobile', 
                [], [], 
                '''                Configurations related to accounting
                ''',
                'mobile',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'mobiles',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaMobile' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaMobile',
            False, 
            [
            _MetaInfoClassMember('mobiles', REFERENCE_CLASS, 'Mobiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaMobile.Mobiles', 
                [], [], 
                '''                AAA Mobile Accounting
                ''',
                'mobiles',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'aaa-mobile',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaDot1X.Authentications.Authentication' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaDot1X.Authentications.Authentication',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'(subscriber)|(service)|(policy-if)|(prepaid)|(dot1x)'], 
                '''                Set authentication lists
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named authentication list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4, min_elements=1),
            _MetaInfoClassMember('server-group-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Server group names
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False, max_elements=4),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaDot1X.Authentications' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaDot1X.Authentications',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_LIST, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaDot1X.Authentications.Authentication', 
                [], [], 
                '''                Configurations related to authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'authentications',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.AaaDot1X' : {
        'meta_info' : _MetaInfoClass('Aaa.AaaDot1X',
            False, 
            [
            _MetaInfoClassMember('authentications', REFERENCE_CLASS, 'Authentications' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaDot1X.Authentications', 
                [], [], 
                '''                AAA authentication
                ''',
                'authentications',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'aaa-dot1x',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.NasPortId.Formats.Format' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.NasPortId.Formats.Format',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '45')], [], 
                '''                Nas-Port-Type value to apply format name on
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('format-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA nas-port attribute format
                ''',
                'format_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'format',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.NasPortId.Formats' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.NasPortId.Formats',
            False, 
            [
            _MetaInfoClassMember('format', REFERENCE_LIST, 'Format' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.NasPortId.Formats.Format', 
                [], [], 
                '''                nas-port-id attribute format
                ''',
                'format',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'formats',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.NasPortId' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.NasPortId',
            False, 
            [
            _MetaInfoClassMember('formats', REFERENCE_CLASS, 'Formats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.NasPortId.Formats', 
                [], [], 
                '''                AAA nas-port-id attribute format
                ''',
                'formats',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'nas-port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.CallingStation.Formats.Format' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.CallingStation.Formats.Format',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '45')], [], 
                '''                Nas-Port-Type value to apply format name on
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('format-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA nas-port attribute format
                ''',
                'format_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'format',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.CallingStation.Formats' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.CallingStation.Formats',
            False, 
            [
            _MetaInfoClassMember('format', REFERENCE_LIST, 'Format' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.CallingStation.Formats.Format', 
                [], [], 
                '''                nas-port-id attribute format
                ''',
                'format',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'formats',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.CallingStation' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.CallingStation',
            False, 
            [
            _MetaInfoClassMember('formats', REFERENCE_CLASS, 'Formats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.CallingStation.Formats', 
                [], [], 
                '''                AAA nas-port-id attribute format
                ''',
                'formats',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'calling-station',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.CalledStation.Formats.Format' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.CalledStation.Formats.Format',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '45')], [], 
                '''                Nas-Port-Type value to apply format name on
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('format-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AAA nas-port attribute format
                ''',
                'format_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'format',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.CalledStation.Formats' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.CalledStation.Formats',
            False, 
            [
            _MetaInfoClassMember('format', REFERENCE_LIST, 'Format' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.CalledStation.Formats.Format', 
                [], [], 
                '''                nas-port-id attribute format
                ''',
                'format',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'formats',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.CalledStation' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.CalledStation',
            False, 
            [
            _MetaInfoClassMember('formats', REFERENCE_CLASS, 'Formats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.CalledStation.Formats', 
                [], [], 
                '''                AAA nas-port-id attribute format
                ''',
                'formats',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'called-station',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended',
            False, 
            [
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                format type
                ''',
                'value',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '45')], [], 
                '''                AAA nas-port attribute format
                ''',
                'type',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('format-identifier', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                A 32 character string representing the
                format to be used
                ''',
                'format_identifier',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'format-extended',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.NasPort.FormatExtendeds' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.NasPort.FormatExtendeds',
            False, 
            [
            _MetaInfoClassMember('format-extended', REFERENCE_LIST, 'FormatExtended' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended', 
                [], [], 
                '''                nas-port-id extended attribute
                ''',
                'format_extended',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'format-extendeds',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.NasPort' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.NasPort',
            False, 
            [
            _MetaInfoClassMember('format-extendeds', REFERENCE_CLASS, 'FormatExtendeds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.NasPort.FormatExtendeds', 
                [], [], 
                '''                AAA nas-port-id attribute format
                ''',
                'format_extendeds',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'nas-port',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.FormatOthers.FormatOther' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.FormatOthers.FormatOther',
            False, 
            [
            _MetaInfoClassMember('nas-port-type-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Nas-Port-Type value to apply format name on
                ''',
                'nas_port_type_name',
                'Cisco-IOS-XR-aaa-aaacore-cfg', True),
            _MetaInfoClassMember('attribute-config1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument1
                ''',
                'attribute_config1',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config10', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument10
                ''',
                'attribute_config10',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config11', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument11
                ''',
                'attribute_config11',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config12', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument12
                ''',
                'attribute_config12',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config13', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument13
                ''',
                'attribute_config13',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config14', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument14
                ''',
                'attribute_config14',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config15', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument15
                ''',
                'attribute_config15',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config16', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument16
                ''',
                'attribute_config16',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config17', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument17
                ''',
                'attribute_config17',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config18', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument18
                ''',
                'attribute_config18',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config19', ATTRIBUTE, 'int' , None, None, 
                [('1', '253')], [], 
                '''                Argument19
                ''',
                'attribute_config19',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument2
                ''',
                'attribute_config2',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument3
                ''',
                'attribute_config3',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config4', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument4
                ''',
                'attribute_config4',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config5', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument5
                ''',
                'attribute_config5',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config6', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument6
                ''',
                'attribute_config6',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config7', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument7
                ''',
                'attribute_config7',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config8', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument8
                ''',
                'attribute_config8',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('attribute-config9', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Argument9
                ''',
                'attribute_config9',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'format-other',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute.FormatOthers' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute.FormatOthers',
            False, 
            [
            _MetaInfoClassMember('format-other', REFERENCE_LIST, 'FormatOther' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.FormatOthers.FormatOther', 
                [], [], 
                '''                Other configs
                ''',
                'format_other',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'format-others',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.RadiusAttribute' : {
        'meta_info' : _MetaInfoClass('Aaa.RadiusAttribute',
            False, 
            [
            _MetaInfoClassMember('called-station', REFERENCE_CLASS, 'CalledStation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.CalledStation', 
                [], [], 
                '''                AAA called station id attribute
                ''',
                'called_station',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('calling-station', REFERENCE_CLASS, 'CallingStation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.CallingStation', 
                [], [], 
                '''                AAA calling station id attribute
                ''',
                'calling_station',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('format-others', REFERENCE_CLASS, 'FormatOthers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.FormatOthers', 
                [], [], 
                '''                AAA nas-port-id attribute format
                ''',
                'format_others',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('nas-port', REFERENCE_CLASS, 'NasPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.NasPort', 
                [], [], 
                '''                AAA nas-port-id attribute
                ''',
                'nas_port',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('nas-port-id', REFERENCE_CLASS, 'NasPortId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute.NasPortId', 
                [], [], 
                '''                AAA nas-port-id attribute
                ''',
                'nas_port_id',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-aaacore-cfg',
            'radius-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-aaacore-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-diameter-cfg', True),
            _MetaInfoClassMember('peer-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name for the diameter peer configuration
                ''',
                'peer_name',
                'Cisco-IOS-XR-aaa-diameter-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server', 
                [], [], 
                '''                A server to include in the server group
                ''',
                'server',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup',
            False, 
            [
            _MetaInfoClassMember('server-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                DIAMETER server group name
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-diameter-cfg', True),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers', 
                [], [], 
                '''                List of DIAMETER servers present in the group
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diameter-server-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.DiameterServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.DiameterServerGroups',
            False, 
            [
            _MetaInfoClassMember('diameter-server-group', REFERENCE_LIST, 'DiameterServerGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup', 
                [], [], 
                '''                DIAMETER server group name
                ''',
                'diameter_server_group',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diameter-server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
                [], [], 
                '''                Specify the attribute list type accept or
                reject
                ''',
                'action',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('attribute-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of RADIUS attribute list
                ''',
                'attribute_list_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
                [], [], 
                '''                Specify the attribute list type accept or
                reject
                ''',
                'action',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('attribute-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of RADIUS attribute list
                ''',
                'attribute_list_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'reply',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting',
            False, 
            [
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'reply',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'request',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of RADIUS server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server', 
                [], [], 
                '''                A server to include in the server group
                ''',
                'server',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of RADIUS server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Idle time for the radius Server
                ''',
                'idle_time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-accounting-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore Accounting port
                ''',
                'ignore_accounting_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-auth-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore authentication Port
                ''',
                'ignore_auth_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('private-key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                RADIUS encryption key
                ''',
                'private_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('private-retransmit', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Number of times to retransmit a request to
                the RADIUS server
                ''',
                'private_retransmit',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('private-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'private_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username to be tested for automated testing
                ''',
                'username',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'private-server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers',
            False, 
            [
            _MetaInfoClassMember('private-server', REFERENCE_LIST, 'PrivateServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer', 
                [], [], 
                '''                A private server to include in the server
                group
                ''',
                'private_server',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'private-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle',
            False, 
            [
            _MetaInfoClassMember('access', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                To flow control the number of access requests
                sent to a radius server
                ''',
                'access',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('access-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Specify the number of timeouts exceeding
                which a throttled access request is dropped
                ''',
                'access_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('accounting', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                To flow control the number of accounting
                requests sent to a radius server
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'server-group-throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name',
            False, 
            [
            _MetaInfoClassMember('batch-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '1500')], [], 
                '''                Batch size for selection of the server
                ''',
                'batch_size',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-preferred-server', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Disable preferred server for this Server
                Group
                ''',
                'ignore_preferred_server',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('least-outstanding', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Pick the server with the least transactions
                outstanding
                ''',
                'least_outstanding',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_CLASS, 'Name' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name', 
                [], [], 
                '''                Batch size for selection of the server
                ''',
                'name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'method',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance',
            False, 
            [
            _MetaInfoClassMember('method', REFERENCE_CLASS, 'Method' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method', 
                [], [], 
                '''                Method by which the next host will be picked
                ''',
                'method',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'load-balance',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
                [], [], 
                '''                Specify the attribute list type accept or
                reject
                ''',
                'action',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('attribute-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of RADIUS attribute list
                ''',
                'attribute_list_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
                [], [], 
                '''                Specify the attribute list type accept or
                reject
                ''',
                'action',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('attribute-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of RADIUS attribute list
                ''',
                'attribute_list_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'reply',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization',
            False, 
            [
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'reply',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'request',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup',
            False, 
            [
            _MetaInfoClassMember('server-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                RADIUS server group name
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting', 
                [], [], 
                '''                List of filters in server group
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('authorization', REFERENCE_CLASS, 'Authorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization', 
                [], [], 
                '''                List of filters in server group
                ''',
                'authorization',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dead-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                This indicates the length of time (in minutes)
                for which RADIUS servers present in this group
                remain marked as dead
                ''',
                'dead_time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('load-balance', REFERENCE_CLASS, 'LoadBalance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance', 
                [], [], 
                '''                Radius load-balancing options
                ''',
                'load_balance',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('private-servers', REFERENCE_CLASS, 'PrivateServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers', 
                [], [], 
                '''                List of private RADIUS servers present in the
                group
                ''',
                'private_servers',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('server-group-throttle', REFERENCE_CLASS, 'ServerGroupThrottle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle', 
                [], [], 
                '''                Radius throttling options
                ''',
                'server_group_throttle',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers', 
                [], [], 
                '''                List of RADIUS servers present in the group
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in RADIUS
                packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify VRF name of RADIUS group
                ''',
                'vrf',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'radius-server-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups',
            False, 
            [
            _MetaInfoClassMember('radius-server-group', REFERENCE_LIST, 'RadiusServerGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup', 
                [], [], 
                '''                RADIUS server group name
                ''',
                'radius_server_group',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'radius-server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of TACACS+ server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server', 
                [], [], 
                '''                A server to include in the server group
                ''',
                'server',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of TACACS+ server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                ]),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Port number (standard 49)
                ''',
                'port_number',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Set TACACS+ encryption key
                ''',
                'key',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Time to wait for a TACACS+ server to reply
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'private-server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers',
            False, 
            [
            _MetaInfoClassMember('private-server', REFERENCE_LIST, 'PrivateServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer', 
                [], [], 
                '''                A private server to include in the server
                group
                ''',
                'private_server',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'private-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup',
            False, 
            [
            _MetaInfoClassMember('server-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                TACACS+ Server group name
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('private-servers', REFERENCE_CLASS, 'PrivateServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers', 
                [], [], 
                '''                List of private TACACS servers present in the
                group
                ''',
                'private_servers',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers', 
                [], [], 
                '''                Specify a TACACS+ server
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify VRF name of TACACS group
                ''',
                'vrf',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'tacacs-server-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups',
            False, 
            [
            _MetaInfoClassMember('tacacs-server-group', REFERENCE_LIST, 'TacacsServerGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup', 
                [], [], 
                '''                TACACS+ Server group name
                ''',
                'tacacs_server_group',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'tacacs-server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups',
            False, 
            [
            _MetaInfoClassMember('diameter-server-groups', REFERENCE_CLASS, 'DiameterServerGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.DiameterServerGroups', 
                [], [], 
                '''                DIAMETER server group definition
                ''',
                'diameter_server_groups',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('radius-server-groups', REFERENCE_CLASS, 'RadiusServerGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups', 
                [], [], 
                '''                RADIUS server group definition
                ''',
                'radius_server_groups',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('tacacs-server-groups', REFERENCE_CLASS, 'TacacsServerGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups', 
                [], [], 
                '''                TACACS+ server-group definition
                ''',
                'tacacs_server_groups',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-username',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames.Username.UsergroupUnderUsernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames',
            False, 
            [
            _MetaInfoClassMember('usergroup-under-username', REFERENCE_LIST, 'UsergroupUnderUsername' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername', 
                [], [], 
                '''                Name of the usergroup
                ''',
                'usergroup_under_username',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-usernames',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames.Username' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the users in the order of
                precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify the password for the user
                ''',
                'password',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('secret', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify the secret for the user
                ''',
                'secret',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usergroup-under-usernames', REFERENCE_CLASS, 'UsergroupUnderUsernames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames', 
                [], [], 
                '''                Specify the usergroup to which this user
                belongs
                ''',
                'usergroup_under_usernames',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'username',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames',
            False, 
            [
            _MetaInfoClassMember('username', REFERENCE_LIST, 'Username' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames.Username', 
                [], [], 
                '''                Local username
                ''',
                'username',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usernames',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the task group to include
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup-under-taskgroup', REFERENCE_LIST, 'TaskgroupUnderTaskgroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup', 
                [], [], 
                '''                Name of the task group to include
                ''',
                'taskgroup_under_taskgroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-taskgroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.Tasks.Task' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.Tasks.Task',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AaaLocaldTaskClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_cfg', 'AaaLocaldTaskClassEnum', 
                [], [], 
                '''                This specifies the operation permitted for
                this task eg: read/write/execute/debug
                ''',
                'type',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Task ID to which permission is to be granted
                (please use class AllTasks to get a list of
                valid task IDs)
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'task',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.Tasks',
            False, 
            [
            _MetaInfoClassMember('task', REFERENCE_LIST, 'Task' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.Tasks.Task', 
                [], [], 
                '''                Task ID to be included
                ''',
                'task',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
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
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description for the task group
                ''',
                'description',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('taskgroup-under-taskgroups', REFERENCE_CLASS, 'TaskgroupUnderTaskgroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups', 
                [], [], 
                '''                Specify a taskgroup to inherit from
                ''',
                'taskgroup_under_taskgroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('tasks', REFERENCE_CLASS, 'Tasks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.Tasks', 
                [], [], 
                '''                Specify task IDs to be part of this group
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup', REFERENCE_LIST, 'Taskgroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup', 
                [], [], 
                '''                Taskgroup name
                ''',
                'taskgroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the task group
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup-under-usergroup', REFERENCE_LIST, 'TaskgroupUnderUsergroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup', 
                [], [], 
                '''                Name of the task group
                ''',
                'taskgroup_under_usergroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the user group
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups',
            False, 
            [
            _MetaInfoClassMember('usergroup-under-usergroup', REFERENCE_LIST, 'UsergroupUnderUsergroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup', 
                [], [], 
                '''                Name of the user group
                ''',
                'usergroup_under_usergroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
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
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description for the user group
                ''',
                'description',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('taskgroup-under-usergroups', REFERENCE_CLASS, 'TaskgroupUnderUsergroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups', 
                [], [], 
                '''                Task group associated with this group
                ''',
                'taskgroup_under_usergroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usergroup-under-usergroups', REFERENCE_CLASS, 'UsergroupUnderUsergroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups', 
                [], [], 
                '''                User group to be inherited by this group
                ''',
                'usergroup_under_usergroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups',
            False, 
            [
            _MetaInfoClassMember('usergroup', REFERENCE_LIST, 'Usergroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup', 
                [], [], 
                '''                Usergroup name
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Gy' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Gy',
            False, 
            [
            _MetaInfoClassMember('dest-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Host name in FQDN format
                ''',
                'dest_host',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('retransmit', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Set retransmit count
                ''',
                'retransmit',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('tx-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Transaction timer value
                ''',
                'tx_timer',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'gy',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Origin' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Origin',
            False, 
            [
            _MetaInfoClassMember('host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Host name in FQDN format
                ''',
                'host',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('realm', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Origin Realm String
                ''',
                'realm',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'origin',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Nas' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Nas',
            False, 
            [
            _MetaInfoClassMember('dest-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Host name in FQDN format
                ''',
                'dest_host',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'nas',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.DiameterTls' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.DiameterTls',
            False, 
            [
            _MetaInfoClassMember('trustpoint', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trustpoint label to be used
                ''',
                'trustpoint',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diameter-tls',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Peers.Peer.PeerTimer' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Peers.Peer.PeerTimer',
            False, 
            [
            _MetaInfoClassMember('connection', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timer value in seconds
                ''',
                'connection',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('transaction', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timer value in seconds
                ''',
                'transaction',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('watchdog', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timer value in seconds
                ''',
                'watchdog',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'peer-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Peers.Peer.PeerType' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Peers.Peer.PeerType',
            False, 
            [
            _MetaInfoClassMember('server', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled
                ''',
                'server',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'peer-type',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('peer-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name for the diameter peer configuration
                ''',
                'peer_name',
                'Cisco-IOS-XR-aaa-diameter-cfg', True),
            _MetaInfoClassMember('host-destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination host information
                ''',
                'host_destination',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of diameter server
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address of diameter server
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('peer-timer', REFERENCE_CLASS, 'PeerTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Peers.Peer.PeerTimer', 
                [], [], 
                '''                Timers used for the peer
                ''',
                'peer_timer',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('peer-type', REFERENCE_CLASS, 'PeerType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Peers.Peer.PeerType', 
                [], [], 
                '''                Peer Type
                ''',
                'peer_type',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('realm-destination', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Realm to which the peer belongs to
                ''',
                'realm_destination',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                DIAMETER packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('tcp-transport', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify a Diameter transport protocol
                ''',
                'tcp_transport',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('tls-transport', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Specify a Diameter security type
                ''',
                'tls_transport',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('vrf-ip', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF the peer belongs to
                ''',
                'vrf_ip',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Peers' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Peers.Peer', 
                [], [], 
                '''                Diameter peer instance
                ''',
                'peer',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue',
            False, 
            [
            _MetaInfoClassMember('data-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Dataypte of attribute
                ''',
                'data_type',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('mandatory', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Is mandatory?
                ''',
                'mandatory',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-binary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Binary type
                ''',
                'type_binary',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-boolean', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Boolean type
                ''',
                'type_boolean',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-enum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Enumeration type
                ''',
                'type_enum',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-grouped', ATTRIBUTE, 'int' , None, None, 
                [('0', '99')], [], 
                '''                Grouped attribute
                ''',
                'type_grouped',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-identity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diameter-identity type
                ''',
                'type_identity',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address type
                ''',
                'type_ipv4_address',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String type
                ''',
                'type_string',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('type-ulong', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Numeric type
                ''',
                'type_ulong',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diam-attr-value',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef',
            False, 
            [
            _MetaInfoClassMember('vendor-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                value for vendor id
                ''',
                'vendor_id',
                'Cisco-IOS-XR-aaa-diameter-cfg', True),
            _MetaInfoClassMember('attribute-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                enter attribute id
                ''',
                'attribute_id',
                'Cisco-IOS-XR-aaa-diameter-cfg', True),
            _MetaInfoClassMember('diam-attr-value', REFERENCE_CLASS, 'DiamAttrValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue', 
                [], [], 
                '''                attr subcommands
                ''',
                'diam_attr_value',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diam-attr-def',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Diams.Diam.DiamAttrDefs' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Diams.Diam.DiamAttrDefs',
            False, 
            [
            _MetaInfoClassMember('diam-attr-def', REFERENCE_LIST, 'DiamAttrDef' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef', 
                [], [], 
                '''                vendor id
                ''',
                'diam_attr_def',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diam-attr-defs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Diams.Diam' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Diams.Diam',
            False, 
            [
            _MetaInfoClassMember('list-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '99')], [], 
                '''                attribute list number
                ''',
                'list_id',
                'Cisco-IOS-XR-aaa-diameter-cfg', True),
            _MetaInfoClassMember('diam-attr-defs', REFERENCE_CLASS, 'DiamAttrDefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Diams.Diam.DiamAttrDefs', 
                [], [], 
                '''                Specify an attribute definition
                ''',
                'diam_attr_defs',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diam',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Diams' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Diams',
            False, 
            [
            _MetaInfoClassMember('diam', REFERENCE_LIST, 'Diam' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Diams.Diam', 
                [], [], 
                '''                attribute list configuration
                ''',
                'diam',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diams',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Gx' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Gx',
            False, 
            [
            _MetaInfoClassMember('dest-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Host name in FQDN format
                ''',
                'dest_host',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('retransmit', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Set retransmit count
                ''',
                'retransmit',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('tx-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Transaction timer value
                ''',
                'tx_timer',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'gx',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.DiameterTimer' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.DiameterTimer',
            False, 
            [
            _MetaInfoClassMember('connection', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timer value in seconds
                ''',
                'connection',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('transaction', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timer value in seconds
                ''',
                'transaction',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('watchdog', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timer value in seconds
                ''',
                'watchdog',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diameter-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Vendor.Supported' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Vendor.Supported',
            False, 
            [
            _MetaInfoClassMember('cisco', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Cisco attribute support
                ''',
                'cisco',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('etsi', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Etsi attribute support
                ''',
                'etsi',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('threegpp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                3GPP attribute support
                ''',
                'threegpp',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('vodafone', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Vodafone attribute support
                ''',
                'vodafone',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'supported',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter.Vendor' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter.Vendor',
            False, 
            [
            _MetaInfoClassMember('supported', REFERENCE_CLASS, 'Supported' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Vendor.Supported', 
                [], [], 
                '''                Supported vendors
                ''',
                'supported',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'vendor',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Diameter' : {
        'meta_info' : _MetaInfoClass('Aaa.Diameter',
            False, 
            [
            _MetaInfoClassMember('diameter-timer', REFERENCE_CLASS, 'DiameterTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.DiameterTimer', 
                [], [], 
                '''                Timers used for the peer
                ''',
                'diameter_timer',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('diameter-tls', REFERENCE_CLASS, 'DiameterTls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.DiameterTls', 
                [], [], 
                '''                TLS sub commands
                ''',
                'diameter_tls',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('diams', REFERENCE_CLASS, 'Diams' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Diams', 
                [], [], 
                '''                Attribute list configuration for test command
                ''',
                'diams',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('gx', REFERENCE_CLASS, 'Gx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Gx', 
                [], [], 
                '''                Start diameter policy-if
                ''',
                'gx',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('gy', REFERENCE_CLASS, 'Gy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Gy', 
                [], [], 
                '''                Start diameter policy-if
                ''',
                'gy',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('nas', REFERENCE_CLASS, 'Nas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Nas', 
                [], [], 
                '''                Start diameter Nas
                ''',
                'nas',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('origin', REFERENCE_CLASS, 'Origin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Origin', 
                [], [], 
                '''                Origin sub commands
                ''',
                'origin',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Peers', 
                [], [], 
                '''                List of diameter peers
                ''',
                'peers',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                DIAMETER packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('vendor', REFERENCE_CLASS, 'Vendor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter.Vendor', 
                [], [], 
                '''                Vendor specific
                ''',
                'vendor',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-diameter-cfg',
            'diameter',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-diameter-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the order
                of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of RADIUS server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('host-key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                RADIUS encryption key
                ''',
                'host_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('host-retransmit', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Number of times to retransmit a request to
                the RADIUS server
                ''',
                'host_retransmit',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('host-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'host_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Idle time for RADIUS server
                ''',
                'idle_time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-accounting-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'ignore_accounting_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-auth-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'ignore_auth_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username to be tested for automated testing
                ''',
                'username',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Hosts' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Hosts.Host', 
                [], [], 
                '''                Instance of a RADIUS server
                ''',
                'host',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DeadCriteria' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DeadCriteria',
            False, 
            [
            _MetaInfoClassMember('time', ATTRIBUTE, 'int' , None, None, 
                [('1', '120')], [], 
                '''                The minimum amount of time which must elapse
                since the router last received a valid RADIUS
                packet from the server prior to marking it
                dead
                ''',
                'time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('tries', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The number of consecutive timeouts the router
                must experience in order to mark the server as
                dead. All transmissions, including the initial
                transmit and all retransmits, will be counted
                ''',
                'tries',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'dead-criteria',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Disallow' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Disallow',
            False, 
            [
            _MetaInfoClassMember('null-username', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Disallow null-username
                ''',
                'null_username',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'disallow',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Ipv6' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify the DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'AaaDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DynamicAuthorization.Clients.Client' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DynamicAuthorization.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of COA client
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('server-key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                RADIUS CoA client encryption key
                ''',
                'server_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of COA client
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('server-key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                RADIUS CoA client encryption key
                ''',
                'server_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'client-vrf-name',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DynamicAuthorization.Clients' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DynamicAuthorization.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization.Clients.Client', 
                [], [], 
                '''                Client data
                ''',
                'client',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('client-vrf-name', REFERENCE_LIST, 'ClientVrfName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName', 
                [], [], 
                '''                Client data
                ''',
                'client_vrf_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DynamicAuthorization' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DynamicAuthorization',
            False, 
            [
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'AaaAuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAuthenticationEnum', 
                [], [], 
                '''                RADIUS  dynamic  authorization  type
                ''',
                'authentication_type',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization.Clients', 
                [], [], 
                '''                Client data
                ''',
                'clients',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore', REFERENCE_ENUM_CLASS, 'AaaSelectKeyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaSelectKeyEnum', 
                [], [], 
                '''                Ignore option for server key or session key
                ''',
                'ignore',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1000', '5000')], [], 
                '''                Specify the COA server port to listen on
                ''',
                'port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('server-key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                RADIUS CoA client encryption key
                ''',
                'server_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'dynamic-authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize',
            False, 
            [
            _MetaInfoClassMember('batch-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '1500')], [], 
                '''                Batch size for selection of the server
                ''',
                'batch_size',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-preferred-server', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Disable preferred server for this Server
                Group
                ''',
                'ignore_preferred_server',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'batch-size',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod',
            False, 
            [
            _MetaInfoClassMember('batch-size', REFERENCE_CLASS, 'BatchSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize', 
                [], [], 
                '''                Batch size for selection of the server
                ''',
                'batch_size',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'load-balance-method',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.LoadBalanceOptions' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.LoadBalanceOptions',
            False, 
            [
            _MetaInfoClassMember('load-balance-method', REFERENCE_CLASS, 'LoadBalanceMethod' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod', 
                [], [], 
                '''                Method by which the next host will be picked
                ''',
                'load_balance_method',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'load-balance-options',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name. Specify 'default' for defalut VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                RADIUS packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vrfs' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vrfs.Vrf', 
                [], [], 
                '''                A VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Throttle' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Throttle',
            False, 
            [
            _MetaInfoClassMember('access', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                To flow control the number of access requests
                sent to a radius server
                ''',
                'access',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('access-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Specify the number of timeouts exceeding which
                a throttled access request is dropped
                ''',
                'access_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('accounting', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                To flow control the number of accounting
                requests sent to a radius server
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vsa.Attribute.Ignore' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vsa.Attribute.Ignore',
            False, 
            [
            _MetaInfoClassMember('unknown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore the VSA and no prefix will reject the
                unknown VSA
                ''',
                'unknown',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'ignore',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vsa.Attribute' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vsa.Attribute',
            False, 
            [
            _MetaInfoClassMember('ignore', REFERENCE_CLASS, 'Ignore' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vsa.Attribute.Ignore', 
                [], [], 
                '''                Ignore the VSA
                ''',
                'ignore',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vsa' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vsa',
            False, 
            [
            _MetaInfoClassMember('attribute', REFERENCE_CLASS, 'Attribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vsa.Attribute', 
                [], [], 
                '''                Vendor Specific Attribute
                ''',
                'attribute',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'vsa',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Ipv4' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify the DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'AaaDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.FilterId11.Defaults' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.FilterId11.Defaults',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AaaDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDirectionEnum', 
                [], [], 
                '''                Filtering is applied to
                ingress(inbound)/egress(outbound) packets
                only
                ''',
                'direction',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.FilterId11' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.FilterId11',
            False, 
            [
            _MetaInfoClassMember('defaults', REFERENCE_CLASS, 'Defaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.FilterId11.Defaults', 
                [], [], 
                '''                Set the attribute default direction
                ''',
                'defaults',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'filter-id-11',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_ENUM_CLASS, 'AaaConfigEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaConfigEnum', 
                [], [], 
                '''                false/true
                ''',
                'config',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'include-parent-session-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctMultiSessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctMultiSessionId',
            False, 
            [
            _MetaInfoClassMember('include-parent-session-id', REFERENCE_CLASS, 'IncludeParentSessionId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId', 
                [], [], 
                '''                Prepend Acct-Session-Id attribute with
                Nas-Port-Id
                ''',
                'include_parent_session_id',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'acct-multi-session-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_ENUM_CLASS, 'AaaConfigEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaConfigEnum', 
                [], [], 
                '''                false/true
                ''',
                'config',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'prepend-nas-port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctSessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctSessionId',
            False, 
            [
            _MetaInfoClassMember('prepend-nas-port-id', REFERENCE_CLASS, 'PrependNasPortId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId', 
                [], [], 
                '''                Prepend Acct-Session-Id attribute with
                Nas-Port-Id
                ''',
                'prepend_nas_port_id',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'acct-session-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute',
            False, 
            [
            _MetaInfoClassMember('acct-multi-session-id', REFERENCE_CLASS, 'AcctMultiSessionId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctMultiSessionId', 
                [], [], 
                '''                Acct-Session-Id attribute(44)
                ''',
                'acct_multi_session_id',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('acct-session-id', REFERENCE_CLASS, 'AcctSessionId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctSessionId', 
                [], [], 
                '''                Acct-Session-Id attribute(44)
                ''',
                'acct_session_id',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('filter-id-11', REFERENCE_CLASS, 'FilterId11' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.FilterId11', 
                [], [], 
                '''                Filter-Id attribute configuration
                ''',
                'filter_id_11',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'radius-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Attributes.Attribute' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Attributes.Attribute',
            False, 
            [
            _MetaInfoClassMember('attribute-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Attribute list name
                ''',
                'attribute_list_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('attribute', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify RADIUS attribute
                ''',
                'attribute',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Attributes' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Attributes',
            False, 
            [
            _MetaInfoClassMember('attribute', REFERENCE_LIST, 'Attribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Attributes.Attribute', 
                [], [], 
                '''                Attribute list name
                ''',
                'attribute',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.SourcePort' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.SourcePort',
            False, 
            [
            _MetaInfoClassMember('extended', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable source-port extend 
                ''',
                'extended',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'source-port',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Attributes', 
                [], [], 
                '''                Table of attribute list
                ''',
                'attributes',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dead-criteria', REFERENCE_CLASS, 'DeadCriteria' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DeadCriteria', 
                [], [], 
                '''                RADIUS server dead criteria
                ''',
                'dead_criteria',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dead-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                This indicates the length of time (in minutes)
                for which a RADIUS server remains marked as
                dead
                ''',
                'dead_time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('disallow', REFERENCE_CLASS, 'Disallow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Disallow', 
                [], [], 
                '''                disallow null-username
                ''',
                'disallow',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dynamic-authorization', REFERENCE_CLASS, 'DynamicAuthorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization', 
                [], [], 
                '''                RADIUS dynamic authorization
                ''',
                'dynamic_authorization',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Hosts', 
                [], [], 
                '''                List of RADIUS servers
                ''',
                'hosts',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Idle time for RADIUS server
                ''',
                'idle_time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-accounting-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'ignore_accounting_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-auth-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'ignore_auth_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Ipv4', 
                [], [], 
                '''                IPv4 configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Ipv6', 
                [], [], 
                '''                IPv6 configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                RADIUS encryption key
                ''',
                'key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('load-balance-options', REFERENCE_CLASS, 'LoadBalanceOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.LoadBalanceOptions', 
                [], [], 
                '''                Radius load-balancing options
                ''',
                'load_balance_options',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('radius-attribute', REFERENCE_CLASS, 'RadiusAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute', 
                [], [], 
                '''                attribute
                ''',
                'radius_attribute',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('retransmit', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Number of times to retransmit a request to the
                RADIUS server(0-Disable)
                ''',
                'retransmit',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('source-port', REFERENCE_CLASS, 'SourcePort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.SourcePort', 
                [], [], 
                '''                Source port
                ''',
                'source_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Throttle', 
                [], [], 
                '''                Radius throttling options
                ''',
                'throttle',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username to be tested for automated testing
                ''',
                'username',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('vsa', REFERENCE_CLASS, 'Vsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vsa', 
                [], [], 
                '''                Unknown VSA (Vendor Specific Attribute) ignore
                configuration for RADIUS server
                ''',
                'vsa',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'radius',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Ipv6' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify the DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'TacacsDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg', 'TacacsDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This is used to sort the servers in the order
                of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of TACACS+ server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                ]),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Port number (standard 49)
                ''',
                'port_number',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Set TACACS+ encryption key
                ''',
                'key',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('single-connect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use a single connection for all sessions for a
                given TACACS+ server
                ''',
                'single_connect',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Time to wait for a TACACS+ server to reply
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Hosts' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Hosts.Host', 
                [], [], 
                '''                One of the TACACS+ servers
                ''',
                'host',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Ipv4' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Specify the DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'TacacsDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_tacacs_cfg', 'TacacsDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name. Specify 'default' for default VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                TACACS+ packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Vrfs' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Vrfs.Vrf', 
                [], [], 
                '''                A VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs',
            False, 
            [
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Hosts', 
                [], [], 
                '''                Specify a TACACS+ server
                ''',
                'hosts',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Ipv4', 
                [], [], 
                '''                IPv4 configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Ipv6', 
                [], [], 
                '''                IPv6 configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Set TACACS+ encryption key
                ''',
                'key',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('single-connect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use a single connection for all sessions for a
                given TACACS+ server
                ''',
                'single_connect',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Time to wait for a TACACS+ server to reply
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'tacacs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa' : {
        'meta_info' : _MetaInfoClass('Aaa',
            False, 
            [
            _MetaInfoClassMember('aaa-dot1x', REFERENCE_CLASS, 'AaaDot1X' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaDot1X', 
                [], [], 
                '''                AAA Dot1x
                ''',
                'aaa_dot1x',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('aaa-mobile', REFERENCE_CLASS, 'AaaMobile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaMobile', 
                [], [], 
                '''                AAA Mobile
                ''',
                'aaa_mobile',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('aaa-subscriber', REFERENCE_CLASS, 'AaaSubscriber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AaaSubscriber', 
                [], [], 
                '''                AAA subscriber
                ''',
                'aaa_subscriber',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('accounting-update', REFERENCE_CLASS, 'AccountingUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AccountingUpdate', 
                [], [], 
                '''                Configuration related to 'update' accounting
                ''',
                'accounting_update',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('accountings', REFERENCE_CLASS, 'Accountings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Accountings', 
                [], [], 
                '''                AAA accounting
                ''',
                'accountings',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('authentications', REFERENCE_CLASS, 'Authentications' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authentications', 
                [], [], 
                '''                AAA authentication
                ''',
                'authentications',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('authorizations', REFERENCE_CLASS, 'Authorizations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authorizations', 
                [], [], 
                '''                AAA authorization
                ''',
                'authorizations',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('banner', REFERENCE_CLASS, 'Banner' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Banner', 
                [], [], 
                '''                AAA banner
                ''',
                'banner',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('default-taskgroup', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This class is used for setting the default
                taskgroup to be used for remote server
                authentication
                ''',
                'default_taskgroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('diameter', REFERENCE_CLASS, 'Diameter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Diameter', 
                [], [], 
                '''                Diameter base protocol
                ''',
                'diameter',
                'Cisco-IOS-XR-aaa-diameter-cfg', False),
            _MetaInfoClassMember('radius', REFERENCE_CLASS, 'Radius' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius', 
                [], [], 
                '''                Remote Access Dial-In User Service
                ''',
                'radius',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('radius-attribute', REFERENCE_CLASS, 'RadiusAttribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.RadiusAttribute', 
                [], [], 
                '''                AAA RADIUS attribute configurations
                ''',
                'radius_attribute',
                'Cisco-IOS-XR-aaa-aaacore-cfg', False),
            _MetaInfoClassMember('server-groups', REFERENCE_CLASS, 'ServerGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups', 
                [], [], 
                '''                AAA group definitions
                ''',
                'server_groups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('tacacs', REFERENCE_CLASS, 'Tacacs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs', 
                [], [], 
                '''                Modify TACACS+ query parameters
                ''',
                'tacacs',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('taskgroups', REFERENCE_CLASS, 'Taskgroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups', 
                [], [], 
                '''                Specify a taskgroup to inherit from
                ''',
                'taskgroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usergroups', REFERENCE_CLASS, 'Usergroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups', 
                [], [], 
                '''                Specify a Usergroup to inherit from
                ''',
                'usergroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usernames', REFERENCE_CLASS, 'Usernames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames', 
                [], [], 
                '''                Configure local usernames
                ''',
                'usernames',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
}
_meta_table['Aaa.Accountings.Accounting']['meta_info'].parent =_meta_table['Aaa.Accountings']['meta_info']
_meta_table['Aaa.Authorizations.Authorization']['meta_info'].parent =_meta_table['Aaa.Authorizations']['meta_info']
_meta_table['Aaa.Authentications.Authentication']['meta_info'].parent =_meta_table['Aaa.Authentications']['meta_info']
_meta_table['Aaa.AaaSubscriber.PolicyIfAuthors.PolicyIfAuthor']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber.PolicyIfAuthors']['meta_info']
_meta_table['Aaa.AaaSubscriber.Accountings.Accounting']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber.Accountings']['meta_info']
_meta_table['Aaa.AaaSubscriber.PrepaidAuthors.PrepaidAuthor']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber.PrepaidAuthors']['meta_info']
_meta_table['Aaa.AaaSubscriber.Authorizations.Authorization']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber.Authorizations']['meta_info']
_meta_table['Aaa.AaaSubscriber.Authentications.Authentication']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber.Authentications']['meta_info']
_meta_table['Aaa.AaaSubscriber.PolicyIfAuthors']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber']['meta_info']
_meta_table['Aaa.AaaSubscriber.Accountings']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber']['meta_info']
_meta_table['Aaa.AaaSubscriber.ServiceAccounting']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber']['meta_info']
_meta_table['Aaa.AaaSubscriber.PrepaidAuthors']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber']['meta_info']
_meta_table['Aaa.AaaSubscriber.Authorizations']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber']['meta_info']
_meta_table['Aaa.AaaSubscriber.Authentications']['meta_info'].parent =_meta_table['Aaa.AaaSubscriber']['meta_info']
_meta_table['Aaa.AaaMobile.Mobiles.Mobile']['meta_info'].parent =_meta_table['Aaa.AaaMobile.Mobiles']['meta_info']
_meta_table['Aaa.AaaMobile.Mobiles']['meta_info'].parent =_meta_table['Aaa.AaaMobile']['meta_info']
_meta_table['Aaa.AaaDot1X.Authentications.Authentication']['meta_info'].parent =_meta_table['Aaa.AaaDot1X.Authentications']['meta_info']
_meta_table['Aaa.AaaDot1X.Authentications']['meta_info'].parent =_meta_table['Aaa.AaaDot1X']['meta_info']
_meta_table['Aaa.RadiusAttribute.NasPortId.Formats.Format']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.NasPortId.Formats']['meta_info']
_meta_table['Aaa.RadiusAttribute.NasPortId.Formats']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.NasPortId']['meta_info']
_meta_table['Aaa.RadiusAttribute.CallingStation.Formats.Format']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.CallingStation.Formats']['meta_info']
_meta_table['Aaa.RadiusAttribute.CallingStation.Formats']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.CallingStation']['meta_info']
_meta_table['Aaa.RadiusAttribute.CalledStation.Formats.Format']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.CalledStation.Formats']['meta_info']
_meta_table['Aaa.RadiusAttribute.CalledStation.Formats']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.CalledStation']['meta_info']
_meta_table['Aaa.RadiusAttribute.NasPort.FormatExtendeds.FormatExtended']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.NasPort.FormatExtendeds']['meta_info']
_meta_table['Aaa.RadiusAttribute.NasPort.FormatExtendeds']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.NasPort']['meta_info']
_meta_table['Aaa.RadiusAttribute.FormatOthers.FormatOther']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute.FormatOthers']['meta_info']
_meta_table['Aaa.RadiusAttribute.NasPortId']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute']['meta_info']
_meta_table['Aaa.RadiusAttribute.CallingStation']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute']['meta_info']
_meta_table['Aaa.RadiusAttribute.CalledStation']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute']['meta_info']
_meta_table['Aaa.RadiusAttribute.NasPort']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute']['meta_info']
_meta_table['Aaa.RadiusAttribute.FormatOthers']['meta_info'].parent =_meta_table['Aaa.RadiusAttribute']['meta_info']
_meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers.Server']['meta_info'].parent =_meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers']['meta_info']
_meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup.Servers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.DiameterServerGroups.DiameterServerGroup']['meta_info'].parent =_meta_table['Aaa.ServerGroups.DiameterServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.DiameterServerGroups']['meta_info'].parent =_meta_table['Aaa.ServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups']['meta_info'].parent =_meta_table['Aaa.ServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups']['meta_info'].parent =_meta_table['Aaa.ServerGroups']['meta_info']
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername']['meta_info'].parent =_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info']
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info'].parent =_meta_table['Aaa.Usernames.Username']['meta_info']
_meta_table['Aaa.Usernames.Username']['meta_info'].parent =_meta_table['Aaa.Usernames']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.Tasks.Task']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup.Tasks']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.Tasks']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info'].parent =_meta_table['Aaa.Taskgroups']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup']['meta_info'].parent =_meta_table['Aaa.Usergroups']['meta_info']
_meta_table['Aaa.Diameter.Peers.Peer.PeerTimer']['meta_info'].parent =_meta_table['Aaa.Diameter.Peers.Peer']['meta_info']
_meta_table['Aaa.Diameter.Peers.Peer.PeerType']['meta_info'].parent =_meta_table['Aaa.Diameter.Peers.Peer']['meta_info']
_meta_table['Aaa.Diameter.Peers.Peer']['meta_info'].parent =_meta_table['Aaa.Diameter.Peers']['meta_info']
_meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef.DiamAttrValue']['meta_info'].parent =_meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef']['meta_info']
_meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs.DiamAttrDef']['meta_info'].parent =_meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs']['meta_info']
_meta_table['Aaa.Diameter.Diams.Diam.DiamAttrDefs']['meta_info'].parent =_meta_table['Aaa.Diameter.Diams.Diam']['meta_info']
_meta_table['Aaa.Diameter.Diams.Diam']['meta_info'].parent =_meta_table['Aaa.Diameter.Diams']['meta_info']
_meta_table['Aaa.Diameter.Vendor.Supported']['meta_info'].parent =_meta_table['Aaa.Diameter.Vendor']['meta_info']
_meta_table['Aaa.Diameter.Gy']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Origin']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Nas']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.DiameterTls']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Peers']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Diams']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Gx']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.DiameterTimer']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Diameter.Vendor']['meta_info'].parent =_meta_table['Aaa.Diameter']['meta_info']
_meta_table['Aaa.Radius.Hosts.Host']['meta_info'].parent =_meta_table['Aaa.Radius.Hosts']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization.Clients.Client']['meta_info'].parent =_meta_table['Aaa.Radius.DynamicAuthorization.Clients']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName']['meta_info'].parent =_meta_table['Aaa.Radius.DynamicAuthorization.Clients']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization.Clients']['meta_info'].parent =_meta_table['Aaa.Radius.DynamicAuthorization']['meta_info']
_meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize']['meta_info'].parent =_meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod']['meta_info']
_meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod']['meta_info'].parent =_meta_table['Aaa.Radius.LoadBalanceOptions']['meta_info']
_meta_table['Aaa.Radius.Vrfs.Vrf']['meta_info'].parent =_meta_table['Aaa.Radius.Vrfs']['meta_info']
_meta_table['Aaa.Radius.Vsa.Attribute.Ignore']['meta_info'].parent =_meta_table['Aaa.Radius.Vsa.Attribute']['meta_info']
_meta_table['Aaa.Radius.Vsa.Attribute']['meta_info'].parent =_meta_table['Aaa.Radius.Vsa']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.FilterId11.Defaults']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute.FilterId11']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.FilterId11']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute']['meta_info']
_meta_table['Aaa.Radius.Attributes.Attribute']['meta_info'].parent =_meta_table['Aaa.Radius.Attributes']['meta_info']
_meta_table['Aaa.Radius.Hosts']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.DeadCriteria']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Disallow']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Ipv6']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.LoadBalanceOptions']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Vrfs']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Throttle']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Vsa']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Ipv4']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Attributes']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.SourcePort']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Tacacs.Hosts.Host']['meta_info'].parent =_meta_table['Aaa.Tacacs.Hosts']['meta_info']
_meta_table['Aaa.Tacacs.Vrfs.Vrf']['meta_info'].parent =_meta_table['Aaa.Tacacs.Vrfs']['meta_info']
_meta_table['Aaa.Tacacs.Ipv6']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.Hosts']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.Ipv4']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.Vrfs']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Accountings']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Authorizations']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.AccountingUpdate']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Banner']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Authentications']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.AaaSubscriber']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.AaaMobile']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.AaaDot1X']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.RadiusAttribute']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.ServerGroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Usernames']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Taskgroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Usergroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Diameter']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Radius']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Tacacs']['meta_info'].parent =_meta_table['Aaa']['meta_info']
