


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SessionMon.Nodes.Node.SessionMonStatistics' : {
        'meta_info' : _MetaInfoClass('SessionMon.Nodes.Node.SessionMonStatistics',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                active sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcp-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcp ds
                ''',
                'dhcp_ds',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcpv4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcpv4
                ''',
                'dhcpv4',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcpv6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcpv6
                ''',
                'dhcpv6',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('ippkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ippkt
                ''',
                'ippkt',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('peak-active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                peak active sessions
                ''',
                'peak_active_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('peak-standby-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                peak standby sessions
                ''',
                'peak_standby_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('pppoe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pppoe
                ''',
                'pppoe',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('pppoe-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pppoe ds
                ''',
                'pppoe_ds',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('standby-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                standby sessions
                ''',
                'standby_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total
                ''',
                'total',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-oper',
            'session-mon-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-session-mon-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper'
        ),
    },
    'SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic' : {
        'meta_info' : _MetaInfoClass('SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-session-mon-oper', True),
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                active sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcp-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcp ds
                ''',
                'dhcp_ds',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcpv4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcpv4
                ''',
                'dhcpv4',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcpv6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcpv6
                ''',
                'dhcpv6',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('ippkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ippkt
                ''',
                'ippkt',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('peak-active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                peak active sessions
                ''',
                'peak_active_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('peak-standby-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                peak standby sessions
                ''',
                'peak_standby_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('pppoe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pppoe
                ''',
                'pppoe',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('pppoe-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pppoe ds
                ''',
                'pppoe_ds',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('standby-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                standby sessions
                ''',
                'standby_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total
                ''',
                'total',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-oper',
            'interface-all-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-session-mon-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper'
        ),
    },
    'SessionMon.Nodes.Node.InterfaceAllStatistics' : {
        'meta_info' : _MetaInfoClass('SessionMon.Nodes.Node.InterfaceAllStatistics',
            False, 
            [
            _MetaInfoClassMember('interface-all-statistic', REFERENCE_LIST, 'InterfaceAllStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper', 'SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic', 
                [], [], 
                '''                Statistics
                ''',
                'interface_all_statistic',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-oper',
            'interface-all-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-session-mon-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper'
        ),
    },
    'SessionMon.Nodes.Node.LicenseStatistics' : {
        'meta_info' : _MetaInfoClass('SessionMon.Nodes.Node.LicenseStatistics',
            False, 
            [
            _MetaInfoClassMember('active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                active sessions
                ''',
                'active_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcp-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcp ds
                ''',
                'dhcp_ds',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcpv4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcpv4
                ''',
                'dhcpv4',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('dhcpv6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dhcpv6
                ''',
                'dhcpv6',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('ippkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ippkt
                ''',
                'ippkt',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('peak-active-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                peak active sessions
                ''',
                'peak_active_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('peak-standby-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                peak standby sessions
                ''',
                'peak_standby_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('pppoe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pppoe
                ''',
                'pppoe',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('pppoe-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pppoe ds
                ''',
                'pppoe_ds',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('standby-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                standby sessions
                ''',
                'standby_sessions',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total
                ''',
                'total',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-oper',
            'license-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-session-mon-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper'
        ),
    },
    'SessionMon.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SessionMon.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Nodeid location 
                ''',
                'node_id',
                'Cisco-IOS-XR-subscriber-session-mon-oper', True),
            _MetaInfoClassMember('interface-all-statistics', REFERENCE_CLASS, 'InterfaceAllStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper', 'SessionMon.Nodes.Node.InterfaceAllStatistics', 
                [], [], 
                '''                Statistics Table
                ''',
                'interface_all_statistics',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('license-statistics', REFERENCE_CLASS, 'LicenseStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper', 'SessionMon.Nodes.Node.LicenseStatistics', 
                [], [], 
                '''                Smart license
                ''',
                'license_statistics',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            _MetaInfoClassMember('session-mon-statistics', REFERENCE_CLASS, 'SessionMonStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper', 'SessionMon.Nodes.Node.SessionMonStatistics', 
                [], [], 
                '''                Session Mon Statistics
                ''',
                'session_mon_statistics',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-session-mon-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper'
        ),
    },
    'SessionMon.Nodes' : {
        'meta_info' : _MetaInfoClass('SessionMon.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper', 'SessionMon.Nodes.Node', 
                [], [], 
                '''                Subscriber sessionmon operational data for a
                particular node
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-session-mon-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper'
        ),
    },
    'SessionMon' : {
        'meta_info' : _MetaInfoClass('SessionMon',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper', 'SessionMon.Nodes', 
                [], [], 
                '''                Subscriber Sessionmon list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-session-mon-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-session-mon-oper',
            'session-mon',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-session-mon-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_session_mon_oper'
        ),
    },
}
_meta_table['SessionMon.Nodes.Node.InterfaceAllStatistics.InterfaceAllStatistic']['meta_info'].parent =_meta_table['SessionMon.Nodes.Node.InterfaceAllStatistics']['meta_info']
_meta_table['SessionMon.Nodes.Node.SessionMonStatistics']['meta_info'].parent =_meta_table['SessionMon.Nodes.Node']['meta_info']
_meta_table['SessionMon.Nodes.Node.InterfaceAllStatistics']['meta_info'].parent =_meta_table['SessionMon.Nodes.Node']['meta_info']
_meta_table['SessionMon.Nodes.Node.LicenseStatistics']['meta_info'].parent =_meta_table['SessionMon.Nodes.Node']['meta_info']
_meta_table['SessionMon.Nodes.Node']['meta_info'].parent =_meta_table['SessionMon.Nodes']['meta_info']
_meta_table['SessionMon.Nodes']['meta_info'].parent =_meta_table['SessionMon']['meta_info']
