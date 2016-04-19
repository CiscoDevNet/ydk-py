


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.AuthenMethod' : {
        'meta_info' : _MetaInfoClass('Aaa.AuthenMethod',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.CurrentUsergroup' : {
        'meta_info' : _MetaInfoClass('Aaa.CurrentUsergroup',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.CurrentuserDetail' : {
        'meta_info' : _MetaInfoClass('Aaa.CurrentuserDetail',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.Global' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Global',
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
                [(0, 4294967295)], [], 
                '''                Number of RADIUS Accounting-Responsepackets
                received from unknownaddresses
                ''',
                'unknown_accounting_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-authentication-response', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of RADIUS Access-Responsepackets received
                from unknownaddresses
                ''',
                'unknown_authentication_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.Servers.Server' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Servers.Server',
            False, 
            [
            _MetaInfoClassMember('aborts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of requests aborted
                ''',
                'aborts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-accepts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access accepts
                ''',
                'access_accepts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-challenges', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access challenges
                ''',
                'access_challenges',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-rejects', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access rejects
                ''',
                'access_rejects',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-request-retransmits', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of retransmitted                         
                access requests
                ''',
                'access_request_retransmits',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-requests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access requests
                ''',
                'access_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('access-timeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access packets timed-out
                ''',
                'access_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Accounting port
                ''',
                'accounting_port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-requests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of accounting requests
                ''',
                'accounting_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of accounting responses
                ''',
                'accounting_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-retransmits', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of retransmitted                         
                accounting requests
                ''',
                'accounting_retransmits',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-rtt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Round-trip time for accounting                  
                in milliseconds
                ''',
                'accounting_rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-timeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of accounting packets                    
                timed-out
                ''',
                'accounting_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of incorrect accounting responses
                ''',
                'acct_incorrect_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-response-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average response time for authentication
                requests
                ''',
                'acct_response_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-server-error-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of server error accounting responses
                ''',
                'acct_server_error_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-transaction-failure', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of failed authentication transactions
                ''',
                'acct_transaction_failure',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-transaction-successess', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of succeeded authentication transactions
                ''',
                'acct_transaction_successess',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('acct-unexpected-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of unexpected accounting responses
                ''',
                'acct_unexpected_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of incorrect authentication responses
                ''',
                'authen_incorrect_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-response-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average response time for authentication
                requests
                ''',
                'authen_response_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-server-error-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of server error authentication responses
                ''',
                'authen_server_error_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-transaction-failure', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of failed authentication transactions
                ''',
                'authen_transaction_failure',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-transaction-successess', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of succeeded authentication transactions
                ''',
                'authen_transaction_successess',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authen-unexpected-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of unexpected authentication responses
                ''',
                'authen_unexpected_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Authentication port
                ''',
                'authentication_port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication-rtt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Round-trip time for authentication              
                in milliseconds
                ''',
                'authentication_rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of incorrect authorization responses
                ''',
                'author_incorrect_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-request-timeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access packets timed out
                ''',
                'author_request_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-requests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access requests
                ''',
                'author_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-response-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average response time for authorization requests
                ''',
                'author_response_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-server-error-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of server error authorization responses
                ''',
                'author_server_error_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-transaction-failure', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of failed authorization transactions
                ''',
                'author_transaction_failure',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-transaction-successess', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of succeeded authorization transactions
                ''',
                'author_transaction_successess',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('author-unexpected-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of unexpected authorization responses
                ''',
                'author_unexpected_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-access-authenticators', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bad access authenticators
                ''',
                'bad_access_authenticators',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-access-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bad access responses
                ''',
                'bad_access_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-accounting-authenticators', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bad accounting                        
                authenticators
                ''',
                'bad_accounting_authenticators',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-accounting-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bad accounting responses
                ''',
                'bad_accounting_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('current-state-duration', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Elapsed time the server has been in             
                current state
                ''',
                'current_state_duration',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('currently-throttled-access-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                No of currently throttled access reqs
                ''',
                'currently_throttled_access_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dead-detect-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Per-server dead-detect time in seconds
                ''',
                'dead_detect_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dead-detect-tries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Per-server dead-detect tries
                ''',
                'dead_detect_tries',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dead-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Per-server deadtime in minutes
                ''',
                'dead_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dropped-access-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of access responses dropped
                ''',
                'dropped_access_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dropped-accounting-responses', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of RADIUS server
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
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
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
                [(0, 4294967295)], [], 
                '''                Time of Server being in DEAD state,             
                after last UP
                ''',
                'last_deadtime',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('max-acct-throttled', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Max throttled acct transactions
                ''',
                'max_acct_throttled',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('max-throttled-access-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Max throttled access reqs
                ''',
                'max_throttled_access_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('packets-in', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of incoming packets read
                ''',
                'packets_in',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('packets-out', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of outgoing packets sent
                ''',
                'packets_out',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-access-requests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of pending access requests
                ''',
                'pending_access_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-accounting-requets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of pending accounting requests
                ''',
                'pending_accounting_requets',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('previous-state-duration', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Elapsed time the server was been in             
                previous state
                ''',
                'previous_state_duration',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A number that indicates the priority            
                of the server
                ''',
                'priority',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('redirected-requests', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of requests redirected
                ''',
                'redirected_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('replies-expected', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of replies expected to arrive
                ''',
                'replies_expected',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('retransmit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                No of throttled access reqs stats
                ''',
                'throttled_access_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-acct-failures-stats', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                No of acct discarded transaction
                ''',
                'throttled_acct_failures_stats',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-acct-timed-out-stats', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                No of acct transaction that is throttled is
                timedout
                ''',
                'throttled_acct_timed_out_stats',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-acct-transactions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                No of throttled acct transactions stats
                ''',
                'throttled_acct_transactions',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-dropped-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                No of discarded access reqs
                ''',
                'throttled_dropped_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttled-timed-out-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                No of access reqs that is throttled is timedout
                ''',
                'throttled_timed_out_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('throttleda-acct-transactions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                No of currently throttled acct transactions
                ''',
                'throttleda_acct_transactions',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('timeout-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Per-server timeout in seconds
                ''',
                'timeout_xr',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of packets timed-out
                ''',
                'timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-deadtime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total time of Server being in DEAD              
                state
                ''',
                'total_deadtime',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-pending', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total acct test pending
                ''',
                'total_test_acct_pending',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                 Total acct test req
                ''',
                'total_test_acct_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-response', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total acct test response
                ''',
                'total_test_acct_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-acct-timeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total acct test timeouts
                ''',
                'total_test_acct_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-pending', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total auth test pending
                ''',
                'total_test_auth_pending',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total auth test request
                ''',
                'total_test_auth_reqs',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-response', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total auth test response
                ''',
                'total_test_auth_response',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('total-test-auth-timeouts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total auth test timeouts
                ''',
                'total_test_auth_timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-access-types', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets received with unknown         
                type from authentication server
                ''',
                'unknown_access_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-accounting-types', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets received with unknown         
                type from accounting server
                ''',
                'unknown_accounting_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius.Servers' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius.Servers',
            False, 
            [
            _MetaInfoClassMember('server', REFERENCE_LIST, 'Server' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.Servers.Server', 
                [], [], 
                '''                RADIUS Server
                ''',
                'server',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'servers',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Radius' : {
        'meta_info' : _MetaInfoClass('Aaa.Radius',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.Global', 
                [], [], 
                '''                RADIUS Client Information
                ''',
                'global_',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('servers', REFERENCE_CLASS, 'Servers' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius.Servers', 
                [], [], 
                '''                List of RADIUS servers configured
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'radius',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.TaskMap',
            False, 
            [
            _MetaInfoClassMember('authenmethod', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.IncludedTaskIds' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.IncludedTaskIds',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'included-task-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups.Taskgroup.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups.Taskgroup.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
            _MetaInfoClassMember('included-task-ids', REFERENCE_CLASS, 'IncludedTaskIds' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.IncludedTaskIds', 
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
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup.TaskMap', 
                [], [], 
                '''                Computed task map
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Taskgroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Taskgroups',
            False, 
            [
            _MetaInfoClassMember('taskgroup', REFERENCE_LIST, 'Taskgroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups.Taskgroup', 
                [], [], 
                '''                Specific Taskgroup Information
                ''',
                'taskgroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'taskgroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'included-task-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups.Usergroup.Taskgroup' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups.Usergroup.Taskgroup',
            False, 
            [
            _MetaInfoClassMember('included-task-ids', REFERENCE_CLASS, 'IncludedTaskIds' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds', 
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
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup.TaskMap', 
                [], [], 
                '''                Computed task map
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'taskgroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.TaskMap', 
                [], [], 
                '''                Computed task map
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskgroup', REFERENCE_LIST, 'Taskgroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup.Taskgroup', 
                [], [], 
                '''                Component taskgroups
                ''',
                'taskgroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'usergroup',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Usergroups' : {
        'meta_info' : _MetaInfoClass('Aaa.Usergroups',
            False, 
            [
            _MetaInfoClassMember('usergroup', REFERENCE_LIST, 'Usergroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups.Usergroup', 
                [], [], 
                '''                Specific Usergroup Information
                ''',
                'usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'usergroups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Users.User.TaskMap' : {
        'meta_info' : _MetaInfoClass('Aaa.Users.User.TaskMap',
            False, 
            [
            _MetaInfoClassMember('tasks', REFERENCE_LIST, 'Tasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users.User.TaskMap.Tasks', 
                [], [], 
                '''                List of permitted tasks
                ''',
                'tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'task-map',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
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
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users.User.TaskMap', 
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
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa.Users' : {
        'meta_info' : _MetaInfoClass('Aaa.Users',
            False, 
            [
            _MetaInfoClassMember('user', REFERENCE_LIST, 'User' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users.User', 
                [], [], 
                '''                Specific local user information
                ''',
                'user',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'users',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
    'Aaa' : {
        'meta_info' : _MetaInfoClass('Aaa',
            False, 
            [
            _MetaInfoClassMember('all-tasks', REFERENCE_CLASS, 'AllTasks' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.AllTasks', 
                [], [], 
                '''                All tasks supported by system
                ''',
                'all_tasks',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('authen-method', REFERENCE_CLASS, 'AuthenMethod' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.AuthenMethod', 
                [], [], 
                '''                Current users authentication method
                ''',
                'authen_method',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('current-usergroup', REFERENCE_CLASS, 'CurrentUsergroup' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.CurrentUsergroup', 
                [], [], 
                '''                Specific Usergroup Information
                ''',
                'current_usergroup',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('currentuser-detail', REFERENCE_CLASS, 'CurrentuserDetail' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.CurrentuserDetail', 
                [], [], 
                '''                Current user specific details
                ''',
                'currentuser_detail',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('radius', REFERENCE_CLASS, 'Radius' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Radius', 
                [], [], 
                '''                RADIUS operational data
                ''',
                'radius',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('task-map', REFERENCE_CLASS, 'TaskMap' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.TaskMap', 
                [], [], 
                '''                Task map of current user
                ''',
                'task_map',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('taskgroups', REFERENCE_CLASS, 'Taskgroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Taskgroups', 
                [], [], 
                '''                Individual taskgroups container
                ''',
                'taskgroups',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('usergroups', REFERENCE_CLASS, 'Usergroups' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Usergroups', 
                [], [], 
                '''                Container for individual usergroup Information
                ''',
                'usergroups',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            _MetaInfoClassMember('users', REFERENCE_CLASS, 'Users' , 'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper', 'Aaa.Users', 
                [], [], 
                '''                Container for individual local user information
                ''',
                'users',
                'Cisco-IOS-XR-aaa-locald-oper', False),
            ],
            'Cisco-IOS-XR-aaa-locald-oper',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-oper'],
        'ydk.models.aaa.Cisco_IOS_XR_aaa_locald_oper'
        ),
    },
}
_meta_table['Aaa.Radius.Servers.Server']['meta_info'].parent =_meta_table['Aaa.Radius.Servers']['meta_info']
_meta_table['Aaa.Radius.Global']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Radius.Servers']['meta_info'].parent =_meta_table['Aaa.Radius']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds.Tasks']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup.TaskMap']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.IncludedTaskIds']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup.TaskMap']['meta_info'].parent =_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info']
_meta_table['Aaa.Taskgroups.Taskgroup']['meta_info'].parent =_meta_table['Aaa.Taskgroups']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.TaskMap']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds.Tasks']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.IncludedTaskIds']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup.TaskMap']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.TaskMap']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup.Taskgroup']['meta_info'].parent =_meta_table['Aaa.Usergroups.Usergroup']['meta_info']
_meta_table['Aaa.Usergroups.Usergroup']['meta_info'].parent =_meta_table['Aaa.Usergroups']['meta_info']
_meta_table['Aaa.Users.User.TaskMap.Tasks']['meta_info'].parent =_meta_table['Aaa.Users.User.TaskMap']['meta_info']
_meta_table['Aaa.Users.User.TaskMap']['meta_info'].parent =_meta_table['Aaa.Users.User']['meta_info']
_meta_table['Aaa.Users.User']['meta_info'].parent =_meta_table['Aaa.Users']['meta_info']
_meta_table['Aaa.AllTasks']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.AuthenMethod']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.CurrentUsergroup']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.CurrentuserDetail']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Radius']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.TaskMap']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Taskgroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Usergroups']['meta_info'].parent =_meta_table['Aaa']['meta_info']
_meta_table['Aaa.Users']['meta_info'].parent =_meta_table['Aaa']['meta_info']
