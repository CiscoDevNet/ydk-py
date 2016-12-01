


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'DnxQoseaShowActionEnum' : _MetaInfoEnum('DnxQoseaShowActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'action-none':'action_none',
            'action-transmit':'action_transmit',
            'action-drop':'action_drop',
            'action-mark':'action_mark',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'PolicyParamUnitEnum' : _MetaInfoEnum('PolicyParamUnitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'policy-param-unit-invalid':'policy_param_unit_invalid',
            'policy-param-unit-bytes':'policy_param_unit_bytes',
            'policy-param-unit-kbytes':'policy_param_unit_kbytes',
            'policy-param-unit-mbytes':'policy_param_unit_mbytes',
            'policy-param-unit-gbytes':'policy_param_unit_gbytes',
            'policy-param-unit-bitsps':'policy_param_unit_bitsps',
            'policy-param-unit-kbitsps':'policy_param_unit_kbitsps',
            'policy-param-unit-mbitsps':'policy_param_unit_mbitsps',
            'policy-param-unit-gbitsps':'policy_param_unit_gbitsps',
            'policy-param-unit-cells-ps':'policy_param_unit_cells_ps',
            'policy-param-unit-packets-ps':'policy_param_unit_packets_ps',
            'policy-param-unit-us':'policy_param_unit_us',
            'policy-param-unit-ms':'policy_param_unit_ms',
            'policy-param-unit-seconds':'policy_param_unit_seconds',
            'policy-param-unit-packets':'policy_param_unit_packets',
            'policy-param-unit-cells':'policy_param_unit_cells',
            'policy-param-unit-percent':'policy_param_unit_percent',
            'policy-param-unit-per-thousand':'policy_param_unit_per_thousand',
            'policy-param-unit-per-million':'policy_param_unit_per_million',
            'policy-param-unit-hz':'policy_param_unit_hz',
            'policy-param-unit-khz':'policy_param_unit_khz',
            'policy-param-unit-mhz':'policy_param_unit_mhz',
            'policy-param-unit-ratio':'policy_param_unit_ratio',
            'policy-param-unit-max':'policy_param_unit_max',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowWredEnum' : _MetaInfoEnum('DnxQoseaShowWredEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'wred-cos':'wred_cos',
            'wred-dscp':'wred_dscp',
            'wred-precedence':'wred_precedence',
            'wred-discard-class':'wred_discard_class',
            'wred-mpls-exp':'wred_mpls_exp',
            'red-with-user-min-max':'red_with_user_min_max',
            'red-with-default-min-max':'red_with_default_min_max',
            'wred-invalid':'wred_invalid',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowHpLevelEnum' : _MetaInfoEnum('DnxQoseaShowHpLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'high-priority-level1':'high_priority_level1',
            'high-priority-level2':'high_priority_level2',
            'high-priority-level3':'high_priority_level3',
            'high-priority-level4':'high_priority_level4',
            'high-priority-level5':'high_priority_level5',
            'high-priority-level6':'high_priority_level6',
            'high-priority-level7':'high_priority_level7',
            'unknown':'unknown',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'QosPolicyAccountEnumEnum' : _MetaInfoEnum('QosPolicyAccountEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'qos-serv-policy-no-ac-count-pref':'qos_serv_policy_no_ac_count_pref',
            'qos-serv-policy-ac-count-l2':'qos_serv_policy_ac_count_l2',
            'qos-serv-policy-no-ac-count-l2':'qos_serv_policy_no_ac_count_l2',
            'qos-serv-policy-ac-count-user-def':'qos_serv_policy_ac_count_user_def',
            'qos-serv-policy-ac-count-l1':'qos_serv_policy_ac_count_l1',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowMarkEnum' : _MetaInfoEnum('DnxQoseaShowMarkEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'mark-none':'mark_none',
            'dscp':'dscp',
            'precedence':'precedence',
            'mpls-topmost':'mpls_topmost',
            'mpls-imposition':'mpls_imposition',
            'qos-group':'qos_group',
            'discard-class':'discard_class',
            'cos':'cos',
            'inner-cos':'inner_cos',
            'un-supported9':'un_supported9',
            'un-supported10':'un_supported10',
            'dscp-tunnel':'dscp_tunnel',
            'precedence-tunnel':'precedence_tunnel',
            'dei':'dei',
            'dei-imposition':'dei_imposition',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowPolicyStatusEnum' : _MetaInfoEnum('DnxQoseaShowPolicyStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'no-error':'no_error',
            'policy-in-reset':'policy_in_reset',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowIntfStatusEnum' : _MetaInfoEnum('DnxQoseaShowIntfStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'state-unknown':'state_unknown',
            'state-down':'state_down',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowLevelEnum' : _MetaInfoEnum('DnxQoseaShowLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'level1':'level1',
            'level2':'level2',
            'level3':'level3',
            'level4':'level4',
            'level5':'level5',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowQueueEnum' : _MetaInfoEnum('DnxQoseaShowQueueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'low-priority-default-queue':'low_priority_default_queue',
            'low-priority-queue':'low_priority_queue',
            'high-priority-queue':'high_priority_queue',
            'unknown-queue-type':'unknown_queue_type',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails',
            False, 
            [
            _MetaInfoClassMember('interface-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Bandwidth (in kbps)
                ''',
                'interface_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                InterfaceHandle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_ENUM_CLASS, 'DnxQoseaShowIntfStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatusEnum', 
                [], [], 
                '''                Interface Status
                ''',
                'interface_status',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NPU ID
                ''',
                'npu_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-status', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatusEnum', 
                [], [], 
                '''                Policy Status
                ''',
                'policy_status',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('stats-accounting-type', REFERENCE_ENUM_CLASS, 'QosPolicyAccountEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnumEnum', 
                [], [], 
                '''                QoS Statistics Accounting Type
                ''',
                'stats_accounting_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('total-number-of-classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of Classes
                ''',
                'total_number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-base-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VOQ base address
                ''',
                'voq_base_address',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-stats-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                VOQ stats handle
                ''',
                'voq_stats_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'policy-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-max-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-min-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-excess-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'conform-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'exceed-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'violate-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'ip-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'common-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mpls-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue',
            False, 
            [
            _MetaInfoClassMember('range-end', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                End value of a range
                ''',
                'range_end',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('range-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Start value of a range
                ''',
                'range_start',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'dnx-qosea-show-red-match-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue',
            False, 
            [
            _MetaInfoClassMember('dnx-qosea-show-red-match-value', REFERENCE_LIST, 'DnxQoseaShowRedMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue', 
                [], [], 
                '''                dnx qosea show red match value
                ''',
                'dnx_qosea_show_red_match_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'wred-match-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred',
            False, 
            [
            _MetaInfoClassMember('config-max-threshold', REFERENCE_CLASS, 'ConfigMaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold', 
                [], [], 
                '''                Configured maximum threshold
                ''',
                'config_max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-threshold', REFERENCE_CLASS, 'ConfigMinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold', 
                [], [], 
                '''                Configured minimum threshold
                ''',
                'config_min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('first-segment', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First segment
                ''',
                'first_segment',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware maximum threshold
                ''',
                'hardware_max_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware minimum threshold
                ''',
                'hardware_min_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('segment-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segment size
                ''',
                'segment_size',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred-match-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowWredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWredEnum', 
                [], [], 
                '''                WREDMatchType
                ''',
                'wred_match_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred-match-value', REFERENCE_CLASS, 'WredMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue', 
                [], [], 
                '''                WRED match values
                ''',
                'wred_match_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('level-one-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                QoS policy class name at level 1
                ''',
                'level_one_class_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('class-level', REFERENCE_ENUM_CLASS, 'DnxQoseaShowLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevelEnum', 
                [], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('common-mark', REFERENCE_LIST, 'CommonMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark', 
                [], [], 
                '''                Common mark
                ''',
                'common_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured excess bandwidth percentage
                ''',
                'config_excess_bandwidth_percent',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-unit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured excess bandwidth unit
                ''',
                'config_excess_bandwidth_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-max-rate', REFERENCE_CLASS, 'ConfigMaxRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate', 
                [], [], 
                '''                Configured maximum rate
                ''',
                'config_max_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-rate', REFERENCE_CLASS, 'ConfigMinRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate', 
                [], [], 
                '''                Configured minimum rate
                ''',
                'config_min_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-average-rate', REFERENCE_CLASS, 'ConfigPolicerAverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate', 
                [], [], 
                '''                Configured policer average rate
                ''',
                'config_policer_average_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-conform-burst', REFERENCE_CLASS, 'ConfigPolicerConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst', 
                [], [], 
                '''                Configured policer conform burst
                ''',
                'config_policer_conform_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-excess-burst', REFERENCE_CLASS, 'ConfigPolicerExcessBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst', 
                [], [], 
                '''                Configured policer excess burst
                ''',
                'config_policer_excess_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-peak-rate', REFERENCE_CLASS, 'ConfigPolicerPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate', 
                [], [], 
                '''                Config policer peak rate
                ''',
                'config_policer_peak_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit', 
                [], [], 
                '''                Configured queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction', 
                [], [], 
                '''                Conform action
                ''',
                'conform_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('egress-queue-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Egress Queue ID
                ''',
                'egress_queue_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction', 
                [], [], 
                '''                Exceed action
                ''',
                'exceed_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-excess-bandwidth-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware excess bandwidth weight
                ''',
                'hardware_excess_bandwidth_weight',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware maximum rate in kbps
                ''',
                'hardware_max_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware minimum rate in kbps
                ''',
                'hardware_min_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-average-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer average in kbps
                ''',
                'hardware_policer_average_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-conform-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer conform burst
                ''',
                'hardware_policer_conform_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-excess-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer excess burst
                ''',
                'hardware_policer_excess_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-peak-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer peak rate
                ''',
                'hardware_policer_peak_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Hardware queue limit in bytes
                ''',
                'hardware_queue_limit_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-microseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Hardware queue limit in microseconds
                ''',
                'hardware_queue_limit_microseconds',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('ip-mark', REFERENCE_LIST, 'IpMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark', 
                [], [], 
                '''                IP mark
                ''',
                'ip_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('level-two-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                QoS policy child class name at level 2
                ''',
                'level_two_class_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mpls-mark', REFERENCE_LIST, 'MplsMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark', 
                [], [], 
                '''                MPLS mark
                ''',
                'mpls_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('network-min-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Network minimum Bandwith
                ''',
                'network_min_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PolicerBucketID
                ''',
                'policer_bucket_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-stats-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PolicerStatsHandle
                ''',
                'policer_stats_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('priority-level', REFERENCE_ENUM_CLASS, 'DnxQoseaShowHpLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevelEnum', 
                [], [], 
                '''                Priority level
                ''',
                'priority_level',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowQueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction', 
                [], [], 
                '''                Violate action
                ''',
                'violate_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_LIST, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_', 
                [], [], 
                '''                QoS policy class
                ''',
                'class_',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Member interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes', 
                [], [], 
                '''                QoS list of class names
                ''',
                'classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-details', REFERENCE_CLASS, 'PolicyDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails', 
                [], [], 
                '''                Policy Details
                ''',
                'policy_details',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'member-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces',
            False, 
            [
            _MetaInfoClassMember('member-interface', REFERENCE_LIST, 'MemberInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface', 
                [], [], 
                '''                QoS interface names
                ''',
                'member_interface',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'member-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails',
            False, 
            [
            _MetaInfoClassMember('interface-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Bandwidth (in kbps)
                ''',
                'interface_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                InterfaceHandle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_ENUM_CLASS, 'DnxQoseaShowIntfStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatusEnum', 
                [], [], 
                '''                Interface Status
                ''',
                'interface_status',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NPU ID
                ''',
                'npu_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-status', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatusEnum', 
                [], [], 
                '''                Policy Status
                ''',
                'policy_status',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('stats-accounting-type', REFERENCE_ENUM_CLASS, 'QosPolicyAccountEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnumEnum', 
                [], [], 
                '''                QoS Statistics Accounting Type
                ''',
                'stats_accounting_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('total-number-of-classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of Classes
                ''',
                'total_number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-base-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VOQ base address
                ''',
                'voq_base_address',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-stats-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                VOQ stats handle
                ''',
                'voq_stats_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'policy-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-max-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-min-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-excess-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'conform-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'exceed-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'violate-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'ip-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'common-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mpls-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue',
            False, 
            [
            _MetaInfoClassMember('range-end', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                End value of a range
                ''',
                'range_end',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('range-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Start value of a range
                ''',
                'range_start',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'dnx-qosea-show-red-match-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue',
            False, 
            [
            _MetaInfoClassMember('dnx-qosea-show-red-match-value', REFERENCE_LIST, 'DnxQoseaShowRedMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue', 
                [], [], 
                '''                dnx qosea show red match value
                ''',
                'dnx_qosea_show_red_match_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'wred-match-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred',
            False, 
            [
            _MetaInfoClassMember('config-max-threshold', REFERENCE_CLASS, 'ConfigMaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold', 
                [], [], 
                '''                Configured maximum threshold
                ''',
                'config_max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-threshold', REFERENCE_CLASS, 'ConfigMinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold', 
                [], [], 
                '''                Configured minimum threshold
                ''',
                'config_min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('first-segment', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First segment
                ''',
                'first_segment',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware maximum threshold
                ''',
                'hardware_max_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware minimum threshold
                ''',
                'hardware_min_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('segment-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segment size
                ''',
                'segment_size',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred-match-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowWredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWredEnum', 
                [], [], 
                '''                WREDMatchType
                ''',
                'wred_match_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred-match-value', REFERENCE_CLASS, 'WredMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue', 
                [], [], 
                '''                WRED match values
                ''',
                'wred_match_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('level-one-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                QoS policy class name at level 1
                ''',
                'level_one_class_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('class-level', REFERENCE_ENUM_CLASS, 'DnxQoseaShowLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevelEnum', 
                [], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('common-mark', REFERENCE_LIST, 'CommonMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark', 
                [], [], 
                '''                Common mark
                ''',
                'common_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured excess bandwidth percentage
                ''',
                'config_excess_bandwidth_percent',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-unit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured excess bandwidth unit
                ''',
                'config_excess_bandwidth_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-max-rate', REFERENCE_CLASS, 'ConfigMaxRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate', 
                [], [], 
                '''                Configured maximum rate
                ''',
                'config_max_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-rate', REFERENCE_CLASS, 'ConfigMinRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate', 
                [], [], 
                '''                Configured minimum rate
                ''',
                'config_min_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-average-rate', REFERENCE_CLASS, 'ConfigPolicerAverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate', 
                [], [], 
                '''                Configured policer average rate
                ''',
                'config_policer_average_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-conform-burst', REFERENCE_CLASS, 'ConfigPolicerConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst', 
                [], [], 
                '''                Configured policer conform burst
                ''',
                'config_policer_conform_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-excess-burst', REFERENCE_CLASS, 'ConfigPolicerExcessBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst', 
                [], [], 
                '''                Configured policer excess burst
                ''',
                'config_policer_excess_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-peak-rate', REFERENCE_CLASS, 'ConfigPolicerPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate', 
                [], [], 
                '''                Config policer peak rate
                ''',
                'config_policer_peak_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit', 
                [], [], 
                '''                Configured queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction', 
                [], [], 
                '''                Conform action
                ''',
                'conform_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('egress-queue-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Egress Queue ID
                ''',
                'egress_queue_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction', 
                [], [], 
                '''                Exceed action
                ''',
                'exceed_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-excess-bandwidth-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware excess bandwidth weight
                ''',
                'hardware_excess_bandwidth_weight',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware maximum rate in kbps
                ''',
                'hardware_max_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware minimum rate in kbps
                ''',
                'hardware_min_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-average-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer average in kbps
                ''',
                'hardware_policer_average_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-conform-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer conform burst
                ''',
                'hardware_policer_conform_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-excess-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer excess burst
                ''',
                'hardware_policer_excess_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-peak-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer peak rate
                ''',
                'hardware_policer_peak_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Hardware queue limit in bytes
                ''',
                'hardware_queue_limit_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-microseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Hardware queue limit in microseconds
                ''',
                'hardware_queue_limit_microseconds',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('ip-mark', REFERENCE_LIST, 'IpMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark', 
                [], [], 
                '''                IP mark
                ''',
                'ip_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('level-two-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                QoS policy child class name at level 2
                ''',
                'level_two_class_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mpls-mark', REFERENCE_LIST, 'MplsMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark', 
                [], [], 
                '''                MPLS mark
                ''',
                'mpls_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('network-min-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Network minimum Bandwith
                ''',
                'network_min_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PolicerBucketID
                ''',
                'policer_bucket_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-stats-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PolicerStatsHandle
                ''',
                'policer_stats_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('priority-level', REFERENCE_ENUM_CLASS, 'DnxQoseaShowHpLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevelEnum', 
                [], [], 
                '''                Priority level
                ''',
                'priority_level',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowQueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction', 
                [], [], 
                '''                Violate action
                ''',
                'violate_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_LIST, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_', 
                [], [], 
                '''                QoS policy class
                ''',
                'class_',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Bundle interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes', 
                [], [], 
                '''                QoS list of class names
                ''',
                'classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('member-interfaces', REFERENCE_CLASS, 'MemberInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces', 
                [], [], 
                '''                QoS list of member interfaces
                ''',
                'member_interfaces',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                NPU ID
                ''',
                'npu_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-details', REFERENCE_CLASS, 'PolicyDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails', 
                [], [], 
                '''                Policy Details
                ''',
                'policy_details',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('qos-direction', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface direction on which QoS is
                applied to.
                ''',
                'qos_direction',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'bundle-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.BundleInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces',
            False, 
            [
            _MetaInfoClassMember('bundle-interface', REFERENCE_LIST, 'BundleInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface', 
                [], [], 
                '''                QoS interface names
                ''',
                'bundle_interface',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'bundle-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails',
            False, 
            [
            _MetaInfoClassMember('interface-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Bandwidth (in kbps)
                ''',
                'interface_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                InterfaceHandle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-status', REFERENCE_ENUM_CLASS, 'DnxQoseaShowIntfStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowIntfStatusEnum', 
                [], [], 
                '''                Interface Status
                ''',
                'interface_status',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NPU ID
                ''',
                'npu_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Policy name
                ''',
                'policy_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-status', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyStatusEnum', 
                [], [], 
                '''                Policy Status
                ''',
                'policy_status',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('stats-accounting-type', REFERENCE_ENUM_CLASS, 'QosPolicyAccountEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'QosPolicyAccountEnumEnum', 
                [], [], 
                '''                QoS Statistics Accounting Type
                ''',
                'stats_accounting_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('total-number-of-classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of Classes
                ''',
                'total_number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-base-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VOQ base address
                ''',
                'voq_base_address',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-stats-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                VOQ stats handle
                ''',
                'voq_stats_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'policy-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-max-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-min-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-average-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-conform-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-policer-excess-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'conform-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'exceed-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark', 
                [], [], 
                '''                Action mark
                ''',
                'mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'violate-action',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'ip-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'common-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Mark value
                ''',
                'mark_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'mpls-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue',
            False, 
            [
            _MetaInfoClassMember('range-end', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                End value of a range
                ''',
                'range_end',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('range-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Start value of a range
                ''',
                'range_start',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'dnx-qosea-show-red-match-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue',
            False, 
            [
            _MetaInfoClassMember('dnx-qosea-show-red-match-value', REFERENCE_LIST, 'DnxQoseaShowRedMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue', 
                [], [], 
                '''                dnx qosea show red match value
                ''',
                'dnx_qosea_show_red_match_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'wred-match-value',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-min-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'PolicyParamUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PolicyParamUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policy value
                ''',
                'policy_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'config-max-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred',
            False, 
            [
            _MetaInfoClassMember('config-max-threshold', REFERENCE_CLASS, 'ConfigMaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold', 
                [], [], 
                '''                Configured maximum threshold
                ''',
                'config_max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-threshold', REFERENCE_CLASS, 'ConfigMinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold', 
                [], [], 
                '''                Configured minimum threshold
                ''',
                'config_min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('first-segment', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First segment
                ''',
                'first_segment',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware maximum threshold
                ''',
                'hardware_max_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware minimum threshold
                ''',
                'hardware_min_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('segment-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Segment size
                ''',
                'segment_size',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred-match-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowWredEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowWredEnum', 
                [], [], 
                '''                WREDMatchType
                ''',
                'wred_match_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred-match-value', REFERENCE_CLASS, 'WredMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue', 
                [], [], 
                '''                WRED match values
                ''',
                'wred_match_value',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('level-one-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                QoS policy class name at level 1
                ''',
                'level_one_class_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('class-level', REFERENCE_ENUM_CLASS, 'DnxQoseaShowLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowLevelEnum', 
                [], [], 
                '''                Class level
                ''',
                'class_level',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('common-mark', REFERENCE_LIST, 'CommonMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark', 
                [], [], 
                '''                Common mark
                ''',
                'common_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured excess bandwidth percentage
                ''',
                'config_excess_bandwidth_percent',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-unit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured excess bandwidth unit
                ''',
                'config_excess_bandwidth_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-max-rate', REFERENCE_CLASS, 'ConfigMaxRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate', 
                [], [], 
                '''                Configured maximum rate
                ''',
                'config_max_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-rate', REFERENCE_CLASS, 'ConfigMinRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate', 
                [], [], 
                '''                Configured minimum rate
                ''',
                'config_min_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-average-rate', REFERENCE_CLASS, 'ConfigPolicerAverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate', 
                [], [], 
                '''                Configured policer average rate
                ''',
                'config_policer_average_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-conform-burst', REFERENCE_CLASS, 'ConfigPolicerConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst', 
                [], [], 
                '''                Configured policer conform burst
                ''',
                'config_policer_conform_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-excess-burst', REFERENCE_CLASS, 'ConfigPolicerExcessBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst', 
                [], [], 
                '''                Configured policer excess burst
                ''',
                'config_policer_excess_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-peak-rate', REFERENCE_CLASS, 'ConfigPolicerPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate', 
                [], [], 
                '''                Config policer peak rate
                ''',
                'config_policer_peak_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit', 
                [], [], 
                '''                Configured queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction', 
                [], [], 
                '''                Conform action
                ''',
                'conform_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('egress-queue-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Egress Queue ID
                ''',
                'egress_queue_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction', 
                [], [], 
                '''                Exceed action
                ''',
                'exceed_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-excess-bandwidth-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware excess bandwidth weight
                ''',
                'hardware_excess_bandwidth_weight',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware maximum rate in kbps
                ''',
                'hardware_max_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware minimum rate in kbps
                ''',
                'hardware_min_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-average-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer average in kbps
                ''',
                'hardware_policer_average_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-conform-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer conform burst
                ''',
                'hardware_policer_conform_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-excess-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer excess burst
                ''',
                'hardware_policer_excess_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-peak-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware policer peak rate
                ''',
                'hardware_policer_peak_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Hardware queue limit in bytes
                ''',
                'hardware_queue_limit_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-microseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Hardware queue limit in microseconds
                ''',
                'hardware_queue_limit_microseconds',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('ip-mark', REFERENCE_LIST, 'IpMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark', 
                [], [], 
                '''                IP mark
                ''',
                'ip_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('level-two-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                QoS policy child class name at level 2
                ''',
                'level_two_class_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mpls-mark', REFERENCE_LIST, 'MplsMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark', 
                [], [], 
                '''                MPLS mark
                ''',
                'mpls_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('network-min-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Network minimum Bandwith
                ''',
                'network_min_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PolicerBucketID
                ''',
                'policer_bucket_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-stats-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PolicerStatsHandle
                ''',
                'policer_stats_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('priority-level', REFERENCE_ENUM_CLASS, 'DnxQoseaShowHpLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowHpLevelEnum', 
                [], [], 
                '''                Priority level
                ''',
                'priority_level',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('queue-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowQueueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowQueueEnum', 
                [], [], 
                '''                Queue type
                ''',
                'queue_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction', 
                [], [], 
                '''                Violate action
                ''',
                'violate_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_LIST, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred', 
                [], [], 
                '''                WRED parameters
                ''',
                'wred',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_', 
                [], [], 
                '''                QoS policy class
                ''',
                'class_',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes', 
                [], [], 
                '''                QoS list of class names
                ''',
                'classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-details', REFERENCE_CLASS, 'PolicyDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails', 
                [], [], 
                '''                Policy Details
                ''',
                'policy_details',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('qos-direction', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface direction on which QoS is
                applied to.
                ''',
                'qos_direction',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                QoS interface names
                ''',
                'interface',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred',
            False, 
            [
            _MetaInfoClassMember('drop-probability', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop Probability
                ''',
                'drop_probability',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum Threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'wred',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred',
            False, 
            [
            _MetaInfoClassMember('drop-probability', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop Probability
                ''',
                'drop_probability',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum Threshold
                ''',
                'min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'hw-wred',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass',
            False, 
            [
            _MetaInfoClassMember('class-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Class ID
                ''',
                'class_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Class Name
                ''',
                'class_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('cos-q', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Class of Service Queue
                ''',
                'cos_q',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware queue limit in bytes
                ''',
                'hardware_queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hw-wred', REFERENCE_LIST, 'HwWred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred', 
                [], [], 
                '''                Hardware WRED profiles
                ''',
                'hw_wred',
                'Cisco-IOS-XR-ncs5500-qos-oper', False, max_elements=4),
            _MetaInfoClassMember('queue-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default/Configured queue limit in bytes
                ''',
                'queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_LIST, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred', 
                [], [], 
                '''                Default/Configured WRED profiles
                ''',
                'wred',
                'Cisco-IOS-XR-ncs5500-qos-oper', False, max_elements=4),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'remote-class',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the remote interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('number-of-classes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Classes
                ''',
                'number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('number-of-virtual-output-queues', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Virtual Output Queues
                ''',
                'number_of_virtual_output_queues',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Policy Name
                ''',
                'policy_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('remote-class', REFERENCE_LIST, 'RemoteClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass', 
                [], [], 
                '''                Remote Class array
                ''',
                'remote_class',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('virtual-output-queue-statistics-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Virtual output queue statistics handle
                ''',
                'virtual_output_queue_statistics_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'remote-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node.RemoteInterfaces' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.RemoteInterfaces',
            False, 
            [
            _MetaInfoClassMember('remote-interface', REFERENCE_LIST, 'RemoteInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface', 
                [], [], 
                '''                QoS remote interface names
                ''',
                'remote_interface',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'remote-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('bundle-interfaces', REFERENCE_CLASS, 'BundleInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces', 
                [], [], 
                '''                QoS list of bundle interfaces
                ''',
                'bundle_interfaces',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces', 
                [], [], 
                '''                QoS list of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('remote-interfaces', REFERENCE_CLASS, 'RemoteInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.RemoteInterfaces', 
                [], [], 
                '''                QoS list of remote interfaces
                ''',
                'remote_interfaces',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos.Nodes' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node', 
                [], [], 
                '''                Node with platform specific QoS configuration
                ''',
                'node',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
    'PlatformQos' : {
        'meta_info' : _MetaInfoClass('PlatformQos',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes', 
                [], [], 
                '''                List of nodes with platform specific QoS
                configuration
                ''',
                'nodes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-qos-oper',
            'platform-qos',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper'
        ),
    },
}
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.WredMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred.ConfigMaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMaxRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigMinRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerAverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerPeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConfigPolicerExcessBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ConformAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ExceedAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.ViolateAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.IpMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.CommonMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.MplsMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class_']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.WredMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred.ConfigMaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMaxRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigMinRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerAverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerPeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConfigPolicerExcessBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ConformAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ExceedAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.ViolateAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.IpMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.CommonMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.MplsMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class_']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.WredMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred.ConfigMaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMaxRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigMinRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerAverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerPeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConfigPolicerExcessBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ConformAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ExceedAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.ViolateAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.IpMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.CommonMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.MplsMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class_']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.PolicyDetails']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass']['meta_info']
_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass.HwWred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass']['meta_info']
_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface.RemoteClass']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces.RemoteInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node.RemoteInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node']['meta_info']
_meta_table['PlatformQos.Nodes.Node']['meta_info'].parent =_meta_table['PlatformQos.Nodes']['meta_info']
_meta_table['PlatformQos.Nodes']['meta_info'].parent =_meta_table['PlatformQos']['meta_info']
