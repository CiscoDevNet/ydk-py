


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SergShowSessionOperationEnum' : _MetaInfoEnum('SergShowSessionOperationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'none':'none',
            'update':'update',
            'delete':'delete',
            'in-sync':'in_sync',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergShowSlaveModeEnum' : _MetaInfoEnum('SergShowSlaveModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'none':'none',
            'warm':'warm',
            'hot':'hot',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergShowMemEnum' : _MetaInfoEnum('SergShowMemEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'standard':'standard',
            'chunk':'chunk',
            'edm':'edm',
            'string':'string',
            'static':'static',
            'unknown':'unknown',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergPeerStatusEnum' : _MetaInfoEnum('SergPeerStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
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
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergShowCompEnum' : _MetaInfoEnum('SergShowCompEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'serga':'serga',
            'ipv6nd':'ipv6nd',
            'dhcpv6':'dhcpv6',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergShowSoReasonEnum' : _MetaInfoEnum('SergShowSoReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'internal':'internal',
            'admin':'admin',
            'peer-up':'peer_up',
            'peer-down':'peer_down',
            'object-tracking-status-change':'object_tracking_status_change',
            'serg-show-so-reason-max':'serg_show_so_reason_max',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergShowRoleEnum' : _MetaInfoEnum('SergShowRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'none':'none',
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergShowSessionErrorEnum' : _MetaInfoEnum('SergShowSessionErrorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'none':'none',
            'hard':'hard',
            'soft':'soft',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SergShowImRoleEnum' : _MetaInfoEnum('SergShowImRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper',
        {
            'none':'none',
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-infra-serg-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper']),
    'SessionRedundancyManager.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyManager.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('forward-referenced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Forward Referenced
                ''',
                'forward_referenced',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-mapping-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Mapping ID
                ''',
                'interface_mapping_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SergShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRoleEnum', 
                [], [], 
                '''                SERG Role
                ''',
                'role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyManager.Interfaces' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyManager.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyManager.Interfaces.Interface', 
                [], [], 
                '''                interface redundancy manager interface
                ''',
                'interface',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyManager.Groups.Group' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyManager.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group
                ''',
                'group',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group Description
                ''',
                'description',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Count
                ''',
                'interface_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Information
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Object Tracking Status (Enabled/Disabled)
                ''',
                'object_tracking_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 Address
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv6 Address
                ''',
                'peer_ipv6_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Preferred Role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SergShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRoleEnum', 
                [], [], 
                '''                SERG Role
                ''',
                'role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SergShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyManager.Groups' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyManager.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyManager.Groups.Group', 
                [], [], 
                '''                Session redundancy manager group
                ''',
                'group',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyManager.Summary' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyManager.Summary',
            False, 
            [
            _MetaInfoClassMember('active-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Process Active State
                ''',
                'active_state',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('disabled-group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Disabled Groups by Config
                ''',
                'disabled_group_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Configured Groups
                ''',
                'group_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switch Over Hold Time
                ''',
                'hold_timer',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Configured Interfaces
                ''',
                'interface_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('master-group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Master/Active Groups
                ''',
                'master_group_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('master-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Master/Active Interfaces
                ''',
                'master_interface_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Preferred Role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('slave-group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Slave Groups
                ''',
                'slave_group_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('slave-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Slave Interfaces
                ''',
                'slave_interface_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SergShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('source-interface-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Interface IPv4 Address
                ''',
                'source_interface_ipv4_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('source-interface-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Interface IPv6 Address
                ''',
                'source_interface_ipv6_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('source-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Interface Name
                ''',
                'source_interface_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyManager' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyManager',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyManager.Groups', 
                [], [], 
                '''                Session Redundancy Manager group table
                ''',
                'groups',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyManager.Interfaces', 
                [], [], 
                '''                Subscriber Redundancy Manager interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyManager.Summary', 
                [], [], 
                '''                Session redundancy manager summary
                ''',
                'summary',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'session-redundancy-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'SergShowCompEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowCompEnum', 
                [], [], 
                '''                Component
                ''',
                'component',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('marked-for-cleanup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Marked For Cleanup
                ''',
                'marked_for_cleanup',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('marked-for-sweeping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Marked For Sweeping
                ''',
                'marked_for_sweeping',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('operation', REFERENCE_ENUM_CLASS, 'SergShowSessionOperationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSessionOperationEnum', 
                [], [], 
                '''                Operation Code
                ''',
                'operation',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-queue-fail', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tx List Queue Failed
                ''',
                'tx_list_queue_fail',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'session-detailed-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation',
            False, 
            [
            _MetaInfoClassMember('last-error-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Error Code
                ''',
                'last_error_code',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('last-error-type', REFERENCE_ENUM_CLASS, 'SergShowSessionErrorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSessionErrorEnum', 
                [], [], 
                '''                Last Error Type
                ''',
                'last_error_type',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('sync-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                No. of Errors occured during Synchronization
                ''',
                'sync_error_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'session-sync-error-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                GroupId
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('group-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('key-index', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key index
                ''',
                'key_index',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('negative-acknowledgement-update-all', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Negative Acknowledgement Update Flag is Set
                ''',
                'negative_acknowledgement_update_all',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('role-master', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Master Role is Set
                ''',
                'role_master',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-detailed-information', REFERENCE_LIST, 'SessionDetailedInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation', 
                [], [], 
                '''                More Session Information
                ''',
                'session_detailed_information',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-sync-error-information', REFERENCE_LIST, 'SessionSyncErrorInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation', 
                [], [], 
                '''                Session Synchroniation Error Information
                ''',
                'session_sync_error_information',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'group-id',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIdXr' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIdXr',
            False, 
            [
            _MetaInfoClassMember('group-id', REFERENCE_LIST, 'GroupId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId', 
                [], [], 
                '''                Group id for subscriber group session
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'group-id-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId',
            False, 
            [
            _MetaInfoClassMember('stats-client-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Client Id
                ''',
                'stats_client_id',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('clean-call-back', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CleanCallBack
                ''',
                'clean_call_back',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('last-replay-all-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LastReplayAllCount
                ''',
                'last_replay_all_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-active-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListActiveNotOk
                ''',
                'tx_list_active_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-active-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListActiveOk
                ''',
                'tx_list_active_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-clear-all-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClearAllAddNotOk
                ''',
                'tx_list_clear_all_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-clear-all-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClearAllAddOk
                ''',
                'tx_list_clear_all_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-clear-selected-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClearSelectedAddNotOk
                ''',
                'tx_list_clear_selected_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-clear-selected-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClearSelectedAddOk
                ''',
                'tx_list_clear_selected_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-cleanup', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientCleanup
                ''',
                'tx_list_client_cleanup',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-connection-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientConnectionDown
                ''',
                'tx_list_client_connection_down',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-de-registration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientDeRegistration
                ''',
                'tx_list_client_de_registration',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-registration-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientRegistrationNotOk
                ''',
                'tx_list_client_registration_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-registration-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientRegistrationOk
                ''',
                'tx_list_client_registration_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-de-active-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListDeActiveNotOk
                ''',
                'tx_list_de_active_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-de-active-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListDeActiveOk
                ''',
                'tx_list_de_active_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-session-session-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeSessionSessionOk
                ''',
                'tx_list_encode_session_session_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-session-session-partial-write', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeSessionSessionPartialWrite
                ''',
                'tx_list_encode_session_session_partial_write',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-end-of-download-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEndOfDownloadAddNotOk
                ''',
                'tx_list_end_of_download_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-end-of-download-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEndOfDownloadAddOk
                ''',
                'tx_list_end_of_download_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-end-of-message-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEndOfMessageAddNotOk
                ''',
                'tx_list_end_of_message_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-end-of-message-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEndOfMessageAddOk
                ''',
                'tx_list_end_of_message_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-command-replay-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveCommandReplayAll
                ''',
                'tx_list_receive_command_replay_all',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-command-replay-selected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveCommandReplaySelected
                ''',
                'tx_list_receive_command_replay_selected',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-clear-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionClearAll
                ''',
                'tx_list_receive_session_session_clear_all',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-clear-selected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionClearSelected
                ''',
                'tx_list_receive_session_session_clear_selected',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-delete-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionDeleteInValid
                ''',
                'tx_list_receive_session_session_delete_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-delete-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionDeleteValid
                ''',
                'tx_list_receive_session_session_delete_valid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-eod-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionEODAll
                ''',
                'tx_list_receive_session_session_eod_all',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-eod-selected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionEODSelected
                ''',
                'tx_list_receive_session_session_eod_selected',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-eoms', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionEOMS
                ''',
                'tx_list_receive_session_session_eoms',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-neg-ack', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionNegAck
                ''',
                'tx_list_receive_session_session_neg_ack',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-neg-ack-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionNegAckNotOk
                ''',
                'tx_list_receive_session_session_neg_ack_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-sod-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionSODAll
                ''',
                'tx_list_receive_session_session_sod_all',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-sod-selected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionSODSelected
                ''',
                'tx_list_receive_session_session_sod_selected',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-update-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionUpdateInValid
                ''',
                'tx_list_receive_session_session_update_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-receive-session-session-update-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReceiveSessionSessionUpdateValid
                ''',
                'tx_list_receive_session_session_update_valid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-replay-all-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReplayAllAddNotOk
                ''',
                'tx_list_replay_all_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-replay-all-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReplayAllAddOk
                ''',
                'tx_list_replay_all_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-replay-selected-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReplaySelectedAddNotOk
                ''',
                'tx_list_replay_selected_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-replay-selected-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListReplaySelectedAddOk
                ''',
                'tx_list_replay_selected_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-session-session-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListSessionSessionAddNotOk
                ''',
                'tx_list_session_session_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-session-session-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListSessionSessionAddOk
                ''',
                'tx_list_session_session_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-session-session-delete', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListSessionSessionDelete
                ''',
                'tx_list_session_session_delete',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-session-session-update-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListSessionSessionUpdateNotOk
                ''',
                'tx_list_session_session_update_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-session-session-update-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListSessionSessionUpdateOk
                ''',
                'tx_list_session_session_update_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-start-of-download-add-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListStartOfDownloadAddNotOk
                ''',
                'tx_list_start_of_download_add_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-start-of-download-add-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListStartOfDownloadAddOk
                ''',
                'tx_list_start_of_download_add_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'client-id',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.ClientIds' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.ClientIds',
            False, 
            [
            _MetaInfoClassMember('client-id', REFERENCE_LIST, 'ClientId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId', 
                [], [], 
                '''                Specify stats client
                ''',
                'client_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'client-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo',
            False, 
            [
            _MetaInfoClassMember('alloc-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocated count
                ''',
                'alloc_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('alloc-fails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocation Fails
                ''',
                'alloc_fails',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('current-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Count
                ''',
                'current_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('freed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Freed Count
                ''',
                'freed_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('memory-type', REFERENCE_ENUM_CLASS, 'SergShowMemEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowMemEnum', 
                [], [], 
                '''                Memory Type
                ''',
                'memory_type',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Size of the datastructure
                ''',
                'size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('structure-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Structure Name
                ''',
                'structure_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'memory-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo',
            False, 
            [
            _MetaInfoClassMember('failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit failure
                ''',
                'failure',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Size of the block
                ''',
                'size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit success
                ''',
                'success',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total request
                ''',
                'total',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'edm-memory-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo',
            False, 
            [
            _MetaInfoClassMember('failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit failure
                ''',
                'failure',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Size of the block
                ''',
                'size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit success
                ''',
                'success',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total request
                ''',
                'total',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'string-memory-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Memory' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Memory',
            False, 
            [
            _MetaInfoClassMember('edm-memory-info', REFERENCE_LIST, 'EdmMemoryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo', 
                [], [], 
                '''                EDM Memory Info
                ''',
                'edm_memory_info',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('memory-info', REFERENCE_LIST, 'MemoryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo', 
                [], [], 
                '''                Memory Info
                ''',
                'memory_info',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('string-memory-info', REFERENCE_LIST, 'StringMemoryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo', 
                [], [], 
                '''                String Memory Info
                ''',
                'string_memory_info',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'memory',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'SergShowCompEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowCompEnum', 
                [], [], 
                '''                Component
                ''',
                'component',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'client-session-count',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface',
            False, 
            [
            _MetaInfoClassMember('forward-referenced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Forward Referenced
                ''',
                'forward_referenced',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-synchronization-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Synchronization ID
                ''',
                'interface_synchronization_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group Id
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('access-tracking-object-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Object Tracking Name
                ''',
                'access_tracking_object_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('access-tracking-object-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Access Object Tracking Status
                ''',
                'access_tracking_object_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('client-session-count', REFERENCE_LIST, 'ClientSessionCount' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount', 
                [], [], 
                '''                Client Session Count
                ''',
                'client_session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('core-tracking-object-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Core Object Tracking Name
                ''',
                'core_tracking_object_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('core-tracking-object-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Core Object Tracking Status
                ''',
                'core_tracking_object_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('current-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Current Role
                ''',
                'current_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group Description
                ''',
                'description',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switch Over Hold Time
                ''',
                'hold_timer',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('init-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Preferred Init Role
                ''',
                'init_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface', 
                [], [], 
                '''                Interface List
                ''',
                'interface',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of Configured Interfaces
                ''',
                'interface_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('last-switchover-reason', REFERENCE_ENUM_CLASS, 'SergShowSoReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSoReasonEnum', 
                [], [], 
                '''                Last Switchover Reason
                ''',
                'last_switchover_reason',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('last-switchover-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Switchover time
                ''',
                'last_switchover_time',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('negotiating-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Negotiating Role
                ''',
                'negotiating_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Object Tracking Status (Enabled/Disabled)
                ''',
                'object_tracking_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-current-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Peer Current Role
                ''',
                'peer_current_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-init-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Peer Preferred Init Role
                ''',
                'peer_init_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 Address
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv6 Address
                ''',
                'peer_ipv6_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-last-down-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Down time of Peer
                ''',
                'peer_last_down_time',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-last-negotiation-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Negotiation time of Peer
                ''',
                'peer_last_negotiation_time',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-last-up-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last UP time of Peer
                ''',
                'peer_last_up_time',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-negotiating-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Peer Negotiating Role
                ''',
                'peer_negotiating_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Peer Object Tracking Status
                ''',
                'peer_object_tracking_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-status', REFERENCE_ENUM_CLASS, 'SergPeerStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergPeerStatusEnum', 
                [], [], 
                '''                Peer Status
                ''',
                'peer_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('pending-session-delete-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Session Delete Count
                ''',
                'pending_session_delete_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('pending-session-update-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Session Update Count
                ''',
                'pending_session_update_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('revertive-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Revertive timer for SWO back
                ''',
                'revertive_timer',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SergShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('slave-update-failure-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Slave Session update fail count
                ''',
                'slave_update_failure_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('switchover-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switchover Count
                ''',
                'switchover_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('switchover-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switchover Hold Time in seconds
                ''',
                'switchover_hold_time',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('switchover-revert-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switchover Revert Time in seconds
                ''',
                'switchover_revert_time',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'group-id',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupIds' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupIds',
            False, 
            [
            _MetaInfoClassMember('group-id', REFERENCE_LIST, 'GroupId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId', 
                [], [], 
                '''                Group id for subscriber group
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'group-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper',
            False, 
            [
            _MetaInfoClassMember('idb-oper-attr-update', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Attribute Update
                ''',
                'idb_oper_attr_update',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-oper-caps-add', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Caps Add
                ''',
                'idb_oper_caps_add',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-oper-caps-remove', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Caps Remove
                ''',
                'idb_oper_caps_remove',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-oper-reg-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Registration Disabled
                ''',
                'idb_oper_reg_disable',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-oper-reg-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Operational Registration Enabled
                ''',
                'idb_oper_reg_enable',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'interface-oper',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus',
            False, 
            [
            _MetaInfoClassMember('idb-client-eoms-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Client EOMS Pending
                ''',
                'idb_client_eoms_pending',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-state-caps-added', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Caps Added
                ''',
                'idb_state_caps_added',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-state-fwd-ref', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Forward Referenced
                ''',
                'idb_state_fwd_ref',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-state-owned-re-source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Owned Resource
                ''',
                'idb_state_owned_re_source',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-state-p-end-caps-rem', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Caps Remove Pending
                ''',
                'idb_state_p_end_caps_rem',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-state-p-end-reg-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface Registration Disable Pending
                ''',
                'idb_state_p_end_reg_disable',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-state-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Registered
                ''',
                'idb_state_registered',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('idb-state-stale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface State Stale
                ''',
                'idb_state_stale',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'interface-status',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'SergShowCompEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowCompEnum', 
                [], [], 
                '''                Component
                ''',
                'component',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('serg-show-idb-client-eoms-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SERG SHOW IDB CLIENT EOMS PENDING
                ''',
                'serg_show_idb_client_eoms_pending',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('serg-show-idb-client-sync-eod-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SERG SHOW IDB CLIENT SYNC EOD PENDING
                ''',
                'serg_show_idb_client_sync_eod_pending',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                session count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'client-status',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('client-status', REFERENCE_LIST, 'ClientStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus', 
                [], [], 
                '''                Interface status for each client
                ''',
                'client_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('forward-referenced', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Forward Referenced
                ''',
                'forward_referenced',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-attribute-update-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Attribute Update Error Count
                ''',
                'interface_attribute_update_error_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-caps-add-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Caps Add Error Count
                ''',
                'interface_caps_add_error_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-caps-remove-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Caps Remove Error Count
                ''',
                'interface_caps_remove_error_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-disable-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Disable Error Count
                ''',
                'interface_disable_error_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-enable-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Enable Error Count
                ''',
                'interface_enable_error_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-oper', REFERENCE_CLASS, 'InterfaceOper' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper', 
                [], [], 
                '''                Interface Batch Operation
                ''',
                'interface_oper',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_CLASS, 'InterfaceStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus', 
                [], [], 
                '''                Interface Status
                ''',
                'interface_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-synchronization-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Sync ID
                ''',
                'interface_synchronization_id',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SergShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRoleEnum', 
                [], [], 
                '''                SERG Role
                ''',
                'role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Specify interface name
                ''',
                'interface',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics',
            False, 
            [
            _MetaInfoClassMember('grp-bound-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of interface bound to a group
                ''',
                'grp_bound_cnt',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('non-stale-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of non stale interfaces
                ''',
                'non_stale_cnt',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('pend-caps-rem-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of interfaces pending caps remove
                ''',
                'pend_caps_rem_cnt',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('pend-other-batch-oper-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of interfaces pending for other (except
                unreg/caps rem) batch oper
                ''',
                'pend_other_batch_oper_cnt',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('pend-reg-disable-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of interfaces pending red disable
                ''',
                'pend_reg_disable_cnt',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'intf-status-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics',
            False, 
            [
            _MetaInfoClassMember('tx-list-clean-command', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListCleanCommand
                ''',
                'tx_list_clean_command',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-clean-marker', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListCleanMarker
                ''',
                'tx_list_clean_marker',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-clean-negotiation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListCleanNegotiation
                ''',
                'tx_list_clean_negotiation',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-command-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeCommandOk
                ''',
                'tx_list_encode_command_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-command-partial-write', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeCommandPartialWrite
                ''',
                'tx_list_encode_command_partial_write',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-marker-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeMarkerOk
                ''',
                'tx_list_encode_marker_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-marker-partial-write', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeMarkerPartialWrite
                ''',
                'tx_list_encode_marker_partial_write',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-negotiation-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeNegotiationOk
                ''',
                'tx_list_encode_negotiation_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-encode-negotiation-partial-write', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListEncodeNegotiationPartialWrite
                ''',
                'tx_list_encode_negotiation_partial_write',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'tx-list-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus',
            False, 
            [
            _MetaInfoClassMember('clean-up-timer-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value in Seconds to trigger the client cleanup
                ''',
                'clean_up_timer_remaining',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('client-connection-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ClientConnectionStatus
                ''',
                'client_connection_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('client-initialization-synchronization-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ClientInitializationSynchronizationPending
                ''',
                'client_initialization_synchronization_pending',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('client-synchronization-end-of-download-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ClientSynchronizationEndOfDownloadPending
                ''',
                'client_synchronization_end_of_download_pending',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'SergShowCompEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowCompEnum', 
                [], [], 
                '''                Component
                ''',
                'component',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('down-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DownTimeStamp
                ''',
                'down_time_stamp',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('up-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                UpTimeStamp
                ''',
                'up_time_stamp',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'client-status',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'SergShowCompEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowCompEnum', 
                [], [], 
                '''                Component
                ''',
                'component',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('opaque-data-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Opaque Data Size for each component
                ''',
                'opaque_data_size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('opaque-high-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                High Watermark of Opaque Data Size for each
                component
                ''',
                'opaque_high_size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('opaque-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Opaque Memory Size for each component
                ''',
                'opaque_size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session count for each component
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'opaque-memory-status',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus',
            False, 
            [
            _MetaInfoClassMember('accept-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Socket Accept Count
                ''',
                'accept_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('active-socket-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Active Socket Count
                ''',
                'active_socket_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('blocked-connect-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocked Socket Connect Count
                ''',
                'blocked_connect_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('buffer-cache-hit', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Buffer Cache Hit Count
                ''',
                'buffer_cache_hit',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('buffer-cache-miss', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Buffer Cache Miss Count
                ''',
                'buffer_cache_miss',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('buffer-freed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Buffer Free Count
                ''',
                'buffer_freed_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('buffer-full-occurence-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Buffer Full on Write Occurence Count
                ''',
                'buffer_full_occurence_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('bytes-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bytes Received Count
                ''',
                'bytes_received',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bytes Sent Count
                ''',
                'bytes_sent',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('connect-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Socket Connect Count
                ''',
                'connect_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('connect-retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Socket Connect Retry Count
                ''',
                'connect_retry_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('maximum-received-message-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Size of Received Message
                ''',
                'maximum_received_message_size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('maximum-requested-buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Size of Requested Buffer
                ''',
                'maximum_requested_buffer_size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('maximum-sent-message-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Size of Sent Message
                ''',
                'maximum_sent_message_size',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('mem-move-bytes-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partial Message Memory Move Byte Count
                ''',
                'mem_move_bytes_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('mem-move-message-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partial Message Memory Move Occurence Count
                ''',
                'mem_move_message_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('messages-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message Received Count
                ''',
                'messages_received',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('messages-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message Sent Count
                ''',
                'messages_sent',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-pause-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peer Pause Count
                ''',
                'peer_pause_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('remote-node-down-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Peer DisConnect Count
                ''',
                'remote_node_down_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('socket-read-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Socket Read Count
                ''',
                'socket_read_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('socket-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Socket Write Count
                ''',
                'socket_write_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'tx-list-over-tcp-status',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.StatsGlobal' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.StatsGlobal',
            False, 
            [
            _MetaInfoClassMember('client-init-sync-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Synchronization TimeStamp
                ''',
                'client_init_sync_time_stamp',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('client-status', REFERENCE_LIST, 'ClientStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus', 
                [], [], 
                '''                Client Status
                ''',
                'client_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('intf-status-statistics', REFERENCE_CLASS, 'IntfStatusStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics', 
                [], [], 
                '''                intf status statistics
                ''',
                'intf_status_statistics',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('opaque-memory-status', REFERENCE_LIST, 'OpaqueMemoryStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus', 
                [], [], 
                '''                Opaque memory Stats
                ''',
                'opaque_memory_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-action-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value in Seconds to trigger the peer actions
                ''',
                'peer_action_timer',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-init-sync-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Synchronization TimeStamp
                ''',
                'peer_init_sync_time_stamp',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('redundancy-role', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Redundancy Role
                ''',
                'redundancy_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('restart-client-sync-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Restart Client Sync In Progress Flag
                ''',
                'restart_client_sync_in_progress',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('restart-peer-sync-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Restart Peer Sync In Progress Flag
                ''',
                'restart_peer_sync_in_progress',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('retry-timer-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value in Seconds to trigger the retry
                ''',
                'retry_timer_remaining',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('source-interface-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Interface IPv4 Address
                ''',
                'source_interface_ipv4_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('source-interface-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Interface IPv6 Address
                ''',
                'source_interface_ipv6_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('source-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Interface Name
                ''',
                'source_interface_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('sync-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sync In Progress Flag
                ''',
                'sync_in_progress',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-connection-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientConnectionDown
                ''',
                'tx_list_client_connection_down',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-connection-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientConnectionUp
                ''',
                'tx_list_client_connection_up',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-de-registration-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientDeRegistrationInvalid
                ''',
                'tx_list_client_de_registration_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-message-call-back', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientMessageCallBack
                ''',
                'tx_list_client_message_call_back',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-peer-done', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientPeerDone
                ''',
                'tx_list_client_peer_done',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-receive-command-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientReceiveCommandInValid
                ''',
                'tx_list_client_receive_command_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-receive-command-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientReceiveCommandValid
                ''',
                'tx_list_client_receive_command_valid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-receive-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientReceiveInValid
                ''',
                'tx_list_client_receive_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-receive-session-session-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientReceiveSessionSessionInValid
                ''',
                'tx_list_client_receive_session_session_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-receive-session-sessionvalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientReceiveSessionSessionValid
                ''',
                'tx_list_client_receive_session_sessionvalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-receive-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientReceiveValid
                ''',
                'tx_list_client_receive_valid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-client-registration-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListClientRegistrationInvalid
                ''',
                'tx_list_client_registration_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-over-tcp-status', REFERENCE_LIST, 'TxListOverTcpStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus', 
                [], [], 
                '''                TCP TxList Statistics
                ''',
                'tx_list_over_tcp_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-cmd-connection-down-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerCmdConnectionDownNotOk
                ''',
                'tx_list_peer_cmd_connection_down_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-cmd-connection-up-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerCmdConnectionUpNotOk
                ''',
                'tx_list_peer_cmd_connection_up_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-de-registration-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerDeRegistrationInValid
                ''',
                'tx_list_peer_de_registration_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-done', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerDone
                ''',
                'tx_list_peer_done',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-message-call-back-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerMessageCallBackInValid
                ''',
                'tx_list_peer_message_call_back_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-message-call-back-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerMessageCallBackValid
                ''',
                'tx_list_peer_message_call_back_valid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-registration-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerRegistrationInValid
                ''',
                'tx_list_peer_registration_invalid',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-session-connection-down-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerSessionConnectionDownNotOk
                ''',
                'tx_list_peer_session_connection_down_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-session-connection-up-not-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerSessionConnectionUpNotOk
                ''',
                'tx_list_peer_session_connection_up_not_ok',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-peer-timer-handler', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TxListPeerTimerHandler
                ''',
                'tx_list_peer_timer_handler',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('tx-list-statistics', REFERENCE_CLASS, 'TxListStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics', 
                [], [], 
                '''                tx list statistics
                ''',
                'tx_list_statistics',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'stats-global',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                GroupId
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disabled by Config
                ''',
                'disabled',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Count
                ''',
                'interface_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('object-tracking-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Object Tracking Status (Enabled/Disabled)
                ''',
                'object_tracking_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv4 Address
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer IPv6 Address
                ''',
                'peer_ipv6_address',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('peer-status', REFERENCE_ENUM_CLASS, 'SergPeerStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergPeerStatusEnum', 
                [], [], 
                '''                Peer Status
                ''',
                'peer_status',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('pending-add-session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pending Session Count for Synchornization
                ''',
                'pending_add_session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SergShowRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowRoleEnum', 
                [], [], 
                '''                Preferred Role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'SergShowImRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowImRoleEnum', 
                [], [], 
                '''                SERG Role
                ''',
                'role',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SergShowSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SergShowSlaveModeEnum', 
                [], [], 
                '''                Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'group-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node.GroupSummaries' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node.GroupSummaries',
            False, 
            [
            _MetaInfoClassMember('group-summary', REFERENCE_LIST, 'GroupSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary', 
                [], [], 
                '''                Session redundancy agent group summary
                ''',
                'group_summary',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'group-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-serg-oper', True),
            _MetaInfoClassMember('client-ids', REFERENCE_CLASS, 'ClientIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.ClientIds', 
                [], [], 
                '''                Stats Client
                ''',
                'client_ids',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-id-xr', REFERENCE_CLASS, 'GroupIdXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIdXr', 
                [], [], 
                '''                Data for particular subscriber group session
                ''',
                'group_id_xr',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-ids', REFERENCE_CLASS, 'GroupIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupIds', 
                [], [], 
                '''                Data for particular subscriber group 
                ''',
                'group_ids',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('group-summaries', REFERENCE_CLASS, 'GroupSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.GroupSummaries', 
                [], [], 
                '''                Session data for a particular node
                ''',
                'group_summaries',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Interfaces', 
                [], [], 
                '''                List of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('memory', REFERENCE_CLASS, 'Memory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.Memory', 
                [], [], 
                '''                Show Memory
                ''',
                'memory',
                'Cisco-IOS-XR-infra-serg-oper', False),
            _MetaInfoClassMember('stats-global', REFERENCE_CLASS, 'StatsGlobal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node.StatsGlobal', 
                [], [], 
                '''                Stats Global
                ''',
                'stats_global',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent.Nodes' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes.Node', 
                [], [], 
                '''                Session data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
    'SessionRedundancyAgent' : {
        'meta_info' : _MetaInfoClass('SessionRedundancyAgent',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper', 'SessionRedundancyAgent.Nodes', 
                [], [], 
                '''                List of nodes for which session data is
                collected
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-serg-oper', False),
            ],
            'Cisco-IOS-XR-infra-serg-oper',
            'session-redundancy-agent',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-serg-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_serg_oper'
        ),
    },
}
_meta_table['SessionRedundancyManager.Interfaces.Interface']['meta_info'].parent =_meta_table['SessionRedundancyManager.Interfaces']['meta_info']
_meta_table['SessionRedundancyManager.Groups.Group']['meta_info'].parent =_meta_table['SessionRedundancyManager.Groups']['meta_info']
_meta_table['SessionRedundancyManager.Interfaces']['meta_info'].parent =_meta_table['SessionRedundancyManager']['meta_info']
_meta_table['SessionRedundancyManager.Groups']['meta_info'].parent =_meta_table['SessionRedundancyManager']['meta_info']
_meta_table['SessionRedundancyManager.Summary']['meta_info'].parent =_meta_table['SessionRedundancyManager']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionDetailedInformation']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId.SessionSyncErrorInformation']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr.GroupId']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.ClientIds.ClientId']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.ClientIds']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Memory.MemoryInfo']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.Memory']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Memory.EdmMemoryInfo']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.Memory']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Memory.StringMemoryInfo']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.Memory']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.ClientSessionCount']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId.Interface']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds.GroupId']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceOper']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.InterfaceStatus']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface.ClientStatus']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.IntfStatusStatistics']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListStatistics']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.ClientStatus']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.OpaqueMemoryStatus']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal.TxListOverTcpStatus']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupSummaries.GroupSummary']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node.GroupSummaries']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIdXr']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.ClientIds']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Memory']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupIds']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.StatsGlobal']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node.GroupSummaries']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes.Node']['meta_info'].parent =_meta_table['SessionRedundancyAgent.Nodes']['meta_info']
_meta_table['SessionRedundancyAgent.Nodes']['meta_info'].parent =_meta_table['SessionRedundancyAgent']['meta_info']
