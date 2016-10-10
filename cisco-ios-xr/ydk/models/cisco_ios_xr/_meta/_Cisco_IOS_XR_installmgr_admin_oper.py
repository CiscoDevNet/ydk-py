


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'InstmgrIssuAbortMethodEnum' : _MetaInfoEnum('InstmgrIssuAbortMethodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'method-undefined':'METHOD_UNDEFINED',
            'method-no-operation':'METHOD_NO_OPERATION',
            'method-standby-reload':'METHOD_STANDBY_RELOAD',
            'method-system-reload':'METHOD_SYSTEM_RELOAD',
            'method-rollback':'METHOD_ROLLBACK',
            'method-not-possible':'METHOD_NOT_POSSIBLE',
            'method-admin-only':'METHOD_ADMIN_ONLY',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrBagRequestTriggerEnum' : _MetaInfoEnum('InstmgrBagRequestTriggerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'cli':'CLI',
            'xr-xml':'XR_XML',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrGroupEnum' : _MetaInfoEnum('InstmgrGroupEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'inst-pkg-group-undefined':'INST_PKG_GROUP_UNDEFINED',
            'inst-pkg-group-grouped':'INST_PKG_GROUP_GROUPED',
            'inst-pkg-group-individual':'INST_PKG_GROUP_INDIVIDUAL',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'IsmCardTypeFamilyEnum' : _MetaInfoEnum('IsmCardTypeFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'ndsc-active-rp':'NDSC_ACTIVE_RP',
            'ndsc-standby-rp':'NDSC_STANDBY_RP',
            'active-drp':'ACTIVE_DRP',
            'standby-drp':'STANDBY_DRP',
            'dsc-active-rp':'DSC_ACTIVE_RP',
            'dsc-standby-rp':'DSC_STANDBY_RP',
            'active-sc':'ACTIVE_SC',
            'standby-sc':'STANDBY_SC',
            'root-active-sc':'ROOT_ACTIVE_SC',
            'root-standby-sc':'ROOT_STANDBY_SC',
            'lc':'LC',
            'sp':'SP',
            'fabric-sp':'FABRIC_SP',
            'spa':'SPA',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrBagUserMsgCategoryEnum' : _MetaInfoEnum('InstmgrBagUserMsgCategoryEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'user-error':'USER_ERROR',
            'non-specific':'NON_SPECIFIC',
            'warning':'WARNING',
            'information':'INFORMATION',
            'user-prompt':'USER_PROMPT',
            'log':'LOG',
            'system-error':'SYSTEM_ERROR',
            'user-response':'USER_RESPONSE',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstallmgrIsmNodeConformingEnum' : _MetaInfoEnum('InstallmgrIsmNodeConformingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'conforming':'CONFORMING',
            'none-conforming':'NONE_CONFORMING',
            'upgrade-fail':'UPGRADE_FAIL',
            'none-conforming-spa':'NONE_CONFORMING_SPA',
            'spa-upgrade-fail':'SPA_UPGRADE_FAIL',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrInstallPhaseEnum' : _MetaInfoEnum('InstmgrInstallPhaseEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'inst-phase-unknown':'INST_PHASE_UNKNOWN',
            'inst-phase-download':'INST_PHASE_DOWNLOAD',
            'inst-phase-sw-change':'INST_PHASE_SW_CHANGE',
            'inst-phase-cleaning-up':'INST_PHASE_CLEANING_UP',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrIssuAbortImpactEnum' : _MetaInfoEnum('InstmgrIssuAbortImpactEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'undefined':'UNDEFINED',
            'hitless':'HITLESS',
            'traffic-outage':'TRAFFIC_OUTAGE',
            'not-applicable':'NOT_APPLICABLE',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrIsmNodeStateEnum' : _MetaInfoEnum('InstmgrIsmNodeStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'none':'NONE',
            'issu-node-gsp-ready':'ISSU_NODE_GSP_READY',
            'load-shut-done':'LOAD_SHUT_DONE',
            'standby-management-upgrade-done':'STANDBY_MANAGEMENT_UPGRADE_DONE',
            'fabric-upgrade-done':'FABRIC_UPGRADE_DONE',
            'imdr-preparation-ack-received':'IMDR_PREPARATION_ACK_RECEIVED',
            'imdr-preparation-failed':'IMDR_PREPARATION_FAILED',
            'imdr-start-ack-received':'IMDR_START_ACK_RECEIVED',
            'imdr-start-failed':'IMDR_START_FAILED',
            'imdr-complete-ack-received':'IMDR_COMPLETE_ACK_RECEIVED',
            'imdr-complete-failed':'IMDR_COMPLETE_FAILED',
            'standby-management-ready':'STANDBY_MANAGEMENT_READY',
            'fo-acknowledged':'FO_ACKNOWLEDGED',
            'fo-complete':'FO_COMPLETE',
            'standby-ready-after-fo':'STANDBY_READY_AFTER_FO',
            'iam-ready-afteri-mdr':'IAM_READY_AFTERI_MDR',
            'nsf-ready':'NSF_READY',
            'nsf-begin-ack-received':'NSF_BEGIN_ACK_RECEIVED',
            'imdr-done':'IMDR_DONE',
            'unshut-done':'UNSHUT_DONE',
            'run-done':'RUN_DONE',
            'imdr-abort-sent':'IMDR_ABORT_SENT',
            'imdr-abort-ack-received':'IMDR_ABORT_ACK_RECEIVED',
            'imdr-abort-failed':'IMDR_ABORT_FAILED',
            'standby-management-downgrade-done':'STANDBY_MANAGEMENT_DOWNGRADE_DONE',
            'fabric-downgrade-done':'FABRIC_DOWNGRADE_DONE',
            'reload-during-issu':'RELOAD_DURING_ISSU',
            'timneout':'TIMNEOUT',
            'fabric-upgrade-failed':'FABRIC_UPGRADE_FAILED',
            'unsupported-hw':'UNSUPPORTED_HW',
            'not-reachable':'NOT_REACHABLE',
            'max':'MAX',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrPkgEnum' : _MetaInfoEnum('InstmgrPkgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'inst-pkg-type-undefined':'INST_PKG_TYPE_UNDEFINED',
            'inst-pkg-type-root':'INST_PKG_TYPE_ROOT',
            'inst-pkg-type-standard':'INST_PKG_TYPE_STANDARD',
            'inst-pkg-type-internal':'INST_PKG_TYPE_INTERNAL',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrCardStateEnum' : _MetaInfoEnum('InstmgrCardStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'instmgr-card-not-present':'INSTMGR_CARD_NOT_PRESENT',
            'instmgr-card-present':'INSTMGR_CARD_PRESENT',
            'instmgr-card-reset':'INSTMGR_CARD_RESET',
            'instmgr-card-booting':'INSTMGR_CARD_BOOTING',
            'instmgr-card-mbi-booting':'INSTMGR_CARD_MBI_BOOTING',
            'instmgr-card-running-mbi':'INSTMGR_CARD_RUNNING_MBI',
            'instmgr-card-running-ena':'INSTMGR_CARD_RUNNING_ENA',
            'instmgr-card-bring-down':'INSTMGR_CARD_BRING_DOWN',
            'instmgr-card-ena-failure':'INSTMGR_CARD_ENA_FAILURE',
            'instmgr-card-f-diag-run':'INSTMGR_CARD_F_DIAG_RUN',
            'instmgr-card-f-diag-failure':'INSTMGR_CARD_F_DIAG_FAILURE',
            'instmgr-card-powered':'INSTMGR_CARD_POWERED',
            'instmgr-card-unpowered':'INSTMGR_CARD_UNPOWERED',
            'instmgr-card-mdr':'INSTMGR_CARD_MDR',
            'instmgr-card-mdr-running-mbi':'INSTMGR_CARD_MDR_RUNNING_MBI',
            'instmgr-card-main-t-mode':'INSTMGR_CARD_MAIN_T_MODE',
            'instmgr-card-admin-down':'INSTMGR_CARD_ADMIN_DOWN',
            'instmgr-card-no-mon':'INSTMGR_CARD_NO_MON',
            'instmgr-card-unknown':'INSTMGR_CARD_UNKNOWN',
            'instmgr-card-failed':'INSTMGR_CARD_FAILED',
            'instmgr-card-ok':'INSTMGR_CARD_OK',
            'instmgr-card-missing':'INSTMGR_CARD_MISSING',
            'instmgr-card-field-diag-downloading':'INSTMGR_CARD_FIELD_DIAG_DOWNLOADING',
            'instmgr-card-field-diag-unmonitor':'INSTMGR_CARD_FIELD_DIAG_UNMONITOR',
            'instmgr-card-fabric-field-diag-unmonitor':'INSTMGR_CARD_FABRIC_FIELD_DIAG_UNMONITOR',
            'instmgr-card-field-diag-rp-launching':'INSTMGR_CARD_FIELD_DIAG_RP_LAUNCHING',
            'instmgr-card-field-diag-running':'INSTMGR_CARD_FIELD_DIAG_RUNNING',
            'instmgr-card-field-diag-pass':'INSTMGR_CARD_FIELD_DIAG_PASS',
            'instmgr-card-field-diag-fail':'INSTMGR_CARD_FIELD_DIAG_FAIL',
            'instmgr-card-field-diag-timeout':'INSTMGR_CARD_FIELD_DIAG_TIMEOUT',
            'instmgr-card-disabled':'INSTMGR_CARD_DISABLED',
            'instmgr-card-spa-booting':'INSTMGR_CARD_SPA_BOOTING',
            'instmgr-card-not-allowed-online':'INSTMGR_CARD_NOT_ALLOWED_ONLINE',
            'instmgr-card-stopped':'INSTMGR_CARD_STOPPED',
            'instmgr-card-incompatible-fw-ver':'INSTMGR_CARD_INCOMPATIBLE_FW_VER',
            'instmgr-card-fpd-hold':'INSTMGR_CARD_FPD_HOLD',
            'instmgr-card-updating-fpd':'INSTMGR_CARD_UPDATING_FPD',
            'instmgr-card-num-states':'INSTMGR_CARD_NUM_STATES',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrNodeRoleEnum' : _MetaInfoEnum('InstmgrNodeRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'redundency-unknown':'REDUNDENCY_UNKNOWN',
            'redundency-active':'REDUNDENCY_ACTIVE',
            'redundency-standby':'REDUNDENCY_STANDBY',
            'redundency-unusable':'REDUNDENCY_UNUSABLE',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrRequestEnum' : _MetaInfoEnum('InstmgrRequestEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'add':'ADD',
            'accept':'ACCEPT',
            'clean':'CLEAN',
            'activate':'ACTIVATE',
            'deactivate':'DEACTIVATE',
            'commit':'COMMIT',
            'verify':'VERIFY',
            'rollback':'ROLLBACK',
            'clear-rollback':'CLEAR_ROLLBACK',
            'clear-log':'CLEAR_LOG',
            'health-check':'HEALTH_CHECK',
            'operation':'OPERATION',
            'stop-timer':'STOP_TIMER',
            'label':'LABEL',
            'clear-label':'CLEAR_LABEL',
            'extend':'EXTEND',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrIsmFsmStateEnum' : _MetaInfoEnum('InstmgrIsmFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'idle':'IDLE',
            'init-done':'INIT_DONE',
            'load-shut':'LOAD_SHUT',
            'load-wait':'LOAD_WAIT',
            'load-stp-root-before':'LOAD_STP_ROOT_BEFORE',
            'load-standby-root-sc-upgrade':'LOAD_STANDBY_ROOT_SC_UPGRADE',
            'load-standby-management-upgrade':'LOAD_STANDBY_MANAGEMENT_UPGRADE',
            'load-stp-root-after':'LOAD_STP_ROOT_AFTER',
            'load-fabric-upgrade':'LOAD_FABRIC_UPGRADE',
            'load-management-issu-ready':'LOAD_MANAGEMENT_ISSU_READY',
            'load-done':'LOAD_DONE',
            'run-prep':'RUN_PREP',
            'run-wait':'RUN_WAIT',
            'runi-mdr-prep':'RUNI_MDR_PREP',
            'runi-mdr-start':'RUNI_MDR_START',
            'runi-mdr-complete':'RUNI_MDR_COMPLETE',
            'run-make-standby-ready':'RUN_MAKE_STANDBY_READY',
            'run-root-scfo':'RUN_ROOT_SCFO',
            'run-ndscfo':'RUN_NDSCFO',
            'run-transient1':'RUN_TRANSIENT1',
            'run-dscfo':'RUN_DSCFO',
            'run-fo-complete':'RUN_FO_COMPLETE',
            'run-stp-root-return':'RUN_STP_ROOT_RETURN',
            'runi-mdr-continue':'RUNI_MDR_CONTINUE',
            'run-am-i-ready-afteri-mdr':'RUN_AM_I_READY_AFTERI_MDR',
            'run-nsf-ready':'RUN_NSF_READY',
            'run-nsf-begin':'RUN_NSF_BEGIN',
            'runi-mdr-done':'RUNI_MDR_DONE',
            'run-management-issu-ready':'RUN_MANAGEMENT_ISSU_READY',
            'run-un-shut':'RUN_UN_SHUT',
            'run-is-done':'RUN_IS_DONE',
            'state-max':'STATE_MAX',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrBagIiDirectionEnum' : _MetaInfoEnum('InstmgrBagIiDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'not-incremental':'NOT_INCREMENTAL',
            'installing':'INSTALLING',
            'unwinding':'UNWINDING',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrPiCardEnum' : _MetaInfoEnum('InstmgrPiCardEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'type-rp':'TYPE_RP',
            'type-drp':'TYPE_DRP',
            'type-lc':'TYPE_LC',
            'type-sc':'TYPE_SC',
            'type-sp':'TYPE_SP',
            'type-other':'TYPE_OTHER',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrBagIiStateEnum' : _MetaInfoEnum('InstmgrBagIiStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'idle':'IDLE',
            'in-progress':'IN_PROGRESS',
            'completed':'COMPLETED',
            'aborted':'ABORTED',
            'rebooted':'REBOOTED',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrBagLogEntryUserMsgCategoryEnum' : _MetaInfoEnum('InstmgrBagLogEntryUserMsgCategoryEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'user-error':'USER_ERROR',
            'non-specific':'NON_SPECIFIC',
            'warning':'WARNING',
            'information':'INFORMATION',
            'user-prompt':'USER_PROMPT',
            'log':'LOG',
            'system-error':'SYSTEM_ERROR',
            'user-response':'USER_RESPONSE',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'InstmgrBagAbortStateEnum' : _MetaInfoEnum('InstmgrBagAbortStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper',
        {
            'abortable':'ABORTABLE',
            'no-longer-abortable':'NO_LONGER_ABORTABLE',
            'never-abortable':'NEVER_ABORTABLE',
            'already-aborted':'ALREADY_ABORTED',
        }, 'Cisco-IOS-XR-installmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper']),
    'Install.ConfigurationRegisters.ConfigurationRegister' : {
        'meta_info' : _MetaInfoClass('Install.ConfigurationRegisters.ConfigurationRegister',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('config-register', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{1,8}'], 
                '''                Configuration register value
                ''',
                'config_register',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'configuration-register',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.ConfigurationRegisters' : {
        'meta_info' : _MetaInfoClass('Install.ConfigurationRegisters',
            False, 
            [
            _MetaInfoClassMember('configuration-register', REFERENCE_LIST, 'ConfigurationRegister' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.ConfigurationRegisters.ConfigurationRegister', 
                [], [], 
                '''                Configuration register for specific node
                ''',
                'configuration_register',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'configuration-registers',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.RequestInformation' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.RequestInformation',
            False, 
            [
            _MetaInfoClassMember('operation-detail', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Detail operation information
                ''',
                'operation_detail',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('operation-type', REFERENCE_ENUM_CLASS, 'InstmgrRequestEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrRequestEnum', 
                [], [], 
                '''                Requested operation type
                ''',
                'operation_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install id of operation
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-option', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Options affecting processing of install requests
                ''',
                'request_option',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('trigger-type', REFERENCE_ENUM_CLASS, 'InstmgrBagRequestTriggerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagRequestTriggerEnum', 
                [], [], 
                '''                Request trigger type
                ''',
                'trigger_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('user-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                User ID that started the reqeust
                ''',
                'user_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'request-information',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.AbortStatus' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.AbortStatus',
            False, 
            [
            _MetaInfoClassMember('abort-impact', REFERENCE_ENUM_CLASS, 'InstmgrIssuAbortImpactEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIssuAbortImpactEnum', 
                [], [], 
                '''                Impact of abort
                ''',
                'abort_impact',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('abort-method', REFERENCE_ENUM_CLASS, 'InstmgrIssuAbortMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIssuAbortMethodEnum', 
                [], [], 
                '''                Method of abort
                ''',
                'abort_method',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'abort-status',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node identifier
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'InstmgrBagIiStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagIiStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.IncrementalInstallInformation' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.IncrementalInstallInformation',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'InstmgrBagIiDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagIiDirectionEnum', 
                [], [], 
                '''                Install direction
                ''',
                'direction',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('ii-error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First error during incremental install
                ''',
                'ii_error',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_LIST, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes', 
                [], [], 
                '''                Participating nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'incremental-install-information',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.IssuMessage.Scope' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.IssuMessage.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which LRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.IssuMessage' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.IssuMessage',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.IssuMessage.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'issu-message',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.Message.Scope' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.Message.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which LRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus.Message' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus.Message',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.Message.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'message',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses.RequestStatus' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses.RequestStatus',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Install operation request ID
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('abort-state', REFERENCE_ENUM_CLASS, 'InstmgrBagAbortStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagAbortStateEnum', 
                [], [], 
                '''                Abort state
                ''',
                'abort_state',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('abort-status', REFERENCE_CLASS, 'AbortStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.AbortStatus', 
                [], [], 
                '''                How the abort will occur
                ''',
                'abort_status',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('downloaded-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Downloaded bytes
                ''',
                'downloaded_bytes',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('incremental-install-information', REFERENCE_CLASS, 'IncrementalInstallInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.IncrementalInstallInformation', 
                [], [], 
                '''                Incremental Install information
                ''',
                'incremental_install_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('issu-message', REFERENCE_LIST, 'IssuMessage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.IssuMessage', 
                [], [], 
                '''                Messages related to ISSU operations
                ''',
                'issu_message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', REFERENCE_LIST, 'Message' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.Message', 
                [], [], 
                '''                Messages output to the user
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('operation-phase', REFERENCE_ENUM_CLASS, 'InstmgrInstallPhaseEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrInstallPhaseEnum', 
                [], [], 
                '''                Phase of the operation
                ''',
                'operation_phase',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Percentage completed
                ''',
                'percentage',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-information', REFERENCE_CLASS, 'RequestInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus.RequestInformation', 
                [], [], 
                '''                Requested install operation
                ''',
                'request_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('unanswered-query', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the operation is blocked waiting for a
                response from the user
                ''',
                'unanswered_query',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'request-status',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.RequestStatuses' : {
        'meta_info' : _MetaInfoClass('Install.RequestStatuses',
            False, 
            [
            _MetaInfoClassMember('request-status', REFERENCE_LIST, 'RequestStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses.RequestStatus', 
                [], [], 
                '''                Request status Information
                ''',
                'request_status',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'request-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.BootVariables.BootVariable' : {
        'meta_info' : _MetaInfoClass('Install.BootVariables.BootVariable',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('boot-variable', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Boot variable value
                ''',
                'boot_variable',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'boot-variable',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.BootVariables' : {
        'meta_info' : _MetaInfoClass('Install.BootVariables',
            False, 
            [
            _MetaInfoClassMember('boot-variable', REFERENCE_LIST, 'BootVariable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.BootVariables.BootVariable', 
                [], [], 
                '''                Boot variable for specific node
                ''',
                'boot_variable',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'boot-variables',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.AliasDevices.AliasDevice.Aliases.Alias' : {
        'meta_info' : _MetaInfoClass('Install.Software.AliasDevices.AliasDevice.Aliases.Alias',
            False, 
            [
            _MetaInfoClassMember('package-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package Name
                ''',
                'package_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('alias-names', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Alias names
                ''',
                'alias_names',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'alias',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.AliasDevices.AliasDevice.Aliases' : {
        'meta_info' : _MetaInfoClass('Install.Software.AliasDevices.AliasDevice.Aliases',
            False, 
            [
            _MetaInfoClassMember('alias', REFERENCE_LIST, 'Alias' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.AliasDevices.AliasDevice.Aliases.Alias', 
                [], [], 
                '''                Aliases for specific package
                ''',
                'alias',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'aliases',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.AliasDevices.AliasDevice' : {
        'meta_info' : _MetaInfoClass('Install.Software.AliasDevices.AliasDevice',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Device Name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('aliases', REFERENCE_CLASS, 'Aliases' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.AliasDevices.AliasDevice.Aliases', 
                [], [], 
                '''                alias information
                ''',
                'aliases',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'alias-device',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.AliasDevices' : {
        'meta_info' : _MetaInfoClass('Install.Software.AliasDevices',
            False, 
            [
            _MetaInfoClassMember('alias-device', REFERENCE_LIST, 'AliasDevice' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.AliasDevices.AliasDevice', 
                [], [], 
                '''                Package alias information for specific device
                ''',
                'alias_device',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'alias-devices',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg' : {
        'meta_info' : _MetaInfoClass('Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the sub-package
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-types', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Node types of the package
                ''',
                'node_types',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'sub-pkg',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.PackageDevices.PackageDevice.Packages.Package' : {
        'meta_info' : _MetaInfoClass('Install.Software.PackageDevices.PackageDevice.Packages.Package',
            False, 
            [
            _MetaInfoClassMember('package-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package Name
                ''',
                'package_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('base', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifies the base bundle that the package is
                for
                ''',
                'base',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('bootable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if package has BOOTIMAGE tag set
                ''',
                'bootable',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('cards', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Card types that the package should be installed
                on
                ''',
                'cards',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('composite', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if package is a composite package
                ''',
                'composite',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('compressed-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Compressed size of package
                ''',
                'compressed_size',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('date', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time and date that the package was built
                ''',
                'date',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('depth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of layers of parent packages
                ''',
                'depth',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the package
                ''',
                'description',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('group-type', REFERENCE_ENUM_CLASS, 'InstmgrGroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrGroupEnum', 
                [], [], 
                '''                Group type of the package
                ''',
                'group_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the package
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package-type', REFERENCE_ENUM_CLASS, 'InstmgrPkgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrPkgEnum', 
                [], [], 
                '''                Type of the package
                ''',
                'package_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('release', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Release that the package belongs to
                ''',
                'release',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('restart-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Restart info of the package
                ''',
                'restart_info',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifies the provider of the package
                ''',
                'source',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('sub-pkg', REFERENCE_LIST, 'SubPkg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg', 
                [], [], 
                '''                Sub-package info of the package
                ''',
                'sub_pkg',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('uncompressed-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Uncompressed size of package
                ''',
                'uncompressed_size',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('vendor', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Information about the vendor that supplied the
                package
                ''',
                'vendor',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the package
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.PackageDevices.PackageDevice.Packages' : {
        'meta_info' : _MetaInfoClass('Install.Software.PackageDevices.PackageDevice.Packages',
            False, 
            [
            _MetaInfoClassMember('package', REFERENCE_LIST, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.PackageDevices.PackageDevice.Packages.Package', 
                [], [], 
                '''                Package information
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'packages',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.PackageDevices.PackageDevice' : {
        'meta_info' : _MetaInfoClass('Install.Software.PackageDevices.PackageDevice',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Device Name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('packages', REFERENCE_CLASS, 'Packages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.PackageDevices.PackageDevice.Packages', 
                [], [], 
                '''                Package information for specific package
                ''',
                'packages',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package-device',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.PackageDevices' : {
        'meta_info' : _MetaInfoClass('Install.Software.PackageDevices',
            False, 
            [
            _MetaInfoClassMember('package-device', REFERENCE_LIST, 'PackageDevice' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.PackageDevices.PackageDevice', 
                [], [], 
                '''                Package information for specific device
                ''',
                'package_device',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package-devices',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component' : {
        'meta_info' : _MetaInfoClass('Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component',
            False, 
            [
            _MetaInfoClassMember('component-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Component Name
                ''',
                'component_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the component
                ''',
                'description',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('files', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                The set of files belonging to the component
                ''',
                'files',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the component
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('release', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Release that the component belongs to
                ''',
                'release',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the component
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'component',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage' : {
        'meta_info' : _MetaInfoClass('Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage',
            False, 
            [
            _MetaInfoClassMember('package-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package Name
                ''',
                'package_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('component', REFERENCE_LIST, 'Component' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component', 
                [], [], 
                '''                Component information
                ''',
                'component',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'component-package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.ComponentDevices.ComponentDevice.ComponentPackages' : {
        'meta_info' : _MetaInfoClass('Install.Software.ComponentDevices.ComponentDevice.ComponentPackages',
            False, 
            [
            _MetaInfoClassMember('component-package', REFERENCE_LIST, 'ComponentPackage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage', 
                [], [], 
                '''                Component information for specific package
                ''',
                'component_package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'component-packages',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.ComponentDevices.ComponentDevice' : {
        'meta_info' : _MetaInfoClass('Install.Software.ComponentDevices.ComponentDevice',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Device Name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('component-packages', REFERENCE_CLASS, 'ComponentPackages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.ComponentDevices.ComponentDevice.ComponentPackages', 
                [], [], 
                '''                Software package information
                ''',
                'component_packages',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'component-device',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software.ComponentDevices' : {
        'meta_info' : _MetaInfoClass('Install.Software.ComponentDevices',
            False, 
            [
            _MetaInfoClassMember('component-device', REFERENCE_LIST, 'ComponentDevice' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.ComponentDevices.ComponentDevice', 
                [], [], 
                '''                Component information for specific device
                ''',
                'component_device',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'component-devices',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Software' : {
        'meta_info' : _MetaInfoClass('Install.Software',
            False, 
            [
            _MetaInfoClassMember('alias-devices', REFERENCE_CLASS, 'AliasDevices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.AliasDevices', 
                [], [], 
                '''                Package alias information
                ''',
                'alias_devices',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('component-devices', REFERENCE_CLASS, 'ComponentDevices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.ComponentDevices', 
                [], [], 
                '''                Software component information
                ''',
                'component_devices',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package-devices', REFERENCE_CLASS, 'PackageDevices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software.PackageDevices', 
                [], [], 
                '''                Package information
                ''',
                'package_devices',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'software',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.DefaultLoadPath',
            False, 
            [
            _MetaInfoClassMember('admin-match', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does this match the Admin Resources load path?
                ''',
                'admin_match',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath', 
                [], [], 
                '''                Default load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Names of SDRs this applies to
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'default-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.AdminLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.AdminLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath', 
                [], [], 
                '''                Admin Resources load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'admin-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.SdrLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.SdrLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'sdr-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary.LocationLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary.LocationLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node identifier
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'location-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Summary' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Summary',
            False, 
            [
            _MetaInfoClassMember('admin-load-path', REFERENCE_CLASS, 'AdminLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.AdminLoadPath', 
                [], [], 
                '''                Admin Resources load path
                ''',
                'admin_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('default-load-path', REFERENCE_CLASS, 'DefaultLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.DefaultLoadPath', 
                [], [], 
                '''                Default load path
                ''',
                'default_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('location-load-path', REFERENCE_LIST, 'LocationLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.LocationLoadPath', 
                [], [], 
                '''                Location load paths
                ''',
                'location_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('sdr-load-path', REFERENCE_LIST, 'SdrLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary.SdrLoadPath', 
                [], [], 
                '''                SDR load paths
                ''',
                'sdr_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Inventories.Inventory' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Inventories.Inventory',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('boot-image-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the boot image
                ''',
                'boot_image_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('major', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Major data version number
                ''',
                'major',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minor data version number
                ''',
                'minor',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Node's type
                ''',
                'node_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed.Inventories' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed.Inventories',
            False, 
            [
            _MetaInfoClassMember('inventory', REFERENCE_LIST, 'Inventory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Inventories.Inventory', 
                [], [], 
                '''                Inventory information for specific node
                ''',
                'inventory',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventories',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Committed' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Committed',
            False, 
            [
            _MetaInfoClassMember('inventories', REFERENCE_CLASS, 'Inventories' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Inventories', 
                [], [], 
                '''                Software inventory
                ''',
                'inventories',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed.Summary', 
                [], [], 
                '''                Summarized inventory information
                ''',
                'summary',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'committed',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath',
            False, 
            [
            _MetaInfoClassMember('admin-match', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does this match the Admin Resources load path?
                ''',
                'admin_match',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath', 
                [], [], 
                '''                Default load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Names of SDRs this applies to
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'default-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.AdminLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath', 
                [], [], 
                '''                Admin Resources load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'admin-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.SdrLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'sdr-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary.LocationLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node identifier
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'location-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Summary' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Summary',
            False, 
            [
            _MetaInfoClassMember('admin-load-path', REFERENCE_CLASS, 'AdminLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.AdminLoadPath', 
                [], [], 
                '''                Admin Resources load path
                ''',
                'admin_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('default-load-path', REFERENCE_CLASS, 'DefaultLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath', 
                [], [], 
                '''                Default load path
                ''',
                'default_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('location-load-path', REFERENCE_LIST, 'LocationLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.LocationLoadPath', 
                [], [], 
                '''                Location load paths
                ''',
                'location_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('sdr-load-path', REFERENCE_LIST, 'SdrLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary.SdrLoadPath', 
                [], [], 
                '''                SDR load paths
                ''',
                'sdr_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Inventories.Inventory' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Inventories.Inventory',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('boot-image-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the boot image
                ''',
                'boot_image_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('major', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Major data version number
                ''',
                'major',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minor data version number
                ''',
                'minor',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Node's type
                ''',
                'node_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive.Inventories' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive.Inventories',
            False, 
            [
            _MetaInfoClassMember('inventory', REFERENCE_LIST, 'Inventory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Inventories.Inventory', 
                [], [], 
                '''                Inventory information for specific node
                ''',
                'inventory',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventories',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Inactive' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Inactive',
            False, 
            [
            _MetaInfoClassMember('inventories', REFERENCE_CLASS, 'Inventories' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Inventories', 
                [], [], 
                '''                Software inventory
                ''',
                'inventories',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive.Summary', 
                [], [], 
                '''                Summarized inventory information
                ''',
                'summary',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('boot-image-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the boot image
                ''',
                'boot_image_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('major', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Major data version number
                ''',
                'major',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minor data version number
                ''',
                'minor',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Node's type
                ''',
                'node_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Requests.Requests.Request.Inventories' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Requests.Requests.Request.Inventories',
            False, 
            [
            _MetaInfoClassMember('inventory', REFERENCE_LIST, 'Inventory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory', 
                [], [], 
                '''                Inventory information
                ''',
                'inventory',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventories',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Requests.Requests.Request' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Requests.Requests.Request',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Install operation request ID
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('inventories', REFERENCE_CLASS, 'Inventories' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Requests.Requests.Request.Inventories', 
                [], [], 
                '''                Inventory information of install operation
                request
                ''',
                'inventories',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Requests.Requests' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Requests.Requests',
            False, 
            [
            _MetaInfoClassMember('request', REFERENCE_LIST, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Requests.Requests.Request', 
                [], [], 
                '''                Install operation request information
                ''',
                'request',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'requests',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Requests' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Requests',
            False, 
            [
            _MetaInfoClassMember('requests', REFERENCE_CLASS, 'Requests' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Requests.Requests', 
                [], [], 
                '''                Install operation request history
                ''',
                'requests',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'requests',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.DefaultLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.DefaultLoadPath',
            False, 
            [
            _MetaInfoClassMember('admin-match', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does this match the Admin Resources load path?
                ''',
                'admin_match',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath', 
                [], [], 
                '''                Default load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Names of SDRs this applies to
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'default-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.AdminLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.AdminLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath', 
                [], [], 
                '''                Admin Resources load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'admin-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.SdrLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.SdrLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'sdr-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'standby-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary.LocationLoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary.LocationLoadPath',
            False, 
            [
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node identifier
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Install op affecting scope
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('standby-load-path', REFERENCE_LIST, 'StandbyLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath', 
                [], [], 
                '''                Load paths for standby nodes
                ''',
                'standby_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'location-load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Summary' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Summary',
            False, 
            [
            _MetaInfoClassMember('admin-load-path', REFERENCE_CLASS, 'AdminLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.AdminLoadPath', 
                [], [], 
                '''                Admin Resources load path
                ''',
                'admin_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('default-load-path', REFERENCE_CLASS, 'DefaultLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.DefaultLoadPath', 
                [], [], 
                '''                Default load path
                ''',
                'default_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('location-load-path', REFERENCE_LIST, 'LocationLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.LocationLoadPath', 
                [], [], 
                '''                Location load paths
                ''',
                'location_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('sdr-load-path', REFERENCE_LIST, 'SdrLoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary.SdrLoadPath', 
                [], [], 
                '''                SDR load paths
                ''',
                'sdr_load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package',
            False, 
            [
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device name
                ''',
                'device_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Package group name
                ''',
                'name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'package',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath',
            False, 
            [
            _MetaInfoClassMember('build-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Build information
                ''',
                'build_information',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('package', REFERENCE_CLASS, 'Package' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package', 
                [], [], 
                '''                Package
                ''',
                'package',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'load-path',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Inventories.Inventory' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Inventories.Inventory',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('boot-image-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the boot image
                ''',
                'boot_image_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('load-path', REFERENCE_LIST, 'LoadPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath', 
                [], [], 
                '''                Load path
                ''',
                'load_path',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('major', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Major data version number
                ''',
                'major',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minor data version number
                ''',
                'minor',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Node's type
                ''',
                'node_type',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('secure-domain-router-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SDR name
                ''',
                'secure_domain_router_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active.Inventories' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active.Inventories',
            False, 
            [
            _MetaInfoClassMember('inventory', REFERENCE_LIST, 'Inventory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Inventories.Inventory', 
                [], [], 
                '''                Inventory information for specific node
                ''',
                'inventory',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'inventories',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory.Active' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory.Active',
            False, 
            [
            _MetaInfoClassMember('inventories', REFERENCE_CLASS, 'Inventories' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Inventories', 
                [], [], 
                '''                Software inventory
                ''',
                'inventories',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active.Summary', 
                [], [], 
                '''                Summarized inventory information
                ''',
                'summary',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.SoftwareInventory' : {
        'meta_info' : _MetaInfoClass('Install.SoftwareInventory',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Active', 
                [], [], 
                '''                Active inventory information
                ''',
                'active',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('committed', REFERENCE_CLASS, 'Committed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Committed', 
                [], [], 
                '''                Committed inventory information
                ''',
                'committed',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Inactive', 
                [], [], 
                '''                Inactive inventory information
                ''',
                'inactive',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('requests', REFERENCE_CLASS, 'Requests' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory.Requests', 
                [], [], 
                '''                Install operation requests
                ''',
                'requests',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'software-inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.CardInventories.CardInventory.Summary' : {
        'meta_info' : _MetaInfoClass('Install.Issu.CardInventories.CardInventory.Summary',
            False, 
            [
            _MetaInfoClassMember('attempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of attempts made
                ''',
                'attempts',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('is-conforming-node', REFERENCE_ENUM_CLASS, 'InstallmgrIsmNodeConformingEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstallmgrIsmNodeConformingEnum', 
                [], [], 
                '''                Node none-cnforming
                ''',
                'is_conforming_node',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('is-node-upgraded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is node upgraded?
                ''',
                'is_node_upgraded',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-current-state', REFERENCE_ENUM_CLASS, 'InstmgrIsmNodeStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIsmNodeStateEnum', 
                [], [], 
                '''                Current node ISSU state
                ''',
                'node_current_state',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-expected-state', REFERENCE_ENUM_CLASS, 'InstmgrIsmNodeStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIsmNodeStateEnum', 
                [], [], 
                '''                Expected ISSU state
                ''',
                'node_expected_state',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-failure-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node failure reason
                ''',
                'node_failure_reason',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node identifier
                ''',
                'node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-role', REFERENCE_ENUM_CLASS, 'InstmgrNodeRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrNodeRoleEnum', 
                [], [], 
                '''                Node roll
                ''',
                'node_role',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-state', REFERENCE_ENUM_CLASS, 'InstmgrCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrCardStateEnum', 
                [], [], 
                '''                Node state
                ''',
                'node_state',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-type-issu', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ISSU node type
                ''',
                'node_type_issu',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-type-pi', REFERENCE_ENUM_CLASS, 'InstmgrPiCardEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrPiCardEnum', 
                [], [], 
                '''                PI Node type
                ''',
                'node_type_pi',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('partner-node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Partner Node IDs
                ''',
                'partner_node_name',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.CardInventories.CardInventory' : {
        'meta_info' : _MetaInfoClass('Install.Issu.CardInventories.CardInventory',
            False, 
            [
            _MetaInfoClassMember('card-type-id', REFERENCE_ENUM_CLASS, 'IsmCardTypeFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'IsmCardTypeFamilyEnum', 
                [], [], 
                '''                ISSU manager card type ID
                ''',
                'card_type_id',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('summary', REFERENCE_LIST, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.CardInventories.CardInventory.Summary', 
                [], [], 
                '''                node state for all nodes
                ''',
                'summary',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'card-inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.CardInventories' : {
        'meta_info' : _MetaInfoClass('Install.Issu.CardInventories',
            False, 
            [
            _MetaInfoClassMember('card-inventory', REFERENCE_LIST, 'CardInventory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.CardInventories.CardInventory', 
                [], [], 
                '''                ISSU manager inventory summary of the same
                card type
                ''',
                'card_inventory',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'card-inventories',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.Stage.NodeInProgress' : {
        'meta_info' : _MetaInfoClass('Install.Issu.Stage.NodeInProgress',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node
                ''',
                'node',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'node-in-progress',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.Stage.NodesInLoad' : {
        'meta_info' : _MetaInfoClass('Install.Issu.Stage.NodesInLoad',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node
                ''',
                'node',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'nodes-in-load',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.Stage.NodesInRun' : {
        'meta_info' : _MetaInfoClass('Install.Issu.Stage.NodesInRun',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node
                ''',
                'node',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'nodes-in-run',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.Stage.NcNodes' : {
        'meta_info' : _MetaInfoClass('Install.Issu.Stage.NcNodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node
                ''',
                'node',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'nc-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu.Stage' : {
        'meta_info' : _MetaInfoClass('Install.Issu.Stage',
            False, 
            [
            _MetaInfoClassMember('is-issu-aborted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ISSU aborted?
                ''',
                'is_issu_aborted',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('is-issu-aborted-by-ism', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ISSU aborted by ISM?
                ''',
                'is_issu_aborted_by_ism',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('issu-manager-fsm-state', REFERENCE_ENUM_CLASS, 'InstmgrIsmFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrIsmFsmStateEnum', 
                [], [], 
                '''                ISM FSM state
                ''',
                'issu_manager_fsm_state',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('issu-op-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISSU operational ID
                ''',
                'issu_op_id',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('issu-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Current ISSU state
                ''',
                'issu_state',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('nc-nodes', REFERENCE_CLASS, 'NcNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.Stage.NcNodes', 
                [], [], 
                '''                None-conforming nodes
                ''',
                'nc_nodes',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('node-in-progress', REFERENCE_CLASS, 'NodeInProgress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.Stage.NodeInProgress', 
                [], [], 
                '''                Nodes in progress
                ''',
                'node_in_progress',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('nodes-in-load', REFERENCE_CLASS, 'NodesInLoad' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.Stage.NodesInLoad', 
                [], [], 
                '''                Node in LOAD phase
                ''',
                'nodes_in_load',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('nodes-in-run', REFERENCE_CLASS, 'NodesInRun' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.Stage.NodesInRun', 
                [], [], 
                '''                Node in RUN phase
                ''',
                'nodes_in_run',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('num-nodes-in-progress', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of node in progress
                ''',
                'num_nodes_in_progress',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('num-of-nodes-in-load', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes in LOAD phase
                ''',
                'num_of_nodes_in_load',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('num-of-nodes-in-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of nodes in RUN phase
                ''',
                'num_of_nodes_in_run',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('numof-nc-nodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of none-conforming nodes
                ''',
                'numof_nc_nodes',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('participating-node-all', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of participating nodes
                ''',
                'participating_node_all',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ISSU progress percentage
                ''',
                'percentage',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'stage',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Issu' : {
        'meta_info' : _MetaInfoClass('Install.Issu',
            False, 
            [
            _MetaInfoClassMember('card-inventories', REFERENCE_CLASS, 'CardInventories' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.CardInventories', 
                [], [], 
                '''                ISSU manager card inventory table
                ''',
                'card_inventories',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('stage', REFERENCE_CLASS, 'Stage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu.Stage', 
                [], [], 
                '''                Summarized ISSU stage information
                ''',
                'stage',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'issu',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.BootImage' : {
        'meta_info' : _MetaInfoClass('Install.BootImage',
            False, 
            [
            _MetaInfoClassMember('system-image-file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The boot image
                ''',
                'system_image_file',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'boot-image',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Header.LogContents.V3.Scope' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Header.LogContents.V3.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which SDRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Header.LogContents.V3' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Header.LogContents.V3',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagLogEntryUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Header.LogContents.V3.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'v3',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Header.LogContents' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Header.LogContents',
            False, 
            [
            _MetaInfoClassMember('v3', REFERENCE_CLASS, 'V3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Header.LogContents.V3', 
                [], [], 
                '''                v3
                ''',
                'v3',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Header' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Header',
            False, 
            [
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Header.LogContents', 
                [], [], 
                '''                Log contents
                ''',
                'log_contents',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'header',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Summary.LogContents.V3.Scope' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Summary.LogContents.V3.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which SDRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Summary.LogContents.V3' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Summary.LogContents.V3',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagLogEntryUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Summary.LogContents.V3.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'v3',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Summary.LogContents' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Summary.LogContents',
            False, 
            [
            _MetaInfoClassMember('v3', REFERENCE_CLASS, 'V3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Summary.LogContents.V3', 
                [], [], 
                '''                v3
                ''',
                'v3',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Summary' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Summary',
            False, 
            [
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Summary.LogContents', 
                [], [], 
                '''                Log contents
                ''',
                'log_contents',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Message.LogContents.V3.Scope' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Message.LogContents.V3.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which SDRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Message.LogContents.V3' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Message.LogContents.V3',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagLogEntryUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Message.LogContents.V3.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'v3',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Message.LogContents' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Message.LogContents',
            False, 
            [
            _MetaInfoClassMember('v3', REFERENCE_CLASS, 'V3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Message.LogContents.V3', 
                [], [], 
                '''                v3
                ''',
                'v3',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Message' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Message',
            False, 
            [
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Message.LogContents', 
                [], [], 
                '''                Log contents
                ''',
                'log_contents',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'message',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Change.LogContents.V3.Scope' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Change.LogContents.V3.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which SDRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Change.LogContents.V3' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Change.LogContents.V3',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagLogEntryUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Change.LogContents.V3.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'v3',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Change.LogContents' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Change.LogContents',
            False, 
            [
            _MetaInfoClassMember('v3', REFERENCE_CLASS, 'V3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Change.LogContents.V3', 
                [], [], 
                '''                v3
                ''',
                'v3',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Change' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Change',
            False, 
            [
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Change.LogContents', 
                [], [], 
                '''                Log contents
                ''',
                'log_contents',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'change',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Detail.LogContents.V3.Scope' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Detail.LogContents.V3.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which SDRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Detail.LogContents.V3' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Detail.LogContents.V3',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagLogEntryUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Detail.LogContents.V3.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'v3',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Detail.LogContents' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Detail.LogContents',
            False, 
            [
            _MetaInfoClassMember('v3', REFERENCE_CLASS, 'V3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Detail.LogContents.V3', 
                [], [], 
                '''                v3
                ''',
                'v3',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Detail' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Detail',
            False, 
            [
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Detail.LogContents', 
                [], [], 
                '''                Log contents
                ''',
                'log_contents',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Communication.LogContents.V3.Scope' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Communication.LogContents.V3.Scope',
            False, 
            [
            _MetaInfoClassMember('admin-read', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the admin want to read this?
                ''',
                'admin_read',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('affected-sd-rs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Which SDRs are affected by the message
                ''',
                'affected_sd_rs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'scope',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Communication.LogContents.V3' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Communication.LogContents.V3',
            False, 
            [
            _MetaInfoClassMember('category', REFERENCE_ENUM_CLASS, 'InstmgrBagLogEntryUserMsgCategoryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'InstmgrBagLogEntryUserMsgCategoryEnum', 
                [], [], 
                '''                Category of the message
                ''',
                'category',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Message
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('scope', REFERENCE_CLASS, 'Scope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Communication.LogContents.V3.Scope', 
                [], [], 
                '''                Scope of the message
                ''',
                'scope',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'v3',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Communication.LogContents' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Communication.LogContents',
            False, 
            [
            _MetaInfoClassMember('v3', REFERENCE_CLASS, 'V3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Communication.LogContents.V3', 
                [], [], 
                '''                v3
                ''',
                'v3',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Version
                ''',
                'version',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'log-contents',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log.Communication' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log.Communication',
            False, 
            [
            _MetaInfoClassMember('log-contents', REFERENCE_CLASS, 'LogContents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Communication.LogContents', 
                [], [], 
                '''                Log contents
                ''',
                'log_contents',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'communication',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs.Log' : {
        'meta_info' : _MetaInfoClass('Install.Logs.Log',
            False, 
            [
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Install operation request ID
                ''',
                'request_id',
                'Cisco-IOS-XR-installmgr-admin-oper', True),
            _MetaInfoClassMember('change', REFERENCE_LIST, 'Change' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Change', 
                [], [], 
                '''                Install changes
                ''',
                'change',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('communication', REFERENCE_LIST, 'Communication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Communication', 
                [], [], 
                '''                Install communications
                ''',
                'communication',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_LIST, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Detail', 
                [], [], 
                '''                Install details
                ''',
                'detail',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('header', REFERENCE_LIST, 'Header' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Header', 
                [], [], 
                '''                Header information
                ''',
                'header',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('message', REFERENCE_LIST, 'Message' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Message', 
                [], [], 
                '''                Status Information Logs
                ''',
                'message',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_LIST, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log.Summary', 
                [], [], 
                '''                Summary information
                ''',
                'summary',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'log',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install.Logs' : {
        'meta_info' : _MetaInfoClass('Install.Logs',
            False, 
            [
            _MetaInfoClassMember('log', REFERENCE_LIST, 'Log' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs.Log', 
                [], [], 
                '''                Log information
                ''',
                'log',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'logs',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
    'Install' : {
        'meta_info' : _MetaInfoClass('Install',
            False, 
            [
            _MetaInfoClassMember('boot-image', REFERENCE_CLASS, 'BootImage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.BootImage', 
                [], [], 
                '''                System Boot Image
                ''',
                'boot_image',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('boot-variables', REFERENCE_CLASS, 'BootVariables' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.BootVariables', 
                [], [], 
                '''                Boot variable information
                ''',
                'boot_variables',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('configuration-registers', REFERENCE_CLASS, 'ConfigurationRegisters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.ConfigurationRegisters', 
                [], [], 
                '''                Configuration register (confreg) information
                ''',
                'configuration_registers',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('issu', REFERENCE_CLASS, 'Issu' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Issu', 
                [], [], 
                '''                Information of install ISSU operations
                ''',
                'issu',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('log-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Install operation log history size
                ''',
                'log_size',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('logs', REFERENCE_CLASS, 'Logs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Logs', 
                [], [], 
                '''                Install operation log
                ''',
                'logs',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('request-statuses', REFERENCE_CLASS, 'RequestStatuses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.RequestStatuses', 
                [], [], 
                '''                Install operation request status
                ''',
                'request_statuses',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('software', REFERENCE_CLASS, 'Software' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.Software', 
                [], [], 
                '''                Software package,component and alias information
                ''',
                'software',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            _MetaInfoClassMember('software-inventory', REFERENCE_CLASS, 'SoftwareInventory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper', 'Install.SoftwareInventory', 
                [], [], 
                '''                Information of install operations
                ''',
                'software_inventory',
                'Cisco-IOS-XR-installmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-installmgr-admin-oper',
            'install',
            _yang_ns._namespaces['Cisco-IOS-XR-installmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_installmgr_admin_oper'
        ),
    },
}
_meta_table['Install.ConfigurationRegisters.ConfigurationRegister']['meta_info'].parent =_meta_table['Install.ConfigurationRegisters']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.IncrementalInstallInformation.Nodes']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus.IncrementalInstallInformation']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.IssuMessage.Scope']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus.IssuMessage']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.Message.Scope']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus.Message']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.RequestInformation']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.AbortStatus']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.IncrementalInstallInformation']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.IssuMessage']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus.Message']['meta_info'].parent =_meta_table['Install.RequestStatuses.RequestStatus']['meta_info']
_meta_table['Install.RequestStatuses.RequestStatus']['meta_info'].parent =_meta_table['Install.RequestStatuses']['meta_info']
_meta_table['Install.BootVariables.BootVariable']['meta_info'].parent =_meta_table['Install.BootVariables']['meta_info']
_meta_table['Install.Software.AliasDevices.AliasDevice.Aliases.Alias']['meta_info'].parent =_meta_table['Install.Software.AliasDevices.AliasDevice.Aliases']['meta_info']
_meta_table['Install.Software.AliasDevices.AliasDevice.Aliases']['meta_info'].parent =_meta_table['Install.Software.AliasDevices.AliasDevice']['meta_info']
_meta_table['Install.Software.AliasDevices.AliasDevice']['meta_info'].parent =_meta_table['Install.Software.AliasDevices']['meta_info']
_meta_table['Install.Software.PackageDevices.PackageDevice.Packages.Package.SubPkg']['meta_info'].parent =_meta_table['Install.Software.PackageDevices.PackageDevice.Packages.Package']['meta_info']
_meta_table['Install.Software.PackageDevices.PackageDevice.Packages.Package']['meta_info'].parent =_meta_table['Install.Software.PackageDevices.PackageDevice.Packages']['meta_info']
_meta_table['Install.Software.PackageDevices.PackageDevice.Packages']['meta_info'].parent =_meta_table['Install.Software.PackageDevices.PackageDevice']['meta_info']
_meta_table['Install.Software.PackageDevices.PackageDevice']['meta_info'].parent =_meta_table['Install.Software.PackageDevices']['meta_info']
_meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage.Component']['meta_info'].parent =_meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage']['meta_info']
_meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages.ComponentPackage']['meta_info'].parent =_meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages']['meta_info']
_meta_table['Install.Software.ComponentDevices.ComponentDevice.ComponentPackages']['meta_info'].parent =_meta_table['Install.Software.ComponentDevices.ComponentDevice']['meta_info']
_meta_table['Install.Software.ComponentDevices.ComponentDevice']['meta_info'].parent =_meta_table['Install.Software.ComponentDevices']['meta_info']
_meta_table['Install.Software.AliasDevices']['meta_info'].parent =_meta_table['Install.Software']['meta_info']
_meta_table['Install.Software.PackageDevices']['meta_info'].parent =_meta_table['Install.Software']['meta_info']
_meta_table['Install.Software.ComponentDevices']['meta_info'].parent =_meta_table['Install.Software']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.DefaultLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.AdminLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.SdrLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary.LocationLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Inventories.Inventory']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed.Inventories']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Summary']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed']['meta_info']
_meta_table['Install.SoftwareInventory.Committed.Inventories']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Committed']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.DefaultLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.AdminLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.SdrLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary.LocationLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Inventories.Inventory']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive.Inventories']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Summary']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive.Inventories']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Inactive']['meta_info']
_meta_table['Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory']['meta_info']
_meta_table['Install.SoftwareInventory.Requests.Requests.Request.Inventories.Inventory']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Requests.Requests.Request.Inventories']['meta_info']
_meta_table['Install.SoftwareInventory.Requests.Requests.Request.Inventories']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Requests.Requests.Request']['meta_info']
_meta_table['Install.SoftwareInventory.Requests.Requests.Request']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Requests.Requests']['meta_info']
_meta_table['Install.SoftwareInventory.Requests.Requests']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Requests']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath.StandbyLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.DefaultLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.AdminLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.SdrLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary.LocationLoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Summary']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath.Package']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Inventories.Inventory.LoadPath']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Inventories.Inventory']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Inventories.Inventory']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active.Inventories']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Summary']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active']['meta_info']
_meta_table['Install.SoftwareInventory.Active.Inventories']['meta_info'].parent =_meta_table['Install.SoftwareInventory.Active']['meta_info']
_meta_table['Install.SoftwareInventory.Committed']['meta_info'].parent =_meta_table['Install.SoftwareInventory']['meta_info']
_meta_table['Install.SoftwareInventory.Inactive']['meta_info'].parent =_meta_table['Install.SoftwareInventory']['meta_info']
_meta_table['Install.SoftwareInventory.Requests']['meta_info'].parent =_meta_table['Install.SoftwareInventory']['meta_info']
_meta_table['Install.SoftwareInventory.Active']['meta_info'].parent =_meta_table['Install.SoftwareInventory']['meta_info']
_meta_table['Install.Issu.CardInventories.CardInventory.Summary']['meta_info'].parent =_meta_table['Install.Issu.CardInventories.CardInventory']['meta_info']
_meta_table['Install.Issu.CardInventories.CardInventory']['meta_info'].parent =_meta_table['Install.Issu.CardInventories']['meta_info']
_meta_table['Install.Issu.Stage.NodeInProgress']['meta_info'].parent =_meta_table['Install.Issu.Stage']['meta_info']
_meta_table['Install.Issu.Stage.NodesInLoad']['meta_info'].parent =_meta_table['Install.Issu.Stage']['meta_info']
_meta_table['Install.Issu.Stage.NodesInRun']['meta_info'].parent =_meta_table['Install.Issu.Stage']['meta_info']
_meta_table['Install.Issu.Stage.NcNodes']['meta_info'].parent =_meta_table['Install.Issu.Stage']['meta_info']
_meta_table['Install.Issu.CardInventories']['meta_info'].parent =_meta_table['Install.Issu']['meta_info']
_meta_table['Install.Issu.Stage']['meta_info'].parent =_meta_table['Install.Issu']['meta_info']
_meta_table['Install.Logs.Log.Header.LogContents.V3.Scope']['meta_info'].parent =_meta_table['Install.Logs.Log.Header.LogContents.V3']['meta_info']
_meta_table['Install.Logs.Log.Header.LogContents.V3']['meta_info'].parent =_meta_table['Install.Logs.Log.Header.LogContents']['meta_info']
_meta_table['Install.Logs.Log.Header.LogContents']['meta_info'].parent =_meta_table['Install.Logs.Log.Header']['meta_info']
_meta_table['Install.Logs.Log.Summary.LogContents.V3.Scope']['meta_info'].parent =_meta_table['Install.Logs.Log.Summary.LogContents.V3']['meta_info']
_meta_table['Install.Logs.Log.Summary.LogContents.V3']['meta_info'].parent =_meta_table['Install.Logs.Log.Summary.LogContents']['meta_info']
_meta_table['Install.Logs.Log.Summary.LogContents']['meta_info'].parent =_meta_table['Install.Logs.Log.Summary']['meta_info']
_meta_table['Install.Logs.Log.Message.LogContents.V3.Scope']['meta_info'].parent =_meta_table['Install.Logs.Log.Message.LogContents.V3']['meta_info']
_meta_table['Install.Logs.Log.Message.LogContents.V3']['meta_info'].parent =_meta_table['Install.Logs.Log.Message.LogContents']['meta_info']
_meta_table['Install.Logs.Log.Message.LogContents']['meta_info'].parent =_meta_table['Install.Logs.Log.Message']['meta_info']
_meta_table['Install.Logs.Log.Change.LogContents.V3.Scope']['meta_info'].parent =_meta_table['Install.Logs.Log.Change.LogContents.V3']['meta_info']
_meta_table['Install.Logs.Log.Change.LogContents.V3']['meta_info'].parent =_meta_table['Install.Logs.Log.Change.LogContents']['meta_info']
_meta_table['Install.Logs.Log.Change.LogContents']['meta_info'].parent =_meta_table['Install.Logs.Log.Change']['meta_info']
_meta_table['Install.Logs.Log.Detail.LogContents.V3.Scope']['meta_info'].parent =_meta_table['Install.Logs.Log.Detail.LogContents.V3']['meta_info']
_meta_table['Install.Logs.Log.Detail.LogContents.V3']['meta_info'].parent =_meta_table['Install.Logs.Log.Detail.LogContents']['meta_info']
_meta_table['Install.Logs.Log.Detail.LogContents']['meta_info'].parent =_meta_table['Install.Logs.Log.Detail']['meta_info']
_meta_table['Install.Logs.Log.Communication.LogContents.V3.Scope']['meta_info'].parent =_meta_table['Install.Logs.Log.Communication.LogContents.V3']['meta_info']
_meta_table['Install.Logs.Log.Communication.LogContents.V3']['meta_info'].parent =_meta_table['Install.Logs.Log.Communication.LogContents']['meta_info']
_meta_table['Install.Logs.Log.Communication.LogContents']['meta_info'].parent =_meta_table['Install.Logs.Log.Communication']['meta_info']
_meta_table['Install.Logs.Log.Header']['meta_info'].parent =_meta_table['Install.Logs.Log']['meta_info']
_meta_table['Install.Logs.Log.Summary']['meta_info'].parent =_meta_table['Install.Logs.Log']['meta_info']
_meta_table['Install.Logs.Log.Message']['meta_info'].parent =_meta_table['Install.Logs.Log']['meta_info']
_meta_table['Install.Logs.Log.Change']['meta_info'].parent =_meta_table['Install.Logs.Log']['meta_info']
_meta_table['Install.Logs.Log.Detail']['meta_info'].parent =_meta_table['Install.Logs.Log']['meta_info']
_meta_table['Install.Logs.Log.Communication']['meta_info'].parent =_meta_table['Install.Logs.Log']['meta_info']
_meta_table['Install.Logs.Log']['meta_info'].parent =_meta_table['Install.Logs']['meta_info']
_meta_table['Install.ConfigurationRegisters']['meta_info'].parent =_meta_table['Install']['meta_info']
_meta_table['Install.RequestStatuses']['meta_info'].parent =_meta_table['Install']['meta_info']
_meta_table['Install.BootVariables']['meta_info'].parent =_meta_table['Install']['meta_info']
_meta_table['Install.Software']['meta_info'].parent =_meta_table['Install']['meta_info']
_meta_table['Install.SoftwareInventory']['meta_info'].parent =_meta_table['Install']['meta_info']
_meta_table['Install.Issu']['meta_info'].parent =_meta_table['Install']['meta_info']
_meta_table['Install.BootImage']['meta_info'].parent =_meta_table['Install']['meta_info']
_meta_table['Install.Logs']['meta_info'].parent =_meta_table['Install']['meta_info']
