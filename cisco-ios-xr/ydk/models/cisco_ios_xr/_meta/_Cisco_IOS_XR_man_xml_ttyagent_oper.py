


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'XrXmlSessionStateEnum' : _MetaInfoEnum('XrXmlSessionStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper',
        {
            'idle':'idle',
            'busy':'busy',
        }, 'Cisco-IOS-XR-man-xml-ttyagent-oper', _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper']),
    'XrXmlSessionAlarmRegisterEnum' : _MetaInfoEnum('XrXmlSessionAlarmRegisterEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper',
        {
            'registered':'registered',
            'not-registered':'not_registered',
        }, 'Cisco-IOS-XR-man-xml-ttyagent-oper', _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper']),
    'Netconf.Agent.Tty.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent.Tty.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', True),
            _MetaInfoClassMember('admin-config-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Admin config session ID
                ''',
                'admin_config_session_id',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('alarm-notification', REFERENCE_ENUM_CLASS, 'XrXmlSessionAlarmRegisterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegisterEnum', 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                 Elapsed time(seconds) since a session is
                created
                ''',
                'elapsed_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('last-state-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time(seconds) since last session state change
                happened 
                ''',
                'last_state_change',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session start time in seconds since the Unix
                Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'XrXmlSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionStateEnum', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'Netconf.Agent.Tty.Sessions' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent.Tty.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'Netconf.Agent.Tty.Sessions.Session', 
                [], [], 
                '''                Session information
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'Netconf.Agent.Tty' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent.Tty',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'Netconf.Agent.Tty.Sessions', 
                [], [], 
                '''                Session information
                ''',
                'sessions',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'tty',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'Netconf.Agent' : {
        'meta_info' : _MetaInfoClass('Netconf.Agent',
            False, 
            [
            _MetaInfoClassMember('tty', REFERENCE_CLASS, 'Tty' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'Netconf.Agent.Tty', 
                [], [], 
                '''                NETCONF agent over TTY
                ''',
                'tty',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'agent',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'Netconf' : {
        'meta_info' : _MetaInfoClass('Netconf',
            False, 
            [
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'Netconf.Agent', 
                [], [], 
                '''                NETCONF agent operational information
                ''',
                'agent',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'netconf',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Tty.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
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
            _MetaInfoClassMember('alarm-notification', REFERENCE_ENUM_CLASS, 'XrXmlSessionAlarmRegisterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegisterEnum', 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                 Elapsed time(seconds) since a session is
                created
                ''',
                'elapsed_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('last-state-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time(seconds) since last session state change
                happened 
                ''',
                'last_state_change',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session start time in seconds since the Unix
                Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'XrXmlSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionStateEnum', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Tty.Sessions' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Tty.Sessions.Session', 
                [], [], 
                '''                xml sessions information
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Tty' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Tty',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Tty.Sessions', 
                [], [], 
                '''                sessions information
                ''',
                'sessions',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'tty',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Default.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
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
            _MetaInfoClassMember('alarm-notification', REFERENCE_ENUM_CLASS, 'XrXmlSessionAlarmRegisterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegisterEnum', 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                 Elapsed time(seconds) since a session is
                created
                ''',
                'elapsed_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('last-state-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time(seconds) since last session state change
                happened 
                ''',
                'last_state_change',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session start time in seconds since the Unix
                Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'XrXmlSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionStateEnum', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Default.Sessions' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Default.Sessions.Session', 
                [], [], 
                '''                xml sessions information
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Default' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Default',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Default.Sessions', 
                [], [], 
                '''                sessions information
                ''',
                'sessions',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'default',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Ssl.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
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
            _MetaInfoClassMember('alarm-notification', REFERENCE_ENUM_CLASS, 'XrXmlSessionAlarmRegisterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionAlarmRegisterEnum', 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                 Elapsed time(seconds) since a session is
                created
                ''',
                'elapsed_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('last-state-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time(seconds) since last session state change
                happened 
                ''',
                'last_state_change',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session start time in seconds since the Unix
                Epoch
                ''',
                'start_time',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'XrXmlSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXmlSessionStateEnum', 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Ssl.Sessions' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Ssl.Sessions.Session', 
                [], [], 
                '''                xml sessions information
                ''',
                'session',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent.Ssl' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent.Ssl',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Ssl.Sessions', 
                [], [], 
                '''                sessions information
                ''',
                'sessions',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'ssl',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml.Agent' : {
        'meta_info' : _MetaInfoClass('XrXml.Agent',
            False, 
            [
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Default', 
                [], [], 
                '''                Default sessions information
                ''',
                'default',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('ssl', REFERENCE_CLASS, 'Ssl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Ssl', 
                [], [], 
                '''                SSL sessions information
                ''',
                'ssl',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            _MetaInfoClassMember('tty', REFERENCE_CLASS, 'Tty' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent.Tty', 
                [], [], 
                '''                TTY sessions information
                ''',
                'tty',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'agent',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
    'XrXml' : {
        'meta_info' : _MetaInfoClass('XrXml',
            False, 
            [
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper', 'XrXml.Agent', 
                [], [], 
                '''                XML agents
                ''',
                'agent',
                'Cisco-IOS-XR-man-xml-ttyagent-oper', False),
            ],
            'Cisco-IOS-XR-man-xml-ttyagent-oper',
            'xr-xml',
            _yang_ns._namespaces['Cisco-IOS-XR-man-xml-ttyagent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_xml_ttyagent_oper'
        ),
    },
}
_meta_table['Netconf.Agent.Tty.Sessions.Session']['meta_info'].parent =_meta_table['Netconf.Agent.Tty.Sessions']['meta_info']
_meta_table['Netconf.Agent.Tty.Sessions']['meta_info'].parent =_meta_table['Netconf.Agent.Tty']['meta_info']
_meta_table['Netconf.Agent.Tty']['meta_info'].parent =_meta_table['Netconf.Agent']['meta_info']
_meta_table['Netconf.Agent']['meta_info'].parent =_meta_table['Netconf']['meta_info']
_meta_table['XrXml.Agent.Tty.Sessions.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Tty.Sessions']['meta_info']
_meta_table['XrXml.Agent.Tty.Sessions']['meta_info'].parent =_meta_table['XrXml.Agent.Tty']['meta_info']
_meta_table['XrXml.Agent.Default.Sessions.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Default.Sessions']['meta_info']
_meta_table['XrXml.Agent.Default.Sessions']['meta_info'].parent =_meta_table['XrXml.Agent.Default']['meta_info']
_meta_table['XrXml.Agent.Ssl.Sessions.Session']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl.Sessions']['meta_info']
_meta_table['XrXml.Agent.Ssl.Sessions']['meta_info'].parent =_meta_table['XrXml.Agent.Ssl']['meta_info']
_meta_table['XrXml.Agent.Tty']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent.Default']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent.Ssl']['meta_info'].parent =_meta_table['XrXml.Agent']['meta_info']
_meta_table['XrXml.Agent']['meta_info'].parent =_meta_table['XrXml']['meta_info']
