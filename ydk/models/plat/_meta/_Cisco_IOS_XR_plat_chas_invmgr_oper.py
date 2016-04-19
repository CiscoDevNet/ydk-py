


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'InvAdminStateEnum' : _MetaInfoEnum('InvAdminStateEnum', 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'admin-state-invalid':'ADMIN_STATE_INVALID',
            'admin-up':'ADMIN_UP',
            'admin-down':'ADMIN_DOWN',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvResetReasonEnum' : _MetaInfoEnum('InvResetReasonEnum', 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'module-reset-reason-unknown':'MODULE_RESET_REASON_UNKNOWN',
            'module-reset-reason-powerup':'MODULE_RESET_REASON_POWERUP',
            'module-reset-reason-user-shutdown':'MODULE_RESET_REASON_USER_SHUTDOWN',
            'module-reset-reason-user-reload':'MODULE_RESET_REASON_USER_RELOAD',
            'module-reset-reason-auto-reload':'MODULE_RESET_REASON_AUTO_RELOAD',
            'module-reset-reason-environment':'MODULE_RESET_REASON_ENVIRONMENT',
            'module-reset-reason-user-unpower':'MODULE_RESET_REASON_USER_UNPOWER',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvCardStateEnum' : _MetaInfoEnum('InvCardStateEnum', 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'inv-card-not-present':'INV_CARD_NOT_PRESENT',
            'inv-card-present':'INV_CARD_PRESENT',
            'inv-card-reset':'INV_CARD_RESET',
            'inv-card-booting':'INV_CARD_BOOTING',
            'inv-card-mbi-booting':'INV_CARD_MBI_BOOTING',
            'inv-card-running-mbi':'INV_CARD_RUNNING_MBI',
            'inv-card-running-ena':'INV_CARD_RUNNING_ENA',
            'inv-card-bring-down':'INV_CARD_BRING_DOWN',
            'inv-card-ena-failure':'INV_CARD_ENA_FAILURE',
            'inv-card-f-diag-run':'INV_CARD_F_DIAG_RUN',
            'inv-card-f-diag-failure':'INV_CARD_F_DIAG_FAILURE',
            'inv-card-powered':'INV_CARD_POWERED',
            'inv-card-unpowered':'INV_CARD_UNPOWERED',
            'inv-card-mdr':'INV_CARD_MDR',
            'inv-card-mdr-running-mbi':'INV_CARD_MDR_RUNNING_MBI',
            'inv-card-main-t-mode':'INV_CARD_MAIN_T_MODE',
            'inv-card-admin-down':'INV_CARD_ADMIN_DOWN',
            'inv-card-no-mon':'INV_CARD_NO_MON',
            'inv-card-unknown':'INV_CARD_UNKNOWN',
            'inv-card-failed':'INV_CARD_FAILED',
            'inv-card-ok':'INV_CARD_OK',
            'inv-card-missing':'INV_CARD_MISSING',
            'inv-card-field-diag-downloading':'INV_CARD_FIELD_DIAG_DOWNLOADING',
            'inv-card-field-diag-unmonitor':'INV_CARD_FIELD_DIAG_UNMONITOR',
            'inv-card-fabric-field-diag-unmonitor':'INV_CARD_FABRIC_FIELD_DIAG_UNMONITOR',
            'inv-card-field-diag-rp-launching':'INV_CARD_FIELD_DIAG_RP_LAUNCHING',
            'inv-card-field-diag-running':'INV_CARD_FIELD_DIAG_RUNNING',
            'inv-card-field-diag-pass':'INV_CARD_FIELD_DIAG_PASS',
            'inv-card-field-diag-fail':'INV_CARD_FIELD_DIAG_FAIL',
            'inv-card-field-diag-timeout':'INV_CARD_FIELD_DIAG_TIMEOUT',
            'inv-card-disabled':'INV_CARD_DISABLED',
            'inv-card-spa-booting':'INV_CARD_SPA_BOOTING',
            'inv-card-not-allowed-online':'INV_CARD_NOT_ALLOWED_ONLINE',
            'inv-card-stopped':'INV_CARD_STOPPED',
            'inv-card-incompatible-fw-ver':'INV_CARD_INCOMPATIBLE_FW_VER',
            'inv-card-fpd-hold':'INV_CARD_FPD_HOLD',
            'inv-card-node-prep':'INV_CARD_NODE_PREP',
            'inv-card-updating-fpd':'INV_CARD_UPDATING_FPD',
            'inv-card-num-states':'INV_CARD_NUM_STATES',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvMonitorStateEnum' : _MetaInfoEnum('InvMonitorStateEnum', 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'unmonitored':'UNMONITORED',
            'monitored':'MONITORED',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'NodeStateEnum' : _MetaInfoEnum('NodeStateEnum', 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'not-present':'NOT_PRESENT',
            'present':'PRESENT',
            'reset':'RESET',
            'rommon':'ROMMON',
            'mbi-boot':'MBI_BOOT',
            'mbi-run':'MBI_RUN',
            'xr-run':'XR_RUN',
            'bring-down':'BRING_DOWN',
            'xr-fail':'XR_FAIL',
            'fdiag-run':'FDIAG_RUN',
            'fdiag-fail':'FDIAG_FAIL',
            'power':'POWER',
            'unpower':'UNPOWER',
            'mdr-warm-reload':'MDR_WARM_RELOAD',
            'mdr-mbi-run':'MDR_MBI_RUN',
            'maintenance-mode':'MAINTENANCE_MODE',
            'admin-down':'ADMIN_DOWN',
            'not-monitor':'NOT_MONITOR',
            'unknown-card':'UNKNOWN_CARD',
            'failed':'FAILED',
            'ok':'OK',
            'missing':'MISSING',
            'diag-download':'DIAG_DOWNLOAD',
            'diag-not-monitor':'DIAG_NOT_MONITOR',
            'fabric-diag-not-monitor':'FABRIC_DIAG_NOT_MONITOR',
            'diag-rp-launch':'DIAG_RP_LAUNCH',
            'diag-run':'DIAG_RUN',
            'diag-pass':'DIAG_PASS',
            'diag-fail':'DIAG_FAIL',
            'diag-timeout':'DIAG_TIMEOUT',
            'disable':'DISABLE',
            'spa-boot':'SPA_BOOT',
            'not-allowed-online':'NOT_ALLOWED_ONLINE',
            'stop':'STOP',
            'incomp-version':'INCOMP_VERSION',
            'fpd-hold':'FPD_HOLD',
            'xr-preparation':'XR_PREPARATION',
            'sync-ready':'SYNC_READY',
            'xr-isolate':'XR_ISOLATE',
            'ready':'READY',
            'invalid':'INVALID',
            'operational':'OPERATIONAL',
            'operational-lock':'OPERATIONAL_LOCK',
            'going-down':'GOING_DOWN',
            'going-offline':'GOING_OFFLINE',
            'going-online':'GOING_ONLINE',
            'offline':'OFFLINE',
            'up':'UP',
            'down':'DOWN',
            'max':'MAX',
            'unknown':'UNKNOWN',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'CardRedundancyStateEnum' : _MetaInfoEnum('CardRedundancyStateEnum', 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'active':'ACTIVE',
            'standby':'STANDBY',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvPowerAdminStateEnum' : _MetaInfoEnum('InvPowerAdminStateEnum', 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'admin-power-invalid':'ADMIN_POWER_INVALID',
            'admin-on':'ADMIN_ON',
            'admin-off':'ADMIN_OFF',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'Platform.Racks.Rack.Slots.Slot.Instances.Instance.State' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot.Instances.Instance.State',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('card-redundancy-state', REFERENCE_ENUM_CLASS, 'CardRedundancyStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'CardRedundancyStateEnum', 
                [], [], 
                '''                Redundancy state
                ''',
                'card_redundancy_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Card type
                ''',
                'card_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-monitored', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if power state is active
                ''',
                'is_monitored',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-powered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if monitor state is active
                ''',
                'is_powered',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if shutdown state is active
                ''',
                'is_shutdown',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('plim', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PLIM
                ''',
                'plim',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'NodeStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'NodeStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots.Slot.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot.Instances.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance name
                ''',
                'instance_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Instances.Instance.State', 
                [], [], 
                '''                State information
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots.Slot.Instances' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Instances.Instance', 
                [], [], 
                '''                Instance name
                ''',
                'instance',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'instances',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots.Slot.State' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot.State',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('card-redundancy-state', REFERENCE_ENUM_CLASS, 'CardRedundancyStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'CardRedundancyStateEnum', 
                [], [], 
                '''                Redundancy state
                ''',
                'card_redundancy_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Card type
                ''',
                'card_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-monitored', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if power state is active
                ''',
                'is_monitored',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-powered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if monitor state is active
                ''',
                'is_powered',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if shutdown state is active
                ''',
                'is_shutdown',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('plim', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PLIM
                ''',
                'plim',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'NodeStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'NodeStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots.Slot.Vm' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot.Vm',
            False, 
            [
            _MetaInfoClassMember('node-descriptiton', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Type
                ''',
                'node_descriptiton',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('node-ip', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node IP Address
                ''',
                'node_ip',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('partner-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Partner Name
                ''',
                'partner_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('red-role', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Redundency Role
                ''',
                'red_role',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SW status
                ''',
                'software_status',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'vm',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('slot-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Slot name
                ''',
                'slot_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Instances', 
                [], [], 
                '''                Table of Instances
                ''',
                'instances',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.State', 
                [], [], 
                '''                State information
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vm', REFERENCE_CLASS, 'Vm' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Vm', 
                [], [], 
                '''                VM information
                ''',
                'vm',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                Slot name
                ''',
                'slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('rack-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Rack name
                ''',
                'rack_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots', 
                [], [], 
                '''                Table of slots
                ''',
                'slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks' : {
        'meta_info' : _MetaInfoClass('Platform.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack', 
                [], [], 
                '''                Rack name
                ''',
                'rack',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform' : {
        'meta_info' : _MetaInfoClass('Platform',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks', 
                [], [], 
                '''                Table of racks
                ''',
                'racks',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'platform',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation',
            False, 
            [
            _MetaInfoClassMember('bootflash-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Bootflash size in kilo-bytes
                ''',
                'bootflash_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('bootflash-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Bootflash type e.g. SIMM
                ''',
                'bootflash_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('image-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Image name
                ''',
                'image_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('major-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Major version
                ''',
                'major_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('micro-image-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Micro image version
                ''',
                'micro_image_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('minor-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minor version
                ''',
                'minor_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('platform-specific', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Platform specific text
                ''',
                'platform_specific',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('platform-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Platform Type
                ''',
                'platform_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('release-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Release type
                ''',
                'release_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sector-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'bootflash-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks',
            False, 
            [
            _MetaInfoClassMember('disk-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Disk name
                ''',
                'disk_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('disk-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Disk size in mega-bytes
                ''',
                'disk_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sector-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Disk sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'disks',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation',
            False, 
            [
            _MetaInfoClassMember('disk-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                (Deprecated) Disk name
                ''',
                'disk_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('disk-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                (Deprecated) Disk size in mega-bytes
                ''',
                'disk_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('disks', REFERENCE_LIST, 'Disks' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks', 
                [], [], 
                '''                Disk attributes
                ''',
                'disks',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sector-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                (Deprecated) Disk sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'disk-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash',
            False, 
            [
            _MetaInfoClassMember('bootflash-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Bootflash size in kilo-bytes
                ''',
                'bootflash_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('bootflash-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Bootflash type e.g. SIMM
                ''',
                'bootflash_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('image-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Image name
                ''',
                'image_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('major-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Major version
                ''',
                'major_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('micro-image-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Micro image version
                ''',
                'micro_image_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('minor-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minor version
                ''',
                'minor_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('platform-specific', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Platform specific text
                ''',
                'platform_specific',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('platform-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Platform Type
                ''',
                'platform_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('release-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Release type
                ''',
                'release_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sector-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'bootflash',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor',
            False, 
            [
            _MetaInfoClassMember('processor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Type e.g. 7457
                ''',
                'processor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Revision. e.g 1.1
                ''',
                'revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Speed e.g. 1197Mhz
                ''',
                'speed',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'processor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom',
            False, 
            [
            _MetaInfoClassMember('image-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Image name
                ''',
                'image_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('major-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Major version
                ''',
                'major_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('micro-image-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Micro image version
                ''',
                'micro_image_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('minor-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Minor version
                ''',
                'minor_version',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('platform-specific', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Platform specific text
                ''',
                'platform_specific',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('release-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Release type
                ''',
                'release_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'rom',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation',
            False, 
            [
            _MetaInfoClassMember('bootflash', REFERENCE_CLASS, 'Bootflash' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash', 
                [], [], 
                '''                Bootflash information
                ''',
                'bootflash',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('main-memory-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Memory size in bytes
                ''',
                'main_memory_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('nvram-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                NVRAM size in bytes
                ''',
                'nvram_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('processor', REFERENCE_CLASS, 'Processor' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor', 
                [], [], 
                '''                Processor information
                ''',
                'processor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('rom', REFERENCE_CLASS, 'Rom' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom', 
                [], [], 
                '''                ROM information
                ''',
                'rom',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'motherboard-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation',
            False, 
            [
            _MetaInfoClassMember('processor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Type e.g. 7457
                ''',
                'processor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Revision. e.g 1.1
                ''',
                'revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Speed e.g. 1197Mhz
                ''',
                'speed',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'processor-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation',
            False, 
            [
            _MetaInfoClassMember('bootflash-information', REFERENCE_CLASS, 'BootflashInformation' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation', 
                [], [], 
                '''                BootflashInformation
                ''',
                'bootflash_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('disk-information', REFERENCE_CLASS, 'DiskInformation' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation', 
                [], [], 
                '''                DiskInformation
                ''',
                'disk_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('motherboard-information', REFERENCE_CLASS, 'MotherboardInformation' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation', 
                [], [], 
                '''                MotherboardInformation
                ''',
                'motherboard_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('processor-information', REFERENCE_CLASS, 'ProcessorInformation' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation', 
                [], [], 
                '''                ProcesorInformation
                ''',
                'processor_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hardware-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                HW component name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-component',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents',
            False, 
            [
            _MetaInfoClassMember('hw-component', REFERENCE_LIST, 'HwComponent' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent', 
                [], [], 
                '''                HW component number
                ''',
                'hw_component',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-components',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port slot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('port', REFERENCE_CLASS, 'Port' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port', 
                [], [], 
                '''                Port
                ''',
                'port',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots',
            False, 
            [
            _MetaInfoClassMember('port-slot', REFERENCE_LIST, 'PortSlot' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot', 
                [], [], 
                '''                Port slot number
                ''',
                'port_slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'ports',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses',
            False, 
            [
            _MetaInfoClassMember('ports', REFERENCE_LIST, 'Ports' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports', 
                [], [], 
                '''                Port number
                ''',
                'ports',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'portses',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port slot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('port', REFERENCE_CLASS, 'Port' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port', 
                [], [], 
                '''                Port
                ''',
                'port',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots',
            False, 
            [
            _MetaInfoClassMember('port-slot', REFERENCE_LIST, 'PortSlot' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot', 
                [], [], 
                '''                Port slot number
                ''',
                'port_slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms                
                what the entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('port-slots', REFERENCE_CLASS, 'PortSlots' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots', 
                [], [], 
                '''                Table of port slots
                ''',
                'port_slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Subslot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module', REFERENCE_CLASS, 'Module' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module', 
                [], [], 
                '''                Module of a subslot
                ''',
                'module',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sub-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots',
            False, 
            [
            _MetaInfoClassMember('sub-slot', REFERENCE_LIST, 'SubSlot' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot', 
                [], [], 
                '''                Subslot number
                ''',
                'sub_slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sub-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Card name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-information', REFERENCE_CLASS, 'HardwareInformation' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation', 
                [], [], 
                '''                HardwareInformationDir
                ''',
                'hardware_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hw-components', REFERENCE_CLASS, 'HwComponents' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents', 
                [], [], 
                '''                Table of  HW components 
                ''',
                'hw_components',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('port-slots', REFERENCE_CLASS, 'PortSlots' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots', 
                [], [], 
                '''                Table of port slots
                ''',
                'port_slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('portses', REFERENCE_CLASS, 'Portses' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses', 
                [], [], 
                '''                Table of spirit port slots
                ''',
                'portses',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sub-slots', REFERENCE_CLASS, 'SubSlots' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots', 
                [], [], 
                '''                Table of subslots
                ''',
                'sub_slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'card',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards',
            False, 
            [
            _MetaInfoClassMember('card', REFERENCE_LIST, 'Card' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card', 
                [], [], 
                '''                Card number
                ''',
                'card',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'cards',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Slot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('cards', REFERENCE_CLASS, 'Cards' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards', 
                [], [], 
                '''                Table of cards
                ''',
                'cards',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                Slot name
                ''',
                'slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Rack name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots', 
                [], [], 
                '''                Table of slots
                ''',
                'slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack', 
                [], [], 
                '''                Rack name
                ''',
                'rack',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory' : {
        'meta_info' : _MetaInfoClass('PlatformInventory',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks', 
                [], [], 
                '''                Table of racks
                ''',
                'racks',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'platform-inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.plat.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
}
_meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance.State']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot.Instances']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.Instances']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.State']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.Vm']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots']['meta_info']
_meta_table['Platform.Racks.Rack.Slots']['meta_info'].parent =_meta_table['Platform.Racks.Rack']['meta_info']
_meta_table['Platform.Racks.Rack']['meta_info'].parent =_meta_table['Platform.Racks']['meta_info']
_meta_table['Platform.Racks']['meta_info'].parent =_meta_table['Platform']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses.Ports']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Portses']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack']['meta_info']
_meta_table['PlatformInventory.Racks.Rack']['meta_info'].parent =_meta_table['PlatformInventory.Racks']['meta_info']
_meta_table['PlatformInventory.Racks']['meta_info'].parent =_meta_table['PlatformInventory']['meta_info']
