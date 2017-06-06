


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LinkErrorStateEnum' : _MetaInfoEnum('LinkErrorStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'link-error-unset':'link_error_unset',
            'link-error-none':'link_error_none',
            'link-error-shut':'link_error_shut',
            'link-error-max':'link_error_max',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'AsicEnum' : _MetaInfoEnum('AsicEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'asic-unset':'asic_unset',
            'asic-unavail':'asic_unavail',
            'asic-fia':'asic_fia',
            'asic-s123':'asic_s123',
            'asic-s13':'asic_s13',
            'asic-s2':'asic_s2',
            'asic-b2b':'asic_b2b',
            'asic-type-unknown':'asic_type_unknown',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'AsicInitMethodEnum' : _MetaInfoEnum('AsicInitMethodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'asic-init-method-unset':'asic_init_method_unset',
            'asic-init-method-no-reset':'asic_init_method_no_reset',
            'asic-init-method-pon-reset':'asic_init_method_pon_reset',
            'asic-init-method-pon-reset-on-intr':'asic_init_method_pon_reset_on_intr',
            'asic-init-method-hard-reset':'asic_init_method_hard_reset',
            'asic-init-method-warmboot':'asic_init_method_warmboot',
            'asic-init-method-issu-wb':'asic_init_method_issu_wb',
            'asic-init-method-pci-shutdown':'asic_init_method_pci_shutdown',
            'asic-init-method-quiesce':'asic_init_method_quiesce',
            'asic-init-method-issu-started':'asic_init_method_issu_started',
            'asic-init-method-issu-rollback':'asic_init_method_issu_rollback',
            'asic-init-method-issu-abort':'asic_init_method_issu_abort',
            'asic-init-method-slice-cleanup':'asic_init_method_slice_cleanup',
            'asic-init-method-lc-remove':'asic_init_method_lc_remove',
            'asic-init-method-node-down':'asic_init_method_node_down',
            'asic-init-method-intr':'asic_init_method_intr',
            'asic-init-method-board-reload':'asic_init_method_board_reload',
            'asic-init-method-max':'asic_init_method_max',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'RackEnum' : _MetaInfoEnum('RackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'rack-type-unset':'rack_type_unset',
            'rack-type-lcc':'rack_type_lcc',
            'rack-type-fcc':'rack_type_fcc',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'LinkEnum' : _MetaInfoEnum('LinkEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'link-type-unset':'link_type_unset',
            'link-type-unavail':'link_type_unavail',
            'link-type-tx':'link_type_tx',
            'link-type-rx':'link_type_rx',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'FcModeEnum' : _MetaInfoEnum('FcModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'fc-mode-unset':'fc_mode_unset',
            'fc-mode-unavail':'fc_mode_unavail',
            'fc-mode-inband':'fc_mode_inband',
            'fc-mode-oob':'fc_mode_oob',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'AsicOperStateEnum' : _MetaInfoEnum('AsicOperStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'asic-oper-unset':'asic_oper_unset',
            'asic-oper-unknown':'asic_oper_unknown',
            'asic-oper-up':'asic_oper_up',
            'asic-oper-down':'asic_oper_down',
            'asic-card-down':'asic_card_down',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'AdminStateEnum' : _MetaInfoEnum('AdminStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'admin-unset':'admin_unset',
            'admin-up':'admin_up',
            'admin-down':'admin_down',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'LinkStageEnum' : _MetaInfoEnum('LinkStageEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'link-stage-unset':'link_stage_unset',
            'link-stage-unused':'link_stage_unused',
            'link-stage-fia':'link_stage_fia',
            'link-stage-s1':'link_stage_s1',
            'link-stage-s2':'link_stage_s2',
            'link-stage-s3':'link_stage_s3',
            'link-stage-unknown':'link_stage_unknown',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'AsicAccessStateEnum' : _MetaInfoEnum('AsicAccessStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'asic-state-unset':'asic_state_unset',
            'asic-state-none':'asic_state_none',
            'asic-state-device-off-line':'asic_state_device_off_line',
            'asic-state-device-created':'asic_state_device_created',
            'asic-state-device-online':'asic_state_device_online',
            'asic-state-warmboot':'asic_state_warmboot',
            'asic-state-de-init-start':'asic_state_de_init_start',
            'asic-state-intr-de-init':'asic_state_intr_de_init',
            'asic-state-bcm-detach':'asic_state_bcm_detach',
            'asic-state-soc-de-init':'asic_state_soc_de_init',
            'asic-state-de-init-done':'asic_state_de_init_done',
            'asic-state-soc-init':'asic_state_soc_init',
            'asic-state-bcm-init':'asic_state_bcm_init',
            'asic-state-intr-init':'asic_state_intr_init',
            'asic-state-soc-init-start':'asic_state_soc_init_start',
            'asic-state-bcm-init-start':'asic_state_bcm_init_start',
            'asic-state-intr-init-start':'asic_state_intr_init_start',
            'asic-state-hard-reset':'asic_state_hard_reset',
            'asic-state-normal':'asic_state_normal',
            'asic-state-exception':'asic_state_exception',
            'asic-state-hp-attached':'asic_state_hp_attached',
            'asic-state-quiesce':'asic_state_quiesce',
            'asic-state-issu-started':'asic_state_issu_started',
            'asic-state-issu-started-nn':'asic_state_issu_started_nn',
            'asic-state-issu-abort':'asic_state_issu_abort',
            'asic-state-max':'asic_state_max',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'OperStateEnum' : _MetaInfoEnum('OperStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'oper-unset':'oper_unset',
            'oper-unknown':'oper_unknown',
            'oper-up':'oper_up',
            'oper-down':'oper_down',
            'card-down':'card_down',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'SliceStateEnum' : _MetaInfoEnum('SliceStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper',
        {
            'slice-oper-unset':'slice_oper_unset',
            'slice-oper-down':'slice_oper_down',
            'slice-oper-up':'slice_oper_up',
            'slice-oper-na':'slice_oper_na',
        }, 'Cisco-IOS-XR-dnx-driver-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper']),
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', REFERENCE_ENUM_CLASS, 'AsicEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicEnum', 
                [], [], 
                '''                Asic Type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', REFERENCE_ENUM_CLASS, 'RackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'RackEnum', 
                [], [], 
                '''                Rack Type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', REFERENCE_ENUM_CLASS, 'LinkStageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStageEnum', 
                [], [], 
                '''                Link Stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', REFERENCE_ENUM_CLASS, 'LinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkEnum', 
                [], [], 
                '''                Link Type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'this-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', REFERENCE_ENUM_CLASS, 'AsicEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicEnum', 
                [], [], 
                '''                Asic Type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', REFERENCE_ENUM_CLASS, 'RackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'RackEnum', 
                [], [], 
                '''                Rack Type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', REFERENCE_ENUM_CLASS, 'LinkStageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStageEnum', 
                [], [], 
                '''                Link Stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', REFERENCE_ENUM_CLASS, 'LinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkEnum', 
                [], [], 
                '''                Link Type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'far-end-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', REFERENCE_ENUM_CLASS, 'AsicEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicEnum', 
                [], [], 
                '''                Asic Type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', REFERENCE_ENUM_CLASS, 'RackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'RackEnum', 
                [], [], 
                '''                Rack Type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', REFERENCE_ENUM_CLASS, 'LinkStageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStageEnum', 
                [], [], 
                '''                Link Stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', REFERENCE_ENUM_CLASS, 'LinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkEnum', 
                [], [], 
                '''                Link Type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'far-end-link-in-hw',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist',
            False, 
            [
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminStateEnum', 
                [], [], 
                '''                Admin State
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', REFERENCE_ENUM_CLASS, 'LinkErrorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorStateEnum', 
                [], [], 
                '''                Error State
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', REFERENCE_ENUM_CLASS, 'OperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperStateEnum', 
                [], [], 
                '''                Oper State
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reasons', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reasons
                ''',
                'reasons',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                timestamp
                ''',
                'timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'hist',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History',
            False, 
            [
            _MetaInfoClassMember('hist', REFERENCE_LIST, 'Hist' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist', 
                [], [], 
                '''                hist
                ''',
                'hist',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=5),
            _MetaInfoClassMember('histnum', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                histnum
                ''',
                'histnum',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                start index
                ''',
                'start_index',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_',
            False, 
            [
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Single link
                ''',
                'link',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminStateEnum', 
                [], [], 
                '''                Admin State
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('correctable-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                correctable errors
                ''',
                'correctable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', REFERENCE_ENUM_CLASS, 'LinkErrorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorStateEnum', 
                [], [], 
                '''                Error State
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('far-end-link', REFERENCE_CLASS, 'FarEndLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink', 
                [], [], 
                '''                far end link
                ''',
                'far_end_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('far-end-link-in-hw', REFERENCE_CLASS, 'FarEndLinkInHw' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw', 
                [], [], 
                '''                far end link in hw
                ''',
                'far_end_link_in_hw',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                flags
                ''',
                'flags',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('flap-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                flap cnt
                ''',
                'flap_cnt',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History', 
                [], [], 
                '''                history
                ''',
                'history',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-conf-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is conf pending
                ''',
                'is_conf_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-link-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is link valid
                ''',
                'is_link_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-admin-shuts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num admin shuts
                ''',
                'num_admin_shuts',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', REFERENCE_ENUM_CLASS, 'OperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperStateEnum', 
                [], [], 
                '''                Oper State
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                speed
                ''',
                'speed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('stage', REFERENCE_ENUM_CLASS, 'LinkStageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStageEnum', 
                [], [], 
                '''                Stage
                ''',
                'stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('this-link', REFERENCE_CLASS, 'ThisLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink', 
                [], [], 
                '''                this link
                ''',
                'this_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('uncorrectable-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                uncorrectable errors
                ''',
                'uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink',
            False, 
            [
            _MetaInfoClassMember('end-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '47')], [], 
                '''                End number
                ''',
                'end_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-link', REFERENCE_LIST, 'RxLink_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_', 
                [], [], 
                '''                Single link information
                ''',
                'rx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '47')], [], 
                '''                Start number
                ''',
                'start_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('status-option', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                RX link status option
                ''',
                'status_option',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks',
            False, 
            [
            _MetaInfoClassMember('rx-link', REFERENCE_LIST, 'RxLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink', 
                [], [], 
                '''                Link number for rx link information
                ''',
                'rx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-links',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance',
            False, 
            [
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Receive instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('rx-links', REFERENCE_CLASS, 'RxLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks', 
                [], [], 
                '''                Link table class for rx information
                ''',
                'rx_links',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances',
            False, 
            [
            _MetaInfoClassMember('rx-asic-instance', REFERENCE_LIST, 'RxAsicInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance', 
                [], [], 
                '''                Instance number for rx link information
                ''',
                'rx_asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption',
            False, 
            [
            _MetaInfoClassMember('option', ATTRIBUTE, 'str' , None, None, 
                [], [b'(flap)|(topo)'], 
                '''                Link option
                ''',
                'option',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('rx-asic-instances', REFERENCE_CLASS, 'RxAsicInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances', 
                [], [], 
                '''                Instance table for rx information
                ''',
                'rx_asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-option',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions',
            False, 
            [
            _MetaInfoClassMember('link-option', REFERENCE_LIST, 'LinkOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption', 
                [], [], 
                '''                Option : topo , flag , stats
                ''',
                'link_option',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-options',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation',
            False, 
            [
            _MetaInfoClassMember('link-options', REFERENCE_CLASS, 'LinkOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions', 
                [], [], 
                '''                Option table for link rx information
                ''',
                'link_options',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', REFERENCE_ENUM_CLASS, 'AsicEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicEnum', 
                [], [], 
                '''                Asic Type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', REFERENCE_ENUM_CLASS, 'RackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'RackEnum', 
                [], [], 
                '''                Rack Type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.DeviceInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.DeviceInfo',
            False, 
            [
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminStateEnum', 
                [], [], 
                '''                Admin State
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-state', REFERENCE_ENUM_CLASS, 'AsicAccessStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicAccessStateEnum', 
                [], [], 
                '''                Asic State
                ''',
                'asic_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fapid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                fapid
                ''',
                'fapid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('hotplug-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                hotplug event
                ''',
                'hotplug_event',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-init-cause', REFERENCE_ENUM_CLASS, 'AsicInitMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicInitMethodEnum', 
                [], [], 
                '''                last init cause
                ''',
                'last_init_cause',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('local-switch-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                local switch state
                ''',
                'local_switch_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-hard-resets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num hard resets
                ''',
                'num_hard_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pon-resets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num pon resets
                ''',
                'num_pon_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', REFERENCE_ENUM_CLASS, 'AsicOperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicOperStateEnum', 
                [], [], 
                '''                Oper State
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slice-state', REFERENCE_ENUM_CLASS, 'SliceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'SliceStateEnum', 
                [], [], 
                '''                Slice State
                ''',
                'slice_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'device-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo',
            False, 
            [
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cur-card-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                cur card state
                ''',
                'cur_card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fia-oir-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                count
                ''',
                'count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fia-oir-info', REFERENCE_LIST, 'FiaOirInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo', 
                [], [], 
                '''                fia oir info
                ''',
                'fia_oir_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=10),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'oir-circular-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.CardInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.CardInfo',
            False, 
            [
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                card name
                ''',
                'card_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                card state
                ''',
                'card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cxp-avail-bitmap', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                cxp avail bitmap
                ''',
                'cxp_avail_bitmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                exp num asics
                ''',
                'exp_num_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics-per-fsdb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                exp num asics per fsdb
                ''',
                'exp_num_asics_per_fsdb',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-powered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is powered
                ''',
                'is_powered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cos-per-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num cos per port
                ''',
                'num_cos_per_port',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-ilkns-per-asic', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num ilkns per asic
                ''',
                'num_ilkns_per_asic',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-local-ports-per-ilkn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num local ports per ilkn
                ''',
                'num_local_ports_per_ilkn',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oir-circular-buffer', REFERENCE_CLASS, 'OirCircularBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer', 
                [], [], 
                '''                oir circular buffer
                ''',
                'oir_circular_buffer',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'card-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation',
            False, 
            [
            _MetaInfoClassMember('asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                asic avail mask
                ''',
                'asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-oper-notify-to-fsdb-pending-bmap', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                asic oper notify to fsdb pending bmap
                ''',
                'asic_oper_notify_to_fsdb_pending_bmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('board-rev-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                board rev id
                ''',
                'board_rev_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                card avail mask
                ''',
                'card_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-info', REFERENCE_LIST, 'CardInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.CardInfo', 
                [], [], 
                '''                card info
                ''',
                'card_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=16),
            _MetaInfoClassMember('coeff-major-rev', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                coeff major rev
                ''',
                'coeff_major_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff-minor-rev', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                coeff minor rev
                ''',
                'coeff_minor_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('device-info', REFERENCE_LIST, 'DeviceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.DeviceInfo', 
                [], [], 
                '''                device info
                ''',
                'device_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=32),
            _MetaInfoClassMember('drv-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                drv version
                ''',
                'drv_version',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('drvr-current-startup-timestamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                drvr current startup timestamp
                ''',
                'drvr_current_startup_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('drvr-initial-startup-timestamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                drvr initial startup timestamp
                ''',
                'drvr_initial_startup_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                exp asic avail mask
                ''',
                'exp_asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fabric-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                fabric mode
                ''',
                'fabric_mode',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fc-mode', REFERENCE_ENUM_CLASS, 'FcModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'FcModeEnum', 
                [], [], 
                '''                FC Mode
                ''',
                'fc_mode',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid conn active
                ''',
                'fgid_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid reg active
                ''',
                'fgid_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb conn active
                ''',
                'fsdb_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb reg active
                ''',
                'fsdb_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('functional-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                functional role
                ''',
                'functional_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-cih-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is cih registered
                ''',
                'is_cih_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-driver-ready', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is driver ready
                ''',
                'is_driver_ready',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-completed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download completed
                ''',
                'is_fgid_download_completed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download in progress
                ''',
                'is_fgid_download_in_progress',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-full-fgid-download-req', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is full fgid download req
                ''',
                'is_full_fgid_download_req',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-gaspp-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is gaspp registered
                ''',
                'is_gaspp_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-rcvd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort rcvd
                ''',
                'issu_abort_rcvd',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-sent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort sent
                ''',
                'issu_abort_sent',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr conn active
                ''',
                'issu_mgr_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr reg active
                ''',
                'issu_mgr_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-ready-ntfy-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu ready ntfy pending
                ''',
                'issu_ready_ntfy_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                issu role
                ''',
                'issu_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                node id
                ''',
                'node_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num cm conn reqs
                ''',
                'num_cm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fgid-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num fgid conn reqs
                ''',
                'num_fgid_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fsdb-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num fsdb conn reqs
                ''',
                'num_fsdb_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fstats-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num fstats conn reqs
                ''',
                'num_fstats_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-intf-ports', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num intf ports
                ''',
                'num_intf_ports',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-issu-mgr-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num issu mgr conn reqs
                ''',
                'num_issu_mgr_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-peer-fia-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num peer fia conn reqs
                ''',
                'num_peer_fia_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num pm conn reqs
                ''',
                'num_pm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('respawn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                respawn count
                ''',
                'respawn_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('total-asics', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                total asics
                ''',
                'total_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('uc-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                uc weight
                ''',
                'uc_weight',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ucmc-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ucmc ratio
                ''',
                'ucmc_ratio',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'driver-information',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Clear value
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.ClearStatistics.AsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.ClearStatistics.AsicInstances',
            False, 
            [
            _MetaInfoClassMember('asic-instance', REFERENCE_LIST, 'AsicInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance', 
                [], [], 
                '''                Asic instance to be cleared
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.ClearStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.ClearStatistics',
            False, 
            [
            _MetaInfoClassMember('asic-instances', REFERENCE_CLASS, 'AsicInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.ClearStatistics.AsicInstances', 
                [], [], 
                '''                Instance table for clear statistics
                information
                ''',
                'asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'clear-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', REFERENCE_ENUM_CLASS, 'AsicEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicEnum', 
                [], [], 
                '''                Asic Type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', REFERENCE_ENUM_CLASS, 'RackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'RackEnum', 
                [], [], 
                '''                Rack Type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', REFERENCE_ENUM_CLASS, 'LinkStageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStageEnum', 
                [], [], 
                '''                Link Stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', REFERENCE_ENUM_CLASS, 'LinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkEnum', 
                [], [], 
                '''                Link Type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'this-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', REFERENCE_ENUM_CLASS, 'AsicEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicEnum', 
                [], [], 
                '''                Asic Type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', REFERENCE_ENUM_CLASS, 'RackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'RackEnum', 
                [], [], 
                '''                Rack Type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', REFERENCE_ENUM_CLASS, 'LinkStageEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkStageEnum', 
                [], [], 
                '''                Link Stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', REFERENCE_ENUM_CLASS, 'LinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkEnum', 
                [], [], 
                '''                Link Type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'far-end-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist',
            False, 
            [
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminStateEnum', 
                [], [], 
                '''                Admin State
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', REFERENCE_ENUM_CLASS, 'LinkErrorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorStateEnum', 
                [], [], 
                '''                Error State
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', REFERENCE_ENUM_CLASS, 'OperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperStateEnum', 
                [], [], 
                '''                Oper State
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reasons', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reasons
                ''',
                'reasons',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                timestamp
                ''',
                'timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'hist',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History',
            False, 
            [
            _MetaInfoClassMember('hist', REFERENCE_LIST, 'Hist' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist', 
                [], [], 
                '''                hist
                ''',
                'hist',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=5),
            _MetaInfoClassMember('histnum', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                histnum
                ''',
                'histnum',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                start index
                ''',
                'start_index',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_',
            False, 
            [
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Single Link
                ''',
                'link',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminStateEnum', 
                [], [], 
                '''                Admin State
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                coeff1
                ''',
                'coeff1',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                coeff2
                ''',
                'coeff2',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', REFERENCE_ENUM_CLASS, 'LinkErrorStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'LinkErrorStateEnum', 
                [], [], 
                '''                Error State
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('far-end-link', REFERENCE_CLASS, 'FarEndLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink', 
                [], [], 
                '''                far end link
                ''',
                'far_end_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History', 
                [], [], 
                '''                history
                ''',
                'history',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-conf-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is conf pending
                ''',
                'is_conf_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-link-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is link valid
                ''',
                'is_link_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-power-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is power enabled
                ''',
                'is_power_enabled',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-admin-shuts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num admin shuts
                ''',
                'num_admin_shuts',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', REFERENCE_ENUM_CLASS, 'OperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'OperStateEnum', 
                [], [], 
                '''                Oper State
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                speed
                ''',
                'speed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('stage', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                stage
                ''',
                'stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats', 
                [], [], 
                '''                stats
                ''',
                'stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('this-link', REFERENCE_CLASS, 'ThisLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink', 
                [], [], 
                '''                this link
                ''',
                'this_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink',
            False, 
            [
            _MetaInfoClassMember('end-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '47')], [], 
                '''                End number
                ''',
                'end_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '47')], [], 
                '''                Start number
                ''',
                'start_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-link', REFERENCE_LIST, 'TxLink_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_', 
                [], [], 
                '''                Single link information
                ''',
                'tx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks',
            False, 
            [
            _MetaInfoClassMember('tx-link', REFERENCE_LIST, 'TxLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink', 
                [], [], 
                '''                Link number for tx link information
                ''',
                'tx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-links',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance',
            False, 
            [
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Transmit instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('tx-links', REFERENCE_CLASS, 'TxLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks', 
                [], [], 
                '''                Link table for tx information
                ''',
                'tx_links',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances',
            False, 
            [
            _MetaInfoClassMember('tx-asic-instance', REFERENCE_LIST, 'TxAsicInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance', 
                [], [], 
                '''                Instance number for tx link information
                ''',
                'tx_asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption',
            False, 
            [
            _MetaInfoClassMember('tx-asic-instances', REFERENCE_CLASS, 'TxAsicInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances', 
                [], [], 
                '''                Instance table for tx information
                ''',
                'tx_asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-status-option',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable',
            False, 
            [
            _MetaInfoClassMember('tx-status-option', REFERENCE_CLASS, 'TxStatusOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption', 
                [], [], 
                '''                Option: data, ctrl, all- for now none
                ''',
                'tx_status_option',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-status-option-table',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation',
            False, 
            [
            _MetaInfoClassMember('tx-status-option-table', REFERENCE_CLASS, 'TxStatusOptionTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable', 
                [], [], 
                '''                Link table for tx information
                ''',
                'tx_status_option_table',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Unit number
                ''',
                'unit',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                output
                ''',
                'output',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'register-dump-unit',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RegisterDump.RegisterDumpUnits',
            False, 
            [
            _MetaInfoClassMember('register-dump-unit', REFERENCE_LIST, 'RegisterDumpUnit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit', 
                [], [], 
                '''                Unit number for register dump
                ''',
                'register_dump_unit',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'register-dump-units',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RegisterDump' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RegisterDump',
            False, 
            [
            _MetaInfoClassMember('register-dump-units', REFERENCE_CLASS, 'RegisterDumpUnits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits', 
                [], [], 
                '''                Unit table for register dump
                ''',
                'register_dump_units',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'register-dump',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output',
            False, 
            [
            _MetaInfoClassMember('output', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                First line
                ''',
                'output',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('output-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                output xr
                ''',
                'output_xr',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command',
            False, 
            [
            _MetaInfoClassMember('cmd', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Shell command
                ''',
                'cmd',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('output', REFERENCE_LIST, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output', 
                [], [], 
                '''                Added to support datalist
                ''',
                'output',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'command',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands',
            False, 
            [
            _MetaInfoClassMember('command', REFERENCE_LIST, 'Command' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command', 
                [], [], 
                '''                Command for diag shell statistics
                ''',
                'command',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'commands',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Unit number
                ''',
                'unit',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('commands', REFERENCE_CLASS, 'Commands' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands', 
                [], [], 
                '''                Command table for diag shell
                ''',
                'commands',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'diag-shell-unit',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits',
            False, 
            [
            _MetaInfoClassMember('diag-shell-unit', REFERENCE_LIST, 'DiagShellUnit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit', 
                [], [], 
                '''                Unit number for diag shell statistics
                ''',
                'diag_shell_unit',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'diag-shell-units',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell',
            False, 
            [
            _MetaInfoClassMember('diag-shell-units', REFERENCE_CLASS, 'DiagShellUnits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits', 
                [], [], 
                '''                Unit table for diag shell
                ''',
                'diag_shell_units',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'diag-shell',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', REFERENCE_ENUM_CLASS, 'AsicEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicEnum', 
                [], [], 
                '''                Asic Type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', REFERENCE_ENUM_CLASS, 'RackEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'RackEnum', 
                [], [], 
                '''                Rack Type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo',
            False, 
            [
            _MetaInfoClassMember('admin-state', REFERENCE_ENUM_CLASS, 'AdminStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AdminStateEnum', 
                [], [], 
                '''                Admin State
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-state', REFERENCE_ENUM_CLASS, 'AsicAccessStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicAccessStateEnum', 
                [], [], 
                '''                Asic State
                ''',
                'asic_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fapid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                fapid
                ''',
                'fapid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('hotplug-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                hotplug event
                ''',
                'hotplug_event',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-init-cause', REFERENCE_ENUM_CLASS, 'AsicInitMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicInitMethodEnum', 
                [], [], 
                '''                last init cause
                ''',
                'last_init_cause',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('local-switch-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                local switch state
                ''',
                'local_switch_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-hard-resets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num hard resets
                ''',
                'num_hard_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pon-resets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num pon resets
                ''',
                'num_pon_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', REFERENCE_ENUM_CLASS, 'AsicOperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'AsicOperStateEnum', 
                [], [], 
                '''                Oper State
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slice-state', REFERENCE_ENUM_CLASS, 'SliceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'SliceStateEnum', 
                [], [], 
                '''                Slice State
                ''',
                'slice_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'device-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo',
            False, 
            [
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cur-card-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                cur card state
                ''',
                'cur_card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fia-oir-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                count
                ''',
                'count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fia-oir-info', REFERENCE_LIST, 'FiaOirInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo', 
                [], [], 
                '''                fia oir info
                ''',
                'fia_oir_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=10),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'oir-circular-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo',
            False, 
            [
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                card name
                ''',
                'card_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                card state
                ''',
                'card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cxp-avail-bitmap', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                cxp avail bitmap
                ''',
                'cxp_avail_bitmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                exp num asics
                ''',
                'exp_num_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics-per-fsdb', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                exp num asics per fsdb
                ''',
                'exp_num_asics_per_fsdb',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-powered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is powered
                ''',
                'is_powered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cos-per-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num cos per port
                ''',
                'num_cos_per_port',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-ilkns-per-asic', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num ilkns per asic
                ''',
                'num_ilkns_per_asic',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-local-ports-per-ilkn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num local ports per ilkn
                ''',
                'num_local_ports_per_ilkn',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oir-circular-buffer', REFERENCE_CLASS, 'OirCircularBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer', 
                [], [], 
                '''                oir circular buffer
                ''',
                'oir_circular_buffer',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'card-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Slot number
                ''',
                'slot',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                asic avail mask
                ''',
                'asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-oper-notify-to-fsdb-pending-bmap', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                asic oper notify to fsdb pending bmap
                ''',
                'asic_oper_notify_to_fsdb_pending_bmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('board-rev-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                board rev id
                ''',
                'board_rev_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                card avail mask
                ''',
                'card_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-info', REFERENCE_LIST, 'CardInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo', 
                [], [], 
                '''                card info
                ''',
                'card_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=16),
            _MetaInfoClassMember('coeff-major-rev', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                coeff major rev
                ''',
                'coeff_major_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff-minor-rev', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                coeff minor rev
                ''',
                'coeff_minor_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('device-info', REFERENCE_LIST, 'DeviceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo', 
                [], [], 
                '''                device info
                ''',
                'device_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=32),
            _MetaInfoClassMember('drv-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                drv version
                ''',
                'drv_version',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('drvr-current-startup-timestamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                drvr current startup timestamp
                ''',
                'drvr_current_startup_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('drvr-initial-startup-timestamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                drvr initial startup timestamp
                ''',
                'drvr_initial_startup_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                exp asic avail mask
                ''',
                'exp_asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fabric-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                fabric mode
                ''',
                'fabric_mode',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fc-mode', REFERENCE_ENUM_CLASS, 'FcModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'FcModeEnum', 
                [], [], 
                '''                FC Mode
                ''',
                'fc_mode',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid conn active
                ''',
                'fgid_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid reg active
                ''',
                'fgid_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb conn active
                ''',
                'fsdb_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb reg active
                ''',
                'fsdb_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('functional-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                functional role
                ''',
                'functional_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-cih-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is cih registered
                ''',
                'is_cih_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-driver-ready', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is driver ready
                ''',
                'is_driver_ready',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-completed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download completed
                ''',
                'is_fgid_download_completed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download in progress
                ''',
                'is_fgid_download_in_progress',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-full-fgid-download-req', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is full fgid download req
                ''',
                'is_full_fgid_download_req',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-gaspp-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is gaspp registered
                ''',
                'is_gaspp_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-rcvd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort rcvd
                ''',
                'issu_abort_rcvd',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-sent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort sent
                ''',
                'issu_abort_sent',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr conn active
                ''',
                'issu_mgr_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr reg active
                ''',
                'issu_mgr_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-ready-ntfy-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu ready ntfy pending
                ''',
                'issu_ready_ntfy_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                issu role
                ''',
                'issu_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                node id
                ''',
                'node_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num cm conn reqs
                ''',
                'num_cm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fgid-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num fgid conn reqs
                ''',
                'num_fgid_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fsdb-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num fsdb conn reqs
                ''',
                'num_fsdb_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fstats-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num fstats conn reqs
                ''',
                'num_fstats_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-intf-ports', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num intf ports
                ''',
                'num_intf_ports',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-issu-mgr-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num issu mgr conn reqs
                ''',
                'num_issu_mgr_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-peer-fia-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num peer fia conn reqs
                ''',
                'num_peer_fia_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                num pm conn reqs
                ''',
                'num_pm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('respawn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                respawn count
                ''',
                'respawn_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('total-asics', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                total asics
                ''',
                'total_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('uc-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                uc weight
                ''',
                'uc_weight',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ucmc-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ucmc ratio
                ''',
                'ucmc_ratio',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot', 
                [], [], 
                '''                Slot number for getting history
                ''',
                'slot',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag',
            False, 
            [
            _MetaInfoClassMember('flag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Flag value
                ''',
                'flag',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots', 
                [], [], 
                '''                Slot table for history
                ''',
                'slots',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'flag',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags',
            False, 
            [
            _MetaInfoClassMember('flag', REFERENCE_LIST, 'Flag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag', 
                [], [], 
                '''                Flag value for physical location
                ''',
                'flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'flags',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_CLASS, 'Flags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags', 
                [], [], 
                '''                Flag table for history
                ''',
                'flags',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'oir-history',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo',
            False, 
            [
            _MetaInfoClassMember('field-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 80)], [], 
                '''                Field Name
                ''',
                'field_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('field-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Field Value
                ''',
                'field_value',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-ovf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Ovf
                ''',
                'is_ovf',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'field-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo',
            False, 
            [
            _MetaInfoClassMember('block-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                Block Name
                ''',
                'block_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('field-info', REFERENCE_LIST, 'FieldInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo', 
                [], [], 
                '''                field info
                ''',
                'field_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=200),
            _MetaInfoClassMember('num-fields', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Num Fields
                ''',
                'num_fields',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'block-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo',
            False, 
            [
            _MetaInfoClassMember('block-info', REFERENCE_LIST, 'BlockInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo', 
                [], [], 
                '''                block info
                ''',
                'block_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=22),
            _MetaInfoClassMember('num-blocks', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Num Blocks
                ''',
                'num_blocks',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'stats-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('chip-ver', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                chip ver
                ''',
                'chip_ver',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack no
                ''',
                'rack_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('stats-info', REFERENCE_CLASS, 'StatsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo', 
                [], [], 
                '''                stats info
                ''',
                'stats_info',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                valid
                ''',
                'valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'pbc-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics',
            False, 
            [
            _MetaInfoClassMember('pbc-stats', REFERENCE_CLASS, 'PbcStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats', 
                [], [], 
                '''                PBC stats bag
                ''',
                'pbc_stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'pbc-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus',
            False, 
            [
            _MetaInfoClassMember('error-token-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                error token count
                ''',
                'error_token_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-code-group-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link code group error
                ''',
                'link_code_group_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-crc-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link crc error
                ''',
                'link_crc_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-mis-align-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link mis align error
                ''',
                'link_mis_align_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-accept-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link no sig accept error
                ''',
                'link_no_sig_accept_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-lock-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link no sig lock error
                ''',
                'link_no_sig_lock_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-size-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link size error
                ''',
                'link_size_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-tokens-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link tokens error
                ''',
                'link_tokens_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-error-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters',
            False, 
            [
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus',
            False, 
            [
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'ovf-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats',
            False, 
            [
            _MetaInfoClassMember('link-counters', REFERENCE_CLASS, 'LinkCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters', 
                [], [], 
                '''                link counters
                ''',
                'link_counters',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-error-status', REFERENCE_CLASS, 'LinkErrorStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus', 
                [], [], 
                '''                link error status
                ''',
                'link_error_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ovf-status', REFERENCE_CLASS, 'OvfStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus', 
                [], [], 
                '''                ovf status
                ''',
                'ovf_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'aggr-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus',
            False, 
            [
            _MetaInfoClassMember('error-token-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                error token count
                ''',
                'error_token_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-code-group-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link code group error
                ''',
                'link_code_group_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-crc-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link crc error
                ''',
                'link_crc_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-mis-align-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link mis align error
                ''',
                'link_mis_align_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-accept-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link no sig accept error
                ''',
                'link_no_sig_accept_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-lock-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link no sig lock error
                ''',
                'link_no_sig_lock_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-size-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link size error
                ''',
                'link_size_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-tokens-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link tokens error
                ''',
                'link_tokens_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-error-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters',
            False, 
            [
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus',
            False, 
            [
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'ovf-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats',
            False, 
            [
            _MetaInfoClassMember('link-counters', REFERENCE_CLASS, 'LinkCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters', 
                [], [], 
                '''                link counters
                ''',
                'link_counters',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-error-status', REFERENCE_CLASS, 'LinkErrorStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus', 
                [], [], 
                '''                link error status
                ''',
                'link_error_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ovf-status', REFERENCE_CLASS, 'OvfStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus', 
                [], [], 
                '''                ovf status
                ''',
                'ovf_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'incr-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic',
            False, 
            [
            _MetaInfoClassMember('asic', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Single asic
                ''',
                'asic',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('aggr-stats', REFERENCE_CLASS, 'AggrStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats', 
                [], [], 
                '''                aggr stats
                ''',
                'aggr_stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('incr-stats', REFERENCE_CLASS, 'IncrStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats', 
                [], [], 
                '''                incr stats
                ''',
                'incr_stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                link no
                ''',
                'link_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                link valid
                ''',
                'link_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rack no
                ''',
                'rack_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                valid
                ''',
                'valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-asic',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink',
            False, 
            [
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Link number
                ''',
                'link',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('fmac-asic', REFERENCE_LIST, 'FmacAsic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic', 
                [], [], 
                '''                Single aisc information
                ''',
                'fmac_asic',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks',
            False, 
            [
            _MetaInfoClassMember('fmac-link', REFERENCE_LIST, 'FmacLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink', 
                [], [], 
                '''                Link number for statistics
                ''',
                'fmac_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-links',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics',
            False, 
            [
            _MetaInfoClassMember('fmac-links', REFERENCE_CLASS, 'FmacLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks', 
                [], [], 
                '''                Link table for statistics
                ''',
                'fmac_links',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance',
            False, 
            [
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Asic instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('fmac-statistics', REFERENCE_CLASS, 'FmacStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics', 
                [], [], 
                '''                Statistics of FMAC
                ''',
                'fmac_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('pbc-statistics', REFERENCE_CLASS, 'PbcStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics', 
                [], [], 
                '''                Packet Byte Counter for a Asic
                ''',
                'pbc_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'statistics-asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances',
            False, 
            [
            _MetaInfoClassMember('statistics-asic-instance', REFERENCE_LIST, 'StatisticsAsicInstance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance', 
                [], [], 
                '''                Asic instance for statistics
                ''',
                'statistics_asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'statistics-asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics',
            False, 
            [
            _MetaInfoClassMember('statistics-asic-instances', REFERENCE_CLASS, 'StatisticsAsicInstances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances', 
                [], [], 
                '''                Instance table for statistics
                ''',
                'statistics_asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('asic-statistics', REFERENCE_CLASS, 'AsicStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics', 
                [], [], 
                '''                FIA asic statistics information
                ''',
                'asic_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('clear-statistics', REFERENCE_CLASS, 'ClearStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.ClearStatistics', 
                [], [], 
                '''                Clear statistics information
                ''',
                'clear_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('diag-shell', REFERENCE_CLASS, 'DiagShell' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell', 
                [], [], 
                '''                FIA diag shell information
                ''',
                'diag_shell',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('driver-information', REFERENCE_CLASS, 'DriverInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation', 
                [], [], 
                '''                FIA driver information
                ''',
                'driver_information',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oir-history', REFERENCE_CLASS, 'OirHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory', 
                [], [], 
                '''                FIA operational data of oir history
                ''',
                'oir_history',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('register-dump', REFERENCE_CLASS, 'RegisterDump' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RegisterDump', 
                [], [], 
                '''                FIA register dump information
                ''',
                'register_dump',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-link-information', REFERENCE_CLASS, 'RxLinkInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation', 
                [], [], 
                '''                FIA link rx information
                ''',
                'rx_link_information',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-link-information', REFERENCE_CLASS, 'TxLinkInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation', 
                [], [], 
                '''                FIA link TX information
                ''',
                'tx_link_information',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node', 
                [], [], 
                '''                FIA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia' : {
        'meta_info' : _MetaInfoClass('Fia',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes', 
                [], [], 
                '''                FIA driver operational data for available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fia',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
}
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History.Hist']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.ThisLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.FarEndLinkInHw']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_.History']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink_']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation']['meta_info']
_meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.ClearStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History.Hist']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.ThisLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.FarEndLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.Stats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_.History']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink_']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation']['meta_info']
_meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits']['meta_info']
_meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RegisterDump']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.ClearStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.RegisterDump']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node']['meta_info'].parent =_meta_table['Fia.Nodes']['meta_info']
_meta_table['Fia.Nodes']['meta_info'].parent =_meta_table['Fia']['meta_info']
