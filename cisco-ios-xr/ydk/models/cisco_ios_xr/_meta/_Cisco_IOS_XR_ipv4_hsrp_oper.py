


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'StandbyGrpStateEnum' : _MetaInfoEnum('StandbyGrpStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper',
        {
            'state-initial':'state_initial',
            'state-learn':'state_learn',
            'state-listen':'state_listen',
            'state-speak':'state_speak',
            'state-standby':'state_standby',
            'state-active':'state_active',
        }, 'Cisco-IOS-XR-ipv4-hsrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper']),
    'HsrpBAfEnum' : _MetaInfoEnum('HsrpBAfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'count':'count',
        }, 'Cisco-IOS-XR-ipv4-hsrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper']),
    'HsrpStateChangeReasonEnum' : _MetaInfoEnum('HsrpStateChangeReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper',
        {
            'state-change-bfd-down':'state_change_bfd_down',
            'state-change-vip-learnt':'state_change_vip_learnt',
            'state-change-interface-ip':'state_change_interface_ip',
            'state-change-delay-timer':'state_change_delay_timer',
            'state-change-startup':'state_change_startup',
            'state-change-shutdown':'state_change_shutdown',
            'state-change-interface-up':'state_change_interface_up',
            'state-change-interface-down':'state_change_interface_down',
            'state-change-active-timer':'state_change_active_timer',
            'state-change-standby-timer':'state_change_standby_timer',
            'state-change-resign':'state_change_resign',
            'state-change-coup':'state_change_coup',
            'state-change-higher-priority-speak':'state_change_higher_priority_speak',
            'state-change-higher-priority-standby':'state_change_higher_priority_standby',
            'state-change-lower-priority-standby':'state_change_lower_priority_standby',
            'state-change-higher-priority-active':'state_change_higher_priority_active',
            'state-change-lower-priority-active':'state_change_lower_priority_active',
            'state-change-virtual-ip-configured':'state_change_virtual_ip_configured',
            'state-change-virtual-ip-lost':'state_change_virtual_ip_lost',
            'state-change-recovered-from-checkpoint':'state_change_recovered_from_checkpoint',
            'state-change-mac-update':'state_change_mac_update',
            'state-change-admin':'state_change_admin',
            'state-change-parent':'state_change_parent',
            'state-change-chkpt-update':'state_change_chkpt_update',
            'state-change-issu-resync':'state_change_issu_resync',
            'state-change-max':'state_change_max',
        }, 'Cisco-IOS-XR-ipv4-hsrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper']),
    'HsrpBfdSessionStateEnum' : _MetaInfoEnum('HsrpBfdSessionStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper',
        {
            'bfd-state-none':'bfd_state_none',
            'bfd-state-inactive':'bfd_state_inactive',
            'bfd-state-up':'bfd_state_up',
            'bfd-state-down':'bfd_state_down',
        }, 'Cisco-IOS-XR-ipv4-hsrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper']),
    'HsrpVmacStateEnum' : _MetaInfoEnum('HsrpVmacStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper',
        {
            'stored':'stored',
            'reserved':'reserved',
            'active':'active',
            'reserving':'reserving',
        }, 'Cisco-IOS-XR-ipv4-hsrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper']),
    'Hsrp.Ipv4.Groups.Group.ResignSentTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.ResignSentTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'resign-sent-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group.ResignReceivedTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.ResignReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'resign-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group.CoupSentTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.CoupSentTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'coup-sent-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group.CoupReceivedTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.CoupReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'coup-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group.Statistics' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.Statistics',
            False, 
            [
            _MetaInfoClassMember('active-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Active State
                ''',
                'active_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('auth-fail-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Packets received that failed
                authentication
                ''',
                'auth_fail_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Coup Packets received
                ''',
                'coup_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Coup Packets sent
                ''',
                'coup_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello Packets received
                ''',
                'hello_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello Packets sent (NB: Bundles only)
                ''',
                'hello_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('init-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Init State
                ''',
                'init_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('invalid-timer-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with invalid Hello
                Time value
                ''',
                'invalid_timer_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('learn-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Learn State
                ''',
                'learn_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('listen-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Listen State
                ''',
                'listen_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('mismatch-virtual-ip-address-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with mismatching
                virtual IP address
                ''',
                'mismatch_virtual_ip_address_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Resign Packets received
                ''',
                'resign_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Resign Packets sent
                ''',
                'resign_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('speak-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Speak State
                ''',
                'speak_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Standby State
                ''',
                'standby_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group.GlobalAddress' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.GlobalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'global-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group.StateChangeHistory' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group.StateChangeHistory',
            False, 
            [
            _MetaInfoClassMember('new-state', REFERENCE_ENUM_CLASS, 'StandbyGrpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'StandbyGrpStateEnum', 
                [], [], 
                '''                New State
                ''',
                'new_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('old-state', REFERENCE_ENUM_CLASS, 'StandbyGrpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'StandbyGrpStateEnum', 
                [], [], 
                '''                Old State
                ''',
                'old_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('reason', REFERENCE_ENUM_CLASS, 'HsrpStateChangeReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpStateChangeReasonEnum', 
                [], [], 
                '''                Reason for state change
                ''',
                'reason',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('time', REFERENCE_CLASS, 'Time' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time', 
                [], [], 
                '''                Time of state change
                ''',
                'time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'state-change-history',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('active-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Active router's IP address
                ''',
                'active_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Active router's IPv6 address
                ''',
                'active_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Active router's interface MAC address
                ''',
                'active_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority of the Active router
                ''',
                'active_priority',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Active timer running flag
                ''',
                'active_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active timer running time msecs
                ''',
                'active_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active timer running time secs
                ''',
                'active_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'HsrpBAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpBAfEnum', 
                [], [], 
                '''                Address family
                ''',
                'address_family',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('authentication-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 9)], [], 
                '''                Authentication string
                ''',
                'authentication_string',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                HSRP BFD fast failover
                ''',
                'bfd_enabled',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                BFD Interface
                ''',
                'bfd_interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD packet send interval
                ''',
                'bfd_interval',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD multiplier
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-peer-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD Peer IP address
                ''',
                'bfd_peer_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD Peer IPv6 address
                ''',
                'bfd_peer_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-session-state', REFERENCE_ENUM_CLASS, 'HsrpBfdSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpBfdSessionStateEnum', 
                [], [], 
                '''                BFD session state
                ''',
                'bfd_session_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('configured-mac-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAC address configured
                ''',
                'configured_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('configured-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured priority
                ''',
                'configured_priority',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('configured-timers', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Non-default timers are configured
                ''',
                'configured_timers',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-received-time', REFERENCE_CLASS, 'CoupReceivedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.CoupReceivedTime', 
                [], [], 
                '''                Time last coup was received
                ''',
                'coup_received_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-sent-time', REFERENCE_CLASS, 'CoupSentTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.CoupSentTime', 
                [], [], 
                '''                Time last coup was sent
                ''',
                'coup_sent_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('current-state-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time in current state secs
                ''',
                'current_state_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('delay-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delay timer running flag
                ''',
                'delay_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('delay-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time msecs
                ''',
                'delay_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('delay-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time secs
                ''',
                'delay_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('followed-session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Followed Session Name
                ''',
                'followed_session_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('global-address', REFERENCE_LIST, 'GlobalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.GlobalAddress', 
                [], [], 
                '''                Global virtual IPv6 addresses
                ''',
                'global_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hellotime in msecs
                ''',
                'hello_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Hello timer running flag
                ''',
                'hello_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello timer running time msecs
                ''',
                'hello_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello timer running time secs
                ''',
                'hello_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holdtime in msecs
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hsrp-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                HSRP Group number
                ''',
                'hsrp_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hsrp-router-state', REFERENCE_ENUM_CLASS, 'StandbyGrpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'StandbyGrpStateEnum', 
                [], [], 
                '''                HSRP router state
                ''',
                'hsrp_router_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interface Name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('is-slave', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Group is a slave group
                ''',
                'is_slave',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('learned-hello-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Learned hellotime in msecs
                ''',
                'learned_hello_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('learned-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Learned holdtime in msecs
                ''',
                'learned_hold_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('min-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum delay time in msecs
                ''',
                'min_delay_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Preempt delay time in seconds
                ''',
                'preempt_delay',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('preempt-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preempt enabled
                ''',
                'preempt_enabled',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('preempt-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Preempt time remaining in seconds
                ''',
                'preempt_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('redirects-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                HSRP redirects disabled
                ''',
                'redirects_disabled',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('reload-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reload delay time in msecs
                ''',
                'reload_delay_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-received-time', REFERENCE_CLASS, 'ResignReceivedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.ResignReceivedTime', 
                [], [], 
                '''                Time last resign was received
                ''',
                'resign_received_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-sent-time', REFERENCE_CLASS, 'ResignSentTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.ResignSentTime', 
                [], [], 
                '''                Time last resign was sent
                ''',
                'resign_sent_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('router-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority of the router
                ''',
                'router_priority',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('secondary-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Secondary virtual IP addresses
                ''',
                'secondary_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('slaves', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of slaves following state
                ''',
                'slaves',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Standby router's IP address
                ''',
                'standby_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Standby router's IPv6 address
                ''',
                'standby_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Standby router's interface MAC address
                ''',
                'standby_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Standby timer running flag
                ''',
                'standby_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Standby timer running time msecs
                ''',
                'standby_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Standby timer running time secs
                ''',
                'standby_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('state-change-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of state changes
                ''',
                'state_change_count',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('state-change-history', REFERENCE_LIST, 'StateChangeHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.StateChangeHistory', 
                [], [], 
                '''                State change history
                ''',
                'state_change_history',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group.Statistics', 
                [], [], 
                '''                HSRP Group statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces
                ''',
                'tracked_interface_count',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interface-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces up
                ''',
                'tracked_interface_up_count',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-bia-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use burnt in MAC address configured
                ''',
                'use_bia_configured',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-configured-timers', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use configured timers
                ''',
                'use_configured_timers',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-configured-virtual-ip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use configured virtual IP
                ''',
                'use_configured_virtual_ip',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                HSRP Protocol Version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configured Virtual IPv4 address
                ''',
                'virtual_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-linklocal-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Virtual linklocal IPv6 address
                ''',
                'virtual_linklocal_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Virtual mac address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address-state', REFERENCE_ENUM_CLASS, 'HsrpVmacStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpVmacStateEnum', 
                [], [], 
                '''                Virtual mac address state
                ''',
                'virtual_mac_address_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups.Group', 
                [], [], 
                '''                An HSRP standby group
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.TrackedInterfaces.TrackedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('tracked-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name of the interface being
                tracked
                ''',
                'tracked_interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('hsrp-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                HSRP Group number
                ''',
                'hsrp_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface-up-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface up flag
                ''',
                'interface_up_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('is-object', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tracked Object Flag
                ''',
                'is_object',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Priority weighting
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Tracked Interface Name
                ''',
                'tracked_interface_name_xr',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'tracked-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.TrackedInterfaces',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.TrackedInterfaces.TrackedInterface', 
                [], [], 
                '''                An HSRP tracked interface entry
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'tracked-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Interfaces.Interface.Statistics' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Interfaces.Interface.Statistics',
            False, 
            [
            _MetaInfoClassMember('advert-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of advertisement packets received
                ''',
                'advert_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('advert-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of advertisement packets sent
                ''',
                'advert_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('conflict-source-ip-address-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received from a conflicting
                Source IP address
                ''',
                'conflict_source_ip_address_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('inoperational-group-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received for an inoperational
                group
                ''',
                'inoperational_group_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('invalid-operation-code-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with invalid
                operation code
                ''',
                'invalid_operation_code_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('invalid-version-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with invalid version
                ''',
                'invalid_version_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('long-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received that were too Long
                ''',
                'long_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('short-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received that were too short
                ''',
                'short_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('unknown-group-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received for an unknown group
                id
                ''',
                'unknown_group_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Interfaces.Interface.Statistics', 
                [], [], 
                '''                HSRP Interface Statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-bia-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use burnt in mac address flag
                ''',
                'use_bia_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4.Interfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Interfaces.Interface', 
                [], [], 
                '''                A HSRP interface entry
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv4' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv4',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Groups', 
                [], [], 
                '''                The HSRP standby group table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.Interfaces', 
                [], [], 
                '''                The HSRP interface information table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4.TrackedInterfaces', 
                [], [], 
                '''                The HSRP tracked interfaces table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.MgoSessions.MgoSession.Slave' : {
        'meta_info' : _MetaInfoClass('Hsrp.MgoSessions.MgoSession.Slave',
            False, 
            [
            _MetaInfoClassMember('slave-group-interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interface of slave group
                ''',
                'slave_group_interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('slave-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group number of slave group
                ''',
                'slave_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'slave',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.MgoSessions.MgoSession' : {
        'meta_info' : _MetaInfoClass('Hsrp.MgoSessions.MgoSession',
            False, 
            [
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                HSRP MGO session name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('primary-af-name', REFERENCE_ENUM_CLASS, 'HsrpBAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpBAfEnum', 
                [], [], 
                '''                Address family of primary session
                ''',
                'primary_af_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('primary-session-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface of primary session
                ''',
                'primary_session_interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('primary-session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Session Name
                ''',
                'primary_session_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('primary-session-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group number of primary session
                ''',
                'primary_session_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('primary-session-state', REFERENCE_ENUM_CLASS, 'StandbyGrpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'StandbyGrpStateEnum', 
                [], [], 
                '''                State of primary session
                ''',
                'primary_session_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('slave', REFERENCE_LIST, 'Slave' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.MgoSessions.MgoSession.Slave', 
                [], [], 
                '''                List of slaves following this primary session
                ''',
                'slave',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'mgo-session',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.MgoSessions' : {
        'meta_info' : _MetaInfoClass('Hsrp.MgoSessions',
            False, 
            [
            _MetaInfoClassMember('mgo-session', REFERENCE_LIST, 'MgoSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.MgoSessions.MgoSession', 
                [], [], 
                '''                HSRP MGO session
                ''',
                'mgo_session',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'mgo-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.TrackedInterfaces.TrackedInterface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.TrackedInterfaces.TrackedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('tracked-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name of the interface being
                tracked
                ''',
                'tracked_interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('hsrp-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                HSRP Group number
                ''',
                'hsrp_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface-up-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface up flag
                ''',
                'interface_up_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('is-object', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tracked Object Flag
                ''',
                'is_object',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Priority weighting
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Tracked Interface Name
                ''',
                'tracked_interface_name_xr',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'tracked-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.TrackedInterfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.TrackedInterfaces',
            False, 
            [
            _MetaInfoClassMember('tracked-interface', REFERENCE_LIST, 'TrackedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.TrackedInterfaces.TrackedInterface', 
                [], [], 
                '''                An HSRP tracked interface entry
                ''',
                'tracked_interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'tracked-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.ResignSentTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.ResignSentTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'resign-sent-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.ResignReceivedTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.ResignReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'resign-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.CoupSentTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.CoupSentTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'coup-sent-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.CoupReceivedTime' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.CoupReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'coup-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.Statistics' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.Statistics',
            False, 
            [
            _MetaInfoClassMember('active-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Active State
                ''',
                'active_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('auth-fail-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Packets received that failed
                authentication
                ''',
                'auth_fail_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Coup Packets received
                ''',
                'coup_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Coup Packets sent
                ''',
                'coup_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello Packets received
                ''',
                'hello_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Hello Packets sent (NB: Bundles only)
                ''',
                'hello_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('init-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Init State
                ''',
                'init_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('invalid-timer-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with invalid Hello
                Time value
                ''',
                'invalid_timer_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('learn-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Learn State
                ''',
                'learn_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('listen-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Listen State
                ''',
                'listen_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('mismatch-virtual-ip-address-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with mismatching
                virtual IP address
                ''',
                'mismatch_virtual_ip_address_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Resign Packets received
                ''',
                'resign_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Resign Packets sent
                ''',
                'resign_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('speak-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Speak State
                ''',
                'speak_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-transitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of transitions to Standby State
                ''',
                'standby_transitions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.GlobalAddress' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.GlobalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'global-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group.StateChangeHistory' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group.StateChangeHistory',
            False, 
            [
            _MetaInfoClassMember('new-state', REFERENCE_ENUM_CLASS, 'StandbyGrpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'StandbyGrpStateEnum', 
                [], [], 
                '''                New State
                ''',
                'new_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('old-state', REFERENCE_ENUM_CLASS, 'StandbyGrpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'StandbyGrpStateEnum', 
                [], [], 
                '''                Old State
                ''',
                'old_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('reason', REFERENCE_ENUM_CLASS, 'HsrpStateChangeReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpStateChangeReasonEnum', 
                [], [], 
                '''                Reason for state change
                ''',
                'reason',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('time', REFERENCE_CLASS, 'Time' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time', 
                [], [], 
                '''                Time of state change
                ''',
                'time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'state-change-history',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('group-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The HSRP group number
                ''',
                'group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('active-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Active router's IP address
                ''',
                'active_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Active router's IPv6 address
                ''',
                'active_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Active router's interface MAC address
                ''',
                'active_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority of the Active router
                ''',
                'active_priority',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Active timer running flag
                ''',
                'active_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active timer running time msecs
                ''',
                'active_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('active-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Active timer running time secs
                ''',
                'active_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'HsrpBAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpBAfEnum', 
                [], [], 
                '''                Address family
                ''',
                'address_family',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('authentication-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 9)], [], 
                '''                Authentication string
                ''',
                'authentication_string',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                HSRP BFD fast failover
                ''',
                'bfd_enabled',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                BFD Interface
                ''',
                'bfd_interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD packet send interval
                ''',
                'bfd_interval',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD multiplier
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-peer-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD Peer IP address
                ''',
                'bfd_peer_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD Peer IPv6 address
                ''',
                'bfd_peer_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-session-state', REFERENCE_ENUM_CLASS, 'HsrpBfdSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpBfdSessionStateEnum', 
                [], [], 
                '''                BFD session state
                ''',
                'bfd_session_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('configured-mac-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAC address configured
                ''',
                'configured_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('configured-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured priority
                ''',
                'configured_priority',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('configured-timers', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Non-default timers are configured
                ''',
                'configured_timers',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-received-time', REFERENCE_CLASS, 'CoupReceivedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.CoupReceivedTime', 
                [], [], 
                '''                Time last coup was received
                ''',
                'coup_received_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('coup-sent-time', REFERENCE_CLASS, 'CoupSentTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.CoupSentTime', 
                [], [], 
                '''                Time last coup was sent
                ''',
                'coup_sent_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('current-state-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time in current state secs
                ''',
                'current_state_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('delay-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delay timer running flag
                ''',
                'delay_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('delay-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time msecs
                ''',
                'delay_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('delay-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time secs
                ''',
                'delay_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('followed-session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Followed Session Name
                ''',
                'followed_session_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('global-address', REFERENCE_LIST, 'GlobalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.GlobalAddress', 
                [], [], 
                '''                Global virtual IPv6 addresses
                ''',
                'global_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hellotime in msecs
                ''',
                'hello_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Hello timer running flag
                ''',
                'hello_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello timer running time msecs
                ''',
                'hello_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hello-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello timer running time secs
                ''',
                'hello_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holdtime in msecs
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hsrp-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                HSRP Group number
                ''',
                'hsrp_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('hsrp-router-state', REFERENCE_ENUM_CLASS, 'StandbyGrpStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'StandbyGrpStateEnum', 
                [], [], 
                '''                HSRP router state
                ''',
                'hsrp_router_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interface Name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('is-slave', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Group is a slave group
                ''',
                'is_slave',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('learned-hello-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Learned hellotime in msecs
                ''',
                'learned_hello_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('learned-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Learned holdtime in msecs
                ''',
                'learned_hold_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('min-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum delay time in msecs
                ''',
                'min_delay_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('preempt-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Preempt delay time in seconds
                ''',
                'preempt_delay',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('preempt-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preempt enabled
                ''',
                'preempt_enabled',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('preempt-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Preempt time remaining in seconds
                ''',
                'preempt_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('redirects-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                HSRP redirects disabled
                ''',
                'redirects_disabled',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('reload-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reload delay time in msecs
                ''',
                'reload_delay_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-received-time', REFERENCE_CLASS, 'ResignReceivedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.ResignReceivedTime', 
                [], [], 
                '''                Time last resign was received
                ''',
                'resign_received_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('resign-sent-time', REFERENCE_CLASS, 'ResignSentTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.ResignSentTime', 
                [], [], 
                '''                Time last resign was sent
                ''',
                'resign_sent_time',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('router-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority of the router
                ''',
                'router_priority',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('secondary-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Secondary virtual IP addresses
                ''',
                'secondary_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('slaves', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of slaves following state
                ''',
                'slaves',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Standby router's IP address
                ''',
                'standby_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Standby router's IPv6 address
                ''',
                'standby_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Standby router's interface MAC address
                ''',
                'standby_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Standby timer running flag
                ''',
                'standby_timer_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Standby timer running time msecs
                ''',
                'standby_timer_msecs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('standby-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Standby timer running time secs
                ''',
                'standby_timer_secs',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('state-change-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of state changes
                ''',
                'state_change_count',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('state-change-history', REFERENCE_LIST, 'StateChangeHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.StateChangeHistory', 
                [], [], 
                '''                State change history
                ''',
                'state_change_history',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group.Statistics', 
                [], [], 
                '''                HSRP Group statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces
                ''',
                'tracked_interface_count',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interface-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces up
                ''',
                'tracked_interface_up_count',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-bia-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use burnt in MAC address configured
                ''',
                'use_bia_configured',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-configured-timers', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use configured timers
                ''',
                'use_configured_timers',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-configured-virtual-ip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use configured virtual IP
                ''',
                'use_configured_virtual_ip',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                HSRP Protocol Version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configured Virtual IPv4 address
                ''',
                'virtual_ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-linklocal-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Virtual linklocal IPv6 address
                ''',
                'virtual_linklocal_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Virtual mac address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address-state', REFERENCE_ENUM_CLASS, 'HsrpVmacStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpVmacStateEnum', 
                [], [], 
                '''                Virtual mac address state
                ''',
                'virtual_mac_address_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Groups' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups.Group', 
                [], [], 
                '''                An HSRP standby group
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Interfaces.Interface.Statistics' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Interfaces.Interface.Statistics',
            False, 
            [
            _MetaInfoClassMember('advert-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of advertisement packets received
                ''',
                'advert_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('advert-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of advertisement packets sent
                ''',
                'advert_packets_sent',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('conflict-source-ip-address-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received from a conflicting
                Source IP address
                ''',
                'conflict_source_ip_address_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('inoperational-group-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received for an inoperational
                group
                ''',
                'inoperational_group_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('invalid-operation-code-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with invalid
                operation code
                ''',
                'invalid_operation_code_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('invalid-version-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received with invalid version
                ''',
                'invalid_version_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('long-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received that were too Long
                ''',
                'long_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('short-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received that were too short
                ''',
                'short_packets_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('unknown-group-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received for an unknown group
                id
                ''',
                'unknown_group_received',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Interfaces.Interface.Statistics', 
                [], [], 
                '''                HSRP Interface Statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('use-bia-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use burnt in mac address flag
                ''',
                'use_bia_flag',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Interfaces.Interface', 
                [], [], 
                '''                A HSRP interface entry
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Ipv6' : {
        'meta_info' : _MetaInfoClass('Hsrp.Ipv6',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Groups', 
                [], [], 
                '''                The HSRP standby group table
                ''',
                'groups',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.Interfaces', 
                [], [], 
                '''                The HSRP interface information table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces', REFERENCE_CLASS, 'TrackedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6.TrackedInterfaces', 
                [], [], 
                '''                The HSRP tracked interfaces table
                ''',
                'tracked_interfaces',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.BfdSessions.BfdSession.Group' : {
        'meta_info' : _MetaInfoClass('Hsrp.BfdSessions.BfdSession.Group',
            False, 
            [
            _MetaInfoClassMember('hsrp-group-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                HSRP Group number
                ''',
                'hsrp_group_number',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.BfdSessions.BfdSession' : {
        'meta_info' : _MetaInfoClass('Hsrp.BfdSessions.BfdSession',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination IP Address of BFD Session
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IP Address of BFD Session
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-hsrp-oper', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IP Address of BFD Session
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ipv4-hsrp-oper', True),
                ]),
            _MetaInfoClassMember('bfd-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                BFD Interface Name
                ''',
                'bfd_interface_name',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD packet send interval
                ''',
                'bfd_interval',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD multiplier
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-session-state', REFERENCE_ENUM_CLASS, 'HsrpBfdSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpBfdSessionStateEnum', 
                [], [], 
                '''                BFD session state
                ''',
                'bfd_session_state',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('destination-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD IPv6 destination address
                ''',
                'destination_ipv6_address',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.BfdSessions.BfdSession.Group', 
                [], [], 
                '''                HSRP Groups tracking the BFD session
                ''',
                'group',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('session-address-family', REFERENCE_ENUM_CLASS, 'HsrpBAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'HsrpBAfEnum', 
                [], [], 
                '''                Session Address family
                ''',
                'session_address_family',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'bfd-session',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.BfdSessions' : {
        'meta_info' : _MetaInfoClass('Hsrp.BfdSessions',
            False, 
            [
            _MetaInfoClassMember('bfd-session', REFERENCE_LIST, 'BfdSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.BfdSessions.BfdSession', 
                [], [], 
                '''                An HSRP BFD Session
                ''',
                'bfd_session',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'bfd-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp.Summary' : {
        'meta_info' : _MetaInfoClass('Hsrp.Summary',
            False, 
            [
            _MetaInfoClassMember('bfd-session-inactive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of HSRP BFD sessions in INACTIVE state
                ''',
                'bfd_session_inactive',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-sessions-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of HSRP BFD sessions in DOWN state
                ''',
                'bfd_sessions_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('bfd-sessions-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of HSRP BFD sessions in UP state
                ''',
                'bfd_sessions_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv4-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of HSRP interfaces with IPv4 caps in DOWN
                state
                ''',
                'interfaces_ipv4_state_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv4-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of HSRP interfaces with IPv4 caps in UP
                state
                ''',
                'interfaces_ipv4_state_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv6-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of HSRP interfaces with IPv6 caps in DOWN
                state
                ''',
                'interfaces_ipv6_state_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv6-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of HSRP interfaces with IPv6 caps in UP
                state
                ''',
                'interfaces_ipv6_state_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in ACTIVE state
                ''',
                'ipv4_sessions_active',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in INIT state
                ''',
                'ipv4_sessions_init',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-learn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in LEARN state
                ''',
                'ipv4_sessions_learn',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-listen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in LISTEN state
                ''',
                'ipv4_sessions_listen',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-speak', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in SPEAK state
                ''',
                'ipv4_sessions_speak',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-standby', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in STANDBY state
                ''',
                'ipv4_sessions_standby',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in ACTIVE state
                ''',
                'ipv4_slaves_active',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in INIT state
                ''',
                'ipv4_slaves_init',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-learn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in LEARN state
                ''',
                'ipv4_slaves_learn',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-listen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in LISTEN state
                ''',
                'ipv4_slaves_listen',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-speak', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in SPEAK state
                ''',
                'ipv4_slaves_speak',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-standby', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in STANDBY state
                ''',
                'ipv4_slaves_standby',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-active-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                groups in ACTIVE state
                ''',
                'ipv4_virtual_ip_addresses_active_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-active-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on groups
                in ACTIVE state
                ''',
                'ipv4_virtual_ip_addresses_active_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-init-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                groups in INIT state
                ''',
                'ipv4_virtual_ip_addresses_init_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-init-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on groups
                in INIT state
                ''',
                'ipv4_virtual_ip_addresses_init_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-learn-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                groups in LEARN state
                ''',
                'ipv4_virtual_ip_addresses_learn_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-learn-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on groups
                in LEARN state
                ''',
                'ipv4_virtual_ip_addresses_learn_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-listen-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                groups in LISTEN state
                ''',
                'ipv4_virtual_ip_addresses_listen_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-listen-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on groups
                in LISTEN state
                ''',
                'ipv4_virtual_ip_addresses_listen_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-speak-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                groups in SPEAK state
                ''',
                'ipv4_virtual_ip_addresses_speak_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-speak-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on groups
                in SPEAK state
                ''',
                'ipv4_virtual_ip_addresses_speak_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-standby-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                groups in STANDBY state
                ''',
                'ipv4_virtual_ip_addresses_standby_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-standby-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on groups
                in STANDBY state
                ''',
                'ipv4_virtual_ip_addresses_standby_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in ACTIVE state
                ''',
                'ipv6_sessions_active',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in INIT state
                ''',
                'ipv6_sessions_init',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-learn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in LEARN state
                ''',
                'ipv6_sessions_learn',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-listen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in LISTEN state
                ''',
                'ipv6_sessions_listen',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-speak', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in SPEAK state
                ''',
                'ipv6_sessions_speak',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-standby', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in STANDBY state
                ''',
                'ipv6_sessions_standby',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in ACTIVE state
                ''',
                'ipv6_slaves_active',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in INIT state
                ''',
                'ipv6_slaves_init',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-learn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in LEARN state
                ''',
                'ipv6_slaves_learn',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-listen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in LISTEN state
                ''',
                'ipv6_slaves_listen',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-speak', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in SPEAK state
                ''',
                'ipv6_slaves_speak',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-standby', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in STANDBY state
                ''',
                'ipv6_slaves_standby',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-active-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                groups in ACTIVE state
                ''',
                'ipv6_virtual_ip_addresses_active_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-active-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on groups
                in ACTIVE state
                ''',
                'ipv6_virtual_ip_addresses_active_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-init-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                groups in INIT state
                ''',
                'ipv6_virtual_ip_addresses_init_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-init-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on groups
                in INIT state
                ''',
                'ipv6_virtual_ip_addresses_init_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-learn-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                groups in LEARN state
                ''',
                'ipv6_virtual_ip_addresses_learn_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-learn-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on groups
                in LEARN state
                ''',
                'ipv6_virtual_ip_addresses_learn_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-listen-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                groups in LISTEN state
                ''',
                'ipv6_virtual_ip_addresses_listen_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-listen-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on groups
                in LISTEN state
                ''',
                'ipv6_virtual_ip_addresses_listen_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-speak-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                groups in SPEAK state
                ''',
                'ipv6_virtual_ip_addresses_speak_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-speak-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on groups
                in SPEAK state
                ''',
                'ipv6_virtual_ip_addresses_speak_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-standby-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                groups in STANDBY state
                ''',
                'ipv6_virtual_ip_addresses_standby_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-standby-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on groups
                in STANDBY state
                ''',
                'ipv6_virtual_ip_addresses_standby_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv4-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv4 caps in
                DOWN state
                ''',
                'tracked_interfaces_ipv4_state_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv4-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv4 caps in
                UP state
                ''',
                'tracked_interfaces_ipv4_state_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv6-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv6 caps in
                DOWN state
                ''',
                'tracked_interfaces_ipv6_state_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv6-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv6 caps in
                UP state
                ''',
                'tracked_interfaces_ipv6_state_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-objects-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked objects in DOWN state
                ''',
                'tracked_objects_down',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('tracked-objects-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked objects in UP state
                ''',
                'tracked_objects_up',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
    'Hsrp' : {
        'meta_info' : _MetaInfoClass('Hsrp',
            False, 
            [
            _MetaInfoClassMember('bfd-sessions', REFERENCE_CLASS, 'BfdSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.BfdSessions', 
                [], [], 
                '''                The table of HSRP BFD Sessions
                ''',
                'bfd_sessions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv4', 
                [], [], 
                '''                IPv4 HSRP information
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Ipv6', 
                [], [], 
                '''                IPv6 HSRP information
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('mgo-sessions', REFERENCE_CLASS, 'MgoSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.MgoSessions', 
                [], [], 
                '''                HSRP MGO session table
                ''',
                'mgo_sessions',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper', 'Hsrp.Summary', 
                [], [], 
                '''                HSRP summary statistics
                ''',
                'summary',
                'Cisco-IOS-XR-ipv4-hsrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-oper',
            'hsrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_hsrp_oper'
        ),
    },
}
_meta_table['Hsrp.Ipv4.Groups.Group.StateChangeHistory.Time']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group.StateChangeHistory']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group.ResignSentTime']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group.ResignReceivedTime']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group.CoupSentTime']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group.CoupReceivedTime']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group.Statistics']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group.GlobalAddress']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group.StateChangeHistory']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv4.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Groups']['meta_info']
_meta_table['Hsrp.Ipv4.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Ipv4.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Ipv4.Interfaces.Interface.Statistics']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Ipv4.Interfaces.Interface']['meta_info'].parent =_meta_table['Hsrp.Ipv4.Interfaces']['meta_info']
_meta_table['Hsrp.Ipv4.Groups']['meta_info'].parent =_meta_table['Hsrp.Ipv4']['meta_info']
_meta_table['Hsrp.Ipv4.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Ipv4']['meta_info']
_meta_table['Hsrp.Ipv4.Interfaces']['meta_info'].parent =_meta_table['Hsrp.Ipv4']['meta_info']
_meta_table['Hsrp.MgoSessions.MgoSession.Slave']['meta_info'].parent =_meta_table['Hsrp.MgoSessions.MgoSession']['meta_info']
_meta_table['Hsrp.MgoSessions.MgoSession']['meta_info'].parent =_meta_table['Hsrp.MgoSessions']['meta_info']
_meta_table['Hsrp.Ipv6.TrackedInterfaces.TrackedInterface']['meta_info'].parent =_meta_table['Hsrp.Ipv6.TrackedInterfaces']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.StateChangeHistory.Time']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group.StateChangeHistory']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.ResignSentTime']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.ResignReceivedTime']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.CoupSentTime']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.CoupReceivedTime']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.Statistics']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.GlobalAddress']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group.StateChangeHistory']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info']
_meta_table['Hsrp.Ipv6.Groups.Group']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Groups']['meta_info']
_meta_table['Hsrp.Ipv6.Interfaces.Interface.Statistics']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Interfaces.Interface']['meta_info']
_meta_table['Hsrp.Ipv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Hsrp.Ipv6.Interfaces']['meta_info']
_meta_table['Hsrp.Ipv6.TrackedInterfaces']['meta_info'].parent =_meta_table['Hsrp.Ipv6']['meta_info']
_meta_table['Hsrp.Ipv6.Groups']['meta_info'].parent =_meta_table['Hsrp.Ipv6']['meta_info']
_meta_table['Hsrp.Ipv6.Interfaces']['meta_info'].parent =_meta_table['Hsrp.Ipv6']['meta_info']
_meta_table['Hsrp.BfdSessions.BfdSession.Group']['meta_info'].parent =_meta_table['Hsrp.BfdSessions.BfdSession']['meta_info']
_meta_table['Hsrp.BfdSessions.BfdSession']['meta_info'].parent =_meta_table['Hsrp.BfdSessions']['meta_info']
_meta_table['Hsrp.Ipv4']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
_meta_table['Hsrp.MgoSessions']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
_meta_table['Hsrp.Ipv6']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
_meta_table['Hsrp.BfdSessions']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
_meta_table['Hsrp.Summary']['meta_info'].parent =_meta_table['Hsrp']['meta_info']
