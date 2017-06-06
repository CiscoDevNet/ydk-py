


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IssuNodeRoleEtEnum' : _MetaInfoEnum('IssuNodeRoleEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper',
        {
            'unknown-role':'unknown_role',
            'primary-role':'primary_role',
            'secondary-role':'secondary_role',
            'tertiary-role':'tertiary_role',
        }, 'Cisco-IOS-XR-spirit-install-instmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper']),
    'IsdIssuStatusEtEnum' : _MetaInfoEnum('IsdIssuStatusEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper',
        {
            'ok':'ok',
            'prep-done':'prep_done',
            'big-bang':'big_bang',
            'done':'done',
            'abort':'abort',
            'cmd-reject':'cmd_reject',
            'unknown':'unknown',
            'abort-cleanup':'abort_cleanup',
            'abort-cmd-reject':'abort_cmd_reject',
        }, 'Cisco-IOS-XR-spirit-install-instmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper']),
    'IsdErrorEtEnum' : _MetaInfoEnum('IsdErrorEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper',
        {
            'none':'none',
            'not-compatible':'not_compatible',
            'not-enough-resource':'not_enough_resource',
            'not-nsr-ready':'not_nsr_ready',
            'not-conn-sdrsm':'not_conn_sdrsm',
            'cmd-invalid':'cmd_invalid',
            'load-prep-fail':'load_prep_fail',
            'error-timeout':'error_timeout',
            'err-node-down':'err_node_down',
            'node-not-ready':'node_not_ready',
            'err-node-new':'err_node_new',
            'err-card-oir':'err_card_oir',
            'invalid-evt':'invalid_evt',
            'disconn-from-calv':'disconn_from_calv',
            'gsp-down':'gsp_down',
            'abort-by-ism':'abort_by_ism',
            'rpfo':'rpfo',
            'pkg-null':'pkg_null',
            'error-general':'error_general',
            'fsa-error':'fsa_error',
            'err-post-issu':'err_post_issu',
            'err-issu-dir-restart':'err_issu_dir_restart',
        }, 'Cisco-IOS-XR-spirit-install-instmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper']),
    'NodeRoleEtEnum' : _MetaInfoEnum('NodeRoleEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper',
        {
            'node-unknown':'node_unknown',
            'node-active':'node_active',
            'node-standby':'node_standby',
            'node-unusable':'node_unusable',
        }, 'Cisco-IOS-XR-spirit-install-instmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper']),
    'IssudirNodeStatusEtEnum' : _MetaInfoEnum('IssudirNodeStatusEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper',
        {
            'not-issu-ready':'not_issu_ready',
            'issu-ready':'issu_ready',
            'isus-go':'isus_go',
            'node-fail':'node_fail',
        }, 'Cisco-IOS-XR-spirit-install-instmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper']),
    'CardTypeEtEnum' : _MetaInfoEnum('CardTypeEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper',
        {
            'card-rp':'card_rp',
            'card-drp':'card_drp',
            'card-lc':'card_lc',
            'card-sc':'card_sc',
            'card-sp':'card_sp',
            'card-other':'card_other',
        }, 'Cisco-IOS-XR-spirit-install-instmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper']),
    'IsdStateEtEnum' : _MetaInfoEnum('IsdStateEtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper',
        {
            'none':'none',
            'idle':'idle',
            'init':'init',
            'init-done':'init_done',
            'load-prep':'load_prep',
            'load-exec':'load_exec',
            'load-issu-go':'load_issu_go',
            'load-done':'load_done',
            'run-prep':'run_prep',
            'big-bang':'big_bang',
            'run-done':'run_done',
            'cleanup':'cleanup',
            'cleanup-done':'cleanup_done',
            'abort':'abort',
            'abort-done':'abort_done',
            'abort-cleanup':'abort_cleanup',
            'unknown-state':'unknown_state',
        }, 'Cisco-IOS-XR-spirit-install-instmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper']),
    'SoftwareInstall.Files.File.Brief' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Files.File.Brief',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Files.File.Detail' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Files.File.Detail',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Files.File' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Files.File',
            False, 
            [
            _MetaInfoClassMember('file-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                File name
                ''',
                'file_name',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', True),
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Files.File.Brief', 
                [], [], 
                '''                Show information about an installed file
                ''',
                'brief',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Files.File.Detail', 
                [], [], 
                '''                Show detail information about an installed
                file
                ''',
                'detail',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'file',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Files' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Files',
            False, 
            [
            _MetaInfoClassMember('file', REFERENCE_LIST, 'File' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Files.File', 
                [], [], 
                '''                Show information about an installed file
                ''',
                'file',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'files',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.LastNOperationLogs.LastNOperationLog' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.LastNOperationLogs.LastNOperationLog',
            False, 
            [
            _MetaInfoClassMember('last-n-logs', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Last N opeartion logs
                ''',
                'last_n_logs',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', True),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail', 
                [], [], 
                '''                Show detailed log file for last n operations
                ''',
                'detail',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary', 
                [], [], 
                '''                Show summary log file for last n operations
                ''',
                'summary',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'last-n-operation-log',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.LastNOperationLogs' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.LastNOperationLogs',
            False, 
            [
            _MetaInfoClassMember('last-n-operation-log', REFERENCE_LIST, 'LastNOperationLog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.LastNOperationLogs.LastNOperationLog', 
                [], [], 
                '''                Show log file of last n operations
                ''',
                'last_n_operation_log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'last-n-operation-logs',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Prepare.Rpm' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Prepare.Rpm',
            False, 
            [
            _MetaInfoClassMember('package', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                package
                ''',
                'package',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'rpm',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Prepare.Package' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Prepare.Package',
            False, 
            [
            _MetaInfoClassMember('package', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                package
                ''',
                'package',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Prepare' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Prepare',
            False, 
            [
            _MetaInfoClassMember('activate-message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ActivateMessage
                ''',
                'activate_message',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('no-prepare-done', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NoPrepareDone
                ''',
                'no_prepare_done',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Prepare.Package', 
                [], [], 
                '''                package
                ''',
                'package',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('prepare-clean-message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PrepareCleanMessage
                ''',
                'prepare_clean_message',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('prepared-boot-image', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PreparedBootImage
                ''',
                'prepared_boot_image',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('prepared-boot-partition', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PreparedBootPartition
                ''',
                'prepared_boot_partition',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('restart-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RestartType
                ''',
                'restart_type',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('rpm', REFERENCE_LIST, 'Rpm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Prepare.Rpm', 
                [], [], 
                '''                rpm
                ''',
                'rpm',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'prepare',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Active.ActivePackageInfo' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Active.ActivePackageInfo',
            False, 
            [
            _MetaInfoClassMember('active-packages', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ActivePackages
                ''',
                'active_packages',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('boot-partition-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BootPartitionName
                ''',
                'boot_partition_name',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('error-message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ErrorMessage
                ''',
                'error_message',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('node-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NodeType
                ''',
                'node_type',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('number-of-active-packages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NumberOfActivePackages
                ''',
                'number_of_active_packages',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'active-package-info',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Active' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Active',
            False, 
            [
            _MetaInfoClassMember('active-package-info', REFERENCE_LIST, 'ActivePackageInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Active.ActivePackageInfo', 
                [], [], 
                '''                active package info
                ''',
                'active_package_info',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Version' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Version',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'version',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Inactive' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Inactive',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Request' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Request',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Issu.Stage' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Issu.Stage',
            False, 
            [
            _MetaInfoClassMember('issu-error', REFERENCE_ENUM_CLASS, 'IsdErrorEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IsdErrorEtEnum', 
                [], [], 
                '''                ISSU Error
                ''',
                'issu_error',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('issu-node-cnt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISSU Node Count
                ''',
                'issu_node_cnt',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('issu-ready-node-cnt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISSU Ready Node Count
                ''',
                'issu_ready_node_cnt',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('issu-status', REFERENCE_ENUM_CLASS, 'IsdIssuStatusEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IsdIssuStatusEtEnum', 
                [], [], 
                '''                Abort Status
                ''',
                'issu_status',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Percentage
                ''',
                'percentage',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IsdStateEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IsdStateEtEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'stage',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Issu.Inventory.Invinfo' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Issu.Inventory.Invinfo',
            False, 
            [
            _MetaInfoClassMember('issu-node-role', REFERENCE_ENUM_CLASS, 'IssuNodeRoleEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IssuNodeRoleEtEnum', 
                [], [], 
                '''                ISSU Node Role
                ''',
                'issu_node_role',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Node ID
                ''',
                'node_id',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('node-role', REFERENCE_ENUM_CLASS, 'NodeRoleEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'NodeRoleEtEnum', 
                [], [], 
                '''                Node role
                ''',
                'node_role',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('node-state', REFERENCE_ENUM_CLASS, 'IssudirNodeStatusEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'IssudirNodeStatusEtEnum', 
                [], [], 
                '''                Node State
                ''',
                'node_state',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('node-type', REFERENCE_ENUM_CLASS, 'CardTypeEtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'CardTypeEtEnum', 
                [], [], 
                '''                Node Type
                ''',
                'node_type',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'invinfo',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Issu.Inventory' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Issu.Inventory',
            False, 
            [
            _MetaInfoClassMember('invinfo', REFERENCE_LIST, 'Invinfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Issu.Inventory.Invinfo', 
                [], [], 
                '''                invinfo
                ''',
                'invinfo',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Issu' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Issu',
            False, 
            [
            _MetaInfoClassMember('inventory', REFERENCE_CLASS, 'Inventory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Issu.Inventory', 
                [], [], 
                '''                Show XR install issu inventory
                ''',
                'inventory',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('stage', REFERENCE_CLASS, 'Stage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Issu.Stage', 
                [], [], 
                '''                Show XR install issu stage
                ''',
                'stage',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'issu',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Committed.CommittedPackageInfo' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Committed.CommittedPackageInfo',
            False, 
            [
            _MetaInfoClassMember('boot-partition-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BootPartitionName
                ''',
                'boot_partition_name',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('committed-packages', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CommittedPackages
                ''',
                'committed_packages',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('error-message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ErrorMessage
                ''',
                'error_message',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Location
                ''',
                'location',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('node-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NodeType
                ''',
                'node_type',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('number-of-committed-packages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NumberOfCommittedPackages
                ''',
                'number_of_committed_packages',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'committed-package-info',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Committed' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Committed',
            False, 
            [
            _MetaInfoClassMember('committed-package-info', REFERENCE_LIST, 'CommittedPackageInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Committed.CommittedPackageInfo', 
                [], [], 
                '''                committed package info
                ''',
                'committed_package_info',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'committed',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.AllOperationsLog.Summary' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.AllOperationsLog.Summary',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.AllOperationsLog.Detail' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.AllOperationsLog.Detail',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.AllOperationsLog' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.AllOperationsLog',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.AllOperationsLog.Detail', 
                [], [], 
                '''                Show detailed log file for all operations
                ''',
                'detail',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.AllOperationsLog.Summary', 
                [], [], 
                '''                Show summary log file for all operations
                ''',
                'summary',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'all-operations-log',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Packages.Package.Verbose' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Packages.Package.Verbose',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'verbose',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Packages.Package.Brief' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Packages.Package.Brief',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Packages.Package.Detail' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Packages.Package.Detail',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Packages.Package' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Packages.Package',
            False, 
            [
            _MetaInfoClassMember('package-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package name
                ''',
                'package_name',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', True),
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Packages.Package.Brief', 
                [], [], 
                '''                Show the info for a installed package
                ''',
                'brief',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Packages.Package.Detail', 
                [], [], 
                '''                Show the deatil info for a installed package
                ''',
                'detail',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('verbose', REFERENCE_CLASS, 'Verbose' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Packages.Package.Verbose', 
                [], [], 
                '''                Show the verbose info for a installed package
                ''',
                'verbose',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Packages' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Packages',
            False, 
            [
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Packages.Package', 
                [], [], 
                '''                Show the info for a installed package
                ''',
                'package',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'packages',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.OperationLogs.OperationLog.Summary' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.OperationLogs.OperationLog.Summary',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.OperationLogs.OperationLog.Detail' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.OperationLogs.OperationLog.Detail',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.OperationLogs.OperationLog' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.OperationLogs.OperationLog',
            False, 
            [
            _MetaInfoClassMember('log-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Log ID number
                ''',
                'log_id',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', True),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.OperationLogs.OperationLog.Detail', 
                [], [], 
                '''                Show detailed log file for the specified
                install ID
                ''',
                'detail',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.OperationLogs.OperationLog.Summary', 
                [], [], 
                '''                Show summary log file for the specified
                install ID
                ''',
                'summary',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'operation-log',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.OperationLogs' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.OperationLogs',
            False, 
            [
            _MetaInfoClassMember('operation-log', REFERENCE_LIST, 'OperationLog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.OperationLogs.OperationLog', 
                [], [], 
                '''                Show log file for the specified install ID
                ''',
                'operation_log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'operation-logs',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Repository.Xr' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Repository.Xr',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'xr',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Repository.All' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Repository.All',
            False, 
            [
            _MetaInfoClassMember('log', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                log
                ''',
                'log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall.Repository' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall.Repository',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Repository.All', 
                [], [], 
                '''                Show contents of all install software
                repositories
                ''',
                'all',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('xr', REFERENCE_CLASS, 'Xr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Repository.Xr', 
                [], [], 
                '''                Show install software repository for XR
                ''',
                'xr',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'repository',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
    'SoftwareInstall' : {
        'meta_info' : _MetaInfoClass('SoftwareInstall',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Active', 
                [], [], 
                '''                Show active packages installed
                ''',
                'active',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('all-operations-log', REFERENCE_CLASS, 'AllOperationsLog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.AllOperationsLog', 
                [], [], 
                '''                Show log file for all operations
                ''',
                'all_operations_log',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('committed', REFERENCE_CLASS, 'Committed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Committed', 
                [], [], 
                '''                Show Committed packages installed
                ''',
                'committed',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('files', REFERENCE_CLASS, 'Files' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Files', 
                [], [], 
                '''                Show information about an installed file
                ''',
                'files',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Inactive', 
                [], [], 
                '''                Show XR inactive packages
                ''',
                'inactive',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('issu', REFERENCE_CLASS, 'Issu' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Issu', 
                [], [], 
                '''                ISSU operation
                ''',
                'issu',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('last-n-operation-logs', REFERENCE_CLASS, 'LastNOperationLogs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.LastNOperationLogs', 
                [], [], 
                '''                Show log file for last n operations
                ''',
                'last_n_operation_logs',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('operation-logs', REFERENCE_CLASS, 'OperationLogs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.OperationLogs', 
                [], [], 
                '''                Show log file
                ''',
                'operation_logs',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('packages', REFERENCE_CLASS, 'Packages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Packages', 
                [], [], 
                '''                Show the list of installed packages
                ''',
                'packages',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('prepare', REFERENCE_CLASS, 'Prepare' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Prepare', 
                [], [], 
                '''                Show prepared packages ready for activation
                ''',
                'prepare',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('repository', REFERENCE_CLASS, 'Repository' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Repository', 
                [], [], 
                '''                Show packages stored in install software
                repositories
                ''',
                'repository',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Request', 
                [], [], 
                '''                Show current request
                ''',
                'request',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            _MetaInfoClassMember('version', REFERENCE_CLASS, 'Version' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper', 'SoftwareInstall.Version', 
                [], [], 
                '''                Show install version
                ''',
                'version',
                'Cisco-IOS-XR-spirit-install-instmgr-oper', False),
            ],
            'Cisco-IOS-XR-spirit-install-instmgr-oper',
            'software-install',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-install-instmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_install_instmgr_oper'
        ),
    },
}
_meta_table['SoftwareInstall.Files.File.Brief']['meta_info'].parent =_meta_table['SoftwareInstall.Files.File']['meta_info']
_meta_table['SoftwareInstall.Files.File.Detail']['meta_info'].parent =_meta_table['SoftwareInstall.Files.File']['meta_info']
_meta_table['SoftwareInstall.Files.File']['meta_info'].parent =_meta_table['SoftwareInstall.Files']['meta_info']
_meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog.Summary']['meta_info'].parent =_meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog']['meta_info']
_meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog.Detail']['meta_info'].parent =_meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog']['meta_info']
_meta_table['SoftwareInstall.LastNOperationLogs.LastNOperationLog']['meta_info'].parent =_meta_table['SoftwareInstall.LastNOperationLogs']['meta_info']
_meta_table['SoftwareInstall.Prepare.Rpm']['meta_info'].parent =_meta_table['SoftwareInstall.Prepare']['meta_info']
_meta_table['SoftwareInstall.Prepare.Package']['meta_info'].parent =_meta_table['SoftwareInstall.Prepare']['meta_info']
_meta_table['SoftwareInstall.Active.ActivePackageInfo']['meta_info'].parent =_meta_table['SoftwareInstall.Active']['meta_info']
_meta_table['SoftwareInstall.Issu.Inventory.Invinfo']['meta_info'].parent =_meta_table['SoftwareInstall.Issu.Inventory']['meta_info']
_meta_table['SoftwareInstall.Issu.Stage']['meta_info'].parent =_meta_table['SoftwareInstall.Issu']['meta_info']
_meta_table['SoftwareInstall.Issu.Inventory']['meta_info'].parent =_meta_table['SoftwareInstall.Issu']['meta_info']
_meta_table['SoftwareInstall.Committed.CommittedPackageInfo']['meta_info'].parent =_meta_table['SoftwareInstall.Committed']['meta_info']
_meta_table['SoftwareInstall.AllOperationsLog.Summary']['meta_info'].parent =_meta_table['SoftwareInstall.AllOperationsLog']['meta_info']
_meta_table['SoftwareInstall.AllOperationsLog.Detail']['meta_info'].parent =_meta_table['SoftwareInstall.AllOperationsLog']['meta_info']
_meta_table['SoftwareInstall.Packages.Package.Verbose']['meta_info'].parent =_meta_table['SoftwareInstall.Packages.Package']['meta_info']
_meta_table['SoftwareInstall.Packages.Package.Brief']['meta_info'].parent =_meta_table['SoftwareInstall.Packages.Package']['meta_info']
_meta_table['SoftwareInstall.Packages.Package.Detail']['meta_info'].parent =_meta_table['SoftwareInstall.Packages.Package']['meta_info']
_meta_table['SoftwareInstall.Packages.Package']['meta_info'].parent =_meta_table['SoftwareInstall.Packages']['meta_info']
_meta_table['SoftwareInstall.OperationLogs.OperationLog.Summary']['meta_info'].parent =_meta_table['SoftwareInstall.OperationLogs.OperationLog']['meta_info']
_meta_table['SoftwareInstall.OperationLogs.OperationLog.Detail']['meta_info'].parent =_meta_table['SoftwareInstall.OperationLogs.OperationLog']['meta_info']
_meta_table['SoftwareInstall.OperationLogs.OperationLog']['meta_info'].parent =_meta_table['SoftwareInstall.OperationLogs']['meta_info']
_meta_table['SoftwareInstall.Repository.Xr']['meta_info'].parent =_meta_table['SoftwareInstall.Repository']['meta_info']
_meta_table['SoftwareInstall.Repository.All']['meta_info'].parent =_meta_table['SoftwareInstall.Repository']['meta_info']
_meta_table['SoftwareInstall.Files']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.LastNOperationLogs']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Prepare']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Active']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Version']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Inactive']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Request']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Issu']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Committed']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.AllOperationsLog']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Packages']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.OperationLogs']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
_meta_table['SoftwareInstall.Repository']['meta_info'].parent =_meta_table['SoftwareInstall']['meta_info']
