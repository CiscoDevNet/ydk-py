


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'XrXmlSessionAlarmRegister_Enum' : _MetaInfoEnum('XrXmlSessionAlarmRegister_Enum', 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper',
        {
            'registered':'REGISTERED',
            'not-registered':'NOT_REGISTERED',
        }, 'Cisco-IOS-XR-man-xml-ttyagent-oper', _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper']),
    'XrXmlSessionState_Enum' : _MetaInfoEnum('XrXmlSessionState_Enum', 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper',
        {
            'idle':'IDLE',
            'busy':'BUSY',
        }, 'Cisco-IOS-XR-man-xml-ttyagent-oper', _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper']),
    'XrXml.Agent.Default.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Session Id
                ''',
                'session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', True),
            _MetaInfoClassMember('admin-config-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Admin config session ID
                ''',
                'admin_config_session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('alarm-notification', REFERENCE_ENUM_CLASS, 'XrXmlSessionAlarmRegister_Enum' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegister_Enum', 
                [], [], 
                '''                is the session registered for alarm
                notifications
                ''',
                'alarm_notification',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('client-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ip address of the client
                ''',
                'client_address',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('client-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                client's port
                ''',
                'client_port',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('config-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Config session ID
                ''',
                'config_session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('elapsed-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                 Elapsed time(seconds) since a session is
                created
                ''',
                'elapsed_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('last-state-change', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time(seconds) since last session state change
                happened 
                ''',
                'last_state_change',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                session start time in seconds since the Unix
                Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'XrXmlSessionState_Enum' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionState_Enum', 
                [], [], 
                '''                state of the session idle/busy
                ''',
                'state',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'username',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name 
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Default.Sessions' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Default.Sessions.Session', 
                [], [], 
                '''                xml sessions information
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Default' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Default.Sessions', 
                [], [], 
                '''                sessions information
                ''',
                'sessions',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'default',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Ssl.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Session Id
                ''',
                'session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', True),
            _MetaInfoClassMember('admin-config-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Admin config session ID
                ''',
                'admin_config_session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('alarm-notification', REFERENCE_ENUM_CLASS, 'XrXmlSessionAlarmRegister_Enum' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegister_Enum', 
                [], [], 
                '''                is the session registered for alarm
                notifications
                ''',
                'alarm_notification',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('client-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ip address of the client
                ''',
                'client_address',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('client-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                client's port
                ''',
                'client_port',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('config-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Config session ID
                ''',
                'config_session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('elapsed-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                 Elapsed time(seconds) since a session is
                created
                ''',
                'elapsed_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('last-state-change', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time(seconds) since last session state change
                happened 
                ''',
                'last_state_change',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                session start time in seconds since the Unix
                Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'XrXmlSessionState_Enum' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionState_Enum', 
                [], [], 
                '''                state of the session idle/busy
                ''',
                'state',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'username',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name 
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Ssl.Sessions' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Ssl.Sessions.Session', 
                [], [], 
                '''                xml sessions information
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Ssl' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Ssl.Sessions', 
                [], [], 
                '''                sessions information
                ''',
                'sessions',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'ssl',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Tty.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Session Id
                ''',
                'session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', True),
            _MetaInfoClassMember('admin-config-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Admin config session ID
                ''',
                'admin_config_session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('alarm-notification', REFERENCE_ENUM_CLASS, 'XrXmlSessionAlarmRegister_Enum' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegister_Enum', 
                [], [], 
                '''                is the session registered for alarm
                notifications
                ''',
                'alarm_notification',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('client-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ip address of the client
                ''',
                'client_address',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('client-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                client's port
                ''',
                'client_port',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('config-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Config session ID
                ''',
                'config_session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('elapsed-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                 Elapsed time(seconds) since a session is
                created
                ''',
                'elapsed_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('last-state-change', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time(seconds) since last session state change
                happened 
                ''',
                'last_state_change',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                session start time in seconds since the Unix
                Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'XrXmlSessionState_Enum' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionState_Enum', 
                [], [], 
                '''                state of the session idle/busy
                ''',
                'state',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'username',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name 
                ''',
                'vrf_name',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Tty.Sessions' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Tty.Sessions.Session', 
                [], [], 
                '''                xml sessions information
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Tty' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Tty.Sessions', 
                [], [], 
                '''                sessions information
                ''',
                'sessions',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'tty',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent',
            False, 
            [
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Default', 
                [], [], 
                '''                Default sessions information
                ''',
                'default',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('ssl', REFERENCE_CLASS, 'Ssl' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Ssl', 
                [], [], 
                '''                SSL sessions information
                ''',
                'ssl',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('tty', REFERENCE_CLASS, 'Tty' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Tty', 
                [], [], 
                '''                TTY sessions information
                ''',
                'tty',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'agent',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml' : {
        'meta_info' : _MetaInfoClass('XrXml',
            False, 
            [
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent' , 'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent', 
                [], [], 
                '''                XML agents
                ''',
                'agent',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'xr-xml',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.man.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
}
_meta_table['XrXml.Agent.Default.Sessions.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Default.Sessions']['meta_info']
_meta_table['XrXml.Agent.Default.Sessions']['meta_info'].parent =_meta_table['XrXml.Agent.Default']['meta_info']
_meta_table['XrXml.Agent.Ssl.Sessions.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl.Sessions']['meta_info']
_meta_table['XrXml.Agent.Ssl.Sessions']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl']['meta_info']
_meta_table['XrXml.Agent.Tty.Sessions.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Tty.Sessions']['meta_info']
_meta_table['XrXml.Agent.Tty.Sessions']['meta_info'].parent =_meta_table['XrXml.Agent.Tty']['meta_info']
_meta_table['XrXml.Agent.Default']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent.Ssl']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent.Tty']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent']['meta_info'].parent =_meta_table['XrXml']['meta_info']
