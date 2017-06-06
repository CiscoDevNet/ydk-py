


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'InvPowerAdminStateEnum' : _MetaInfoEnum('InvPowerAdminStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'admin-power-invalid':'admin_power_invalid',
            'admin-on':'admin_on',
            'admin-off':'admin_off',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvCardStateEnum' : _MetaInfoEnum('InvCardStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'inv-card-not-present':'inv_card_not_present',
            'inv-card-present':'inv_card_present',
            'inv-card-reset':'inv_card_reset',
            'inv-card-booting':'inv_card_booting',
            'inv-card-mbi-booting':'inv_card_mbi_booting',
            'inv-card-running-mbi':'inv_card_running_mbi',
            'inv-card-running-ena':'inv_card_running_ena',
            'inv-card-bring-down':'inv_card_bring_down',
            'inv-card-ena-failure':'inv_card_ena_failure',
            'inv-card-f-diag-run':'inv_card_f_diag_run',
            'inv-card-f-diag-failure':'inv_card_f_diag_failure',
            'inv-card-powered':'inv_card_powered',
            'inv-card-unpowered':'inv_card_unpowered',
            'inv-card-mdr':'inv_card_mdr',
            'inv-card-mdr-running-mbi':'inv_card_mdr_running_mbi',
            'inv-card-main-t-mode':'inv_card_main_t_mode',
            'inv-card-admin-down':'inv_card_admin_down',
            'inv-card-no-mon':'inv_card_no_mon',
            'inv-card-unknown':'inv_card_unknown',
            'inv-card-failed':'inv_card_failed',
            'inv-card-ok':'inv_card_ok',
            'inv-card-missing':'inv_card_missing',
            'inv-card-field-diag-downloading':'inv_card_field_diag_downloading',
            'inv-card-field-diag-unmonitor':'inv_card_field_diag_unmonitor',
            'inv-card-fabric-field-diag-unmonitor':'inv_card_fabric_field_diag_unmonitor',
            'inv-card-field-diag-rp-launching':'inv_card_field_diag_rp_launching',
            'inv-card-field-diag-running':'inv_card_field_diag_running',
            'inv-card-field-diag-pass':'inv_card_field_diag_pass',
            'inv-card-field-diag-fail':'inv_card_field_diag_fail',
            'inv-card-field-diag-timeout':'inv_card_field_diag_timeout',
            'inv-card-disabled':'inv_card_disabled',
            'inv-card-spa-booting':'inv_card_spa_booting',
            'inv-card-not-allowed-online':'inv_card_not_allowed_online',
            'inv-card-stopped':'inv_card_stopped',
            'inv-card-incompatible-fw-ver':'inv_card_incompatible_fw_ver',
            'inv-card-fpd-hold':'inv_card_fpd_hold',
            'inv-card-node-prep':'inv_card_node_prep',
            'inv-card-updating-fpd':'inv_card_updating_fpd',
            'inv-card-num-states':'inv_card_num_states',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvMonitorStateEnum' : _MetaInfoEnum('InvMonitorStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'unmonitored':'unmonitored',
            'monitored':'monitored',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvAdminStateEnum' : _MetaInfoEnum('InvAdminStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'admin-state-invalid':'admin_state_invalid',
            'admin-up':'admin_up',
            'admin-down':'admin_down',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'InvResetReasonEnum' : _MetaInfoEnum('InvResetReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'module-reset-reason-unknown':'module_reset_reason_unknown',
            'module-reset-reason-powerup':'module_reset_reason_powerup',
            'module-reset-reason-user-shutdown':'module_reset_reason_user_shutdown',
            'module-reset-reason-user-reload':'module_reset_reason_user_reload',
            'module-reset-reason-auto-reload':'module_reset_reason_auto_reload',
            'module-reset-reason-environment':'module_reset_reason_environment',
            'module-reset-reason-user-unpower':'module_reset_reason_user_unpower',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'CardRedundancyStateEnum' : _MetaInfoEnum('CardRedundancyStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'active':'active',
            'standby':'standby',
        }, 'Cisco-IOS-XR-plat-chas-invmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper']),
    'NodeStateEnum' : _MetaInfoEnum('NodeStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper',
        {
            'not-present':'not_present',
            'present':'present',
            'reset':'reset',
            'rommon':'rommon',
            'mbi-boot':'mbi_boot',
            'mbi-run':'mbi_run',
            'xr-run':'xr_run',
            'bring-down':'bring_down',
            'xr-fail':'xr_fail',
            'fdiag-run':'fdiag_run',
            'fdiag-fail':'fdiag_fail',
            'power':'power',
            'unpower':'unpower',
            'mdr-warm-reload':'mdr_warm_reload',
            'mdr-mbi-run':'mdr_mbi_run',
            'maintenance-mode':'maintenance_mode',
            'admin-down':'admin_down',
            'not-monitor':'not_monitor',
            'unknown-card':'unknown_card',
            'failed':'failed',
            'ok':'ok',
            'missing':'missing',
            'diag-download':'diag_download',
            'diag-not-monitor':'diag_not_monitor',
            'fabric-diag-not-monitor':'fabric_diag_not_monitor',
            'diag-rp-launch':'diag_rp_launch',
            'diag-run':'diag_run',
            'diag-pass':'diag_pass',
            'diag-fail':'diag_fail',
            'diag-timeout':'diag_timeout',
            'disable':'disable',
            'spa-boot':'spa_boot',
            'not-allowed-online':'not_allowed_online',
            'stop':'stop',
            'incomp-version':'incomp_version',
            'fpd-hold':'fpd_hold',
            'xr-preparation':'xr_preparation',
            'sync-ready':'sync_ready',
            'xr-isolate':'xr_isolate',
            'ready':'ready',
            'invalid':'invalid',
            'operational':'operational',
            'operational-lock':'operational_lock',
            'going-down':'going_down',
            'going-offline':'going_offline',
            'going-online':'going_online',
            'offline':'offline',
            'up':'up',
            'down':'down',
            'max':'max',
            'unknown':'unknown',
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
            _MetaInfoClassMember('card-redundancy-state', REFERENCE_ENUM_CLASS, 'CardRedundancyStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'CardRedundancyStateEnum', 
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
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'NodeStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'NodeStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Instances.Instance.State', 
                [], [], 
                '''                State information
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots.Slot.Instances' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Instances.Instance', 
                [], [], 
                '''                Instance name
                ''',
                'instance',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'instances',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
            _MetaInfoClassMember('card-redundancy-state', REFERENCE_ENUM_CLASS, 'CardRedundancyStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'CardRedundancyStateEnum', 
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
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'NodeStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'NodeStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('slot-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Slot name
                ''',
                'slot_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Instances', 
                [], [], 
                '''                Table of Instances
                ''',
                'instances',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.State', 
                [], [], 
                '''                State information
                ''',
                'state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('vm', REFERENCE_CLASS, 'Vm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot.Vm', 
                [], [], 
                '''                VM information
                ''',
                'vm',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                Slot name
                ''',
                'slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('Platform.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('rack-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Rack name
                ''',
                'rack_name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack.Slots', 
                [], [], 
                '''                Table of slots
                ''',
                'slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform.Racks' : {
        'meta_info' : _MetaInfoClass('Platform.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks.Rack', 
                [], [], 
                '''                Rack name
                ''',
                'rack',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'Platform' : {
        'meta_info' : _MetaInfoClass('Platform',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'Platform.Racks', 
                [], [], 
                '''                Table of racks
                ''',
                'racks',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'platform',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash',
            False, 
            [
            _MetaInfoClassMember('bootflash-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                Sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'bootflash',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation',
            False, 
            [
            _MetaInfoClassMember('bootflash', REFERENCE_CLASS, 'Bootflash' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash', 
                [], [], 
                '''                Bootflash information
                ''',
                'bootflash',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('main-memory-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Memory size in bytes
                ''',
                'main_memory_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('nvram-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NVRAM size in bytes
                ''',
                'nvram_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('processor', REFERENCE_CLASS, 'Processor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor', 
                [], [], 
                '''                Processor information
                ''',
                'processor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('rom', REFERENCE_CLASS, 'Rom' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom', 
                [], [], 
                '''                ROM information
                ''',
                'rom',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'motherboard-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation',
            False, 
            [
            _MetaInfoClassMember('bootflash-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
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
                [('0', '4294967295')], [], 
                '''                Sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'bootflash-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
                [('0', '4294967295')], [], 
                '''                Disk size in mega-bytes
                ''',
                'disk_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sector-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disk sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'disks',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
                [('0', '4294967295')], [], 
                '''                (Deprecated) Disk size in mega-bytes
                ''',
                'disk_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('disks', REFERENCE_LIST, 'Disks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks', 
                [], [], 
                '''                Disk attributes
                ''',
                'disks',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sector-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                (Deprecated) Disk sector size in bytes
                ''',
                'sector_size',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'disk-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation',
            False, 
            [
            _MetaInfoClassMember('bootflash-information', REFERENCE_CLASS, 'BootflashInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation', 
                [], [], 
                '''                BootflashInformation
                ''',
                'bootflash_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('disk-information', REFERENCE_CLASS, 'DiskInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation', 
                [], [], 
                '''                DiskInformation
                ''',
                'disk_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('motherboard-information', REFERENCE_CLASS, 'MotherboardInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation', 
                [], [], 
                '''                MotherboardInformation
                ''',
                'motherboard_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('processor-information', REFERENCE_CLASS, 'ProcessorInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation', 
                [], [], 
                '''                ProcesorInformation
                ''',
                'processor_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hardware-information',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                HW component name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-component',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents',
            False, 
            [
            _MetaInfoClassMember('hw-component', REFERENCE_LIST, 'HwComponent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent', 
                [], [], 
                '''                HW component number
                ''',
                'hw_component',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-components',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hw-components', REFERENCE_CLASS, 'HwComponents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents', 
                [], [], 
                '''                Table of  HW components 
                ''',
                'hw_components',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'ports',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses',
            False, 
            [
            _MetaInfoClassMember('ports', REFERENCE_LIST, 'Ports' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports', 
                [], [], 
                '''                Port number
                ''',
                'ports',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'portses',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port slot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('portses', REFERENCE_CLASS, 'Portses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses', 
                [], [], 
                '''                Table of spirit port slots
                ''',
                'portses',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots',
            False, 
            [
            _MetaInfoClassMember('port-slot', REFERENCE_LIST, 'PortSlot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot', 
                [], [], 
                '''                Port slot number
                ''',
                'port_slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('port-slots', REFERENCE_CLASS, 'PortSlots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots', 
                [], [], 
                '''                Table of port slots
                ''',
                'port_slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Subslot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module', REFERENCE_CLASS, 'Module' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module', 
                [], [], 
                '''                Module of a subslot
                ''',
                'module',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sub-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots',
            False, 
            [
            _MetaInfoClassMember('sub-slot', REFERENCE_LIST, 'SubSlot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot', 
                [], [], 
                '''                Subslot number
                ''',
                'sub_slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sub-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                HW component name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-component',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents',
            False, 
            [
            _MetaInfoClassMember('hw-component', REFERENCE_LIST, 'HwComponent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent', 
                [], [], 
                '''                HW component number
                ''',
                'hw_component',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-components',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo',
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hw-components', REFERENCE_CLASS, 'HwComponents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents', 
                [], [], 
                '''                Table of  HW components 
                ''',
                'hw_components',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'ports',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses',
            False, 
            [
            _MetaInfoClassMember('ports', REFERENCE_LIST, 'Ports' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports', 
                [], [], 
                '''                Port number
                ''',
                'ports',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'portses',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port slot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('portses', REFERENCE_CLASS, 'Portses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses', 
                [], [], 
                '''                Table of spirit port slots
                ''',
                'portses',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots',
            False, 
            [
            _MetaInfoClassMember('port-slot', REFERENCE_LIST, 'PortSlot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot', 
                [], [], 
                '''                Port slot number
                ''',
                'port_slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'port-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                HW component name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-component',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents',
            False, 
            [
            _MetaInfoClassMember('hw-component', REFERENCE_LIST, 'HwComponent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent', 
                [], [], 
                '''                HW component number
                ''',
                'hw_component',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'hw-components',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor', 
                [], [], 
                '''                Sensor number
                ''',
                'sensor',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Card name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hardware-information', REFERENCE_CLASS, 'HardwareInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation', 
                [], [], 
                '''                HardwareInformationDir
                ''',
                'hardware_information',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('hw-components', REFERENCE_CLASS, 'HwComponents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents', 
                [], [], 
                '''                Table of  HW components 
                ''',
                'hw_components',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('port-slots', REFERENCE_CLASS, 'PortSlots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots', 
                [], [], 
                '''                Table of port slots
                ''',
                'port_slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensors',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('sub-slots', REFERENCE_CLASS, 'SubSlots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots', 
                [], [], 
                '''                Table of subslots
                ''',
                'sub_slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'card',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Cards' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Cards',
            False, 
            [
            _MetaInfoClassMember('card', REFERENCE_LIST, 'Card' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card', 
                [], [], 
                '''                Card number
                ''',
                'card',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'cards',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Slot name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('cards', REFERENCE_CLASS, 'Cards' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot.Cards', 
                [], [], 
                '''                Table of cards
                ''',
                'cards',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                Slot name
                ''',
                'slot',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'module-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                Time operational state is   last changed
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-administrative-state', REFERENCE_ENUM_CLASS, 'InvAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvAdminStateEnum', 
                [], [], 
                '''                Administrative    state
                ''',
                'module_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-monitor-state', REFERENCE_ENUM_CLASS, 'InvMonitorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvMonitorStateEnum', 
                [], [], 
                '''                Monitor state
                ''',
                'module_monitor_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Operation state
                ''',
                'module_operational_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-power-administrative-state', REFERENCE_ENUM_CLASS, 'InvPowerAdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvPowerAdminStateEnum', 
                [], [], 
                '''                Power administrative state
                ''',
                'module_power_administrative_state',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-reset-reason', REFERENCE_ENUM_CLASS, 'InvResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'InvResetReasonEnum', 
                [], [], 
                '''                Reset reason
                ''',
                'module_reset_reason',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('module-up-time', REFERENCE_CLASS, 'ModuleUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime', 
                [], [], 
                '''                Module up time
                ''',
                'module_up_time',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack.Attributes' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack.Attributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.BasicInfo', 
                [], [], 
                '''                Entity attributes
                ''',
                'basic_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) attributes
                ''',
                'fru_info',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Rack name
                ''',
                'name',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', True),
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Attributes', 
                [], [], 
                '''                Attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack.Slots', 
                [], [], 
                '''                Table of slots
                ''',
                'slots',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory.Racks' : {
        'meta_info' : _MetaInfoClass('PlatformInventory.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks.Rack', 
                [], [], 
                '''                Rack name
                ''',
                'rack',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
    'PlatformInventory' : {
        'meta_info' : _MetaInfoClass('PlatformInventory',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper', 'PlatformInventory.Racks', 
                [], [], 
                '''                Table of racks
                ''',
                'racks',
                'Cisco-IOS-XR-plat-chas-invmgr-oper', False),
            ],
            'Cisco-IOS-XR-plat-chas-invmgr-oper',
            'platform-inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-plat-chas-invmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_plat_chas_invmgr_oper'
        ),
    },
}
_meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance.State']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot.Instances']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.Instances']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.Vm']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot.State']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Platform.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['Platform.Racks.Rack.Slots']['meta_info']
_meta_table['Platform.Racks.Rack.Slots']['meta_info'].parent =_meta_table['Platform.Racks.Rack']['meta_info']
_meta_table['Platform.Racks.Rack']['meta_info'].parent =_meta_table['Platform.Racks']['meta_info']
_meta_table['Platform.Racks']['meta_info'].parent =_meta_table['Platform']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Rom']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Bootflash']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation.Processor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation.Disks']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.ProcessorInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.MotherboardInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.BootflashInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation.DiskInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.HwComponents']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses.Ports']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Portses']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents.HwComponent']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.HwComponents']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses.Ports']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Portses']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HardwareInformation']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Cards']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Slots']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo.ModuleUpTime']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.BasicInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes.FruInfo']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack.Attributes']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Slots']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack']['meta_info']
_meta_table['PlatformInventory.Racks.Rack.Attributes']['meta_info'].parent =_meta_table['PlatformInventory.Racks.Rack']['meta_info']
_meta_table['PlatformInventory.Racks.Rack']['meta_info'].parent =_meta_table['PlatformInventory.Racks']['meta_info']
_meta_table['PlatformInventory.Racks']['meta_info'].parent =_meta_table['PlatformInventory']['meta_info']
