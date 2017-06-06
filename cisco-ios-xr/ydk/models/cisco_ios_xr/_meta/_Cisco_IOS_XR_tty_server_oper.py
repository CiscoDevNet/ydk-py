


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SessionOperationEnum' : _MetaInfoEnum('SessionOperationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper',
        {
            'none':'none',
            'setup':'setup',
            'shell':'shell',
            'transitioning':'transitioning',
            'packet':'packet',
        }, 'Cisco-IOS-XR-tty-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper']),
    'LineStateEnum' : _MetaInfoEnum('LineStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper',
        {
            'none':'none',
            'registered':'registered',
            'in-use':'in_use',
        }, 'Cisco-IOS-XR-tty-server-oper', _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper']),
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232',
            False, 
            [
            _MetaInfoClassMember('baud-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound/Outbound baud rate in bps
                ''',
                'baud_rate',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('data-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of databits
                ''',
                'data_bits',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('exec-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Exec disabled on TTY
                ''',
                'exec_disabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('framing-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Framing error count
                ''',
                'framing_error_count',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('hardware-flow-control-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware flow control status
                ''',
                'hardware_flow_control_status',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('overrun-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Overrun error count
                ''',
                'overrun_error_count',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('parity-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parity error count
                ''',
                'parity_error_count',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('parity-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parity status
                ''',
                'parity_status',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('stop-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of stopbits
                ''',
                'stop_bits',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'rs232',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics',
            False, 
            [
            _MetaInfoClassMember('absolute-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Absolute timeout period
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('async-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Usable as async interface
                ''',
                'async_interface',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('domain-lookup-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DNS resolution enabled
                ''',
                'domain_lookup_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('flow-control-start-character', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Software flow control start char
                ''',
                'flow_control_start_character',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('flow-control-stop-character', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Software flow control stop char
                ''',
                'flow_control_stop_character',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TTY idle time
                ''',
                'idle_time',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('motd-banner-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MOTD banner enabled
                ''',
                'motd_banner_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('private-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TTY private flag
                ''',
                'private_flag',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Terminal length
                ''',
                'terminal_length',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Terminal type
                ''',
                'terminal_type',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Line width
                ''',
                'terminal_width',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'general-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_',
            False, 
            [
            _MetaInfoClassMember('time-stamp-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether timestamp is enabled or not
                ''',
                'time_stamp_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'exec',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa',
            False, 
            [
            _MetaInfoClassMember('user-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The authenticated username
                ''',
                'user_name',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics',
            False, 
            [
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa', 
                [], [], 
                '''                AAA related statistics
                ''',
                'aaa',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('exec', REFERENCE_CLASS, 'Exec_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_', 
                [], [], 
                '''                Exec related statistics
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('general-statistics', REFERENCE_CLASS, 'GeneralStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics', 
                [], [], 
                '''                General statistics of line
                ''',
                'general_statistics',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('rs232', REFERENCE_CLASS, 'Rs232' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232', 
                [], [], 
                '''                RS232 statistics of console line
                ''',
                'rs232',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'console-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the template
                ''',
                'name',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General',
            False, 
            [
            _MetaInfoClassMember('general-state', REFERENCE_ENUM_CLASS, 'LineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'LineStateEnum', 
                [], [], 
                '''                State of the line
                ''',
                'general_state',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'SessionOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'SessionOperationEnum', 
                [], [], 
                '''                application running of on the tty line
                ''',
                'operation',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'general',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State',
            False, 
            [
            _MetaInfoClassMember('general', REFERENCE_CLASS, 'General' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General', 
                [], [], 
                '''                General information
                ''',
                'general',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('template', REFERENCE_CLASS, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template', 
                [], [], 
                '''                Information related to template applied to the
                line
                ''',
                'template',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput',
            False, 
            [
            _MetaInfoClassMember('none', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Not used
                ''',
                'none',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('protocol1', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol1
                ''',
                'protocol1',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol2
                ''',
                'protocol2',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('select', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolSelectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelectEnum', 
                [], [], 
                '''                Choose transport protocols
                ''',
                'select',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'transport-input',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration',
            False, 
            [
            _MetaInfoClassMember('acl-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL for inbound traffic
                ''',
                'acl_in',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('acl-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL for outbound traffic
                ''',
                'acl_out',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('transport-input', REFERENCE_CLASS, 'TransportInput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput', 
                [], [], 
                '''                Protocols to use when connecting to the
                terminal server
                ''',
                'transport_input',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'connection-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration',
            False, 
            [
            _MetaInfoClassMember('connection-configuration', REFERENCE_CLASS, 'ConnectionConfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration', 
                [], [], 
                '''                Conection configuration information
                ''',
                'connection_configuration',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode.ConsoleLine' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode.ConsoleLine',
            False, 
            [
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration', 
                [], [], 
                '''                Configuration information of the line
                ''',
                'configuration',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('console-statistics', REFERENCE_CLASS, 'ConsoleStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics', 
                [], [], 
                '''                Statistics of the console line
                ''',
                'console_statistics',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State', 
                [], [], 
                '''                Line state information
                ''',
                'state',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'console-line',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes.ConsoleNode' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes.ConsoleNode',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'id',
                'Cisco-IOS-XR-tty-server-oper', True),
            _MetaInfoClassMember('console-line', REFERENCE_CLASS, 'ConsoleLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode.ConsoleLine', 
                [], [], 
                '''                Console line
                ''',
                'console_line',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'console-node',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.ConsoleNodes' : {
        'meta_info' : _MetaInfoClass('Tty.ConsoleNodes',
            False, 
            [
            _MetaInfoClassMember('console-node', REFERENCE_LIST, 'ConsoleNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes.ConsoleNode', 
                [], [], 
                '''                Console line configuration on a node
                ''',
                'console_node',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'console-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.VtyStatistics.Connection' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.VtyStatistics.Connection',
            False, 
            [
            _MetaInfoClassMember('host-address-family', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming host address family
                ''',
                'host_address_family',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('incoming-host-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 46)], [], 
                '''                Incoming host address(max)
                ''',
                'incoming_host_address',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('service', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input transport
                ''',
                'service',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'connection',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics',
            False, 
            [
            _MetaInfoClassMember('absolute-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Absolute timeout period
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('async-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Usable as async interface
                ''',
                'async_interface',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('domain-lookup-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DNS resolution enabled
                ''',
                'domain_lookup_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('flow-control-start-character', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Software flow control start char
                ''',
                'flow_control_start_character',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('flow-control-stop-character', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Software flow control stop char
                ''',
                'flow_control_stop_character',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TTY idle time
                ''',
                'idle_time',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('motd-banner-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MOTD banner enabled
                ''',
                'motd_banner_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('private-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TTY private flag
                ''',
                'private_flag',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Terminal length
                ''',
                'terminal_length',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Terminal type
                ''',
                'terminal_type',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Line width
                ''',
                'terminal_width',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'general-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.VtyStatistics.Exec_' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.VtyStatistics.Exec_',
            False, 
            [
            _MetaInfoClassMember('time-stamp-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether timestamp is enabled or not
                ''',
                'time_stamp_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'exec',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.VtyStatistics.Aaa' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.VtyStatistics.Aaa',
            False, 
            [
            _MetaInfoClassMember('user-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The authenticated username
                ''',
                'user_name',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.VtyStatistics' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.VtyStatistics',
            False, 
            [
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.VtyStatistics.Aaa', 
                [], [], 
                '''                AAA related statistics
                ''',
                'aaa',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('connection', REFERENCE_CLASS, 'Connection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.VtyStatistics.Connection', 
                [], [], 
                '''                Connection related statistics
                ''',
                'connection',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('exec', REFERENCE_CLASS, 'Exec_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.VtyStatistics.Exec_', 
                [], [], 
                '''                Exec related statistics
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('general-statistics', REFERENCE_CLASS, 'GeneralStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics', 
                [], [], 
                '''                General statistics of line
                ''',
                'general_statistics',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'vty-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.State.Template' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.State.Template',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the template
                ''',
                'name',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.State.General' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.State.General',
            False, 
            [
            _MetaInfoClassMember('general-state', REFERENCE_ENUM_CLASS, 'LineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'LineStateEnum', 
                [], [], 
                '''                State of the line
                ''',
                'general_state',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'SessionOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'SessionOperationEnum', 
                [], [], 
                '''                application running of on the tty line
                ''',
                'operation',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'general',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.State' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.State',
            False, 
            [
            _MetaInfoClassMember('general', REFERENCE_CLASS, 'General' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.State.General', 
                [], [], 
                '''                General information
                ''',
                'general',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('template', REFERENCE_CLASS, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.State.Template', 
                [], [], 
                '''                Information related to template applied to the
                line
                ''',
                'template',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput',
            False, 
            [
            _MetaInfoClassMember('none', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Not used
                ''',
                'none',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('protocol1', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol1
                ''',
                'protocol1',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol2
                ''',
                'protocol2',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('select', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolSelectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelectEnum', 
                [], [], 
                '''                Choose transport protocols
                ''',
                'select',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'transport-input',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration',
            False, 
            [
            _MetaInfoClassMember('acl-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL for inbound traffic
                ''',
                'acl_in',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('acl-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL for outbound traffic
                ''',
                'acl_out',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('transport-input', REFERENCE_CLASS, 'TransportInput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput', 
                [], [], 
                '''                Protocols to use when connecting to the
                terminal server
                ''',
                'transport_input',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'connection-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.Configuration' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.Configuration',
            False, 
            [
            _MetaInfoClassMember('connection-configuration', REFERENCE_CLASS, 'ConnectionConfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration', 
                [], [], 
                '''                Conection configuration information
                ''',
                'connection_configuration',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'HostAfIdBaseIdentity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper', 'HostAfIdBaseIdentity', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-tty-management-oper', False),
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'host-address',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.Sessions.OutgoingConnection' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.Sessions.OutgoingConnection',
            False, 
            [
            _MetaInfoClassMember('connection-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Connection ID [1-20]
                ''',
                'connection_id',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('host-address', REFERENCE_CLASS, 'HostAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress', 
                [], [], 
                '''                Host address
                ''',
                'host_address',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Host name
                ''',
                'host_name',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Elapsed time since session was suspended (in
                seconds)
                ''',
                'idle_time',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('is-last-active-session', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True indicates last active session
                ''',
                'is_last_active_session',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('transport-protocol', REFERENCE_ENUM_CLASS, 'TransportServiceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_oper', 'TransportServiceEnum', 
                [], [], 
                '''                Session transport protocol
                ''',
                'transport_protocol',
                'Cisco-IOS-XR-tty-management-oper', False),
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'outgoing-connection',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine.Sessions' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine.Sessions',
            False, 
            [
            _MetaInfoClassMember('outgoing-connection', REFERENCE_LIST, 'OutgoingConnection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.Sessions.OutgoingConnection', 
                [], [], 
                '''                List of outgoing sessions
                ''',
                'outgoing_connection',
                'Cisco-IOS-XR-tty-management-oper', False),
            ],
            'Cisco-IOS-XR-tty-management-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-management-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines.VtyLine' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines.VtyLine',
            False, 
            [
            _MetaInfoClassMember('line-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                VTY Line number
                ''',
                'line_number',
                'Cisco-IOS-XR-tty-server-oper', True),
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.Configuration', 
                [], [], 
                '''                Configuration information of the line
                ''',
                'configuration',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.Sessions', 
                [], [], 
                '''                Outgoing sessions
                ''',
                'sessions',
                'Cisco-IOS-XR-tty-management-oper', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.State', 
                [], [], 
                '''                Line state information
                ''',
                'state',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('vty-statistics', REFERENCE_CLASS, 'VtyStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine.VtyStatistics', 
                [], [], 
                '''                Statistics of the VTY line
                ''',
                'vty_statistics',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'vty-line',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.VtyLines' : {
        'meta_info' : _MetaInfoClass('Tty.VtyLines',
            False, 
            [
            _MetaInfoClassMember('vty-line', REFERENCE_LIST, 'VtyLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines.VtyLine', 
                [], [], 
                '''                VTY Line
                ''',
                'vty_line',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'vty-lines',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232',
            False, 
            [
            _MetaInfoClassMember('baud-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inbound/Outbound baud rate in bps
                ''',
                'baud_rate',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('data-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of databits
                ''',
                'data_bits',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('exec-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Exec disabled on TTY
                ''',
                'exec_disabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('framing-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Framing error count
                ''',
                'framing_error_count',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('hardware-flow-control-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware flow control status
                ''',
                'hardware_flow_control_status',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('overrun-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Overrun error count
                ''',
                'overrun_error_count',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('parity-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parity error count
                ''',
                'parity_error_count',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('parity-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parity status
                ''',
                'parity_status',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('stop-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of stopbits
                ''',
                'stop_bits',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'rs232',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics',
            False, 
            [
            _MetaInfoClassMember('absolute-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Absolute timeout period
                ''',
                'absolute_timeout',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('async-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Usable as async interface
                ''',
                'async_interface',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('domain-lookup-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DNS resolution enabled
                ''',
                'domain_lookup_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('flow-control-start-character', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Software flow control start char
                ''',
                'flow_control_start_character',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('flow-control-stop-character', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                Software flow control stop char
                ''',
                'flow_control_stop_character',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('idle-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TTY idle time
                ''',
                'idle_time',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('motd-banner-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MOTD banner enabled
                ''',
                'motd_banner_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('private-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TTY private flag
                ''',
                'private_flag',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Terminal length
                ''',
                'terminal_length',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Terminal type
                ''',
                'terminal_type',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('terminal-width', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Line width
                ''',
                'terminal_width',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'general-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_',
            False, 
            [
            _MetaInfoClassMember('time-stamp-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether timestamp is enabled or not
                ''',
                'time_stamp_enabled',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'exec',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa',
            False, 
            [
            _MetaInfoClassMember('user-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The authenticated username
                ''',
                'user_name',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics',
            False, 
            [
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa', 
                [], [], 
                '''                AAA related statistics
                ''',
                'aaa',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('exec', REFERENCE_CLASS, 'Exec_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_', 
                [], [], 
                '''                Exec related statistics
                ''',
                'exec_',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('general-statistics', REFERENCE_CLASS, 'GeneralStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics', 
                [], [], 
                '''                General statistics of line
                ''',
                'general_statistics',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('rs232', REFERENCE_CLASS, 'Rs232' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232', 
                [], [], 
                '''                RS232 statistics of console line
                ''',
                'rs232',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'auxiliary-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the template
                ''',
                'name',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General',
            False, 
            [
            _MetaInfoClassMember('general-state', REFERENCE_ENUM_CLASS, 'LineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'LineStateEnum', 
                [], [], 
                '''                State of the line
                ''',
                'general_state',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'SessionOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'SessionOperationEnum', 
                [], [], 
                '''                application running of on the tty line
                ''',
                'operation',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'general',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State',
            False, 
            [
            _MetaInfoClassMember('general', REFERENCE_CLASS, 'General' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General', 
                [], [], 
                '''                General information
                ''',
                'general',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('template', REFERENCE_CLASS, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template', 
                [], [], 
                '''                Information related to template applied to the
                line
                ''',
                'template',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput',
            False, 
            [
            _MetaInfoClassMember('none', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Not used
                ''',
                'none',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('protocol1', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol1
                ''',
                'protocol1',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolEnum', 
                [], [], 
                '''                Transport protocol2
                ''',
                'protocol2',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('select', REFERENCE_ENUM_CLASS, 'TtyTransportProtocolSelectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_management_datatypes', 'TtyTransportProtocolSelectEnum', 
                [], [], 
                '''                Choose transport protocols
                ''',
                'select',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'transport-input',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration',
            False, 
            [
            _MetaInfoClassMember('acl-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL for inbound traffic
                ''',
                'acl_in',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('acl-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL for outbound traffic
                ''',
                'acl_out',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('transport-input', REFERENCE_CLASS, 'TransportInput' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput', 
                [], [], 
                '''                Protocols to use when connecting to the
                terminal server
                ''',
                'transport_input',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'connection-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration',
            False, 
            [
            _MetaInfoClassMember('connection-configuration', REFERENCE_CLASS, 'ConnectionConfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration', 
                [], [], 
                '''                Conection configuration information
                ''',
                'connection_configuration',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine',
            False, 
            [
            _MetaInfoClassMember('auxiliary-statistics', REFERENCE_CLASS, 'AuxiliaryStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics', 
                [], [], 
                '''                Statistics of the auxiliary line
                ''',
                'auxiliary_statistics',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration', 
                [], [], 
                '''                Configuration information of the line
                ''',
                'configuration',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State', 
                [], [], 
                '''                Line state information
                ''',
                'state',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'auxiliary-line',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes.AuxiliaryNode' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes.AuxiliaryNode',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'id',
                'Cisco-IOS-XR-tty-server-oper', True),
            _MetaInfoClassMember('auxiliary-line', REFERENCE_CLASS, 'AuxiliaryLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine', 
                [], [], 
                '''                Auxiliary line
                ''',
                'auxiliary_line',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'auxiliary-node',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty.AuxiliaryNodes' : {
        'meta_info' : _MetaInfoClass('Tty.AuxiliaryNodes',
            False, 
            [
            _MetaInfoClassMember('auxiliary-node', REFERENCE_LIST, 'AuxiliaryNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes.AuxiliaryNode', 
                [], [], 
                '''                Line configuration on a node
                ''',
                'auxiliary_node',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'auxiliary-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
    'Tty' : {
        'meta_info' : _MetaInfoClass('Tty',
            False, 
            [
            _MetaInfoClassMember('auxiliary-nodes', REFERENCE_CLASS, 'AuxiliaryNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.AuxiliaryNodes', 
                [], [], 
                '''                List of Nodes attached with an auxiliary line
                ''',
                'auxiliary_nodes',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('console-nodes', REFERENCE_CLASS, 'ConsoleNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.ConsoleNodes', 
                [], [], 
                '''                List of Nodes for console
                ''',
                'console_nodes',
                'Cisco-IOS-XR-tty-server-oper', False),
            _MetaInfoClassMember('vty-lines', REFERENCE_CLASS, 'VtyLines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper', 'Tty.VtyLines', 
                [], [], 
                '''                List of VTY lines
                ''',
                'vty_lines',
                'Cisco-IOS-XR-tty-server-oper', False),
            ],
            'Cisco-IOS-XR-tty-server-oper',
            'tty',
            _yang_ns._namespaces['Cisco-IOS-XR-tty-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_server_oper'
        ),
    },
}
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Rs232']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.GeneralStatistics']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Exec_']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics.Aaa']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.Template']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State.General']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration.ConnectionConfiguration']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.ConsoleStatistics']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.State']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine.Configuration']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode.ConsoleLine']['meta_info'].parent =_meta_table['Tty.ConsoleNodes.ConsoleNode']['meta_info']
_meta_table['Tty.ConsoleNodes.ConsoleNode']['meta_info'].parent =_meta_table['Tty.ConsoleNodes']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Connection']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.VtyStatistics']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.VtyStatistics.GeneralStatistics']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.VtyStatistics']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Exec_']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.VtyStatistics']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.VtyStatistics.Aaa']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.VtyStatistics']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.State.Template']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.State']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.State.General']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.State']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.Configuration.ConnectionConfiguration']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.Configuration']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.Sessions.OutgoingConnection.HostAddress']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.Sessions.OutgoingConnection']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.Sessions.OutgoingConnection']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine.Sessions']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.VtyStatistics']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.State']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.Configuration']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine']['meta_info']
_meta_table['Tty.VtyLines.VtyLine.Sessions']['meta_info'].parent =_meta_table['Tty.VtyLines.VtyLine']['meta_info']
_meta_table['Tty.VtyLines.VtyLine']['meta_info'].parent =_meta_table['Tty.VtyLines']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Rs232']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.GeneralStatistics']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Exec_']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics.Aaa']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.Template']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State.General']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration.TransportInput']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration.ConnectionConfiguration']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.AuxiliaryStatistics']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.State']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine.Configuration']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode.AuxiliaryLine']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode']['meta_info']
_meta_table['Tty.AuxiliaryNodes.AuxiliaryNode']['meta_info'].parent =_meta_table['Tty.AuxiliaryNodes']['meta_info']
_meta_table['Tty.ConsoleNodes']['meta_info'].parent =_meta_table['Tty']['meta_info']
_meta_table['Tty.VtyLines']['meta_info'].parent =_meta_table['Tty']['meta_info']
_meta_table['Tty.AuxiliaryNodes']['meta_info'].parent =_meta_table['Tty']['meta_info']
