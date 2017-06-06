


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Radius.Nodes.Node.Client' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.Client',
            False, 
            [
            _MetaInfoClassMember('authentication-nas-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NAS-Identifier of the RADIUS authentication
                client
                ''',
                'authentication_nas_id',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-accounting-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of RADIUS accounting responses packets
                received from unknown addresses
                ''',
                'unknown_accounting_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-authentication-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of RADIUS access responses packets
                received from unknown addresses
                ''',
                'unknown_authentication_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time',
            False, 
            [
            _MetaInfoClassMember('is-computed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if computed; false if not
                ''',
                'is_computed',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value for time or tries
                ''',
                'value',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'time',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries',
            False, 
            [
            _MetaInfoClassMember('is-computed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if computed; false if not
                ''',
                'is_computed',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value for time or tries
                ''',
                'value',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'tries',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.DeadCriteria.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.DeadCriteria.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('acct-port-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Accounting Port number (standard port 1646)
                ''',
                'acct_port_number',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('auth-port-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Authentication Port number (standard port
                1645)
                ''',
                'auth_port_number',
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
            _MetaInfoClassMember('time', REFERENCE_CLASS, 'Time' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time', 
                [], [], 
                '''                Time in seconds
                ''',
                'time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('tries', REFERENCE_CLASS, 'Tries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries', 
                [], [], 
                '''                Number of tries
                ''',
                'tries',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.DeadCriteria.Hosts' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.DeadCriteria.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.DeadCriteria.Hosts.Host', 
                [], [], 
                '''                RADIUS Server
                ''',
                'host',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.DeadCriteria' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.DeadCriteria',
            False, 
            [
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.DeadCriteria.Hosts', 
                [], [], 
                '''                RADIUS server dead criteria host table
                ''',
                'hosts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'dead-criteria',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_',
            False, 
            [
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
                '''                Number of retransmitted access requests
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
                '''                Number of access packets timed out
                ''',
                'access_timeouts',
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
            _MetaInfoClassMember('dropped-access-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access responses dropped
                ''',
                'dropped_access_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-access-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending access requests
                ''',
                'pending_access_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round trip time for authentication in
                milliseconds
                ''',
                'rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-access-types', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with unknown type
                from authentication server
                ''',
                'unknown_access_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.Authentication.AuthenticationGroup' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.Authentication.AuthenticationGroup',
            False, 
            [
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_', 
                [], [], 
                '''                Authentication data
                ''',
                'authentication',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address Family
                ''',
                'family',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address buffer
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication port number
                ''',
                'port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of RADIUS server
                ''',
                'server_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'authentication-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.Authentication' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.Authentication',
            False, 
            [
            _MetaInfoClassMember('authentication-group', REFERENCE_LIST, 'AuthenticationGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.Authentication.AuthenticationGroup', 
                [], [], 
                '''                List of authentication groups
                ''',
                'authentication_group',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_',
            False, 
            [
            _MetaInfoClassMember('acct-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of incorrect accounting responses
                ''',
                'acct_incorrect_responses',
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
            _MetaInfoClassMember('bad-authenticators', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad accounting authenticators
                ''',
                'bad_authenticators',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad accounting responses
                ''',
                'bad_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dropped-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting responses dropped
                ''',
                'dropped_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending accounting requests
                ''',
                'pending_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting requests
                ''',
                'requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting responses
                ''',
                'responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('retransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retransmitted accounting requests
                ''',
                'retransmits',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round trip time for accounting in milliseconds
                ''',
                'rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting packets timed-out
                ''',
                'timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-packet-types', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with unknown type
                from accounting server
                ''',
                'unknown_packet_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.Accounting.AccountingGroup' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.Accounting.AccountingGroup',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_', 
                [], [], 
                '''                Accounting data
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address Family
                ''',
                'family',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address buffer
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting port number
                ''',
                'port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of RADIUS server
                ''',
                'server_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'accounting-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.Accounting' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.Accounting',
            False, 
            [
            _MetaInfoClassMember('accounting-group', REFERENCE_LIST, 'AccountingGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.Accounting.AccountingGroup', 
                [], [], 
                '''                List of accounting groups
                ''',
                'accounting_group',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting',
            False, 
            [
            _MetaInfoClassMember('acct-incorrect-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of incorrect accounting responses
                ''',
                'acct_incorrect_responses',
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
            _MetaInfoClassMember('bad-authenticators', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad accounting authenticators
                ''',
                'bad_authenticators',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('bad-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bad accounting responses
                ''',
                'bad_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dropped-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting responses dropped
                ''',
                'dropped_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending accounting requests
                ''',
                'pending_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting requests
                ''',
                'requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting responses
                ''',
                'responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('retransmits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retransmitted accounting requests
                ''',
                'retransmits',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round trip time for accounting in milliseconds
                ''',
                'rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of accounting packets timed-out
                ''',
                'timeouts',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-packet-types', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with unknown type
                from accounting server
                ''',
                'unknown_packet_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication',
            False, 
            [
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
                '''                Number of retransmitted access requests
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
                '''                Number of access packets timed out
                ''',
                'access_timeouts',
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
            _MetaInfoClassMember('dropped-access-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of access responses dropped
                ''',
                'dropped_access_responses',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('pending-access-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending access requests
                ''',
                'pending_access_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('rtt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Round trip time for authentication in
                milliseconds
                ''',
                'rtt',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('unknown-access-types', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with unknown type
                from authentication server
                ''',
                'unknown_access_types',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization',
            False, 
            [
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
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting', 
                [], [], 
                '''                Accounting data
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('accounting-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accounting port
                ''',
                'accounting_port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication', 
                [], [], 
                '''                Authentication data
                ''',
                'authentication',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication port
                ''',
                'authentication_port',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authorization', REFERENCE_CLASS, 'Authorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization', 
                [], [], 
                '''                Authorization data
                ''',
                'authorization',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address Family
                ''',
                'family',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address buffer
                ''',
                'ip_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('is-private', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if private
                ''',
                'is_private',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Server address
                ''',
                'server_address',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'server-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.ServerGroups.ServerGroup' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.ServerGroups.ServerGroup',
            False, 
            [
            _MetaInfoClassMember('server-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group name
                ''',
                'server_group_name',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', True),
            _MetaInfoClassMember('dead-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dead time in minutes
                ''',
                'dead_time',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('groups', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of groups
                ''',
                'groups',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('server-group', REFERENCE_LIST, 'ServerGroup_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_', 
                [], [], 
                '''                Server groups
                ''',
                'server_group',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('servers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of servers
                ''',
                'servers',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'server-group',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.ServerGroups' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.ServerGroups',
            False, 
            [
            _MetaInfoClassMember('server-group', REFERENCE_LIST, 'ServerGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.ServerGroups.ServerGroup', 
                [], [], 
                '''                RADIUS server group data
                ''',
                'server_group',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'server-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node.DynamicAuthorization' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node.DynamicAuthorization',
            False, 
            [
            _MetaInfoClassMember('disconnected-invalid-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid disconnected requests
                ''',
                'disconnected_invalid_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('invalid-coa-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid change of authorization requests
                ''',
                'invalid_coa_requests',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'dynamic-authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', True),
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.Accounting', 
                [], [], 
                '''                RADIUS accounting data
                ''',
                'accounting',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.Authentication', 
                [], [], 
                '''                RADIUS authentication data
                ''',
                'authentication',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.Client', 
                [], [], 
                '''                RADIUS client data
                ''',
                'client',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dead-criteria', REFERENCE_CLASS, 'DeadCriteria' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.DeadCriteria', 
                [], [], 
                '''                RADIUS dead criteria information
                ''',
                'dead_criteria',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('dynamic-authorization', REFERENCE_CLASS, 'DynamicAuthorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.DynamicAuthorization', 
                [], [], 
                '''                Dynamic authorization data
                ''',
                'dynamic_authorization',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            _MetaInfoClassMember('server-groups', REFERENCE_CLASS, 'ServerGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node.ServerGroups', 
                [], [], 
                '''                RADIUS server group table
                ''',
                'server_groups',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius.Nodes' : {
        'meta_info' : _MetaInfoClass('Radius.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes.Node', 
                [], [], 
                '''                RADIUS operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
    'Radius' : {
        'meta_info' : _MetaInfoClass('Radius',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper', 'Radius.Nodes', 
                [], [], 
                '''                Contains all the nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-aaa-protocol-radius-oper', False),
            ],
            'Cisco-IOS-XR-aaa-protocol-radius-oper',
            'radius',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-protocol-radius-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_protocol_radius_oper'
        ),
    },
}
_meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host.Time']['meta_info'].parent =_meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host']['meta_info']
_meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host.Tries']['meta_info'].parent =_meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host']['meta_info']
_meta_table['Radius.Nodes.Node.DeadCriteria.Hosts.Host']['meta_info'].parent =_meta_table['Radius.Nodes.Node.DeadCriteria.Hosts']['meta_info']
_meta_table['Radius.Nodes.Node.DeadCriteria.Hosts']['meta_info'].parent =_meta_table['Radius.Nodes.Node.DeadCriteria']['meta_info']
_meta_table['Radius.Nodes.Node.Authentication.AuthenticationGroup.Authentication_']['meta_info'].parent =_meta_table['Radius.Nodes.Node.Authentication.AuthenticationGroup']['meta_info']
_meta_table['Radius.Nodes.Node.Authentication.AuthenticationGroup']['meta_info'].parent =_meta_table['Radius.Nodes.Node.Authentication']['meta_info']
_meta_table['Radius.Nodes.Node.Accounting.AccountingGroup.Accounting_']['meta_info'].parent =_meta_table['Radius.Nodes.Node.Accounting.AccountingGroup']['meta_info']
_meta_table['Radius.Nodes.Node.Accounting.AccountingGroup']['meta_info'].parent =_meta_table['Radius.Nodes.Node.Accounting']['meta_info']
_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Accounting']['meta_info'].parent =_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_']['meta_info']
_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authentication']['meta_info'].parent =_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_']['meta_info']
_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_.Authorization']['meta_info'].parent =_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_']['meta_info']
_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup.ServerGroup_']['meta_info'].parent =_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup']['meta_info']
_meta_table['Radius.Nodes.Node.ServerGroups.ServerGroup']['meta_info'].parent =_meta_table['Radius.Nodes.Node.ServerGroups']['meta_info']
_meta_table['Radius.Nodes.Node.Client']['meta_info'].parent =_meta_table['Radius.Nodes.Node']['meta_info']
_meta_table['Radius.Nodes.Node.DeadCriteria']['meta_info'].parent =_meta_table['Radius.Nodes.Node']['meta_info']
_meta_table['Radius.Nodes.Node.Authentication']['meta_info'].parent =_meta_table['Radius.Nodes.Node']['meta_info']
_meta_table['Radius.Nodes.Node.Accounting']['meta_info'].parent =_meta_table['Radius.Nodes.Node']['meta_info']
_meta_table['Radius.Nodes.Node.ServerGroups']['meta_info'].parent =_meta_table['Radius.Nodes.Node']['meta_info']
_meta_table['Radius.Nodes.Node.DynamicAuthorization']['meta_info'].parent =_meta_table['Radius.Nodes.Node']['meta_info']
_meta_table['Radius.Nodes.Node']['meta_info'].parent =_meta_table['Radius.Nodes']['meta_info']
_meta_table['Radius.Nodes']['meta_info'].parent =_meta_table['Radius']['meta_info']
