


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
            'action-none':'ACTION_NONE',
            'action-transmit':'ACTION_TRANSMIT',
            'action-drop':'ACTION_DROP',
            'action-mark':'ACTION_MARK',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowPolicyUnitEnum' : _MetaInfoEnum('DnxQoseaShowPolicyUnitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'invalid':'INVALID',
            'bytes':'BYTES',
            'kilo-bytes':'KILO_BYTES',
            'mega-bytes':'MEGA_BYTES',
            'giga-bytes':'GIGA_BYTES',
            'bits-per-second':'BITS_PER_SECOND',
            'kilo-bits-per-second':'KILO_BITS_PER_SECOND',
            'mega-bits-per-second':'MEGA_BITS_PER_SECOND',
            'giga-bits-per-second':'GIGA_BITS_PER_SECOND',
            'cells-per-second':'CELLS_PER_SECOND',
            'packets-per-second':'PACKETS_PER_SECOND',
            'microseconds':'MICROSECONDS',
            'milliseconds':'MILLISECONDS',
            'packets':'PACKETS',
            'cells':'CELLS',
            'percent':'PERCENT',
            'ratio':'RATIO',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowWredEnum' : _MetaInfoEnum('DnxQoseaShowWredEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'wred-cos':'WRED_COS',
            'wred-dscp':'WRED_DSCP',
            'wred-precedence':'WRED_PRECEDENCE',
            'wred-discard-class':'WRED_DISCARD_CLASS',
            'wred-mpls-exp':'WRED_MPLS_EXP',
            'red-with-user-min-max':'RED_WITH_USER_MIN_MAX',
            'red-with-default-min-max':'RED_WITH_DEFAULT_MIN_MAX',
            'wred-invalid':'WRED_INVALID',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowHpLevelEnum' : _MetaInfoEnum('DnxQoseaShowHpLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'high-priority-level1':'HIGH_PRIORITY_LEVEL1',
            'high-priority-level2':'HIGH_PRIORITY_LEVEL2',
            'high-priority-level3':'HIGH_PRIORITY_LEVEL3',
            'high-priority-level4':'HIGH_PRIORITY_LEVEL4',
            'high-priority-level5':'HIGH_PRIORITY_LEVEL5',
            'high-priority-level6':'HIGH_PRIORITY_LEVEL6',
            'high-priority-level7':'HIGH_PRIORITY_LEVEL7',
            'unknown':'UNKNOWN',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'QosPolicyAccountEnumEnum' : _MetaInfoEnum('QosPolicyAccountEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'qos-serv-policy-no-ac-count-pref':'QOS_SERV_POLICY_NO_AC_COUNT_PREF',
            'qos-serv-policy-ac-count-l2':'QOS_SERV_POLICY_AC_COUNT_L2',
            'qos-serv-policy-no-ac-count-l2':'QOS_SERV_POLICY_NO_AC_COUNT_L2',
            'qos-serv-policy-ac-count-user-def':'QOS_SERV_POLICY_AC_COUNT_USER_DEF',
            'qos-serv-policy-ac-count-l1':'QOS_SERV_POLICY_AC_COUNT_L1',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowMarkEnum' : _MetaInfoEnum('DnxQoseaShowMarkEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'mark-none':'MARK_NONE',
            'dscp':'DSCP',
            'precedence':'PRECEDENCE',
            'mpls-topmost':'MPLS_TOPMOST',
            'mpls-imposition':'MPLS_IMPOSITION',
            'qos-group':'QOS_GROUP',
            'discard-class':'DISCARD_CLASS',
            'cos':'COS',
            'inner-cos':'INNER_COS',
            'dscp-tunnel':'DSCP_TUNNEL',
            'precedence-tunnel':'PRECEDENCE_TUNNEL',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowPolicyStatusEnum' : _MetaInfoEnum('DnxQoseaShowPolicyStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'no-error':'NO_ERROR',
            'policy-in-reset':'POLICY_IN_RESET',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowIntfStatusEnum' : _MetaInfoEnum('DnxQoseaShowIntfStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'state-unknown':'STATE_UNKNOWN',
            'state-down':'STATE_DOWN',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowLevelEnum' : _MetaInfoEnum('DnxQoseaShowLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'level1':'LEVEL1',
            'level2':'LEVEL2',
            'level3':'LEVEL3',
            'level4':'LEVEL4',
            'level5':'LEVEL5',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'DnxQoseaShowQueueEnum' : _MetaInfoEnum('DnxQoseaShowQueueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper',
        {
            'low-priority-default-queue':'LOW_PRIORITY_DEFAULT_QUEUE',
            'low-priority-queue':'LOW_PRIORITY_QUEUE',
            'high-priority-queue':'HIGH_PRIORITY_QUEUE',
            'unknown-queue-type':'UNKNOWN_QUEUE_TYPE',
        }, 'Cisco-IOS-XR-ncs5500-qos-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-oper']),
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails',
            False, 
            [
            _MetaInfoClassMember('interface-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Interface Bandwidth (in kbps)
                ''',
                'interface_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
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
                [(0, 65535)], [], 
                '''                Number of Classes
                ''',
                'total_number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-base-address', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                VOQ base address
                ''',
                'voq_base_address',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-stats-handle', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMaxRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMaxRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMinRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMinRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerAverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerAverageRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerPeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerPeakRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerConformBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerExcessBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerExcessBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction.Mark', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction.Mark', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction.Mark', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.IpMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.IpMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.CommonMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.CommonMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.MplsMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.MplsMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue',
            False, 
            [
            _MetaInfoClassMember('range-end', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                End value of a range
                ''',
                'range_end',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('range-start', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue',
            False, 
            [
            _MetaInfoClassMember('dnx-qosea-show-red-match-value', REFERENCE_LIST, 'DnxQoseaShowRedMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMinThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMaxThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred',
            False, 
            [
            _MetaInfoClassMember('config-max-threshold', REFERENCE_CLASS, 'ConfigMaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMaxThreshold', 
                [], [], 
                '''                Configured maximum threshold
                ''',
                'config_max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-threshold', REFERENCE_CLASS, 'ConfigMinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMinThreshold', 
                [], [], 
                '''                Configured minimum threshold
                ''',
                'config_min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('first-segment', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First segment
                ''',
                'first_segment',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware maximum threshold
                ''',
                'hardware_max_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware minimum threshold
                ''',
                'hardware_min_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('segment-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('wred-match-value', REFERENCE_CLASS, 'WredMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class',
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
            _MetaInfoClassMember('common-mark', REFERENCE_LIST, 'CommonMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.CommonMark', 
                [], [], 
                '''                Common mark
                ''',
                'common_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-percent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Configured excess bandwidth percentage
                ''',
                'config_excess_bandwidth_percent',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-unit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Configured excess bandwidth unit
                ''',
                'config_excess_bandwidth_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-max-rate', REFERENCE_CLASS, 'ConfigMaxRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMaxRate', 
                [], [], 
                '''                Configured maximum rate
                ''',
                'config_max_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-rate', REFERENCE_CLASS, 'ConfigMinRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMinRate', 
                [], [], 
                '''                Configured minimum rate
                ''',
                'config_min_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-average-rate', REFERENCE_CLASS, 'ConfigPolicerAverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerAverageRate', 
                [], [], 
                '''                Configured policer average rate
                ''',
                'config_policer_average_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-conform-burst', REFERENCE_CLASS, 'ConfigPolicerConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerConformBurst', 
                [], [], 
                '''                Configured policer conform burst
                ''',
                'config_policer_conform_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-excess-burst', REFERENCE_CLASS, 'ConfigPolicerExcessBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerExcessBurst', 
                [], [], 
                '''                Configured policer excess burst
                ''',
                'config_policer_excess_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-peak-rate', REFERENCE_CLASS, 'ConfigPolicerPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerPeakRate', 
                [], [], 
                '''                Config policer peak rate
                ''',
                'config_policer_peak_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigQueueLimit', 
                [], [], 
                '''                Configured queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction', 
                [], [], 
                '''                Conform action
                ''',
                'conform_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('egress-queue-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Egress Queue ID
                ''',
                'egress_queue_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction', 
                [], [], 
                '''                Exceed action
                ''',
                'exceed_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-excess-bandwidth-weight', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware excess bandwidth weight
                ''',
                'hardware_excess_bandwidth_weight',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware maximum rate in kbps
                ''',
                'hardware_max_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware minimum rate in kbps
                ''',
                'hardware_min_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-average-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer average in kbps
                ''',
                'hardware_policer_average_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-conform-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer conform burst
                ''',
                'hardware_policer_conform_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-excess-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer excess burst
                ''',
                'hardware_policer_excess_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-peak-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer peak rate
                ''',
                'hardware_policer_peak_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Hardware queue limit in bytes
                ''',
                'hardware_queue_limit_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-microseconds', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Hardware queue limit in microseconds
                ''',
                'hardware_queue_limit_microseconds',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('ip-mark', REFERENCE_LIST, 'IpMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.IpMark', 
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
            _MetaInfoClassMember('mpls-mark', REFERENCE_LIST, 'MplsMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.MplsMark', 
                [], [], 
                '''                MPLS mark
                ''',
                'mpls_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('network-min-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Network minimum Bandwith
                ''',
                'network_min_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                PolicerBucketID
                ''',
                'policer_bucket_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-stats-handle', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction', 
                [], [], 
                '''                Violate action
                ''',
                'violate_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_LIST, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred', 
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
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class', 
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
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
                [(0, 4294967295)], [], 
                '''                Interface Bandwidth (in kbps)
                ''',
                'interface_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
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
                [(0, 65535)], [], 
                '''                Number of Classes
                ''',
                'total_number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-base-address', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                VOQ base address
                ''',
                'voq_base_address',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-stats-handle', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMaxRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMaxRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMinRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMinRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerAverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerAverageRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerPeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerPeakRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerConformBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerExcessBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerExcessBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction.Mark', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction.Mark', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction.Mark', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.IpMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.IpMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.CommonMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.CommonMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.MplsMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.MplsMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue',
            False, 
            [
            _MetaInfoClassMember('range-end', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                End value of a range
                ''',
                'range_end',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('range-start', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue',
            False, 
            [
            _MetaInfoClassMember('dnx-qosea-show-red-match-value', REFERENCE_LIST, 'DnxQoseaShowRedMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMinThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMaxThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred',
            False, 
            [
            _MetaInfoClassMember('config-max-threshold', REFERENCE_CLASS, 'ConfigMaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMaxThreshold', 
                [], [], 
                '''                Configured maximum threshold
                ''',
                'config_max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-threshold', REFERENCE_CLASS, 'ConfigMinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMinThreshold', 
                [], [], 
                '''                Configured minimum threshold
                ''',
                'config_min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('first-segment', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First segment
                ''',
                'first_segment',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware maximum threshold
                ''',
                'hardware_max_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware minimum threshold
                ''',
                'hardware_min_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('segment-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('wred-match-value', REFERENCE_CLASS, 'WredMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue', 
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
    'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class',
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
            _MetaInfoClassMember('common-mark', REFERENCE_LIST, 'CommonMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.CommonMark', 
                [], [], 
                '''                Common mark
                ''',
                'common_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-percent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Configured excess bandwidth percentage
                ''',
                'config_excess_bandwidth_percent',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-unit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Configured excess bandwidth unit
                ''',
                'config_excess_bandwidth_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-max-rate', REFERENCE_CLASS, 'ConfigMaxRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMaxRate', 
                [], [], 
                '''                Configured maximum rate
                ''',
                'config_max_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-rate', REFERENCE_CLASS, 'ConfigMinRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMinRate', 
                [], [], 
                '''                Configured minimum rate
                ''',
                'config_min_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-average-rate', REFERENCE_CLASS, 'ConfigPolicerAverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerAverageRate', 
                [], [], 
                '''                Configured policer average rate
                ''',
                'config_policer_average_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-conform-burst', REFERENCE_CLASS, 'ConfigPolicerConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerConformBurst', 
                [], [], 
                '''                Configured policer conform burst
                ''',
                'config_policer_conform_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-excess-burst', REFERENCE_CLASS, 'ConfigPolicerExcessBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerExcessBurst', 
                [], [], 
                '''                Configured policer excess burst
                ''',
                'config_policer_excess_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-peak-rate', REFERENCE_CLASS, 'ConfigPolicerPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerPeakRate', 
                [], [], 
                '''                Config policer peak rate
                ''',
                'config_policer_peak_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigQueueLimit', 
                [], [], 
                '''                Configured queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction', 
                [], [], 
                '''                Conform action
                ''',
                'conform_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('egress-queue-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Egress Queue ID
                ''',
                'egress_queue_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction', 
                [], [], 
                '''                Exceed action
                ''',
                'exceed_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-excess-bandwidth-weight', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware excess bandwidth weight
                ''',
                'hardware_excess_bandwidth_weight',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware maximum rate in kbps
                ''',
                'hardware_max_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware minimum rate in kbps
                ''',
                'hardware_min_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-average-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer average in kbps
                ''',
                'hardware_policer_average_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-conform-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer conform burst
                ''',
                'hardware_policer_conform_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-excess-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer excess burst
                ''',
                'hardware_policer_excess_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-peak-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer peak rate
                ''',
                'hardware_policer_peak_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Hardware queue limit in bytes
                ''',
                'hardware_queue_limit_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-microseconds', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Hardware queue limit in microseconds
                ''',
                'hardware_queue_limit_microseconds',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('ip-mark', REFERENCE_LIST, 'IpMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.IpMark', 
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
            _MetaInfoClassMember('mpls-mark', REFERENCE_LIST, 'MplsMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.MplsMark', 
                [], [], 
                '''                MPLS mark
                ''',
                'mpls_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('network-min-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Network minimum Bandwith
                ''',
                'network_min_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                PolicerBucketID
                ''',
                'policer_bucket_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-stats-handle', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction', 
                [], [], 
                '''                Violate action
                ''',
                'violate_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_LIST, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred', 
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
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class', 
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
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
                [(-2147483648, 2147483647)], [], 
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
                [(0, 4294967295)], [], 
                '''                Interface Bandwidth (in kbps)
                ''',
                'interface_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
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
                [(0, 65535)], [], 
                '''                Number of Classes
                ''',
                'total_number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-base-address', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                VOQ base address
                ''',
                'voq_base_address',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('voq-stats-handle', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMaxRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMaxRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMinRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMinRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigQueueLimit' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigQueueLimit',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerAverageRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerAverageRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerPeakRate' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerPeakRate',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerConformBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerConformBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerExcessBurst' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerExcessBurst',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction.Mark', 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction.Mark', 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction.Mark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction.Mark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowActionEnum', 
                [], [], 
                '''                Policer action type
                ''',
                'action_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark', REFERENCE_LIST, 'Mark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction.Mark', 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.IpMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.IpMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.CommonMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.CommonMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.MplsMark' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.MplsMark',
            False, 
            [
            _MetaInfoClassMember('mark-type', REFERENCE_ENUM_CLASS, 'DnxQoseaShowMarkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowMarkEnum', 
                [], [], 
                '''                Mark type
                ''',
                'mark_type',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('mark-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue',
            False, 
            [
            _MetaInfoClassMember('range-end', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                End value of a range
                ''',
                'range_end',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('range-start', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue',
            False, 
            [
            _MetaInfoClassMember('dnx-qosea-show-red-match-value', REFERENCE_LIST, 'DnxQoseaShowRedMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue', 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMinThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMinThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMaxThreshold' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMaxThreshold',
            False, 
            [
            _MetaInfoClassMember('policy-unit', REFERENCE_ENUM_CLASS, 'DnxQoseaShowPolicyUnitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'DnxQoseaShowPolicyUnitEnum', 
                [], [], 
                '''                Policy unit
                ''',
                'policy_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policy-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred',
            False, 
            [
            _MetaInfoClassMember('config-max-threshold', REFERENCE_CLASS, 'ConfigMaxThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMaxThreshold', 
                [], [], 
                '''                Configured maximum threshold
                ''',
                'config_max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-threshold', REFERENCE_CLASS, 'ConfigMinThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMinThreshold', 
                [], [], 
                '''                Configured minimum threshold
                ''',
                'config_min_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('first-segment', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                First segment
                ''',
                'first_segment',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware maximum threshold
                ''',
                'hardware_max_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-threshold-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware minimum threshold
                ''',
                'hardware_min_threshold_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('segment-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('wred-match-value', REFERENCE_CLASS, 'WredMatchValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue', 
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
    'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class' : {
        'meta_info' : _MetaInfoClass('PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class',
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
            _MetaInfoClassMember('common-mark', REFERENCE_LIST, 'CommonMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.CommonMark', 
                [], [], 
                '''                Common mark
                ''',
                'common_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-percent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Configured excess bandwidth percentage
                ''',
                'config_excess_bandwidth_percent',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-excess-bandwidth-unit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Configured excess bandwidth unit
                ''',
                'config_excess_bandwidth_unit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-max-rate', REFERENCE_CLASS, 'ConfigMaxRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMaxRate', 
                [], [], 
                '''                Configured maximum rate
                ''',
                'config_max_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-min-rate', REFERENCE_CLASS, 'ConfigMinRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMinRate', 
                [], [], 
                '''                Configured minimum rate
                ''',
                'config_min_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-average-rate', REFERENCE_CLASS, 'ConfigPolicerAverageRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerAverageRate', 
                [], [], 
                '''                Configured policer average rate
                ''',
                'config_policer_average_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-conform-burst', REFERENCE_CLASS, 'ConfigPolicerConformBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerConformBurst', 
                [], [], 
                '''                Configured policer conform burst
                ''',
                'config_policer_conform_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-excess-burst', REFERENCE_CLASS, 'ConfigPolicerExcessBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerExcessBurst', 
                [], [], 
                '''                Configured policer excess burst
                ''',
                'config_policer_excess_burst',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-policer-peak-rate', REFERENCE_CLASS, 'ConfigPolicerPeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerPeakRate', 
                [], [], 
                '''                Config policer peak rate
                ''',
                'config_policer_peak_rate',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('config-queue-limit', REFERENCE_CLASS, 'ConfigQueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigQueueLimit', 
                [], [], 
                '''                Configured queue limit
                ''',
                'config_queue_limit',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction', 
                [], [], 
                '''                Conform action
                ''',
                'conform_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('egress-queue-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Egress Queue ID
                ''',
                'egress_queue_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction', 
                [], [], 
                '''                Exceed action
                ''',
                'exceed_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-excess-bandwidth-weight', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware excess bandwidth weight
                ''',
                'hardware_excess_bandwidth_weight',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-max-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware maximum rate in kbps
                ''',
                'hardware_max_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-min-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware minimum rate in kbps
                ''',
                'hardware_min_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-average-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer average in kbps
                ''',
                'hardware_policer_average_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-conform-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer conform burst
                ''',
                'hardware_policer_conform_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-excess-burst-bytes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer excess burst
                ''',
                'hardware_policer_excess_burst_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-policer-peak-rate-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Hardware policer peak rate
                ''',
                'hardware_policer_peak_rate_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Hardware queue limit in bytes
                ''',
                'hardware_queue_limit_bytes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit-microseconds', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Hardware queue limit in microseconds
                ''',
                'hardware_queue_limit_microseconds',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('ip-mark', REFERENCE_LIST, 'IpMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.IpMark', 
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
            _MetaInfoClassMember('mpls-mark', REFERENCE_LIST, 'MplsMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.MplsMark', 
                [], [], 
                '''                MPLS mark
                ''',
                'mpls_mark',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('network-min-bandwidth-kbps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Network minimum Bandwith
                ''',
                'network_min_bandwidth_kbps',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-bucket-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                PolicerBucketID
                ''',
                'policer_bucket_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('policer-stats-handle', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction', 
                [], [], 
                '''                Violate action
                ''',
                'violate_action',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('wred', REFERENCE_LIST, 'Wred' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred', 
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
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_qos_oper', 'PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class', 
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
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
                [(0, 4294967295)], [], 
                '''                Drop Probability
                ''',
                'drop_probability',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum Threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                Drop Probability
                ''',
                'drop_probability',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum Threshold
                ''',
                'max_threshold',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
                '''                Class ID
                ''',
                'class_id',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('cos-q', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Class of Service Queue
                ''',
                'cos_q',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('hardware-queue-limit', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
                [(0, 4294967295)], [], 
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
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the remote interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ncs5500-qos-oper', True),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Interface Handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('number-of-classes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of Classes
                ''',
                'number_of_classes',
                'Cisco-IOS-XR-ncs5500-qos-oper', False),
            _MetaInfoClassMember('number-of-virtual-output-queues', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
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
            _MetaInfoClassMember('virtual-output-queue-statistics-handle', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
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
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.WredMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred.ConfigMaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMaxRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigMinRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerAverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerPeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConfigPolicerExcessBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ConformAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ExceedAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.ViolateAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.IpMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.CommonMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.MplsMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes.Class']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.PolicyDetails']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface.Classes']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces.MemberInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.WredMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred.ConfigMaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMaxRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigMinRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerAverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerPeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConfigPolicerExcessBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ConformAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ExceedAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.ViolateAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.IpMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.CommonMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.MplsMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes.Class']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.MemberInterfaces']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.PolicyDetails']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface.Classes']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['PlatformQos.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.BundleInterfaces']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction.Mark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue.DnxQoseaShowRedMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.WredMatchValue']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMinThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred.ConfigMaxThreshold']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMaxRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigMinRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigQueueLimit']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerAverageRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerPeakRate']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerConformBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConfigPolicerExcessBurst']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ConformAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ExceedAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.ViolateAction']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.IpMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.CommonMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.MplsMark']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class.Wred']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info']
_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes.Class']['meta_info'].parent =_meta_table['PlatformQos.Nodes.Node.Interfaces.Interface.Classes']['meta_info']
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
