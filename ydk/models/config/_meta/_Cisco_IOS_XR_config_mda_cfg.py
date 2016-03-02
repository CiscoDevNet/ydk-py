


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold',
            False, 
            [
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int' , None, None, 
                [(3, 40)], [], 
                '''                Threshold, Range(3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [(5, 40)], [], 
                '''                Threshold, Range(5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [(4, 40)], [], 
                '''                Threshold, Range(4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'memory-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-watchd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold',
            False, 
            [
            _MetaInfoClassMember('memory-threshold', REFERENCE_CLASS, 'MemoryThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold', 
                [], [], 
                '''                Memory thresholds
                ''',
                'memory_threshold',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-watchd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold',
            False, 
            [
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int' , None, None, 
                [(3, 40)], [], 
                '''                Threshold, Range(3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [(5, 40)], [], 
                '''                Threshold, Range(5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [(4, 40)], [], 
                '''                Threshold, Range(4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-wd-cfg', False),
            ],
            'Cisco-IOS-XR-wd-cfg',
            'memory-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold',
            False, 
            [
            _MetaInfoClassMember('memory-threshold', REFERENCE_CLASS, 'MemoryThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold', 
                [], [], 
                '''                Memory thresholds
                ''',
                'memory_threshold',
                'Cisco-IOS-XR-wd-cfg', False),
            ],
            'Cisco-IOS-XR-wd-cfg',
            'Cisco-IOS-XR-wd-cfg_watchdog-node-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences',
            False, 
            [
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Precedence values
                ''',
                'precedence',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'LptsPreIFibPrecedenceNumber_Enum' , 'ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber_Enum', 
                        [], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [(0, 7)], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'precedences',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow',
            False, 
            [
            _MetaInfoClassMember('flow-type', REFERENCE_ENUM_CLASS, 'LptsFlow_Enum' , 'ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow_Enum', 
                [], [], 
                '''                LPTS Flow Type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('precedences', REFERENCE_CLASS, 'Precedences' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences', 
                [], [], 
                '''                TOS Precedence value(s)
                ''',
                'precedences',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flow',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows',
            False, 
            [
            _MetaInfoClassMember('flow', REFERENCE_LIST, 'Flow' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow', 
                [], [], 
                '''                selected flow type
                ''',
                'flow',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flows',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled
                ''',
                'enable',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('flows', REFERENCE_CLASS, 'Flows' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows', 
                [], [], 
                '''                Table for Flows
                ''',
                'flows',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer-local',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                none
                ''',
                'id1',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Packets per second
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'np',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps',
            False, 
            [
            _MetaInfoClassMember('np', REFERENCE_LIST, 'Np' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np', 
                [], [], 
                '''                Table of NP names
                ''',
                'np',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'nps',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                none
                ''',
                'id1',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('nps', REFERENCE_CLASS, 'Nps' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps', 
                [], [], 
                '''                NP name
                ''',
                'nps',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer-local-table',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables',
            False, 
            [
            _MetaInfoClassMember('ipolicer-local-table', REFERENCE_LIST, 'IpolicerLocalTable' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable', 
                [], [], 
                '''                Pre IFIB (Internal Forwarding Information
                Base) configuration table
                ''',
                'ipolicer_local_table',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer-local-tables',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode.LptsLocal' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode.LptsLocal',
            False, 
            [
            _MetaInfoClassMember('ipolicer-local', REFERENCE_CLASS, 'IpolicerLocal' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal', 
                [], [], 
                '''                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                ''',
                'ipolicer_local',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('ipolicer-local-tables', REFERENCE_CLASS, 'IpolicerLocalTables' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables', 
                [], [], 
                '''                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                ''',
                'ipolicer_local_tables',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'lpts-local',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes.ActiveNode' : {
        'meta_info' : _MetaInfoClass('ActiveNodes.ActiveNode',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The identifier for this node
                ''',
                'node_name',
                'Cisco-IOS-XR-config-mda-cfg', True),
            _MetaInfoClassMember('Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold', REFERENCE_CLASS, 'CiscoIOSXRWatchdCfg_watchdogNodeThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold', 
                [], [], 
                '''                watchdog node threshold
                ''',
                'cisco_ios_xr_watchd_cfg_watchdog_node_threshold',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('Cisco-IOS-XR-wd-cfg_watchdog-node-threshold', REFERENCE_CLASS, 'CiscoIOSXRWdCfg_watchdogNodeThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold', 
                [], [], 
                '''                Watchdog threshold configuration
                ''',
                'cisco_ios_xr_wd_cfg_watchdog_node_threshold',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('lpts-local', REFERENCE_CLASS, 'LptsLocal' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode.LptsLocal', 
                [], [], 
                '''                lpts node specific configuration commands
                ''',
                'lpts_local',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-config-mda-cfg',
            'active-node',
            _yang_ns._namespaces['Cisco-IOS-XR-config-mda-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'ActiveNodes' : {
        'meta_info' : _MetaInfoClass('ActiveNodes',
            False, 
            [
            _MetaInfoClassMember('active-node', REFERENCE_LIST, 'ActiveNode' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'ActiveNodes.ActiveNode', 
                [], [], 
                '''                The configuration for an active node
                ''',
                'active_node',
                'Cisco-IOS-XR-config-mda-cfg', False),
            ],
            'Cisco-IOS-XR-config-mda-cfg',
            'active-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-config-mda-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold',
            False, 
            [
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int' , None, None, 
                [(3, 40)], [], 
                '''                Threshold, Range(3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [(5, 40)], [], 
                '''                Threshold, Range(5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [(4, 40)], [], 
                '''                Threshold, Range(4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'memory-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-watchd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold',
            False, 
            [
            _MetaInfoClassMember('memory-threshold', REFERENCE_CLASS, 'MemoryThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold', 
                [], [], 
                '''                Memory thresholds
                ''',
                'memory_threshold',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-watchd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold',
            False, 
            [
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int' , None, None, 
                [(3, 40)], [], 
                '''                Threshold, Range(3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [(5, 40)], [], 
                '''                Threshold, Range(5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [(4, 40)], [], 
                '''                Threshold, Range(4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-wd-cfg', False),
            ],
            'Cisco-IOS-XR-wd-cfg',
            'memory-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold',
            False, 
            [
            _MetaInfoClassMember('memory-threshold', REFERENCE_CLASS, 'MemoryThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold', 
                [], [], 
                '''                Memory thresholds
                ''',
                'memory_threshold',
                'Cisco-IOS-XR-wd-cfg', False),
            ],
            'Cisco-IOS-XR-wd-cfg',
            'Cisco-IOS-XR-wd-cfg_watchdog-node-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences',
            False, 
            [
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Precedence values
                ''',
                'precedence',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'LptsPreIFibPrecedenceNumber_Enum' , 'ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumber_Enum', 
                        [], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [(0, 7)], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'precedences',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow',
            False, 
            [
            _MetaInfoClassMember('flow-type', REFERENCE_ENUM_CLASS, 'LptsFlow_Enum' , 'ydk.models.lpts.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlow_Enum', 
                [], [], 
                '''                LPTS Flow Type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('precedences', REFERENCE_CLASS, 'Precedences' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences', 
                [], [], 
                '''                TOS Precedence value(s)
                ''',
                'precedences',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flow',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows',
            False, 
            [
            _MetaInfoClassMember('flow', REFERENCE_LIST, 'Flow' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow', 
                [], [], 
                '''                selected flow type
                ''',
                'flow',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flows',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled
                ''',
                'enable',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('flows', REFERENCE_CLASS, 'Flows' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows', 
                [], [], 
                '''                Table for Flows
                ''',
                'flows',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer-local',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                none
                ''',
                'id1',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Packets per second
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'np',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps',
            False, 
            [
            _MetaInfoClassMember('np', REFERENCE_LIST, 'Np' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np', 
                [], [], 
                '''                Table of NP names
                ''',
                'np',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'nps',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable',
            False, 
            [
            _MetaInfoClassMember('id1', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                none
                ''',
                'id1',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('nps', REFERENCE_CLASS, 'Nps' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps', 
                [], [], 
                '''                NP name
                ''',
                'nps',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer-local-table',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables',
            False, 
            [
            _MetaInfoClassMember('ipolicer-local-table', REFERENCE_LIST, 'IpolicerLocalTable' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable', 
                [], [], 
                '''                Pre IFIB (Internal Forwarding Information
                Base) configuration table
                ''',
                'ipolicer_local_table',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer-local-tables',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode.LptsLocal' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode.LptsLocal',
            False, 
            [
            _MetaInfoClassMember('ipolicer-local', REFERENCE_CLASS, 'IpolicerLocal' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal', 
                [], [], 
                '''                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                ''',
                'ipolicer_local',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('ipolicer-local-tables', REFERENCE_CLASS, 'IpolicerLocalTables' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables', 
                [], [], 
                '''                Node specific Pre IFIB (Internal Forwarding
                Information Base) Configuration
                ''',
                'ipolicer_local_tables',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'lpts-local',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes.PreconfiguredNode' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes.PreconfiguredNode',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The identifier for this node
                ''',
                'node_name',
                'Cisco-IOS-XR-config-mda-cfg', True),
            _MetaInfoClassMember('Cisco-IOS-XR-watchd-cfg_watchdog-node-threshold', REFERENCE_CLASS, 'CiscoIOSXRWatchdCfg_watchdogNodeThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold', 
                [], [], 
                '''                watchdog node threshold
                ''',
                'cisco_ios_xr_watchd_cfg_watchdog_node_threshold',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('Cisco-IOS-XR-wd-cfg_watchdog-node-threshold', REFERENCE_CLASS, 'CiscoIOSXRWdCfg_watchdogNodeThreshold' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold', 
                [], [], 
                '''                Watchdog threshold configuration
                ''',
                'cisco_ios_xr_wd_cfg_watchdog_node_threshold',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('lpts-local', REFERENCE_CLASS, 'LptsLocal' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode.LptsLocal', 
                [], [], 
                '''                lpts node specific configuration commands
                ''',
                'lpts_local',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-config-mda-cfg',
            'preconfigured-node',
            _yang_ns._namespaces['Cisco-IOS-XR-config-mda-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
    'PreconfiguredNodes' : {
        'meta_info' : _MetaInfoClass('PreconfiguredNodes',
            False, 
            [
            _MetaInfoClassMember('preconfigured-node', REFERENCE_LIST, 'PreconfiguredNode' , 'ydk.models.config.Cisco_IOS_XR_config_mda_cfg', 'PreconfiguredNodes.PreconfiguredNode', 
                [], [], 
                '''                The configuration for a non-active node
                ''',
                'preconfigured_node',
                'Cisco-IOS-XR-config-mda-cfg', False),
            ],
            'Cisco-IOS-XR-config-mda-cfg',
            'preconfigured-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-config-mda-cfg'],
        'ydk.models.config.Cisco_IOS_XR_config_mda_cfg'
        ),
    },
}
_meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold']['meta_info']
_meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal.Flows']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocal']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal.IpolicerLocalTables']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode.LptsLocal']['meta_info']
_meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode']['meta_info']
_meta_table['ActiveNodes.ActiveNode.CiscoIOSXRWdCfg_watchdogNodeThreshold']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode']['meta_info']
_meta_table['ActiveNodes.ActiveNode.LptsLocal']['meta_info'].parent =_meta_table['ActiveNodes.ActiveNode']['meta_info']
_meta_table['ActiveNodes.ActiveNode']['meta_info'].parent =_meta_table['ActiveNodes']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold.MemoryThreshold']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow.Precedences']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows.Flow']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal.Flows']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps.Np']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable.Nps']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables.IpolicerLocalTable']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocal']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal.IpolicerLocalTables']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWatchdCfg_watchdogNodeThreshold']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.CiscoIOSXRWdCfg_watchdogNodeThreshold']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode.LptsLocal']['meta_info'].parent =_meta_table['PreconfiguredNodes.PreconfiguredNode']['meta_info']
_meta_table['PreconfiguredNodes.PreconfiguredNode']['meta_info'].parent =_meta_table['PreconfiguredNodes']['meta_info']
