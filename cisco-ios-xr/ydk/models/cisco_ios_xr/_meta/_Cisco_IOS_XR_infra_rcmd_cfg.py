


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RcmdPriorityEnum' : _MetaInfoEnum('RcmdPriorityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        {
            'critical':'critical',
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'Cisco-IOS-XR-infra-rcmd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg']),
    'ProtocolNameEnum' : _MetaInfoEnum('ProtocolNameEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg',
        {
            'ospf':'ospf',
            'isis':'isis',
        }, 'Cisco-IOS-XR-infra-rcmd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg']),
    'RouterConvergence.Protocols.Protocol.Priorities.Priority' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols.Protocol.Priorities.Priority',
            False, 
            [
            _MetaInfoClassMember('rcmd-priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RcmdPriorityEnum', 
                [], [], 
                '''                Specify the priority
                ''',
                'rcmd_priority',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disables the monitoring of route convergence
                for specified priority
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Priority. Deletion of this object
                also causes deletion of all associated
                objects under Priority.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('frr-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value for Fast ReRoute Coverage
                (in percentage)
                ''',
                'frr_threshold',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('leaf-networks', ATTRIBUTE, 'int' , None, None, 
                [('10', '100')], [], 
                '''                Specify the maximum number of leaf networks
                monitored
                ''',
                'leaf_networks',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value for convergence (in msec)
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.Protocols.Protocol.Priorities' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols.Protocol.Priorities',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols.Protocol.Priorities.Priority', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'priorities',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.Protocols.Protocol' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols.Protocol',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'ProtocolNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'ProtocolNameEnum', 
                [], [], 
                '''                Specify the protocol
                ''',
                'protocol_name',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Protocol for which to configure RCMD
                parameters. Deletion of this object also
                causes deletion of all associated objects
                under Protocol.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('priorities', REFERENCE_CLASS, 'Priorities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols.Protocol.Priorities', 
                [], [], 
                '''                Table of Priority
                ''',
                'priorities',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.Protocols' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Protocols',
            False, 
            [
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols.Protocol', 
                [], [], 
                '''                Protocol for which to configure RCMD parameters
                ''',
                'protocol',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'protocols',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.StorageLocation' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.StorageLocation',
            False, 
            [
            _MetaInfoClassMember('diagnostics', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Absolute directory path for storing diagnostic
                reports. Example /disk0:/rcmd/ or
                <tftp-location>/rcmd/
                ''',
                'diagnostics',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('diagnostics-size', ATTRIBUTE, 'int' , None, None, 
                [('5', '80')], [], 
                '''                Maximum size of diagnostics dir (5% - 80%) for
                local storage.
                ''',
                'diagnostics_size',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('reports', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Absolute directory path for storing reports.
                Example /disk0:/rcmd/ or <tftp-location>/rcmd/
                ''',
                'reports',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('reports-size', ATTRIBUTE, 'int' , None, None, 
                [('5', '80')], [], 
                '''                Maximum size of reports dir (5% - 80%) for
                local storage.
                ''',
                'reports_size',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'storage-location',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.MplsLdp.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.MplsLdp.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value for label coverage (in
                percentage)
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.MplsLdp' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.MplsLdp',
            False, 
            [
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.MplsLdp.RemoteLfa', 
                [], [], 
                '''                Monitoring configuration for Remote LFA
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'mpls-ldp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.CollectDiagnostics.CollectDiagnostic' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.CollectDiagnostics.CollectDiagnostic',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Specified location
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enables collection of diagnostics on the
                specified location
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'collect-diagnostic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.CollectDiagnostics' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.CollectDiagnostics',
            False, 
            [
            _MetaInfoClassMember('collect-diagnostic', REFERENCE_LIST, 'CollectDiagnostic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.CollectDiagnostics.CollectDiagnostic', 
                [], [], 
                '''                Collect diagnostics on specified node
                ''',
                'collect_diagnostic',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'collect-diagnostics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'((([a-zA-Z0-9_]*\\d+)|(\\*))/){2}(([a-zA-Z0-9_]*\\d+)|(\\*))'], 
                '''                Wildcard expression(eg. */*/*, R/*/*, R/S/*,
                R/S/I)
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-cfg', True),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disables the monitoring of route convergence
                on specified location
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Configure parameters for the specified
                node (Partially qualified location allowed).
                Deletion of this object also causes deletion
                of all associated objects under Node.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence.Nodes' : {
        'meta_info' : _MetaInfoClass('RouterConvergence.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Nodes.Node', 
                [], [], 
                '''                Configure parameters for the specified node
                (Partially qualified location allowed)
                ''',
                'node',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
    'RouterConvergence' : {
        'meta_info' : _MetaInfoClass('RouterConvergence',
            False, 
            [
            _MetaInfoClassMember('collect-diagnostics', REFERENCE_CLASS, 'CollectDiagnostics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.CollectDiagnostics', 
                [], [], 
                '''                Table of CollectDiagnostics
                ''',
                'collect_diagnostics',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable the monitoring of route convergence on
                the entire router
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Configure Router Convergence Monitoring.
                Deletion of this object also causes deletion of
                all associated objects under RouterConvergence.
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('event-buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('100', '500')], [], 
                '''                Event buffer size for storing event traces (as
                number of events)
                ''',
                'event_buffer_size',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('max-events-stored', ATTRIBUTE, 'int' , None, None, 
                [('10', '500')], [], 
                '''                Maximum number of events stored in the server
                ''',
                'max_events_stored',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('monitoring-interval', ATTRIBUTE, 'int' , None, None, 
                [('5', '120')], [], 
                '''                Interval in which to collect logs (in mins)
                ''',
                'monitoring_interval',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.MplsLdp', 
                [], [], 
                '''                RCMD related configuration for MPLS-LDP
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Nodes', 
                [], [], 
                '''                Table of Node
                ''',
                'nodes',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('prefix-monitor-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Limits Individual Prefix Monitoring
                ''',
                'prefix_monitor_limit',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('protocols', REFERENCE_CLASS, 'Protocols' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.Protocols', 
                [], [], 
                '''                Table of Protocol
                ''',
                'protocols',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            _MetaInfoClassMember('storage-location', REFERENCE_CLASS, 'StorageLocation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg', 'RouterConvergence.StorageLocation', 
                [], [], 
                '''                Absolute directory path for saving the archive
                files. Example /disk0:/rcmd/ or
                <tftp-location>/rcmd/
                ''',
                'storage_location',
                'Cisco-IOS-XR-infra-rcmd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-cfg',
            'router-convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_cfg'
        ),
    },
}
_meta_table['RouterConvergence.Protocols.Protocol.Priorities.Priority']['meta_info'].parent =_meta_table['RouterConvergence.Protocols.Protocol.Priorities']['meta_info']
_meta_table['RouterConvergence.Protocols.Protocol.Priorities']['meta_info'].parent =_meta_table['RouterConvergence.Protocols.Protocol']['meta_info']
_meta_table['RouterConvergence.Protocols.Protocol']['meta_info'].parent =_meta_table['RouterConvergence.Protocols']['meta_info']
_meta_table['RouterConvergence.MplsLdp.RemoteLfa']['meta_info'].parent =_meta_table['RouterConvergence.MplsLdp']['meta_info']
_meta_table['RouterConvergence.CollectDiagnostics.CollectDiagnostic']['meta_info'].parent =_meta_table['RouterConvergence.CollectDiagnostics']['meta_info']
_meta_table['RouterConvergence.Nodes.Node']['meta_info'].parent =_meta_table['RouterConvergence.Nodes']['meta_info']
_meta_table['RouterConvergence.Protocols']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.StorageLocation']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.MplsLdp']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.CollectDiagnostics']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
_meta_table['RouterConvergence.Nodes']['meta_info'].parent =_meta_table['RouterConvergence']['meta_info']
