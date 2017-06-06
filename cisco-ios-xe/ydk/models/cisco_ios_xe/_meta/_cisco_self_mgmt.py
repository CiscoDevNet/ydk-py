


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NetconfYang.CiscoIa.SnmpTrapControl.TrapList' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.SnmpTrapControl.TrapList',
            False, 
            [
            _MetaInfoClassMember('trap-oid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This leaf contains the OID for the 
                SNMP trap to be forwarded.
                ''',
                'trap_oid',
                'cisco-ia', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This leaf contains the name of the SNMP trap to be 
                forwarded.
                ''',
                'description',
                'cisco-ia', False),
            _MetaInfoClassMember('forward', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf enables or disables forwarding for this
                SNMP trap.
                ''',
                'forward',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'trap-list',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.SnmpTrapControl' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.SnmpTrapControl',
            False, 
            [
            _MetaInfoClassMember('global-forwarding', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf enables or disables forwarding
                for all SNMP traps.
                ''',
                'global_forwarding',
                'cisco-ia', False),
            _MetaInfoClassMember('trap-list', REFERENCE_LIST, 'TrapList' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.SnmpTrapControl.TrapList', 
                [], [], 
                '''                This list describes SNMP Traps that are 
                supported for automatic translation to NetConf
                notifications.
                ''',
                'trap_list',
                'cisco-ia', False, max_elements=10),
            ],
            'cisco-ia',
            'snmp-trap-control',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.PreserveNedPath' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.PreserveNedPath',
            False, 
            [
            _MetaInfoClassMember('xpath', ATTRIBUTE, 'str' , None, None, 
                [(1, 1024)], [], 
                '''                An XPath from the NED model.
                ''',
                'xpath',
                'cisco-ia', True),
            ],
            'cisco-ia',
            'preserve-ned-path',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.ParserMsgIgnore' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.ParserMsgIgnore',
            False, 
            [
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                A regular expression to match parser
                output to be ignored
                ''',
                'message',
                'cisco-ia', True),
            ],
            'cisco-ia',
            'parser-msg-ignore',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.ConfParserMsgIgnore' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.ConfParserMsgIgnore',
            False, 
            [
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                A regular expression to match parser
                output to be ignored
                ''',
                'message',
                'cisco-ia', True),
            ],
            'cisco-ia',
            'conf-parser-msg-ignore',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.FullSyncCli' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.FullSyncCli',
            False, 
            [
            _MetaInfoClassMember('command', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                A regular expression matching command
                lines which cause other automatic
                configuration changes
                ''',
                'command',
                'cisco-ia', True),
            ],
            'cisco-ia',
            'full-sync-cli',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.ConfFullSyncCli' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.ConfFullSyncCli',
            False, 
            [
            _MetaInfoClassMember('command', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                A regular expression matching command
                lines which cause other automatic
                configuration changes
                ''',
                'command',
                'cisco-ia', True),
            ],
            'cisco-ia',
            'conf-full-sync-cli',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.Logging' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.Logging',
            False, 
            [
            _MetaInfoClassMember('ciaauthd-log-level', REFERENCE_ENUM_CLASS, 'CiaLogLevelEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevelEnum', 
                [], [], 
                '''                Logging level for CiaAuthDaemon
                ''',
                'ciaauthd_log_level',
                'cisco-ia', False),
            _MetaInfoClassMember('confd-log-level', REFERENCE_ENUM_CLASS, 'SyslogSeverityEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'SyslogSeverityEnum', 
                [], [], 
                '''                Logging level for Confd
                ''',
                'confd_log_level',
                'cisco-ia', False),
            _MetaInfoClassMember('nes-log-level', REFERENCE_ENUM_CLASS, 'CiaLogLevelEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevelEnum', 
                [], [], 
                '''                Logging level for Network Element Synchronizer
                ''',
                'nes_log_level',
                'cisco-ia', False),
            _MetaInfoClassMember('odm-log-level', REFERENCE_ENUM_CLASS, 'CiaLogLevelEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevelEnum', 
                [], [], 
                '''                Logging level for 
                Operational Data Manager
                ''',
                'odm_log_level',
                'cisco-ia', False),
            _MetaInfoClassMember('onep-log-level', REFERENCE_ENUM_CLASS, 'OnepLogLevelEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'OnepLogLevelEnum', 
                [], [], 
                '''                Logging level for ONEP
                ''',
                'onep_log_level',
                'cisco-ia', False),
            _MetaInfoClassMember('sync-log-level', REFERENCE_ENUM_CLASS, 'CiaLogLevelEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'CiaLogLevelEnum', 
                [], [], 
                '''                Logging level for Sync-From Daemon
                ''',
                'sync_log_level',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'logging',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.Blocking.NetworkElementCommand' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.Blocking.NetworkElementCommand',
            False, 
            [
            _MetaInfoClassMember('command', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                A regular expression matching command
                lines which should be blocked from
                entry via console/vty
                ''',
                'command',
                'cisco-ia', True),
            ],
            'cisco-ia',
            'network-element-command',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.Blocking.ConfdCfgCommand' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.Blocking.ConfdCfgCommand',
            False, 
            [
            _MetaInfoClassMember('command', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A regular expression matching command
                lines which should be blocked from
                being sent to Confd from the network
                element
                ''',
                'command',
                'cisco-ia', True),
            ],
            'cisco-ia',
            'confd-cfg-command',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa.Blocking' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa.Blocking',
            False, 
            [
            _MetaInfoClassMember('cli-blocking-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables blocking of designated command lines via the 
                network element's CLI
                ''',
                'cli_blocking_enabled',
                'cisco-ia', False),
            _MetaInfoClassMember('confd-cfg-blocking-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables blocking of designated command lines via the 
                network element's CLI
                ''',
                'confd_cfg_blocking_enabled',
                'cisco-ia', False),
            _MetaInfoClassMember('confd-cfg-command', REFERENCE_LIST, 'ConfdCfgCommand' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.Blocking.ConfdCfgCommand', 
                [], [], 
                '''                Command line pattern to omit syncing to Confd CDB
                ''',
                'confd_cfg_command',
                'cisco-ia', False, max_elements=50),
            _MetaInfoClassMember('network-element-command', REFERENCE_LIST, 'NetworkElementCommand' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.Blocking.NetworkElementCommand', 
                [], [], 
                '''                Command line pattern to disallow via the
                network element's CLI
                ''',
                'network_element_command',
                'cisco-ia', False, max_elements=30),
            ],
            'cisco-ia',
            'blocking',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoIa' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoIa',
            False, 
            [
            _MetaInfoClassMember('auto-sync', REFERENCE_ENUM_CLASS, 'CiaSyncTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'CiaSyncTypeEnum', 
                [], [], 
                '''                Enables automatic synchronization of the network element's
                running configuration with the DMI database.
                ''',
                'auto_sync',
                'cisco-ia', False),
            _MetaInfoClassMember('blocking', REFERENCE_CLASS, 'Blocking' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.Blocking', 
                [], [], 
                '''                Controls blocking of command lines, either 
                from the NE to Confd or disallowing
                manual input from the console/vty
                ''',
                'blocking',
                'cisco-ia', False),
            _MetaInfoClassMember('conf-full-sync-cli', REFERENCE_LIST, 'ConfFullSyncCli' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.ConfFullSyncCli', 
                [], [], 
                '''                A user-configurable list of IOS commands 
                that result in other automatic configurations 
                being applied for which a complete sync 
                is required
                ''',
                'conf_full_sync_cli',
                'cisco-ia', False, max_elements=50),
            _MetaInfoClassMember('conf-parser-msg-ignore', REFERENCE_LIST, 'ConfParserMsgIgnore' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.ConfParserMsgIgnore', 
                [], [], 
                '''                Parser output from configuration 
                change that is informational only,
                not an error
                ''',
                'conf_parser_msg_ignore',
                'cisco-ia', False, max_elements=50),
            _MetaInfoClassMember('config-change-delay', ATTRIBUTE, 'int' , None, None, 
                [('-32768', '32767')], [], 
                '''                Delay in ms before applying CDB change to NE
                ''',
                'config_change_delay',
                'cisco-ia', False),
            _MetaInfoClassMember('full-sync-cli', REFERENCE_LIST, 'FullSyncCli' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.FullSyncCli', 
                [], [], 
                '''                IOS commands that result in other
                automatic configurations being applied
                for which a complete sync is required
                ''',
                'full_sync_cli',
                'cisco-ia', False, max_elements=200),
            _MetaInfoClassMember('init-sync', REFERENCE_ENUM_CLASS, 'CiaSyncTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_ia', 'CiaSyncTypeEnum', 
                [], [], 
                '''                Enables synchronization of the network element's
                running configuration with the DMI database when
                DMI initializes.
                ''',
                'init_sync',
                'cisco-ia', False),
            _MetaInfoClassMember('intelligent-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled, intelligent-sync monitors all 
                ttys for configuration changes and replays 
                these changes to the DMI database once the
                tty exits configuration mode.  When 
                disabled, the complete running-configuration
                is used to synchronize the DMI database
                whenever a CLI configuration change is 
                detected
                ''',
                'intelligent_sync',
                'cisco-ia', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.Logging', 
                [], [], 
                '''                Controls logging behavior of DMI applications
                ''',
                'logging',
                'cisco-ia', False),
            _MetaInfoClassMember('max-diag-messages-saved', ATTRIBUTE, 'int' , None, None, 
                [('0', '199')], [], 
                '''                The maximum number of messages whose diagnostic data 
                in kept in persistent storage.
                ''',
                'max_diag_messages_saved',
                'cisco-ia', False),
            _MetaInfoClassMember('message-diag-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '3')], [], 
                '''                0 = Disabled, 
                1 = Save input message, DMI debugs, and response, 
                2 = Level 1 + Save "before" and "after" 
                    running-config,
                3 = Level 2 + rollback file and configuration diff
                ''',
                'message_diag_level',
                'cisco-ia', False),
            _MetaInfoClassMember('nes-ttynum', ATTRIBUTE, 'int' , None, None, 
                [('-32768', '32767')], [], 
                '''                TTY number used by NetworkElementSynchronizer
                ''',
                'nes_ttynum',
                'cisco-ia', False),
            _MetaInfoClassMember('parser-msg-ignore', REFERENCE_LIST, 'ParserMsgIgnore' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.ParserMsgIgnore', 
                [], [], 
                '''                Parser output from configuration 
                change that is informational only,
                not an error. This is a read only
                list containing known informational 
                messages
                ''',
                'parser_msg_ignore',
                'cisco-ia', False, max_elements=200),
            _MetaInfoClassMember('post-sync-acl-process', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Run "show ip access-list" and send to ConfD
                ''',
                'post_sync_acl_process',
                'cisco-ia', False),
            _MetaInfoClassMember('preserve-ned-path', REFERENCE_LIST, 'PreserveNedPath' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.PreserveNedPath', 
                [], [], 
                '''                Model paths from the NED model to preserve
                upon a sync from the network element.
                These paths are not cleared from the 
                running data store prior to the sync.
                These are expressed as nodes separated by 
                slash '/', e.g.  /native/ip/access-list
                ''',
                'preserve_ned_path',
                'cisco-ia', False, max_elements=50),
            _MetaInfoClassMember('preserve-paths-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preserve specified model paths in the NED model
                when performing a sync from the 
                network element.
                ''',
                'preserve_paths_enabled',
                'cisco-ia', False),
            _MetaInfoClassMember('process-missing-prc', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Process any parser output from configuration changes
                as a possible error.
                ''',
                'process_missing_prc',
                'cisco-ia', False),
            _MetaInfoClassMember('restored', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if CDB restored from NES running-config
                ''',
                'restored',
                'cisco-ia', False),
            _MetaInfoClassMember('snmp-community-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The community string for communication with the SNMP 
                       agent
                ''',
                'snmp_community_string',
                'cisco-ia', False),
            _MetaInfoClassMember('snmp-trap-control', REFERENCE_CLASS, 'SnmpTrapControl' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa.SnmpTrapControl', 
                [], [], 
                '''                This container describes the configuration parameters
                for SNMP Trap to NetConf notification processing.
                ''',
                'snmp_trap_control',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'cisco-ia',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoOdm.Actions.ModeEnum' : _MetaInfoEnum('ModeEnum', 'ydk.models.cisco_ios_xe.cisco_self_mgmt',
        {
            'poll':'poll',
            'on-demand':'on_demand',
            'none':'none',
        }, 'cisco-odm', _yang_ns._namespaces['cisco-odm']),
    'NetconfYang.CiscoOdm.Actions' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoOdm.Actions',
            False, 
            [
            _MetaInfoClassMember('action-name', REFERENCE_IDENTITY_CLASS, 'ParsernameIdentity' , 'ydk.models.cisco_ios_xe.cisco_odm', 'ParsernameIdentity', 
                [], [], 
                '''                ''',
                'action_name',
                'cisco-odm', True),
            _MetaInfoClassMember('cdb-xpath', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'cdb_xpath',
                'cisco-odm', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'ModeEnum' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoOdm.Actions.ModeEnum', 
                [], [], 
                '''                ''',
                'mode',
                'cisco-odm', False),
            _MetaInfoClassMember('polling-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'polling_interval',
                'cisco-odm', False),
            ],
            'cisco-odm',
            'actions',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang.CiscoOdm' : {
        'meta_info' : _MetaInfoClass('NetconfYang.CiscoOdm',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_LIST, 'Actions' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoOdm.Actions', 
                [], [], 
                '''                ''',
                'actions',
                'cisco-odm', False),
            _MetaInfoClassMember('on-demand-default-time', ATTRIBUTE, 'int' , None, None, 
                [('500', '4294967295')], [], 
                '''                ''',
                'on_demand_default_time',
                'cisco-odm', False),
            _MetaInfoClassMember('on-demand-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ''',
                'on_demand_enable',
                'cisco-odm', False),
            _MetaInfoClassMember('polling-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ''',
                'polling_enable',
                'cisco-odm', False),
            ],
            'cisco-odm',
            'cisco-odm',
            _yang_ns._namespaces['cisco-odm'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
    'NetconfYang' : {
        'meta_info' : _MetaInfoClass('NetconfYang',
            False, 
            [
            _MetaInfoClassMember('cisco-ia', REFERENCE_CLASS, 'CiscoIa' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoIa', 
                [], [], 
                '''                Customize the behavior of the DMI applications
                ''',
                'cisco_ia',
                'cisco-ia', False),
            _MetaInfoClassMember('cisco-odm', REFERENCE_CLASS, 'CiscoOdm' , 'ydk.models.cisco_ios_xe.cisco_self_mgmt', 'NetconfYang.CiscoOdm', 
                [], [], 
                '''                ''',
                'cisco_odm',
                'cisco-odm', False),
            ],
            'cisco-self-mgmt',
            'netconf-yang',
            _yang_ns._namespaces['cisco-self-mgmt'],
        'ydk.models.cisco_ios_xe.cisco_self_mgmt'
        ),
    },
}
_meta_table['NetconfYang.CiscoIa.SnmpTrapControl.TrapList']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa.SnmpTrapControl']['meta_info']
_meta_table['NetconfYang.CiscoIa.Blocking.NetworkElementCommand']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa.Blocking']['meta_info']
_meta_table['NetconfYang.CiscoIa.Blocking.ConfdCfgCommand']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa.Blocking']['meta_info']
_meta_table['NetconfYang.CiscoIa.SnmpTrapControl']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoIa.PreserveNedPath']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoIa.ParserMsgIgnore']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoIa.ConfParserMsgIgnore']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoIa.FullSyncCli']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoIa.ConfFullSyncCli']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoIa.Logging']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoIa.Blocking']['meta_info'].parent =_meta_table['NetconfYang.CiscoIa']['meta_info']
_meta_table['NetconfYang.CiscoOdm.Actions']['meta_info'].parent =_meta_table['NetconfYang.CiscoOdm']['meta_info']
_meta_table['NetconfYang.CiscoIa']['meta_info'].parent =_meta_table['NetconfYang']['meta_info']
_meta_table['NetconfYang.CiscoOdm']['meta_info'].parent =_meta_table['NetconfYang']['meta_info']
