


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SrgShowRoleEnum' : _MetaInfoEnum('SrgShowRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'none':'none',
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SrgShowSoReasonEnum' : _MetaInfoEnum('SrgShowSoReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'internal':'internal',
            'admin':'admin',
            'peer-up':'peer_up',
            'peer-down':'peer_down',
            'object-tracking-status-change':'object_tracking_status_change',
            'srg-show-so-reason-max':'srg_show_so_reason_max',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SrgShowCompEnum' : _MetaInfoEnum('SrgShowCompEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'srga':'srga',
            'dhcpv4':'dhcpv4',
            'dhcpv6':'dhcpv6',
            'pppoe':'pppoe',
            'ppp':'ppp',
            'l2tp':'l2tp',
            'iedge':'iedge',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SrgShowSlaveModeEnum' : _MetaInfoEnum('SrgShowSlaveModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'none':'none',
            'warm':'warm',
            'hot':'hot',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SrgShowSessionOperationEnum' : _MetaInfoEnum('SrgShowSessionOperationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'none':'none',
            'update':'update',
            'delete':'delete',
            'in-sync':'in_sync',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SrgPeerStatusEnum' : _MetaInfoEnum('SrgPeerStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'not-configured':'not_configured',
            'initialize':'initialize',
            'retry':'retry',
            'connect':'connect',
            'listen':'listen',
            'registration':'registration',
            'cleanup':'cleanup',
            'connected':'connected',
            'established':'established',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SrgShowSessionErrorEnum' : _MetaInfoEnum('SrgShowSessionErrorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'none':'none',
            'hard':'hard',
            'soft':'soft',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SrgShowImRoleEnum' : _MetaInfoEnum('SrgShowImRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper',
        {
            'none':'none',
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-subscriber-srg-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper']),
    'SubscriberRedundancyManager.Groups.Group' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyManager.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group
                ''',
                'group',
                'Cisco-IOS-XR-subscriber-srg-oper', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group Description
                ''',
                'description',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Count
                ''',
                'interface_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Information
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Object Tracking Status (Enabled/Disabled)
                ''',
                'object_tracking_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 Address
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv6 Address
                ''',
                'peer_ipv6_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Preferred Role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SrgShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowImRoleEnum', 
                [], [], 
                '''                SRG Role
                ''',
                'role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SrgShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Virtual MAC Address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('virtual-mac-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Virtual MAC Address Disable
                ''',
                'virtual_mac_address_disable',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyManager.Groups' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyManager.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyManager.Groups.Group', 
                [], [], 
                '''                Subscriber redundancy manager group
                ''',
                'group',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyManager.Summary' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyManager.Summary',
            False, 
            [
            _MetaInfoClassMember('active-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Process Active State
                ''',
                'active_state',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('disabled-group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Disabled Groups by Config
                ''',
                'disabled_group_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Configured Groups
                ''',
                'group_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switch Over Hold Time
                ''',
                'hold_timer',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Configured Interfaces
                ''',
                'interface_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('master-group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Master/Active Groups
                ''',
                'master_group_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('master-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Master/Active Interfaces
                ''',
                'master_interface_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Preferred Role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('slave-group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Slave Groups
                ''',
                'slave_group_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('slave-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Slave Interfaces
                ''',
                'slave_interface_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SrgShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('source-interface-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Interface IPv4 Address
                ''',
                'source_interface_ipv4_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('source-interface-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Interface IPv6 Address
                ''',
                'source_interface_ipv6_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('source-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Interface Name
                ''',
                'source_interface_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyManager.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyManager.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-srg-oper', True),
            _MetaInfoClassMember('forward-referenced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Forward Referenced
                ''',
                'forward_referenced',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-mapping-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Mapping ID
                ''',
                'interface_mapping_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SrgShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowImRoleEnum', 
                [], [], 
                '''                SRG Role
                ''',
                'role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyManager.Interfaces' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyManager.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyManager.Interfaces.Interface', 
                [], [], 
                '''                Subscriber redundancy manager interface
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyManager' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyManager',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyManager.Groups', 
                [], [], 
                '''                Subscriber Redundancy Manager group table
                ''',
                'groups',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyManager.Interfaces', 
                [], [], 
                '''                Subscriber Redundancy Manager interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyManager.Summary', 
                [], [], 
                '''                Subscriber redundancy manager summary
                ''',
                'summary',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'subscriber-redundancy-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'SrgShowCompEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowCompEnum', 
                [], [], 
                '''                Component
                ''',
                'component',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('marked-for-cleanup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Marked For Cleanup
                ''',
                'marked_for_cleanup',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('marked-for-sweeping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Marked For Sweeping
                ''',
                'marked_for_sweeping',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'SrgShowSessionOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowSessionOperationEnum', 
                [], [], 
                '''                Operation Code
                ''',
                'operation',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('tx-list-queue-fail', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tx List Queue Failed
                ''',
                'tx_list_queue_fail',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'session-detailed-information',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation',
            False, 
            [
            _MetaInfoClassMember('last-error-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Error Code
                ''',
                'last_error_code',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('last-error-type', REFERENCE_ENUM_CLASS, 'SrgShowSessionErrorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowSessionErrorEnum', 
                [], [], 
                '''                Last Error Type
                ''',
                'last_error_type',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('sync-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                No. of Errors occured during Synchronization
                ''',
                'sync_error_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'session-sync-error-information',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                GroupId
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', True),
            _MetaInfoClassMember('group-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('inner-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Inner VLAN Information
                ''',
                'inner_vlan',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('l2tp-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L2TP Tunnel local ID
                ''',
                'l2tp_tunnel_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('negative-acknowledgement-update-all', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Negative Acknowledgement Update Flag is Set
                ''',
                'negative_acknowledgement_update_all',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('outer-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outer VLAN Information
                ''',
                'outer_vlan',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('pppoe-session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                PPPoE Session ID
                ''',
                'pppoe_session_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('role-master', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Master Role is Set
                ''',
                'role_master',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-detailed-information', REFERENCE_LIST, 'SessionDetailedInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation', 
                [], [], 
                '''                More Session Information
                ''',
                'session_detailed_information',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session MAC Address
                ''',
                'session_mac_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-sync-error-information', REFERENCE_LIST, 'SessionSyncErrorInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation', 
                [], [], 
                '''                Session Synchroniation Error Information
                ''',
                'session_sync_error_information',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('valid-mac-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Holds a Valid MAC Address
                ''',
                'valid_mac_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'group-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupIdXr',
            False, 
            [
            _MetaInfoClassMember('group-id', REFERENCE_LIST, 'GroupId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId', 
                [], [], 
                '''                Group id for subscriber group session
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'group-id-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper',
            False, 
            [
            _MetaInfoClassMember('idb-oper-attr-update', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Attribute Update
                ''',
                'idb_oper_attr_update',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-oper-caps-add', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Caps Add
                ''',
                'idb_oper_caps_add',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-oper-caps-remove', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Caps Remove
                ''',
                'idb_oper_caps_remove',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-oper-reg-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Registration Disabled
                ''',
                'idb_oper_reg_disable',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-oper-reg-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Registration Enabled
                ''',
                'idb_oper_reg_enable',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'interface-oper',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus',
            False, 
            [
            _MetaInfoClassMember('idb-client-eoms-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Client EOMS Pending
                ''',
                'idb_client_eoms_pending',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-state-caps-added', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Caps Added
                ''',
                'idb_state_caps_added',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-state-fwd-ref', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Forward Referenced
                ''',
                'idb_state_fwd_ref',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-state-owned-re-source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Owned Resource
                ''',
                'idb_state_owned_re_source',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-state-p-end-caps-rem', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Caps Remove Pending
                ''',
                'idb_state_p_end_caps_rem',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-state-p-end-reg-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Registration Disable Pending
                ''',
                'idb_state_p_end_reg_disable',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-state-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Registered
                ''',
                'idb_state_registered',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('idb-state-stale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Stale
                ''',
                'idb_state_stale',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'interface-status',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'SrgShowCompEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowCompEnum', 
                [], [], 
                '''                Component
                ''',
                'component',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('srg-show-idb-client-eoms-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SRG SHOW IDB CLIENT EOMS PENDING
                ''',
                'srg_show_idb_client_eoms_pending',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('srg-show-idb-client-sync-eod-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SRG SHOW IDB CLIENT SYNC EOD PENDING
                ''',
                'srg_show_idb_client_sync_eod_pending',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'client-status',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-srg-oper', True),
            _MetaInfoClassMember('client-status', REFERENCE_LIST, 'ClientStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus', 
                [], [], 
                '''                Interface status for each client
                ''',
                'client_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('forward-referenced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Forward Referenced
                ''',
                'forward_referenced',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-attribute-update-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Attribute Update Error Count
                ''',
                'interface_attribute_update_error_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-caps-add-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Caps Add Error Count
                ''',
                'interface_caps_add_error_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-caps-remove-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Caps Remove Error Count
                ''',
                'interface_caps_remove_error_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-disable-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Disable Error Count
                ''',
                'interface_disable_error_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-enable-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Enable Error Count
                ''',
                'interface_enable_error_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-oper', REFERENCE_CLASS, 'InterfaceOper' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper', 
                [], [], 
                '''                Interface Batch Operation
                ''',
                'interface_oper',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_CLASS, 'InterfaceStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus', 
                [], [], 
                '''                Interface Status
                ''',
                'interface_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-synchronization-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Sync ID
                ''',
                'interface_synchronization_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SrgShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowImRoleEnum', 
                [], [], 
                '''                SRG Role
                ''',
                'role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Specify interface name
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                GroupId
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', True),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Count
                ''',
                'interface_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Object Tracking Status (Enabled/Disabled)
                ''',
                'object_tracking_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 Address
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv6 Address
                ''',
                'peer_ipv6_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-status', REFERENCE_ENUM_CLASS, 'SrgPeerStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgPeerStatusEnum', 
                [], [], 
                '''                Peer Status
                ''',
                'peer_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('pending-add-session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Session Count for Synchornization
                ''',
                'pending_add_session_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Preferred Role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SrgShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowImRoleEnum', 
                [], [], 
                '''                SRG Role
                ''',
                'role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SrgShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'group-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupSummaries' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupSummaries',
            False, 
            [
            _MetaInfoClassMember('group-summary', REFERENCE_LIST, 'GroupSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary', 
                [], [], 
                '''                Subscriber redundancy agent group summary
                ''',
                'group_summary',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'group-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface',
            False, 
            [
            _MetaInfoClassMember('forward-referenced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Forward Referenced
                ''',
                'forward_referenced',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-synchronization-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Synchronization ID
                ''',
                'interface_synchronization_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group Id
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', True),
            _MetaInfoClassMember('access-tracking-object-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Object Tracking Name
                ''',
                'access_tracking_object_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('access-tracking-object-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Access Object Tracking Status
                ''',
                'access_tracking_object_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('core-tracking-object-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Core Object Tracking Name
                ''',
                'core_tracking_object_name',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('core-tracking-object-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Core Object Tracking Status
                ''',
                'core_tracking_object_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('current-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Current Role
                ''',
                'current_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group Description
                ''',
                'description',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switch Over Hold Time
                ''',
                'hold_timer',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('init-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Preferred Init Role
                ''',
                'init_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface', 
                [], [], 
                '''                Interface List
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Configured Interfaces
                ''',
                'interface_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('l2tp-source-ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                L2TP Souce IP Address
                ''',
                'l2tp_source_ip',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('last-switchover-reason', REFERENCE_ENUM_CLASS, 'SrgShowSoReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowSoReasonEnum', 
                [], [], 
                '''                Last Switchover Reason
                ''',
                'last_switchover_reason',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('last-switchover-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Switchover time
                ''',
                'last_switchover_time',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('negotiating-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Negotiating Role
                ''',
                'negotiating_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Object Tracking Status (Enabled/Disabled)
                ''',
                'object_tracking_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-current-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Peer Current Role
                ''',
                'peer_current_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-init-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Peer Preferred Init Role
                ''',
                'peer_init_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 Address
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv6 Address
                ''',
                'peer_ipv6_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-last-down-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Down time of Peer
                ''',
                'peer_last_down_time',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-last-negotiation-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Negotiation time of Peer
                ''',
                'peer_last_negotiation_time',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-last-up-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last UP time of Peer
                ''',
                'peer_last_up_time',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-negotiating-role', REFERENCE_ENUM_CLASS, 'SrgShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowRoleEnum', 
                [], [], 
                '''                Peer Negotiating Role
                ''',
                'peer_negotiating_role',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Peer Object Tracking Status
                ''',
                'peer_object_tracking_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('peer-status', REFERENCE_ENUM_CLASS, 'SrgPeerStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgPeerStatusEnum', 
                [], [], 
                '''                Peer Status
                ''',
                'peer_status',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('pending-session-delete-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Session Delete Count
                ''',
                'pending_session_delete_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('pending-session-update-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Session Update Count
                ''',
                'pending_session_update_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('revertive-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Revertive timer for SWO back
                ''',
                'revertive_timer',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SrgShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SrgShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('slave-update-failure-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Slave Session update fail count
                ''',
                'slave_update_failure_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('switchover-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switchover Count
                ''',
                'switchover_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('switchover-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switchover Hold Time in seconds
                ''',
                'switchover_hold_time',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('switchover-revert-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switchover Revert Time in seconds
                ''',
                'switchover_revert_time',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('tunnel-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel Count
                ''',
                'tunnel_count',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Virtual MAC Address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('virtual-mac-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Virtual MAC Address Disable
                ''',
                'virtual_mac_address_disable',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'group-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node.GroupIds' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node.GroupIds',
            False, 
            [
            _MetaInfoClassMember('group-id', REFERENCE_LIST, 'GroupId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId', 
                [], [], 
                '''                Group id for subscriber group
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'group-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-srg-oper', True),
            _MetaInfoClassMember('group-id-xr', REFERENCE_CLASS, 'GroupIdXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupIdXr', 
                [], [], 
                '''                Data for particular subscriber group session
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-ids', REFERENCE_CLASS, 'GroupIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupIds', 
                [], [], 
                '''                Data for particular subscriber group 
                ''',
                'group_ids',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('group-summaries', REFERENCE_CLASS, 'GroupSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.GroupSummaries', 
                [], [], 
                '''                Subscriber data for a particular node
                ''',
                'group_summaries',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node.Interfaces', 
                [], [], 
                '''                List of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent.Nodes' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes.Node', 
                [], [], 
                '''                Subscriber data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
    'SubscriberRedundancyAgent' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancyAgent',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper', 'SubscriberRedundancyAgent.Nodes', 
                [], [], 
                '''                List of nodes for which subscriber data is
                collected
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-srg-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-oper',
            'subscriber-redundancy-agent',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_oper'
        ),
    },
}
_meta_table['SubscriberRedundancyManager.Groups.Group']['meta_info'].parent =_meta_table['SubscriberRedundancyManager.Groups']['meta_info']
_meta_table['SubscriberRedundancyManager.Interfaces.Interface']['meta_info'].parent =_meta_table['SubscriberRedundancyManager.Interfaces']['meta_info']
_meta_table['SubscriberRedundancyManager.Groups']['meta_info'].parent =_meta_table['SubscriberRedundancyManager']['meta_info']
_meta_table['SubscriberRedundancyManager.Summary']['meta_info'].parent =_meta_table['SubscriberRedundancyManager']['meta_info']
_meta_table['SubscriberRedundancyManager.Interfaces']['meta_info'].parent =_meta_table['SubscriberRedundancyManager']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupSummaries']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds.GroupId']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIdXr']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupSummaries']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node.GroupIds']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes.Node']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent.Nodes']['meta_info']
_meta_table['SubscriberRedundancyAgent.Nodes']['meta_info'].parent =_meta_table['SubscriberRedundancyAgent']['meta_info']
