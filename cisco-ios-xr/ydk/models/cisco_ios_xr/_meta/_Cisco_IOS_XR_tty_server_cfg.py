


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Tty.TtyLines.TtyLine.General' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.General',
            False, 
            [
            _MetaInfoClassMember('absolute-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '10000')], [], 
                '''                Absolute timeout for line disconnection
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '512')], [], 
                '''                Number of lines on a screen.
                ''',
                'length',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '512')], [], 
                '''                Number of characters on a screen line.
                ''',
                'width',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'general',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Telnet' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Telnet',
            False, 
            [
            _MetaInfoClassMember('transparent', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Send a CR as a CR followed by a NULL instead
                of a CRfollowed by a LF
                ''',
                'transparent',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'telnet',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the group
                ''',
                'name',
                'Cisco-IOS-XR-tty-server-cfg', True),
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify as 'root-system' for root-system
                group and 'other' for remaining groups
                ''',
                'category',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'user-group',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.UserGroups' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.UserGroups',
            False, 
            [
            _MetaInfoClassMember('user-group', REFERENCE_LIST, 'UserGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup', 
                [], [], 
                '''                Group to which the user will belong
                ''',
                'user_group',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'user-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.Authorization' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.Authorization',
            False, 
            [
            _MetaInfoClassMember('commands', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For exec (shell) configuration
                ''',
                'commands',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('event-manager', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify 'default' or use an authorization
                list with this name
                ''',
                'event_manager',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('exec', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For starting an exec (shell)
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'authorization',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.Authentication' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.Authentication',
            False, 
            [
            _MetaInfoClassMember('login', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication list name
                ''',
                'login',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa.Accounting' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa.Accounting',
            False, 
            [
            _MetaInfoClassMember('commands', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For exec (shell) configuration
                ''',
                'commands',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('exec', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                For starting an exec (shell)
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Aaa' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Aaa',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.Accounting', 
                [], [], 
                '''                Accounting parameters
                ''',
                'accounting',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.Authentication', 
                [], [], 
                '''                Authentication parameters
                ''',
                'authentication',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('authorization', REFERENCE_CLASS, 'Authorization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.Authorization', 
                [], [], 
                '''                Authorization parameters
                ''',
                'authorization',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('login-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Timeouts for any user input during login
                sequence
                ''',
                'login_timeout',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Configure the password for the user
                ''',
                'password',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('secret', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Configure a secure one way encrypted password
                ''',
                'secret',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('user-groups', REFERENCE_CLASS, 'UserGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa.UserGroups', 
                [], [], 
                '''                Users characteristics
                ''',
                'user_groups',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Exec_.Timeout' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Exec_.Timeout',
            False, 
            [
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '35791')], [], 
                '''                Timeout in minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483')], [], 
                '''                Timeout in seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'timeout',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Exec_' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Exec_',
            False, 
            [
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                'True' to Enable & 'False' to Disable time
                stamp
                ''',
                'time_stamp',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('timeout', REFERENCE_CLASS, 'Timeout' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Exec_.Timeout', 
                [], [], 
                '''                EXEC Timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'exec',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Connection.TransportInput' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection.TransportInput',
            False, 
            [
            _MetaInfoClassMember('none', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Not used
                ''',
                'none',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('protocol1', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol1
                ''',
                'protocol1',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol2
                ''',
                'protocol2',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('select', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolSelectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelectEnum', 
                [], [], 
                '''                Choose transport protocols
                ''',
                'select',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'transport-input',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Connection.TransportOutput' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection.TransportOutput',
            False, 
            [
            _MetaInfoClassMember('none', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Not used
                ''',
                'none',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('protocol1', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol1
                ''',
                'protocol1',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol2
                ''',
                'protocol2',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('select', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolSelectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelectEnum', 
                [], [], 
                '''                Choose transport protocols
                ''',
                'select',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'transport-output',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Connection.SessionTimeout' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection.SessionTimeout',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'TtySessionTimeoutDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtySessionTimeoutDirectionEnum', 
                [], [], 
                '''                Include output traffic as well as input
                traffic
                ''',
                'direction',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '35791')], [], 
                '''                Session timeout interval in minutes
                ''',
                'timeout',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'session-timeout',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.Connection' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.Connection',
            False, 
            [
            _MetaInfoClassMember('acl-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL to filter ingoing connections
                ''',
                'acl_in',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('acl-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL to filter outgoing connections
                ''',
                'acl_out',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('cli-white-space-completion', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Command completion on whitespace
                ''',
                'cli_white_space_completion',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('disconnect-character', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Disconnect character's decimal equivalent value
                or Character 
                ''',
                'disconnect_character',
                'Cisco-IOS-XR-tty-management-cfg', False, [
                    _MetaInfoClassMember('disconnect-character', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(\\p{IsBasicLatin}|\\p{IsLatin-1Supplement})*'], 
                        '''                        Disconnect character's decimal equivalent value
                        or Character 
                        ''',
                        'disconnect_character',
                        'Cisco-IOS-XR-tty-management-cfg', False),
                    _MetaInfoClassMember('disconnect-character', ATTRIBUTE, 'int' , None, None, 
                        [('0', '255')], [], 
                        '''                        Disconnect character's decimal equivalent value
                        or Character 
                        ''',
                        'disconnect_character',
                        'Cisco-IOS-XR-tty-management-cfg', False),
                ]),
            _MetaInfoClassMember('escape-character', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Escape character or ASCII decimal equivalent
                value orspecial strings NONE,DEFAULT,BREAK
                ''',
                'escape_character',
                'Cisco-IOS-XR-tty-management-cfg', False, [
                    _MetaInfoClassMember('escape-character', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((\\p{IsBasicLatin}|\\p{IsLatin-1Supplement})*)|(DEFAULT)|(BREAK)|(NONE)'], 
                        '''                        Escape character or ASCII decimal equivalent
                        value orspecial strings NONE,DEFAULT,BREAK
                        ''',
                        'escape_character',
                        'Cisco-IOS-XR-tty-management-cfg', False),
                    _MetaInfoClassMember('escape-character', ATTRIBUTE, 'int' , None, None, 
                        [('0', '255')], [], 
                        '''                        Escape character or ASCII decimal equivalent
                        value orspecial strings NONE,DEFAULT,BREAK
                        ''',
                        'escape_character',
                        'Cisco-IOS-XR-tty-management-cfg', False),
                ]),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '20')], [], 
                '''                The number of outgoing connections
                ''',
                'session_limit',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('session-timeout', REFERENCE_CLASS, 'SessionTimeout' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection.SessionTimeout', 
                [], [], 
                '''                Interval for closing connection when there is
                no input traffic
                ''',
                'session_timeout',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('transport-input', REFERENCE_CLASS, 'TransportInput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection.TransportInput', 
                [], [], 
                '''                Protocols to use when connecting to the
                terminal server
                ''',
                'transport_input',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('transport-output', REFERENCE_CLASS, 'TransportOutput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection.TransportOutput', 
                [], [], 
                '''                Protocols to use for outgoing connections
                ''',
                'transport_output',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('transport-preferred', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                The preferred protocol to use
                ''',
                'transport_preferred',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'connection',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine.ExecMode' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine.ExecMode',
            False, 
            [
            _MetaInfoClassMember('pager', REFERENCE_ENUM_CLASS, 'TtyPagerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyPagerEnum', 
                [], [], 
                '''                Preferred Paging Utility
                ''',
                'pager',
                'Cisco-IOS-XR-tty-management-cfg', False),
            ],
            'Cisco-IOS-XR-tty-management-cfg',
            'exec-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines.TtyLine' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines.TtyLine',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the template
                ''',
                'name',
                'Cisco-IOS-XR-tty-server-cfg', True),
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Aaa', 
                [], [], 
                '''                Container class for AAA related TTY
                configuration
                ''',
                'aaa',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('connection', REFERENCE_CLASS, 'Connection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Connection', 
                [], [], 
                '''                Management connection configuration
                ''',
                'connection',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('exec', REFERENCE_CLASS, 'Exec_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Exec_', 
                [], [], 
                '''                EXEC timeout and timestamp configurtion
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('exec-mode', REFERENCE_CLASS, 'ExecMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.ExecMode', 
                [], [], 
                '''                Exec Mode Pager  configurtion
                ''',
                'exec_mode',
                'Cisco-IOS-XR-tty-management-cfg', False),
            _MetaInfoClassMember('general', REFERENCE_CLASS, 'General' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.General', 
                [], [], 
                '''                TTY line general configuration
                ''',
                'general',
                'Cisco-IOS-XR-tty-server-cfg', False),
            _MetaInfoClassMember('telnet', REFERENCE_CLASS, 'Telnet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine.Telnet', 
                [], [], 
                '''                Telnet protocol-specific configuration
                ''',
                'telnet',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'tty-line',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty.TtyLines' : {
        'meta_info' : _MetaInfoClass('Tty.TtyLines',
            False, 
            [
            _MetaInfoClassMember('tty-line', REFERENCE_LIST, 'TtyLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines.TtyLine', 
                [], [], 
                '''                TTY Line,Use string 'console' to configure a
                console line,Use string 'default' to configure
                a default line,Use any string to configure a
                user defined template
                ''',
                'tty_line',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'tty-lines',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
    'Tty' : {
        'meta_info' : _MetaInfoClass('Tty',
            False, 
            [
            _MetaInfoClassMember('tty-lines', REFERENCE_CLASS, 'TtyLines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg', 'Tty.TtyLines', 
                [], [], 
                '''                TTY templates
                ''',
                'tty_lines',
                'Cisco-IOS-XR-tty-server-cfg', False),
            ],
            'Cisco-IOS-XR-tty-server-cfg',
            'tty',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_cfg'
        ),
    },
}
_meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups.UserGroup']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.UserGroups']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.Authorization']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.Authentication']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa.Accounting']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Exec_.Timeout']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Exec_']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection.TransportInput']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection.TransportOutput']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection.SessionTimeout']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.General']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Telnet']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Aaa']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Exec_']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.Connection']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine.ExecMode']['meta_info'].parent =_meta_table['Tty.TtyLines.TtyLine']['meta_info']
_meta_table['Tty.TtyLines.TtyLine']['meta_info'].parent =_meta_table['Tty.TtyLines']['meta_info']
_meta_table['Tty.TtyLines']['meta_info'].parent =_meta_table['Tty']['meta_info']
