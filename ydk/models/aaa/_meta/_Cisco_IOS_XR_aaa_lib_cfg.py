


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AaaMethodEnum' : _MetaInfoEnum('AaaMethodEnum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg',
        {
            'not-set':'NOT_SET',
            'none':'NONE',
            'local':'LOCAL',
            'radius':'RADIUS',
            'tacacs-plus':'TACACS_PLUS',
            'dsmd':'DSMD',
            'sgbp':'SGBP',
            'acct-d':'ACCT_D',
            'error':'ERROR',
            'if-authenticated':'IF_AUTHENTICATED',
            'server-group':'SERVER_GROUP',
            'server-group-not-defined':'SERVER_GROUP_NOT_DEFINED',
            'line':'LINE',
            'enable':'ENABLE',
            'kerberos':'KERBEROS',
            'diameter':'DIAMETER',
            'last':'LAST',
        }, 'Cisco-IOS-XR-aaa-lib-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg']),
    'AaaAccountingUpdateEnum' : _MetaInfoEnum('AaaAccountingUpdateEnum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg',
        {
            'none':'NONE',
            'newinfo':'NEWINFO',
            'periodic':'PERIODIC',
        }, 'Cisco-IOS-XR-aaa-lib-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg']),
    'AaaAccountingEnum' : _MetaInfoEnum('AaaAccountingEnum', 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg',
        {
            'not-set':'NOT_SET',
            'start-stop':'START_STOP',
            'stop-only':'STOP_ONLY',
        }, 'Cisco-IOS-XR-aaa-lib-cfg', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg']),
    'Aaa.AccountingUpdate' : {
        'meta_info' : _MetaInfoClass('Aaa.AccountingUpdate',
            False, 
            [
            _MetaInfoClassMember('periodic-interval', ATTRIBUTE, 'int' , None, None, 
                [(0, 35791394)], [], 
                '''                Periodic update interval in minutes
                ''',
                'periodic_interval',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AaaAccountingUpdateEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'AaaAccountingUpdateEnum', 
                [], [], 
                '''                newinfo/periodic
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'accounting-update',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Accountings.Accounting' : {
        'meta_info' : _MetaInfoClass('Aaa.Accountings.Accounting',
            False, 
            [
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Named accounting list
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                exec:Account exec sessions, commands: Account
                CLI commands
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('broadcast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Broadcast
                ''',
                'broadcast',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'AaaMethodEnum', 
                [], [], 
                '''                Method Types
                ''',
                'method',
                'Cisco-IOS-XR-aaa-lib-cfg', False, max_elements=4),
            _MetaInfoClassMember('rp-failover', ATTRIBUTE, 'Empty' , None, None, 
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
            _MetaInfoClassMember('type-xr', REFERENCE_ENUM_CLASS, 'AaaAccountingEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'AaaAccountingEnum', 
                [], [], 
                '''                Stop only/Start Stop
                ''',
                'type_xr',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Accountings' : {
        'meta_info' : _MetaInfoClass('Aaa.Accountings',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_LIST, 'Accounting' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Accountings.Accounting', 
                [], [], 
                '''                Configurations related to accounting
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'accountings',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authentications.Authentication' : {
        'meta_info' : _MetaInfoClass('Aaa.Authentications.Authentication',
            False, 
            [
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                List name for AAA authentication
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                login: Authenticate login sessions, ppp:
                Authenticate ppp sessions
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'AaaMethodEnum', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authentications' : {
        'meta_info' : _MetaInfoClass('Aaa.Authentications',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_LIST, 'Authentication' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authentications.Authentication', 
                [], [], 
                '''                Configurations related to authentication
                ''',
                'authentication',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'authentications',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authorizations.Authorization' : {
        'meta_info' : _MetaInfoClass('Aaa.Authorizations.Authorization',
            False, 
            [
            _MetaInfoClassMember('listname', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                List name for AAA authorization
                ''',
                'listname',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                network: Authorize IKE requests, commands:
                Authorize CLI commands
                ''',
                'type',
                'Cisco-IOS-XR-aaa-lib-cfg', True),
            _MetaInfoClassMember('method', REFERENCE_LEAFLIST, 'AaaMethodEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'AaaMethodEnum', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Authorizations' : {
        'meta_info' : _MetaInfoClass('Aaa.Authorizations',
            False, 
            [
            _MetaInfoClassMember('authorization', REFERENCE_LIST, 'Authorization' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authorizations.Authorization', 
                [], [], 
                '''                Configurations related to authorization
                ''',
                'authorization',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'authorizations',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Attributes.Attribute' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Attributes.Attribute',
            False, 
            [
            _MetaInfoClassMember('attribute-list-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Attributes' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Attributes',
            False, 
            [
            _MetaInfoClassMember('attribute', REFERENCE_LIST, 'Attribute' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Attributes.Attribute', 
                [], [], 
                '''                Attribute list name
                ''',
                'attribute',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DeadCriteria' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DeadCriteria',
            False, 
            [
            _MetaInfoClassMember('time', ATTRIBUTE, 'int' , None, None, 
                [(1, 120)], [], 
                '''                The minimum amount of time which must elapse
                since the router last received a valid RADIUS
                packet from the server prior to marking it
                dead
                ''',
                'time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('tries', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Disallow' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Disallow',
            False, 
            [
            _MetaInfoClassMember('null-username', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Disallow null-username
                ''',
                'null_username',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'disallow',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('server-key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                RADIUS CoA client encryption key
                ''',
                'server_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of COA client
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of COA client
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('server-key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                RADIUS CoA client encryption key
                ''',
                'server_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'client-vrf-name',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DynamicAuthorization.Clients' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DynamicAuthorization.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization.Clients.Client', 
                [], [], 
                '''                Client data
                ''',
                'client',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('client-vrf-name', REFERENCE_LIST, 'ClientVrfName' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName', 
                [], [], 
                '''                Client data
                ''',
                'client_vrf_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.DynamicAuthorization' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.DynamicAuthorization',
            False, 
            [
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'AaaAuthenticationEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaAuthenticationEnum', 
                [], [], 
                '''                RADIUS  dynamic  authorization  type
                ''',
                'authentication_type',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization.Clients', 
                [], [], 
                '''                Client data
                ''',
                'clients',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore', REFERENCE_ENUM_CLASS, 'AaaSelectKeyEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaSelectKeyEnum', 
                [], [], 
                '''                Ignore option for server key or session key
                ''',
                'ignore',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [(1000, 5000)], [], 
                '''                Specify the COA server port to listen on
                ''',
                'port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('server-key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                RADIUS CoA client encryption key
                ''',
                'server_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'dynamic-authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of RADIUS server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This is used to sort the servers in the order
                of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('host-key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                RADIUS encryption key
                ''',
                'host_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('host-retransmit', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Number of times to retransmit a request to
                the RADIUS server
                ''',
                'host_retransmit',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('host-timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Time to wait for a RADIUS server to reply
                ''',
                'host_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Hosts' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Hosts.Host', 
                [], [], 
                '''                Instance of a RADIUS server
                ''',
                'host',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'AaaDscpValueEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'AaaDscpValueEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize',
            False, 
            [
            _MetaInfoClassMember('batch-size', ATTRIBUTE, 'int' , None, None, 
                [(1, 1500)], [], 
                '''                Batch size for selection of the server
                ''',
                'batch_size',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-preferred-server', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Disable preferred server for this Server
                Group
                ''',
                'ignore_preferred_server',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'batch-size',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod',
            False, 
            [
            _MetaInfoClassMember('batch-size', REFERENCE_CLASS, 'BatchSize' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize', 
                [], [], 
                '''                Batch size for selection of the server
                ''',
                'batch_size',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'load-balance-method',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.LoadBalanceOptions' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.LoadBalanceOptions',
            False, 
            [
            _MetaInfoClassMember('load-balance-method', REFERENCE_CLASS, 'LoadBalanceMethod' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod', 
                [], [], 
                '''                Method by which the next host will be picked
                ''',
                'load_balance_method',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'load-balance-options',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_ENUM_CLASS, 'AaaConfigEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaConfigEnum', 
                [], [], 
                '''                false/true
                ''',
                'config',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'include-parent-session-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctMultiSessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctMultiSessionId',
            False, 
            [
            _MetaInfoClassMember('include-parent-session-id', REFERENCE_CLASS, 'IncludeParentSessionId' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_ENUM_CLASS, 'AaaConfigEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaConfigEnum', 
                [], [], 
                '''                false/true
                ''',
                'config',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'prepend-nas-port-id',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute.AcctSessionId' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute.AcctSessionId',
            False, 
            [
            _MetaInfoClassMember('prepend-nas-port-id', REFERENCE_CLASS, 'PrependNasPortId' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.RadiusAttribute' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.RadiusAttribute',
            False, 
            [
            _MetaInfoClassMember('acct-multi-session-id', REFERENCE_CLASS, 'AcctMultiSessionId' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctMultiSessionId', 
                [], [], 
                '''                Acct-Session-Id attribute(44)
                ''',
                'acct_multi_session_id',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('acct-session-id', REFERENCE_CLASS, 'AcctSessionId' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute.AcctSessionId', 
                [], [], 
                '''                Acct-Session-Id attribute(44)
                ''',
                'acct_session_id',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'radius-attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Throttle' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Throttle',
            False, 
            [
            _MetaInfoClassMember('access', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                To flow control the number of access requests
                sent to a radius server
                ''',
                'access',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('access-timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                Specify the number of timeouts exceeding which
                a throttled access request is dropped
                ''',
                'access_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('accounting', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                To flow control the number of accounting
                requests sent to a radius server
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name. Specify 'default' for defalut VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                RADIUS packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vrfs' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vrfs.Vrf', 
                [], [], 
                '''                A VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vsa.Attribute.Ignore' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vsa.Attribute.Ignore',
            False, 
            [
            _MetaInfoClassMember('unknown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Ignore the VSA and no prefix will reject the
                unkown VSA 
                ''',
                'unknown',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'ignore',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vsa.Attribute' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vsa.Attribute',
            False, 
            [
            _MetaInfoClassMember('ignore', REFERENCE_CLASS, 'Ignore' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vsa.Attribute.Ignore', 
                [], [], 
                '''                Ignore the VSA 
                ''',
                'ignore',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'attribute',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius.Vsa' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Vsa',
            False, 
            [
            _MetaInfoClassMember('attribute', REFERENCE_CLASS, 'Attribute' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vsa.Attribute', 
                [], [], 
                '''                Vendor Specific Attribute 
                ''',
                'attribute',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'vsa',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Radius' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Attributes', 
                [], [], 
                '''                Table of attribute list
                ''',
                'attributes',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dead-criteria', REFERENCE_CLASS, 'DeadCriteria' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DeadCriteria', 
                [], [], 
                '''                RADIUS server dead criteria
                ''',
                'dead_criteria',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dead-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 1440)], [], 
                '''                This indicates the length of time (in minutes)
                for which a RADIUS server remains marked as
                dead
                ''',
                'dead_time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('disallow', REFERENCE_CLASS, 'Disallow' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Disallow', 
                [], [], 
                '''                disallow null-username
                ''',
                'disallow',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dynamic-authorization', REFERENCE_CLASS, 'DynamicAuthorization' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.DynamicAuthorization', 
                [], [], 
                '''                RADIUS dynamic authorization
                ''',
                'dynamic_authorization',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Hosts', 
                [], [], 
                '''                List of RADIUS servers
                ''',
                'hosts',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
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
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Ipv4', 
                [], [], 
                '''                IPv4 configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Ipv6', 
                [], [], 
                '''                IPv6 configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                RADIUS encryption key
                ''',
                'key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('load-balance-options', REFERENCE_CLASS, 'LoadBalanceOptions' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.LoadBalanceOptions', 
                [], [], 
                '''                Radius load-balancing options
                ''',
                'load_balance_options',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('radius-attribute', REFERENCE_CLASS, 'RadiusAttribute' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.RadiusAttribute', 
                [], [], 
                '''                attribute
                ''',
                'radius_attribute',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('retransmit', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Number of times to retransmit a request to the
                RADIUS server
                ''',
                'retransmit',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('source-port', REFERENCE_CLASS, 'SourcePort' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.SourcePort', 
                [], [], 
                '''                Source port
                ''',
                'source_port',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Throttle', 
                [], [], 
                '''                Radius throttling options
                ''',
                'throttle',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
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
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('vsa', REFERENCE_CLASS, 'Vsa' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius.Vsa', 
                [], [], 
                '''                VSA  ignore configuration for RADIUS server
                ''',
                'vsa',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'radius',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting',
            False, 
            [
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'reply',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'request',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'AaaActionEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_protocol_radius_cfg', 'AaaActionEnum', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization',
            False, 
            [
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'reply',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request', 
                [], [], 
                '''                Specify a filter in server group
                ''',
                'request',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name',
            False, 
            [
            _MetaInfoClassMember('batch-size', ATTRIBUTE, 'int' , None, None, 
                [(1, 1500)], [], 
                '''                Batch size for selection of the server
                ''',
                'batch_size',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('ignore-preferred-server', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Disable preferred server for this Server
                Group
                ''',
                'ignore_preferred_server',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('least-outstanding', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Pick the server with the least transactions
                outstanding
                ''',
                'least_outstanding',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'name',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_CLASS, 'Name' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name', 
                [], [], 
                '''                Batch size for selection of the server
                ''',
                'name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'method',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance',
            False, 
            [
            _MetaInfoClassMember('method', REFERENCE_CLASS, 'Method' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method', 
                [], [], 
                '''                Method by which the next host will be picked
                ''',
                'method',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'load-balance',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer',
            False, 
            [
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of RADIUS server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 60)], [], 
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
                [], ['(!.+)|([^!].+)'], 
                '''                RADIUS encryption key
                ''',
                'private_key',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('private-retransmit', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                Number of times to retransmit a request to
                the RADIUS server
                ''',
                'private_retransmit',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('private-timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers',
            False, 
            [
            _MetaInfoClassMember('private-server', REFERENCE_LIST, 'PrivateServer' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle',
            False, 
            [
            _MetaInfoClassMember('access', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                To flow control the number of access requests
                sent to a radius server
                ''',
                'access',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('access-timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                Specify the number of timeouts exceeding
                which a throttled access request is dropped
                ''',
                'access_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('accounting', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                To flow control the number of accounting
                requests sent to a radius server
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'server-group-throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of RADIUS server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
                ]),
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server', 
                [], [], 
                '''                A server to include in the server group
                ''',
                'server',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Throttle' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Throttle',
            False, 
            [
            _MetaInfoClassMember('access', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                To flow control the number of access requests
                sent to a radius server
                ''',
                'access',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('access-timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                Specify the number of timeouts exceeding which
                a throttled access request is dropped
                ''',
                'access_timeout',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('accounting', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                To flow control the number of accounting
                requests sent to a radius server
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup',
            False, 
            [
            _MetaInfoClassMember('server-group-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                RADIUS server group name
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', True),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting', 
                [], [], 
                '''                List of filters in server group
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('authorization', REFERENCE_CLASS, 'Authorization' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization', 
                [], [], 
                '''                List of filters in server group
                ''',
                'authorization',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('dead-time', ATTRIBUTE, 'int' , None, None, 
                [(1, 1440)], [], 
                '''                This indicates the length of time (in minutes)
                for which RADIUS servers present in this group
                remain marked as dead
                ''',
                'dead_time',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('load-balance', REFERENCE_CLASS, 'LoadBalance' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance', 
                [], [], 
                '''                Radius load-balancing options
                ''',
                'load_balance',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('private-servers', REFERENCE_CLASS, 'PrivateServers' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers', 
                [], [], 
                '''                List of private RADIUS servers present in the
                group
                ''',
                'private_servers',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('server-group-throttle', REFERENCE_CLASS, 'ServerGroupThrottle' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle', 
                [], [], 
                '''                Radius throttling options
                ''',
                'server_group_throttle',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers', 
                [], [], 
                '''                List of RADIUS servers present in the group
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in RADIUS
                packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Throttle', 
                [], [], 
                '''                Radius throttling options
                ''',
                'throttle',
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.RadiusServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.RadiusServerGroups',
            False, 
            [
            _MetaInfoClassMember('radius-server-group', REFERENCE_LIST, 'RadiusServerGroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup', 
                [], [], 
                '''                RADIUS server group name
                ''',
                'radius_server_group',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-cfg',
            'radius-server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of TACACS+ server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                ]),
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Port number (standard 49)
                ''',
                'port_number',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Set TACACS+ encryption key
                ''',
                'key',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 1000)], [], 
                '''                Time to wait for a TACACS+ server to reply
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'private-server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers',
            False, 
            [
            _MetaInfoClassMember('private-server', REFERENCE_LIST, 'PrivateServer' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of TACACS+ server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                ]),
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This is used to sort the servers in the
                order of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server', 
                [], [], 
                '''                A server to include in the server group
                ''',
                'server',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup',
            False, 
            [
            _MetaInfoClassMember('server-group-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                TACACS+ Server group name
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('private-servers', REFERENCE_CLASS, 'PrivateServers' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers', 
                [], [], 
                '''                List of private TACACS servers present in the
                group
                ''',
                'private_servers',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups.TacacsServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups.TacacsServerGroups',
            False, 
            [
            _MetaInfoClassMember('tacacs-server-group', REFERENCE_LIST, 'TacacsServerGroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup', 
                [], [], 
                '''                TACACS+ Server group name
                ''',
                'tacacs_server_group',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'tacacs-server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.ServerGroups' : {
        'meta_info' : _MetaInfoClass('Aaa.ServerGroups',
            False, 
            [
            _MetaInfoClassMember('radius-server-groups', REFERENCE_CLASS, 'RadiusServerGroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.RadiusServerGroups', 
                [], [], 
                '''                RADIUS server group definition
                ''',
                'radius_server_groups',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('tacacs-server-groups', REFERENCE_CLASS, 'TacacsServerGroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups.TacacsServerGroups', 
                [], [], 
                '''                TACACS+ server-group definition
                ''',
                'tacacs_server_groups',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of TACACS+ server
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of TACACS+ server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', True),
                ]),
            _MetaInfoClassMember('ordering-index', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This is used to sort the servers in the order
                of precedence
                ''',
                'ordering_index',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Port number (standard 49)
                ''',
                'port_number',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
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
                [(1, 1000)], [], 
                '''                Time to wait for a TACACS+ server to reply
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Hosts' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Hosts.Host', 
                [], [], 
                '''                One of the TACACS+ servers
                ''',
                'host',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'TacacsDscpValueEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_tacacs_cfg', 'TacacsDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'TacacsDscpValueEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_tacacs_cfg', 'TacacsDscpValueEnum', 
                        [], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [(0, 63)], [], 
                        '''                        Specify the DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-aaa-tacacs-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name. Specify 'default' for default VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-tacacs-cfg', True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                TACACS+ packets
                ''',
                'source_interface',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs.Vrfs' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Vrfs.Vrf', 
                [], [], 
                '''                A VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Tacacs' : {
        'meta_info' : _MetaInfoClass('Aaa.Tacacs',
            False, 
            [
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Hosts', 
                [], [], 
                '''                Specify a TACACS+ server
                ''',
                'hosts',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Ipv4', 
                [], [], 
                '''                IPv4 configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Ipv6', 
                [], [], 
                '''                IPv6 configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
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
                [(1, 1000)], [], 
                '''                Time to wait for a TACACS+ server to reply
                ''',
                'timeout',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-tacacs-cfg',
            'tacacs',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-tacacs-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the task group to include
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup-under-taskgroup', REFERENCE_LIST, 'TaskgroupUnderTaskgroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups.TaskgroupUnderTaskgroup', 
                [], [], 
                '''                Name of the task group to include
                ''',
                'taskgroup_under_taskgroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-taskgroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.Tasks.Task' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.Tasks.Task',
            False, 
            [
            _MetaInfoClassMember('task-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Task ID to which permission is to be granted
                (please use class AllTasks to get a list of
                valid task IDs)
                ''',
                'task_id',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AaaLocaldTaskClassEnum' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_cfg', 'AaaLocaldTaskClassEnum', 
                [], [], 
                '''                This specifies the operation permitted for
                this task eg: read/write/execute/debug
                ''',
                'type',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'task',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.Tasks' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.Tasks',
            False, 
            [
            _MetaInfoClassMember('task', REFERENCE_LIST, 'Task' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.Tasks.Task', 
                [], [], 
                '''                Task ID to be included
                ''',
                'task',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'tasks',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
            _MetaInfoClassMember('taskgroup-under-taskgroups', REFERENCE_CLASS, 'TaskgroupUnderTaskgroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.TaskgroupUnderTaskgroups', 
                [], [], 
                '''                Specify a taskgroup to inherit from
                ''',
                'taskgroup_under_taskgroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('tasks', REFERENCE_CLASS, 'Tasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup.Tasks', 
                [], [], 
                '''                Specify task IDs to be part of this group
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Taskgroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup', REFERENCE_LIST, 'Taskgroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups.Taskgroup', 
                [], [], 
                '''                Taskgroup name
                ''',
                'taskgroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the task group
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup-under-usergroup', REFERENCE_LIST, 'TaskgroupUnderUsergroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups.TaskgroupUnderUsergroup', 
                [], [], 
                '''                Name of the task group
                ''',
                'taskgroup_under_usergroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'taskgroup-under-usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the user group
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups',
            False, 
            [
            _MetaInfoClassMember('usergroup-under-usergroup', REFERENCE_LIST, 'UsergroupUnderUsergroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups.UsergroupUnderUsergroup', 
                [], [], 
                '''                Name of the user group
                ''',
                'usergroup_under_usergroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
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
            _MetaInfoClassMember('taskgroup-under-usergroups', REFERENCE_CLASS, 'TaskgroupUnderUsergroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.TaskgroupUnderUsergroups', 
                [], [], 
                '''                Task group associated with this group
                ''',
                'taskgroup_under_usergroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usergroup-under-usergroups', REFERENCE_CLASS, 'UsergroupUnderUsergroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup.UsergroupUnderUsergroups', 
                [], [], 
                '''                User group to be inherited by this group
                ''',
                'usergroup_under_usergroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups',
            False, 
            [
            _MetaInfoClassMember('usergroup', REFERENCE_LIST, 'Usergroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups.Usergroup', 
                [], [], 
                '''                Usergroup name
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-username',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames.Username.UsergroupUnderUsernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames',
            False, 
            [
            _MetaInfoClassMember('usergroup-under-username', REFERENCE_LIST, 'UsergroupUnderUsername' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername', 
                [], [], 
                '''                Name of the usergroup
                ''',
                'usergroup_under_username',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usergroup-under-usernames',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames.Username' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-cfg', True),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Specify the password for the user
                ''',
                'password',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('secret', ATTRIBUTE, 'str' , None, None, 
                [], ['(!.+)|([^!].+)'], 
                '''                Specify the secret for the user
                ''',
                'secret',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usergroup-under-usernames', REFERENCE_CLASS, 'UsergroupUnderUsernames' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa.Usernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames',
            False, 
            [
            _MetaInfoClassMember('username', REFERENCE_LIST, 'Username' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames.Username', 
                [], [], 
                '''                Local username
                ''',
                'username',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-cfg',
            'usernames',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
    'Aaa' : {
        'meta_info' : _MetaInfoClass('Aaa',
            False, 
            [
            _MetaInfoClassMember('accounting-update', REFERENCE_CLASS, 'AccountingUpdate' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.AccountingUpdate', 
                [], [], 
                '''                Configuration related to 'update' accounting
                ''',
                'accounting_update',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('accountings', REFERENCE_CLASS, 'Accountings' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Accountings', 
                [], [], 
                '''                AAA accounting
                ''',
                'accountings',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('authentications', REFERENCE_CLASS, 'Authentications' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authentications', 
                [], [], 
                '''                AAA authentication
                ''',
                'authentications',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('authorizations', REFERENCE_CLASS, 'Authorizations' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Authorizations', 
                [], [], 
                '''                AAA authorization
                ''',
                'authorizations',
                'Cisco-IOS-XR-aaa-lib-cfg', False),
            _MetaInfoClassMember('default-taskgroup', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This class is used for setting the default
                taskgroup to be used for remote server
                authentication
                ''',
                'default_taskgroup',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('radius', REFERENCE_CLASS, 'Radius' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Radius', 
                [], [], 
                '''                Remote Access Dial-In User Service
                ''',
                'radius',
                'Cisco-IOS-XR-aaa-protocol-radius-cfg', False),
            _MetaInfoClassMember('server-groups', REFERENCE_CLASS, 'ServerGroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.ServerGroups', 
                [], [], 
                '''                AAA group definitions
                ''',
                'server_groups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('tacacs', REFERENCE_CLASS, 'Tacacs' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Tacacs', 
                [], [], 
                '''                Modify TACACS+ query parameters
                ''',
                'tacacs',
                'Cisco-IOS-XR-aaa-tacacs-cfg', False),
            _MetaInfoClassMember('taskgroups', REFERENCE_CLASS, 'Taskgroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Taskgroups', 
                [], [], 
                '''                Specify a taskgroup to inherit from
                ''',
                'taskgroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usergroups', REFERENCE_CLASS, 'Usergroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usergroups', 
                [], [], 
                '''                Specify a Usergroup to inherit from
                ''',
                'usergroups',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            _MetaInfoClassMember('usernames', REFERENCE_CLASS, 'Usernames' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg', 'Aaa.Usernames', 
                [], [], 
                '''                Configure local usernames
                ''',
                'usernames',
                'Cisco-IOS-XR-aaa-locald-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-lib-cfg',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-cfg'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_lib_cfg'
        ),
    },
}
_meta_table['Aaa.Accountings.Accounting']['meta_info'].parent =_meta_table['Aaa.Accountings']['meta_info']
_meta_table['Aaa.Authentications.Authentication']['meta_info'].parent =_meta_table['Aaa.Authentications']['meta_info']
_meta_table['Aaa.Authorizations.Authorization']['meta_info'].parent =_meta_table['Aaa.Authorizations']['meta_info']
_meta_table['Aaa.Radius.Attributes.Attribute']['meta_info'].parent =_meta_table['Aaa.Radius.Attributes']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization.Clients.Client']['meta_info'].parent =_meta_table['Aaa.Radius.DynamicAuthorization.Clients']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization.Clients.ClientVrfName']['meta_info'].parent =_meta_table['Aaa.Radius.DynamicAuthorization.Clients']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization.Clients']['meta_info'].parent =_meta_table['Aaa.Radius.DynamicAuthorization']['meta_info']
_meta_table['Aaa.Radius.Hosts.Host']['meta_info'].parent =_meta_table['Aaa.Radius.Hosts']['meta_info']
_meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod.BatchSize']['meta_info'].parent =_meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod']['meta_info']
_meta_table['Aaa.Radius.LoadBalanceOptions.LoadBalanceMethod']['meta_info'].parent =_meta_table['Aaa.Radius.LoadBalanceOptions']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId.IncludeParentSessionId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId.PrependNasPortId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctMultiSessionId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute.AcctSessionId']['meta_info'].parent =_meta_table['Aaa.Radius.RadiusAttribute']['meta_info']
_meta_table['Aaa.Radius.Vrfs.Vrf']['meta_info'].parent =_meta_table['Aaa.Radius.Vrfs']['meta_info']
_meta_table['Aaa.Radius.Vsa.Attribute.Ignore']['meta_info'].parent =_meta_table['Aaa.Radius.Vsa.Attribute']['meta_info']
_meta_table['Aaa.Radius.Vsa.Attribute']['meta_info'].parent =_meta_table['Aaa.Radius.Vsa']['meta_info']
_meta_table['Aaa.Radius.Attributes']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.DeadCriteria']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Disallow']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.DynamicAuthorization']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Hosts']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Ipv4']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Ipv6']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.LoadBalanceOptions']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.RadiusAttribute']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.SourcePort']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Throttle']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Vrfs']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Vsa']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Reply']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting.Request']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Reply']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization.Request']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method.Name']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance.Method']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers.PrivateServer']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers.Server']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Accounting']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Authorization']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.LoadBalance']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.PrivateServers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.ServerGroupThrottle']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Servers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup.Throttle']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups.RadiusServerGroup']['meta_info'].parent =_meta_table['Aaa.ServerGroups.RadiusServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers.PrivateServer']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers.Server']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.PrivateServers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup.Servers']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups.TacacsServerGroup']['meta_info'].parent =_meta_table['Aaa.ServerGroups.TacacsServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.RadiusServerGroups']['meta_info'].parent =_meta_table['Aaa.ServerGroups']['meta_info']
_meta_table['Aaa.ServerGroups.TacacsServerGroups']['meta_info'].parent =_meta_table['Aaa.ServerGroups']['meta_info']
_meta_table['Aaa.Tacacs.Hosts.Host']['meta_info'].parent =_meta_table['Aaa.Tacacs.Hosts']['meta_info']
_meta_table['Aaa.Tacacs.Vrfs.Vrf']['meta_info'].parent =_meta_table['Aaa.Tacacs.Vrfs']['meta_info']
_meta_table['Aaa.Tacacs.Hosts']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.Ipv4']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.Ipv6']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
_meta_table['Aaa.Tacacs.Vrfs']['meta_info'].parent =_meta_table['Aaa.Tacacs']['meta_info']
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
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername']['meta_info'].parent =_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info']
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info'].parent =_meta_table['Aaa.Usernames.Username']['meta_info']
_meta_table['Aaa.Usernames.Username']['meta_info'].parent =_meta_table['Aaa.Usernames']['meta_info']
_meta_table['Aaa.AccountingUpdate']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Accountings']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Authentications']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Authorizations']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Radius']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.ServerGroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Tacacs']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Taskgroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Usergroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Usernames']['meta_info'].parent =_meta_table['Aaa']['meta_info']
